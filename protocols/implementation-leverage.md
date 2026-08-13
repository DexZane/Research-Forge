# Implementation Leverage Protocol

## Purpose

Turn a locked scientific direction into an auditable implementation plan that reuses suitable open-source building blocks before creating new code. Reuse reduces avoidable engineering work; it neither proves a mechanism nor creates novelty.

## Timing and Boundary

Do not search for components while generating candidates or use available code to choose a research question. Begin the `IL-` implementation-leverage plan in S15 only after G3 has locked the candidate commitment and hypothesis. Finalize it in S18 after G4 GO. Research Forge specifies the plan; a downstream coding agent implements it.

## Reuse-First Decision Ladder

For every required implementation role, use exactly one decision:

1. `REUSE_AS_IS`: use a verified, compatible component unchanged when it supplies the required capability and preserves the planned comparison.
2. `ADAPT_EXISTING`: make the smallest interface, configuration, or instrumentation adaptation when it does not alter the frozen mechanism, baseline treatment, primary metric, or comparison budget.
3. `NEW_MINIMAL`: write only the smallest isolated component needed when a documented source scan finds no suitable reusable or safely adaptable component for the frozen requirement.
4. `DEFERRED`: use only while source, license, or interface facts are unresolved; it cannot close execution readiness.

`NEW_MINIMAL` requires all of: audited considered sources, a concrete rejection reason for each relevant candidate, a frozen-mechanism requirement that cannot be met by reuse/adaptation, a minimal public interface, and a planned equivalence/ablation control. “It is easier,” “it looks cleaner,” “it may be more novel,” or personal familiarity are not sufficient reasons.

## Source and License Audit

For every selected or seriously considered source, record repository URL, source kind, component locator/API, immutable commit/release, declared license identifier, project-recorded license status, verification evidence, rejection reason when not selected, and known maintenance/reproducibility limits. A bare URL or an issue comment is a discovery lead, not a completed source audit.

Use only legally authorized access. `LICENSE_UNKNOWN`, `LICENSE_REVIEW_REQUIRED`, or `LICENSE_INCOMPATIBLE` blocks reuse until resolved; do not copy source text or bypass a license restriction. License status is a project risk assessment, not legal advice.

## Composition and Fairness

Map each reused/adapted/new component to one frozen mechanism role, diagnostic hook, baseline, or infrastructure role. Keep infrastructure reuse separate from the claimed intervention. For an adaptation, record the exact delta and verify that it does not create an unmatched capacity, recipe, data, tuning, or instrumentation advantage.

When a new component is necessary, isolate it behind a minimal interface and include the closest reusable/adapted alternative in the ablation or control plan where feasible. A reused upstream implementation cannot be presented as the project's novel module, and a new wrapper cannot silently redefine the locked scientific commitment.

## Handoff and Revision

The S18 handoff pins the `IL-` plan and each selected source revision. The downstream coding agent must follow its component decisions. A source revision, adaptation, or new-code change that affects the frozen mechanism, diagnostic validity, baseline fairness, primary prediction, or resource estimate creates a revision request and routes back to the earliest affected state.
