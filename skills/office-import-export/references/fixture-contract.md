# Fixture tổng hợp cho pipeline Office

Bộ [expected.json](../assets/fixtures/expected.json) mô tả từng file, SHA-256,
expected và giới hạn. Tất cả nội dung/ảnh do kho này tạo, không lấy dữ liệu thật
UND. Không mở input lỗi bằng Office; đưa qua parser được thử trong môi trường
cô lập. Không extract archive bằng tool không kiểm đường dẫn.

| File | Nội dung và điều phải giữ |
| --- | --- |
| [structured.docx](../assets/fixtures/structured.docx) | Thứ tự paragraph–table–paragraph, bảng lồng, chữ Việt, OMML `x+1`, ảnh PNG qua relationship |
| [typed-cells.xlsx](../assets/fixtures/typed-cells.xlsx) | Sheet `Synthetic`, merged A1:B1, decimal 1.5, text `=1+1` và formula `1+1` có kiểu khác nhau |
| [external-link.docx](../assets/fixtures/external-link.docx) | Relationship ngoài tới domain `.invalid`; không fetch, giữ diagnostic/URL theo policy |
| [traversal.docx](../assets/fixtures/traversal.docx) | ZIP chứa entry `../outside.txt`; reject trước extract, không ghi ngoài vùng xử lý |
| [corrupt.docx](../assets/fixtures/corrupt.docx) | Bytes không phải ZIP; failure có diagnostic, không trả success rỗng |

Template ID `synthetic-office-v1` chỉ là marker thử. Không ép parser dự án phải
nhận schema này; có thể map các facts sang template hư cấu đã được dự án chấp
nhận. Expected mô tả facts của input và invariant, không đặt tên DTO/error code.

Với DOCX, so semantic order và vị trí table/cell, không so nguyên ZIP bytes sau
round-trip. Giữ công thức/source editable hoặc diagnostic unsupported rõ; text
`x+1` đơn thuần không chứng minh OMML được bảo toàn. PNG 1×1 chỉ kiểm extraction/
relationship, không đủ đánh giá chất lượng hình ảnh hoặc bố cục render.

XLSX không có cached formula result; library không có calculation engine không
được hứa recalculate. Phải giữ phân biệt string cell B2 (`=1+1`) và formula cell
B3 (`1+1`) khi đọc/ghi theo contract; không chuyển text thành executable formula.

Kiểm limits bằng cấu hình thấp trên fixture nhỏ hoặc generator thử được phép,
không cần nhập zip bomb. Thêm golden của dự án cho template versions, XLS,
conversion, fonts/layout, count limits, revalidation, idempotency và side effect
ngoài DB khi slice đó được giao. Bộ này chưa bao phủ các trường hợp ấy.
