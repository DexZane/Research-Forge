# Falsification-Ready Example

## Locked Hypothesis

`HYPOTHESIS`: Under a defined tiny-object O2O setting, candidate coverage may be adequate while instability in selecting the best available candidate explains part of the performance gap.

Alternatives: representation ceiling is low; annotations/metric create apparent instability; recipe/optimization causes both instability and outcome.

## Predictions

- `PR-0001`: candidate ceiling exceeds realized selection on preregistered size/density strata.
- `PR-0002`: selection regret/switch rate relates to outcome under alternative metric operationalizations.
- `PR-0003`: a controlled reliability intervention changes the diagnostic before final task performance.

## Cheapest Killer

Use F0/F1 on existing baseline outputs: compute candidate ceiling, realized selection, regret, switch rate, annotation-quality strata, and an alternative operationalization. Match evaluation and avoid new-method training.

## Pre-registered Logic

- KILL the selection-only project if valid ceiling gap is practically negligible.
- REFINE toward representation if ceiling is low.
- HOLD if hooks or annotation validity prevent measurement.
- GO to a controlled F2 intervention only if the gap is non-trivial, robust to metric/strata checks, and not explained by the strongest alternative.

Any numeric practical threshold is an internal project criterion with rationale, not a universal field fact.
