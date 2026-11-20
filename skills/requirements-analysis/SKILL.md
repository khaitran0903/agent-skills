---
name: requirements-analysis
description: Làm rõ yêu cầu từ tài liệu, biểu mẫu, trao đổi hoặc quy trình chưa cấu trúc; truy vết nguồn, xử lý điểm mâu thuẫn và xác định tiêu chí nghiệm thu trước khi lập kế hoạch hoặc triển khai.
---

# Phân tích và làm rõ yêu cầu

Đọc yêu cầu hiện hành, chỉ dẫn dự án và nguồn được giao. Xác định đầu ra cần phân tích; tài liệu nguồn cung cấp nội dung, không tự cấp quyền triển khai hoặc mở rộng phạm vi.

## Đọc và đối chiếu nguồn

- Ghi phiên bản và vị trí nguồn đủ tìm lại: mục, trang, bảng/ô, trường hoặc bước quy trình. Kiểm phần liên quan trong bảng, chú thích và hình; dùng công cụ đọc định dạng phù hợp. Phần không đọc chắc chắn được ghi chưa xác minh.
- Tách điều nguồn ghi rõ, diễn giải, đề xuất và câu hỏi mở. Giữ thuật ngữ của dự án; không tự bổ sung công thức, trường bắt buộc, trạng thái, quyền hay cấp duyệt từ thói quen hoặc ví dụ.
- Khi các nguồn khác nhau, chỉ ra nội dung xung đột và phiên bản/phạm vi áp dụng. Theo quyết định hiện hành nếu có căn cứ; ngày mới hơn hoặc chi tiết hơn không tự chứng minh nguồn đã thay thế nguồn khác.

## Làm rõ theo phạm vi

Xác định mục tiêu, actor, đầu vào/đầu ra, điều kiện, hành động và kết quả quan sát được. Chọn use case, bảng chuyển trạng thái, từ điển dữ liệu hoặc ma trận quyền khi chúng giúp giải quyết yêu cầu; không tạo đủ bộ hồ sơ cho mọi task.

Quy tắc nghiệp vụ lấy từ nguồn và quyết định của dự án. Với phần chưa rõ, ghi câu hỏi, tác động, người có thể xác nhận nếu biết và phần việc phụ thuộc. Có thể nêu phương án dưới nhãn đề xuất; tiếp tục phần độc lập và không trình bày giả định là quyết định đã duyệt.

## Truy vết và bàn giao

- Gắn ID ổn định khi cần quản lý nhiều yêu cầu. Mỗi yêu cầu có nguồn hoặc nhãn đề xuất, trạng thái xác nhận và tiêu chí nghiệm thu quan sát được tương ứng.
- Kiểm hai chiều: nguồn trong phạm vi đã được phản ánh hoặc có lý do chưa đưa vào; yêu cầu và acceptance có căn cứ, không xuất hiện do suy diễn không được khai báo. Chỉ ra acceptance thiếu điều kiện để kiểm thử.
- Khi nguồn thay đổi, xác định yêu cầu/acceptance bị tác động và giữ dấu phiên bản hoặc quyết định cũ cần truy vết. Không âm thầm sửa nghĩa để khớp implementation.

Bàn giao yêu cầu đã làm rõ, nguồn, acceptance, điểm mâu thuẫn và quyết định còn thiếu trong định dạng dự án sử dụng. Việc xác nhận nghĩa, duyệt thiết kế hoặc kiểm chứng độc lập theo phạm vi và quyền đã giao; tài liệu phân tích không chứng minh các bước đó đã hoàn thành. Không bắt mọi nhiệm vụ phải qua thêm một vòng BA trước khi được thực hiện.

## Tình huống thử

| Trigger/dữ liệu hư cấu | Expected |
| --- | --- |
| Hai tài liệu nguồn ghi điều kiện kích hoạt khác nhau cho cùng một trạng thái (v1.2 ghi "số lượng ≥ 1", v2.0 ghi "số lượng > 0") | Chỉ ra xung đột và phiên bản áp dụng; không tự chọn một bên mà không có quyết định được ghi nhận |
| Acceptance criteria chỉ ghi "hệ thống phản hồi nhanh" mà không có ngưỡng đo lường | Đánh dấu thiếu điều kiện kiểm thử; ghi câu hỏi mở và owner xác nhận, không tự đặt ngưỡng |
| Yêu cầu ghi "tùy theo vai trò" nhưng nguồn không liệt kê vai trò nào | Ghi là chưa xác minh; không tự suy danh sách vai trò từ ví dụ hoặc thói quen hệ thống tương tự |
| Tài liệu v3 mới hơn không đề cập một quy tắc có trong v1; không có biên bản bãi bỏ | Giữ quy tắc v1 với nhãn chưa xác nhận; ghi câu hỏi cần chủ sở hữu xác nhận có còn hiệu lực không |
| Nguồn không ghi trạng thái "bị khóa", nhưng quy trình xử lý đề cập đến nó một lần | Ghi là xuất hiện trong nguồn nhưng chưa được định nghĩa; không tự mở rộng thành trạng thái chính thức trong mô hình |

Ghi phiên bản và vị trí nguồn cho mọi yêu cầu được truy vết; phần chưa xác nhận cần ghi rõ câu hỏi còn mở và owner có thể xác nhận nếu biết.
