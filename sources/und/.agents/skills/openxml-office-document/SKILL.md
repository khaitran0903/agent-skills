---
name: openxml-office-document
description: Implement or review UND Word/Excel question import/export using Open XML SDK, ClosedXML/NPOI, and staged validation. Use for STT-01 template versions, two-grid review, editable formulas, media extraction, and batch commit/rollback.
---

# STT-01 Office Import and Export

## Baseline and library selection

Read repository instructions, the approved import contract, and
`TASK/STT-01/05-technical-execution-plan.md` / `07-test-plan.md`.
B-07/D selects Open XML SDK, ClosedXML/NPOI, Mammoth preview, and a LibreOffice
worker when needed. Do not add WIRIS/MathType DLLs, Aspose, Syncfusion/Doconut,
or another proprietary replacement to target dependencies without a changed decision.
Check actual package compatibility and licenses before selecting versions.

B-08/B schedules Word/Excel import in P2 and ZIP/bulk media in P3. Single media
upload in the question form still belongs to P2. Use the real approved template/
version schema and all supported question types; a fixed A/B/C/D spreadsheet is
not a universal 15-type parser.

## Scope Parser Core đã được Owner giao

Read the latest decisions in the task plan and WP-P2-IMPORT-01. Parser Core is an
in-memory DTO/parser slice; it does not persist ImportBatch/Item, upload MEDIA,
convert formulas, or implement the staging/UI/atomic commit of IMPORT-02/03.
Do not reopen those gates from Core technical acceptance.

The approved Core contract recognizes v1.0/v2.0/v2.1 and UNKNOWN best-effort;
missing cognitive level is inferred NB with a diagnostic for later review.
Current Owner limits: 10 MB/file, 200 questions, 5 images/question, 3 MB/image;
read the canonical options/plan before changing limits. Keep question boundaries,
nested tables, source location and original MathType/OLE binaries/provenance;
unsupported conversion remains reviewable. Fatal resource failures cannot later
be overwritten as Success. Unknown parsing does not authorize guessed scoring keys.
These decisions are Core-specific; evidence namespace is TC-IMPORT-*, not reused
T-086..088 acceptance from a different task. Latest state/approval remains in plan/WP.

## Staging and commit (only when that dependent scope is opened)

1. Validate caller permissions/subject scope, declared type and actual file content,
   configured size/count limits, template version, and required metadata.
2. Parse in a bounded operation into staging: retain original, source location,
   raw/normalized content, children/answers, formula/media references, and diagnostics.
3. Present two synchronized grids for summary/detail correction. Revalidate edits,
   parent/child structure, scoring schema, subject/bank/chapter/lesson, and media.
4. Run duplicate checks in the same QuestionBank: 100 percent blocks; 90-99 is
   strong warning; 80-89 advisory; approved overrides require reason and audit.
5. Commit only when the entire batch has no blocking errors. Retry must not
   duplicate items, revisions, or media. Use approved atomic commit semantics;
   do not commit just the valid subset while hiding unresolved errors.
6. Record mapping/audit/ownership and rollback batch behavior. Account for media
   external side effects: a DB transaction cannot undo a file-service upload.

Parsing errors must remain reviewable, not silently dropped. Do not guess column
aliases, blank-sheet defaults, or question boundaries; follow versioned templates.
Handle empty/corrupt files, merged cells, Unicode, styles, images, equations, tables,
and legacy XLS differences with golden fixtures.

## Document and formula fidelity

Open XML reads/writes OOXML; it is not a page layout renderer. Mammoth HTML is a
preview, not proof of Word pagination or formula fidelity.
Preserve run/table ordering and embedded relationships; plain paragraph InnerText
alone discards formatting, media, and OMML and cannot prove complete import.

For OMML/MathType/OLE, read `../mathlive-latex-renderer/SKILL.md`.
Verify a converter's provenance, license, distribution availability, and supported
formats before adopting it. Do not assume an Office-installed OMML2MML.XSL exists
or may be redistributed on IIS/Docker. Disable external XML resolution and DTDs;
use vetted conversion assets and golden round-trip evidence.

## Resource and content controls

Use configured limits for compressed/decompressed bytes, entries, rows, formulas,
images, worker runtime, and memory; do not invent a universal 50 MB limit.
Reject archive path traversal and external relationship fetches, avoid executing
embedded macros/OLE, and isolate converter workers. Sanitize preview HTML/URLs
using the approved policy without destroying editable source.
Validate workbook formula handling on export so untrusted text is not emitted as
an executable formula. Preserve explicitly intended formulas under the template.

Route media through the approved UND.MEDIA integration; credentials remain on
the server. Track failures/cancelled batches and cleanup orphan objects according
to the approved lifecycle. Export/report must enforce data scope and bounded
paging/batching, not load all rows or unbounded AdjustToContents scans by default.

## Evidence

Verify T-033, T-034, T-039, T-063, T-064, T-066, T-072, T-073, T-085 as relevant.
Golden DOCX/XLSX/XLS must cover accepted templates, 15-type semantics, media,
Vietnamese fonts, edits/revalidation, formula source preservation, and corrupt/
oversized input. Check approved IIS Windows/Docker Linux worker environments.
Record source checksum, output/round-trip, losses, manual-review disposition,
commit retry/rollback, and actual commands. Do not report parity from preview alone.
