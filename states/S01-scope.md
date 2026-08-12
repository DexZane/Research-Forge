# S01 — Scope

## Purpose

Define research boundaries and obtain G1 approval.

## Entry Conditions

S00 intake is valid and mode is explicit.

## Reads

Project/intake, initial RQ canvas, user constraints, resource profile, current unknowns.

## Writes

Completed RQ canvas, `FIT-` project-fit card, minimum/core/extension scope ladder, task/method/time/venue/resource/user-interest boundaries, out-of-scope list, search cutoff, and G1 packet.

## Required Questions

What phenomenon, unit/condition, knowledge gap, mechanism question, and observable outcome make the question answerable? What is the cheapest plausible discriminating path? Which task/setting, method class, publication horizon/venues, dates, compute/data/engineering budget, mentor/team availability, and preferences constrain work? Which are hard constraints versus preferences versus assumptions?

## Required Actions

Complete the RQ canvas and FIT card; write three nested scopes; separate scientific scope from user interest and mentor advice; expose conflicts, capability gaps, assumed availability, and missing choices; define what evidence would reopen scope; stage G1 packet and a human-discussion packet when requested.

## Required Protocols

[Reasoning](../protocols/reasoning.md), [Researchability](../protocols/researchability.md), [Collaboration](../protocols/collaboration.md), [Resources](../protocols/resources.md), [Gates](../runtime/gates.md), [Integrity](../protocols/integrity.md).

## Parallelizable Work

Read-only feasibility checks for data/compute/venue constraints after task scope is stable.

## Sequential Work

Boundary draft → integrity audit → G1.

## Required Outputs

`reports/scope.md`, RQ canvas, FIT card, scope ladder, resource profile, exclusions, search cutoff, G1 packet, and optional human-discussion packet.

## Exit Conditions

Human explicitly approves an answerable RQ canvas and viable minimum path at G1; transition to S02. Use HOLD_SCOPE, HOLD_RESOURCE, or REFRAME when this condition fails.

## Rollback Conditions

New constraints invalidate intake assumptions: return S00. Later scope change re-enters S01 and requires delta search.

## Kill Conditions

No scientific KILL; use HOLD if no feasible or coherent scope can be approved.

## Forbidden Actions

Do not infer gate approval, let target venue prove value, treat preferences or human advice as evidence, or hide an unavailable dependency inside the minimum scope.

## Gate Behavior

Freeze S02+ work pending G1. Record approval, revision, or hold as a decision.
