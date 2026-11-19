# Thực thi QC, bug và evidence

Đọc khi chạy kiểm thử, điều tra/retest bug hoặc tổng hợp kết quả. Dùng runner,
state, nơi lưu evidence và quy tắc phân loại của task; chỉ thêm trường thực sự
cần để hiểu kết quả. Không xuất log/trace chưa loại secret vào báo cáo.

## Chuẩn bị một lần chạy

Xác minh đúng source/host/route và target, phiên bản config/fixture, danh tính
kiểm thử theo role/data scope và quyền thực thi đã có. Command phải có cwd,
tham số lọc và tác động dự kiến. Không ghi token, connection string hoặc mật
khẩu vào bảng. Fixture synthetic có marker/cô lập/cleanup theo contract; không
reseed, xóa dữ liệu hoặc khởi chạy worker ngoài scope để chuẩn bị test.

Với live DB/Redis, theo đúng ngoại lệ/giới hạn trong `AGENTS.md`, phase và plan.
Tách transaction rollback của ca synthetic khỏi rollback triển khai: DEVELOPMENT
không mặc định bắt rehearsal rollback/cutover. Quyền còn hiệu lực được tái dùng
trong cùng target/scope; thiếu quyền chỉ chặn phần thực thi phụ thuộc.

## Ghi kết quả và độ mạnh của evidence

| Trường | Nội dung cần ghi |
| --- | --- |
| Liên kết | Task/WP, AC, test/UAT ID và bug nếu có |
| Bản được kiểm | Source commit và dirty diff/hash liên quan; runtime/build/config/schema/fixture khi ảnh hưởng kết luận |
| Môi trường | Host/route/browser/viewport và role/data scope cần phân biệt, không lộ credential |
| Thực thi | Ngày giờ/múi giờ, command/cwd/tool version hoặc các bước manual, native exit nếu là command |
| Kết quả | Assertion/quan sát thực tế so với expected; trạng thái cuối và side effect/readback phù hợp |
| Evidence | Link log/report/ảnh/trace đã loại dữ liệu nhạy cảm; ghi rõ mock, HTTP, browser thật, persistence, load hoặc tái dùng |
| Hạn chế | Ca chưa chạy/bị chặn, nguyên nhân, rủi ro còn lại và phần nào cần kiểm tiếp |

Với kiểm thủ công, ghi thao tác/quan sát và evidence thực; không tạo số test
runner hoặc exit code giả. Với kiểm tự động, exit 0 phải đi cùng assertion và
danh sách ca đã chạy/skip. Mất report, không có ca cần kiểm, timeout hoặc runner
nuốt lỗi không phải bằng chứng Đạt.

Khi kết luận luồng UI đạt, kiểm trạng thái cuối sau transition chịu tác động.
Ví dụ: sau lưu/đóng/mở lại, đối chiếu field/rich content/ID và response/readback
liên quan; media phải decode/playback trên form nếu đó là AC. Chỉ chụp ảnh khi
trạng thái cần kiểm đã ổn định và xem ảnh để nhận xét chữ/bố cục/control. Mask
hẹp phần nhạy cảm để ảnh vẫn chứng minh được vùng chịu tác động.

Security cần request thật tới boundary được tuyên bố: một stub auth luôn cho
qua không chứng minh signature/expiry/revocation/data scope. Race cần thao tác
đồng thời; hai lần submit tuần tự chỉ chứng minh duplicate theo thứ tự đó.

## Khối ghi bug

Đặt bug/finding tại nơi task đang quản lý, giữ ID khi retest; không tự gửi Jira,
email hoặc tin nhắn. Một finding đủ tái hiện gồm:

- Tiêu đề nêu trigger và hành vi sai; task/AC/test liên quan.
- Bản source/môi trường, role/data scope và tiền điều kiện/fixture đã loại secret.
- Các bước và dữ liệu gây lỗi; tần suất hoặc điều kiện tái hiện nếu đã quan sát.
- Expected result kèm nguồn requirement/contract/quyết định; actual result cụ thể.
- Tác động nghiệp vụ và mức độ nghiêm trọng theo thang hiện hữu; priority xử lý
  tách riêng vì còn phụ thuộc phạm vi, thời điểm và quyết định Owner.
- Link evidence, side effect/dữ liệu còn lại nếu có; nguyên nhân đã xác minh
  tách khỏi giả thuyết và câu hỏi còn mở.
- Trạng thái xử lý và liên kết bản sửa/lần retest khi có.

Phân biệt lỗi sản phẩm với fixture/runner/môi trường bằng evidence. Khi test
không tới được hành vi cần kiểm, ghi Bị chặn hoặc Chưa chạy cho hành vi đó và
finding môi trường/runner riêng; không kết luận sản phẩm đúng hoặc sai từ lỗi
setup. Nếu expected còn mâu thuẫn, ghi câu hỏi đặc tả và phần phụ thuộc, không
đổi expected theo actual để đóng bug.

## Retest và regression

Khi được giao sửa, giữ trigger tái hiện và kỳ vọng có nguồn; thay code/selector/
wait theo nguyên nhân đã xác minh trong phạm vi cho phép. Sửa runner phải chứng
minh assertion bắt kết quả sai, report ghi thất bại và process trả exit khác 0
ở ca kiểm có chủ đích. Không thực hiện negative control gây hỏng hệ thống live.

Chạy lại ca gốc trên bản sửa, kiểm trạng thái cuối rồi các ca regression được
chọn theo tác động. Chỉ xác nhận bug đã sửa khi lỗi gốc không còn và kỳ vọng
được kiểm đủ lớp; giữ mở/bị chặn nếu retest chưa chạy. Không dùng việc không
tái hiện một lần để phủ nhận lỗi chập chờn; ghi số lần và điều kiện quan sát.

Áp dụng giới hạn retry tối đa 3 lần tự sửa/chạy lại mỗi failure theo repo khi
được giao sửa. Hết giới hạn hoặc cần quyết định ngoài scope, ghi evidence,
nguyên nhân/phương án vào worklog và dừng phần phụ thuộc; không tăng retry,
skip ca hoặc sửa fixture/assertion/DoD để biến lỗi thành PASS.

## Báo cáo kết quả

Tóm tắt phạm vi và bản đã kiểm, AC/luồng đạt hoặc còn gap, bug chưa giải quyết,
ca chưa chạy/lý do/rủi ro và evidence tương ứng. Nếu dùng số liệu, phân biệt số
ca đã chạy, đạt, lỗi, skip và bị chặn; mẫu số có nguồn, không suy phần trăm phủ
requirement hoặc sản phẩm từ test count. Một ca Đạt không tự có nghĩa AC đã đủ
evidence nếu còn nhánh bắt buộc chưa kiểm.

Evidence tái dùng cần nguồn/ngày/fingerprint và căn cứ còn phù hợp theo policy;
phân biệt rõ với lần chạy mới. Scan secret/dependency/performance ghi kết quả
thật hoặc không áp dụng/chưa chạy kèm lý do, theo tác động và phase. Kết luận
kỹ thuật không tự ký thay QA/Owner sản phẩm hoặc xác nhận phát hành.
