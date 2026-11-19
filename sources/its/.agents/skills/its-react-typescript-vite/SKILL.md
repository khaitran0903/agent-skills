---
name: its-react-typescript-vite
description: Xây dựng frontend ITS bằng React 19, TypeScript và Vite theo module registry, API contract và chuẩn i18n/accessibility của repository.
---

# ITS React TypeScript Vite

Giữ owner_role và baseline/check/evidence của task; chỉ đọc [KPI](../../../docs/development/role-kpi.md) khi lập/thay/đánh giá phép đo. Nạp nguồn theo AGENTS, không đọc hồ sơ toàn đội hoặc runner khi task không gọi CLI.

Skill này hướng dẫn frontend ITS; không cấp quyền thay đổi backend contract, permission, authentication hoặc dependency ngoài pull request đã giao.

## Baseline phải đọc

Đọc AGENTS, task và mục kiến trúc/design system liên quan trong `docs/architecture/Architecture_Design_v1.0.md`, [chuẩn giao diện ITS](../../../docs/architecture/Frontend_Design_System.md), manifest module, OpenAPI/permission/requirement của feature. Kiểm package.json, lockfile, TypeScript config và scripts thật trước ghi lệnh build/test; không nạp phần ngoài tác động.

## Ranh giới frontend

- Shell quản lý router, session state, i18n, module registry và error boundary.
- Feature module quản lý màn hình và use case của module; không tự tạo token store, URL API hoặc permission rule riêng.
- API client là boundary duy nhất cho HTTP; kiểu DTO khớp OpenAPI, dùng `unknown` tại biên không tin cậy và không dùng `any` để che mismatch.
- Server authorization là nguồn quyết định. UI chỉ ẩn/hiện thao tác hỗ trợ người dùng; không coi việc ẩn nút là bảo mật.
- Tách remote state, form draft và transient UI state. Sau mutation thành công phải invalidate dữ liệu liên quan; hủy hoặc bỏ qua response cũ khi unmount.

## Đa ngôn ngữ và trải nghiệm

Mọi nhãn, validation, error message, empty/loading/error/disabled state dùng resource key. Mặc định `vi-VN`; thêm `en-US` khi feature được công bố. Hiển thị thời điểm theo UTC+7, trao đổi API bằng ISO 8601. Không đưa mã task, tên field nội bộ, HTTP code hoặc thuật ngữ hạ tầng vào giao diện.

Màn hình có keyboard navigation, focus rõ, label, tương phản và trạng thái dài/không có dữ liệu. Khi sửa layout, kiểm tra desktop/mobile và dữ liệu đại diện, không chỉ màn hình rỗng.

## Lưới quản trị

Khi xây mới hoặc sửa lưới danh sách, áp dụng [chuẩn lưới quản trị, mục 5.1](../../../docs/architecture/Frontend_Design_System.md#admin-grid-standard), tiêu chí GRID-01–GRID-09 đã được chủ dự án duyệt. Dùng pattern chung cho sort, xuất bằng nút/phím tắt, ghim, ẩn/hiện, đổi vị trí và ghi nhớ/khôi phục bố cục; module khai báo cột và quyền theo contract. Giữ nhóm Thao tác → Checkbox → STT. Không sort một trang rồi nhận là đã sort toàn bộ kết quả, hoặc xuất các trường vượt quyền.

Task và bàn giao phải nêu tiêu chí áp dụng/không áp dụng cùng lý do, phạm vi xuất, tổ hợp phím đã kiểm tra, nơi lưu bố cục và phụ thuộc backend còn thiếu. Dùng [checklist review](../../../docs/design/Design_Review.md); thêm bằng chứng bàn phím, mobile sau đổi cột và đối soát file xuất khi có tích hợp. Không kế thừa kết quả prototype cũ cho tiêu chí mới chưa kiểm chứng.

## Trải nghiệm quản trị và ngữ cảnh tìm kiếm

Áp dụng [UX-01–UX-24 đã duyệt, mục 5.2](../../../docs/architecture/Frontend_Design_System.md#admin-ux-standard) cho phần màn hình được giao. Task khai báo loại lưới, cột/nhóm/cây, đơn vị/căn chỉnh, filter, quyền, selection/tổng/export và phần không áp dụng có lý do. Dùng chung vị trí/tên control và pattern state; lưới cây/header nhóm là khả năng theo requirement, không tự thay row detail thành cây hoặc chọn hành vi mặc định thư viện thay nghiệp vụ.

Khi có tìm kiếm, điều hướng hoặc lựa chọn phụ thuộc, đọc [contract UX-10–UX-13](../../../docs/architecture/Frontend_Search_Context.md): truyền filter bằng mapping ID/ngữ nghĩa; tách applied filter, draft, server state và tùy chọn cá nhân; Quay lại giữ trạng thái hợp lệ; xử lý response cũ, quyền đổi và vòng đời user/scope/tab. Không truyền toàn bộ state giữa feature, âm thầm mở rộng query/export khi điều kiện mất hiệu lực, hoặc tự chọn kho lưu/API/schema mới. Thiếu contract là blocker của phần phụ thuộc.

Bàn giao ma trận GRID/UX và [UI-26–UI-49](../../../docs/design/Design_Review.md#admin-ux-review), evidence hai màn tham chiếu khi có liên thông, keyboard/mobile/IME, trạng thái lỗi và đối soát dữ liệu theo tác động. Chấp thuận tiêu chí không chứng minh source/prototype đã đạt; ghi Not Run cho kiểm tra chưa chạy. Nhiều view/đồng bộ thiết bị/chỉnh sửa kiểu spreadsheet chỉ triển khai khi có task riêng.

## Module registry

Module đăng ký route, menu, translation, permission, feature flag và API base path tại build time. Manifest được kiểm tra trong CI. Không tải JavaScript từ URL tùy ý và không dùng micro frontend nếu chưa có ADR.

## Kiểm chứng

Chạy typecheck riêng vì Vite build có thể không kiểm tra đầy đủ type; chạy lint, unit/renderer/serializer test và browser smoke phù hợp. Kiểm tra refresh, hết session, bị thu hồi quyền, lỗi mạng, response trễ và dữ liệu dài. Không dùng mock serializer hoặc response giả để kết luận luồng API thật đạt.
