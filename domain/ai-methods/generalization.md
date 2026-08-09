# Generalization

## Diagnostic Questions

- Is failure IID variance, subgroup/long-tail weakness, domain shift, temporal shift, corruption, adversarial sensitivity, or transfer?
- Which invariant/spurious relation changes?
- Are gains broad or confined to one benchmark artifact?
- Does adaptation use target-domain data or extra supervision?

## Evidence Targets

Predefined subgroups, cross-dataset/domain tests, controlled shifts/interventions, robustness curves, calibration, failure taxonomy, and confidence intervals.

## Confounders

External/pretraining exposure, dataset overlap, class mapping, tuning on target, evaluation protocol, and selective reporting.

## Stitching Risks

Do not claim universal generalization from one dataset or one tiny subgroup. State the tested boundary and downgrade broad language.
