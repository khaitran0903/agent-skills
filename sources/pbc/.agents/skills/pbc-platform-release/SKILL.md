---
name: pbc-platform-release
description: Chuẩn bị môi trường, CI/CD, migration, backup và phát hành PBC với smoke test và phương án khôi phục phù hợp PostgreSQL và ứng dụng nguyên khối.
---

# Nền tảng và phát hành PBC

Đọc `AGENTS.md`, task, cấu hình và kiến trúc thực tế. Kiểm kê SDK/package/DB/host/pipeline, môi trường và phần còn thiếu. Thư mục hoặc template CI không chứng minh dịch vụ hay pipeline đã chạy.

Giữ cấu hình clone độc lập đường dẫn máy; tham số hóa môi trường. Secret/connection string/key ở ngoài source và artifact, tài liệu chỉ ghi tên/reference. Không copy cấu hình cá nhân, `.mcp.json`, CLI registry hay credential từ ITS.

Worktree task mới nằm trong `worktree/<task-id>` dưới checkout chính PBC; máy hiện tại là `D:\PROJECT\PBC\worktree`. Dùng launcher cấp checkout riêng, đặt task.md/runner/report/log trong workdir và probe đọc/ghi thực tế. Lỗi truy cập phải chẩn đoán/sửa đường dẫn trước thử lại cùng CLI/model/effort; không mở rộng allow-rule hoặc tự override sang CLI khác. Không tự di chuyển checkout đang được worker khác dùng.

Local dùng dữ liệu hư cấu và cấu hình tối thiểu cho PBC. Không dựng Kafka/Redis/BFF/Media/Notification từ template ITS khi PBC chưa cần. PostgreSQL dùng container riêng loopback khi phát triển; tách migration owner và runtime NOSUPERUSER/NOCREATEDB, test admin CREATEDB riêng. Không dùng DB ITS. Xem docs/development/foundation/backend-runbook.md.

CI đọc lockfile, build/test phần đã có, quyền workflow tối thiểu và artifact gắn commit/digest. Dependency/license/secret checks chỉ báo kết quả khi thực chạy. Không thêm ruleset, reviewer, Environment approval hay quyền tài khoản ngoài yêu cầu.

Migration có version trong source, người/chương trình thực thi xác định và cơ chế tránh chạy đồng thời. Chuẩn bị thứ tự schema/API/FE, tương thích và điều kiện dừng. Không tự chạy DDL production hay migration mỗi lần API start chỉ vì thuận tiện.

Backup PostgreSQL bằng pg_dump/pg_restore hoặc physical backup/PITR phù hợp; không sao chép thư mục dữ liệu đang hoạt động làm bằng chứng backup hợp lệ. Kiểm restore trên môi trường thử khi được giao, ghi thời điểm khôi phục và phần mất dữ liệu dự kiến. Bao gồm file/template cấu hình cần để phục hồi ứng dụng.

Rollout ghi artifact, cấu hình, health/readiness và smoke theo vai trò. Rollback chỉ rõ bản trước có tương thích schema mới không và cách xử lý dữ liệu đã ghi; revert source/down migration không mặc nhiên phục hồi dữ liệu.

Bàn giao runbook, lệnh thực tế, secret references, migration order, backup/restore, smoke và rollback. Chưa chạy ghi `Not Run`; tạo runbook không đồng nghĩa được deploy hay đã diễn tập khôi phục thành công.

Khi gặp sai lệch hoặc blocker, ghi hướng xử lý/chẩn đoán, runner/runtime/quyền còn thiếu, owner, phép kiểm readiness và điều kiện đóng theo [quy trình chung](../../../docs/development/agent-orchestration.md#finding-resolution). Báo cáo theo [ba nhóm](../../../docs/development/agent-cli-quickstart.md#report-checklist); đề xuất cải tiến runbook/preflight có [mốc đo hiệu quả](../../../docs/development/agent-orchestration.md#improvement-loop), giữ quyền môi trường đã giao.
