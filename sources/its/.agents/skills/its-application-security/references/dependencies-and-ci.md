# Dependency, secret và CI

Kiểm inventory và script thật tại candidate trước khi chọn lệnh. [Workflow PR](../../../../.github/workflows/pr.yml)
và [runbook workflow](../../../../.github/workflows/README.md) có cấu hình Gitleaks,
NuGet advisory, npm audit và license inventory; file cấu hình không chứng minh GitHub
đã thực chạy hoặc application không có lỗ hổng.

## Triage và phạm vi

Ghi tool/version/ruleset, input lockfile/source/image digest, thời điểm advisory,
exit code và vùng không quét. Xem package trực tiếp/bắc cầu, code path có thể tới,
môi trường runtime/build/test/deploy và bản vá tương thích. Giữ ID advisory và lý do
cảnh báo thật/không áp dụng/chưa đủ bằng chứng; không tự `audit fix --force` hoặc bỏ rule.

License inventory là đầu vào review, không là phê duyệt pháp lý. Thay dependency,
image hoặc quyền workflow phải có owner, task, deployment order/rollback và test tác động.

## Review cấu hình

- Quyền workflow/token tối thiểu, action pin, cách xử lý input PR không tin cậy,
  runner và ranh giới secret; không để mã PR tùy ý chạm môi trường phát hành.
- Credential/signing/Data Protection keys nằm ngoài source/image, quyền truy cập
  và rotation đúng owner. Dùng secret reference, không đọc/in giá trị để chứng minh tồn tại.
- Network/TLS/trusted proxy, DB runtime so với migration principal, Redis/Kafka và
  storage không bị mở rộng truy cập do cấu hình mặc định hoặc thiếu giá trị.
- Log/trace/error/audit giữ đủ correlation để điều tra nhưng không chứa token,
  session identifier, connection string hoặc PII dư thừa.

CodeQL/Semgrep/ZAP chỉ là công cụ ứng viên: trước tích hợp, đánh giá hỗ trợ C#/TS,
phạm vi phân tích, license, outbound/telemetry và cách chạy trong môi trường ITS.
Không cài plugin/script ngoài, bật cloud upload hoặc biến cảnh báo scanner thành lỗi
đã xác minh nếu task chưa đủ đầu vào. Source review có thể tiếp tục khi scanner chưa sẵn.
