# Thay đổi

## 0.4.0 — 2026-11-21

- Nâng `qc-independent-verification` lên `1.3.0`: thêm evidence contract và helper Python đi cùng package; đối chiếu report với acceptance/context ngoài report, observation của runner và artifact/hash. Tách report hợp lệ khỏi acceptance đạt; không chạy command trong report hoặc tự cấp quyền phát hành.
- Nâng `qa-test-design` lên `1.2.0`: giữ inventory acceptance có version bên ngoài report, oracle độc lập và cập nhật plan khi contract đổi. Ca chưa chạy giữ Not Run.
- Sửa tình huống QC mới trên upstream: dirty candidate có snapshot/diff định danh vẫn kiểm được; không buộc commit/revert thay đổi có sẵn hoặc nhận static/mock là runtime.
- Thêm kiểm thử subprocess/negative controls cho helper, chạy từ bản package sao chép độc lập. Kiểm thiếu check, zero/skipped tests, report cũ, sai candidate, timeout, exit bị nuốt và artifact bị thay đổi; từ chối field acceptance lạ thay vì âm thầm bỏ ràng buộc bị viết sai tên.
- Giữ định dạng lock, lệnh sync và 60 file snapshot nguồn; không áp luật tên tiêu đề hoặc field frontmatter mới. Ghi giới hạn pilot và việc tích hợp/thử hành vi tại dự án còn cần làm.
- Sửa ví dụ output sync trong README cho khớp công cụ và đóng code fence đúng.

## 0.3.0 — 2026-11-20

- Chốt phạm vi chỉ gồm quy trình, phương pháp kiểm chứng và quy định kỹ thuật dùng chung; nghiệp vụ riêng và ca minh họa nghiệp vụ giữ tại dự án. Không thêm package Data, ledger/KPI, evaluator hay script Git từ ITS.
- Thêm `requirements-analysis` `1.0.0`: đối chiếu nguồn, phân biệt yêu cầu/diễn giải/đề xuất, xử lý mâu thuẫn và truy vết acceptance theo phạm vi.
- Nâng `qa-test-design` lên `1.1.0` với reference đối soát kết quả; `react-typescript-vite` lên `1.2.0` với reference state khi điều hướng; `platform-release` lên `1.1.0` với reference tích hợp Git qua worktrees.
- Nâng `qc-independent-verification` lên `1.2.0`: đối chiếu danh sách acceptance/checks, kiểm phạm vi evidence dùng lại và giới hạn hash, theo policy của dự án.
- Sửa diễn đạt hủy form trong `ui-design-system` `1.0.1`: hủy chờ/đóng form không chứng minh rollback request đã gửi.
- References nằm trong từng package, không tạo dependency tới package khác. Giữ nguyên 60 file snapshot, manifest, định dạng lock và công cụ sync; ghi nguồn tham khảo bổ sung cùng phần giữ/bỏ trong source map.

## 0.2.0 — 2026-11-19

- Tiếp nhận 5 file skill/reference UND dưới dạng snapshot workspace nguyên byte, SHA-256 và provenance không có Git commit; giữ 55 file ITS/PBC đã chụp.
- Thêm `staging-review-ux` và `office-import-export` version `1.0.0`; package Office có 5 fixture hư cấu DOCX/XLSX/input lỗi kèm expected và hash.
- Nâng `react-typescript-vite`, `dotnet-clean-architecture`, `qc-independent-verification` lên `1.1.0`: references form ergonomics, EF Core/Dapper và runner negative control.
- Thêm profile UND, nguồn/adaptation và tình huống thử; không nhập ngưỡng nghiệp vụ, component, endpoint hay quyền thực thi UND vào package chung.
- Validator nhận provenance workspace ngoài Git, giữ kiểm hash/inventory và commit của nguồn Git; bổ sung tests cho metadata sai và snapshot bị đổi/thêm.
- Định dạng lock và lệnh sync giữ tương thích. Chưa cài hoặc chuyển đổi skill tại ITS/PBC/UND; cập nhật package tại dự án cần review diff và commit nguồn đã được chốt.

## 0.1.0 — 2026-11-19

- Tập hợp nguyên bản 12 skill ITS, 11 skill PBC và adapter Claude ITS; 55 file có commit và hash nguồn.
- Biên tập 9 skill dùng chung, mỗi skill version `1.0.0`; tách ràng buộc dự án vào profiles/bản đồ nguồn.
- Đưa phương pháp 15 tiêu chí CRAFT vào reference UI độc lập, giữ attribution và mô tả điều chỉnh.
- Thêm catalog, quy trình cập nhật/rollback, công cụ sync xem trước và lock phát hiện thay đổi cục bộ.
- Thêm CI kiểm cấu trúc, hash nguồn và hành vi sync. Chưa chuyển cấu hình hay cập nhật trực tiếp ITS/PBC.
