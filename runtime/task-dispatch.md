# Task Dispatch Runtime

## Worker Types

`SEARCH`, `READER`, `CODE_VERIFIER`, `ANALYST`, `NOVELTY_ATTACKER`, `HYPOTHESIS_ATTACKER`, `REVIEWER_N`, `REVIEWER_M`, `REVIEWER_E`.

## Dispatch Conditions

Dispatch only if the task is independent, bounded, based on a frozen snapshot, and has a schema/stop condition. Keep global transitions, conflict reconciliation, threat formalization, peeling, gates, and commits with the orchestrator.

## Task Packet & Compact Payload

Dispatch with minimal context (see [templates/worker-task-packet.yaml](../templates/worker-task-packet.yaml)): include task ID/type, decision question, intent, scope/cutoff/exclusions, minimal relevant entity IDs/signatures, exact permitted actions, forbidden global writes, evidence/reading requirements, compact return schema, dependencies, budget, stop/escalation conditions. Never transmit the full state ledger to a subagent.

## Return Contract

Return proposed records, locators, epistemic classes, reading tier, confidence+rationale, duplicate/family candidates, conflicts, coverage limits, unresolved questions, and next-action recommendation. Mark source access failures explicitly.

## Integration

Reject or revalidate stale returns. Normalize IDs/paper families, check primary sources, deduplicate evidence, open contradictions, and stage changes. Never paste worker prose directly into global state.

## Reviewer Independence

Dispatch R_N/R_M/R_E from the same immutable dossier without cross-report visibility. Freeze first passes before meta-review.
