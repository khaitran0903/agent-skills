---
name: its-application-security
description: Review thiết kế, mã nguồn và kiểm thử bảo mật ứng dụng ITS theo phạm vi được giao; dùng cho threat model, IAM/BFF, phân quyền, API/Media, trạng thái phân tán, dependency và xác minh lỗ hổng.
---

# Bảo mật ứng dụng ITS

Giữ owner_role và baseline/check/evidence của task; chỉ đọc [KPI](../../../docs/development/role-kpi.md) khi lập/thay/đánh giá phép đo. Nạp nguồn theo AGENTS, không đọc hồ sơ toàn đội hoặc runner khi task không gọi CLI.

Đọc `AGENTS.md`, mục [security](../../../docs/development/role-profiles.md#security),
[quy trình Security](../../../docs/development/security-review.md), task brief và
requirement/contract/ADR đúng phiên bản. Security mặc định dùng Codex; CLI/model/effort
theo registry và chỉ định của task. Tên vai trò không cấp quyền kiểm thử hệ thống bất kỳ.

## Xác định công việc

Ghi module owner, tài sản, actor, ranh giới tin cậy, branch/SHA và diff chưa commit.
Phân biệt thiết kế, prototype, test double và runtime thật. ADR `Proposed` là đầu vào
review, chưa là baseline triển khai; xung đột hoặc thiếu quyết định chuyển PM.

Chọn đúng playbook, chỉ đọc phần tác động:

| Công việc | Playbook | Đầu ra |
| --- | --- | --- |
| Review thiết kế, PR/diff, tìm lỗi cùng nguyên nhân | [Threat model và review](references/threat-model-and-review.md) | Trust boundary, abuse case, phạm vi ảnh hưởng và finding |
| Login, token/session, quyền và scope | [IAM/BFF và phân quyền](references/iam-bff-and-authorization.md) | Ma trận actor–permission–scope–state và oracle thu hồi truy cập |
| Web/API, file, cache, event và concurrency | [API, Media và trạng thái phân tán](references/api-media-and-distributed-state.md) | Ca kiểm thử âm, race/replay và điều kiện sau từ chối |
| Secret, dependency, workflow và cấu hình | [Dependency và CI](references/dependencies-and-ci.md) | Triage cảnh báo, phạm vi quét và hướng xử lý |
| Xác minh, báo cáo và retest | [Finding và retest](references/finding-and-retest.md) | Finding có evidence, kết luận và lịch sử retest |

## Thực hiện trong ITS

- Review tĩnh có thể làm trên source được giao. Trước kiểm thử chủ động, đối chiếu
  target, môi trường, danh tính test, hành động, giới hạn tải/thời gian và điều kiện
  dừng trong task theo quy trình Security. Quyền đã giao còn hiệu lực; không hỏi lại
  cho từng lệnh trong phạm vi đó. Thiếu phạm vi thì tiếp tục phần review độc lập và
  chuyển PM phần kiểm thử phụ thuộc.
- Theo đường đi dữ liệu tới authorization và thao tác cuối; không suy quyền từ UI,
  tên role, JWT còn hạn hoặc dữ liệu do caller tự khẳng định. Kiểm cả trạng thái sau
  request bị từ chối, side effect, worker, export và đường gọi trực tiếp service.
- Giữ API envelope, module ownership, Media/Notification boundary và chuẩn Identity
  của ITS. Không áp ví dụ framework ngoài để đổi password hashing, HTTP status,
  schema, permission hay cơ chế auth. Lựa chọn cần đổi baseline chuyển PM.
- Dùng skill BE/FE/Platform theo đúng phần review cần thiết; Security không nhận luôn
  quyền sửa implementation. Nếu được giao sửa riêng, kết quả đó cần reviewer và QC
  khác phiên; không tự ký xác minh bản sửa của mình.
- Dùng dữ liệu hư cấu và credential reference do Platform cấp. Không ghi credential,
  token, session identifier, fingerprint, connection string hoặc PII vào evidence.
  Không gửi source/dữ liệu lên dịch vụ scanner ngoài hoặc cài script từ nguồn tham
  khảo khi task chưa giao các hành động đó.
- Finding có đường đi dữ liệu, điều kiện khai thác và bằng chứng cụ thể. Thiếu runtime
  không biến nghi vấn thành lỗi đã khai thác, cũng không biến kiểm tra thành Passed.

## Bàn giao

Trả về Trưởng phòng Dev: phạm vi/bản đã kiểm, threat model và test matrix khi áp dụng,
finding theo mẫu, lệnh/exit code, evidence đã lọc, phần chưa kiểm và yêu cầu quyết định.
Trưởng phòng Dev chỉ đạo owner sửa; Security retest đúng bản; QC kiểm chứng độc lập.
Giữ giới hạn [ba lần chạy tính cả lần đầu](../../../docs/development/agent-orchestration.md#blocker-closure) và tuyến PM.

Nguồn và quyết định tuyển chọn tại [hồ sơ nguồn](../../../docs/development/evidence/security-skill-source-review-2026-10-23.md).
