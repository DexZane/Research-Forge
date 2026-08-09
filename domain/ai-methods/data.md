# Data

## Diagnostic Questions

- Is failure driven by quantity, coverage, quality, label noise, imbalance, duplication, or leakage?
- Does utility vary by sample, class, scale, density, difficulty, or domain?
- Is synthetic data distributionally faithful and independently evaluated?
- Are curriculum/active-selection effects separable from extra compute or tuning?
- Does train/evaluation distribution shift explain the symptom?

## Evidence Targets

Learning/utility curves, controlled subsampling, label audits, subgroup error, duplicate/leak checks, noise intervention, external-data provenance, and matched training steps.

## Confounders

More data often means more optimization steps, broader augmentation, pretrained exposure, or class rebalancing. Match budgets and data lineage.

## Stitching Risks

“Add synthetic data,” “use active learning,” or “apply curriculum” is a method label, not a mechanism. Require a data-property → internal-response → outcome chain and a prediction unique to the connection.
