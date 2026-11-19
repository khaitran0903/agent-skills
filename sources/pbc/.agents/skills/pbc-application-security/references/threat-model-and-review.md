# Threat model và review

Vẽ luồng thật của lát cắt: Browser → API → Application → PostgreSQL và import/export khi có. Ghi nơi xác thực, nơi kiểm quyền cuối, dữ liệu do client kiểm soát và nơi chứa công/lương. Không thêm service ITS vào sơ đồ khi PBC không có.

Đánh giá giả mạo danh tính, sửa công/giá/tiền, phủ nhận thao tác, lộ phiếu lương, cạn tài nguyên và nâng quyền. Mỗi abuse case có actor, tiền điều kiện, tài sản, control và test phân biệt đúng/sai. Chính sách lưu giữ dữ liệu và công thức lương cần nguồn nghiệp vụ, không do Security tự chốt.

Review PR phải định danh base/candidate và diff chưa commit, theo cả caller/handler/adapter/config ngoài diff. Ưu tiên auth/scope, validation bị gỡ, upload/export, secret và cấu hình. Kiểm missing/null/rỗng, hết hạn, lỗi dependency và sai môi trường theo contract; không mặc định mở quyền khi lỗi.

Khi có lỗi gốc, tìm các đường cùng nguyên nhân và xác minh control upstream trước kết luận. Giữ phạm vi review và phần chưa đọc. Finding theo [mẫu](finding-and-retest.md); checklist bên ngoài không tự trở thành tiêu chí chứng nhận.

Quyết định 17/11/2026: không mã hóa lương ở tầng ứng dụng. Kiểm quyền/field leak, hash mật khẩu, secret ngoài Git và least privilege PostgreSQL vẫn bắt buộc. Runtime không owner/superuser/CREATEDB, audit chỉ SELECT/INSERT; migration role riêng.
