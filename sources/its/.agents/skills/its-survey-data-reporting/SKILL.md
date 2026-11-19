---
name: its-survey-data-reporting
description: Định nghĩa, đối soát và review chỉ tiêu thống kê khảo sát ITS, nhất là mẫu số, phiếu trùng, thiếu dữ liệu, đa lựa chọn và nhu cầu nhân lực theo khoảng; không tự suy ra số tuyển dụng chính xác từ nhóm khoảng.
---

# Dữ liệu và báo cáo khảo sát ITS

Giữ owner_role và baseline/check/evidence của task; chỉ đọc [KPI](../../../docs/development/role-kpi.md) khi lập/thay/đánh giá phép đo. Nạp nguồn theo AGENTS, không đọc hồ sơ toàn đội hoặc runner khi task không gọi CLI.

Làm rõ ý nghĩa và khả năng tái lập từng chỉ tiêu trước khi viết truy vấn hoặc vẽ biểu đồ. Đọc `AGENTS.md`, yêu cầu được xác nhận, biểu mẫu gốc, quy tắc thu thập/làm sạch và quyền dữ liệu. Có thể lập phương án khi thiếu quyết định, nhưng không công bố chỉ tiêu chưa đủ định nghĩa như kết quả chính thức.

## Hợp đồng chỉ tiêu

Với mỗi chỉ tiêu, dùng [đặc tả chỉ tiêu và chất lượng dữ liệu](references/metric-specification.md). Xác định population, đơn vị một dòng dữ liệu và đơn vị đếm: doanh nghiệp, doanh nghiệp–ngành–đợt, phiếu hay người trả lời. Không mặc định mỗi doanh nghiệp chỉ có một phiếu cho mọi mục đích.

Ghi tử số, mẫu số, điều kiện đủ/loại, bộ lọc, phạm vi quyền, thời điểm chốt, phiên bản câu hỏi/danh mục, quy tắc làm tròn và kết quả khi mẫu số bằng 0. Tỷ lệ phải kèm số đếm và mẫu số để người đọc hiểu đúng; không lấy trung bình các phần trăm nhóm khi mẫu số khác nhau.

## Quy tắc dễ sai

- Chuẩn hóa trùng theo khóa nghiệp vụ đã duyệt. Nếu chưa chốt giữ phiếu mới nhất/hợp lệ hay gộp đáp án, trình bày tác động và câu hỏi cần chốt; không tự chọn thuật toán rồi coi là quy tắc nghiệp vụ.
- Phân biệt không có nhu cầu/giá trị 0 với bỏ trống, chưa xác định, không áp dụng và không được hỏi do nhánh điều kiện. Chỉ đưa dữ liệu thiếu vào mẫu số khi định nghĩa chỉ tiêu quy định như vậy; không biến missing thành 0.
- Câu hỏi đa lựa chọn: khử chọn trùng trong cùng một đơn vị đếm, không nhân bản mẫu số theo số đáp án. Tổng tỷ lệ các lựa chọn có thể vượt 100%; ghi rõ dạng câu hỏi. “Khác” và nội dung tự do cần xử lý riêng theo quy tắc mã hóa được duyệt.
- Khoảng tuyển dụng không phải số chính xác. Với BM12, “Dưới 10”, “10–30”, “31–50”, “Trên 50” theo từng giai đoạn mô tả người/năm; không tự đổi thành số trung điểm, tổng số người nhiều năm hay số vacancy thực tế. Nhóm “Trên 50” không có cận trên hữu hạn. Ước tính chỉ thực hiện khi được giao và có phương pháp/giả định được nêu rõ, tách khỏi số quan sát.
- Giữ nguyên ngữ nghĩa khoảng của nguồn; nếu ranh giới chồng lấn hoặc không rõ, chuyển BA/nghiệp vụ xác nhận. Không tự sửa nhãn hoặc khoảng đã thu thập để truy vấn dễ hơn.
- Tỷ lệ phản hồi và độ bao phủ/đại diện là các khái niệm khác nhau. Không kết luận đại diện toàn bộ doanh nghiệp từ một tỷ lệ phản hồi cao hoặc suy rộng tổng nhu cầu ngoài mẫu nếu chưa có phương pháp lấy mẫu/trọng số được duyệt.
- Không cộng cùng doanh nghiệp qua các nhóm chồng lấn rồi đặt tên là tổng doanh nghiệp duy nhất. So sánh các đợt cần kiểm tra tương thích câu hỏi, đơn vị đếm, thời gian và quần thể.

## Dữ liệu sạch và snapshot

Giữ truy vết dữ liệu gốc, phiên bản làm sạch, lý do loại/sửa, actor và thời điểm phù hợp. Thay đổi tên/ngành/quy mô doanh nghiệp hiện tại không được âm thầm thay kết quả lịch sử đã chốt. Báo cáo ghi snapshot dữ liệu, phiên bản định nghĩa chỉ tiêu và bộ tham số để chạy lại.

Thiết kế logic/read model thuộc service sở hữu; không join database service khác. File xuất đi qua Media, quyền tạo/tải được kiểm tra, dữ liệu chi tiết có thông tin liên hệ tách quyền với số tổng hợp. Đưa yêu cầu thời hạn lưu, nhóm mẫu nhỏ có thể lộ danh tính và dữ liệu tự do nhạy cảm cho người phụ trách quyết định; không tự đặt ngưỡng như một quy định đã có.

## Kiểm chứng và đầu ra

Dựng bộ dữ liệu hư cấu nhỏ gồm trùng, thiếu, 0, đa lựa chọn, khoảng mở, câu hỏi không áp dụng và hai snapshot. Tính kết quả kỳ vọng độc lập bằng phép tính tay hoặc công cụ bảng tính/script riêng, không gọi lại hàm truy vấn đang cần kiểm tra làm oracle.

Đối soát tổng số trước/sau loại, kết quả từng nhóm, tử số/mẫu số, quyền lọc và file xuất so với màn hình trên cùng snapshot. Ghi sự khác nhau do làm tròn/tổng nhóm chồng lấn. Nếu không được giao truy cập dữ liệu hoặc chạy hệ thống, bàn giao thiết kế kiểm chứng và ghi Not Run cho phần thực nghiệm.

Bàn giao từ điển chỉ tiêu, quy tắc chất lượng dữ liệu, câu hỏi chưa chốt, bộ dữ liệu/kết quả kỳ vọng, đặc tả báo cáo và bằng chứng đối soát trong phạm vi nhiệm vụ. Đại diện nghiệp vụ xác nhận ý nghĩa; QC xác minh implementation độc lập.
