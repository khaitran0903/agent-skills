---
name: its-platform-release
description: Chuẩn bị hoặc kiểm tra môi trường, CI/CD, migration và kế hoạch phát hành ITS có health, quan sát và rollback; thực thi chỉ trong môi trường và hành động đã được giao.
---

# Nền tảng và phát hành ITS

Giữ owner_role và baseline/check/evidence của task; chỉ đọc [KPI](../../../docs/development/role-kpi.md) khi lập/thay/đánh giá phép đo. Nạp nguồn theo AGENTS, không đọc hồ sơ toàn đội hoặc runner khi task không gọi CLI.

Đọc `AGENTS.md`, kiến trúc/ADR, manifest/contract bị tác động và cấu hình thật. Phân biệt nhiệm vụ kiểm kê, chuẩn bị cấu hình/kế hoạch với triển khai thực tế. Tạo runbook không tự cấp quyền chạy migration, publish package, thay secret hoặc deploy lên môi trường khác.

## Kiểm kê trước khi thay đổi

Xác định service sở hữu, môi trường, topology, version image/SDK/package thực tế, pipeline và các điều kiện thiếu. Không nhận Auth/BFF/Media/Notification là sẵn sàng chỉ vì tồn tại thư mục hoặc UI fixture. Liệt kê phụ thuộc nào cần cho lát cắt và người xử lý; dùng evidence health/contract/smoke để xác nhận.

Các đường dẫn cấu hình/script tương đối repository root; tham số hóa domain, storage và provider theo môi trường. Không đưa đường dẫn clone của một máy vào cấu hình chung. Biến môi trường thật/secret nằm ngoài Git; tài liệu chỉ nêu tên và nơi cấp, không ghi giá trị.

## Chuẩn bị nền tảng và pipeline

- Local dùng Compose profile/dependency hiện có và seed hư cấu; kiểm tra bootstrap chạy lặp lại được, liveness/readiness phản ánh đúng dependency và không mất dữ liệu khi restart theo cấu hình được cam kết.
- Auth/BFF theo kiến trúc: token ở server, cookie/CSRF cho web, allowlist tuyến proxy, kiểm tra permission/scope ở API. Không thêm auth bypass để môi trường dễ khởi động.
- File qua Media, thông báo qua Notification; Outbox/Inbox và cache theo ownership. Không lấy shared database login đặc quyền để giải quyết tích hợp hoặc báo cáo.
- Pipeline đọc lockfile, build/test phù hợp, checks dependency/license/secret đã cấu hình, artifact định danh được và quyền workflow tối thiểu. Bản publish/deploy dùng artifact/digest đã kiểm tra; không dùng tag trôi làm bằng chứng bản phát hành.
- GitHub ruleset/Environment và secret references cần xác minh trạng thái thực. Chuẩn bị file/checklist trong phạm vi; cấu hình quản trị hoặc deploy chỉ khi việc đó đã được giao. Không tự thêm approval mới nếu quyền trong phiên đã đủ cho hành động.

Backend/hạ tầng và QC mặc định dùng Codex CLI theo [bàn giao CLI](../../../docs/development/agent-cli-handoff.md) và [registry](../../../docs/development/agent-registry.yaml); chọn CLI khác khi chủ dự án/task chỉ định. Phiên QC độc lập với implementation và QA, model/effort lấy đúng override vai trò. Không coi đặc quyền của một CLI là quyền ngoài task.

## Kế hoạch migration và rollout

Mô tả thứ tự triển khai schema/producer/consumer/API/FE và khoảng tương thích; dùng mở rộng–chuyển đổi–thu gọn khi cần tránh phá bản đang chạy. Migration chạy bằng job/pipeline có lock và danh tính phù hợp, không chạy DDL khi API tự khởi động. Chỉ thực thi trên môi trường đã được giao và đáp ứng điều kiện của môi trường đó.

Nêu backup/restore cần thiết, kiểm tra trước migration, smoke/readiness sau rollout và tín hiệu dừng dựa trên tác động: lỗi, latency, backlog, job thất bại hoặc số liệu sai. Job/export cần lưu bền vững, chống xử lý trùng, có quyền và kết quả đi qua Media.

Rollback phải chỉ ra bản artifact/cấu hình trước, tương thích với schema mới và xử lý dữ liệu đã ghi. Không mặc định down migration hoặc revert source sẽ khôi phục dữ liệu; nếu phải restore/forward-fix, ghi mất mát dự kiến, điều kiện và người quyết định. Không diễn tập restore vào dữ liệu thật ngoài phạm vi được giao.

## Bàn giao và kiểm chứng

Bàn giao thay đổi cấu hình, danh sách secret references, lệnh local/staging thực sự có trong repo, deployment order, smoke/rollback runbook, owner vận hành và rủi ro. Lệnh chưa chạy ghi Not Run; template CI chưa được GitHub chạy không được báo pipeline xanh. Khi có thực thi, ghi môi trường, artifact/commit, thời điểm, exit code và health/smoke evidence đã lọc bí mật.
