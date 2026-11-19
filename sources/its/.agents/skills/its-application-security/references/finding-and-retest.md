# Finding và retest

## Xác minh trước khi phân mức

Ghi claim cụ thể, actor đã có quyền gì, input nào kiểm soát được, đường từ input đến
sink và control trước/sau đó. Phân biệt lỗi thật với hành vi chủ ý theo contract.
Thử bác bỏ claim bằng validation, scope, state và caller constraints thực tế.

`Confirmed` khi evidence chứng minh vi phạm control/contract; nói rõ static hay runtime.
`Suspected` khi còn thiếu điều kiện/đường khai thác; `False Positive` khi có chứng cứ
bác bỏ; `Fixed` chỉ sau retest bản sửa; `Risk Accepted` cần quyết định có thẩm quyền.
Trạng thái finding khác verdict test: `Passed`, `Failed`, `Not Run`. Thiếu môi trường
không đủ để đánh dấu False Positive hoặc Passed. Risk Accepted không đổi test Failed
thành Passed và không miễn acceptance/gate bắt buộc.

Mức Critical/High/Medium/Low dựa trên ảnh hưởng, actor, khả năng thực hiện và phạm vi
dữ liệu thật; ghi căn cứ, không nâng mức chỉ vì tên pattern/scanner. CVSS nếu task yêu
cầu phải có vector và giả định. Bằng chứng tĩnh đủ để xác nhận một số sai lệch, nhưng
không được nhận là đã khai thác runtime.

## Mẫu finding

```markdown
# SEC-<task>-F<sequence>: <hành vi và ảnh hưởng>

- Task / requirement / contract hoặc control có phiên bản:
- Module / owner sửa / người review:
- Candidate: base SHA, candidate SHA, manifest diff chưa commit nếu có:
- Phạm vi và loại evidence: static / test double / runtime:
- Finding status / severity / căn cứ:
- Actor, quyền sẵn có, dữ liệu hư cấu và tiền điều kiện:
- Claim và nguyên nhân: đã xác minh / giả thuyết / chưa biết; căn cứ:
- Đường input → control → sink; file/dòng:
- Bước tái hiện / lệnh / exit code:
- Expected / actual / side effect sau từ chối:
- Evidence đã lọc và giới hạn:
- Hướng sửa / vùng có cùng nguyên nhân / regression cần chạy:
- Điều kiện đóng / bước chẩn đoán và owner nếu chưa biết cách sửa:
- Phương án owner/Dev Lead chọn / delta và evidence tự kiểm trước trình lại:
- Test verdict: Passed / Failed / Not Run:
- Retest: bản sửa, người thực hiện, lệnh/bước, kết quả và ngày UTC:
- Decision Request / quyết định rủi ro / thời hạn xử lý nếu có:
```

Evidence chỉ dùng fixture label, thời điểm tương đối và kết quả. Không đính kèm raw
HTTP/HAR, cookie, token, SID/fingerprint hoặc thông tin cá nhân; lọc trước khi lưu.
PoC vừa đủ chứng minh trên tài nguyên được giao; dừng khi gặp dữ liệu thật ngoài phạm vi.

## Sửa và retest

Security trả finding về Trưởng phòng Dev; owner BE/FE/Platform sửa theo phân công.
Nối hướng sửa, điều kiện đóng và delta vào hồ sơ hiện có theo
[xử lý finding](../../../../docs/development/agent-orchestration.md#finding-resolution).
Retest trên đúng candidate mới và chạy regression cho control/biến thể bị tác động.
Giữ lịch sử Failed và bộ đếm [ba lần chạy task](../../../../docs/development/agent-orchestration.md#blocker-closure) qua các phiên.
Nếu Security cũng viết bản sửa thì phiên khác thực hiện Security retest; QC luôn độc
lập với implementation, QA và Security. Người xác nhận risk acceptance và điều kiện
tiếp nhận theo [quy trình Security](../../../../docs/development/security-review.md).
