# Baseline Fairness Protocol

## Core Budget Matching

Before attributing a gain to a mechanism, match or explicitly account for:

- training and evaluation data, external data, and label processing;
- pretrained weights and initialization;
- input resolution and preprocessing;
- epochs, optimizer steps, schedule, batch size, and early stopping;
- augmentation and regularization;
- inference protocol, post-processing, thresholds, and test-time augmentation;
- evaluation code, metric version, splits, and exclusions;
- hyperparameter search and tuning budget;
- seed/repeat policy and checkpoint selection.

## Confounder Ledger

Track parameters, FLOPs/MACs, measured latency/throughput, memory, training steps/time, resolution, external data, augmentation, tuning budget, software/hardware, and instrumentation differences. Mark each `MATCHED`, `CONTROLLED`, `MEASURED`, `UNMATCHED_JUSTIFIED`, or `OPEN`.

## Stronger-baseline Check

Choose mechanism-relevant controls from:

- official/reproduced baseline;
- baseline + longer or matched training;
- baseline + matched parameters/compute;
- baseline + stronger augmentation/recipe;
- baseline + equal tuning budget;
- simplest intervention or ablation;
- proposed approach.

Do not add every control mechanically; explain which alternative explanation each control tests.

## Attribution Rule

If improvement disappears under a fair stronger baseline, record negative evidence and weaken the mechanism claim. If budgets cannot be matched, narrow the claim and downgrade confidence; do not call the comparison fair.

## Efficiency

Report both theoretical and measured cost when relevant. Latency claims require matched hardware, software, precision, batch size, warm-up, and measurement protocol. Parameter count cannot substitute for latency or energy.

## Pre-gate Checklist

- Every claimed gain has a valid comparison.
- Major unmatched budgets are visible.
- Tuning/search effort is accounted for.
- Metric implementation and checkpoint selection match.
- Mechanism controls distinguish capacity/recipe effects.
- Resource infeasibility is separated from scientific invalidity.
