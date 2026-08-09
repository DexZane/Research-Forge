# S08 — Beam Selection

## Purpose

Reduce the broad pool to 3–5 candidates, then ask G2 to select at most 1–3 finalists.

## Entry Conditions

Every candidate has S07 threat/kill status.

## Reads

Candidate and threat ledgers, evidence, red-ocean map, resource profile, genealogy.

## Writes

Hard-gate results, scorecards with rationale/confidence, Pareto analysis, beam, G2 packet.

## Required Questions

Does each candidate have basic novelty possibility, non-stitching form, clear question, preliminary falsifiability, potential optimization space, and no confirmed fatal prior art? Which candidates are Pareto dominated?

## Required Actions

Apply hard gates first; score scientific novelty, mechanism depth, impact, reviewer clarity, falsifiability, evidence, competition, time/cost, feasibility, generalization, and ceiling; never average away a hard failure.

## Required Protocols

[Reasoning](../protocols/reasoning.md), [Novelty](../protocols/novelty.md), [Resources](../protocols/resources.md), [Gates](../runtime/gates.md), [Integrity](../protocols/integrity.md).

## Parallelizable Work

Independent candidate score rationales from frozen evidence; central Pareto/reconciliation is sequential.

## Sequential Work

Hard gates → score/rationale → Pareto → beam → integrity → G2.

## Required Outputs

`reports/beam-selection.md` and G2 packet showing survivors, kills, strongest prior art, cost, and uncertainty.

## Exit Conditions

Human explicitly selects 1–3 finalists at G2; transition S09.

## Rollback Conditions

No adequate beam: S06 or upstream coverage. User requests exploration: S02/S06.

## Kill Conditions

Failed hard gate or clear Pareto domination for depth-budget allocation; archive, do not delete.

## Forbidden Actions

Do not use total score to rescue hard-gate failure or let user preference change evidence-based scores.

## Gate Behavior

Freeze S09 pending G2; record keep/prioritize/delete/re-explore choices.
