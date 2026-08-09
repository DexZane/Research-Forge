# S15 — Feasibility Audit

## Purpose

Determine whether falsification and full project execution are feasible while keeping scientific value separate from resources.

## Entry Conditions

Falsification plan, baseline requirements, and diagnostic hooks are defined.

## Reads

Experiments, diagnostics, baselines/confounders, datasets, code/checkpoint sources, resource profile, licenses.

## Writes

C_F and C_P ranges/assumptions, feasibility/risk ledger, execution decision, R4 code verification evidence and contradictions.

## Required Questions

What compute, data, engineering, dependency, time, storage, API, licensing, reproducibility, and instrumentation resources are required? Are official checkpoints/configs/hooks accessible?

## Required Actions

Audit baseline reproducibility and code at R4 when needed; estimate ranges; identify F0/F1 alternatives; separate scientific `GO/HOLD/KILL/REFINE` from execution `READY/HOLD_RESOURCE/BLOCKED`.

## Required Protocols

[Resources](../protocols/resources.md), [Reading](../protocols/reading.md), [Baseline Fairness](../protocols/baseline-fairness.md), [Contradiction](../protocols/contradiction.md), [Integrity](../protocols/integrity.md).

## Parallelizable Work

Independent compute, data/license, code, and instrumentation checks.

## Sequential Work

Verify assumptions → reconcile contradictions → estimate C_F/C_P → execution decision.

## Required Outputs

`reports/feasibility-audit.md`, resource/risk profile, code verification evidence, execution decision.

## Exit Conditions

C_F/C_P, access, reproducibility, dependencies, and blockers are explicit; route S16 even if `HOLD_RESOURCE` is likely.

## Rollback Conditions

Unmeasurable hooks: S13; infeasible test: S14; constraint changes: S01.

## Kill Conditions

Scientific KILL only if no feasible discriminating observation exists in any reasonable scope. Resource shortage alone is HOLD_RESOURCE.

## Forbidden Actions

Do not use false precision, silently assume licenses/access, or conflate execution difficulty with scientific invalidity.

## Gate Behavior

No gate; expose external dependency requiring user authority.
