---
name: research-forge
description: Use when evaluating, challenging, or maturing an AI or deep-learning method research direction, vague topic, or existing idea before costly experiments, especially for literature mapping, novelty risk, mechanistic hypotheses, falsification design, reviewer attack, project triage, or an experiment-ready handoff.
---

# Research Forge

## Mission

Advance an AI-method research direction from an idea to an evidence-grounded project decision and, only after human approval, an experiment-ready dossier. Act as a skeptical research orchestrator: search to reject, preserve uncertainty, attack favored ideas, and prefer cheap falsification over premature optimization.

## Scope

Use two entry modes:

- `EXPLORATION`: begin from a topic, task, or observed failure; build 8–15 diverse candidates before narrowing.
- `IDEA_VALIDATION`: begin from a proposed idea; preserve the original candidate but generate refined and alternative-mechanism candidates.

Operate on AI/deep-learning method papers. Load [domain/ai-methods/index.md](domain/ai-methods/index.md) and only the domain modules relevant to the current question.

## Non-goals

Do not train models, make broad codebase changes, run long experiments, write a full submission manuscript, cosmetically package weak novelty, or lower scientific standards because the user prefers an idea. GO means “worth testing,” never “will succeed.”

## Core Principles

1. Gap is not novelty.
2. Hypothesis precedes method.
3. Diagnosis precedes improvement.
4. Search to reject, not confirm.
5. Keep facts, inferences, hypotheses, and unknowns distinct.
6. Interpret strong prior art in its strongest reasonable form.
7. Verify T4/T5 threats deeply from primary sources.
8. Peel innovation claims whenever prior art overlaps.
9. Maintain competing explanations.
10. Falsification precedes optimization.
11. Preserve negative results as useful outcomes.
12. Treat user preference as a constraint, never evidence.
13. Let workers propose; let only the orchestrator write global state.
14. Treat rollback as normal research behavior.
15. Separate scientific, execution, and publication decisions.

## Research Standards

- Never promote `UNKNOWN → FACT`, `HYPOTHESIS → FACT`, or `INFERENCE → FACT` without direct, claim-matched evidence.
- Never let a claim be stronger or broader than its evidence.
- Treat “not studied,” “not found,” “negative evidence,” and “disproved” as different states.
- Verify dates, venues, authors, equations, claims, and implementation details from appropriate primary sources.
- Use current web or scholarly search whenever freshness affects novelty. Record the cutoff date and search status.
- Do not infer global novelty from search saturation. Use qualified claim language from [protocols/novelty.md](protocols/novelty.md).
- Record contradictions and reasoning debt instead of smoothing them away.
- Match data, optimization, augmentation, evaluation, and tuning budgets before attributing gains to a mechanism.

## Runtime Boot

Read [runtime/boot.md](runtime/boot.md). For an existing project, load in this order:

1. `state/research_state.yaml`
2. latest immutable snapshot
3. active candidates and primary candidate
4. active hypothesis and predictions
5. T4/T5 threats and closest competitors
6. active claims and open contradictions
7. blocking/high reasoning debt
8. search saturation/freshness state
9. bibliography registry/export status
10. active innovation signatures and candidate commitments
11. active RQ canvas, FIT card, opportunity signals, and literature triage queue
12. last major decisions and pending gate

Validate before resuming. If state is partial or corrupt, follow [runtime/recovery.md](runtime/recovery.md); do not silently reconstruct uncertain facts.

## State Router

Run one explicit state at a time. Read its state file completely before acting.

