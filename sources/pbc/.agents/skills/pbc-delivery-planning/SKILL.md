---
name: pbc-delivery-planning
description: Lập kế hoạch và phân rã backlog PBC theo lát cắt nghiệp vụ, phụ thuộc, tiêu chí nghiệm thu và bằng chứng bàn giao.
---

# Lập kế hoạch PBC

Đọc `AGENTS.md`, yêu cầu hiện hành và phần tài liệu PBC liên quan. Phân biệt quyết định đã chốt, đề xuất và vấn đề còn chờ; không dùng bản phản biện như quyết định thay yêu cầu.

Phân rã theo lát cắt có thể kiểm chứng gồm UI/API/quyền/dữ liệu/test liên quan. Mỗi việc ghi nguồn yêu cầu, owner, phạm vi file, phụ thuộc, đầu ra, acceptance, cách kiểm chứng và môi trường. Không tạo một service cho mỗi bảng hoặc kéo quy trình tổ chức ITS sang PBC.

Ưu tiên chứng minh đường đi TKB → công thực dạy → xác nhận → tính lương → duyệt → phiếu lương. Đưa đối soát số học và phiên bản dữ liệu vào các lát cắt sớm; không đợi cuối dự án mới thử tính lương. Ước lượng phải nêu giả định và phần chưa quyết định.

Các phụ thuộc cần làm rõ theo tác động: kỳ công/kỳ lương, ngày hiệu lực TKB và đơn giá, dạy thay, khóa/mở công, xác nhận hết hạn, duyệt hai cấp, sửa sau duyệt, phạm vi xem/in phiếu lương, chính sách thuế/BHXH. Ghi câu hỏi và ảnh hưởng cho phần thiếu; tiếp tục việc độc lập.

QA thiết kế acceptance và dữ liệu kỳ vọng từ yêu cầu. Khi có nhiệm vụ QC độc lập, bàn giao candidate và evidence cho người/phiên khác; tự kiểm không được gọi là QC độc lập. Không tự tạo đội agent, chọn model/CLI, KPI hay gate phê duyệt mới.

Theo [ma trận phối hợp](../../../docs/development/agent-orchestration.md#coordination-matrix) và [bảng kiểm giao/nhận](../../../docs/development/agent-cli-quickstart.md#task-checklist), PM làm rõ mục tiêu/acceptance, Dev Lead chốt cách làm hoặc chẩn đoán, mốc kiểm và readiness; worker báo cáo sai lệch, nguyên nhân và hành động tiếp theo.

Finding cần có expected/actual, bản tái hiện, nguyên nhân đã xác minh/giả thuyết/chưa biết, hướng xử lý hoặc bước chẩn đoán cụ thể, owner và điều kiện đóng theo [quy trình chung](../../../docs/development/agent-orchestration.md#finding-resolution). Dev Lead cùng owner xác định phương án/vùng tác động/evidence trước giao sửa; PM xử lý scope/ưu tiên/quyết định trong quyền. Trước retest đối chiếu delta và evidence mới, giữ lịch sử kết quả.

Theo [vòng cải tiến](../../../docs/development/agent-orchestration.md#improvement-loop), mỗi hành động được chọn có owner, thời hạn/mốc kiểm, reviewer và cách xác minh hiệu quả; đưa vào backlog hiện có. Không dùng việc phòng ngừa tương lai để đóng lỗi chặn hiện tại hoặc nhận đã đo hiệu quả khi còn chờ kỳ quan sát.

Đầu ra là backlog có thứ tự phụ thuộc, tiêu chí Ready/Done phù hợp nhiệm vụ, rủi ro, quyết định chờ và bước tiếp theo. Chỉ lập kế hoạch không đồng nghĩa đã triển khai, kiểm thử, merge hoặc phát hành.
