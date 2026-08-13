# Implementation Leverage Schema

## Implementation-Leverage Plan

Required: `IL-` ID, candidate/frozen commitment IDs and version, decision policy, component records, source-scan provenance, lifecycle, and version.

Each component requires: stable component key, frozen mechanism/diagnostic/baseline/infrastructure role, required capability, decision, audited `considered_sources`, source evidence/debt IDs, fairness impact, and lifecycle/version context. Every considered-source record includes source kind, repository URL, immutable revision/release, component locator/API, declared license identifier, project-recorded license status, verification status/evidence, maintenance/reproducibility limits, and a rejection reason when it is not selected.

## Validity

- `REUSE_AS_IS` and `ADAPT_EXISTING` require a selected source with repository URL, immutable revision/release, component locator, declared license identifier, `LICENSE_COMPATIBLE` status, and verified source evidence. It must also appear in `considered_sources`.
- `ADAPT_EXISTING` records its exact delta and states that it does not change the frozen mechanism, primary metric, or comparison budget. Otherwise request commitment, diagnostic, or fairness revision.
- `NEW_MINIMAL` requires source-scan results, rejection reasons, a minimal interface, necessity tied to the frozen requirement, and an equivalence/ablation control. It cannot be justified by novelty, convenience, style, or familiarity.
- `DEFERRED` leaves execution readiness unresolved and cannot be serialized as a final S18 plan.
- License status records project risk, not legal advice. Unknown, review-required, or incompatible licenses cannot authorize reuse.
- Reused components are implementation provenance, not scientific evidence or innovation claims.
