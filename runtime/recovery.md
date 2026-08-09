# Recovery Protocol

## Triggers

Broken YAML, missing registry, state/snapshot disagreement, stale report, duplicate/invalid ID, unresolved dirty transaction, incomplete state output, or gate/state inconsistency.

## Recovery Order

1. Freeze all forward work and copy no uncertain value into active state.
2. Inventory project files, parseability, versions, manifests, and transaction markers.
3. Select latest internally consistent immutable snapshot.
4. Classify post-snapshot changes as committed, staged, partial, or unknown.
5. Choose `RESTORE`, `REPLAY_VALIDATED_DELTA`, or `MANUAL_RECONSTRUCTION`.
6. For reconstruction, mark every uncertain field `UNKNOWN` and create blocking debt.
7. Validate schemas, references, state/gates, report sync, and integrity.
8. Create recovery snapshot/decision and resume earliest valid state.

## Rules

Reports are not authoritative over registries. File modification time is not proof of commit. Do not discard a dirty transaction until its base snapshot and changed files are identified. Missing evidence cannot be reconstructed from prose as FACT.

## Completion

Recovery completes only when no dirty marker remains, active references resolve, state/gate are legal, reports are synchronized or marked stale, and the next action is explicit.
