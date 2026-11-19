# Form nhập liệu, bàn phím và bảo toàn draft

Đọc khi làm editor/form có nhập lặp, danh sách token hoặc nguy cơ mất nội dung.
Tìm component, validation/schema và dirty guard hiện có trước khi bổ sung hành vi.

## Tag/chip và IME

- Xác định field là danh sách token hay văn bản tự do. Delimiter lấy từ schema;
  dấu phẩy có thể là nội dung hoặc số thập phân, không mặc định tách chuỗi.
- Trong IME composition, Enter/Backspace/delimiter chưa phải thao tác commit/xóa
  token. Kiểm cả kết thúc composition và phím Enter kế tiếp trên trình duyệt đích.
- Giữ Tab để điều hướng trừ khi contract của control quy định rõ cách khác.
  Paste nhiều token chỉ tách theo grammar được hỗ trợ; dữ liệu mơ hồ phải giữ lại
  cho người dùng sửa. Trim/deduplicate theo quy tắc field, không tự đổi hoa/thường
  hoặc chuẩn hóa làm mất ý nghĩa.
- Mỗi chip có tên và nút xóa truy cập được bằng bàn phím. Backspace khi input
  rỗng chỉ chọn/xóa chip theo hành vi component đã chốt; input có chữ vẫn sửa chữ.
  Sau xóa, focus trở về vị trí dự đoán được, không rơi ra ngoài form.

## Dirty guard và recovery

So sánh giá trị có nghĩa với baseline lúc tải/lưu thành công. Không đánh dirty chỉ
vì server state refresh, thứ tự property hay metadata UI thay đổi. Khi save thất
bại hoặc kết quả chưa rõ, giữ draft; response cũ không đánh dấu draft mới là sạch.

Áp dụng guard của host cho route, tab nội bộ và modal close; unload của trình
duyệt có giới hạn và không bảo đảm lưu được nội dung. Khi được giao recovery bền
vững, chốt actor/tenant/scope, entity và schema version, TTL, chính sách dữ liệu
nhạy cảm, cleanup khi logout/revoke và xung đột với dữ liệu mới trên server.
Key chỉ gồm entity ID có thể lộ draft trên máy dùng chung. Không tự thêm
localStorage hoặc tuyên bố không mất dữ liệu từ dirty guard.

## Validation và focus

Counter dùng cùng cách đếm với contract (byte/code point/grapheme/code unit),
nhất là Unicode và emoji. Inline validation xuất hiện đúng thời điểm tương tác;
kiểm bất đồng bộ phải bỏ response của giá trị cũ. Submit lỗi focus field lỗi đầu
tiên và liên kết thông báo bằng semantics của component. Sau thêm dòng, focus
input mới; sau đóng dialog trả focus về control mở dialog.

Shortcut submit/Escape theo host, không kích hoạt giữa composition, trong editor
đang dùng phím đó hoặc gây submit kép. Pending phản ánh trạng thái request thật.

## Tình huống thử

| Trigger/dữ liệu hư cấu | Expected |
| --- | --- |
| Field chỉ dùng Enter để thêm; nhập `1,5` rồi Tab | Không tách thành hai chip; Tab chuyển focus |
| Gõ tiếng Việt bằng IME, Enter để xác nhận âm tiết | Không thêm token hoặc submit trước khi kết thúc composition |
| Save draft A, gõ tiếp B trong lúc chờ response A | B còn dirty; response A không ghi đè hoặc đánh sạch B |
| Tài khoản A có draft, logout rồi B mở cùng entity | Không khôi phục nội dung của A cho B |
| Validation uniqueness của giá trị cũ trả về sau giá trị mới | Kết quả cũ không đổi trạng thái field mới |

Ghi actual và môi trường khi chạy; bảng expected không chứng minh UI đã được thử.
