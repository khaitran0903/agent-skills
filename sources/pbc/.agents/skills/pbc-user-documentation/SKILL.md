---
name: pbc-user-documentation
description: Soạn và kiểm chứng hướng dẫn sử dụng PBC theo vai trò cho TKB, công, xác nhận, lương và in phiếu; phân biệt bản nháp với thao tác đã kiểm trên ứng dụng.
---

# Hướng dẫn sử dụng PBC

Đọc `AGENTS.md`, yêu cầu/quy trình đã chốt, ma trận quyền và bản ứng dụng/prototype được giao. Ghi nguồn, build/commit, môi trường, vai trò và phạm vi dữ liệu. Tài liệu người dùng mới đặt trong `docs/user-guides/`; runbook kỹ thuật trong `docs/runbooks/`.

Hướng dẫn theo mục tiêu: quyền và điều kiện bắt đầu, dữ liệu chuẩn bị, thao tác bằng đúng tên menu/nút, kết quả quan sát và xử lý lỗi. Không đưa lệnh triển khai, DB schema hay thuật ngữ nội bộ vào luồng giáo viên/kế toán.

Quy trình nhiều vai trò phải nêu ai thực hiện, đầu vào/đầu ra, trạng thái, người nhận và nhánh từ chối/trả lại. Với công/lương ghi rõ kỳ, phiên bản, xác nhận, khóa và duyệt theo quyết định hiện hành; không tạo chính sách hết hạn hoặc mở khóa từ suy đoán.

Ảnh dùng dữ liệu hư cấu/đã ẩn danh, có chú thích và đúng phiên bản. Chưa có bản chạy chỉ soạn nháp từ đặc tả/prototype, nêu phần chưa xác minh; không dựng ảnh và gọi là ảnh ứng dụng thực tế.

Khi kiểm chứng, thực hiện lại bước trên đúng build bằng vai trò tương ứng: luồng chính, validation, từ chối quyền và bàn giao. Ghi expected/actual và `Passed`, `Failed`, `Not Run`. Chỉ đọc source/ảnh không chứng minh thao tác đã chạy. Không sửa hướng dẫn để hợp thức hóa lỗi ứng dụng.

Bàn giao file, nguồn áp dụng, build, evidence đã lọc, phần chưa chạy và quyết định chờ. Markdown là bản nguồn; chỉ xuất Word/PDF khi yêu cầu và dùng công cụ kiểm bố cục phù hợp.

Finding tài liệu nêu hướng cập nhật hoặc bước đối chiếu build/nguồn, owner và điều kiện đóng theo [quy trình chung](../../../docs/development/agent-orchestration.md#finding-resolution). Báo cáo theo [ba nhóm](../../../docs/development/agent-cli-quickstart.md#report-checklist); bài học đã xác minh có thể cập nhật hướng dẫn/skill trong scope, không hợp thức hóa lỗi ứng dụng bằng đổi tài liệu.
