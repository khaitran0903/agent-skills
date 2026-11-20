# Phần giữ tại ITS

Nguồn snapshot: `80a4f57de21e4bde3cd33fd5d393773703b7eb3e` ngày 19/11/2026. Đây là bản ghi bối cảnh, không là lệnh cập nhật ITS.

- Router `its`, adapter Claude, intake PM, role registry, model/effort, launcher, KPI và worktree thuộc ITS. Giữ tại dự án; không đóng gói chúng vào mọi skill chung.
- Clean Architecture/DDD/CQRS, API envelope, service ownership, BFF/Media/Notification, Outbox/Inbox, cache và event chỉ áp dụng theo ADR/contract ITS.
- Frontend dùng component đã duyệt ở `web/src/shared/components/ui`; quy định GRID/UX, RFC và token do ITS quản lý. Skill UI chung cung cấp phương pháp CRAFT, không thay chuẩn component ITS.
- `its-employment-business-analysis` và `its-survey-data-reporting` cần biểu mẫu/quy trình/định nghĩa chỉ tiêu nguồn. Giữ skill nghiệp vụ tại ITS, snapshot chỉ để truy vết. `requirements-analysis` và quy trình đối soát trong QA chỉ tiếp nhận phương pháp chung; cải tiến nghiệp vụ tiếp tục tại ITS.
- Bản dùng chung không mang version .NET/React hoặc yêu cầu KPI 98% của ITS sang dự án khác.

Khi nhận skill chung: chọn lát cắt thử, giữ adapter `its-*` nếu registry còn trỏ vào chúng, cập nhật dẫn chiếu có chủ ý và kiểm các ca thật trước mở rộng. Chưa có thao tác chuyển đổi nào được chạy ở ITS trong lần tập hợp này.
