---
name: pbc
description: Tiếp nhận lệnh PBC, phân loại và giao vai trò đúng Codex hoặc agy theo registry của dự án; dùng cho yêu cầu mới, xử lý và tiếp tục công việc PBC.
---

# Đầu mối PBC

Đọc [AGENTS](../../../AGENTS.md), yêu cầu hiện hành và [điều phối](../../../docs/development/agent-orchestration.md). Registry [agent-registry.json](../../../config/agent-registry.json) là nguồn CLI/model/effort.

Với `PBC:`, ghi biên nhận ngắn và giao PM tiếp nhận qua Codex. PM xác định mode/phạm vi/acceptance, Dev Lead phân rã khi cần, host thực thi launcher của đúng vai trò. Không tự chuyển yêu cầu phân tích thành sửa code hoặc chạy cả đội cho việc đơn giản.

Với `Ruflo:`, dùng [skill Ruflo](../pbc-ruflo/SKILL.md). Khi đã chỉ định runtime thì không âm thầm thay bằng xử lý trực tiếp.

Worker đã có ownerRole giữ vai trò/task, không intake lại, không delegate tiếp. CLI/model/effort lấy qua resolver và được truyền bằng cờ thật. Không dùng nhãn vai trò hoặc model trong câu trả lời làm bằng chứng đã chạy đúng CLI.

Chuẩn bị task JSON và workdir theo [recipe](../../../docs/development/agent-cli-quickstart.md). Giữ output, exit và scope; QC độc lập khi tiêu chí yêu cầu. Chưa có môi trường hoặc quyền công cụ phù hợp thì ghi mã lỗi cụ thể, tiếp tục phần không phụ thuộc và giữ các quyết định đã được giao.

Task mới dùng worktree riêng tại `worktree/<task-id>` dưới checkout chính; `run` tự cấp từ inputCommit khi task chưa có workdir. Prompt/artifact nằm trong workdir, không buộc worker đọc task.md bên ngoài checkout. Lỗi đường dẫn không cấp quyền đổi CLI/model/effort; giữ binding và sửa bố trí tệp trước thử lại.

Giao/nhận theo [bảng kiểm](../../../docs/development/agent-cli-quickstart.md#task-checklist) và [ma trận phối hợp](../../../docs/development/agent-orchestration.md#coordination-matrix). Mọi finding phải có hướng xử lý hoặc bước chẩn đoán, owner và điều kiện đóng theo [quy trình chung](../../../docs/development/agent-orchestration.md#finding-resolution); PM/Dev Lead theo dõi hành động và [hiệu quả cải tiến](../../../docs/development/agent-orchestration.md#improvement-loop) trong hồ sơ hiện có.
