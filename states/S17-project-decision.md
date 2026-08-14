# S17 — Project Decision

## Purpose

Make an explicit scientific, execution, and publication decision without further research, then present G4.

## Entry Conditions

Reviewer panel and all prerequisite registries are synchronized.

## Reads

Hard-gate evidence, selected `BL-` baseline contract, current frozen commitment/signature, scorecards, meta-review, resources, active capability profile, source trust/dependency limits, novelty boundary, hypotheses, falsification plan, risks, contradictions/debt.

## Writes

`GO`, `HOLD`, `REFINE`, `HOLD_RESOURCE`, or `KILL`; publication tier T1–T4; primary/backup portfolio; G4 packet.

## Required Questions

Do novelty, clear mechanistic question, falsifiability, absence of fatal prior art, optimization space, selected baseline validity/fairness, diagnostic access, integrity, reviewer-fatal gates, and execution capability/source-trust requirements pass? What uncertainty remains?

## Required Actions

Apply hard gates before scorecard; verify that no dependent artifact is stale against the active frozen commitment or capability profile; assess Pareto/portfolio risk; separate scientific/execution decisions; give rationale, confidence, alternatives, rollback target, and exact next action.

## Required Protocols

[Reasoning](../protocols/reasoning.md), [Commitment Integrity](../protocols/commitment-integrity.md), [Resources](../protocols/resources.md), [Capability Preflight](../runtime/capability-preflight.md), [Implementation Leverage](../protocols/implementation-leverage.md), [Reviewer Panel](../protocols/reviewer-panel.md), [Gates](../runtime/gates.md), [Integrity](../protocols/integrity.md).

## Parallelizable Work

None for the final integrated decision; supporting audits must already be complete.

## Sequential Work

Hard gates → dimensional rationale → decision/tiers → integrity → G4.

## Required Outputs

`reports/project-decision.md`, decision log, primary/backup candidate statuses, `G4_PROJECT_LAUNCH` packet.

## Exit Conditions

Human chooses GO, HOLD, KILL, or REVISE. Only explicit GO routes S18.

## Rollback Conditions

REFINE/REVISE specifies S06–S16 target and reason; new evidence uses dependency-aware rollback.

## Kill Conditions

Any scientific hard gate fails irreparably or fatal prior art/reviewer issue remains. Archive all artifacts.

## Forbidden Actions

Do not research further to avoid a decision, average failed hard gates, or upgrade tier because the user wants a top venue.

## Gate Behavior

Freeze S18 pending explicit G4 GO. Silence is not approval.
