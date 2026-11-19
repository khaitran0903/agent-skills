# agent-skills

Kho skill dùng chung được tập hợp từ **ITS**, **PBC** và **UND**, để nâng cấp một nơi và tiếp nhận có kiểm soát ở nhiều dự án. Bản `0.2.0` ngày **19/11/2026** có **11 package**; UND góp 5 phần đã biên tập, gồm 2 package mới và references cho 3 skill hiện có.

| Thành phần | Mục đích |
| --- | --- |
| [`skills/`](skills/) | 11 package có thể cài vào dự án, chia nhóm qua catalog |
| [`catalog.json`](catalog.json) | Version, nhóm và nguồn của từng package |
| [`profiles/`](profiles/) | Ranh giới tùy chỉnh riêng ITS/PBC/UND và mẫu cho dự án mới |
| [`sources/`](sources/README.md) | Snapshot nguyên bản, commit hoặc capture workspace, hash và provenance |
| [`tools/skills.py`](tools/skills.py) | Liệt kê, kiểm tra và cài/cập nhật có phát hiện chỉnh sửa cục bộ |
| [`docs/update-workflow.md`](docs/update-workflow.md) | Quy trình nhận nâng cấp, xử lý xung đột và rollback |

## Bộ dùng chung

| Nhóm | Skill | Dùng khi |
| --- | --- | --- |
| Quy trình | [delivery-planning](skills/delivery-planning/SKILL.md) | Kế hoạch, backlog, finding và bàn giao |
| Quy trình | [qa-test-design](skills/qa-test-design/SKILL.md) | Test plan, dữ liệu và expected độc lập |
| Quy trình | [qc-independent-verification](skills/qc-independent-verification/SKILL.md) | Kiểm chứng candidate, retest, evidence và độ tin cậy runner |
| Quy trình | [user-documentation](skills/user-documentation/SKILL.md) | Hướng dẫn theo vai trò và phiên bản |
| Công nghệ | [dotnet-clean-architecture](skills/dotnet-clean-architecture/SKILL.md) | Backend .NET, ranh giới lớp và EF Core/Dapper |
| Công nghệ | [react-typescript-vite](skills/react-typescript-vite/SKILL.md) | Frontend, contract, state và form ergonomics |
| Công nghệ | [staging-review-ux](skills/staging-review-ux/SKILL.md) | Rà lô import, tái kiểm, selection và batch action |
| Công nghệ | [office-import-export](skills/office-import-export/SKILL.md) | Pipeline Word/Excel, fidelity, giới hạn và staging |
| Công nghệ | [ui-design-system](skills/ui-design-system/SKILL.md) | UI, component và 15 tiêu chí CRAFT |
| Công nghệ | [application-security](skills/application-security/SKILL.md) | Review bảo mật ứng dụng theo scope |
| Công nghệ | [platform-release](skills/platform-release/SKILL.md) | Môi trường, migration, CI và khôi phục |

Skill nghiệp vụ Việc làm/khảo sát, router `its`/`pbc` và `pbc-ruflo` được giữ đầy đủ trong snapshot. Chúng cần tài liệu/runtime dự án gốc, nên chưa được đóng gói thành skill độc lập. Xem [bản đồ nguồn](docs/source-map.md).

Đóng góp UND giữ các luật khảo thí, component, endpoint, quyền DEV và quyết định STT-01 ở [profile UND](profiles/und.md). Package Office có [fixture hư cấu và expected](skills/office-import-export/references/fixture-contract.md); tình huống thử của các phần khác nằm trong reference/skill tương ứng. Đây là dữ liệu và tiêu chí thử, không phải kết quả pilot tại dự án.

## Dùng cho một dự án

Yêu cầu Python 3.10+ và Git. Công cụ chỉ dùng thư viện chuẩn, không tải dependency hay chạy agent CLI.

```powershell
git clone https://github.com/khaitran0903/agent-skills.git D:\PROJECT\agent-skills
cd D:\PROJECT\agent-skills
python tools/skills.py list
python tools/skills.py validate

# Xem trước, chưa ghi file
python tools/skills.py sync --project D:\PROJECT\MyApp --skill delivery-planning --skill ui-design-system
# Cài đúng những skill đã chọn
python tools/skills.py sync --project D:\PROJECT\MyApp --skill delivery-planning --skill ui-design-system --apply
```

Skill được cài vào `<project>/.agents/skills/<name>/`. Lock tại `.agents/agent-skills.lock.json` ghi repository, commit nguồn, version và hash file đã nhận. Commit lock cùng thay đổi dự án. Không chạy hai phiên sync cùng dự án đồng thời.

Khi đã có lock, chạy `sync --project <path>` để xem nâng cấp cho các skill đang quản lý; thêm `--apply` sau khi xem diff. Công cụ từ chối ghi khi phát hiện file đã sửa/xóa/thêm cục bộ, thư mục trùng chưa thuộc lock, hoặc lock không hợp lệ. Không có tùy chọn ép ghi đè. [Quy trình cập nhật](docs/update-workflow.md) hướng dẫn nhận thay đổi bằng review thủ công khi cần.

## Giữ tùy chỉnh riêng

Nghiệp vụ, thương hiệu, kiến trúc đã duyệt, registry CLI/model, quyền và launcher ở dự án sử dụng. Dùng [mẫu profile](profiles/project-template.md), dẫn chiếu từ AGENTS hoặc skill adapter của dự án. Không cài cả bộ snapshot như các skill tự hoạt động. Không thay các skill `its-*`/`pbc-*` đang dùng mà chưa cập nhật registry và kiểm chứng tại dự án đó.

## Đóng góp và lộ trình

Mỗi cải tiến nên xuất phát từ một tình huống thật, đưa phần tái sử dụng vào kho chung và giữ ngoại lệ ở dự án. Đọc [CONTRIBUTING](CONTRIBUTING.md), [CHANGELOG](CHANGELOG.md) và [các đề xuất tiếp theo](docs/roadmap.md). Repo chưa chọn license chung; xem [thông báo nguồn và quyền](THIRD_PARTY_NOTICES.md).
