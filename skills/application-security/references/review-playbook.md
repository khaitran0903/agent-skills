# Playbook chọn theo ranh giới

## Thiết kế và đường dữ liệu

Ghi actor, tài sản, entrypoint, trust boundary, sink và control dự kiến. Kiểm spoofing/tampering/disclosure/replay/quá tải/nâng quyền khi liên quan. Theo caller thực tế và điều kiện khai thác; cấu hình hoặc tên hàm đáng ngờ chưa đủ là vulnerability. Đọc mã các nhánh có thể bác bỏ claim.

## Auth, session và quyền

Lập ma trận actor–permission–resource–scope–state. Thử đổi ID/scope, quyền bị thu hồi, tài khoản đổi trạng thái và đường gọi API trực tiếp. JWT còn hạn hoặc UI ẩn nút không chứng minh truy cập hợp lệ. Sau deny kiểm dữ liệu/side effect. Với cookie, kiểm CSRF/cookie attributes theo cơ chế thật; với BFF/proxy, kiểm allowlist tuyến và forwarding khi dự án có BFF.

## API, file và trạng thái

Xét parameterized query, output encoding theo context, mass assignment, URL/outbound request, giới hạn kích thước/thời gian. File có quyền tạo/tải, tên/path không thoát vùng lưu, nội dung/type được xác thực phù hợp, không public dữ liệu riêng chỉ vì đoán được URL. Không nhận extension là bằng chứng an toàn.

Kiểm duplicate/replay/race, transaction/concurrency và trạng thái sau từ chối. Khi có cache/event/worker, đối chiếu scope cache, invalidation, idempotency và commit/ack; không thêm hạ tầng phân tán cho dự án chưa sử dụng. Export cùng quyền/filter, không lộ field hoặc dữ liệu ngoài scope.

## Secret, dependency và CI

Không đưa credential/session/connection string hay dữ liệu riêng vào source, log, prompt hoặc evidence. Kiểm quyền workflow/artifact và đường dữ liệu không tin cậy vào command khi scope có CI. Với cảnh báo dependency, xác minh version thực từ lockfile, đường kéo vào, reachability và advisory chính thức hiện hành; không suy chỉ từ tên package. Báo công cụ/check chưa chạy.

## Xác minh và retest

PoC vừa đủ trên tài nguyên được giao, dừng theo giới hạn task. Lưu reproduction và expected/actual đã loại bí mật, không lưu raw HAR/cookie/token. Tách static hypothesis và runtime result. Bản sửa cần kiểm control thực thi đúng đường lỗi và regression; source chứa thêm `if` chưa chứng minh remediation đạt.
