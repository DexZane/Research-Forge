# S02 — Landscape

## Purpose

Build a problem/mechanism landscape that exposes failure classes and research lines before candidate generation.

## Entry Conditions

G1 approved with current scope and cutoff.

## Reads

Scope/RQ canvas/FIT card, selected `BL-` baseline contract, AI-method domain index/modules, paper/search registries, existing evidence.

## Writes

Problem taxonomy, mechanism map, concept dictionary, coverage map, initial research lines, opportunity-signal ledger, and landscape evidence.

## Required Questions

What fails: data, representation, architecture, objective, assignment, optimization, training, inference, efficiency, generalization, or evaluation? Which source-grounded signals expose that failure? Which mechanisms and mathematical objects connect symptoms to outcomes? Which baseline-specific queries test known limits without narrowing the broader task/mechanism search?

## Required Actions

In exploration mode survey the scoped field; in validation mode map the idea plus alternatives; create source-grounded `OP-` signals for slice failures, limitations, anomalies, artifacts, constraints, or open technical questions; use baseline-specific queries as one branch while preserving independent task/mechanism/failure-mode queries; label established/inferred/unknown links; identify benchmark artifacts and neighboring mechanisms.

## Required Protocols

[Reasoning](../protocols/reasoning.md), [Baseline Selection](../protocols/baseline-selection.md), [Opportunity Signals](../protocols/opportunity-signals.md), [Search](../protocols/search.md), [Evidence](../protocols/evidence.md), relevant [AI-method modules](../domain/ai-methods/index.md).

## Parallelizable Work

Independent research-line discovery and domain failure-class mapping with central deduplication.

## Sequential Work

Concept normalization precedes query graph; evidence integration precedes taxonomy freeze.

## Required Outputs

`reports/landscape.md`, problem taxonomy, mechanism map, concept dictionary, opportunity-signal ledger, and search coverage map.

## Exit Conditions

Major scoped failure classes, research lines, mechanisms, artifacts, source-grounded opportunity signals, and unknown cells are explicit; route S03.

## Rollback Conditions

Landscape reveals scope mismatch: S01. Missing foundational concept: continue S02.

## Kill Conditions

None; landscape may invalidate a user framing but not the entire broad topic.

## Forbidden Actions

Do not call empty matrix cells novelty, a user report a verified signal, rank modules as candidates, or organize only by model chronology.

## Gate Behavior

No gate; surface material scope contradiction immediately.
