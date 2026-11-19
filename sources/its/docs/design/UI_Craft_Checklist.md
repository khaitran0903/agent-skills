# Rà soát chất lượng hình thức và trải nghiệm giao diện ITS

Phiên bản 1.0, ngày 19/11/2026. Chủ dự án đã duyệt việc chọn lọc phương pháp
unslop và các bổ sung trong task `ITS-UI-UNSLOP-20261119`. Áp dụng cho thiết kế,
prototype, sửa UI và review màn hình trong phạm vi task; không xác nhận mọi màn
ITS đã đạt hoặc thay quyết định duyệt thị giác/nghiệp vụ.

## Nguồn chuẩn và phạm vi

- Dùng [Design System](../architecture/Frontend_Design_System.md#its-ui-rule-01),
  [GRID/UX](../architecture/Frontend_Design_System.md#admin-grid-standard),
  [ngữ cảnh tìm kiếm](../architecture/Frontend_Search_Context.md) và
  [chuẩn nội dung](../architecture/Content_Style_Guide.md) làm căn cứ. Checklist này
  bổ sung cách rà và evidence vào [review hiện có](Design_Review.md), không thay
  bảng acceptance hoặc tạo một hệ token/component khác.
- Xác định actor, màn/route, trạng thái, candidate và phần thay đổi. Kiểm source
  component/export và token đang áp dụng; phân biệt giá trị đã duyệt, đề xuất và
  giá trị chỉ đang tồn tại trong code. Không tự chốt font, màu, radius hay thời
  lượng chuyển động mới từ ví dụ của unslop.
- Tái sử dụng `web/src/shared/components/ui` theo `ITS-UI-RULE-01`; thiếu
  control/variant thì theo RFC hiện hành. Không tạo raw table/search/modal riêng
  tại feature để hoàn thành một bản làm đẹp.

## Cách thực hiện

1. Quan sát màn chạy khi có môi trường; lập finding cụ thể với vị trí và ảnh
   trước sửa. Nếu chỉ đọc source, ghi rõ static review và phần runtime Not Run.
2. Nêu ngắn actor/mục tiêu, điều cần cải thiện, component/token dùng lại và hành
   vi phải giữ. Mức chỉnh tương xứng finding; màn tốt chỉ cần chỉnh phần có căn cứ.
   Quyền đã giao trong task đủ rõ thì tiếp tục, không thêm vòng xin duyệt cho
   lựa chọn triển khai thường. Quyết định thiếu đi đúng tuyến AGENTS/RFC.
3. Rà chín nhóm dưới theo thứ tự, chỉ sửa phần có finding trong scope. Kiểm lại
   trạng thái và luồng bị tác động; không đổi nghiệp vụ/API để khớp hình mẫu.
4. Bàn giao kết quả theo mã tiêu chí, finding và evidence trong hồ sơ task hiện
   có. Không lập thêm kho trạng thái hoặc checkbox chung “đã loại AI slop”.

## Chín nhóm rà hình thức

| ID | Nhóm | Điều kiện quan sát/đối chiếu |
| --- | --- | --- |
| CRAFT-01 | Khoảng cách | Dùng scale/token hiện hành; cùng loại control/row có nhịp nhất quán, nhãn và số liệu thẳng hàng; giữ mật độ phù hợp công việc, không tăng khoảng trống làm mất thông tin cần dùng. |
| CRAFT-02 | Màu | Dùng token ngữ nghĩa và nhận diện được áp dụng; giảm hiệu ứng trang trí gây cạnh tranh. Giữ màu lỗi/cảnh báo/thành công, selection, focus và màu chuỗi biểu đồ có nghĩa. Không cấm gradient thương hiệu hoặc palette hợp lệ chỉ vì một xu hướng thẩm mỹ. |
| CRAFT-03 | Icon | Dùng bộ icon hiện có, kích thước/stroke nhất quán theo component; icon thao tác có tên truy cập. Loại emoji trang trí trong UI do hệ thống biên soạn; không sửa dữ liệu người dùng, tên pháp lý hoặc trích dẫn gốc. |
| CRAFT-04 | Câu chữ | Theo CT/COPY; nhãn trực tiếp, phân biệt Lưu/Gửi/Hủy/Đóng và trạng thái pending/kết quả. Rút gọn vẫn giữ hậu quả, phạm vi và nghĩa nghiệp vụ; không tự bỏ thuật ngữ hợp lệ. |
| CRAFT-05 | Kiểu chữ | Giữ font/hierarchy theo nguồn áp dụng; kiểm dấu tiếng Việt, line-height, nhãn dài và số liệu. Không mặc định Inter hay ép mọi tiêu đề về một weight; không giảm chữ để che lỗi bố cục. |
| CRAFT-06 | Bố cục | Dùng đúng Admin/Public shell và component chung; thao tác chính rõ, tìm/lọc/bảng/phân trang giữ vị trí và ngữ nghĩa GRID/UX. Không tự bỏ cột hoặc đổi thứ tự quy trình để màn thoáng hơn. |
| CRAFT-07 | Chi tiết | Radius/border/hover/selected/disabled/focus nhất quán theo component. Chặn style tự phát phá chuẩn tại nơi tiêu thụ; inline style cho giá trị động hoặc implementation component chung được đánh giá theo contract, không tự coi là vi phạm. |
| CRAFT-08 | Hình ảnh và dữ liệu trực quan | Ưu tiên thông tin phục vụ nhiệm vụ; biểu đồ có nhãn, đơn vị và ý nghĩa dữ liệu. Không tạo biểu đồ/số liệu/tính năng chỉ để trang trí. Fixture phải được ghi rõ; không suy ảnh đẹp thành số liệu đúng. |
| CRAFT-09 | Chuyển động | Phản hồi có mục đích, nhất quán với component; tránh chuyển động lặp gây phân tâm. Giữ tín hiệu xử lý cần thiết, hỗ trợ reduced motion khi có hiệu ứng; không ép mọi hiệu ứng vào một khoảng thời lượng mới. |

## Kiểm chứng trải nghiệm và bảo toàn hành vi

| ID | Kiểm tra | Expected/evidence cần có trong phạm vi tác động |
| --- | --- | --- |
| CRAFT-10 | Trợ năng | Thao tác bằng bàn phím, focus nhìn thấy/không bị che, nhãn truy cập, Escape/trap/return focus khi áp dụng; tương phản cặp màu thực tế, nghĩa không chỉ dựa vào màu. Ảnh đơn lẻ hoặc tên token không chứng minh đạt. |
| CRAFT-11 | Responsive và dữ liệu khó | Dùng viewport/zoom/reflow hiện hành; thử tên dài, tiếng Việt, số lớn, bảng nhiều cột. Không tràn toàn trang, cắt mất thao tác hoặc giấu dữ liệu bắt buộc. Kiểm theme/palette bị tác động, không tự mở phạm vi sang mọi tổ hợp không liên quan. |
| CRAFT-12 | Trạng thái | Kiểm loading, empty, no-results, error/retry, disabled/read-only, thiếu quyền/hết phiên theo requirement; trạng thái phân biệt được và có hướng xử lý. Mục không tồn tại trong scope ghi lý do, không tự tạo nghiệp vụ. |
| CRAFT-13 | Bảo toàn thao tác và quyền | So trước/sau lọc/sort/paging/selection, điều hướng/ngữ cảnh, draft chưa lưu, pending/chống gửi lặp, xác nhận và phạm vi hàng loạt theo tác động. UI ẩn nút không chứng minh server đã kiểm quyền; thay đổi quyền/API cần task riêng đúng scope. |
| CRAFT-14 | Nội dung và số liệu | Theo CT/COPY và định nghĩa chỉ tiêu: vi-VN, ngày/giờ/đơn vị, 0 khác thiếu/chưa tải/không áp dụng. Không sửa dữ liệu người dùng hoặc tạo claim thật từ fixture; kiểm nhãn/giá trị trên cả màn và đầu ra bị tác động. |
| CRAFT-15 | Evidence và candidate | Ghi commit và diff/hash nếu dirty, route/actor, dữ liệu fixture/thật được phép, browser/viewport/theme. So trước/sau cùng điều kiện; mỗi expected có actual, đường dẫn evidence và trạng thái. Lệnh thành công không thay bằng chứng thị giác/hành vi. |

## Phân vai, kết quả và bàn giao

UX/UI xác định vấn đề và hướng chỉnh; FE thực hiện bằng component/token chung và
tự kiểm. QA thiết kế case/expected từ yêu cầu trước thực hiện, truy vết mã CRAFT
với UI/GRID/UX/CT/COPY khi liên quan. QC ở phiên độc lập chạy lại ca trọng yếu trên
candidate bàn giao, giữ verdict và finding; PM tiếp nhận đúng phạm vi.

Chọn tiêu chí theo tác động trước kiểm thử. `Passed` cần quan sát/đối chiếu đúng
expected; `Failed` có sai lệch và evidence; `Not Run` khi chưa kiểm chứng;
`Not Applicable` có lý do cụ thể. Tách kết quả static, jsdom, browser và tích hợp;
không nâng chúng thành nhau. Finding theo mức ảnh hưởng và quy trình hiện hành:
mất thông tin/thao tác/quyền/a11y có căn cứ khác với đề nghị thẩm mỹ. Không áp thêm
gate toàn hệ thống cho PR chỉ sửa tài liệu hoặc mở lại nghiệm thu lịch sử.

Dùng bảng trong task/evidence sẵn có, ví dụ:

| ID / lớp kiểm | Expected | Actual / trạng thái | Evidence / candidate | Finding / owner |
| --- | --- | --- | --- | --- |
| CRAFT-… / static, jsdom hoặc browser | Tiêu chí quan sát được | Kết quả thực kiểm | Tham chiếu bản và bằng chứng | ID nếu có |

## Nguồn tham khảo và điều chỉnh

Tham khảo phương pháp audit và chín nhóm rà từ **unslop**, Damir Sokolovsky
([@heydamir](https://x.com/heydamir)),
[commit 620163eedb3529d9cd23a3994ed8d287d06f760d](https://github.com/heydamir/unslop/tree/620163eedb3529d9cd23a3994ed8d287d06f760d),
[license CC BY 4.0](https://github.com/heydamir/unslop/blob/620163eedb3529d9cd23a3994ed8d287d06f760d/LICENSE).
Đã viết lại và bổ sung cho chuẩn ITS theo nội dung chủ dự án duyệt; không nhập
script snapshot/story, asset, installer, workflow sinh ảnh hoặc dependency nguồn.
[Hồ sơ adaptation và kiểm chứng](../development/evidence/its-ui-unslop-adaptation-20261119.md).
