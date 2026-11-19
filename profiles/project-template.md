# Profile dự án sử dụng skill

Giữ tài liệu này trong dự án sử dụng và dẫn chiếu từ AGENTS/adapter, không sửa bản dùng chung chỉ để gắn đường dẫn dự án.

| Nội dung cần chốt | Nguồn tại dự án |
| --- | --- |
| Mục tiêu, nghiệp vụ và thuật ngữ | Requirement/contract đã duyệt |
| Kiến trúc, ownership và dependency | ADR/kiến trúc hiện hành |
| SDK, DB, package, lệnh kiểm chứng | Cấu hình thực tế, lockfile và CI |
| UI, thương hiệu, component và nội dung | Design system/theme/component thực tế |
| Phân vai, CLI/model/effort và launcher | Registry/task hiện hành nếu có |
| Quyền thực thi, môi trường, giới hạn | Chỉ định trong phiên/task và cấu hình môi trường |
| Evidence và quy trình bàn giao | Mẫu task, finding, QC của dự án |
| Skill chung đã nhận | `.agents/agent-skills.lock.json` |
| Chỉnh sửa riêng | File/đoạn điều chỉnh, lý do, owner, ngày và commit nguồn |

Profile không tự cấp quyền cho agent hay thay ưu tiên chỉ dẫn của người dùng. Nếu chưa có chính sách ở dự án, làm trong phạm vi yêu cầu hiện hành và ghi quyết định còn thiếu, không dựng một quy trình toàn đội từ mẫu này.
