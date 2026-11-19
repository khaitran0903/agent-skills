---
name: its
description: Nhận câu gọi ITS và chọn vai trò trong dự án ITS; dùng quy ước và skill chuẩn của repository.
---

# ITS — adapter skill cho Claude Code

Đọc AGENTS/task ở root. Worker giữ owner_role, chỉ nạp mục role/skill được giao.
Vấn đề mới dùng [skill chuẩn its](../../../.agents/skills/its/SKILL.md); policy và
nguồn đọc tiếp theo bảng AGENTS, không nạp toàn intake/KPI/runner cho worker.
Mọi đường dẫn đọc tiếp trong skill chuẩn được tính từ vị trí file chuẩn đó.
