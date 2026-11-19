# Xác thực và phân quyền

Tên file giữ từ nguồn ITS để truy vết; không yêu cầu PBC triển khai BFF. Lấy expected từ cơ chế auth và ma trận quyền thật.

Với JWT kiểm issuer/audience/signature/type/expiry và xử lý logout/disable/đổi quyền theo cam kết. Với cookie kiểm flags, CSRF và Origin cho mutation theo thiết kế. Kiểm cách lưu token/phiên thật, tránh lộ qua URL/log/bundle; không tự thay cơ chế auth hoặc thêm SSO/MFA ngoài task.

Lập ma trận actor × action × resource × campus × trạng thái nghiệp vụ × trạng thái phiên. Dùng giáo viên A/B hư cấu và tài khoản lập/duyệt theo quyền được chốt.

- Đổi ID/query/body hoặc gọi trực tiếp API không được đọc/sửa công hay phiếu lương ngoài phạm vi.
- List/count/detail/batch/export/in phiếu phải cùng ranh giới dữ liệu và field policy.
- Tự gửi role, teacher ID, giá, số tiền hoặc trạng thái duyệt không được nâng quyền.
- Request duyệt/mở khóa đồng thời phải giữ invariant và audit.
- Đổi quyền/phiên và cache cũ không được kéo dài truy cập quá contract; kiểm cả response đang bay.

Sau từ chối kiểm dữ liệu và side effect. Chưa có runtime ghi `Not Run`; JWT còn hạn hoặc UI ẩn nút không là oracle cho quyền tài nguyên.
