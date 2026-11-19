# API, file và trạng thái

Tên file giữ từ nguồn ITS; không yêu cầu Media service hay hệ phân tán.

Theo input tới DTO/validation/query/process/template/output. Kiểm injection, XSS, nhận thừa trường, parser và field leak. Nếu có outbound URL, kiểm đích/redirect theo phạm vi; chỉ thử target được giao. React escape mặc định không chứng minh raw HTML hoặc template an toàn.

Import Excel kiểm extension/MIME/nội dung, kích thước, số sheet/dòng, tên file/đường dẫn và thư viện đọc đúng `.xls`/`.xlsx`. File nằm ngoài web root, không thực thi macro hoặc formula từ nguồn không tin cậy. Export xử lý ô văn bản bắt đầu như công thức theo định dạng đầu ra; không phá công thức template đã kiểm soát. Quyền tạo/tải file và thời hạn lưu theo contract.

Kiểm transaction, uniqueness, concurrency và idempotency cho sinh công, import, tính/duyệt lương. Lập lịch xen kẽ request/commit/mở khóa/duyệt và kết quả timeout chưa rõ. Không retry mutation khi chưa biết kết quả nếu thiếu cơ chế đối soát.

Chỉ kiểm cache/job/notification khi có trong bản chạy. Kiểm side effect sau deny/timeout và dữ liệu đã khóa/duyệt. Dùng PostgreSQL thật khi kết luận hành vi transaction/concurrency của PostgreSQL; mock không đủ bằng chứng.
