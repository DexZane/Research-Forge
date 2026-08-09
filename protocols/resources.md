# Resource and Feasibility Protocol

## Separate Costs

- `C_F_FALSIFICATION`: minimum resources to learn whether the hypothesis is worth pursuing.
- `C_P_PUBLICATION`: resources for a credible full project and publication story.

Never reject scientific value solely because C_P is currently unavailable; use `HOLD_RESOURCE` when C_F can establish value but execution conditions are missing.

## Audit Dimensions

Estimate compute, accelerator type/count, time, storage, data access, licensing, engineering, dependencies, official checkpoints, baseline reproducibility, required hooks/internal variables, evaluation time, external APIs, and human expertise. Use ranges and assumptions; avoid false precision.

## Feasibility Checks

- Official baseline/checkpoint/config exists or reproduction risk is explicit.
- Required datasets and licenses are accessible.
- Internal variables can be instrumented without changing the tested mechanism.
- F0/F1 alternatives have been considered before training.
- Compute estimates distinguish short falsification from full training.
- External services, privacy, and redistribution constraints are visible.

## Decision Separation

Record independently:

```yaml
scientific_decision: GO | HOLD | KILL | REFINE
execution_decision: READY | HOLD_RESOURCE | BLOCKED
publication_tier: T1 | T2 | T3 | T4
```

User ambition does not raise publication tier. Resources do not turn weak novelty into strong novelty.

## Risk Treatment

For each risk record likelihood qualitatively, impact, evidence, mitigation, trigger, owner, and decision consequence. If mitigation changes the scientific question, rollback and reopen novelty search.
