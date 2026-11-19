# Nguồn gốc bộ skill PBC

Ngày chuyển: **17/11/2026**. Nguồn do chủ dự án chỉ định: thư mục `.agents/skills/` của repository ITS tại máy làm việc. Các thư mục đã được copy trước rồi hiệu chỉnh nội dung cho PBC, không phải bản sao nguyên văn.

Commit nguồn khi ghi nhận: `4480c0b05d2e82e5506dc3f4d2cc0c28553fa239`. Hash từng file nguồn nằm trong [manifest](skill-source-manifest.json); chúng là hash nguồn trước hiệu chỉnh, không phải hash file PBC.

| Skill nguồn | Skill PBC |
| --- | --- |
| `its-delivery-planning` | `pbc-delivery-planning` |
| `its-dotnet-clean-architecture` | `pbc-dotnet-clean-architecture` |
| `its-react-typescript-vite` | `pbc-react-typescript-vite` |
| `its-ui-design-system` | `pbc-ui-design-system` |
| `its-qa-test-design` | `pbc-qa-test-design` |
| `its-qc-independent-verification` | `pbc-qc-independent-verification` |
| `its-application-security` | `pbc-application-security` |
| `its-platform-release` | `pbc-platform-release` |
| `its-user-documentation` | `pbc-user-documentation` |

## Điều chỉnh cho dự án

- Đổi namespace ITS thành PBC, giữ cấu trúc discoverable trong `.agents/skills/` và metadata có sẵn.
- Giữ các nguyên tắc phân lớp, DTO/quyền server, test oracle độc lập, evidence, audit, migration/rollback và tài liệu người dùng.
- Backend nguyên khối .NET/EF Core/PostgreSQL theo quyết định chủ dự án ngày 17/11/2026, thay lựa chọn SQL Server ban đầu; không ép CQRS, Kafka, Redis, BFF hoặc service Media/Notification.
- Chuyển UI sang Ant Design và component PBC; bỏ quy chuẩn component/cột/RFC chỉ được duyệt cho ITS. Phiên bản React/.NET theo quyết định và cấu hình dự án thật.
- Thay tình huống khảo sát bằng TKB, công/dạy thay, kỳ lương, giá hiệu lực, xác nhận/khóa/duyệt, import/export Excel và quyền xem/in phiếu lương.
- Loại liên kết tới tài liệu/registry/CLI/KPI/quy trình đội ITS không tồn tại trong PBC; skill chỉ liên kết tới file có trong repo. Năm reference bảo mật đã được hiệu chỉnh; một số tên file nguồn giữ để truy vết.

Không chuyển `its` (router/điều phối toàn ITS), `its-employment-business-analysis` hoặc `its-survey-data-reporting` vì khác phạm vi. Không copy `.claude` adapter, `.mcp.json`, cấu hình CLI, credential hay code ứng dụng ITS.

## Bổ sung điều phối theo yêu cầu chủ dự án

Ngày 17/11/2026, chủ dự án yêu cầu áp dụng phân vai CLI như ITS và tiền tố `Ruflo:`. Bổ sung `pbc` và `pbc-ruflo`, adapter trỏ về AGENTS, registry cùng launcher riêng cho PBC. Bảng role/model/effort được đối chiếu registry ITS hiện hành và recipe OPS-006; chỉ sao chép chính sách vai trò, không sao chép credential hoặc runtime ứng dụng ITS. Hai skill này được viết cho PBC, không thuộc manifest 9 skill nguồn ở trên.

Ruflo cài trên máy là native 3.71.4. Tích hợp `pbc-ruflo-native-cli` dùng API quản lý task của bản này và gọi executable Codex/agy thật; không dùng extension `its-9router` hoặc tự coi metadata model là thực thi CLI. Registry và tài liệu điều phối trong repo là nguồn cấu hình PBC sau chuyển giao.

Ngày 18/11/2026, chủ dự án yêu cầu bổ sung các nội dung phối hợp đã áp dụng tại ITS: hướng xử lý/chẩn đoán bắt buộc cho mọi finding, ma trận bàn giao, vòng cải tiến có cách đo hiệu quả và bảng kiểm trước giao/khi báo cáo. Quy trình chung đặt tại [điều phối PBC](agent-orchestration.md#finding-resolution), bảng kiểm và cách đóng gói task dùng [recipe hiện có](agent-cli-quickstart.md#task-checklist); các skill và hồ sơ vai trò dẫn chiếu theo chuyên môn. Đây là adaptation cho PBC, không đổi manifest nguồn ngày 17/11 hoặc registry/schema/runtime launcher.

## Phạm vi kiểm chứng

Kiểm YAML/frontmatter và tên bằng `quick_validate.py` của skill-creator; kiểm metadata, liên kết nội bộ, dấu vết phụ thuộc ITS và `git diff --check`. Đây là kiểm cấu trúc/nội dung, chưa phải forward-test hành vi agent hoặc kiểm thử ứng dụng PBC. Repository khởi tạo chưa có mã ứng dụng để build/test.

PGUI-BE001 (17/11/2026): cập nhật skill backend/platform/QC và security references theo PostgreSQL, xmin, UTC và tách migration/runtime grants. Source manifest vẫn ghi hash nguồn ITS lúc nhập, không phải hash artifact PBC đã adaptation. Không đổi registry/launcher/routing.