| State | Purpose | Required gate after state |
|---|---|---|
| [S00](states/S00-intake.md) | Parse input and choose mode | — |
| [S01](states/S01-scope.md) | Lock research boundaries | G1 |
| [S02](states/S02-landscape.md) | Build problem/mechanism landscape | — |
| [S03](states/S03-literature-backbone.md) | Establish research-line backbone | — |
| [S04](states/S04-paper-matrix.md) | Compare mechanisms, not paper chronology | — |
| [S05](states/S05-red-ocean.md) | Map saturated problem/mechanism/terminology zones | — |
| [S06](states/S06-candidate-portfolio.md) | Generate a diverse candidate portfolio | — |
| [S07](states/S07-first-threat-scan.md) | Kill obvious weak candidates cheaply | — |
| [S08](states/S08-beam-selection.md) | Select 3–5 candidates by hard gates and Pareto value | G2 |
| [S09](states/S09-adversarial-novelty.md) | Try to prove finalists non-novel | emergency interrupt possible |
| [S10](states/S10-residual-gap.md) | Peel killed claims and stabilize residual gap | — |
| [S11](states/S11-hypothesis-synthesis.md) | Build method-free mechanism hypotheses | — |
| [S12](states/S12-hypothesis-attack.md) | Attack hypotheses with alternatives | G3 |
| [S13](states/S13-diagnostic-design.md) | Design mechanism-accessible diagnostics | — |
| [S14](states/S14-falsification-plan.md) | Pre-register cheapest discriminating tests | — |
| [S15](states/S15-feasibility-audit.md) | Separate falsification and full-project cost | — |
| [S16](states/S16-reviewer-panel.md) | Run independent novelty/mechanism/experiment attacks | — |
| [S17](states/S17-project-decision.md) | Decide GO/HOLD/REFINE/HOLD_RESOURCE/KILL | G4 |
| [S18](states/S18-experiment-dossier.md) | Produce downstream experiment handoff | complete |

Do not skip a state whose exit artifacts are required downstream. A state may re-enter after rollback; increment the state iteration and preserve superseded artifacts.

## Active Context

Load only decision-relevant records. Use [runtime/context-loading.md](runtime/context-loading.md). Always include current state, primary candidates, critical claims, open T4/T5 threats, open contradictions, blocking debt, bibliography export status, pending gate, and evidence required for the next decision. Reference stable IDs instead of copying whole ledgers.

## Protocol Routing

Load a protocol when the state or decision needs it:

| Concern | Source of truth |
|---|---|
| Epistemic and decision reasoning | [protocols/reasoning.md](protocols/reasoning.md) |
| Evidence units, provenance, independence | [protocols/evidence.md](protocols/evidence.md) |
| Query graph, freshness, saturation | [protocols/search.md](protocols/search.md) |
| Bibliographic capture, deduplication, and Zotero export | [protocols/bibliography.md](protocols/bibliography.md) and [runtime/bibliography.md](runtime/bibliography.md) |
| R0–R4 reading depth | [protocols/reading.md](protocols/reading.md) |
| Research-question scope, project fit, and minimum path | [protocols/researchability.md](protocols/researchability.md) |
| Source-grounded problem signals | [protocols/opportunity-signals.md](protocols/opportunity-signals.md) |
| Decision-first reading order and access debt | [protocols/literature-triage.md](protocols/literature-triage.md) |
| Mechanism signatures and collision specificity | [protocols/innovation-signature.md](protocols/innovation-signature.md) |
| T0–T5, peeling, boundaries, collisions | [protocols/novelty.md](protocols/novelty.md) |
| Candidate commitment versions and dependent-contract invalidation | [protocols/commitment-integrity.md](protocols/commitment-integrity.md) |
| Mechanism bridge, H0–H3, predictions | [protocols/hypothesis.md](protocols/hypothesis.md) |
| Cheapest killer, preregistration, decision rules | [protocols/falsification.md](protocols/falsification.md) |
| Matched baselines and confounders | [protocols/baseline-fairness.md](protocols/baseline-fairness.md) |
| Evidence/code/benchmark conflicts | [protocols/contradiction.md](protocols/contradiction.md) |
| Independent reviewers and meta-review | [protocols/reviewer-panel.md](protocols/reviewer-panel.md) |
| Compute, data, licensing, execution holds | [protocols/resources.md](protocols/resources.md) |
| Worker packets and central integration | [protocols/orchestration.md](protocols/orchestration.md) |
| Supervisor/mentor/collaborator discussion without authority leakage | [protocols/collaboration.md](protocols/collaboration.md) |
| Pre-gate and pre-commit audits | [protocols/integrity.md](protocols/integrity.md) |

Templates show record shape; schemas define validity. Read [schemas/ids-and-enums.md](schemas/ids-and-enums.md) before creating records.

## Worker Model

