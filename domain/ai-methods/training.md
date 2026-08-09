# Training

## Diagnostic Questions

- Is the claimed effect due to curriculum, augmentation, supervision, distillation, regularization, schedule, or simply more steps/tuning?
- Which training-time mechanism changes an inference-time behavior?
- Is the recipe robust across seeds and baselines?
- Does the intervention preserve data and compute budgets?

## Evidence Targets

Matched-step curves, component schedules, intervention timing, seed variation, gradient/feature diagnostics, equal tuning budget, and inference-only evaluation.

## Confounders

Hidden preprocessing, checkpoint selection, teacher/external data, augmentation strength, regularization, precision, and hyperparameter search.

## Stitching Risks

A recipe difference is implementation novelty unless it tests a distinct mechanism hypothesis and produces a discriminating prediction.
