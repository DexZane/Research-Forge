# Evaluation

## Diagnostic Questions

- Does the task metric measure the hypothesized mechanism or only downstream performance?
- Could benchmark composition, annotations, split, leakage, threshold, or averaging create the effect?
- Are primary strata preregistered and sample sizes adequate?
- What oracle, ceiling, calibration, regret, or subgroup metric exposes mechanism headroom?

## Evidence Targets

Metric definition/implementation, construct validity, alternative metrics, subgroup counts, uncertainty intervals, bootstrap/repeats where appropriate, oracle analysis, failure cases, and cross-benchmark checks.

## Statistical Reporting

Separate exploratory E0 from publication evidence. Report effect size and uncertainty; distinguish biological/data units from technical repeats; control multiple comparisons and model assumptions when claims depend on them.

## Artifacts

Check class/scale/density imbalance, annotation ambiguity, exclusion rules, evaluation code versions, checkpoint selection, and evaluator-model bias.

## Rule

Task improvement does not prove the mechanism. Diagnostic metrics must apply to baselines, have alternative operationalizations, and predict different outcomes under competing hypotheses.
