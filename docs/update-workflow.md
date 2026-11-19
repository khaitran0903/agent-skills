# Nhận nâng cấp và giữ tùy chỉnh

## Vòng cải tiến

1. Dự án phát hiện nhu cầu qua tình huống thật; ghi expected/actual và phần riêng của dự án.
2. Đưa phần có thể tái sử dụng lên `skills/`, cập nhật version/catalog/CHANGELOG và kiểm chứng. Giữ thay đổi nghiệp vụ/CLI/token trong dự án.
3. Review và đưa thay đổi vào commit/release xác định. Dự án nhận chọn commit/tag đã xem, không cập nhật mù từ `main`.
4. Xem diff so với `upstream_commit` trong lock; chạy sync xem trước. Kiểm tiếp tại dự án rồi commit cả skill và lock.

## Lệnh cập nhật

```powershell
# Trong checkout agent-skills sạch, fetch rồi checkout commit/tag muốn nhận
git fetch origin
git switch --detach <commit-or-tag>
python tools/skills.py validate
python tools/skills.py sync --project D:\PROJECT\MyApp
python tools/skills.py sync --project D:\PROJECT\MyApp --apply
git -C D:\PROJECT\MyApp diff -- .agents
```

Mặc định không có `--skill` thì chỉ cập nhật các skill đã nằm trong lock. Lần cài đầu phải chọn `--skill`, có thể lặp cờ. Công cụ không sửa AGENTS/registry, không rename skill dự án, không xóa package khỏi danh sách quản lý và không gọi network/agent CLI. Nếu nguồn có thay đổi chưa commit, sync dừng để commit nguồn trước nhằm truy vết chính xác.

Lock ghi version và commit tiếp nhận riêng từng skill; cập nhật một skill không đổi baseline của skill còn lại. Hash là bytes thực nhận, nên đổi newline cục bộ cũng được báo là chỉnh sửa. Không dùng formatter tự động trên package được quản lý nếu muốn sync trực tiếp.

## Khi có chỉnh sửa cục bộ

Sync kiểm toàn bộ lựa chọn trước ghi; nếu bất kỳ skill có conflict thì dừng tất cả lựa chọn. File thêm, sửa hoặc xóa đều được giữ. Xử lý trong branch/worktree của dự án:

1. Đọc `upstream_commit`/hash cũ từ lock; lấy bản gốc bằng `git show <old-commit>:skills/<name>/<file>` tại kho nguồn.
2. So sánh ba bản: nguồn cũ, bản đang dùng và nguồn mới. Chuyển tùy chỉnh có thể tách ra AGENTS/profile/adapter riêng.
3. Muốn dùng công cụ sync: sau khi đã commit/sao lưu phần riêng, khôi phục package về đúng baseline cũ (kể cả file thêm/xóa), chạy lại xem trước rồi apply. Tuyệt đối không sửa hash lock để coi phần riêng là bản nguồn.
4. Nếu cần giữ fork của skill, merge thủ công và duy trì provenance/adaptation riêng ngoài lock do công cụ quản lý; không nhận fork là package nguyên bản. Kiểm các trigger, references và hành vi thật trước tiếp nhận.

Không có `--force`; lock không phải cơ chế tự merge ngữ nghĩa. Lỗi ghi/đĩa hoặc ngắt process có thể để lại trạng thái một phần: kiểm Git diff, phục hồi từ commit dự án rồi thử lại. Chạy sync trong checkout đã lưu thay đổi và chỉ một process tại một thời điểm.

## Rollback

Ưu tiên revert commit tiếp nhận tại dự án để khôi phục đồng thời skill và lock. Khi cần rollback bằng kho nguồn, checkout commit cũ, chạy xem trước rồi apply nếu package không bị chỉnh riêng. Rollback skill không hoàn tác thay đổi code/dữ liệu mà agent đã thực hiện trong các task trước đó.

## Version và release

Repo bắt đầu ở `0.1.0`; từng skill có SemVer riêng trong catalog. Release tương lai nên dùng tag bất biến `vX.Y.Z`, ghi các skill đổi version, breaking changes và hướng dẫn chuyển đổi. Bản đầu chưa tạo tag hoặc tự động đồng bộ vào ITS/PBC.
