# S02 — Landscape

## Purpose

Build a problem/mechanism landscape that exposes failure classes and research lines before candidate generation.

## Entry Conditions

G1 approved with current scope and cutoff.

## Reads

Scope, AI-method domain index/modules, paper/search registries, existing evidence.

## Writes

Problem taxonomy, mechanism map, concept dictionary, coverage map, initial research lines, and landscape evidence.

## Required Questions

What fails: data, representation, architecture, objective, assignment, optimization, training, inference, efficiency, generalization, or evaluation? Which mechanisms and mathematical objects connect symptoms to outcomes?

## Required Actions

In exploration mode survey the scoped field; in validation mode map the idea plus alternatives; label established/inferred/unknown links; identify benchmark artifacts and neighboring mechanisms.

## Required Protocols

[Reasoning](../protocols/reasoning.md), [Search](../protocols/search.md), [Evidence](../protocols/evidence.md), relevant [AI-method modules](../domain/ai-methods/index.md).

## Parallelizable Work

Independent research-line discovery and domain failure-class mapping with central deduplication.

## Sequential Work

Concept normalization precedes query graph; evidence integration precedes taxonomy freeze.

## Required Outputs

`reports/landscape.md`, problem taxonomy, mechanism map, concept dictionary, and search coverage map.

## Exit Conditions

Major scoped failure classes, research lines, mechanisms, artifacts, and unknown cells are explicit; route S03.

## Rollback Conditions

Landscape reveals scope mismatch: S01. Missing foundational concept: continue S02.

## Kill Conditions

None; landscape may invalidate a user framing but not the entire broad topic.

## Forbidden Actions

Do not call empty matrix cells novelty, rank modules as candidates, or organize only by model chronology.

## Gate Behavior

No gate; surface material scope contradiction immediately.
