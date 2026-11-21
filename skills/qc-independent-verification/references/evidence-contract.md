# Bản ghi evidence và phép đối chiếu

Đọc khi cần bàn giao evidence có cấu trúc hoặc tích hợp kiểm tính nhất quán vào
runner/CI. Không bắt mọi nhiệm vụ dùng JSON; định dạng và gate của dự án vẫn áp dụng.
[Helper](../scripts/check_evidence.py) dùng Python 3.10+ và thư viện chuẩn, đi cùng
package khi cài riêng. Nó chỉ đọc JSON/artifact, không chạy command trong report.

## Ba đầu vào độc lập và observation của runner

- `contract.json`: acceptance đã chốt ở task/contract/test plan, có version/ID.
  Reviewer giữ inventory bên ngoài report. Tất cả check liệt kê trong contract
  của helper đều bắt buộc Passed; ngoại lệ cần xử lý ở contract theo quyền dự án.
- `context.json`: run ID, candidate và môi trường dự kiến do caller/runner cung cấp.
  Không lấy context bằng cách sao chép identity từ report cần kiểm.
- `report.json`: expected/actual/verdict và artifact do người/agent bàn giao.
- `observations.json`: với check tự động, runner ghi command/cwd, exit thật,
  outcome, inventory thực chạy và artifact. Không điền lại từ lời khai report.

Trong CI, bảo vệ contract/context/observations khỏi sửa bởi công việc đang được
đánh giá theo cơ chế dự án. Nếu cùng một tác giả tự tạo cả bốn đầu vào, kết quả
chỉ kiểm các lời khai khớp nhau; không chứng minh chương trình đã chạy hay oracle đúng.
Hash chỉ ràng buộc bytes. Nhãn browser/runtime cần runner hoặc reviewer xác nhận.
Helper không thay QC độc lập, quyết định tiếp nhận, UAT hoặc quyền phát hành.

## Dạng v1 tối thiểu

Ví dụ sau là dữ liệu hư cấu cho một ca chưa chạy, không phải evidence Passed.

`contract.json`:

```json
{
  "schema_version": 1,
  "contract_id": "sample-contract-v1",
  "checks": [
    {"id": "AC-1", "expected": "The independently specified assertion holds.", "kinds": ["unit"], "execution": "command", "minimum_tests": 1}
  ]
}
```

`context.json`:

```json
{
  "schema_version": 1,
  "run_id": "sample-run-1",
  "candidate": {"revision": "sample-revision", "snapshot": "sample-snapshot"},
  "environment": "sample-isolated-runtime"
}
```

`report.json`:

```json
{
  "schema_version": 1,
  "contract_id": "sample-contract-v1",
  "run_id": "sample-run-1",
  "candidate": {"revision": "sample-revision", "snapshot": "sample-snapshot"},
  "environment": "sample-isolated-runtime",
  "checks": [{
    "id": "AC-1", "kind": "unit", "verdict": "Not Run",
    "expected": "The independently specified assertion holds.",
    "actual": "No execution observed.",
    "reason": "The test environment is not ready.",
    "artifacts": []
  }],
  "limitations": ["Example only; no application was tested."]
}
```

Mỗi check trong contract giữ `expected` có nguồn; report phải giữ đúng giá trị này,
không sửa expected theo actual. Phép so chuỗi chỉ ràng buộc phát biểu đã chốt,
không chứng minh actual đúng hoặc oracle đầy đủ.

Contract `kinds` là tập loại evidence được chấp nhận: dự án chọn tên phân biệt
static/mock/unit/integration/browser/runtime/formal phù hợp. Không tự nâng loại.
`execution` chọn `command` hoặc `manual`. Chỉ check chạy test mới cần
`minimum_tests`; giá trị này là số **passed thực chạy** tối thiểu, không tính skipped.
Số lượng không thay inventory acceptance/check ID hoặc kiểm đúng case/selector.
Command build/lint không bắt buộc có test count. Kết quả manual cần `steps`
là danh sách bước đã quan sát; helper không xác thực ngữ nghĩa của các bước đó.

`candidate.revision` và `candidate.snapshot` là định danh không rỗng, được đối
chiếu chính xác với context ngoài report. Dự án chọn cách tạo snapshot tái hiện
được: commit sạch hoặc digest/tree manifest gồm thay đổi tracked, file mới và
config/fixture cần thiết. HEAD và dòng `git status` không đủ định danh dirty tree.
Ghi branch/status/diff và cách tạo snapshot ở artifact khi cần; không ép commit,
revert hoặc dọn thay đổi của người dùng để được kiểm.

Khi đã chạy, mỗi check ghi `execution` như sau (thay bằng dữ liệu runner thật):

```json
{
  "command": ["python", "checks.py"],
  "cwd": "workspace-relative-or-runner-cwd",
  "exit_code": 0,
  "tests": {"total": 1, "passed": 1, "failed": 0, "skipped": 0}
}
```

`artifacts` là danh sách `{"path": "logs/check.log", "sha256": "<64 lowercase hex>"}`,
đường dẫn tương đối với thư mục truyền qua `--artifacts`. File phải tồn tại và
hash đúng; không dùng đường dẫn tuyệt đối, traversal, symlink/junction.
Passed cần ít nhất một artifact. Not Run/Not Applicable phải có `reason`.
Failed có thể có execution/artifact thất bại; vẫn là report hợp lệ nếu đúng cấu trúc.

`observations.json` có `schema_version`, `run_id`, `candidate`, `environment`
như context và danh sách `checks`. Mỗi observation gồm `id`, `kind`, `execution`
và `artifacts`; `execution` có thêm `outcome`: `completed`, `timeout` hoặc `error`.
Timeout/error có thể có `exit_code: null`. Runner ghi counts từ report parser thật
nếu có; không suy counts từ exit 0 hoặc chuỗi log PASS. Report và observation
phải khớp command/cwd/exit/counts, kind và artifact. Completed cần exit code nguyên.

Helper kiểm lượt chạy hiện tại. Evidence reuse từ candidate/run khác phải được
review delta theo skill; v1 chưa tự chấp nhận reuse, không đổi identity của report
cũ để vượt phép đối chiếu.

## Chạy và đọc kết quả

Từ thư mục dự án sau khi cài package, thay đường dẫn JSON/artifact theo runner:

```powershell
python .agents/skills/qc-independent-verification/scripts/check_evidence.py --contract acceptance.json --context context.json --report report.json --observations observations.json --artifacts evidence
$evidenceExit = $LASTEXITCODE
exit $evidenceExit
```

Manual checks không cần `--observations`. JSON stdout có `report_valid`,
`acceptance_met`, `unmet` (hoặc `errors`) và giới hạn của phép kiểm.

| Exit | Ý nghĩa |
| --- | --- |
| 0 | Cấu trúc và các đối chiếu được khai báo đạt; không phải phê duyệt sản phẩm |
| 1 | Report đúng cấu trúc nhưng thiếu check/Passed/evidence hoặc không khớp context/runner |
| 2 | Input, schema, đường dẫn hoặc I/O không hợp lệ |

Runner/CI phải giữ exit này ra process ngoài cùng. Khi timeout, setup lỗi hoặc
không có test cần chạy, ghi Not Run/Failed trung thực và không dùng report cũ.
Đọc [negative controls](runner-reliability.md) khi thay đường report/exit hoặc
tích hợp helper; giữ cả lượt fail có chủ đích và lượt pass sau khi bỏ injection.
