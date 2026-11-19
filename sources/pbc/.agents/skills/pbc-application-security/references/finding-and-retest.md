# Finding và retest

Ghi claim, actor/quyền sẵn có, input kiểm soát, đường tới sink và control liên quan. Thử bác bỏ bằng validation, scope, state và caller constraints trước phân mức. Phân biệt static evidence với khai thác runtime.

`Confirmed` có bằng chứng vi phạm; `Suspected` còn thiếu điều kiện; `False Positive` có bằng chứng bác bỏ; `Fixed` sau retest; `Risk Accepted` cần quyết định có thẩm quyền. Trạng thái finding khác test verdict `Passed`, `Failed`, `Not Run`. Chấp nhận rủi ro không biến test Failed thành Passed.

Mỗi finding ghi:

- ID, ảnh hưởng/mức độ và căn cứ; requirement/control có phiên bản.
- Base/candidate SHA, diff chưa commit, module và owner.
- Actor, tiền điều kiện, fixture hư cấu, đường input → control → sink với file/dòng.
- Bước/lệnh, expected/actual, side effect, loại evidence và giới hạn.
- Nguyên nhân đã xác minh/giả thuyết/chưa biết và căn cứ, hướng sửa hoặc bước chẩn đoán cụ thể có owner, điều kiện đóng, mốc kiểm và evidence cần thu theo [xử lý chung](../../../../docs/development/agent-orchestration.md#finding-resolution).
- Bản retest, người/phiên kiểm, kết quả và thời điểm.

Không lưu raw HAR/cookie/token hoặc phiếu lương thật vào evidence. PoC vừa đủ trên tài nguyên được giao. Retest đúng bản sửa và regression theo control tác động, giữ lịch sử Failed. Người viết bản sửa không được mô tả tự kiểm là xác minh độc lập; báo rõ nếu chưa có reviewer độc lập.

Trước retest đối chiếu delta và evidence mới đáp ứng phần thiếu. Đề xuất control/test phòng ngừa theo [vòng cải tiến](../../../../docs/development/agent-orchestration.md#improvement-loop); Risk Accepted hoặc một task cải tiến tương lai không thay bằng chứng bản sửa đạt điều kiện đóng.
