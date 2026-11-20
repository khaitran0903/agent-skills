---
name: platform-release
description: Chuẩn bị môi trường, CI, migration, rollout, backup và rollback có artifact/evidence rõ ràng; dùng cho công việc nền tảng hoặc phát hành đã được giao, theo topology của dự án.
---

# Môi trường và phát hành

Đọc task, cấu hình/kiến trúc thật và runbook liên quan. Kiểm kê SDK/package/DB/host/pipeline, quyền/môi trường và phần thiếu. File template hoặc thư mục không chứng minh dịch vụ/pipeline đã chạy.

Giữ cấu hình clone độc lập đường dẫn máy. Secret/key/connection string ngoài source/artifact; tài liệu chỉ ghi tên/reference. Worktree/runtime dùng cơ chế đã được dự án giao, không tự đổi CLI/model hoặc nới quyền khi lỗi đường dẫn.

Khi nhiệm vụ có tích hợp/đồng bộ Git qua nhiều checkout/worktree, đọc [quy trình tích hợp Git](references/git-integration-with-worktrees.md). Giữ quyền và chính sách nhánh đã giao; không coi đồng bộ refs là phát hành sản phẩm.

- Local dùng dữ liệu hư cấu, dịch vụ tối thiểu theo nhu cầu. Tách quyền migration/runtime theo DB; không dùng tài khoản đặc quyền giải quyết mọi lỗi truy cập.
- CI đọc lockfile, chạy checks theo tác động, quyền workflow tối thiểu; artifact gắn commit/digest và giữ cùng bản đã kiểm cho rollout. Template chưa được CI chạy giữ Not Run.
- Migration có version, người/job thực thi và cơ chế tránh chạy đồng thời. Mô tả thứ tự schema/API/producer/consumer/FE khi liên quan, tương thích và điều kiện dừng. Không tự DDL production hoặc auto-migrate lúc API start từ một template.
- Backup nêu dữ liệu/file/config cần khôi phục, thời điểm và mất mát chấp nhận theo task. Restore thử trên môi trường được giao mới chứng minh dùng được; copy thư mục DB đang hoạt động không mặc nhiên là backup hợp lệ.
- Rollout ghi artifact/config, readiness/health và smoke theo vai trò. Chọn tín hiệu dừng theo ảnh hưởng: lỗi, latency, backlog hoặc sai dữ liệu.
- Rollback nêu artifact/config trước có tương thích schema mới không, dữ liệu đã ghi xử lý thế nào, khi nào cần restore/forward-fix. Revert source/down migration không tự khôi phục dữ liệu.

Bàn giao runbook với lệnh thực tế, secret references, deployment order, smoke, rollback/restore, owner và rủi ro. Thực thi theo quyền đã giao; tài liệu kế hoạch không tự cấp quyền deploy hay thay cấu hình tài khoản.

Báo môi trường, candidate/digest, lệnh/exit, evidence đã lọc và kết quả Passed/Failed/Not Run. Blocker có lỗi gốc, bước chẩn đoán/khắc phục, owner và điều kiện readiness; không nhận đã diễn tập chỉ từ runbook.
