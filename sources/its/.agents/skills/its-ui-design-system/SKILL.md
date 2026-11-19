---
name: its-ui-design-system
description: Thiết kế hoặc review layout, component và tương tác giao diện ITS để các module dùng chung shell, form, lưới và trạng thái accessibility; hỗ trợ prototype v0 và bàn giao React/Vite.
---

# Thiết kế giao diện đồng nhất ITS

Giữ owner_role và baseline/check/evidence của task; chỉ đọc [KPI](../../../docs/development/role-kpi.md) khi lập/thay/đánh giá phép đo. Nạp nguồn theo AGENTS, không đọc hồ sơ toàn đội hoặc runner khi task không gọi CLI.

Đọc `AGENTS.md`, requirement/contract của màn hình và [chuẩn giao diện ITS](../../../docs/architecture/Frontend_Design_System.md). Chuẩn chứa cả quy tắc tổ chức và giá trị thiết kế còn chờ duyệt; xác minh trạng thái thay vì nhận mọi màu/kích thước là đã duyệt. Chỉ đạo mới của chủ dự án áp dụng cho phạm vi được giao.

## Chọn phạm vi

Với thiết kế/prototype, dùng dữ liệu hư cấu, ghi các trường/hành vi mới là đề xuất; không sửa schema hoặc API để khớp hình mẫu. Với implementation, đọc skill FE tại `.agents/skills/its-react-typescript-vite/SKILL.md` cùng API/permission được duyệt; FE mặc định dùng agy, chỉ định CLI của chủ dự án/task được ưu tiên theo [bàn giao CLI](../../../docs/development/agent-cli-handoff.md). Duyệt hình thức và kiểm chứng tích hợp là hai kết quả riêng.

## Bố cục và component

Khi thiết kế, tinh chỉnh hoặc review UI, dùng [checklist chất lượng hình thức và
trải nghiệm](../../../docs/design/UI_Craft_Checklist.md). Audit trước sửa, rà chín
nhóm trong scope và giữ hành vi được duyệt; lấy token/component từ nguồn ITS,
không lấy mặc định của unslop làm chuẩn mới. Bàn giao theo mã CRAFT với actual và
evidence; mục chưa quan sát giữ Not Run. Màn đã tốt chỉ chỉnh finding có căn cứ.

