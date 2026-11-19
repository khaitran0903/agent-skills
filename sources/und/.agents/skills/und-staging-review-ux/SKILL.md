---
name: und-staging-review-ux
description: Guide bulk import staging, two-grid review, error highlighting, inline editing, batch actions, and enterprise pagination in UND React/Vite applications.
---

# UND Staging Review & Batch Operations UX

This skill defines UI/UX standards for handling bulk data intake, import staging (Word/Excel), duplicate deduplication, batch commit, and enterprise table pagination.

## Scope and current decisions

Read AGENTS.md, the assigned task/WP, the current UND.EXAM UI rule and the owning
host's contracts/components first. Patterns below apply when the task and contract
support them; a layout review does not authorize new storage, dependencies, upload
protocols, batch actions or business rules. Reuse the host's auth/dirty-form behavior.

## Core Principles

1. **Two-Grid Review & Conflict Resolution:**
   - Clearly separate the staging batch summary (overall status, file info, item count) from the detailed item review grid.
   - Distinct color-coded badge states for item status: Valid (green), Warning/Duplicate (yellow/orange), Invalid/Syntax error (red), Committed (blue).
   - Provide quick-filter tabs: "Tất cả", "Cần xử lý / Lỗi", "Trùng lặp", "Hợp lệ".

2. **Inline Fast-Fixing & Keyboard Table Navigation:**
   - When staged mutation/validation APIs and task scope permit, allow inline editing directly in the grid or adjacent review drawer without opening separate dialogs.
   - Only expose batch actions already supported by the contract. For selection/delete/revalidation, state the exact scope/count; use measured progress and required confirmation, without inventing an API or workflow.

3. **Enterprise Pagination & Information Density:**
   - Pagination must look polished, balanced, and professional:
     * Informative summary: `Hiển thị 1–20 trong tổng số 150 câu hỏi`.
     * Direct page buttons with active state highlighting (primary brand color, clear contrast).
     * Smart ellipsis (`...`) when total pages > 7 to avoid overwhelming the screen.
     * Previous (`‹ Trang trước`) and Next (`Trang sau ›`) buttons with accessible labels.
     * Graceful fallback when total items = 0 or 1 page.
   - Data tables must have horizontal scroll protection on smaller viewports, sticky table headers for long lists, and clear empty/loading states.
