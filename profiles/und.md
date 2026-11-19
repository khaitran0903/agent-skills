# Phần giữ tại UND

Nguồn bổ sung ngày 19/11/2026 là 5 file skill/reference từ workspace UND, không
nằm trong Git repo. [Manifest](../sources/manifest.json) ghi `kind: workspace`,
ngày chụp, SHA-256 và `commit: null`; không suy commit từ các repo BE/FE/Media
nằm bên dưới. Snapshot là dữ liệu truy vết, không phải trạng thái task mới nhất.

| Phần tại UND | Phần dùng chung | Giữ ở profile/contract UND |
| --- | --- | --- |
| `und-form-ergonomics` | Reference form của `react-typescript-vite` | Component/hook dirty guard, ngôn ngữ, chính sách draft theo actor/tenant |
| `und-staging-review-ux` | `staging-review-ux` | API/quyền và trạng thái batch/item, ngữ nghĩa commit |
| `openxml-office-document` | `office-import-export` | Template/version, loại câu hỏi, giới hạn dữ liệu, duplicate thresholds, parser/commit work package |
| `efcore-dapper-hybrid` | Reference của `dotnet-clean-architecture` | EXAM/TEST, CQRS/MediatR, SQL Server grants, SP/view và migration owner theo task |
| `und-qa-qc/references/execution-evidence.md` | Reference runner của `qc-independent-verification` | Docs-as-State, test IDs, quyền DEV, phase, evidence/retry policy hiện hành |

Giữ bộ skill UND và adapter/registry hiện có. Bộ 6 component, tích hợp media,
source/endpoint, auth, luật khảo thí và quyết định STT-01 phải đọc từ tài liệu hiện
hành tại UND; không đưa các ngưỡng/endpoint trong snapshot thành mặc định dùng chung.
Profile này không chạy launcher, đổi CLI/model, giao agent hay cấp quyền DB.

Hai tên `dotnet-clean-architecture` và `react-typescript-vite` đã tồn tại ở UND.
Sync sẽ từ chối nhận thư mục chưa thuộc lock hoặc file bị sửa cục bộ; không tạo
lock giả, xóa thư mục hay ghi đè để vượt bảo vệ. Muốn tiếp nhận, review ba phía
nguồn cũ/bản UND/bản chung theo [quy trình cập nhật](../docs/update-workflow.md),
tách tùy chỉnh vào adapter/reference dự án và ghi nguồn đã nhận đúng thực tế.

Lần đóng góp này chỉ sửa kho `agent-skills`. Chưa cài, đổi registry hoặc kiểm luồng
ứng dụng tại UND. Khi pilot, chọn một task có scope cụ thể rồi ghi expected/actual
và evidence theo quyền đang có; bản profile không chứng minh pilot đã đạt.
