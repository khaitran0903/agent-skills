# Đối soát kết quả từ nhiều đầu ra

Đọc khi cùng một kết quả xuất hiện ở query/API, màn hình, báo cáo hoặc file xuất và cần kiểm tính nhất quán.

## Chốt căn cứ so sánh

Lấy công thức, đơn vị, điều kiện chọn dữ liệu và cách hiển thị từ requirement/contract của dự án. Ghi phần định nghĩa còn thiếu trước khi tạo expected; không tự chọn quy tắc xử lý trùng, dữ liệu thiếu hoặc phạm vi tính.

Xác định phiên bản dữ liệu, thời điểm hoặc snapshot, tham số, actor/scope và phiên bản định nghĩa đang so sánh. Hai đầu ra có thể dùng cách trình bày khác nhau nhưng phải được đối chiếu theo cùng ngữ nghĩa đã khai báo. Nếu không thể giữ cùng dữ liệu, ghi giới hạn và kiểm lại trên bộ dữ liệu kiểm soát được khi phù hợp.

## Thiết kế và thực hiện đối soát

1. Chọn dữ liệu nhỏ, trung tính đủ phân biệt cách tính đúng và sai theo contract. Tính expected độc lập; giữ nguồn dữ liệu và các bước biến đổi cần tái lập.
2. So từng đầu ra với expected, rồi đối chiếu giữa các đầu ra. Hai output giống nhau vẫn có thể cùng sai nếu dùng chung một hàm lỗi.
3. Phân biệt giá trị gốc, giá trị sau biến đổi và giá trị hiển thị. So ở giai đoạn và độ chính xác mà contract quy định; không áp một quy tắc làm tròn cho mọi loại kiểm tra.
4. Khi lệch, lần theo định nghĩa, dữ liệu đầu vào, phạm vi, phép biến đổi và trình bày. Chỉ kết luận nguyên nhân khi có bằng chứng; không đổi expected theo implementation.

Ghi expected/actual của từng đầu ra cùng candidate, dữ liệu/tham số và bằng chứng. Nếu chưa đủ căn cứ định nghĩa thì nêu phần chưa đánh giá được; chưa chạy thì giữ Not Run. Kết quả đối soát không tự xác nhận mọi quyền dữ liệu hoặc toàn bộ báo cáo ngoài phạm vi đã kiểm.
