# S15 — Feasibility Audit

## Purpose

Determine whether falsification and full project execution are feasible while keeping scientific value separate from resources.

## Entry Conditions

Falsification plan, frozen candidate commitment, selected `BL-` baseline contract/requirements, and diagnostic hooks are defined.

## Reads

Experiments, frozen commitment budget assumptions, selected baseline configuration, diagnostics, baselines/confounders, datasets, code/checkpoint sources, resource profile, active capability profile, licenses, and candidate open-source component sources.

## Writes

C_F and C_P ranges/assumptions, feasibility/risk ledger, execution decision, R4 code verification evidence/contradictions, and draft `IL-` implementation-leverage plan.

## Required Questions

What compute, data, engineering, dependency, time, storage, API, licensing, reproducibility, and instrumentation resources are required? Which frozen implementation roles can use verified compatible, trust-reviewed but not executed open-source components unchanged or with a minimal adaptation? If no such component fits, what source scan and discriminating requirement justify minimal new code?

## Required Actions

Audit the selected baseline reproducibility/configuration and code at R4 when needed; identify source revisions/licenses/trust/dependency limits and compose a draft `IL-` plan using `REUSE_AS_IS` → `ADAPT_EXISTING` → `NEW_MINIMAL` without executing third-party code; recheck host capability limits; estimate ranges; identify F0/F1 alternatives; separate scientific `GO/HOLD/KILL/REFINE` from execution `READY/HOLD_RESOURCE/BLOCKED`.

## Required Protocols

[Resources](../protocols/resources.md), [Implementation Leverage](../protocols/implementation-leverage.md), [Commitment Integrity](../protocols/commitment-integrity.md), [Reading](../protocols/reading.md), [Baseline Fairness](../protocols/baseline-fairness.md), [Contradiction](../protocols/contradiction.md), [Integrity](../protocols/integrity.md).

## Parallelizable Work

Independent compute, data/license, source-component, code, and instrumentation checks.

## Sequential Work

Verify assumptions/source provenance → compose reuse-first plan → reconcile contradictions → estimate C_F/C_P → execution decision.

## Required Outputs

`reports/feasibility-audit.md`, resource/risk profile, code verification evidence, draft `IL-` plan, execution decision.

## Exit Conditions

C_F/C_P, access, reproducibility, dependencies, source revisions/licenses/trust, reuse/adaptation/new-code decisions, and blockers are explicit; route S16 even if `HOLD_RESOURCE` is likely.

## Rollback Conditions

Unmeasurable hooks: S13; infeasible test: S14; constraint changes: S01.

## Kill Conditions

Scientific KILL only if no feasible discriminating observation exists in any reasonable scope. Resource shortage alone is HOLD_RESOURCE.

## Forbidden Actions

Do not use false precision, silently assume licenses/trust/access, execute or install an external source, write a new module because it feels more novel or familiar, or conflate execution difficulty with scientific invalidity.

## Gate Behavior

No gate; expose external dependency requiring user authority.
