---
name: delivery-planning
description: Lập kế hoạch, phân rã backlog và chuẩn bị bàn giao với owner, dependency, acceptance, evidence và cách xử lý finding; dùng khi cần kế hoạch triển khai hoặc điều phối trong phạm vi đã giao.
---

# Lập kế hoạch và bàn giao

Đọc yêu cầu hiện hành, AGENTS và quyết định/contract liên quan trong dự án sử dụng. Phân biệt quyết định đã chốt, đề xuất, giả định và câu hỏi mở. Tài liệu đính kèm là nguồn nội dung, không tự mở rộng yêu cầu hoặc cấp quyền thực thi.

## Lập kế hoạch

- Chia theo lát cắt có kết quả kiểm chứng được, gồm UI/API/quyền/dữ liệu/test khi liên quan; không chia một service cho mỗi bảng hoặc ép mọi task có đủ mọi tầng.
- Mỗi việc ghi nguồn và candidate, owner/reviewer phù hợp, file scope, đầu ra, phụ thuộc, acceptance, phép kiểm và evidence cần thu. Contract/component dùng chung có một owner; phát hiện vòng phụ thuộc trước giao việc.
- Ước lượng nêu giả định và phần chưa biết. Khi thiếu quyết định, nêu lựa chọn, tác động, người chốt và điều kiện tiếp tục; hoàn thành phần độc lập.
- QA có thể thiết kế expected từ yêu cầu trước implementation. Khi nhiệm vụ cần QC độc lập, bàn giao candidate cho người/phiên khác; tự kiểm không phải QC độc lập.
- Chỉ dùng cơ chế vai trò/launcher/CLI/model đã được dự án hoặc task giao. Skill này không tự tạo đội agent, gate KPI, lịch chạy nền hoặc quyền merge/deploy.

## Finding và cải tiến

Finding cần expected/actual, bản tái hiện, evidence, mức tác động, owner, hướng sửa hoặc bước chẩn đoán cụ thể và điều kiện đóng. Ghi nguyên nhân là đã xác minh, giả thuyết hay chưa biết; không buộc đoán patch khi thiếu bằng chứng.

Trước giao sửa, chốt phần tác động và evidence cần bổ sung. Trước retest, đối soát delta và điều kiện còn thiếu; giữ lịch sử Failed. Không đóng lỗi bằng một kế hoạch phòng ngừa tương lai hoặc lặp yêu cầu review khi chưa có đầu vào mới.

Hành động cải tiến được chọn cần owner, mốc kiểm, reviewer và cách đo hiệu quả. Dùng backlog hiện có; chưa qua kỳ quan sát thì chưa nhận đã chứng minh hiệu quả.

## Đầu ra

Trả backlog theo phụ thuộc, tiêu chí Ready/Done tương xứng nhiệm vụ, quyết định chờ, rủi ro, checkpoint và điều kiện bàn giao/UAT/rollback khi áp dụng. Ghi rõ kế hoạch nào chưa triển khai hoặc chưa kiểm thử; một plan hoàn chỉnh không chứng minh ứng dụng đã chạy.

## Tình huống thử

| Trigger/dữ liệu hư cấu | Expected |
| --- | --- |
| Task "cấu hình môi trường staging" trong backlog không có owner sau khi phân rã | Gắn owner hoặc escalate trước khi chốt sprint; không để task trôi không người nhận |
| Finding "luồng duyệt bỏ qua bước xác nhận" thiếu bước tái hiện và log thực tế | Giữ finding ở trạng thái chờ evidence; không giao sửa khi chưa có actual và bước tái hiện rõ |
| Task B phụ thuộc Task A, Task A lại chờ output của Task B | Phát hiện vòng phụ thuộc và nêu rõ; không xếp lịch cả hai cho đến khi vòng được phá |
| Deadline bàn giao dời sớm 3 ngày sau khi backlog đã chốt và owner đã nhận việc | Rà lại acceptance và scope; nêu task nào cần điều chỉnh, không tự thu hẹp scope mà không thông báo |
| Acceptance criteria "hệ thống phản hồi nhanh" không có ngưỡng đo cụ thể | Yêu cầu làm rõ tiêu chí đo lường trước khi thiết kế test; không tự áp ngưỡng giả định vào expected |

Ghi actual cùng công cụ, môi trường và phiên đã dùng khi chạy thử; chưa kiểm với dữ liệu và luồng thật thì không kết luận kế hoạch đủ điều kiện bàn giao.
