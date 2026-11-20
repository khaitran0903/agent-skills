# Điều hướng, ngữ cảnh và vòng đời state

Đọc khi task có truyền điều kiện giữa màn hình, khôi phục trạng thái điều hướng, filter phụ thuộc hoặc thay đổi tài khoản/scope.

## Xác định contract state

Tìm cơ chế router, cache và lưu state hiện có. Phân biệt điều kiện đã áp dụng, dữ liệu đang nhập, state history, server state và tùy chọn cá nhân. Với mỗi giá trị cần truyền/khôi phục, làm rõ nguồn, ý nghĩa/định danh, phạm vi tồn tại, thứ tự ưu tiên và hành vi reset theo yêu cầu dự án.

- Cùng tên hiển thị không chứng minh hai trường có cùng nghĩa. Mapping cần giữ kiểu, operator và tập giá trị; thiếu mapping thì làm rõ phần phụ thuộc, không đoán bằng tên.
- Phân biệt không cung cấp giá trị với chủ ý xóa giá trị. Việc khôi phục hoặc fallback không được tự lấp lại thao tác xóa đã được contract xác định.
- Back/Forward, quay về từ form, refresh, direct link và tab mới có thể có nguồn state khác nhau. Xác định hành vi cho các đường thực sự được hỗ trợ; không tự đặt URL hay saved state làm ưu tiên chung.
- Phạm vi chia sẻ giữa tab hoặc màn hình phải có chủ ý. Không thêm persistent storage hay đồng bộ toàn ứng dụng chỉ để nhớ một điều kiện cục bộ.

## Kiểm trước khi sử dụng state

State từ URL, history hoặc cache vẫn phải được kiểm theo contract và quyền/scope hiện hành. Khi giá trị mất hiệu lực, lỗi tải hoặc chưa rõ quyền, không coi việc bỏ filter là cách mặc nhiên hợp lệ để mở rộng query/export. Áp dụng đường xử lý đã chốt; phần chưa có quyết định cần được làm rõ trước truy vấn phụ thuộc.

Với lựa chọn cha–con, kiểm chuỗi theo phụ thuộc và giữ phản hồi gắn với request/cha/scope tương ứng. Response cũ không thay options hoặc selection của context mới. Lỗi tải chưa chứng minh lựa chọn cũ đã bị xóa.

Khôi phục state không làm dữ liệu server tự trở nên mới. Revalidate/invalidate khi có thay đổi liên quan; xử lý trang hoặc anchor không còn hợp lệ theo component/contract. Không để khôi phục history tạo vòng history mới hoặc ghi đè draft đang sửa.

## Kiểm chứng theo đường điều hướng

Chọn các đường bị tác động và quan sát cả UI state lẫn request/scope: truyền giá trị, chủ ý xóa, khôi phục history, thay context trong khi request cũ còn chờ, đổi phiên/quyền và giá trị không còn hợp lệ. Expected lấy từ contract đã xác định, không ép mọi ứng dụng có cùng cách nhớ trang hoặc chia sẻ tab.
