# Pilot evidence QA/QC

Mục tiêu: phát hiện báo cáo thiếu/sai căn cứ trước khi kết luận đạt, đồng thời giữ
skill dùng chung và cài độc lập. Bản `0.4.0` bổ sung phương tiện đối chiếu, không
áp một pipeline, KPI hoặc quyền phê duyệt mới cho ITS/PBC/UND.

## Phạm vi thay đổi

- QA `1.2.0`: [inventory acceptance](../skills/qa-test-design/references/acceptance-inventory.md)
  có version/check ID bên ngoài report; expected có nguồn và ca chưa chạy Not Run.
- QC `1.3.0`: [evidence contract](../skills/qc-independent-verification/references/evidence-contract.md)
  và helper trong package. Chạy được sau khi chỉ cài QC; không cần checkout kho chung.
- [Tests](../tests/test_evidence.py) chạy helper qua subprocess từ package sao chép
  ra thư mục thử. Lỗi assertion và exit được tạo bởi process Python thật;
  report bị biến đổi riêng để kiểm đường đối chiếu với observation.

## Phép kiểm trong repo

| Trường hợp | Kết quả cần giữ |
| --- | --- |
| Run hiện tại, đủ acceptance, artifact đúng | report_valid và acceptance_met cùng true |
| Report trung thực chứa Failed/Not Run | report_valid true, acceptance_met false, exit 1 |
| Report bỏ check bắt buộc | Inventory ngoài report phát hiện thiếu |
| Viết sai tên field acceptance | Từ chối input, không âm thầm bỏ ràng buộc |
| Report khai Passed nhưng process fail | Observation thật chặn; không tin exit do report tự ghi |
| Assertion đầu fail, assertion sau pass, wrapper trả 0 | Inventory failure vẫn chặn |
| Zero tests hoặc toàn skipped | Không đáp ứng minimum_tests của acceptance |
| Run/candidate/environment sai hoặc timeout | Không nhận artifact/report cũ là lần chạy mới |
| Chỉ có mock cho acceptance browser | Không đáp ứng loại evidence |
| Hash/file sai, traversal hoặc cấu trúc input sai | Không được nhận đạt; lỗi input trả exit 2 |
| Dirty candidate có snapshot định danh | Kiểm được mà không buộc commit/revert |
| Static/manual hoặc build không yêu cầu test | Không ép browser/test count ngoài acceptance |
| Bỏ fault injection, chạy lại cùng runner | Có thể pass; negative control trước vẫn có trong log test |

CI hiện có chạy validator và toàn bộ unittest trên Windows/Ubuntu, nên các tests
helper mới đi vào cùng pipeline. Chạy CI thành công vẫn không chứng minh branch
protection đã enforce, app thật đã chạy hoặc agent dùng skill đúng trên mọi task.

## Tiếp nhận và thử tại dự án

1. Review commit/diff và [quy trình sync](update-workflow.md). Chọn QA/QC cần dùng,
   pin commit/tag theo dự án; không sửa hash lock hoặc ghi đè tùy chỉnh.
2. Chọn task nhỏ với acceptance/expected đã chốt. Giữ contract ngoài report;
   caller tạo context, runner giữ observation/exit/report thật. Dùng cơ chế hiện
   có để bảo vệ các đầu vào này khỏi sửa trong cùng công việc bị đánh giá.
3. Tích hợp helper ở cuối runner và truyền exit ra process ngoài cùng. Chạy một
   negative control qua đúng wrapper/report pipeline rồi bỏ injection và chạy lại.
   Không coi observation được agent tự chép từ report là bằng chứng độc lập.
4. So baseline và bản sửa trên task/input tương đương. Ghi version skill,
   candidate/snapshot, model/công cụ, run, oracle, actual/verdict và giới hạn;
   quan sát đúng scope và tập skill phù hợp. Một lần chạy không cho phép suy rộng
   tỷ lệ lỗi; lặp khi cần phân biệt biến thiên.
5. Ghi số Passed thiếu căn cứ, ca bị bỏ, lần làm lại, công sức review và xung đột
   tiếp nhận. Chỉ mở rộng sang skill/dự án khác khi có lợi ích quan sát được.

Task lập/cập nhật plan giữ Not Run cho ca chưa chạy; task QC đánh giá candidate
và evidence. Tự kiểm và QC độc lập được ghi đúng theo quyền/tiêu chí của task.
Không tự tạo thêm agent, đổi CLI/model, merge hoặc deploy từ một file hướng dẫn.

## Trạng thái và giới hạn

Kiểm local ngày 21/11/2026 trên Windows, Python 3.12.10: validator đạt cho 12
package/60 file nguồn; 46 unittest đạt sau khi thêm ca lỗi tên field acceptance.
Candidate helper tại commit `2c03a0a`
đã được cài qua sync vào consumer cô lập. Bốn lượt thử lưu log riêng cho fault
injection, report khai Passed sai, wrapper nuốt exit và lượt bỏ injection; exit
checker lần lượt là `1, 1, 1, 0`, đúng kết quả cần quan sát. Đây là lượt thử
pipeline tổng hợp, không phải kết quả CI remote hoặc kiểm app dự án.

Lượt dùng thử độc lập QA/QC trên package sao chép từ consumer đã kiểm ba bộ
evidence: một bộ khớp, một thiếu acceptance và một sai run ID; helper trả `0, 1, 1`.
QA bàn giao tám ca sản phẩm mới và giữ toàn bộ Not Run vì không có implementation
được giao. Reviewer chỉ tiếp nhận consistency synthetic, không nhận là app đã đạt.
Lượt này dùng helper trước bổ sung guard từ chối field acceptance lạ; guard được
kiểm bằng ca hồi quy riêng và toàn bộ suite. Không suy đây là đánh giá đủ mọi task.

Helper chỉ kiểm cấu trúc và sự nhất quán của các đầu vào được cung cấp. Nó không
phân tích nội dung video/log để chứng minh claim, không xác thực oracle, không
tự tạo snapshot và chưa tự chấp nhận evidence reuse. Chỉ caller/runner/reviewer
của dự án mới xác nhận nguồn, phạm vi và tính đáng tin của observation.

Các ca trong repo dùng dữ liệu trung tính; không phải pilot ứng dụng tại
ITS/PBC/UND. Kết quả lần kiểm cụ thể cần log/candidate tương ứng. Thử áp dụng ở
dự án và đo hiệu quả sử dụng vẫn nằm trong roadmap; không suy từ unit tests rằng
12 skill đã được đánh giá hành vi đầy đủ.
