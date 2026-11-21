---
name: qa-test-design
description: Thiết kế hoặc cập nhật test plan, dataset và expected độc lập từ yêu cầu, contract và rủi ro; dùng trước hoặc trong phát triển, giữ tách biệt thiết kế test với kết quả thực chạy.
---

# Thiết kế kiểm thử

Đọc yêu cầu/contract và quyết định liên quan. Liên kết yêu cầu → acceptance → test ID → dataset → expected → evidence. Phần chưa chốt ghi câu hỏi và tác động, không tự tạo oracle chính thức.

Ưu tiên mất/rò dữ liệu, sai số liệu/tiền, thay đổi sau duyệt, xử lý trùng và lỗi khó phục hồi. Chọn unit cho invariant, integration cho DB/adapter/transaction, contract cho API/event và E2E cho luồng người dùng. Mock không chứng minh hạ tầng thật.

## Chọn ca theo tác động

- Thành công, validation, ranh giới, chuyển trạng thái sai, retry, gửi lặp và concurrency.
- API allow/deny theo actor–permission–resource–scope–state. Sau deny kiểm dữ liệu, side effect và thông tin không được lộ; không chỉ HTTP status.
- Công thức/báo cáo: đơn vị đếm, tử số/mẫu số, distinct/trùng, 0/missing, cutoff/snapshot, ngày hiệu lực, precision/làm tròn. Không lấy output implementation làm đáp án.
- Import/export: định dạng thật được hỗ trợ, mapping, dòng lỗi, trùng, preview và rollback; scope file khớp quyền/màn hình. Kiểm ô văn bản có thể bị ứng dụng bảng tính diễn giải như công thức khi liên quan.
- UI: loading/error/quyền/phiên, filter/paging/sort/selection, draft/pending/response trễ, keyboard/focus/mobile và dữ liệu dài.
- Event/cache/worker: duplicate/restart/retry/invalidation chỉ khi lát cắt tác động, không ép mọi PR chạy toàn hạ tầng.
- Hướng dẫn người dùng: làm lại bước theo đúng vai trò/build, nhánh lỗi và bàn giao khi phạm vi có walkthrough.

Mỗi ca có ID, nguồn/rủi ro, lớp kiểm, tiền điều kiện, actor/scope, dữ liệu, bước, expected quan sát được, cleanup và evidence cần thu. Với UI dùng tiêu chí thiết kế đã chọn; nếu áp CRAFT thì ghi mã tương ứng, không coi regex hay screenshot là phép kiểm mọi hành vi.

Dữ liệu hư cấu/ẩn danh giữ đặc điểm cần kiểm; đồng hồ/ngày kiểm soát được. Expected tính tay hoặc bằng công cụ độc lập, không gọi lại hàm đang kiểm. Không đổi expected để hợp thức hóa lỗi.

Khi lập/cập nhật plan cần bàn giao cho thực kiểm, đọc [inventory acceptance](references/acceptance-inventory.md). Giữ danh sách check và oracle có nguồn bên ngoài report kết quả; đã có plan vẫn cần QA khi contract/coverage đổi. Không tự thêm một vòng QC hoặc yêu cầu thêm skill chỉ để hoàn thành thiết kế test.

Khi cần so kết quả giữa query/API, UI, báo cáo hoặc file xuất, đọc [quy trình đối soát](references/result-reconciliation.md). Định nghĩa và quy tắc tính lấy từ dự án; reference chỉ hướng dẫn chuẩn bị căn cứ và kiểm kết quả.

Bàn giao test plan/dataset/expected và phần thiếu. `Passed` chỉ khi thực chạy đáp ứng expected; `Failed` có sai lệch; `Not Run` khi chưa chạy hoặc bị chặn. Ghi rõ mock/prototype/static/runtime. Ca mới thiết kế giữ Not Run; coverage không chỉ là số test. Finding thiếu oracle/coverage cần hành động hoặc bước làm rõ, owner và điều kiện đóng.

## Tình huống thử

| Trigger/dữ liệu hư cấu | Expected |
| --- | --- |
| Acceptance criterion ghi "hệ thống xử lý đúng" nhưng không nêu giá trị, điều kiện hay tolerance cụ thể | Ghi câu hỏi mở, đánh dấu ca Not Run cho đến khi criterion được làm rõ; không tự suy oracle |
| Expected của ca kiểm công thức tổng được lấy bằng cách gọi lại hàm đang kiểm thay vì tính độc lập | Thay bằng expected tính tay hoặc bằng công cụ độc lập; ghi nguồn oracle; không dùng output implementation làm đáp án |
| Dataset dùng bản sao bảng production chưa ẩn danh; trường định danh cá nhân còn nguyên | Thay bằng dữ liệu hư cấu giữ đặc điểm cần kiểm; ghi rõ nguồn và loại dữ liệu trong evidence |
| Test pass toàn bộ nhưng mock trả cứng HTTP 200 cho mọi đầu vào; adapter thật chưa được kiểm | Phân loại ca là mock-only; không kết luận hạ tầng thật đạt; ghi phạm vi chưa kiểm và ca còn Not Run |
| Công thức báo cáo tỉ lệ chia cho tổng; fixture có dòng tổng bằng 0 và dòng có giá trị null | Expected ghi rõ hành vi cho từng trường hợp 0 và null; ca kiểm riêng hai biên; không để formula lỗi im lặng |

Ghi actual quan sát được, loại môi trường đã dùng (mock, staging, runtime thật) và giới hạn của từng lần chạy. Chưa kiểm trên hạ tầng thật thì không kết luận hành vi production đạt.
