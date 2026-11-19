---
name: dotnet-clean-architecture
description: Xây dựng hoặc review backend .NET và EF Core theo ranh giới lớp, use case, quyền tài nguyên và dữ liệu; dùng với kiến trúc phân lớp hiện có, không tự áp CQRS hay hệ thống phân tán.
---

# Backend .NET theo ranh giới dự án

Đọc AGENTS, yêu cầu/ADR, ownership và project bị tác động. Kiểm `global.json`, target framework, package/lockfile, DB provider và lệnh thật. Phiên bản công nghệ và topology lấy từ cấu hình/quyết định dự án.

## Ranh giới

| Lớp | Trách nhiệm |
| --- | --- |
| Domain | Entity/value object/invariant nghiệp vụ; không phụ thuộc EF Core/ASP.NET |
| Application | Use case, DTO, validation và abstraction cần thiết |
| Infrastructure | Persistence, migration, file và adapter ngoài |
| API | HTTP binding, auth boundary, mapping và DI; gọi use case theo kiến trúc hiện có |

Không trả entity persistence như DTO public. Giữ dependency hướng vào nghiệp vụ; không đặt công thức trong controller hoặc đưa nghiệp vụ module vào shared infrastructure. Không tạo abstraction, CQRS/MediatR, Outbox, broker, cache hoặc Worker chỉ vì mẫu skill có thể hỗ trợ.

## Triển khai use case

1. Xác định actor, tài nguyên/scope, trạng thái, invariant, input/output và acceptance. Kiểm endpoint tương đương để giữ style và error/serialization contract hiện có.
2. Validate và kiểm quyền ở server; không tin ID chủ thể, scope, giá hoặc tổng tiền do client tự khẳng định. Sau deny không được có side effect trái contract.
3. Đặt invariant ở Domain, orchestration ở Application và I/O ở adapter. Dùng cancellation, timeout và lifecycle phù hợp; retry có giới hạn và chỉ khi semantics cho phép.
4. Thay dữ liệu cần transaction, unique constraint/concurrency theo DB provider và migration có version. Không lấy EF InMemory làm bằng chứng khóa, transaction hoặc migration của PostgreSQL/SQL Server.
5. Khi dự án đã có event/cache, giữ atomicity, idempotency và invalidation sau commit theo contract. Với service tách DB, tôn trọng ownership; với monolith, không tự dựng ranh giới mạng mới.

Ngày nghiệp vụ khác timestamp sự kiện: giữ `DateOnly`/date, UTC/offset và timezone theo contract. Tiền dùng kiểu chính xác và quy tắc làm tròn đã chốt; không tự suy chính sách tính từ một ví dụ.

Giữ secret ngoài source/image/log. Query parameterized, output được encode theo context, file/input có giới hạn phù hợp. Tập trung kiểm ranh giới auth/file/tích hợp bị tác động; không thay auth hoặc nới quyền để làm local chạy.

## Kiểm chứng

Chọn unit cho invariant, integration trên DB thật phù hợp cho transaction/concurrency, contract cho API/event và smoke cho luồng/quyền bị tác động. Ghi candidate kể cả diff chưa commit, môi trường, lệnh/kết quả, evidence và phần chưa chạy. Finding có hướng xử lý hoặc bước chẩn đoán, owner và điều kiện đóng trước bàn giao.
