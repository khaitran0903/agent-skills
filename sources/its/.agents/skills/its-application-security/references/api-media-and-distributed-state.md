# API, Media và trạng thái phân tán

Chọn ca theo lát cắt được giao; dùng dữ liệu hư cấu trong runtime cô lập.

## Web/API và dữ liệu

- Truy input qua DTO/validation tới query, process, template, outbound HTTP và output.
  Kiểm SQL/command injection, XSS, nhận thừa trường, parser khác biệt và lộ field.
- Với SSRF, review URL do người dùng ảnh hưởng, allowlist, redirect và DNS/IP; kiểm
  cả proxy BFF/Gateway để tránh gọi URL tùy ý. Chỉ thử endpoint đích được task cấp.
- React escape mặc định không chứng minh raw HTML, preview hoặc template an toàn.
  Kiểm CSP/CORS/cookie theo policy đã duyệt, không tự đổi để browser chạy được.
- Pagination/filter/export phải giữ scope và trường được phép. Kiểm lỗi không lộ
  stack trace, secret/PII; response vẫn đúng envelope và HTTP status của ITS.

## File qua Media

Module dùng fileId, không tự mở đường upload/storage khác. Kiểm quyền upload,
finalize, preview, download và delete; chỉ nội dung có trạng thái hợp lệ được dùng.
Kiểm extension/MIME/magic bytes, tên/đường dẫn chuẩn hóa, quota và kích thước tại
ingress/Gateway/Media; signed URL đúng tài nguyên, thao tác và thời hạn theo contract.

Review giới hạn worker preview, nội dung HTML/SVG hoạt động, archive và cách ly.
Thử giới hạn bằng mẫu vô hại; không tạo archive bomb, malware hoặc phá quota thực
ngoài phạm vi kiểm thử đã giao. Phân biệt signed URL còn hạn với cơ chế thu hồi ngay;
không hứa khả năng storage chưa có bằng chứng. Kiểm cache/CDN không công khai file riêng.

## Cache, event và concurrency

- Redis key/cache/result coalescing cần chứa đúng context quyền/phiên theo contract;
  phân tích response cũ ghi đè, stampede, invalidation, TTL và fail-closed.
- Review transaction dữ liệu + Outbox, Inbox/idempotency, retry, offset và replay.
  Kiểm message không tự thành authority để cấp quyền hoặc đọc dữ liệu ngoài namespace.
- Lập lịch xen kẽ request/commit/revoke và trường hợp restart/dependency outage.
  PostgreSQL/Kafka/Redis thật cần thiết khi kết luận tính đúng liên quan các hệ này.
- Theo dõi side effect sau deny/timeout: dữ liệu, Outbox, file và notification.
  Không retry thao tác có kết quả chưa rõ nếu chưa đối soát theo cơ chế idempotency.

Không đọc database service khác để sửa tích hợp; mọi thông báo qua Notification.
Lỗi cần đổi contract/schema/permission chuyển PM trước khi sửa phần phụ thuộc.
