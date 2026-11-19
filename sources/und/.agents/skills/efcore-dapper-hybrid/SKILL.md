---
name: efcore-dapper-hybrid
description: Implement and verify UND EF Core runtime/command persistence and Dapper parameterized read models through existing Infrastructure contracts. Use for CQRS data access, shared transactions, SQL Server permission boundaries, and STT-01 migration planning.
---

# UND EF Core and Dapper

## Baseline and boundaries

Read `AGENTS.md`, project rules, approved task design, actual csproj/package
versions, and `../dotnet-clean-architecture/SKILL.md`. Find existing repository,
unit-of-work, connection, and query abstractions before adding anything.
Application handlers orchestrate approved abstractions; concrete DbContext, SQL,
Dapper, and transaction/connection plumbing stay in Infrastructure.
Do not expose DbContext through IApplicationDbContext, call Dapper in a handler,
or scaffold new repositories/interfaces/Result/error codes from a generic example.

STT-01 B-03/A uses EF Core for TEST runtime state and Dapper parameterized reads
for published paper. Other reads may use Dapper or EF projections under the
approved convention. B-04/C forbids all SP/View calls in the target, including
legacy; this task exception overrides generic UND preferences for SP reports.
It does not change other tasks' database rules.

## Query and command implementation

- Use approved Domain methods for invariants and Application for orchestration.
  Infrastructure persists the resulting state, not scoring/approval rules.
- Select explicit columns or projections; use no-tracking for read-only EF entity
  loads when applicable. DTO/scalar projections do not need artificial tracking flags.
- Parameterize values with EF or Dapper. Dynamic identifiers/order clauses require
  approved allowlists, not value parameters or user-input interpolation.
- Apply permission/data-scope predicates in the database query; add paging and a
  deterministic order for lists. Avoid N+1 calls, unbounded exports, and oversized
  paper loads. Define data scope, timeout, query-count and size guards in the plan.
- Preserve null/tenant/legacy mappings, immutable versions, and parent/child order.
  Multi-mapping must match real column aliases/split boundaries and left-join nulls.
- Use cancellation and configured timeouts; dispose owned connections. Do not
  dispose connections borrowed from EF or open another connection inside a
  transaction that is supposed to be atomic.

## Transactions and runtime concurrency

Implement transaction boundaries in Infrastructure through approved contracts.
If EF and Dapper participate in the same approved operation, use the same
connection and transaction. Coordinate rollback, execution-strategy retries, and
idempotency; a retry must not repeat an external side effect.
Do not add Dapper runtime writes or SQL MERGE merely to optimize a load test.

For STT-01, verify duplicate clientEventId, stale/out-of-order sequence,
ack watermark, concurrent submits, and manual-submit/timeout-worker races.
Unique constraints, concurrency control, and server deadlines must enforce the
approved semantics. A plain last-write-wins update or MERGE statement does not
prove exactly-once results or eliminate locks.

## Database and cache ownership

EXAM and TEST share WEB_ORG_EXAM but do not share DbContexts/project dependencies.
TEST uses its designated schema/user and approved read/write grants; never copy
EXAM's migration/admin connection. Published content delivery remains separate
from internal grading-key access and from scoped candidate state.

Invalidate catalog/permission caches after committed mutations. Revocation must
affect the next request. Cache is not the source of truth for answers/results.
Scope cache keys by their actual contract and identity; candidate content cache
must never reuse internal scoring-key objects. Fail-safe cache behavior cannot
serve revoked permissions or unpublished/restricted content.

## Migration and cutover

For mapping, startup migration, rehearsal, or cutover, read
[references/migration-cutover.md](references/migration-cutover.md).
Only EXAM runs startup migration under the approved database lock; TEST does not.
Prepare versioned DB changes according to repository instructions and approved
task artifacts. Do not run DB-changing commands just because this skill is loaded.

## Verification

Use T-016, T-018, T-024, T-037, T-038, T-040, T-045, T-046, T-055, T-057,
T-082, T-083 and other mapped tests as applicable. Check actual SQL Server
transactions, permissions, indexes/plans, and contract parity on an authorized
isolated environment. InMemory/SQLite is not evidence for SQL Server behavior.
Record real build/test commands, performance results, artifacts, and Not Run
limitations; passing a query scan alone does not close a migration/runtime gate.
