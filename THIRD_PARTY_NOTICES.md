# Nguồn và quyền tái sử dụng

Repo chưa tuyên bố license chung cho phần nội dung ITS/PBC/UND. Việc tập hợp theo yêu cầu chủ dự án không tự xác lập quyền cấp phép lại toàn bộ nguồn hoặc dependency. Chủ dự án có thể bổ sung LICENSE sau khi chốt phạm vi quyền.

## Đóng góp UND

5 file UND được chủ dự án yêu cầu đưa vào kho chung ngày 19/11/2026; snapshot và SHA-256 ở `sources/und/` và manifest. Đây là capture workspace ngoài Git, không nhận là bản phát hành hoặc commit của các repo con UND. Nội dung đã được biên tập độc lập với nghiệp vụ/endpoint/quyền dự án; chưa gán license mới.

Fixtures ở `skills/office-import-export/assets/fixtures/` là dữ liệu tổng hợp tạo cho kho này, gồm XML, ảnh PNG 1×1 và input lỗi; không sao chép tài liệu nghiệp vụ, font, binary MathType/OLE, macro hoặc asset của UND. Các tên thư viện trong skill chỉ là hướng dẫn lựa chọn, không phân phối kèm thư viện/converter hay suy quyền license của chúng.

## unslop / UI CRAFT

- Tác giả phương pháp nguồn: **Damir Sokolovsky**, [@heydamir](https://x.com/heydamir).
- Nguồn: [unslop tại commit 620163eedb3529d9cd23a3994ed8d287d06f760d](https://github.com/heydamir/unslop/tree/620163eedb3529d9cd23a3994ed8d287d06f760d).
- License được ghi trong hồ sơ nguồn ITS: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), [LICENSE tại commit nguồn](https://github.com/heydamir/unslop/blob/620163eedb3529d9cd23a3994ed8d287d06f760d/LICENSE).
- File liên quan: `sources/its/docs/design/UI_Craft_Checklist.md` và bản biên tập `skills/ui-design-system/references/ui-craft-checklist.md`.
- Thay đổi: viết lại cách audit/chín nhóm rà cho nguồn ITS; thêm sáu nhóm kiểm chứng, candidate và evidence. Bản dùng chung bỏ ràng buộc token/component/CLI và liên kết nội bộ ITS; giữ 15 mã và ý nghĩa kiểm tra. Reference CRAFT dùng chung tiếp tục ghi nhận CC BY 4.0. Không hàm ý tác giả nguồn bảo trợ ITS/PBC hoặc kho này.

Không nhập script, installer, asset hay dependency của unslop. Metadata dẫn nguồn trong snapshot Security được giữ nguyên; nguồn được nhắc tới không tự trở thành dependency được cài hoặc quyền chạy scanner.
