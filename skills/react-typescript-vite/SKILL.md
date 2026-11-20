---
name: react-typescript-vite
description: Xây dựng hoặc review frontend React, TypeScript và Vite với API contract, phân tách state, xử lý response trễ và kiểm chứng trình duyệt; dùng theo component và phiên bản của dự án.
---

# Frontend React / TypeScript / Vite

Đọc AGENTS, yêu cầu màn hình, API/permission, design system và `package.json`/lockfile/scripts thực tế. Giữ framework, phiên bản, router, state library và component đã được dự án chọn.

- Shell giữ router, session, layout và error boundary theo kiến trúc hiện có. Feature giữ use case; API client là boundary HTTP chung, DTO khớp contract. Dùng `unknown` ở biên không tin cậy, không dùng `any` che mismatch.
- Server quyết định quyền. UI ẩn/hiện thao tác hỗ trợ trải nghiệm; không là bằng chứng phân quyền API.
- Tách server state, form draft và transient UI state. Mutation thành công invalidate dữ liệu liên quan; response trễ không ghi đè filter/form/phiên mới. Pending chống gửi lặp; hủy/unmount không để callback trễ lưu tiếp ngoài contract.
- Hủy form chỉ bỏ thay đổi của form đó; không reset dữ liệu đã lưu hoặc draft của luồng khác. Cache dữ liệu riêng tư phải được cô lập/loại bỏ phù hợp khi đổi tài khoản hoặc scope.
- Sort/filter/paging/tổng/selection/export có phạm vi rõ và nhất quán. Không sort một trang rồi mô tả là toàn bộ kết quả; không xuất field vượt quyền.
- Điều hướng liên thông truyền ID và ngữ nghĩa được chốt; phân biệt applied filter với draft. Khi lựa chọn phụ thuộc mất hiệu lực, không âm thầm mở rộng query/export hoặc ghi đè form chưa lưu.
- Tái sử dụng token/component thật; không giả định thư viện ITS hoặc Ant Design tồn tại. Không thêm hai cơ chế quản lý cùng loại state từ hai template.
- Ngôn ngữ, i18n, tiền, đơn vị và timezone theo dự án. Tách ngày nghiệp vụ khỏi timestamp UTC; thông báo phục vụ người dùng, không lộ stack trace hoặc field nội bộ.

Thiết kế loading, empty, no-results, error/retry, read-only/forbidden, hết phiên, validation và nội dung dài theo màn hình. Label gắn control, focus rõ, hỗ trợ bàn phím và responsive. Không thêm trạng thái nghiệp vụ chỉ vì checklist nêu ví dụ.

Khi làm form nhập liệu nhiều, tag/chip, bàn phím, dirty guard hoặc khôi phục draft, đọc [form ergonomics](references/form-ergonomics.md). Reference giữ IME, ngữ nghĩa delimiter và cô lập draft; không yêu cầu thêm persistent storage chỉ để chỉnh giao diện.

Khi truyền context, khôi phục history hoặc xử lý filter phụ thuộc, đọc [state khi điều hướng](references/navigation-context.md). Xác định mapping và vòng đời theo contract hiện có; không lấy thứ tự ưu tiên state của một dự án làm mặc định chung.

Chạy typecheck riêng nếu build chưa làm; Vite build không mặc nhiên chứng minh typecheck đạt. Lint/build/test theo scripts và tác động. Browser smoke kiểm refresh/deep link, lỗi mạng, quyền/phiên, response trễ, bàn phím, dữ liệu dài và mobile khi liên quan. Ghi rõ static/jsdom/mock/prototype/tích hợp thật, candidate và evidence. Chưa quan sát hành vi thì ghi Not Run.
