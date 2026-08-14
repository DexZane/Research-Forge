# Baseline Model Profile Schema

## Required Fields

A `BL-` profile contains model identity, selection source/status, task setting, exact configuration, provenance/evidence, fit assessment, known limitations, selection decision, baseline-contract version, lifecycle, and record version.

## Selection Status

- `USER_PROPOSED`: named by the user; not yet verified or selected.
- `DISCOVERED`: found by direction-based search; not yet decision-ready.
- `VERIFIED`: identity and fit evidence are checked; awaiting user selection.
- `SELECTED`: explicitly chosen by the user and locked as the active primary baseline.
- `UNSUITABLE`: fails an explicit fit/access/identity requirement.
- `NOT_SELECTED`: valid option not chosen for this scope.

`selection_source` is `USER_INPUT` or `DIRECTION_SEARCH`. `fit` values are `MATCHED`, `BORDERLINE`, `MISMATCH`, or `UNKNOWN`.

## Validity

- Only one `BL-` profile is active and `SELECTED` at a time.
- A selected profile requires `verification_status: VERIFIED`, non-empty exact model/variant, task/setting, data/evaluation protocol, provenance/evidence, user selection decision, non-`UNKNOWN` fit assessment, and a positive integer baseline-contract version.
- `SELECTED` cannot use `MISMATCH` for task, data, metric, resource, or implementation fit.
- `BORDERLINE` fit requires a visible limitation and G1 rationale; it never becomes an implicit match.
- S02+ candidates reference the active `BL-` ID and state their bounded delta relative to its contract.
- A `BL-` profile is not a `P-` paper record, `IL-` implementation plan, or novelty claim. Its evidence supports identity/configuration/fit only.
