# Ý tưởng hoàn thiện

## Nên làm sớm

- Pilot tại một task ITS và một task PBC: chọn planning/UI/QA, so thời gian nhận nâng cấp và số lỗi do tùy chỉnh. Chỉ mở rộng khi có bằng chứng dùng tốt.
- Chốt license phần tự viết và quyền phân phối tài liệu gốc. Giữ attribution riêng cho nguồn bên thứ ba; không gán một license tùy ý cho toàn bộ snapshot.
- Phát hành tag và release note sau review; dự án pin commit/tag. Có thể dùng PR nhắc cập nhật, để dự án kiểm và tiếp nhận.
- Profile thứ ba [UND](../profiles/und.md) đã có từ `0.2.0`, cùng 5 phần đóng góp và fixture hư cấu. Tiếp theo pilot một task có scope tại UND để kiểm cách giữ component/contract riêng và xử lý tên skill trùng; chưa ghi nhận pilot ứng dụng.

## Sau khi có dữ liệu sử dụng

- Bộ tình huống đánh giá hành vi: chọn đúng skill, chỉ đọc reference cần thiết, giữ phạm vi, không tự chọn CLI hay làm sai oracle. Ghi candidate/model/công cụ và giới hạn; không chỉ chấm câu trả lời chứa từ khóa.
- Tách package chuyên ngành khảo sát/báo cáo và công/lương khi có nhiều dự án cần. Mỗi package có dữ liệu hư cấu, metric/invariant và dependency rõ; không tổng quát hóa mọi nghiệp vụ ngay từ đầu.
- Đóng gói điều phối nhiều CLI thành bộ riêng gồm schema/launcher/preflight đã kiểm chứng, không chỉ chép router `SKILL.md`.
- Công cụ xem diff ba chiều và báo dự án nào đang dùng commit cũ. Mọi cập nhật vẫn qua review, giữ phần riêng và không gửi source lên dịch vụ ngoài mặc định.
- Gắn owner, ngày review gần nhất và kết quả pilot cho từng skill; loại quy tắc trùng/lỗi thời thay vì chỉ cộng thêm checklist.

Ưu tiên hiện tại là một nguồn rõ ràng, provenance đủ dùng và quy trình tiếp nhận có thể kiểm lại. Chưa cần package registry, daemon hay đồng bộ nền cho mọi dự án.
