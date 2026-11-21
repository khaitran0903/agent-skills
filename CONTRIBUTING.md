# Đóng góp

1. Mô tả trigger và kết quả quan sát: agent đã chọn sai gì, thiếu thông tin gì, tác động nào có bằng chứng. Phân biệt lỗi skill với thiếu cấu hình dự án.
2. Chỉ đưa quy trình, phương pháp kiểm chứng và quy định kỹ thuật tái sử dụng vào `skills/`; nghiệp vụ riêng giữ tại dự án. Sửa skill đang sở hữu quy trình trước; chỉ tạo skill mới khi có trigger/đầu ra độc lập, không tách theo tên vai trò hoặc vì nguồn chưa có package. Thêm reference khi cần đọc có điều kiện và đặt trong chính package. Không buộc dự án nhận CLI, công nghệ phụ hoặc cơ chế duyệt mới từ ví dụ.
3. Bổ sung nguồn và mô tả adaptation trong `catalog.json`/`docs/source-map.md` khi nhập nguồn mới. Kiểm quyền tái sử dụng và giữ attribution. Không nhập credential, dữ liệu nghiệp vụ thật hay cấu hình máy.
4. Tăng version skill theo SemVer và ghi CHANGELOG. Không đồng nhất version skill với version SDK hoặc số release của repo.
5. Chạy validator; thay logic sync hoặc helper thực thi phải chạy tests phù hợp. Với thay đổi hành vi đáng kể, thử một yêu cầu thực tế trong workspace thử, ghi kết quả, công cụ, candidate và giới hạn. Khi sửa đường evidence/report/exit, giữ negative control và lượt pass sau khi bỏ injection; xem [pilot evidence](docs/evidence-pilot.md). Kiểm Markdown/YAML không thay thử hành vi.
6. PR nêu vấn đề, hành vi sau sửa, các skill ảnh hưởng, rủi ro tương thích, kiểm chứng và cách dự án nhận cập nhật. Merge/phát hành theo quyền đã được giao.

Ví dụ/fixture mới dùng nội dung trung tính để thử quy trình hoặc cơ chế kỹ thuật. Không chuyển công thức, điều kiện đủ/loại, luồng duyệt hay ngưỡng nghiệp vụ của nguồn thành mặc định chung; thêm câu “tùy dự án” không làm một kịch bản nghiệp vụ thành quy trình dùng chung. Kiểm cả thiếu đầu vào, nguồn mâu thuẫn và hành vi giữ phạm vi khi có tác động; không tạo bộ kiểm lớn chỉ để khớp câu chữ.

Nếu cải tiến bắt nguồn ở dự án, chọn phần quy trình/quy định dùng chung để đưa lên kho; cải tiến nghiệp vụ tiếp tục ở dự án. Tại dự án nhận, so sánh commit cũ/mới và giữ phần riêng. Không chỉnh snapshot lịch sử để phản ánh bản dùng chung đã biên tập.
