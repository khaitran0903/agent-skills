---
name: pbc-qa-test-design
description: Thiết kế kiểm thử PBC từ yêu cầu và rủi ro, với dữ liệu và kết quả kỳ vọng độc lập cho công, lương, quyền và nhập xuất Excel.
---

# Thiết kế kiểm thử PBC

Đọc `AGENTS.md`, yêu cầu/contract và phần tài liệu liên quan. Liên kết yêu cầu → acceptance → test ID → dataset → expected → evidence. Phần chưa chốt phải ghi câu hỏi, không tự tạo oracle chính thức.

Ưu tiên sai tiền, mất công, lộ phiếu lương, sửa sau duyệt, xử lý trùng và hành vi khó phục hồi. Chọn unit cho quy tắc, integration cho DB/transaction/import và E2E cho luồng người dùng. Mock không chứng minh hạ tầng thật.

## Nhóm ca theo tác động

- Kỳ lương qua hai tháng; TKB đổi giữa kỳ, ngày thi/nghỉ, lớp chia nhóm, chào cờ và lịch trống có chủ đích.
- Công thực dạy, vắng/dạy thay, sửa tay rồi đồng bộ lại; chạy sinh công hai lần và đồng thời không nhân đôi công.
- Giá có hiệu lực, nhiều giá trong kỳ, ngoại lệ hệ số và phụ cấp, `decimal`/làm tròn; chính sách thuế/BHXH theo hồ sơ được chốt.
- Tính lại lương, khóa/mở lại, xác nhận theo phiên bản, chưa phản hồi/hết hạn, từ chối/duyệt hai cấp và điều chỉnh sau duyệt theo đặc tả.
- API allow/deny theo actor/resource/campus/state; giáo viên A không xem phiếu B qua đổi ID hoặc export. Sau deny kiểm cả dữ liệu và side effect.
- Import `.xls`/`.xlsx`, mapping mơ hồ, trùng, ô công thức, ngày/số sai định dạng, lỗi từng dòng, preview và rollback theo contract. Export đúng template, tổng và scope; xét formula injection ở ô văn bản.
- UI loading/empty/error, hết phiên, filter/page/sort/selection, draft/pending, response trễ, bàn phím và mobile. Hướng dẫn sử dụng phải làm lại được trên đúng bản chạy.

Tính expected bằng phép tính tay hoặc công cụ độc lập, không gọi lại hàm đang kiểm. Mẫu thực tế chỉ dùng tại môi trường được phép; fixture trong Git dùng dữ liệu hư cấu/đã ẩn danh và vẫn giữ đặc điểm cần kiểm.

Mỗi ca ghi actor, tiền điều kiện, dữ liệu, bước, expected quan sát được, cleanup và evidence. Với test âm nêu dữ liệu không được thay đổi/lộ. Ngày và đồng hồ test kiểm soát được, không lệ thuộc ngày máy.

Bàn giao plan/dataset/expected và phần thiếu. `Passed` chỉ khi đã chạy và đạt, `Failed` có sai lệch, `Not Run` khi mới thiết kế hoặc bị chặn. Khi cần QC độc lập, chuyển [skill QC](../pbc-qc-independent-verification/SKILL.md); không đổi expected để hợp thức hóa lỗi.

Finding chỉ rõ case/assertion/dataset/oracle cần bổ sung hoặc bước làm rõ quyết định nghiệp vụ, owner và điều kiện đóng theo [xử lý finding](../../../docs/development/agent-orchestration.md#finding-resolution). Báo cáo theo [ba nhóm](../../../docs/development/agent-cli-quickstart.md#report-checklist); đề xuất coverage/regression từ bài học và [cách kiểm hiệu quả](../../../docs/development/agent-orchestration.md#improvement-loop) trong scope.
