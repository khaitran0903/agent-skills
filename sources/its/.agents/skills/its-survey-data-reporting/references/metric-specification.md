# Đặc tả chỉ tiêu và đối soát dữ liệu

Đọc khi định nghĩa chỉ tiêu mới hoặc kiểm tra báo cáo. Đây là cấu trúc bàn giao, không ấn định một công thức cho mọi khảo sát.

## Một định nghĩa chỉ tiêu đủ tái lập

| Thuộc tính | Cần làm rõ |
| --- | --- |
| Mã, tên và phiên bản | Tên nghiệp vụ, mục đích, nguồn yêu cầu/câu hỏi |
| Population và kỳ | Ai thuộc đối tượng; đợt/ngành/thời gian; timezone khi cắt kỳ |
| Grain và khóa đếm | Một quan sát là gì; khóa khử trùng, phiên bản phản hồi được chọn |
| Tử số và mẫu số | Điều kiện chọn, đếm distinct hay số phiếu, mẫu số eligible/valid/answered |
| Giá trị và đơn vị | Số lượng, phần trăm, khoảng người/năm hoặc đơn vị khác |
| Missing và ngoại lệ | Bỏ trống, không biết, 0, không áp dụng, phiếu chưa nộp/không hợp lệ |
| Nhóm và bộ lọc | Nhóm có loại trừ nhau không, scope quyền, từ điển mã dùng để phân nhóm |
| Phiên bản dữ liệu | Snapshot gốc/sạch, phiên bản câu hỏi/danh mục/công thức, cutoff |
| Hiển thị | Số chữ số làm tròn, mẫu số 0, ghi chú đa lựa chọn hoặc ước tính |
| Kiểm chứng | Dữ liệu hư cấu, kết quả kỳ vọng, phép tính độc lập và người xác nhận |

Khi chưa đủ dữ liệu quyết định một thuộc tính, ghi câu hỏi và tác động. Có thể cung cấp kết quả các phương án dưới nhãn minh họa; không chọn một phương án làm quy tắc chính thức chỉ để hoàn thành bảng.

## Các tình huống cần đưa vào bộ đối soát

- Hai phiếu cùng khóa nghiệp vụ, khác trạng thái hoặc thời điểm; quy tắc chọn phiên bản cần xác nhận.
- Một phiếu chọn ba đáp án; một đáp án lặp do dữ liệu nhập; một phiếu bỏ trống; một phiếu không được hỏi theo điều kiện.
- Hai ngành cùng có một doanh nghiệp: tổng nhóm có thể khác tổng distinct toàn đợt.
- Nhóm “không có nhu cầu” và nhóm thiếu câu trả lời được lưu tách biệt.
- Khoảng đóng, khoảng mở, các khoảng theo giai đoạn có đơn vị năm; không đủ thông tin để suy ra tổng nhiều năm chính xác.
- Mẫu số bằng 0 hoặc bộ lọc không có dữ liệu; phân biệt không tính được tỷ lệ với tỷ lệ 0% có quan sát.
- Dữ liệu sửa sau khi báo cáo đã chốt: chạy lại snapshot cũ phải giữ kết quả cũ; báo cáo mới ghi phiên bản mới.
- User xem tổng hợp được nhưng không được tải liên hệ chi tiết; export không được mở rộng scope.

Không dùng dữ liệu liên hệ thực trong ví dụ/fixture. Đối với dữ liệu thật đã được phép xử lý, chỉ lưu các trường cần cho mục đích và che thông tin trong evidence.
