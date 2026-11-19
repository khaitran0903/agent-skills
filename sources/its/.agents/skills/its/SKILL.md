---
name: its
description: PM nhận và phân loại mọi nội dung chủ dự án gửi trong ITS. Worker giữ owner_role đã giao.
---

# Đầu mối ITS

Đọc [AGENTS](../../../AGENTS.md) và task hiện hành. Xử lý yêu cầu mới hoặc tin nhắn
tiếp tục theo [intake](../../../docs/development/its-intake.md). PM ghi biên nhận,
phân loại và chuyển đúng `owner_role`.

Khi lập kế hoạch hoặc giao việc, dùng [vòng điều phối](../../../docs/development/agent-orchestration.md#coordination-loop).
Worker đọc task và phần hồ sơ/skill được giao. Khi tiếp tục, đối soát checkpoint,
candidate và worker còn chạy trước khi cấp lại việc.
