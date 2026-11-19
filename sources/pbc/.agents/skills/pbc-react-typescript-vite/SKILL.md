---
name: pbc-react-typescript-vite
description: Xây dựng frontend PBC bằng React, TypeScript và Vite với Ant Design, API contract và các luồng công, lương theo quyền.
---

# Frontend PBC

Đọc `AGENTS.md`, yêu cầu màn hình, API/permission và package.json/lockfile/scripts thật. Theo phiên bản và thư viện đã chốt trong PBC; không ép React 19 hoặc module registry của ITS.

Shell giữ router, phiên đăng nhập, layout và error boundary. Feature giữ màn hình/use case, API client là biên HTTP chung. DTO khớp contract; dùng `unknown` tại biên không tin cậy, không dùng `any` để che sai kiểu. Server quyết định quyền; ẩn nút chỉ hỗ trợ trải nghiệm.

Tách server state, form draft và UI state. Dùng React Query, Zustand, React Hook Form/Zod khi phù hợp với baseline dự án; không thêm hai cơ chế cho cùng nhiệm vụ chỉ vì có trong template. Mutation thành công phải invalidate dữ liệu liên quan; response trễ không được ghi đè filter/form/phiên mới. Pending chống gửi lặp.

Dùng Ant Design và component dùng chung PBC cho table/form/modal; tham khảo [skill UI](../pbc-ui-design-system/SKILL.md) khi thay layout. Không copy đường dẫn/component `web/src/shared/components/ui` của ITS như thể đã tồn tại trong PBC.

Giao diện tiếng Việt, tiền VNĐ và ngày theo UTC+7. Tách ngày dạy/kỳ lương khỏi timestamp UTC. Không đưa tên field, mã kỹ thuật hoặc stack trace vào thông báo nghiệp vụ. Không tự thêm bản tiếng Anh khi chưa có yêu cầu.

Bảng công/lương hiển thị kỳ, trạng thái và phạm vi dữ liệu rõ ràng. Tính tổng, sort, filter, pagination và export phải cùng scope; không sort một trang rồi mô tả là toàn bộ dữ liệu. Tiền tính từ server; preview FE không là số tiền có thẩm quyền.

Phiếu lương kiểm đúng chủ thể và quyền xem/in. Khi hết phiên hoặc đổi tài khoản phải loại cache dữ liệu riêng tư tương ứng. Hành động khóa, mở lại, gửi xác nhận, duyệt và điều chỉnh thể hiện hậu quả theo contract, không tự nghĩ workflow mới.

Chạy typecheck riêng nếu build chưa làm; lint/build/test theo scripts và tác động. Browser smoke kiểm refresh/deep link, hết phiên/thu hồi quyền, lỗi mạng, response trễ, dữ liệu dài, bàn phím và mobile. Ghi rõ mock, prototype và tích hợp thật.

Finding phải có hướng sửa hoặc bước chẩn đoán theo luồng/trạng thái, owner và điều kiện đóng theo [quy trình chung](../../../docs/development/agent-orchestration.md#finding-resolution). Bàn giao delta, evidence mới và regression; báo cáo theo [ba nhóm](../../../docs/development/agent-cli-quickstart.md#report-checklist), đề xuất phòng ngừa ở component/state/test khi có căn cứ.
