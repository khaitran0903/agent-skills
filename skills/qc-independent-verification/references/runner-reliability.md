# Kiểm runner có thực sự phát hiện thất bại

Đọc khi thay assertion, selector/wait, wrapper, aggregation hoặc report/exit.
Giữ candidate, fixture và expected có nguồn; sửa harness không được làm yếu
acceptance để biến lỗi sản phẩm thành Passed.

## Negative control trong môi trường thử

1. Chọn một ca nhỏ và deterministic, dùng cùng entrypoint/wrapper/report pipeline
   như lần chạy cần tin cậy. Định danh candidate và cấu hình. Với pipeline có
   nhiều suite, cho một suite fail và một suite pass để kiểm aggregation.
2. Tạo actual sai có chủ đích bằng fixture/stub thử hoặc expected khác ở bản sao
   cô lập. Không gây lỗi dữ liệu live, sửa baseline sản phẩm hay chạy thao tác
   phá hoại để làm negative control.
3. Chạy và kiểm đủ ba quan sát: assertion chỉ ra expected/actual khác nhau;
   report mới ghi đúng case Failed; process ngoài cùng trả native exit khác 0.
   Chỉ log chữ FAIL mà wrapper vẫn exit 0 là runner lỗi.
4. Bỏ fault injection, chạy lại đúng ca để chứng minh có thể Passed. Giữ cả log
   fail và pass; bản runner được dùng tiếp không còn mutation thử.

Report cần thuộc đúng lần chạy (run ID/thời gian/candidate), có inventory ca
được yêu cầu, đã chạy và skipped. Không lấy report cũ sau timeout làm kết quả
mới; zero tests, report thiếu, crash hoặc setup fail không chứng minh ca đạt.
Phân loại lỗi runner riêng và ghi Not Run cho hành vi sản phẩm chưa tới được.

## Qua wrapper/shell

Wrapper phải giữ exit ngay sau process con và trả nó ra process cha, kể cả khi
tee/format log hoặc chạy nhiều suite. Ví dụ PowerShell cho một native command:

```powershell
& python ./checks.py
$checkExit = $LASTEXITCODE
exit $checkExit
```

Thay command theo runner thật; ví dụ không bắt dự án dùng Python. Với nhiều
command, giữ failure của từng command theo policy, không để command pass cuối
che failure trước. PowerShell exception cũng cần đường trả failure; `$?` sau
một lệnh ghi log không thay native exit của process được kiểm.

## Bản ghi tối thiểu cho tình huống thử

| Tình huống hư cấu | Expected cần quan sát |
| --- | --- |
| Fixture trả tổng 101 trong khi oracle là 100 | Assertion fail, report ghi case Failed và exit ngoài cùng khác 0 |
| Suite đầu fail, suite cuối pass | Kết quả tổng vẫn failure |
| Filter sai nên không chạy case được yêu cầu | Không nhận Passed cho scope đó; báo inventory thiếu |
| Process timeout và còn report từ lần trước | Report cũ không được tính; ghi lỗi runner và scope Not Run |
| Bỏ injection, chạy ca tổng 100 | Assertion pass và report mới đúng case; giữ evidence failure trước đó |

Ghi command/cwd, run ID, expected/actual, exit, log/report và giới hạn. Negative
control chứng minh đường phát hiện lỗi đã kiểm, không chứng minh mọi assertion
của bộ test đúng hoặc thay QC độc lập khi dự án yêu cầu phiên khác.
