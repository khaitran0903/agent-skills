---
name: pbc-dotnet-clean-architecture
description: Xây dựng backend PBC bằng .NET và EF Core theo kiến trúc nguyên khối phân lớp, cho TKB, chấm công, tính lương và xuất Excel.
---

# Backend PBC

Đọc `AGENTS.md`, yêu cầu/đặc tả liên quan và project thật trước khi sửa. Kiểm `global.json`, target framework, package và công cụ đã có; không suy phiên bản SDK từ tên skill hoặc sao chép phiên bản trong tài liệu cũ. Khi khởi tạo, chọn phiên bản còn hỗ trợ theo quyết định dự án.

## Ranh giới

- Domain giữ entity và invariant nghiệp vụ, không tham chiếu EF Core/ASP.NET.
- Application giữ use case, service, DTO, validation và abstraction cần thiết.
- Infrastructure giữ EF Core/PostgreSQL, migration, import/export và adapter.
- API giữ HTTP binding, authentication/authorization, mapping và DI; không đặt công thức lương trong controller.

Giữ kiến trúc nguyên khối gọn theo tài liệu PBC. Không mang Kafka, Redis, BFF, Media service, CQRS/MediatR, Outbox hoặc Worker của ITS vào chỉ vì skill nguồn sử dụng chúng. Chỉ thêm abstraction/hạ tầng khi use case có nhu cầu cụ thể.

## Triển khai use case

Xác định actor, quyền trên tài nguyên, trạng thái, đầu vào/đầu ra và acceptance. Tách DTO khỏi entity persistence. Kiểm validation và quyền ở server; không tin teacher ID, campus ID, giá hoặc tổng tiền do client gửi.

Dùng `decimal` cho tiền và quy tắc làm tròn đã chốt. Giữ kỳ lương với ngày bắt đầu/kết thúc rõ ràng, chọn phiên bản TKB/giá theo ngày hiệu lực. Không dùng tháng dương lịch hoặc quy tắc 70% làm mặc định khi đặc tả có ngoại lệ. Không tự ban hành chính sách thuế/BHXH.

Sinh/đồng bộ công phải chạy lại an toàn: khóa duy nhất theo tiết học thực tế, transaction, nguồn phiên bản và quy tắc bảo toàn chỉnh tay. Dạy thay phải giữ công của người thực dạy. Khóa, mở khóa, tính và duyệt kiểm phiên bản/concurrency tại server; dữ liệu đã duyệt cần bản chụp và lịch sử theo đặc tả.

Lưu audit đủ actor, thời điểm, trước/sau và lý do cho thay đổi trọng yếu. Ngày dạy/kỳ lương là ngày nghiệp vụ UTC+7; timestamp audit dùng UTC. Không chuyển ngày nghiệp vụ qua UTC rồi làm lệch ngày.

Import Excel có preview, ánh xạ, lỗi dòng và transaction/rollback theo phạm vi. Phân biệt `.xls` và `.xlsx`; không nhận ClosedXML đọc được mọi định dạng. Export kiểm quyền và scope, dùng template/kết quả đã chốt, không lộ field ngoài quyền.

## Kiểm chứng

Unit test quy tắc tính và chuyển trạng thái bằng expected độc lập. Integration test với PostgreSQL phù hợp khi xác nhận transaction, khóa duy nhất, concurrency và migration; EF InMemory không chứng minh các tính chất này. Kiểm API allow/deny và dữ liệu sau từ chối. Báo lệnh, bản kiểm, kết quả và giới hạn; không lấy mock làm bằng chứng E2E.

Finding phải có hướng sửa hoặc bước chẩn đoán, owner và điều kiện đóng theo [quy trình chung](../../../docs/development/agent-orchestration.md#finding-resolution). Tự kiểm delta/regression trước bàn giao QC; báo cáo theo [ba nhóm](../../../docs/development/agent-cli-quickstart.md#report-checklist), đề xuất phòng ngừa ở control/contract/test khi có căn cứ.

Quyết định 17/11/2026: PostgreSQL thay SQL Server; uint xmin cho concurrency hiện hành, UTC timestamptz, DateOnly/date cho ngày nghiệp vụ UTC+7 tương lai. Tiền decimal/numeric theo contract, không mã hóa lương ở tầng ứng dụng theo chỉ định chủ dự án. Giữ hash mật khẩu/quyền/audit. Initial migration chỉ DB trống, không autoDDL startup.
