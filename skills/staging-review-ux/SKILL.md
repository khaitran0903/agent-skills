---
name: staging-review-ux
description: Thiết kế hoặc review giao diện rà lô import, summary/detail, sửa và tái kiểm từng dòng, selection, thao tác hàng loạt và pagination theo contract hiện có.
---

# Rà lô import và thao tác hàng loạt

Đọc task, API/permission, trạng thái batch/item và component của dự án. Skill áp
dụng cho staging review ở nhiều nghiệp vụ; không tự mở scope parser, lưu trữ,
deduplication, API mới hoặc thay luật commit chỉ vì đang sửa layout.

## Summary, detail và trạng thái

Tách thông tin batch (file/version, số dòng, tình trạng, thời điểm kiểm) khỏi
detail từng item và source location. Có thể dùng hai grid, master/detail hoặc
drawer theo host; giữ cùng batch ID và revision, tránh hiển thị summary mới với
detail cũ. Filter lỗi/cảnh báo/trùng/hợp lệ chỉ dùng trạng thái contract hỗ trợ.

Status có chữ/icon và semantics truy cập được; màu theo theme và mức tác động,
không chỉ dùng màu để phân biệt. Cho biết cảnh báo có chặn commit hay cần xử lý
theo policy; không mặc định mọi duplicate đều được bỏ qua hoặc tự merge.

## Sửa, revalidation và response trễ

Chỉ cho inline edit/drawer khi có mutation/validation API và quyền tương ứng.
Giữ draft nếu request fail; chỉ cập nhật kết quả validation cho revision đã kiểm.
Sửa item có thể làm đổi trạng thái, tổng và membership filter: cập nhật theo
response thật, giữ focus/pending rõ và tránh hàng đang sửa biến mất bất ngờ.
Nếu chỉ hỗ trợ xem, chỉ ra source và lỗi để người dùng sửa file rồi nhập lại.

## Selection và batch action

- Nêu rõ chọn trang hiện tại, ID cụ thể hay toàn bộ kết quả lọc; tổng số lấy từ
  server/selection contract. Đổi filter/batch hoặc quyền phải reconcile selection,
  không giữ ID ẩn rồi ngầm mở rộng phạm vi hành động.
- Trước action, hiển thị thao tác/phạm vi/count và confirmation theo mức tác động
  của host. Server kiểm lại scope/revision; pending chống gửi lặp.
- Tiến độ chỉ có phần trăm khi đo được. Timeout/cancel không khẳng định server
  đã rollback; đối soát job/operation ID trước retry. Giữ lỗi theo item nếu API
  có partial result, không báo toàn lô thành công từ HTTP 200.
- Commit toàn lô hay từng phần, duplicate override và audit theo contract dự án.
  UI không tự chuyển lỗi thành warning để bật nút commit.

## Pagination và thao tác bàn phím

Hiển thị khoảng và tổng đúng filter, ví dụ `1–20 / 150`; khi rỗng không ghi `1–0`.
Nếu server không có tổng, dùng next/cursor và nhãn trung thực. Nút trước/sau,
trang hiện tại, page-size và ellipsis theo component; sau xóa/lọc trang cuối cần
chọn trang còn hợp lệ. Sort ổn định ở server khi mô tả toàn tập, không sort riêng
một trang rồi gọi là toàn bộ.

Giữ header/cột nhận dạng trong vùng cuộn khi cần, không để sticky che focus/lỗi.
Hỗ trợ keyboard vào detail, sửa, lưu/hủy, trả focus; loading/empty/error có trạng
thái riêng. Viewport hẹp vẫn đọc được source, lỗi và action chính.

## Tình huống thử

| Trigger/dữ liệu hư cấu | Expected |
| --- | --- |
| Chọn 2 ID ở trang 1, sang trang 2 rồi đổi filter | Nhãn/count/action phản ánh selection policy; không ngầm chọn toàn bộ filter mới |
| Revalidate revision 4 đang chờ thì sửa thành revision 5 | Response revision 4 không đánh revision 5 hợp lệ |
| Batch chỉ có 1 lỗi cuối; contract commit toàn lô | Nêu lỗi chặn; không commit phần hợp lệ và báo cả lô thành công |
| Xóa item cuối trên trang cuối | Trang/tổng cập nhật hợp lệ, không để range ngoài tập dữ liệu |
| Commit timeout nhưng server đã hoàn tất | Đối soát trạng thái operation trước retry; không tạo lô trùng |

Ghi actual với mock/browser/API đã dùng; chưa kiểm API thật thì không kết luận
atomicity, phân quyền hoặc idempotency của backend đạt.
