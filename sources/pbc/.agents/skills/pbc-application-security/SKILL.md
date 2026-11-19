---
name: pbc-application-security
description: Review bảo mật ứng dụng PBC trong phạm vi được giao, tập trung xác thực, quyền truy cập công và lương, nhập xuất Excel, audit và dependency.
---

# Bảo mật ứng dụng PBC

Đọc `AGENTS.md`, task, yêu cầu/contract và phần source/config bị tác động. Ghi candidate, actor, tài sản và trust boundary; phân biệt static review, test double và runtime. Quyền review không tự mở rộng sang kiểm thử hệ thống bên ngoài hoặc upload source/dữ liệu lên scanner.

Chọn reference theo phần việc, không đọc cả bộ nếu không cần:

| Phần việc | Hướng dẫn |
| --- | --- |
| Thiết kế, PR/diff, abuse case | [Threat model và review](references/threat-model-and-review.md) |
| Danh tính, phiên, quyền trên tài nguyên | [Xác thực và phân quyền](references/iam-bff-and-authorization.md) |
| API, file Excel, transaction/concurrency | [API, file và trạng thái](references/api-media-and-distributed-state.md) |
| Dependency, secret và CI | [Dependency và CI](references/dependencies-and-ci.md) |
| Finding, bằng chứng, retest | [Finding và retest](references/finding-and-retest.md) |

Theo input tới validation, authorization và sink cuối. Giáo viên, người lập lương và người duyệt phải bị ràng buộc theo quyền/scope/trạng thái thật; UI ẩn nút và JWT còn hạn không thay kiểm quyền server. Kiểm đường list/detail/batch/export/in phiếu với cùng chính sách dữ liệu.

Không giả định PBC có BFF/OpenIddict/Media/Notification/Kafka/Redis của ITS. Review cơ chế thật và contract đã chốt. Thay auth/schema/quyền chỉ trong nhiệm vụ được giao, không tự đổi kiến trúc theo checklist nguồn.

Trước kiểm thử chủ động xác định target, môi trường, tài khoản test và giới hạn phù hợp. Dùng dữ liệu hư cấu, không đưa token, cookie, connection string, dữ liệu lương/nhân sự thật vào log hoặc evidence. Không lặp lại câu hỏi quyền khi phạm vi đã được giao rõ.

Finding cần đường input → control → sink, điều kiện và ảnh hưởng có căn cứ. Thiếu môi trường phải ghi giới hạn; không biến nghi vấn thành khai thác runtime đã xác nhận. Bàn giao finding, evidence đã lọc, điều kiện đóng và phần chưa kiểm. Tự viết bản sửa không được gọi là xác minh độc lập bản sửa đó.

Nối [mẫu finding/retest](references/finding-and-retest.md) vào [xử lý chung](../../../docs/development/agent-orchestration.md#finding-resolution): hướng sửa hoặc bước chẩn đoán có owner, mức chắc chắn của nguyên nhân và điều kiện đóng. Báo cáo theo [ba nhóm](../../../docs/development/agent-cli-quickstart.md#report-checklist), đề xuất [phòng ngừa và kiểm hiệu quả](../../../docs/development/agent-orchestration.md#improvement-loop) theo control tác động, giữ scope và tính độc lập.