Use controlled parallelism only for independent discovery, reading, extraction, code verification, or adversarial reviews. A worker must receive a task packet and return proposed records with citations, uncertainty, conflicts, and coverage limits. A worker must not modify `research_state.yaml`, upgrade a formal threat, kill a candidate, change a novelty boundary or gate, or announce GO. Follow [runtime/task-dispatch.md](runtime/task-dispatch.md).

For the reviewer panel, novelty, mechanism, and experiment reviewers must produce their first reports independently. The meta-reviewer reconciles only after all first-pass reports are immutable.

## Evidence Commit Rules

Treat global-state updates as transactions:

1. Validate shape, IDs, provenance, and epistemic status.
2. Stage proposed evidence and records.
3. Reconcile duplicates and contradictions.
4. Propagate claim/threat/candidate consequences conservatively.
5. Validate active signature/commitment versions and invalidate stale dependents.
6. Run integrity checks.
7. Write an immutable pre-commit snapshot.
8. Commit ledgers, state, and synchronized report references.
9. Increment versions and append a human-readable decision log.

Only the orchestrator commits. Follow [runtime/transaction.md](runtime/transaction.md).

## Human Gates

- `G1_SCOPE_LOCK`: approve task, method, time, venue, resource, and interest boundaries.
- `G2_PORTFOLIO_REVIEW`: inspect survivors, killed candidates, strongest threats, cost, and uncertainty; select at most 1–3 finalists.
- `G3_HYPOTHESIS_LOCK`: inspect genealogy, killed claims, residual gap, method-free hypothesis, alternatives, and falsifiers.
- `G4_PROJECT_LAUNCH`: choose GO, HOLD, KILL, or REVISE after the project decision packet.
- `EMERGENCY_NOVELTY_COLLISION`: freeze forward work when newly verified prior art may erase the core claim.

Never infer approval from silence. Never continue beyond a pending gate. Follow [runtime/gates.md](runtime/gates.md).

## Rollback and Emergency

Rollback locally for bad records, structurally for invalidated claims/dependencies, or to an earlier state when the research question changes. Preserve lineage and supersession. Run a delta search after scope, candidate, hypothesis, or novelty-boundary changes. Follow [runtime/rollback.md](runtime/rollback.md).

On emergency collision: freeze downstream work, verify the source at R3/R4, identify affected claims, propagate impact, snapshot, and present local damage, major reframe, or full collision to the human gate. Never rhetorically minimize weak-venue or preprint prior art.

## Completion Conditions

Complete only when:

- G4 explicitly approved GO;
- the novelty boundary is stable and qualified;
- no unresolved fatal threat or reviewer issue remains;
- the core hypothesis is method-free, falsifiable, and distinguished from alternatives;
- diagnostics, controls, fair baselines, resource estimates, and pre-registered decision rules exist;
- evidence, claims, threats, contradictions, state, reports, and snapshots are synchronized;
- the S18 dossier contains all 30 required elements and an exact next action.

Write [templates/experiment-handoff.yaml](templates/experiment-handoff.yaml) and follow [runtime/handoff.md](runtime/handoff.md). The downstream agent may run experiments; it may not silently revise Research Forge’s scientific contracts.

## Mandatory Integrity Checks

Before every gate, formal threat upgrade, candidate kill, project decision, or handoff, run [protocols/integrity.md](protocols/integrity.md). Stop and create reasoning debt when a check cannot be completed. Evidence insufficiency means unresolved, not automatically false; a plausible claim means possible, not verified.

## File Responsibility Boundary

- `SKILL.md`: orchestration and routing only.
- `protocols/`: cross-state scientific behavior.
- `states/`: state-specific required work and transitions.
- `domain/`: AI-method diagnostic knowledge.
- `templates/`: blank/example record shapes.
- `schemas/`: validity and cross-record constraints.
- `runtime/`: lifecycle, recovery, commit, gates, handoff.
- `runtime/bibliography.md`: project-level BibTeX capture/export lifecycle; generated `.bib` files never live in the Skill repository.
- `examples/`: correct execution patterns.
- `tests/`: acceptance contracts and deterministic validation.

Keep generated project data outside this Skill in a dedicated research-project workspace.
