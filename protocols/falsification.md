# Falsification Protocol

## Objective

Design the cheapest valid experiment that can distinguish the core hypothesis from its strongest alternatives or show that actionable optimization space is absent. Do not design the full paper experiment first.

## Experimental Cost Ladder

| Tier | Work | Default role |
|---|---|---|
| `F0` | analyze existing outputs/logs/checkpoints | first choice |
| `F1` | diagnostic inference or lightweight perturbation | E0 probe |
| `F2` | short controlled training | only if F0/F1 insufficient |
| `F3` | full matched baseline training | validation stage |
| `F4` | new-method training | after hypothesis survives |

Prefer F0/F1 for E0. Escalate cost only when the lower tier cannot answer the discriminating question.

## Cheapest Killer

For each hypothesis, identify one cheap killer with high decision impact. A valid experiment specifies hypothesis, alternatives, manipulated/observed variable, control, measurement, expected-if-true, expected-if-false, kill condition, ambiguity branch, cost, and required artifacts.

## Falsifier Types

- `DIRECT`: predicted pattern absent under valid measurement.
- `MECHANISM`: relationship exists but proposed causal link fails.
- `GENERALIZATION`: effect exists only outside claimed scope or in a trivial corner.
- `PRACTICAL`: oracle/ceiling gain or feasible effect is too small to justify the project.

## Diagnostic Metrics

A metric must have construct validity, interpretability, baseline applicability, method independence, robustness, and downstream relevance. Record boundaries/extrema where meaningful and at least one alternative operationalization. If only the proposed method can produce the metric, it cannot independently diagnose the baseline mechanism.

## Ceiling–Selection Decomposition

Where applicable, separate whether a useful candidate/representation exists (`ceiling`) from whether the system selects/uses it (`selection`). Compute an oracle or candidate ceiling and a realized score. If the ceiling gap is negligible, KILL interventions aimed only at selection. If ceiling is high but realized performance is low, selection/optimization space may exist.

## Interventions

Prefer controlled changes to one mechanism variable: scale, noise, occlusion, density, proposal count, assignment constraint, routing load, label quality, or controlled representation access. Add mechanism controls that distinguish “candidate absent” from “candidate present but chosen poorly.”

Use correlation language for observational evidence. Upgrade causal language only with credible intervention, controlled stratification, temporal evidence, or mediation-style evidence appropriate to the claim.

## Preregistration

Freeze before results:

- primary hypothesis/version and alternatives;
- primary setting and stratification;
- metrics and alternative metrics;
- controls and matched baselines;
- exclusion/failure rules;
- GO, HOLD, KILL, and ambiguous-result criteria;
- seeds/repeats appropriate to the stage;
- effect-size or practical-utility threshold with rationale.

Do not quietly move kill thresholds after results. Revise only as a new preregistration version before rerun, with the previous version retained.

## Decision Rules

- `GO`: predicted mechanism pattern survives, beats alternatives under controls, has non-trivial actionable ceiling, and replicates to the preregistered stage standard.
- `HOLD`: measurement validity, power, data, or dependency prevents a decision.
- `KILL`: a valid killer fires, optimization space is negligible, simpler explanation dominates, or effect violates the minimum practical threshold.
- `REFINE`: result narrows scope or mechanism but leaves a new falsifiable survivor.

Do not rely solely on p-values. Consider effect size, uncertainty interval, robustness across preregistered settings, and construct validity. E0 may be exploratory but must not pretend to provide publication-level statistical proof.

## Validity Audit

Check internal, construct, external, and statistical validity; confounders; multiple comparisons; primary vs exploratory stratification; seeds; effect size; confidence intervals/bootstraps where appropriate; and failure cases. A diagnostic visualization should reveal the mechanism claim, not merely overall metric improvement.

## Negative Results

Commit negative evidence, update claims/hypotheses, and choose KILL/REFINE/HOLD. Never hide a valid negative result because method implementation has begun.
