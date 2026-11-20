---
name: user-documentation
description: Soạn, cập nhật và kiểm chứng hướng dẫn sử dụng hoặc quy trình theo vai trò, quyền và build ứng dụng; dùng cho tài liệu người dùng, không thay đặc tả nghiệp vụ hay runbook hạ tầng.
---

# Hướng dẫn sử dụng theo phiên bản

Đọc yêu cầu/quy trình đã chốt, ma trận quyền và bản ứng dụng được giao. Ghi nguồn, build/commit, môi trường và vai trò; phần thiếu quyết định có owner, không tự tạo chính sách hoặc sửa nghĩa nghiệp vụ để khớp ứng dụng lỗi.

Chọn đầu ra theo việc người dùng cần làm:

- Hướng dẫn tác vụ: mục tiêu, quyền/scope, điều kiện bắt đầu, dữ liệu cần chuẩn bị, bước với đúng tên menu/nút, kết quả quan sát và lỗi/cách xử lý.
- Quy trình nhiều vai trò: người làm từng bước, đầu vào/đầu ra, chuyển trạng thái, người nhận bàn giao và nhánh trả lại/từ chối/hủy đã chốt. Liên kết tới hướng dẫn thao tác; sơ đồ không thay điều kiện cụ thể.
- Hồ sơ walkthrough: ứng dụng/tài liệu version nào, actor/dataset, bước, expected/actual, verdict và evidence.

Giữ tài liệu ở vị trí/mục lục theo dự án. Không đặt lệnh triển khai, field nội bộ hoặc thông số hạ tầng vào luồng người dùng trừ khi cần cho quyết định của họ.

Ảnh từ bản được ghi nhận, có chú thích và dữ liệu mẫu, không lộ bí mật/PII. Chưa có runtime thì ghi Draft từ đặc tả/prototype và phần chưa xác minh; không dựng ảnh rồi nhận là ảnh thực tế.

Tác giả tự đối chiếu; khi được giao kiểm chứng, làm lại bước trên đúng build/vai trò. Nếu yêu cầu QC độc lập, chuyển candidate/evidence cho người/phiên khác. `Passed` cần quan sát đạt, `Failed` có sai lệch, `Not Run` khi chưa thực hiện; đọc source/ảnh không thay walkthrough. Build đổi luồng/quyền cần kiểm lại phần tác động.

Bàn giao file, nguồn, build, ảnh/evidence, kết quả thực chạy và quyết định còn chờ. Xuất Word/PDF khi được yêu cầu, dùng công cụ/skill định dạng phù hợp và kiểm layout; file Markdown chưa chứng minh bản xuất đẹp hoặc luồng thật đã đúng.

## Tình huống thử

| Trigger/dữ liệu hư cấu | Expected |
| --- | --- |
| Tài liệu mô tả luồng duyệt 3 bước; ứng dụng đã rút còn 2 bước sau bản cập nhật gần nhất | Phát hiện lệch, ghi Draft, gắn build thực tế và chờ xác nhận trước khi cập nhật |
| Ảnh chụp màn hình nút "Gửi yêu cầu" lấy từ bản demo; bản production dùng nhãn "Trình duyệt" | Ghi chú ảnh lấy từ build nào; không dùng ảnh demo làm minh chứng bản chính thức |
| Walkthrough viết từ đặc tả; tác giả chưa chạy thật trên môi trường staging | Đánh dấu từng bước là Draft, ghi rõ nguồn đặc tả và phần chưa xác minh bằng runtime |
| Hướng dẫn không có nhánh lỗi khi người dùng nhập sai mã xác nhận | Bổ sung nhánh lỗi có thông báo hệ thống và hướng xử lý; không để luồng kết thúc không rõ |
| Tài liệu ghi quyền "Quản trị viên" cho bước xuất báo cáo; thực tế vai trò "Kế toán" cũng có quyền đó | Đối chiếu ma trận quyền, ghi đúng vai trò được phép; không tự mở rộng hoặc thu hẹp phạm vi |

Ghi build, vai trò và môi trường đã dùng khi soạn hoặc kiểm chứng từng bước; phần chưa chạy thật trên đúng build/vai trò cần đánh dấu rõ để tránh nhận nhầm là đã xác minh.
