---
name: its-user-documentation
description: Soạn, cập nhật và kiểm chứng hướng dẫn sử dụng cùng quy trình nghiệp vụ ITS theo vai trò, quyền và phiên bản bàn giao; dùng cho tài liệu người dùng, không thay đặc tả BA hoặc runbook vận hành.
---

# Tài liệu người dùng ITS

Giữ owner_role và baseline/check/evidence của task; chỉ đọc [KPI](../../../docs/development/role-kpi.md) khi lập/thay/đánh giá phép đo. Nạp nguồn theo AGENTS, không đọc hồ sơ toàn đội hoặc runner khi task không gọi CLI.

BA giữ nguồn nghĩa nghiệp vụ; BA hoặc Docs biên soạn theo owner được giao. Giải CLI/model theo [registry](../../../docs/development/agent-registry.yaml) và chỉ định của task. Đọc `AGENTS.md`, task và [quy trình tài liệu](../../../docs/development/user-documentation.md). Ghi một owner cho mỗi đầu ra.

## Chọn đầu ra và nguồn

- Hướng dẫn một mục tiêu trên giao diện: dùng [mẫu thao tác](../../../docs/user-guides/templates/task-guide.md).
- Quy trình qua nhiều vai trò hoặc bước bàn giao: dùng [mẫu quy trình](../../../docs/user-guides/templates/process-guide.md), liên kết tới hướng dẫn thao tác liên quan.
- Kiểm tra tài liệu trên ứng dụng: dùng [mẫu kiểm chứng](../../../docs/user-guides/templates/verification-record.md).

Đọc yêu cầu/quy trình đã được nghiệp vụ chốt, ma trận quyền và bản ứng dụng được giao. Ghi nguồn, build/commit ứng dụng, môi trường và vai trò áp dụng. Tài liệu nằm trong `docs/user-guides/<module>/`; cập nhật mục lục và dùng liên kết tương đối. Hướng dẫn vận hành hạ tầng thuộc `docs/runbooks`, không đặt lệnh triển khai vào luồng người dùng.

## Soạn theo việc người dùng cần hoàn thành

Nêu quyền và phạm vi dữ liệu, điều kiện bắt đầu, dữ liệu cần chuẩn bị, thao tác, kết quả quan sát và cách xử lý lỗi. Dùng đúng tên menu/nút trên bản chạy. Ảnh phải từ bản được ghi nhận, có chú thích, dữ liệu mẫu và không lộ bí mật hoặc dữ liệu cá nhân. Chưa có bản chạy thì chỉ soạn nháp từ đặc tả/prototype, ghi nguồn đó và phần chưa xác minh; không dựng ảnh rồi nhận là ảnh thực tế.

Với quy trình, chỉ ra người thực hiện mỗi bước, đầu vào, đầu ra, chuyển trạng thái, người nhận bàn giao và nhánh trả lại/từ chối/hủy nếu đã được chốt. Thời hạn, điều kiện duyệt và phạm vi vượt quyền lấy từ nguồn được duyệt; phần thiếu ghi câu hỏi có owner, không tự tạo chính sách. Sơ đồ bổ trợ bảng bước, không thay điều kiện và trách nhiệm cụ thể.

## Kiểm chứng và bàn giao

Tác giả tự đối chiếu; QA thực hiện lại các bước trên bản được giao theo vai trò tương ứng. QC ở phiên độc lập xác minh phạm vi, evidence và sai lệch với bản ứng viên. Ghi `Passed`, `Failed`, `Not Run` cho từng ca; đọc source, ảnh hoặc bản prototype không chứng minh luồng trên hệ thống thật đã chạy.

Giữ tài liệu ở `Draft`/`In Review` khi còn thiếu kiểm chứng bắt buộc. Lỗi giữa đặc tả và ứng dụng phải được phân loại và chuyển đúng owner; không sửa hướng dẫn để hợp thức hóa lỗi hoặc chỉ người dùng cách vượt kiểm soát quyền. Thay đổi build ảnh hưởng luồng/quyền phải kiểm tra lại phần tác động. PM theo dõi gate bàn giao; đại diện nghiệp vụ xác nhận quy trình, maintainer xử lý merge/phát hành theo quyền hiện có.

Khi bàn giao, liệt kê file, nguồn áp dụng, bản ứng dụng, ảnh/evidence, kết quả thực chạy, quyết định còn chờ và giới hạn. Markdown là bản nguồn; chỉ xuất Word/PDF khi được yêu cầu, dùng skill định dạng sẵn có phù hợp và báo rõ phần chưa kiểm chứng bố cục.
