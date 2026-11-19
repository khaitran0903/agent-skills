---
name: application-security
description: Review thiết kế hoặc mã ứng dụng và xác minh ranh giới auth, dữ liệu, file, dependency theo phạm vi bảo mật được giao; phân biệt nghi vấn tĩnh, khai thác runtime và kết quả retest.
---

# Review bảo mật ứng dụng

Đọc yêu cầu, AGENTS, security policy/contract/ADR liên quan và candidate kể cả diff chưa commit. Xác định tài sản, actor, input kiểm soát, trust boundary và hành động được giao. Tên skill không tự cấp quyền kiểm thử chủ động trên một hệ thống.

Chọn phần liên quan trong [playbook](references/review-playbook.md), không buộc mọi task chạy toàn bộ. Theo dữ liệu từ entrypoint qua validation/authorization đến sink; tìm control và caller constraint có thể bác bỏ giả thuyết trước phân mức.

Review tĩnh source trong scope có thể tiếp tục khi thiếu môi trường runtime. Với kiểm thử chủ động, dùng target/danh tính test/hành động/giới hạn đã được giao; quyền rõ rồi không xin lại cho từng lệnh. Phần thiếu phạm vi phải được làm rõ trước hành động phụ thuộc.

Giữ kiến trúc, auth, ownership và contract dự án. Không đổi password hashing, response status/envelope, topology hoặc schema từ ví dụ ngoài; không nới sandbox/auth để làm PoC chạy. Dùng dữ liệu hư cấu và evidence đã lọc bí mật. Không tự gửi source lên scanner ngoài hoặc cài script nguồn tham khảo.

## Finding

Ghi claim, ảnh hưởng/mức độ và căn cứ, candidate, actor/quyền sẵn có, input, đường input → control → sink với file/dòng, bước tái hiện, expected/actual, side effect, loại evidence và giới hạn. Có owner, hướng sửa hoặc bước chẩn đoán cụ thể và điều kiện đóng.

`Confirmed` có bằng chứng vi phạm; `Suspected` thiếu điều kiện; `False Positive` có bằng chứng bác bỏ; `Fixed` sau retest; `Risk Accepted` cần quyết định có thẩm quyền. Các trạng thái này khác verdict test. Chấp nhận rủi ro không biến Failed thành Passed; thiếu runtime không biến nghi vấn thành khai thác đã xác minh.

Khi được giao sửa, giữ phạm vi và tự kiểm; xác minh độc lập cần người/phiên khác theo nhiệm vụ. Retest đúng candidate mới, kiểm đường lỗi gốc và regression control liên quan, giữ lịch sử. Bàn giao finding/evidence, phần chưa chạy và quyết định chờ; không chỉ trả một nhãn HOLD.
