# Bản đồ nguồn và phần biên tập

Các file gốc và hash được liệt kê đầy đủ trong [manifest](../sources/manifest.json). Tên `ITS/PBC` dưới đây chỉ nguồn nội dung, không làm scope thực thi của skill chung.

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
