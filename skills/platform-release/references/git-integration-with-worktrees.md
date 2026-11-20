# Tích hợp Git khi có nhiều checkout hoặc worktree

Đọc khi được giao tích hợp/đồng bộ nhánh hoặc cập nhật refs trong repository có nhiều task. Giữ remote, topology và chính sách merge của dự án; hướng dẫn này không chọn sẵn tên nhánh, kiểu merge hay quyền phát hành.

## Xác định đầu vào và phạm vi

- Kiểm remote URL, refs local/remote, worktrees và branch đang được checkout. Ghi SHA đầu vào, Git status gồm thay đổi chưa commit và phần công việc được giao.
- Phân biệt yêu cầu đồng bộ refs, tích hợp thay đổi và phát hành sản phẩm. Quyền push/merge đã được giao dùng trong đúng phạm vi đó; không tự mở rộng sang deploy hoặc bỏ required checks.
- Fetch refs cần thiết trước khi chọn candidate. Xem quan hệ lịch sử và diff nội dung; commit còn reachable không chứng minh nội dung của nó vẫn có tác dụng đúng sau tích hợp.

## Chọn và thực hiện thao tác

Chọn fast-forward, merge hoặc cách tích hợp khác theo đồ thị và chính sách được giao. Nếu lịch sử phân kỳ hoặc có conflict, giữ các thay đổi cần bảo toàn, giải quyết trong checkout được sở hữu và kiểm lại phần tác động. Không tự chọn giữ một phía chỉ để hết conflict.

Branch đang được checkout phải được cập nhật qua checkout/worktree phù hợp và rảnh cho thao tác đó. Không sửa ref bên dưới working tree đang dùng, chuyển branch, stash hoặc reset thay đổi của task khác. Với dirty state không tách an toàn được, dùng checkout cô lập từ đúng commit và giữ nguyên nguồn.

Sau tích hợp, kiểm diff, ancestry theo mục tiêu và các checks cần thiết cho thay đổi thực tế. Bản cần push phải được định danh; tránh đẩy thêm commit hoặc ref ngoài scope vì dùng lệnh quá rộng.

## Push và hậu kiểm

1. Trước push, đối chiếu lại đầu remote liên quan. Nếu đã dịch chuyển, fetch và đánh giá lại candidate/khả năng fast-forward; không lặp push mù hoặc force để vượt thay đổi mới.
2. Push refs được giao một cách tường minh. Mặc định giữ lịch sử, không force; viết lại lịch sử chỉ khi được giao rõ phạm vi và có biện pháp bảo vệ tương ứng.
3. Khi cần nhiều refs cùng đổi hoặc cùng giữ nguyên, dùng atomic push nếu remote hỗ trợ. Nếu không hỗ trợ hoặc ruleset chặn, ghi lỗi và trạng thái thực; không âm thầm đổi sang các push rời có thể cập nhật một phần trái yêu cầu.
4. Kiểm đầu remote thực sau thao tác, đối chiếu SHA mong đợi và trạng thái checkout bị tác động. Nếu có cập nhật một phần hoặc kết quả chưa rõ, xác định trạng thái trước khi quyết định bước tiếp; không tự rollback remote hoặc ghi đè task khác.

Bàn giao refs/SHA trước và sau, thao tác/checks thực chạy, thay đổi đã bảo toàn, lỗi và phần chưa hoàn thành. Thành công Git chỉ xác nhận mục tiêu Git đã kiểm; readiness sản phẩm vẫn theo acceptance/checks và quyền của dự án.
