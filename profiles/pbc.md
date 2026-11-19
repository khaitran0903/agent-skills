# Phần giữ tại PBC

Nguồn snapshot: `7d0077eb47c289e81853eb3f2bc7cd6b96bbeddf` ngày 19/11/2026. PBC đã nhận 9 skill từ ITS commit `4480c0b05d2e82e5506dc3f4d2cc0c28553fa239` ngày 17/11; hồ sơ gốc được giữ trong `sources/pbc/docs/development/`.

- TKB, công thực dạy/dạy thay, kỳ lương, ngày hiệu lực, giá/làm tròn, khóa/xác nhận/duyệt, audit và dữ liệu sau duyệt thuộc contract PBC. Không biến các ví dụ này thành quy tắc mặc định của skill chung.
- Kiến trúc nguyên khối phân lớp, PostgreSQL, concurrency `xmin`, ngày nghiệp vụ và migration/runtime grants theo quyết định PBC. Không kế thừa hạ tầng ITS từ kho chung.
- Ant Design, wrapper PBC, `pbcTheme`, logo, slogan và nhận diện trường giữ tại dự án. 15 tiêu chí CRAFT chỉ bổ sung cách quan sát và evidence, không thay token thương hiệu.
- `pbc`/`pbc-ruflo`, native runtime, registry CLI/model/effort và launcher cần môi trường thật. Snapshot không bao gồm bộ launcher và không thể cài router bằng công cụ sync chung.
- Giữ provenance cũ ngày 17/11; lock mới của `agent-skills` là một lớp nguồn tiếp nhận khác, không ghi đè manifest lịch sử.

Khi nhận skill chung: ưu tiên pilot planning/UI/QA trong task riêng, giữ bất biến nghiệp vụ và skill adapter đang được registry sử dụng. Chưa có thao tác chuyển đổi nào được chạy ở PBC trong lần tập hợp này.
