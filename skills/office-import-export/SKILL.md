---
name: office-import-export
description: Xây dựng hoặc review pipeline import/export Word và Excel với template có version, source location, bảng/media/công thức, kiểm tài nguyên, staging và commit theo contract; không dùng cho việc soạn tài liệu đơn lẻ.
---

# Pipeline import/export Office

Đọc schema/template, scope parser/staging/commit, package và môi trường worker
thực tế. Chỉ làm slice được giao: parser in-memory không tự mở persistence,
upload media, conversion hoặc commit. Giữ thư viện/version/license dự án đã chọn;
Open XML SDK, ClosedXML hay NPOI là lựa chọn theo định dạng và runtime, không
phải dependency bắt buộc của skill.

## Parse có nguồn và giới hạn

Nhận diện actual file type và template version; thiếu/không biết version xử lý
theo contract, không đoán cột, boundary hoặc mặc định nghiệp vụ để nhận Success.
Kiểm quyền và data scope ở boundary tương ứng. Parse có giới hạn vào DTO/staging,
giữ source file checksum, vị trí paragraph/table/cell/sheet/row, raw/normalized
content và diagnostics. Không nuốt item lỗi hoặc ghi đè fatal failure thành Success.

Giới hạn cấu hình cho compressed/decompressed bytes, entry, row/cell, ảnh/công
thức, thời gian và memory; không đưa ngưỡng riêng của một dự án thành mặc định.
Chặn archive traversal, external relationship fetch, DTD/external XML resolution;
không execute macro/OLE. Converter cần cô lập, timeout và cleanup theo lifecycle.

## Fidelity và export

Giữ run/table order, bảng lồng/merged cells, embedded relationships, Unicode,
formula/media source và provenance. `InnerText` của paragraph không đại diện đủ
nội dung; Open XML không phải page renderer, HTML preview không chứng minh
pagination hoặc formula round-trip của Word.

Với OMML/MathType/OLE, phân biệt bảo toàn binary/source với chuyển đổi thành nội
dung editable. Khả năng, license và asset converter phải được xác minh ở môi
trường đích; không giả định có Office/XSL trên máy chủ. Unsupported conversion
cần diagnostic/manual review theo contract, không âm thầm bỏ công thức.

Preview HTML/URL dùng sanitizer của dự án, vẫn giữ editable source tách riêng.
Trên Excel export, untrusted text bắt đầu như formula phải được ghi dưới kiểu
text theo thư viện; chỉ formula được contract chủ động cho phép mới thành formula
cell. Legacy XLS không phải OOXML: chỉ nhận khi parser thật hỗ trợ và có fixture.
Export theo data scope, batching/paging và giới hạn, không load vô hạn.

## Staging và commit khi thuộc scope

Giữ diagnostics/source để sửa rồi tái kiểm đúng revision. Commit toàn lô hay từng
phần, duplicate threshold, override và audit do contract quyết định. Validate lại
quyền, batch state và version ở server; retry dùng operation identity/idempotency
hiện có. Kết quả chưa rõ phải readback trước khi lặp tác động.

DB transaction không undo upload/file-service. Theo lifecycle được thiết kế cho
temporary media, finalize, compensation và orphan cleanup; ghi partial failure
và khả năng khôi phục. Không tự thêm distributed transaction hoặc xóa asset đã
được sử dụng để giả lập rollback.

## Fixtures và evidence

Đọc [contract fixture hư cấu](references/fixture-contract.md) khi thử parser/export
hoặc lập golden cases. Package có DOCX/XLSX và input lỗi cùng expected/hash; đây
là dữ liệu thử, không phải template nghiệp vụ buộc dự án nhận.

So expected với parse output/diagnostics, round-trip source và render khi AC có
layout. Kiểm môi trường worker thật khi tuyên bố conversion/fidelity. Ghi command,
checksum input/output, mất mát/manual review, commit retry/rollback và loại evidence.
Fixture hợp lệ hoặc preview đẹp không chứng minh pipeline ứng dụng đã hoạt động.
