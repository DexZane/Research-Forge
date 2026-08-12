# S00 — Intake

## Purpose

Parse the research input, recover existing context if present, and choose `EXPLORATION` or `IDEA_VALIDATION` without judging novelty.

## Entry Conditions

New topic/idea, explicit project resume, or recovery routing has supplied a valid project root.

## Reads

User input; existing `PROJECT.md` and state/snapshot only when resuming; project bootstrap template.

## Writes

Project identity, mode, raw request, normalized intake, initial `RQ-` research-question canvas, initial unknowns, user constraints, and `research_state.yaml` navigation fields.

## Required Questions

What is the topic/task? Is a specific idea proposed? What symptom, cause, solution, target, resources, and exclusions are stated versus inferred or missing? What potentially observable phenomenon and decision-relevant unit/condition are present?

## Required Actions

Preserve the original request verbatim; decompose topic/symptom/proposed cause/proposed solution; initialize the RQ canvas without inventing a knowledge gap; label uncertainties; choose mode; create stable project ID and initial decision log.

## Required Protocols

[Reasoning](../protocols/reasoning.md), [Researchability](../protocols/researchability.md), [Boot](../runtime/boot.md), [Integrity](../protocols/integrity.md).

## Parallelizable Work

None before mode and project identity are stable.

## Sequential Work

Boot validation → intake decomposition → mode selection → initial commit.

## Required Outputs

`PROJECT.md`, `state/research_state.yaml`, initial `RQ-` canvas, `reports/intake.md`, and initial `RD-` entries for missing decision-critical context.

## Exit Conditions

Mode, project identity, user-provided facts/constraints, inferred elements, unknowns, and initial RQ canvas are explicit; route to S01.

## Rollback Conditions

Corrupt/resumed state routes to runtime recovery; conflicting project identity returns to BOOT.

## Kill Conditions

None; insufficient input produces HOLD for scope clarification, not scientific KILL.

## Forbidden Actions

Do not claim novelty, choose a method, call a module or score target a research question, search only the user’s favored solution, or convert inferred intent into fact.

## Gate Behavior

No human gate. Ask only for missing scope choices that materially change S01.