Áp dụng bắt buộc [ITS-UI-RULE-01](../../../docs/architecture/Frontend_Design_System.md#its-ui-rule-01)
(Intake `ITS-UI-20261113-01`): tái sử dụng **100% control/pattern áp dụng** từ
`web/src/shared/components/ui` cho mọi feature/layout, cả trang public, dialog và
control trong slot/children. Không tính import một component là toàn màn đạt;
không tạo thư viện UI song song. Shell/PageHeader/state wrapper hiện có tiếp tục
được tái sử dụng đúng trách nhiệm. Kiểm nguồn/export thực tế trước khi thiết kế;
không giả định `Button`, `Input`, `Select`, `Textarea` độc lập đã có.

Cấm raw `<table>`, naked action buttons (gồm nút cấp trang/icon tự dựng), custom
search bar và inline modal trong nơi tiêu thụ. Dùng `RowActionMenu` cho chức năng
dòng, `FormActionButtons` khi đúng loại form, `Dialog` và
`ConfirmDialog`/`ConfirmModal` đúng contract. HTML nền tảng bên trong component
chuẩn vẫn được dùng theo review. Bảng ma trận/chi tiết cần semantics riêng phải
có RFC cho pattern dùng chung phù hợp, không tự ép thành lưới quản trị hoặc miễn trừ.

- **BẮT BUỘC DÙNG SHARED COMPONENTS ĐÓNG GÓI:** Mọi màn hình danh sách và lưới dữ liệu xây mới hoặc cập nhật BẮT BUỘC phải dùng bộ component chuẩn tại `web/src/shared/components/ui`:
  1. `<AdminDataTable<T>>`: CẤM tự viết thẻ `<table>` thủ công. Component tự động cố định cứng 3 cột đầu: `Thao tác (Menu 3 gạch)` → `Checkbox` → `STT`.
  2. `<StandardFilterBar>`: CẤM dùng grid kéo dãn toàn màn hình. Bắt buộc ô tìm kiếm 280px ở góc trái, bộ lọc và nút Đặt lại cạnh nhau, nút hành động cấp trang ở bên phải.
  3. `<BatchActionBar>`: Dùng cho thao tác hàng loạt khi chọn nhiều dòng.
  4. `<EmptyState>` và `<ConfirmModal>`: Dùng cho trạng thái rỗng và xác nhận hành động nguy hiểm.
- **Ngôn ngữ và dữ liệu:** Theo Content Style Guide; dùng tiếng Việt dễ hiểu và không lộ thông số kỹ thuật nội bộ không phục vụ tác vụ. Giữ tên pháp lý, thuật ngữ nghiệp vụ được duyệt, trích dẫn biểu mẫu và dữ liệu người dùng; không xóa/đổi chúng chỉ để đạt một quy tắc rút gọn câu chữ.
- Chọn Admin shell cho cán bộ hoặc Public shell cho người bên ngoài theo actor; dùng lại layout/tokens/primitives/patterns hiện có. Không nhúng shell quản trị vào form trả lời public hoặc tạo một hệ component riêng cho từng module.
- Màn danh sách dùng PageHeader, `StandardFilterBar` trong khung dữ liệu và footer phân trang gọn; `FilterBar` cũ chỉ là nợ cần hợp nhất theo RFC. Toolbar tìm kiếm/lọc cùng chiều cao, nút Đặt lại trung tính, xuống dòng có chủ ý trên mobile. Sau đổi lọc đưa trang về đầu và xử lý selection theo phạm vi đã quy định.
- Lưới quản trị theo yêu cầu hiện hành: **Thao tác → Checkbox → STT → dữ liệu**. Nút ba gạch ngang mở dropdown, không tự mở chi tiết; chọn Xem chi tiết mới mở vùng ngay dưới dòng đang chọn. Các chức năng dòng nằm trong dropdown; thao tác cấp trang đặt tại PageHeader. STT tính theo trang, selection có trạng thái mixed và hiển thị số dòng được chọn.
- Khi thiết kế/review lưới, áp dụng [chuẩn lưới quản trị đã duyệt, mục 5.1](../../../docs/architecture/Frontend_Design_System.md#admin-grid-standard), tiêu chí GRID-01–GRID-09: sort, xuất đúng phạm vi bằng nút/phím tắt, ghim, ẩn/hiện, đổi vị trí, nhớ/khôi phục bố cục và accessibility/mobile. Ghi rõ tiêu chí không áp dụng theo requirement/quyền; bản thiết kế phải thể hiện Tùy chỉnh cột và phạm vi Xuất dữ liệu, không chỉ vẽ bảng mặc định.
- Áp dụng [chuẩn trải nghiệm UX-01–UX-24, mục 5.2](../../../docs/architecture/Frontend_Design_System.md#admin-ux-standard): phân biệt header nhiều tầng/cây/row detail; căn theo ý nghĩa dữ liệu; cùng chức năng giữ vị trí, nhãn và hành vi. Khả năng cây/tổng hợp/hàng loạt theo requirement; task phải có ma trận áp dụng và lý do ngoại lệ. Không dùng mặc định thư viện để chốt ngữ nghĩa nghiệp vụ.
- Với tìm kiếm/liên thông/điều hướng, theo [contract UX-10–UX-13](../../../docs/architecture/Frontend_Search_Context.md): thiết kế điều kiện đang áp dụng/kế thừa/khóa và cách gỡ/reset; mapping cùng ID/nghĩa, lựa chọn phụ thuộc, Quay lại và vòng đời user/scope/tab. Thể hiện giá trị không hợp lệ/lỗi tải, không âm thầm mở rộng kết quả hoặc ghi đè form chưa lưu. Dùng [UI-26–UI-49](../../../docs/design/Design_Review.md#admin-ux-review) và case hai màn tham chiếu khi có liên thông; duyệt tiêu chí không phải nghiệm thu hình thức/tích hợp.
- Header quản trị có chuông thông báo, số chưa đọc, panel và trạng thái rỗng/đã đọc. Tích hợp thật theo contract Notification qua BFF, không tạo kênh thông báo riêng trong module.
- Form khảo sát giữ rõ nhóm câu hỏi, một/nhiều lựa chọn, ma trận và đơn vị; không biến câu đa lựa chọn thành radio hoặc hiển thị số khoảng như số chính xác. Label/error gắn đúng control; không dùng placeholder thay label.
- Tách dữ liệu form đang sửa, server state và trạng thái UI. Bỏ thay đổi chỉ loại bản nháp của form đang hủy, giữ dữ liệu đã lưu và dữ liệu/bản nháp của luồng khác; prototype cũng không reset toàn bộ fixture khi hủy một form. Pending chống gửi lặp; hủy/thay route/unmount không được để callback trễ vẫn ghi dữ liệu. Cơ chế lưu nháp/tự lưu chỉ làm khi yêu cầu có quy định.

## Shared Component RFC

Khi control/variant chưa có hoặc không đáp ứng semantics, không tự dựng tại
feature. Theo [quy trình RFC chuẩn](../../../docs/architecture/Frontend_Design_System.md#its-ui-rule-01):

1. Gửi nhu cầu qua intake PM; tra component tương đương và dòng trong
   [ma trận kiểm kê](../../../docs/architecture/UI_Design_System_Inventory_Matrix.md).
   RFC `ITS-UI-RFC-<nnn>` ở `docs/design/` bắt đầu `Proposed` theo task được cấp.
2. Nêu use case/actor, khoảng trống, màn tiêu thụ, API props/slots/types,
   variants/tokens, state, nội dung/i18n, responsive/keyboard/focus, acceptance,
   kiểm thử, guide, compatibility, thứ tự triển khai và rollback.
3. Dev Lead chỉ định một FE owner; UX/UI review pattern/a11y, Architect quyết
   contract/tái sử dụng, QA review acceptance, PM ghi quyết định. BA/Data/Security
   theo tác động. Chưa `Accepted` thì giữ phần implementation phụ thuộc chờ;
   tiếp tục phần độc lập, không code control riêng rồi hợp nhất sau.
4. FE bàn giao component ở `web/src/shared/components/ui` và export phù hợp
   trước feature tiêu thụ; chuyển từng màn theo dependency, cập nhật ma trận và
   user-guide khi đổi thao tác. QC phiên riêng kiểm đúng candidate; chỉ ghi
   `Implemented`/`Verified` theo evidence và xác nhận thực tế.

PR nêu component tái sử dụng/RFC/dòng ma trận/evidence. Vi phạm hoặc thiếu RFC chặn
bàn giao phần UI bị tác động. Bước 1 chỉ thể chế hóa; chưa thêm guard CI và không
nhận nợ hiện hữu đã được miễn trừ hoặc đã khắc phục.

## Tương tác và accessibility cần quan sát

Mô tả loading, empty, no-results, error/retry, forbidden, hết phiên, validation, pending và nội dung dài phù hợp với màn hình. Error nghiệp vụ dùng ngôn ngữ người dùng, không lộ stack trace hay tên field nội bộ.

Kiểm tra nhãn truy cập, bàn phím, focus rõ, menu Escape/return focus, dialog trap và background inert. Dialog lồng nhau chỉ cho dialog trên cùng tương tác; khi đóng tất cả trả focus về nút mở ngoài cùng. Sidebar desktop chuyển drawer mobile phải đồng bộ breakpoint CSS/JS và giữ đủ nhãn khi desktop từng bị thu gọn.

Kiểm tra các viewport 1440, 1024, 768, 390; zoom/reflow theo chuẩn hiện hành. Bảng chỉ cuộn trong container khi cần, không làm cả trang tràn ngang. Đo tương phản cặp màu thực tế, không suy ra đạt từ tên token. Nếu chưa kiểm tra mục nào, ghi Not Run; ảnh chụp đơn lẻ không chứng minh bàn phím/interaction đạt.

## Dùng v0 và bàn giao

Brief v0 gồm mục tiêu, actor, màn hình, shell, component/state và dữ liệu hư cấu. Kiểm kê mã sinh ra: Next.js wrapper, dependency, CSS reset, routing và icon; port có chủ ý sang React/Vite ITS thay vì chép nguyên ứng dụng mẫu. Không đưa secret hoặc dữ liệu thật vào prompt. Không mua gói, publish hoặc kết nối GitHub ngoài phạm vi được giao; nếu công cụ bị giới hạn, giữ nguồn/brief và ghi phần chưa làm.

Bàn giao prototype/source hoặc implementation theo task, danh sách component được tái sử dụng, trạng thái đã kiểm tra, ảnh đại diện desktop/mobile, nguồn/phiên bản được duyệt và vấn đề còn lại. Khi có code, chạy typecheck/lint/build/test phù hợp; QC kiểm tra độc lập các luồng thật trong phạm vi tích hợp.
