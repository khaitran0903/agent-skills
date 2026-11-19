---
name: its-dotnet-clean-architecture
description: Xây dựng backend ITS bằng .NET 10 theo Clean Architecture, DDD, CQRS và các hợp đồng nền tảng của repository.
---

# ITS .NET Clean Architecture

Giữ owner_role và baseline/check/evidence của task; chỉ đọc [KPI](../../../docs/development/role-kpi.md) khi lập/thay/đánh giá phép đo. Nạp nguồn theo AGENTS, không đọc hồ sơ toàn đội hoặc runner khi task không gọi CLI.

Skill này hướng dẫn cách làm trong ITS. Nó không cấp quyền thay đổi schema, contract, dependency, deployment hoặc dữ liệu ngoài phạm vi được giao.

## Baseline phải đọc

Đọc AGENTS, task, các mục kiến trúc liên quan trong `docs/architecture/Architecture_Design_v1.0.md`, ownership/dependency, requirement/ADR và project thật bị tác động. Kiểm `global.json`, target framework, package version/command/config trước thêm dependency; không nạp toàn kiến trúc ngoài tác động.

## Ranh giới project

| Lớp | Trách nhiệm | Không được làm |
| --- | --- | --- |
| Domain | Entity, value object, invariant, domain event | Không tham chiếu EF Core, ASP.NET, Infrastructure hoặc transport |
| Application | Use case, command/query, handler, DTO, orchestration | Không dùng concrete DbContext, repository implementation hoặc HTTP client cụ thể |
| Infrastructure | PostgreSQL/EF Core, Redis, Kafka, Media, Notification và adapter ngoài | Không đặt business rule và không công bố entity persistence |
| Api | HTTP binding, authentication/authorization boundary, response mapping, DI composition | Không truy cập DbContext/repository trực tiếp và không chứa nghiệp vụ |
| Worker | Consumer, job và xử lý nền có scope/cancellation/telemetry | Không chạy tác vụ quan trọng chỉ bằng Task.Run trong request |

Dependency chuẩn: `Api -> Application -> Domain`, `Api -> Infrastructure` chỉ để composition/DI, `Infrastructure -> Domain`, `Application -> Domain`. Shared package chỉ cung cấp abstraction/hạ tầng được duyệt; không đưa nghiệp vụ module vào SharedKernel.

## Cách triển khai một use case

1. Xác định module sở hữu, actor, permission, aggregate, trạng thái và acceptance criteria.
2. Chốt request/response, error code, event và migration impact trước khi viết handler. Với HTTP API, đọc endpoint hiện có để giữ cùng một style; không trộn controller và minimal API trong cùng project chỉ vì skill nguồn có ví dụ khác.
3. Tách request/response DTO khỏi entity persistence; không trả entity EF trực tiếp. DTO public dùng kiểu bất biến phù hợp convention hiện có, ngày giờ dùng `DateTimeOffset`, OpenAPI mô tả được payload và error shape của ITS.
4. Viết invariant ở Domain, use case ở Application, adapter/data ở Infrastructure, endpoint mỏng ở Api.
5. Với thay đổi dữ liệu, dùng migration có version, optimistic concurrency và transaction. Không join database service khác.
6. Với thay đổi trạng thái và phát event, dùng Outbox trong cùng transaction. Consumer dùng Inbox/idempotency và chỉ commit offset sau khi commit nghiệp vụ.
7. Với danh mục, dùng cache key có service/table/query/scope/culture; invalidation sau commit và có retry qua Outbox.
8. Kiểm tra response `isOk`, `result`, `errorMessages`, `warningMessages`, `traceId`, HTTP status và bản địa hóa.

Không áp dụng cứng một cấu hình JSON nghiêm ngặt hoặc quy ước enum nếu API hiện tại đã có client phụ thuộc; thay đổi serialization là contract change, cần compatibility check/ADR. API mới có thể áp dụng quy tắc chặt hơn khi đã được chốt và có contract test.

## Threat model trước API và tích hợp

Trước khi triển khai endpoint, file upload, webhook, message consumer hoặc tích hợp ngoài, lập nhanh các ranh giới tin cậy và abuse case:

- HTTP input, file, webhook, queue payload, provider response và dữ liệu từ browser đều là dữ liệu không tin cậy; xác định tài sản cần bảo vệ như credential, PII, quyền quản trị và dữ liệu khảo sát.
- Kiểm tra spoofing, tampering, repudiation, disclosure, denial of service và elevation of privilege; liên kết mỗi abuse case với test đầu tiên và control tương ứng.
- Validate ở server, parameterize query, encode output, giới hạn kích thước/thời gian, kiểm tra authorization trên resource/scope cụ thể và ghi audit/security event có correlation ID.
- Không ghi secret/token/PII dư thừa; không dùng client-side validation, UI ẩn nút hoặc username để thay authorization server.
- Khi thay đổi auth, CORS, file upload, rate limit, external integration hoặc quyền cao hơn, dừng tại decision request/approval theo `AGENTS.md`; không tự nới boundary để làm local chạy được.

## Bảo mật và vận hành

Auth dùng policy/permission handler; mặc định deny. Không bypass quyền theo username. Token, Data Protection key, provider secret và connection string nằm ngoài source/image. API có HTTPS/forwarded headers đúng proxy, rate limit, timeout, health check, structured logging và OpenTelemetry.

Dùng `IHttpClientFactory`, cancellation token và retry có giới hạn chỉ cho lỗi tạm thời/idempotent. DbContext scoped theo request/job; worker tạo scope cho dependency scoped. Health endpoint tách liveness và readiness.

## Kiểm chứng

Chạy architecture test cho dependency, unit test cho invariant, integration test với PostgreSQL/Kafka/Redis phù hợp, contract test cho OpenAPI/event và smoke test endpoint/auth. Không dùng EF InMemory để kết luận transaction PostgreSQL. Ghi lệnh, môi trường, commit/version, kết quả và giới hạn vào pull request.
