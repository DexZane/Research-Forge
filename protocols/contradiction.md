# Contradiction Protocol

## Types

- `EVIDENCE_CONFLICT`: direct evidence units support opposing claims.
- `PAPER_DISAGREEMENT`: papers reach incompatible bounded conclusions.
- `PAPER_CODE_CONTRADICTION`: implementation differs from described method/config.
- `BENCHMARK_CONFLICT`: dataset, split, metric, or evaluation protocol changes the result.
- `VERSION_CONFLICT`: preprint, proceedings, journal, or code versions differ materially.
- `SCOPE_CONFLICT`: apparent conflict is caused by different conditions.

## Procedure

1. Create `CT-` record; do not overwrite either side.
2. Normalize claims and scopes.
3. Check paper family/version, definitions, metrics, data, controls, and implementation.
4. Assess evidence directness, quality, and independence.
5. Seek discriminating evidence or an R3/R4 read.
6. Resolve as `RECONCILED`, `CONDITIONED`, `SOURCE_ERROR`, `UNRESOLVED`, or `SUPERSEDED`.
7. Downgrade dependent confidence while material conflict remains.

## Reconciliation Rules

Use scope-conditioned claims when both results can hold under different settings. Use source error only with direct verification. “The higher-prestige paper wins” and majority vote are invalid reconciliation methods.

## State Impact

A blocking contradiction prevents the affected threat upgrade, hypothesis lock, project decision, or handoff. A non-blocking contradiction remains visible in the dossier with its scope and risk.

## Paper–Code Rule

Record the exact paper version, repository, commit/release, config, and differing behavior. If feasibility or novelty depends on code reality, require R4 and treat unresolved behavior as `UNKNOWN`.
