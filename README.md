# agent-skills

[![release](https://img.shields.io/badge/release-0.3.0-blue)](CHANGELOG.md) [![skills](https://img.shields.io/badge/skills-12-green)](catalog.json) [![CI](https://github.com/khaitran0903/agent-skills/actions/workflows/validate.yml/badge.svg)](https://github.com/khaitran0903/agent-skills/actions/workflows/validate.yml) [![Python](https://img.shields.io/badge/python-3.10%2B-blue)](tools/skills.py)

Kho quy trình, phương pháp kiểm chứng và quy định kỹ thuật dùng chung được tập hợp từ **ITS**, **PBC** và **UND**, để nâng cấp một nơi và tiếp nhận có kiểm soát ở nhiều dự án. Bản `0.3.0` ngày **20/11/2026** có **12 package**. Công thức, luồng duyệt và chính sách nghiệp vụ riêng giữ tại dự án sử dụng.

| Thành phần | Mục đích |
| --- | --- |
| [`skills/`](skills/) | 12 package có thể cài vào dự án, chia nhóm qua catalog |
| [`catalog.json`](catalog.json) | Version, nhóm và nguồn của từng package |
| [`profiles/`](profiles/) | Ranh giới tùy chỉnh riêng ITS/PBC/UND và mẫu cho dự án mới |
| [`sources/`](sources/README.md) | Snapshot nguyên bản, commit hoặc capture workspace, hash và provenance |
| [`tools/skills.py`](tools/skills.py) | Liệt kê, kiểm tra và cài/cập nhật có phát hiện chỉnh sửa cục bộ |
| [`docs/update-workflow.md`](docs/update-workflow.md) | Quy trình nhận nâng cấp, xử lý xung đột và rollback |

## Cấu trúc thư mục

```
agent-skills/
├── skills/                          # 12 package cài được vào dự án
│   ├── requirements-analysis/       │   ├── SKILL.md
│   ├── delivery-planning/           │   ├── agents/
│   ├── qa-test-design/              │   └── references/
│   ├── qc-independent-verification/ │
│   ├── user-documentation/          │
│   ├── dotnet-clean-architecture/   │
│   ├── react-typescript-vite/       │
│   ├── staging-review-ux/           │
│   ├── office-import-export/        │
│   ├── ui-design-system/            │
│   ├── application-security/        │
│   └── platform-release/            │
├── catalog.json                     # Version, nhóm, nguồn từng package
├── profiles/                        # Ranh giới ITS / PBC / UND + mẫu dự án mới
│   ├── its.md
│   ├── pbc.md
│   ├── und.md
│   └── project-template.md
├── sources/                         # Snapshot nguyên bản (không cài trực tiếp)
│   ├── its/
│   ├── pbc/
│   └── und/
├── docs/                            # update-workflow, source-map, roadmap
├── tools/
│   └── skills.py                    # CLI: list / validate / sync
├── tests/                           # Unit test cho tools/skills.py
└── .github/workflows/validate.yml   # CI: validate + unittest trên Ubuntu & Windows
```

## Bộ dùng chung

| Nhóm | Skill | Dùng khi |
| --- | --- | --- |
| Quy trình | [requirements-analysis](skills/requirements-analysis/SKILL.md) | Làm rõ nguồn, điểm mâu thuẫn, yêu cầu và acceptance |
| Quy trình | [delivery-planning](skills/delivery-planning/SKILL.md) | Kế hoạch, backlog, finding và bàn giao |
| Quy trình | [qa-test-design](skills/qa-test-design/SKILL.md) | Test plan, expected độc lập và đối soát kết quả theo contract |
| Quy trình | [qc-independent-verification](skills/qc-independent-verification/SKILL.md) | Kiểm chứng candidate, retest, evidence và độ tin cậy runner |
| Quy trình | [user-documentation](skills/user-documentation/SKILL.md) | Hướng dẫn theo vai trò và phiên bản |
| Công nghệ | [dotnet-clean-architecture](skills/dotnet-clean-architecture/SKILL.md) | Backend .NET, ranh giới lớp và EF Core/Dapper |
| Công nghệ | [react-typescript-vite](skills/react-typescript-vite/SKILL.md) | Frontend, contract, điều hướng/state và form ergonomics |
| Công nghệ | [staging-review-ux](skills/staging-review-ux/SKILL.md) | Rà lô import, tái kiểm, selection và batch action |
| Công nghệ | [office-import-export](skills/office-import-export/SKILL.md) | Pipeline Word/Excel, fidelity, giới hạn và staging |
| Công nghệ | [ui-design-system](skills/ui-design-system/SKILL.md) | UI, component và 15 tiêu chí CRAFT |
| Công nghệ | [application-security](skills/application-security/SKILL.md) | Review bảo mật ứng dụng theo scope |
| Công nghệ | [platform-release](skills/platform-release/SKILL.md) | Môi trường, tích hợp Git, migration, CI và khôi phục |

Skill nghiệp vụ và router dự án được giữ trong snapshot lịch sử để truy vết; snapshot không được cài như skill chung. Phần phương pháp phân tích/đối soát đã được chọn lọc ở `0.3.0`; các biểu mẫu, công thức và ca nghiệp vụ tiếp tục thuộc dự án gốc. Xem [bản đồ nguồn](docs/source-map.md).

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

**Ví dụ output sync (xem trước — dry run):**
```
```
\$ python tools/skills.py sync --project <duong-dan-du-an> --skill delivery-planning --skill ui-design-system
```
[DRY RUN] 2 skill(s) selected: delivery-planning, ui-design-system
```
  delivery-planning   v1.0.0  -> install  (not present)
  ui-design-system    v1.0.1  -> install  (not present)
```
No files written. Run with --apply to install.
`
```
**Sau khi thêm --apply:**
```
`
\$ python tools/skills.py sync --project <duong-dan-du-an> --skill delivery-planning --skill ui-design-system --apply
```
  delivery-planning   v1.0.0  OK installed  (3 files)
  ui-design-system    v1.0.1  OK installed  (4 files)
```
Lock written: <duong-dan-du-an>/.agents/agent-skills.lock.json
Commit lock together with your project changes.
`
```
```
Skill được cài vào `<project>/.agents/skills/<name>/`. Lock tại `.agents/agent-skills.lock.json` ghi repository, commit nguồn, version và hash file đã nhận. Commit lock cùng thay đổi dự án. Không chạy hai phiên sync cùng dự án đồng thời.

Khi đã có lock, chạy `sync --project <path>` để xem nâng cấp cho các skill đang quản lý; thêm `--apply` sau khi xem diff. Công cụ từ chối ghi khi phát hiện file đã sửa/xóa/thêm cục bộ, thư mục trùng chưa thuộc lock, hoặc lock không hợp lệ. Không có tùy chọn ép ghi đè. [Quy trình cập nhật](docs/update-workflow.md) hướng dẫn nhận thay đổi bằng review thủ công khi cần.

## Giữ tùy chỉnh riêng

Nghiệp vụ, thương hiệu, kiến trúc đã duyệt, registry CLI/model, quyền và launcher ở dự án sử dụng. Dùng [mẫu profile](profiles/project-template.md), dẫn chiếu từ AGENTS hoặc skill adapter của dự án. Không cài cả bộ snapshot như các skill tự hoạt động. Không thay các skill `its-*`/`pbc-*` đang dùng mà chưa cập nhật registry và kiểm chứng tại dự án đó.

## Đóng góp và lộ trình

Mỗi cải tiến nên xuất phát từ một tình huống thật, đưa phần tái sử dụng vào kho chung và giữ ngoại lệ ở dự án. Đọc [CONTRIBUTING](CONTRIBUTING.md), [CHANGELOG](CHANGELOG.md) và [các đề xuất tiếp theo](docs/roadmap.md). Repo chưa chọn license chung; xem [thông báo nguồn và quyền](THIRD_PARTY_NOTICES.md).
