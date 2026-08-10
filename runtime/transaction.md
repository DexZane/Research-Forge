# State Transaction Protocol

## Single Writer

Only the orchestrator writes global project state. Use a transaction for every evidence, claim, threat, candidate, hypothesis, experiment, decision, transition, or report change.

## Transaction Stages

1. `VALIDATE`: parse records; validate IDs/enums/locators/references and worker snapshot.
2. `STAGE`: write proposed delta under transaction ID without changing active pointers.
3. `RECONCILE`: deduplicate paper families/bibliography records/evidence and open/resolve contradictions.
4. `PROPAGATE`: compute explicit dependency consequences conservatively.
5. `INTEGRITY`: run required audits; failures keep transaction staged/aborted.
6. `SNAPSHOT`: create immutable pre-commit snapshot and manifest/checksum.
7. `COMMIT`: atomically replace affected registries/state or use journaled ordered writes; commit a validated BibTeX export only with its registry delta.
8. `SYNCHRONIZE`: update human reports with current IDs/versions.
9. `FINALIZE`: increment versions once, append decision log, clear dirty marker.

## Dirty and Failure Behavior

Set transaction dirty marker before writes. On interruption, do not resume state work; recovery inspects marker and either completes a validated commit or restores the snapshot. Never leave state pointing to records not committed.

## Propagation

Invalidate automatically only across `REQUIRES` edges. Other dependency types stage human/orchestrator review. Record every changed status and affected report.

## Audit Trail

Transaction stores ID, base/new version, timestamp, actor, reason, changed files/IDs, evidence, propagation, integrity result, snapshot, and decision ID.
