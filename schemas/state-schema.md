# Research State Schema

## Required Fields

`project_id`, `schema_version`, `state`, `state_iteration`, `status`, `mode`, `pending_gate`, active/critical ID lists, search status/cutoff, scientific/execution decisions, publication tier, snapshot/transaction pointers, version, and timestamp.

## Legal Forward Transitions

Default forward path is S00→S01→…→S18. G1 is required after S01, G2 after S08, G3 after S12, and G4 after S17. S18 requires explicit G4 GO. Emergency novelty collision may interrupt S09–S18 and freezes forward transitions.

## Rollback

Any state may return to the earliest invalid dependency when a decision record contains `rollback_to`, reason, affected IDs, evidence, and snapshot. Re-entry increments `state_iteration`; it never erases prior outputs. Scope/candidate/hypothesis/boundary changes require delta search.

## Cross-field Invariants

- `WAITING_FOR_GATE` requires non-`NONE` pending gate.
- Pending gate forbids forward state mutation.
- `S18_EXPERIMENT_DOSSIER` requires scientific `GO`, execution not `BLOCKED`, and G4 approval in decision log.
- T4/T5 critical IDs require threat records meeting threat schema.
- Active hypothesis IDs require G3 at or after S13.
- Active candidate IDs resolve to current `IS-` signature and `CM-` commitment records; frozen commitments resolve from S14 onward.
- A semantic commitment revision invalidates dependent novelty mappings, hypothesis/diagnostic/falsification/feasibility records, reviewer reports, and gate packets until they are revalidated.
- `COMPLETE` requires S18 validation and immutable snapshot.
- At S18, `bibliography.export_path` is `exports/references.bib` and the final snapshot records the validated export timestamp, count, and excluded paper IDs.
- State version increments once per committed transaction.

## Recovery

Broken YAML, missing registry, state/snapshot disagreement, or uncommitted transaction sets `RECOVERY_REQUIRED`; runtime recovery decides restore/replay/reconstruct.
