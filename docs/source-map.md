# Bản đồ nguồn và phần biên tập

Các file gốc và hash được liệt kê đầy đủ trong [manifest](../sources/manifest.json). Tên `ITS/PBC/UND` dưới đây chỉ nguồn nội dung, không làm scope thực thi của skill chung.

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
