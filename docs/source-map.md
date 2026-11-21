# Bản đồ nguồn và phần biên tập

Các file chụp nguyên bản và hash được liệt kê đầy đủ trong [manifest](../sources/manifest.json). Nguồn chỉ tham khảo để biên tập được ghi riêng bên dưới. Tên `ITS/PBC/UND` chỉ nguồn nội dung, không làm scope thực thi của skill chung.

| Skill dùng chung | Nguồn chính trong `.agents/skills/` của cả ITS/PBC | Điều chỉnh |
| --- | --- | --- |
| delivery-planning | `its-delivery-planning`, `pbc-delivery-planning` | Giữ slice, owner, acceptance, finding; bỏ intake/KPI/registry cố định |
| dotnet-clean-architecture | `its-dotnet-clean-architecture`, `pbc-dotnet-clean-architecture` | Giữ ranh giới, DTO, DB đúng môi trường; kiến trúc phân tán/monolith tùy baseline |
| react-typescript-vite | `its-react-typescript-vite`, `pbc-react-typescript-vite` | Giữ state, race, scope, typecheck; bỏ version/component/ngôn ngữ bắt buộc |
| ui-design-system | `its-ui-design-system`, `pbc-ui-design-system` | Giữ semantics, component, a11y; thương hiệu/GRID/RFC ở profile |
| qa-test-design | `its-qa-test-design`, `pbc-qa-test-design` | Giữ oracle độc lập, traceability, ca âm; ví dụ nghiệp vụ ở nguồn |
| qc-independent-verification | `its-qc-independent-verification`, `pbc-qc-independent-verification` | Giữ candidate/evidence/retest; không tự cấp vai trò hoặc spawn đội |
| application-security | `its-application-security`, `pbc-application-security` và references | Viết lại playbook độc lập, giữ scope, đường dữ liệu và mức độ bằng chứng |
| platform-release | `its-platform-release`, `pbc-platform-release` | Giữ migration/rollback/restore; bỏ launcher và topology riêng |
| user-documentation | `its-user-documentation`, `pbc-user-documentation` | Giữ hướng dẫn theo vai trò/build và walkthrough; không cần mẫu ngoài package |

Reference CRAFT biên tập từ `ITS:docs/design/UI_Craft_Checklist.md`, phương pháp chín nhóm có nguồn unslop; bổ sung sáu nhóm kiểm chứng, bỏ liên kết tới quy định nội bộ ITS. Xem [attribution](../THIRD_PARTY_NOTICES.md).

Giữ nguyên tại snapshot: `its`, `its-employment-business-analysis`, `its-survey-data-reporting`, adapter `.claude/skills/its`, `pbc`, `pbc-ruflo`. Không đổi tên rồi nhận rằng các router/skill chuyên ngành này đã độc lập với tài liệu gốc.

## Đóng góp UND — 0.2.0

Nguồn UND được chụp từ workspace ngoài Git ngày 19/11/2026; có SHA-256 từng file,
không có commit nguồn. Không dùng HEAD BE/FE/Media để gắn lịch sử không tồn tại.

| Package và version | Nguồn trong `sources/und/.agents/skills/` | Phần biên tập và tình huống thử |
| --- | --- | --- |
| react-typescript-vite 1.1.0 | `und-form-ergonomics/SKILL.md` | [Form reference](../skills/react-typescript-vite/references/form-ergonomics.md): IME, delimiter, Tab, draft/actor và response save trễ |
| staging-review-ux 1.0.0 | `und-staging-review-ux/SKILL.md` | [Skill](../skills/staging-review-ux/SKILL.md): summary/detail, revision, selection/count, commit theo contract; bỏ màu/ngưỡng/component cố định |
| office-import-export 1.0.0 | `openxml-office-document/SKILL.md` | [Skill](../skills/office-import-export/SKILL.md) và [fixture contract](../skills/office-import-export/references/fixture-contract.md): giữ nguồn/fidelity/limits/side effect; bỏ loại câu hỏi, template và số liệu riêng UND |
| dotnet-clean-architecture 1.1.0 | `efcore-dapper-hybrid/SKILL.md` | [Hybrid reference](../skills/dotnet-clean-architecture/references/efcore-dapper-hybrid.md): connection/transaction ownership, retry, mapping; không bắt dùng Dapper/CQRS hay luật SP/view UND |
| qc-independent-verification 1.1.0 | `und-qa-qc/references/execution-evidence.md` | [Runner reference](../skills/qc-independent-verification/references/runner-reliability.md): assertion sai, report mới và exit ngoài cùng; không nhập retry limit/DEV policy UND |

Tên hook/component, endpoint, ngưỡng duplicate, quyền DEV, test IDs và quyết định
STT-01 giữ tại UND; [profile](../profiles/und.md) ghi ranh giới và xung đột tên khi
tiếp nhận. Tình huống expected trong package chưa phải evidence pilot tại UND.

## Quy trình dùng chung — 0.3.0

Theo phạm vi chủ dự án chốt ngày 20/11/2026, chỉ giữ quy trình, phương pháp kiểm chứng và quy định kỹ thuật chung. Không đóng gói nghiệp vụ, kể cả ví dụ khảo sát đã đổi tên thành dữ liệu hư cấu. Không tạo package Data hoặc cơ chế ledger/KPI mới.

