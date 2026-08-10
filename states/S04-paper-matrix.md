# S04 — Paper Matrix

## Purpose

Transform paper-centric reading into mechanism-centric comparison.

## Entry Conditions

Backbone and R2 anchor reads exist.

## Reads

Paper registry/families, evidence ledger, landscape taxonomy, R2 notes.

## Writes

Mechanism matrix, normalized claims, synchronized citation metadata, not-addressed inferences, contradiction records, and preliminary cross-line gaps.

## Required Questions

For each paper: problem, observation, hypothesis, mechanism, changed mathematical object, data, representation, assignment, loss, training, inference, efficiency, evidence, limitation, relevance, and what it does not address?

## Required Actions

Require R2 for formal entries; distinguish author-stated limitations from orchestrator `INFERENCE`; compare columns across lines; identify intersections as `CANDIDATE_GAP`, never novelty.

## Required Protocols

[Reading](../protocols/reading.md), [Bibliography](../protocols/bibliography.md), [Evidence](../protocols/evidence.md), [Reasoning](../protocols/reasoning.md), [Contradiction](../protocols/contradiction.md).

## Parallelizable Work

R2 extraction per paper family using one normalized schema.

## Sequential Work

Entity normalization and contradiction reconciliation before matrix synthesis.

## Required Outputs

`reports/paper-matrix.md`, matrix records, normalized claim/evidence links, synchronized bibliography records, candidate-gap list.

## Exit Conditions

Critical research lines are comparable by mechanism and mathematical object; important matrix claims have evidence/status; route S05.

## Rollback Conditions

Missing backbone coverage: S03. Unclear taxonomy: S02.

## Kill Conditions

None; individual gap notions may be discarded.

## Forbidden Actions

Do not equate empty cells with novelty or state inferred non-coverage as an author fact.

## Gate Behavior

No gate.
