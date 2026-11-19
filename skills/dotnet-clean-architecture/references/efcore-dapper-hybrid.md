# EF Core và Dapper trong cùng hệ thống

Đọc khi dự án đã chọn EF Core + Dapper hoặc đang được giao đánh giá phương án đó.
Lấy provider/package, repository/query abstraction và transaction boundary từ
code/contract hiện hành; không tự dựng CQRS hoặc thay abstraction của dự án.

## Query và mapping

Đặt concrete persistence/SQL ở adapter theo kiến trúc dự án; Application điều
phối use case qua contract hiện có. Phân vai read/write của hai thư viện theo
quyết định dự án, không áp một quy tắc EF-write/Dapper-read cho mọi hệ thống.

- Parameterize giá trị; tên cột/bảng và order động phải qua allowlist vì value
  parameter không thay được identifier.
- Đưa quyền/tenant/data scope vào query; paging có order ổn định và tie-breaker.
  Dùng projection/cột tường minh, giới hạn kích thước và tránh N+1. Chỉ thêm
  no-tracking khi EF đang materialize entity đọc; scalar/DTO thuần không cần nó.
- Kiểm aliases, split boundary, null của left join, parent/child order và duplicate
  parent khi multi-map. Giữ null/decimal/date/version theo contract, không để
  giá trị mặc định của mapper che một quan hệ thiếu.
- Truyền cancellation và timeout qua API thư viện hỗ trợ; dispose connection do
  operation sở hữu, không dispose connection mượn từ DbContext.

## Atomicity, retry và kết quả chưa rõ

Nếu EF và Dapper phải atomic trong một thao tác, dùng đúng cùng connection và
transaction. Truyền transaction vào lệnh Dapper; connection thứ hai cùng connection
string không tham gia transaction thứ nhất. Connection/transaction lấy từ EF phải
còn sống đến khi thao tác kết thúc, không tự đóng object mượn.

Với execution strategy của provider, explicit transaction và phần retry cần được
thiết kế cùng nhau theo API/version thực tế. Retry toàn đơn vị atomic nếu contract
cho phép; xử lý trạng thái tracking sau rollback theo convention dự án. Không
retry riêng nửa Dapper hoặc lặp upload/email trong một callback được chạy lại.
Mất kết nối lúc commit có thể để lại kết quả chưa rõ: đối soát bằng operation ID/
unique constraint/readback trước khi phát lại. Transaction không tự tạo exactly-once.

Unique constraint/concurrency token và luật trạng thái phải chịu được hai request
đồng thời. Plain last-write-wins hoặc SQL MERGE không chứng minh hết race/lock.
SP/view, migration owner và quyền runtime theo DB/task; không sao chép tài khoản
admin từ module khác. Invalidation/cache chỉ theo sự kiện commit được xác nhận.

## Tình huống integration cần quan sát

| Thao tác trong DB thử cô lập | Expected |
| --- | --- |
| EF ghi parent, Dapper ghi/read trong cùng transaction rồi cố ý fail trước commit | Không có ghi đã commit; query dùng đúng transaction thấy trạng thái theo isolation đã chọn |
| Hai request cùng operation ID đồng thời | Số record/side effect theo chính sách idempotency, không suy từ hai lần gọi tuần tự |
| Transient failure ở phần sau của operation | Retry không để lại nửa thao tác hoặc lặp tác động ngoài DB |
| Left join không có child; hai parent trùng sort key ở ranh trang | Null và số parent đúng; paging xác định trên cùng snapshot |

Chạy với provider thật khi khẳng định transaction, grants, isolation hoặc query
plan; InMemory/SQLite không thay evidence SQL Server/PostgreSQL. Nếu chưa có DB
được phép dùng, ghi Not Run thay vì dựng kết quả từ source scan.
