---
name: ui-design-system
description: Thiết kế, tinh chỉnh hoặc review UI bằng component/token của dự án và 15 tiêu chí CRAFT, giữ semantics, accessibility, responsive và hành vi; dùng cho prototype hoặc giao diện triển khai.
---

# Thiết kế và review giao diện

Đọc yêu cầu, actor/quyền, design system, content guide và component/export thực tế. Phân biệt giá trị đã duyệt, đề xuất và giá trị chỉ đang tồn tại trong source. Prototype dùng dữ liệu hư cấu; duyệt hình thức và xác minh tích hợp là các kết quả riêng.

Khi audit/tinh chỉnh/review, đọc [15 tiêu chí CRAFT](references/ui-craft-checklist.md). Chọn tiêu chí theo tác động, ghi finding trước sửa và kiểm lại trong cùng điều kiện. Không mở phạm vi làm lại màn đã tốt khi chỉ có finding hẹp.

- Dùng shell, token và component chung phù hợp. Nếu thiếu pattern, ghi khoảng trống và giải quyết theo quy trình dự án; không tự áp quy định RFC hoặc đường dẫn component của một dự án khác.
- Bảng danh mục, ma trận, cây và row detail có semantics khác nhau. Thứ tự cột, toolbar, scope selection/export theo yêu cầu; không ép mặc định thư viện thành quy tắc nghiệp vụ.
- Form giữ draft độc lập. Hủy chỉ bỏ thay đổi form đó; pending/response trễ không tạo ghi lặp hoặc lưu sau hủy.
- Mô tả loading/empty/no-results/error/retry, quyền/phiên, validation và dữ liệu dài theo phạm vi. Xác nhận thao tác nêu đối tượng và hậu quả thật.
- Nội dung dùng ngôn ngữ người dùng và giữ thuật ngữ hợp lệ. Không xóa dữ liệu người dùng, tên pháp lý hoặc màu semantic/gradient thương hiệu để đạt một xu hướng thẩm mỹ.
- Quan sát keyboard/focus, tên truy cập, dialog trap/Escape/return focus khi áp dụng; đo tương phản thực tế. Kiểm responsive/zoom/dữ liệu khó, tránh tràn toàn trang.

Với mã từ công cụ sinh UI, kiểm router, wrapper framework, reset CSS và dependency trước port vào ứng dụng; giữ công nghệ đích đã chọn. Không đưa dữ liệu thật/secret vào prompt hoặc nhận prototype là production.

Bàn giao màn/component, quyết định nguồn, finding/delta, tiêu chí áp dụng, expected/actual/evidence, candidate, browser/viewport và phần Not Run. Khi có code, chạy checks theo tác động. Ảnh chụp không chứng minh bàn phím, số liệu hoặc tích hợp đạt.
