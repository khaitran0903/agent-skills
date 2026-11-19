---
name: pbc-ui-design-system
description: Thiết kế và review giao diện PBC nhất quán trên Ant Design, chú trọng bảng công, bảng lương, form và accessibility.
---

# Giao diện PBC

Đọc `AGENTS.md`, yêu cầu màn hình, actor/quyền và component thực tế trước thiết kế. Dữ liệu prototype dùng tên/mã hư cấu. Phân biệt đề xuất hình thức, hành vi đã chốt và tích hợp đã kiểm chứng.

Tái sử dụng Ant Design và wrapper/pattern PBC đã có, giữ token, khoảng cách, nhãn và vị trí chức năng nhất quán. Không áp quy tắc cột cố định, kích thước search 280px, RFC hoặc thư viện UI nội bộ ITS sang PBC. Bảng ma trận TKB/công có semantics riêng; chọn cấu trúc phù hợp với yêu cầu thay vì ép thành bảng danh mục.

Với danh sách, nêu phạm vi tìm kiếm, filter/paging/sort/selection và xuất. Khi đổi filter xử lý page/selection rõ ràng. Bảng tiền căn theo ý nghĩa và có đơn vị; tổng theo kỳ/scope phải rõ. Người xem nhận biết công dự kiến, công đã sửa, đang xác nhận, đã khóa và lương đã duyệt theo trạng thái thật.

Form giữ bản nháp độc lập với dữ liệu đã lưu. Hủy chỉ bỏ thay đổi của form đó; không reset fixture hoặc bản nháp luồng khác. Label gắn control, lỗi chỉ đúng vị trí; placeholder không thay label. Pending và response trễ không gây ghi lặp hoặc lưu sau khi đã hủy.

Thiết kế loading, empty, no-results, error/retry, forbidden, hết phiên, validation và nội dung dài. Thao tác khóa/mở lại/duyệt cần nội dung xác nhận cụ thể về đối tượng và hậu quả. Không đưa chi tiết triển khai vào luồng của giáo viên/kế toán.

Kiểm keyboard, focus, tên truy cập, tương phản, menu/dialog Escape và trả focus. Kiểm desktop và mobile bằng dữ liệu đại diện; bảng có thể cuộn trong vùng chứa mà không làm cả trang tràn ngang. Ảnh chụp không chứng minh keyboard/interaction đạt.

## Nhận diện thương hiệu & Bảng màu quy chuẩn PBC

Tuân thủ nghiêm ngặt nhận diện thương hiệu Trường THCS - THPT Phan Bội Châu (TP.HCM):

- **Đơn vị:** Trường THCS - THPT Phan Bội Châu (TP.HCM).
- **Khẩu hiệu chính thức (Slogan):** *"Kỷ cương – Sáng tạo – Đột phá – Phát triển"*. Sử dụng trên màn hình đăng nhập, banner tổng quan, footer và tài liệu hướng dẫn.
- **Biểu trưng (Icon & Brand Mark):** Chiếc khiên phong cách Heraldic (kỷ luật, vững bền), quyển sách mở (tri thức khai phóng) và hai nhánh vòng nguyệt quế đối xứng (vinh quang học tập). Monogram đại diện: **PBC**.

### Bảng màu chuẩn & Ant Design Theme Token (`pbcTheme`)

Mọi màn hình và component xây dựng mới hoặc hiệu chỉnh bổ sung phải tuân thủ đúng token chuẩn đã chốt tại `web/src/app/theme.ts`:

- **Primary Color (Chủ đạo):** `#1B3693` (Deep Educational Navy - uy tín học thuật, công nghệ giáo dục). Hover: `#2A4CB8`, Active: `#12266D`.
- **Secondary / Accent Color:** 
  - `#C9031F` (Crimson Red - màu truyền thống nhà trường, dùng cho điểm nhấn nhận diện, vạch chỉ báo active navigation bar, tag trạng thái quan trọng, lỗi).
  - `#00A8E8` (Cerulean / Cyan - đại diện cho chuyển đổi số và công nghệ).
- **Trạng thái:** Success: `#52C41A`, Warning: `#FAAD14`, Error: `#C9031F`, Info: `#00A8E8`.
- **Nền & Viền:** Nền layout `#F4F6F9`, Nền container/card `#FFFFFF`, Viền `#E2E8F0`, Viền phụ `#F1F5F9`.
- **Chữ (Text):** Text chính `#172554`, Text phụ `#475569` / `#64748B`.
- **Typography:** `fontFamily: '"Roboto", "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Arial, sans-serif'`.
- **Bo góc (Border Radius):** Base 8px, Card 10px, Button 6px, Tag 4px.

### Quy chuẩn bố cục & Header/Sidebar

- **Topbar:** Nền trắng `#FFFFFF`, viền đáy `1px solid #E2E8F0`, hiển thị định danh cổng trường, avatar và thông tin người dùng.
- **Sidebar:** Nền Deep Navy `#0A192F`, chữ `#CBD5E1`. Mục menu đang chọn (`aria-current`) có nền `#ffffff1f`, chữ trắng và vạch chỉ báo đỏ đô ở mép trái (`box-shadow: inset 3px 0 #C9031F`). Chân sidebar có slogan *"Kỷ cương · Sáng tạo · Đột phá"*.
- **Login / Hero Banner:** Sử dụng gradient chuyển từ Navy tối (`#0A192F`) sang Cyan (`#00A8E8`) và Royal Navy (`#1B3693`), vạch ngăn cách màu đỏ `#C9031F`, typography rõ nét, trang trọng.

Bàn giao màn hình/component, trạng thái, dữ liệu mẫu, phần phụ thuộc API/quyền, ảnh desktop/mobile khi đã kiểm và giới hạn. Prototype không được mô tả là production hoặc tích hợp hoàn tất.

Finding UI/interaction nêu hướng điều chỉnh hoặc phép kiểm tiếp, owner và điều kiện đóng theo [quy trình chung](../../../docs/development/agent-orchestration.md#finding-resolution). Báo cáo theo [ba nhóm](../../../docs/development/agent-cli-quickstart.md#report-checklist); đề xuất cải tiến pattern/accessibility có cách kiểm hiệu quả trong scope.
