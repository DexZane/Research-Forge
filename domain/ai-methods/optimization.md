# Optimization

## Diagnostic Questions

- Is failure non-convergence, slow convergence, gradient conflict, instability, sharpness, conditioning, or poor basin access?
- Does the final representation ceiling exist but training fail to reach it?
- Are gradients aligned with task strata and objectives?
- Is an auxiliary signal causal or merely regularizing/capacity-increasing?

## Evidence Targets

Learning curves, gradient norm/cosine/conflict, loss surfaces/proxies, controlled initialization, schedule/step matches, short interventions, and multiple seeds.

## Confounders

Optimizer, schedule, batch size, precision, normalization, gradient clipping, augmentation, early stopping, and tuning budget.

## Stitching Risks

New optimizer/auxiliary loss/curriculum must predict a diagnostic change tied to the claimed failure, not only higher final accuracy.
