# IAM/BFF và phân quyền

Lấy expected result từ contract/task đã chốt. [ADR 0011](../../../../docs/adr/0011-iam-v1-security-contracts.md)
phải được kiểm trạng thái tại bản review; nội dung Proposed chỉ phục vụ phân tích.
Các ca dưới đây là hướng chọn test, không tự ban hành contract IAM mới.

## Danh tính và phiên

- Review Identity/OpenIddict tại đúng lớp Infrastructure; không dùng auth giả của
  Development làm bằng chứng production. Phân biệt access token, ID token và session.
- Đối chiếu issuer, audience, signature, type, expiry, client/redirect allowlist,
  PKCE/state/nonce và đường đọc trạng thái authoritative khi contract yêu cầu.
- Kiểm browser chỉ giữ cookie theo thiết kế BFF; token/ticket store phía server,
  không lộ qua URL, response, bundle, localStorage, log hoặc trace. Cookie flags
  không thay CSRF token và exact Origin cho mutation theo contract ITS.
- Kiểm refresh rotation/reuse và nhiều replica; logout/disable/revoke/đổi quyền
  tác động đúng phiên, tài khoản và thời hạn được cam kết. Dependency lỗi phải có
  expected riêng; không kết luận cho phép chỉ vì JWT còn signature/expiry hợp lệ.
- Kiểm MFA/xác thực gần thời điểm thao tác, bootstrap và khóa tài khoản theo policy
  được giao; không tự thêm SSO, reset flow, break-glass hoặc admin bypass.

## Permission, tài nguyên và trạng thái

Lập ma trận actor × action × permission × exact scope × resource state × session
state. Dùng ID hư cấu A/B; không ghi giá trị token hoặc session identifier thật.

| Bài kiểm tra | Điều cần chứng minh theo contract |
| --- | --- |
| Có read@A và update@B | Không ghép sai permission của nguồn này với scope của nguồn khác |
| Đổi ID, query filter, body hoặc tuyến trực tiếp | API kiểm đúng tài nguyên/scope; menu và Gateway không là control duy nhất |
| List/count/detail/batch/export/preview | Cùng ranh giới dữ liệu và field-level policy; kiểm side effect của lệnh bị từ chối |
| Nhiều nguồn grant; gỡ một/gỡ nguồn cuối | Tính quyền từ nguồn còn hợp lệ; không cấp hoặc thu hồi rộng hơn contract |
| Tự sửa role/membership hoặc thao tác đồng thời | Không tự nâng quyền; giữ invariant quản trị đã được duyệt |
| Hai phiên A/B cùng user, thu hồi B và giữ A hoạt động | Không dùng trạng thái/cache hợp lệ của A kéo dài quyền B; A theo policy riêng |
| Cache cũ, response đang bay, event trùng/sai thứ tự | Không khôi phục quyền đã thu hồi; đo deadline riêng và live-check theo contract |

API nội bộ phải xác thực caller và dữ liệu subject theo hợp đồng; không tin user ID,
scope hoặc version do caller tự khai. Kiểm endpoint nội bộ không bị lộ qua Gateway.
Đo giới hạn thu hồi bằng thời điểm tương đối đã lọc; không lấy TTL cấu hình thay số đo.
Chưa có runtime phù hợp thì ghi `Not Run`, không dùng prototype làm oracle.
