# S18 — Experiment-Ready Dossier

## Purpose

Compress the approved project into an evidence-linked handoff that an experiment/coding agent can execute without silently redefining the science.

## Entry Conditions

G4 explicitly approved GO; integrity and freshness checks are current.

## Reads

All active registries/reports, frozen candidate commitment/signature, active `CAP-` profile, finalized `IL-` implementation-leverage plan, bibliography registry, G4 decision, immutable snapshot, handoff/dossier templates.

## Writes

Final dossier, validated `exports/references.bib`, machine-readable experiment handoff, final snapshot, remaining unknowns, exact next action.

## Required Questions

Can a downstream agent identify the research problem, boundary, hypothesis, alternatives, diagnostics, minimal tests, controls, baselines, data, hooks, thresholds, resources, reuse/adaptation/new-code decisions, current-host capability limits, source revisions/licenses/trust/dependency limits, reviewer risks, and stop conditions without inference?

## Required Actions

Finalize the `IL-` plan and assemble all 30 required elements; run final freshness and integrity sweeps; link IDs/versions including the frozen `CM-` commitment, `IS-` signature, and active `CAP-` profile; regenerate bibliography and reading queue; preserve killed claims and uncertainties; state exact E0 action, pinned source revisions/trust/dependency limits, and forbidden scientific changes.

## Required Protocols

[Integrity](../protocols/integrity.md), [Capability Preflight](../runtime/capability-preflight.md), [Implementation Leverage](../protocols/implementation-leverage.md), [Commitment Integrity](../protocols/commitment-integrity.md), [Bibliography](../protocols/bibliography.md), [Falsification](../protocols/falsification.md), [Baseline Fairness](../protocols/baseline-fairness.md), [Handoff](../runtime/handoff.md), [Bibliography Runtime](../runtime/bibliography.md).

## Parallelizable Work

Read-only synchronization checks by dossier section; one orchestrator assembles and commits.

## Sequential Work

Freshness sweep → registry sync → finalize capability/implementation-leverage plans → bibliography and reading-queue export → dossier assembly → integrity → immutable snapshot → handoff.

## Required Outputs

Experiment dossier with: title, problem, scope, target, tier; frozen candidate commitment/signature; backbone, matrix, red-ocean map, competitors, threats; genealogy, killed claims, boundary, residual, unknowns; hypothesis, known mechanisms, missing link, predictions, alternatives; diagnostics, minimal falsification experiments, controls, baselines, datasets, hooks, decision thresholds; resource estimate, active `CAP-` profile, and final `IL-` implementation-leverage plan; reviewer result, exact next action, and the record count/path for `exports/references.bib` and `exports/reading-queue.md`. Also `handoff/experiment-handoff.yaml`.

## Exit Conditions

All 30 elements validate, IDs/versions resolve, no final component is `DEFERRED`, no selected source lacks required provenance/license/trust/non-execution status, no fatal open issue remains, and handoff identifies one exact next action; mark project stage complete.

## Rollback Conditions

Freshness collision: S09 emergency; synchronization failure: recovery/transaction; newly invalidated science: appropriate upstream state.

## Kill Conditions

No new KILL is decided here; route back to S17 or emergency if a fatal issue appears.

## Forbidden Actions

Do not execute experiments, invent missing details, omit negative evidence, or let the downstream agent change locked hypothesis/boundary without rollback.

## Gate Behavior

G4 already granted GO. Any material scientific change requires a new gate cycle.
