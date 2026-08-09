# S11 — Hypothesis Synthesis

## Purpose

Convert the residual gap into method-free, mechanism-grounded, falsifiable hypotheses.

## Entry Conditions

Stable non-trivial novelty boundary and residual gap from S10.

## Reads

Residual gap/boundary, active claims/evidence, landscape/matrix, domain modules, genealogy.

## Writes

Hypothesis records, mechanism bridge, predictions, preliminary alternatives, falsifiers, and hypothesis debt.

## Required Questions

What observation lacks explanation? Which known relations bound the missing link? What changes if the link is true or false? Can the statement survive removal of method/module names?

## Required Actions

Classify G_A/G_B/G_C; build known A → missing link → known B; place hypotheses on H0–H3 ladder; register specific predictions and 2–4 alternatives; run stitching tests.

## Required Protocols

[Hypothesis](../protocols/hypothesis.md), [Reasoning](../protocols/reasoning.md), [Evidence](../protocols/evidence.md), relevant AI-method modules.

## Parallelizable Work

Independent alternative mechanism bridges or prediction proposals; central activation/versioning is sequential.

## Sequential Work

Residual → mechanism bridge → method-free hypothesis → predictions → alternatives → activation check.

## Required Outputs

Active/draft hypotheses, prediction registry, mechanism bridge, `reports/hypothesis-synthesis.md`.

## Exit Conditions

At least one hypothesis meets activation contract with predictions, alternatives, falsifiers, and evidence-linked known relations; route S12.

## Rollback Conditions

Boundary unclear: S10; evidence gap: S03/S04/S09; no scientific hypothesis: S06.

## Kill Conditions

No method-free or observable hypothesis can be formed, or all bridges are arbitrary stitching.

## Forbidden Actions

Do not propose the final method, claim causality from correlation, or label a hypothesis verified.

## Gate Behavior

No gate; S12 attack must precede G3.
