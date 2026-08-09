# S12 — Hypothesis Attack

## Purpose

Try to explain the same observations more simply or differently, then lock only a surviving hypothesis at G3.

## Entry Conditions

S11 produced at least one active/draft hypothesis and predictions.

## Reads

Hypotheses, predictions, claims/evidence, contradictions, baseline confounders, novelty boundary.

## Writes

Steelmanned alternatives, discriminating-test questions, weakened/invalidated/superseded hypotheses, G3 packet.

## Required Questions

Could representation, optimization, assignment, data/annotation, metric/benchmark artifact, capacity, recipe, parameter/scale confounder, or a simpler cause explain the observation?

## Required Actions

Maintain 2–4 alternatives; compare predictions; run Occam, artifact, confounder, and correlation/causation attacks; identify the cheapest distinguishing observation; freeze hypothesis version and preregistration inputs.

## Required Protocols

[Hypothesis](../protocols/hypothesis.md), [Reasoning](../protocols/reasoning.md), [Baseline Fairness](../protocols/baseline-fairness.md), [Gates](../runtime/gates.md), [Integrity](../protocols/integrity.md).

## Parallelizable Work

Independent steelman attacks by explanation family from a frozen hypothesis version.

## Sequential Work

Integrate alternatives → adjudicate → update hypothesis → integrity → G3.

## Required Outputs

`reports/hypothesis-attack.md`, competing-hypothesis table, discriminating questions, `G3_HYPOTHESIS_LOCK` packet showing genealogy, killed claims, residual, core hypothesis, alternatives, and falsifiers.

## Exit Conditions

Human explicitly locks a surviving scoped hypothesis at G3; route S13.

## Rollback Conditions

Core hypothesis fails: S11 or S06; new novelty issue: S09/S10; boundary changes: S10.

## Kill Conditions

Simpler/alternative explanation dominates and no distinct prediction remains, or the construct cannot be observed even in principle within scope.

## Forbidden Actions

Do not let the core hypothesis see only weak alternatives or infer G3 approval.

## Gate Behavior

Freeze diagnostic design until explicit G3 approval or revision.
