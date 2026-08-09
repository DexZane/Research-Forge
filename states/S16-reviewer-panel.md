# S16 — Reviewer Panel

## Purpose

Simulate independent top-tier novelty, mechanism, and experiment rejection before launch.

## Entry Conditions

Frozen pre-review dossier includes novelty boundary, hypothesis, diagnostics, falsification, fairness, and feasibility.

## Reads

Immutable dossier snapshot and all linked evidence; reviewers receive identical versions.

## Writes

Independent R_N/R_M/R_E reports, meta-review, fatal/resolvable issues, disagreement records, ceiling recommendation.

## Required Questions

Why is it incremental? Why is the mechanism unsupported? Why would experiments be insufficient? What single issue is most likely fatal?

## Required Actions

Run first-pass reviews independently; freeze reports; meta-review without averaging; classify issues; require reject simulation for T1 candidates; link every issue to affected records.

## Required Protocols

[Reviewer Panel](../protocols/reviewer-panel.md), [Novelty](../protocols/novelty.md), [Baseline Fairness](../protocols/baseline-fairness.md), [Integrity](../protocols/integrity.md).

## Parallelizable Work

R_N, R_M, and R_E first-pass reports only.

## Sequential Work

Freeze shared dossier → independent reviews → freeze reports → meta-review → impact propagation.

## Required Outputs

Reviewer reports, meta-review, reject-simulation responses, `reports/reviewer-panel.md`.

## Exit Conditions

No unclassified issue; fatal/resolvable/disagreement impact is explicit; route S17 or rollback.

## Rollback Conditions

Novelty issue: S09/S10; mechanism: S11/S12; diagnostic/experiment: S13/S14; resources: S15.

## Kill Conditions

Verified fatal issue eliminates the core and cannot be resolved without trivializing the project.

## Forbidden Actions

Do not share first-pass reviewer conclusions, average away fatal issues, or answer attacks with rhetoric.

## Gate Behavior

No human gate unless a fatal issue requires emergency/authority; normal decision follows S17.