| Package và version | Nguồn và phần giữ | Phần bỏ hoặc giữ tại dự án |
| --- | --- | --- |
| requirements-analysis 1.0.0 | [BA nguồn](../sources/its/.agents/skills/its-employment-business-analysis/SKILL.md): vị trí nguồn, đối chiếu mâu thuẫn, làm rõ theo scope và truy vết acceptance | Biểu mẫu, actor/chức danh cố định, luồng duyệt, trường/điều kiện nghiệp vụ và cơ chế PM của ITS |
| qa-test-design 1.1.0 | [Data nguồn](../sources/its/.agents/skills/its-survey-data-reporting/SKILL.md) và [metric reference](../sources/its/.agents/skills/its-survey-data-reporting/references/metric-specification.md): căn cứ cùng dữ liệu/scope, expected độc lập, lần theo sai lệch | Công thức, lựa chọn mẫu số, quy tắc missing/dedup, khoảng/đa lựa chọn và dataset khảo sát |
| react-typescript-vite 1.2.0 | Nguồn điều hướng bổ sung ở bảng dưới: xác định contract state, mapping, vòng đời và kiểm trước khi query | Thứ tự ưu tiên state, UX/GRID, route, store và cách chia sẻ tab cố định của ITS |
| qc-independent-verification 1.2.0 | Nguồn KPI/handoff bổ sung: inventory checks, binding evidence, giữ kết quả thiếu và giới hạn hash | Điểm/trọng số, ngưỡng KPI, ledger vai trò, evaluator, quyền phê duyệt và số vòng retry |
| platform-release 1.1.0 | Nguồn branching/handoff bổ sung: nhận diện worktree/ref, bảo toàn thay đổi, kiểm remote drift và hậu kiểm | Topology nhánh, prefix theo vai trò, đường dẫn, script, launcher và chính sách release ITS |
| ui-design-system 1.0.1 | Đối chiếu quy tắc xử lý kết quả chưa rõ đã có trong staging review và form ergonomics | Không thay chính sách hủy ở server; chỉ làm rõ hủy UI không chứng minh rollback |

BA/Data và metric reference đã có trong snapshot ITS commit `80a4f57de21e4bde3cd33fd5d393773703b7eb3e`; bytes còn khớp khi đối chiếu ITS commit mới bên dưới. Giữ nguyên commit và hash lịch sử trong manifest.

Các tài liệu bổ sung chỉ dùng để chọn phương pháp; không sao chép nguyên bản vào snapshot hoặc package. Nguồn: repository `https://github.com/khaitt-huit/ITS`, commit `18391ce2c01065abc44d5049a434c616778c939c`, đối chiếu ngày 20/11/2026:

| Đường dẫn nguồn tại commit trên | SHA-256 bytes đã đọc |
| --- | --- |
| [docs/architecture/Frontend_Search_Context.md](https://github.com/khaitt-huit/ITS/blob/18391ce2c01065abc44d5049a434c616778c939c/docs/architecture/Frontend_Search_Context.md) | `cee2668a64b0b3b474cd405f19ca0865bd7bd82a2b73ed8cecf8ec14c23bf2eb` |
| [docs/development/role-kpi.md](https://github.com/khaitt-huit/ITS/blob/18391ce2c01065abc44d5049a434c616778c939c/docs/development/role-kpi.md) | `8a45e91cf9b82b3b5c3cfef3e7516a96b1a5e34d275bc7c819e629bef734d2b1` |
| [docs/development/agent-cli-handoff.md](https://github.com/khaitt-huit/ITS/blob/18391ce2c01065abc44d5049a434c616778c939c/docs/development/agent-cli-handoff.md) | `baa9f65fbf3dae0ac1272e5b138c590c94a33b22fffd2537584f594ec663e0d5` |
| [docs/development/branching.md](https://github.com/khaitt-huit/ITS/blob/18391ce2c01065abc44d5049a434c616778c939c/docs/development/branching.md) | `90658690f975291f3c22a541d00d1903b5d44b7f2224c4ca41c8654839077d16` |

Không nhập evaluator/tests governance hoặc báo cáo Git của task thật. References mới mô tả quy trình trung tính, không nhận kết quả thực nghiệm của ITS làm evidence cho package chung. Quyền và attribution tiếp tục theo [notices](../THIRD_PARTY_NOTICES.md).

## Pilot evidence — 0.4.0

Theo yêu cầu chủ dự án ngày 21/11/2026, biên tập từ các quy tắc candidate,
inventory và runner negative control hiện có trong package QA/QC; helper và tests
được viết mới cho kho chung bằng thư viện chuẩn Python. Không sao chép launcher,
evaluator/KPI hoặc dữ liệu/runner nghiệp vụ từ ITS/PBC/UND.

| Package | Phần bổ sung | Ranh giới |
| --- | --- | --- |
| qa-test-design 1.2.0 | [Acceptance inventory](../skills/qa-test-design/references/acceptance-inventory.md): version/check ID ngoài report và cập nhật plan | Oracle, acceptance và ngoại lệ do dự án quyết định |
| qc-independent-verification 1.3.0 | [Evidence contract/helper](../skills/qc-independent-verification/references/evidence-contract.md): đối chiếu report với acceptance/context/runner và file/hash | Kiểm nhất quán không chứng minh tính đúng đắn hoặc quyền duyệt; không ép commit dirty tree |

Ý tưởng thiết kế môi trường kiểm chứng được đối chiếu với [bài nói Lauren Tan do
AI Engineer công bố](https://www.ai.engineer/code/2026/talks/lauren-tan).
Không nhập slide/transcript hoặc coi số PR/revert được báo cáo là kết quả của kho.
Giữ nguyên snapshot và attribution trước đó. [Pilot](evidence-pilot.md) phân biệt
kiểm helper với kết quả sử dụng thực tế tại dự án.
