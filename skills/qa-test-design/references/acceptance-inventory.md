# Inventory acceptance cho bàn giao QA/QC

Đọc khi lập hoặc cập nhật test plan cần đối chiếu với evidence thực chạy.
Nguồn acceptance và oracle được chốt bên ngoài report của implementation.

- Giữ contract/test-plan version và ID ổn định. Truy vết acceptance → check ID →
  input/fixture → expected có nguồn. Thêm ca khi contract đổi; đã có plan không
  có nghĩa công việc QA kết thúc hoặc phải chuyển toàn bộ sang QC.
- Chọn loại evidence và phép kiểm theo claim: static/mock không thay kiểm browser,
  DB hoặc runtime thật. Build/lint không mặc nhiên là test; test count không thay
  danh sách case cần chạy.
- Tách inventory bắt buộc khỏi report kết quả. Đối chiếu cả ca thiếu, Failed,
  Not Run và skipped; không cho report tự bỏ ca rồi tuyên bố scope đầy đủ.
- Ca mới thiết kế giữ Not Run. Không chạy được không phải bằng chứng lỗi sản phẩm
  hoặc Passed. Expected chưa rõ giữ câu hỏi và điều kiện tiếp tục, không lấy
  actual của implementation làm oracle.
- Khi dự án cần kiểm tự động, bàn giao contract gồm version/ID, danh sách check,
  loại evidence chấp nhận, manual/command và số ca thực chạy tối thiểu khi có ý nghĩa.
  Quy tắc ngoại lệ và quyết định tiếp nhận thuộc dự án.

| Tình huống trung tính | Expected quan sát được |
| --- | --- |
| Contract bổ sung một acceptance sau khi plan đã có | Plan được cập nhật và giữ dấu version; ca mới chưa chạy vẫn Not Run |
| Report chỉ có ca thành công, thiếu một check bắt buộc | Đối chiếu inventory phát hiện thiếu; không nhận scope đầy đủ |
| Yêu cầu kiểm browser, dataset chỉ có mock result | Giữ nhãn mock, chỉ ra browser check còn thiếu |
| Expected độc lập khác actual | Giữ oracle có nguồn và sai lệch; không sửa expected để làm pass |

Reference này dùng độc lập để bàn giao test plan; không yêu cầu cài thêm skill,
runner hoặc đổi pipeline dự án.
