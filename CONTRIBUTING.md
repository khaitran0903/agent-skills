# Đóng góp

1. Mô tả trigger và kết quả quan sát: agent đã chọn sai gì, thiếu thông tin gì, tác động nào có bằng chứng. Phân biệt lỗi skill với thiếu cấu hình dự án.
2. Sửa phần dùng chung trong `skills/`; thêm reference khi cần đọc có điều kiện. Giữ package tự chứa; không buộc dự án nhận CLI, công nghệ phụ hoặc cơ chế duyệt mới từ ví dụ.
3. Bổ sung nguồn và mô tả adaptation trong `catalog.json`/`docs/source-map.md` khi nhập nguồn mới. Kiểm quyền tái sử dụng và giữ attribution. Không nhập credential, dữ liệu nghiệp vụ thật hay cấu hình máy.
4. Tăng version skill theo SemVer và ghi CHANGELOG. Không đồng nhất version skill với version SDK hoặc số release của repo.
5. Chạy validator; thay logic sync phải chạy tests. Với thay đổi hành vi đáng kể, thử một yêu cầu thực tế trong workspace thử, ghi kết quả, công cụ, candidate và giới hạn. Kiểm Markdown/YAML không thay thử hành vi.
6. PR nêu vấn đề, hành vi sau sửa, các skill ảnh hưởng, rủi ro tương thích, kiểm chứng và cách dự án nhận cập nhật. Merge/phát hành theo quyền đã được giao.

Nếu cải tiến bắt nguồn ở dự án, đưa lên kho chung trước; tại dự án nhận, so sánh commit cũ/mới và giữ phần riêng. Không chỉnh snapshot lịch sử để phản ánh bản dùng chung đã biên tập.
