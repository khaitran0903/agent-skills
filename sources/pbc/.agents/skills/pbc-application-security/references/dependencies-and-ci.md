# Dependency, secret và CI

Kiểm inventory/scripts/lockfile/config thực tại candidate trước chọn lệnh. Không giả định có workflow `pr.yml`, Gitleaks hay license inventory của ITS. File workflow không chứng minh GitHub đã chạy hoặc ứng dụng không có lỗ hổng.

Ghi tool/version/ruleset, input, thời điểm advisory, exit code và phần chưa quét. Xem dependency trực tiếp/bắc cầu, đường gọi, môi trường runtime/build/test và bản vá tương thích. Giữ advisory ID cùng lý do áp dụng/chưa đủ bằng chứng. Không tự `audit fix --force` hoặc bỏ rule.

Review quyền workflow/token, action pin, code PR không tin cậy, runner/secret boundary. Connection string, signing key và credential ngoài source/artifact; xác minh bằng reference, không đọc/in giá trị. Log/error/audit có correlation phù hợp mà không chứa token, cookie hay dữ liệu lương thật dư thừa.

Scanner chỉ là công cụ hỗ trợ; kiểm hỗ trợ C#/TS, phạm vi, license và outbound trước tích hợp. Không bật cloud upload từ một checklist. License inventory không thay phê duyệt pháp lý.
