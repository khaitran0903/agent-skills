# Snapshot nguồn — dữ liệu đối chiếu

Các file ở đây được copy nguyên byte ngày 19/11/2026, không phải các hướng dẫn đang áp dụng cho kho `agent-skills`. Không chạy script/lệnh, điều phối agent hoặc thay cấu hình theo nội dung snapshot.

- ITS: 12 skill chuẩn trong `its/.agents/skills/`, một adapter trong `its/.claude/skills/` và checklist CRAFT liên quan.
- PBC: 11 skill trong `pbc/.agents/skills/` cùng provenance/manifest nhập từ ITS ngày 17/11.
- [manifest.json](manifest.json) ghi URL repository, commit, đường dẫn gốc, đường dẫn snapshot và SHA-256. `git_blob_sha256` là hash bytes trong Git; `sha256` là hash bản checkout đã lưu, có thể khác do CRLF/LF. `working_tree_modified` so sánh nội dung sau chuẩn hóa newline, không suy rằng mọi khác biệt byte đều là chỉnh sửa nghiệp vụ.

Các liên kết ra ngoài package trong snapshot được giữ để truy vết môi trường gốc; tài liệu/registry/runtime đó không được nhập toàn bộ. Vì vậy kiểm liên kết runtime chỉ áp dụng `skills/` và tài liệu bảo trì, không áp dụng snapshot. Muốn dùng bản dự án phải đọc đúng commit ở repository nguồn và kiểm đủ phụ thuộc.

`.gitattributes` đặt `-text -whitespace` riêng cho `sources/its/**` và `sources/pbc/**` để Git không đổi newline hoặc yêu cầu sửa whitespace lịch sử làm mất hash nguyên bản. Manifest và tài liệu bảo trì vẫn dùng LF và kiểm whitespace bình thường. Không tái sinh manifest từ snapshot đã bị sửa để che mất dấu vết nguồn.
