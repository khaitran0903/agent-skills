---
name: und-form-ergonomics
description: Optimize UND form input ergonomics, keyboard workflows, tag/chip inputs, real-time validation, character counters, and unsaved state protection. Use for authoring, editors, and administration screens in React/Vite.
---

# UND Form Ergonomics & Input UX

This skill defines standards and patterns for high-efficiency, ergonomic data entry in UND (Khảo thí & Ngân hàng câu hỏi). Educational authors and teachers frequently enter large volumes of content, multiple question variants, and metadata. Forms must be swift, clear, accessible, and protective against data loss.

## Scope and current decisions

Read AGENTS.md, the assigned task/WP, the current UND.EXAM UI rule and the owning
host's contracts/components first. Patterns below apply when the task and contract
support them; a layout review does not authorize new storage, dependencies, upload
protocols, batch actions or business rules. Reuse the host's auth/dirty-form behavior.

## Core Principles

1. **Protect User Effort (Zero Data Loss):**
   - Track form dirty state accurately using deep comparison or serialized snapshot (`JSON.stringify` or baseline ref).
   - Use `useUnsavedForm` / `canLeaveCurrentView` to intercept navigation, tab switches, and modal closes.
   - Keep the host dirty guard. Add persistent recovery drafts only when assigned with an approved policy for actor/tenant/scope, entity/schema version, TTL, logout/revoke cleanup and stale/conflict handling. A question-ID-only key must not expose another teacher's draft on a shared machine; do not promise zero loss from localStorage alone.

2. **Smart Tag / Chip Input for Lists & Variants:**
   - Never use raw comma-separated text inputs for critical keywords, search tags, or accepted answer variants without structure.
   - Use structured Tag/Chip input:
     * Use delimiters approved for the field/schema. Preserve commas in answer text or decimal values and keep Tab navigation; handle IME composition, paste/edit and accessible removal before committing a token.
     * Press `Backspace` on an empty input to remove the last tag.
     * Trim whitespace automatically and prevent exact duplicate tags.
     * Provide a clear `×` button on each chip for mouse/touch users.

3. **Real-Time Inline Validation & Live Counters:**
   - Display live character counters (`{current} / {max} ký tự`) for bounded fields (codes, titles, short stems).
   - Show validation warnings inline immediately (debounced if checking uniqueness) rather than delaying until submit.
   - When submit fails validation, auto-scroll and focus the first invalid field.

4. **Keyboard-First Workflow & Focus Ergonomics:**
   - When user clicks "+ Thêm phương án" or "+ Thêm câu hỏi con", automatically focus the newly created input.
   - Maintain a predictable `tabindex` order through forms.
   - Support `Escape` to close modal/cancel with unsaved prompt, and `Ctrl + Enter` (or `Cmd + Enter`) to submit primary forms quickly.

5. **Vietnamese Pedagogical Copywriting:**
   - Follow `react-typescript-vite` rules: use clean, natural Vietnamese labels ("Nội dung câu hỏi:", "Từ khóa / biến thể chấp nhận", "Mã môn học").
   - Actionable error feedback: specify field name and exact character limit or rule.
