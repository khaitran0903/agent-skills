---
name: its-delivery-planning
description: Lập kế hoạch, phân rã backlog và điều phối bàn giao ITS với owner, phụ thuộc, acceptance và evidence; giữ quyết định nghiệp vụ/kiến trúc đúng thẩm quyền.
---

# Lập kế hoạch và điều phối

Đọc AGENTS, yêu cầu/task và [quy trình điều phối](../../../docs/development/agent-orchestration.md).
PM/Dev Lead chỉ đọc mục của mình trong [hồ sơ](../../../docs/development/role-profiles.md).
Khi lập hoặc đánh giá task, dùng [KPI](../../../docs/development/role-kpi.md); khi
gọi CLI mới đọc quickstart/recipe qua bảng trong AGENTS. Không đọc catalog toàn đội.

Phân rã theo vertical slice có thể kiểm chứng, gồm UI/API/quyền/dữ liệu/test liên
quan. Không chia một service cho mỗi bảng/màn hình. Mỗi việc có mã, nguồn/candidate,
owner/reviewer, file scope, dependency, đầu ra, acceptance, kiểm chứng/evidence và
môi trường riêng. Contract/component dùng chung có một owner, dependency không vòng.
Ước lượng nêu giả định; thời lượng nghiệp vụ không phải thời gian viết phần mềm.

PM tự chuẩn bị review đủ Ready ngay trong yêu cầu phân tích/lập kế hoạch, không
đợi task code hoặc anh chuyển việc. Dev Lead hiểu baseline/nguyên nhân gốc, chỉ
đạo giải pháp và review từng dòng/ca tác động; vòng giao/nhận/retest dùng quy trình
chuẩn, không lập bản sao trạng thái, model policy hoặc công thức KPI trong task.

Khi nhận finding, dùng [xử lý finding](../../../docs/development/agent-orchestration.md#finding-resolution). PM yêu cầu làm rõ phần chưa đủ để hành động; Dev Lead cùng owner ghi phương án hoặc bước chẩn đoán, điều kiện đóng và evidence cần thu trước giao sửa. Trước trình lại, đối soát delta và tự kiểm theo từng finding; không chuyển HOLD chung hoặc gọi thẩm định lại khi chưa có đầu vào mới phù hợp.

QA thiết kế từ lúc yêu cầu; QC độc lập kiểm bản bàn giao. Security theo applicability
và scope trong [quy trình](../../../docs/development/security-review.md). UI/quy trình
người dùng có BA/Docs soạn hướng dẫn, QA walkthrough, QC kiểm đúng phiên bản theo
[user-documentation](../../../docs/development/user-documentation.md). Với Việc làm,
đọc [phân công module](../../../docs/Module_QuanLyViecLam/QuanLyDoanhNghiep_Va_KhaoSat/Team_PhanCong_Va_Skill.md)
khi task thuộc phạm vi đó; không lấy đề xuất/tham khảo làm quyết định.

Đầu ra: backlog có dependency/Ready, task brief dùng [mẫu](../../../docs/development/agent-skills.md#task-brief),
KPI plan, quyết định chờ, rủi ro, checkpoint và điều kiện bàn giao/UAT/rollback.
Không sửa lịch sử để nhận đã chạy, không tự merge/deploy hoặc tạo lịch nền.
