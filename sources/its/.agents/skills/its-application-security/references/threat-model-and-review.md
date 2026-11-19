# Threat model và review thay đổi

Áp dụng cho thiết kế, PR/commit/diff hoặc bắt đầu review một module chưa quen.

## Hiểu hệ thống trước khi kết luận

Đọc ownership/dependency, contract, ADR và implementation tương đương. Vẽ ngắn luồng
Browser → WebHost/BFF → Gateway → resource service; thêm Auth, Media, Notification,
PostgreSQL, Redis và Kafka đúng phạm vi. Ghi ai kiểm danh tính, ai quyết quyền cuối,
ai sở hữu dữ liệu và mỗi giá trị đến từ nguồn nào.

Đánh giá giả mạo danh tính, sửa dữ liệu, phủ nhận hành vi, lộ thông tin, cạn tài nguyên
và nâng quyền trên từng ranh giới có tác động. Mỗi abuse case cần actor/điều kiện,
tài sản, control, nguồn quyết định và test có thể phân biệt đúng/sai. Với Việc làm,
kiểm cả phiếu khảo sát, dữ liệu cá nhân và file xuất theo quyền; BA/Data xác nhận ý
nghĩa nghiệp vụ và tập dữ liệu, Security không tự quyết retention/công thức.

## Review PR/diff

- Định danh base/candidate và thay đổi chưa commit. Đọc cả caller, handler, resolver,
  adapter, worker và cấu hình liên quan; các dòng ngoài diff có thể quyết định an toàn.
- Ưu tiên auth/scope, validation bị gỡ, outbound URL, upload, secret, cache và config.
  Ghi rõ vùng đã đọc và vùng chưa đọc; kích thước PR không chứng minh rủi ro thấp.
- Xem lịch sử khi cần hiểu lý do control cũ; kiểm test còn assertion đúng hành vi,
  không chỉ kiểm tên test hoặc exit code. Mock không chứng minh giao dịch/thu hồi thật.
- Kiểm cấu hình thiếu, null, rỗng, hết hạn, mất dependency và sai môi trường: phải
  từ chối/suy giảm theo contract, không tự mở quyền hoặc dùng default rộng hơn.

## Khi đã có lỗi gốc

Xác minh lỗi tại vị trí đầu tiên rồi tìm biến thể trong các đường có cùng nguyên nhân.
Bắt đầu bằng mẫu khớp vị trí đã biết; mở rộng dần và đọc từng candidate. Kiểm upstream
validation, quyền, state và cách gọi trước khi kết luận. Phạm vi vượt task thì ghi đề
nghị qua PM thay vì tự sửa module khác.

Đầu ra gồm threat model/abuse case, phạm vi ảnh hưởng, control/test thiếu và finding
theo [mẫu](finding-and-retest.md). Tài liệu OWASP dùng để đối chiếu theo phiên bản đã
ghi trong task, không tự nâng thành tiêu chí nghiệm thu mới hoặc tuyên bố chứng nhận.
