---
name: pbc-ruflo
description: Thực hiện lệnh Ruflo trong dự án PBC bằng Ruflo native để theo dõi task và launcher PBC để chạy đúng Codex hoặc agy theo vai trò.
---

# PBC qua Ruflo

Khi người dùng gõ `Ruflo: <công việc>`, chọn runtime `pbc-ruflo-native-cli`. Đọc [AGENTS](../../../AGENTS.md), [điều phối](../../../docs/development/agent-orchestration.md) và [recipe](../../../docs/development/agent-cli-quickstart.md).

Gọi `scripts\ruflo.cmd policy` để đối soát Ruflo thật và capability. Chuẩn bị task JSON ở `.local/tasks/`, exact SHA, role/scope/acceptance và workdir; gọi `scripts\ruflo.cmd run --task <file>`. Launcher gọi API native Ruflo để tạo agent/task rồi chạy Codex/agy với model/effort đã giải. Dùng `scripts\pbc-agent.cmd status --id <id>` để đọc trạng thái và đối chiếu task native.

Worktree mới ở `worktree/<task-id>` dưới checkout chính; có thể bỏ workdir để launcher tự cấp từ SHA. Prompt/runner/report/log nằm trong workdir của worker, dùng đường dẫn prompt tương đối cho agy. Không đổi FE từ agy sang Codex vì task.md ngoài phạm vi; sửa bố trí tệp và thử lại đúng binding, ID mới, giữ runtime native.

Đây là Ruflo native cộng worker CLI của PBC. Không dùng `agent_execute` để thay CLI: API đó là đường gọi LLM khác. Không nhận model GPT/Gemini trong Ruflo metadata là chứng cứ đã gọi Codex/agy. Không dùng extension `its-9router` hoặc policy snapshot ITS cho PBC.

Giữ connection/process và theo dõi đến khi kết thúc hoặc có blocker. `Review`/90% giữ native task `in_progress`, chưa hoàn thành nghiệp vụ. Đối chiếu report, exit, diff/scope, check và QC độc lập trước tiếp nhận. Host ghi evidence đã kiểm chứng rồi gọi `scripts\ruflo.cmd accept --id <id> --evidence <file>` để đồng bộ Done/completed. Không tự gọi `task_complete` hoặc gắn Done từ exit 0.

Task ID mỗi attempt riêng; không chạy trùng ID, không tự resume phiên gần nhất. Thiếu Ruflo/version/CLI/quyền thì báo lỗi cụ thể, không tự cài, tắt policy hoặc fallback runtime. Machine config, queue và log chỉ local; không đưa credential hay dữ liệu lương thật vào prompt/evidence.

Đóng gói phương án/chẩn đoán, owner, mốc kiểm, evidence và điều kiện đóng vào task theo [bảng kiểm giao/nhận](../../../docs/development/agent-cli-quickstart.md#task-checklist) và [xử lý finding](../../../docs/development/agent-orchestration.md#finding-resolution); báo cáo đủ ba nhóm, không chỉ trả HOLD. Theo dõi [cải tiến](../../../docs/development/agent-orchestration.md#improvement-loop) trong task/backlog hiện có, giữ runtime native và gate accept; đủ trường hoặc metadata Ruflo không tự chứng minh lỗi đã đóng.
