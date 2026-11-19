# 15 tiêu chí CRAFT

Audit trước sửa; giữ dữ liệu, viewport, theme và candidate đủ rõ để so trước/sau. Dùng token/component và contract của dự án sử dụng, không tạo chuẩn thương hiệu mới từ checklist.

| ID | Nội dung | Căn cứ quan sát |
| --- | --- | --- |
| CRAFT-01 | Khoảng cách | Scale/nhịp nhất quán, nhãn và số liệu thẳng hàng; mật độ phù hợp công việc |
| CRAFT-02 | Màu | Token ngữ nghĩa/thương hiệu, focus/selection rõ; không xóa màu trạng thái hay palette hợp lệ |
| CRAFT-03 | Icon | Bộ icon/size/stroke nhất quán, thao tác có tên truy cập; không sửa emoji trong dữ liệu người dùng |
| CRAFT-04 | Câu chữ | Nhãn và Lưu/Gửi/Hủy/Đóng rõ; rút gọn giữ hậu quả, phạm vi và nghĩa nghiệp vụ |
| CRAFT-05 | Kiểu chữ | Hierarchy/font theo dự án, dấu tiếng Việt và nhãn dài; không thu nhỏ chữ để che lỗi layout |
| CRAFT-06 | Bố cục | Shell/component phù hợp actor; tác vụ chính rõ, không bỏ dữ liệu/quy trình để màn thoáng |
| CRAFT-07 | Chi tiết | Border/radius/hover/disabled/focus theo component; style động được xét theo contract |
| CRAFT-08 | Hình và biểu đồ | Phục vụ nhiệm vụ, nhãn/đơn vị đúng; fixture ghi rõ, hình đẹp không chứng minh số liệu đúng |
| CRAFT-09 | Chuyển động | Phản hồi có mục đích, giữ tín hiệu xử lý và reduced motion khi có hiệu ứng |
| CRAFT-10 | Trợ năng | Keyboard, focus, tên truy cập, Escape/trap/return focus, tương phản thực và nghĩa ngoài màu |
| CRAFT-11 | Responsive | Viewport/zoom/reflow, tên dài, số lớn, nhiều cột; không tràn trang hoặc mất thao tác |
| CRAFT-12 | Trạng thái | Loading/empty/no-results/error/retry/read-only/quyền/phiên phân biệt được và có hướng xử lý |
| CRAFT-13 | Bảo toàn hành vi | Filter/sort/paging/selection, context, draft, pending, xác nhận và phạm vi hàng loạt giữ contract |
| CRAFT-14 | Nội dung/số liệu | Locale/ngày/đơn vị đúng, phân biệt 0 với thiếu/chưa tải/không áp dụng; màn và export cùng scope |
| CRAFT-15 | Evidence | Commit/diff, route/actor, dữ liệu, browser/viewport/theme; expected có actual và bằng chứng |

Mỗi mục ghi `Passed`, `Failed`, `Not Run` hoặc `Not Applicable` có lý do. Phân biệt static, jsdom, browser và tích hợp. Không dùng tên token, regex cấm màu/emoji hoặc ảnh đơn lẻ làm oracle toàn diện. Finding về mất dữ liệu/thao tác/quyền/a11y khác đề xuất thẩm mỹ; ghi tác động và owner.

Bảng bàn giao: `ID | lớp kiểm | expected | actual/verdict | evidence/candidate | finding/owner`. QA thiết kế expected, implementation tự kiểm; khi được yêu cầu QC độc lập thì chuyển candidate cho người/phiên khác.

Nguồn: biên tập từ checklist ITS ngày 19/11/2026. Phương pháp audit/chín nhóm đầu tham khảo **unslop**, **Damir Sokolovsky** ([nguồn tại commit 620163eedb3529d9cd23a3994ed8d287d06f760d](https://github.com/heydamir/unslop/tree/620163eedb3529d9cd23a3994ed8d287d06f760d)), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). ITS bổ sung sáu nhóm kiểm chứng; bản này viết gọn, bỏ ràng buộc component/token/CLI riêng ITS. Reference này được cung cấp theo CC BY 4.0; không hàm ý tác giả nguồn bảo trợ dự án.
