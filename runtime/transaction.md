# State Transaction Protocol

## Single Writer

Only the orchestrator writes global project state. Use a transaction for every evidence, claim, threat, candidate, hypothesis, experiment, decision, transition, or report change.

## Transaction Stages

1. `VALIDATE`: parse records; validate IDs/enums/locators/references, active research-question/fit pointers, candidate opportunity-signal provenance, gate-critical literature-triage access, implementation-leverage source/revision/license fields, active signature/commitment versions, and worker snapshot.
2. `STAGE`: write proposed delta under transaction ID without changing active pointers.
3. `RECONCILE`: deduplicate paper families/bibliography records/evidence/opportunity signals/component sources and open/resolve contradictions.
4. `PROPAGATE`: compute explicit dependency consequences conservatively, including mandatory invalidation for semantic commitment changes.
5. `INTEGRITY`: run required audits; failures keep transaction staged/aborted.
6. `SNAPSHOT`: create immutable pre-commit snapshot and manifest/checksum.
7. `COMMIT`: atomically replace affected registries/state or use journaled ordered writes; commit a validated BibTeX export only with its registry delta.
8. `SYNCHRONIZE`: update human reports with current IDs/versions.
9. `FINALIZE`: increment versions once, append decision log, clear dirty marker.

## Dirty and Failure Behavior

Set transaction dirty marker before writes. On interruption, do not resume state work; recovery inspects marker and either completes a validated commit or restores the snapshot. Never leave state pointing to records not committed.

## Propagation

Invalidate automatically only across `REQUIRES` edges, except for the mandatory commitment-revision dependents defined below. Other dependency types stage human/orchestrator review. Record every changed status and affected report.

## Commitment Revision

Before commit, compare the active and proposed `CM-` records. If bottleneck, operation, changed object, critical condition, core mechanism, differentiating claim, primary predicted contrast, falsifier, or budget assumption changes, require a new commitment version, supersession link, reason, changed-field list, and stale dependent IDs. Invalidate required novelty mappings, hypothesis attacks, diagnostics, falsification plans, feasibility estimates, reviewer reports, and gate packets; route to the earliest affected state. Workers may propose a revision cue but never modify the commitment.

## Researchability Revision

Before commit, compare active and proposed `RQ-`, `FIT-`, `OP-`, and `LT-` records. A material research-question change creates a new `RQ-` version, identifies affected candidates, and rechecks the scope ladder; route to S01 when the minimum discriminating path is no longer viable. An invalidated or weakened verified `OP-` reviews dependent candidates and their novelty/gap claims. A gate-critical `LT-` entry that lacks the required reading tier or access creates blocking reasoning debt and caps the affected gate. Preference or mentorship changes may revise the fit card or scope, but cannot promote a scientific claim.

## Implementation-Leverage Revision

Before commit, compare active and proposed `IL-` plans against the frozen `CM-` commitment. A selected-source revision, license-status change, adaptation delta, or `NEW_MINIMAL` necessity change invalidates affected feasibility estimates, fairness controls, reviewer reports, dossiers, and handoffs. If the change touches the frozen mechanism, diagnostic, primary prediction/metric, or comparison budget, route to the earliest scientific dependency rather than treating it as an implementation-only edit. A worker may propose component evidence but only the orchestrator commits an `IL-` plan.

## Audit Trail

Transaction stores ID, base/new version, timestamp, actor, reason, changed files/IDs, evidence, propagation, integrity result, snapshot, and decision ID.
