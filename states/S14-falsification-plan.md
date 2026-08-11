# S14 — Falsification Plan

## Purpose

Pre-register the lowest-cost, highest-information experiments that can kill or discriminate the hypothesis.

## Entry Conditions

Valid diagnostic metrics and locked hypothesis version exist.

## Reads

Locked hypothesis version, active draft commitment, alternatives/predictions, diagnostics, baseline/confounder data, resources and existing outputs.

## Writes

E0 experiment records, controls, stratification, preregistered GO/HOLD/KILL/REFINE rules, cost and ambiguity branches, and a frozen candidate commitment linked to the plan.

## Required Questions

Can F0/F1 answer first? Which experiment distinguishes core from strongest alternative? What valid observation kills it? What result is ambiguous? What mechanism control separates ceiling from selection?

## Required Actions

Choose cheapest killer; define variables, controls, measures, expected true/false patterns, kill condition, cost; prefer intervention; freeze primary metrics/settings/thresholds and the related `CM-` commitment before results.

## Required Protocols

[Falsification](../protocols/falsification.md), [Commitment Integrity](../protocols/commitment-integrity.md), [Baseline Fairness](../protocols/baseline-fairness.md), [Resources](../protocols/resources.md), [Integrity](../protocols/integrity.md).

## Parallelizable Work

Cost estimates, control designs, and independent falsifier proposals after hypotheses/metrics freeze.

## Sequential Work

Information-gain ranking → experiment selection → fairness/validity audit → preregistration commit.

## Required Outputs

`reports/falsification-plan.md`, experiment registry entries, controls/baselines, decision thresholds, expected figures.

## Exit Conditions

At least one feasible E0 distinguishes the core from a strong alternative or tests practical ceiling, with preregistered decision rules and an active frozen commitment; route S15.

## Rollback Conditions

No discriminating test: S12/S13; method required to diagnose: S13; scope/resource conflict: S01/S15.

## Kill Conditions

No feasible falsifier or all valid tests have negligible information value relative to cost.

## Forbidden Actions

Do not design a full new-method training campaign first or move thresholds after results.

## Gate Behavior

No gate; plan remains unexecuted in Research Forge.
