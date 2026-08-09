# Rollback Protocol

## Types

- `LOCAL`: discard/revise an uncommitted or isolated bad record.
- `STRUCTURAL`: invalidate a committed dependency and recalculate descendants.
- `SCOPE`: reopen S01 and every affected search/boundary artifact.
- `STATE_REENTRY`: return to earliest state that owns the invalid artifact.

## Procedure

1. Identify trigger evidence/contradiction and affected IDs.
2. Determine earliest invalid dependency, not merely current state.
3. Snapshot current history.
4. Create rollback decision with target, reason, preserved artifacts, and affected outputs.
5. Mark records invalidated/superseded; never delete history.
6. Restore/rebuild active pointers from a valid snapshot plus explicit delta.
7. Increment target state iteration.
8. Run delta search if scope, candidate, hypothesis, threat, or boundary changed.
9. Re-run downstream gates whose inputs changed.

## Typical Routes

- S09/S10 gap disappears → S06.
- S14 cannot measure hypothesis → S11/S13.
- S16 reveals representation alternative → S12.
- Post-GO prior art collision → emergency gate and S09/S10.

Rollback count is not failure. Silent mutation without lineage is failure.
