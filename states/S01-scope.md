# S01 — Scope

## Purpose

Define research boundaries and obtain G1 approval.

## Entry Conditions

S00 intake is valid and mode is explicit.

## Reads

Project/intake, user constraints, resource profile, current unknowns.

## Writes

Task, method, time, venue, resource, and user-interest boundaries; out-of-scope list; search cutoff; G1 packet.

## Required Questions

Which task/setting, method class, publication horizon/venues, dates, compute/data/engineering budget, and user preferences constrain work? Which are hard constraints versus preferences?

## Required Actions

Separate scientific scope from user interest; expose conflicts and missing choices; define what evidence would reopen scope; stage G1 packet.

## Required Protocols

[Reasoning](../protocols/reasoning.md), [Resources](../protocols/resources.md), [Gates](../runtime/gates.md), [Integrity](../protocols/integrity.md).

## Parallelizable Work

Read-only feasibility checks for data/compute/venue constraints after task scope is stable.

## Sequential Work

Boundary draft → integrity audit → G1.

## Required Outputs

`reports/scope.md`, resource profile, exclusions, search cutoff, and `G1_SCOPE_LOCK` packet.

## Exit Conditions

Human explicitly approves G1; transition to S02.

## Rollback Conditions

New constraints invalidate intake assumptions: return S00. Later scope change re-enters S01 and requires delta search.

## Kill Conditions

No scientific KILL; use HOLD if no feasible or coherent scope can be approved.

## Forbidden Actions

Do not infer gate approval, let target venue prove value, or treat preferences as evidence.

## Gate Behavior

Freeze S02+ work pending G1. Record approval, revision, or hold as a decision.
