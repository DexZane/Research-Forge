# S00 — Intake

## Purpose

Parse the research input, recover existing context if present, and choose `EXPLORATION` or `IDEA_VALIDATION` without judging novelty.

## Entry Conditions

New topic/idea, explicit project resume, or recovery routing has supplied a valid project root.

## Reads

User input; existing `PROJECT.md` and state/snapshot only when resuming; project bootstrap and capability-profile templates.

## Writes

Project identity, mode, raw request, normalized intake, user-supplied baseline model if present, initial `RQ-` research-question canvas, initial `CAP-` capability profile, initial unknowns, user constraints, and `research_state.yaml` navigation fields.

## Required Questions

What is the topic/task? Is a specific idea proposed? Which exact baseline model/variant/configuration does the user provide, if any? What symptom, cause, solution, target, resources, and exclusions are stated versus inferred or missing? What potentially observable phenomenon and decision-relevant unit/condition are present? What can this host actually search, read, write, validate, inspect, or execute without assuming credentials or permissions?

## Required Actions

Preserve the original request verbatim; decompose topic/symptom/proposed cause/proposed solution; create a `BL-` record with `USER_PROPOSED` status when the user names a baseline, otherwise record baseline selection as decision-critical unknown; initialize the RQ canvas without inventing a knowledge gap; run capability preflight and create `CAP-` without storing credentials; label uncertainties; choose mode; create stable project ID and initial decision log.

## Required Protocols

[Reasoning](../protocols/reasoning.md), [Baseline Selection](../protocols/baseline-selection.md), [Researchability](../protocols/researchability.md), [Boot](../runtime/boot.md), [Capability Preflight](../runtime/capability-preflight.md), [Integrity](../protocols/integrity.md).

## Parallelizable Work

None before mode and project identity are stable.

## Sequential Work

Boot validation → intake decomposition → mode selection → initial commit.

## Required Outputs

`PROJECT.md`, `state/research_state.yaml`, initial `RQ-` canvas, initial `BL-` record or baseline-selection debt, initial `CAP-` profile, `reports/intake.md`, and initial `RD-` entries for missing decision-critical context/capabilities.

## Exit Conditions

Mode, project identity, user-provided facts/constraints, baseline input status, inferred elements, unknowns, initial RQ canvas, and host capability limits are explicit; route to S01.

## Rollback Conditions

Corrupt/resumed state routes to runtime recovery; conflicting project identity returns to BOOT.

## Kill Conditions

None; insufficient input produces HOLD for scope clarification, not scientific KILL.

## Forbidden Actions

Do not claim novelty, choose a method, silently select or substitute a baseline, call a module or score target a research question, search only the user’s favored solution, convert inferred intent into fact, or install/execute external code to test a host capability.

## Gate Behavior

No human gate. Ask only for missing scope choices that materially change S01.
