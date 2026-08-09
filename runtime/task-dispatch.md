# Task Dispatch Runtime

## Worker Types

`SEARCH`, `READER`, `CODE_VERIFIER`, `ANALYST`, `NOVELTY_ATTACKER`, `HYPOTHESIS_ATTACKER`, `REVIEWER_N`, `REVIEWER_M`, `REVIEWER_E`.

## Dispatch Conditions

Dispatch only if the task is independent, bounded, based on a frozen snapshot, and has a schema/stop condition. Keep global transitions, conflict reconciliation, threat formalization, peeling, gates, and commits with the orchestrator.

## Task Packet

Include task ID/type, decision question, intent, scope/cutoff/exclusions, snapshot/version, input IDs, exact permitted actions, forbidden global writes, evidence/reading requirements, output fields, dependencies, budget, stop/escalation conditions.

## Return Contract

Return proposed records, locators, epistemic classes, reading tier, confidence+rationale, duplicate/family candidates, conflicts, coverage limits, unresolved questions, and next-action recommendation. Mark source access failures explicitly.

## Integration

Reject or revalidate stale returns. Normalize IDs/paper families, check primary sources, deduplicate evidence, open contradictions, and stage changes. Never paste worker prose directly into global state.

## Reviewer Independence

Dispatch R_N/R_M/R_E from the same immutable dossier without cross-report visibility. Freeze first passes before meta-review.
