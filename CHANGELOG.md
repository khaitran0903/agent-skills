# Thay đổi

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
