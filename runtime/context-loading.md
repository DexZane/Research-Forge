# Active Context Loading

## Minimal Context Rule

Load IDs and decision-relevant fields, not entire project history. Always include current state/iteration/version, pending gate, active research-question canvas, fit card, baseline profile/contract, and capability profile, verified/decision-critical opportunity signals, gate-critical literature-triage entries and access debt, active implementation-leverage plan/source revisions/trust/dependency assessment, active candidates/hypotheses, T4/T5 threats, open blocking contradictions/debt, bibliography export/reading-queue status, latest snapshot, and last major decisions.

## State Groups

| States | Add to context |
|---|---|
| S00–S01 | intake, research-question canvas, fit card, user-proposed or direction-searched baseline profiles, baseline-selection packet, capability profile, scope ladder, project constraints, resource profile |
| S02–S05 | selected baseline contract, research-question canvas, fit card, opportunity-signal ledger, literature-triage queue/access debt, scope, concept dictionary, research lines, awareness-only leads, citable lineage, coverage map, anchor papers/bibliography/evidence, paper signatures |
| S06–S08 | selected baseline contract, candidate registry/genealogy, candidate-to-question/signal/baseline-delta provenance, draft signatures/commitments, red-ocean constraints, preliminary threats, score rationale, minimum discriminating paths |
| S09–S10 | version-pinned finalist signature/commitment versions, query graph, closest competitors, all T4/T5 evidence, claims, contradictions |
| S11–S12 | boundary/residual, mechanism claims, hypotheses, predictions, alternatives, falsifiers |
| S13–S15 | selected baseline contract, locked hypothesis/commitment version, diagnostics, experiments, baselines/confounders, resources/code evidence, implementation-leverage source scan, trust/dependency assessments, and component decisions |
| S16–S17 | immutable dossier, active commitment/signature, independent reviewer reports/meta-review, hard gates, risks |
| S18 | G4 decision, selected baseline contract, all active dossier IDs/versions, frozen commitment, finalized implementation-leverage plan/pinned source revisions/trust, freshness/integrity results, bibliography export/reading queue status, handoff template |
| FAST_AUDIT | intake, single candidate signature/commitment, locked baseline profile, targeted competitor queries/evidence, residual gap, single cheapest killer, rapid reviewer summary |

## Loading Rules

- Load full primary-source passages only for the current decision; otherwise use evidence summaries plus locators.
- For worker/subagent dispatch, transmit only the minimal targeted entity fields (see [templates/worker-task-packet.yaml](../templates/worker-task-packet.yaml)), never full multi-state ledgers.
- Include killed/superseded records only when genealogy, rollback, or reviewer risk needs them.
- A stale report cannot override a newer registry; mark synchronization debt.
- If the context cannot fit, prioritize fatal threats, blocking integrity, and decision dependencies over broad background.

## Output

Record loaded snapshot/version and context manifest in the task/decision log so worker results can be checked for staleness.
