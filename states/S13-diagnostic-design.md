# S13 — Diagnostic Design

## Purpose

Define how to measure the proposed mechanism directly before designing a new method.

## Entry Conditions

G3 locked a hypothesis version, alternatives, predictions, and falsifiers.

## Reads

Locked hypotheses/predictions, selected `BL-` baseline contract/artifacts/hooks, domain evaluation module, resource profile.

## Writes

Diagnostic metric records, alternative operationalizations, ceiling/oracle definitions, construct-validity risks.

## Required Questions

What does each metric measure? Does it apply to the selected baseline and stronger-baseline controls under the locked configuration? What do boundaries/extrema mean? Which prediction and alternative does it distinguish? What confounds it?

## Required Actions

Design interpretable, method-independent diagnostics; define candidate ceiling/selection regret/oracle where applicable; add alternative metrics and artifact tests; verify required hooks are accessible.

## Required Protocols

[Falsification](../protocols/falsification.md), [Hypothesis](../protocols/hypothesis.md), [Evaluation](../domain/ai-methods/evaluation.md), [Resources](../protocols/resources.md).

## Parallelizable Work

Alternative metric formulations and hook feasibility checks.

## Sequential Work

Construct definition → operationalization → baseline applicability → artifact/validity audit → registration.

## Required Outputs

Diagnostic metric registry, oracle/ceiling specification, `reports/diagnostic-design.md`.

## Exit Conditions

At least one valid diagnostic per primary prediction plus an alternative operationalization and known confounders; route S14.

## Rollback Conditions

Mechanism unmeasurable: S11/S12; unavailable hooks that alter scope: S15 or S01; metric artifact dominates: redesign S13.

## Kill Conditions

No method-independent measurement or valid proxy can distinguish the core hypothesis within feasible scope.

## Forbidden Actions

Do not define success only through final task performance or a metric available only to the proposed method.

## Gate Behavior

No gate.
