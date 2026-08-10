# Active Context Loading

## Minimal Context Rule

Load IDs and decision-relevant fields, not entire project history. Always include current state/iteration/version, pending gate, active candidates/hypotheses, T4/T5 threats, open blocking contradictions/debt, bibliography export status, latest snapshot, and last major decisions.

## State Groups

| States | Add to context |
|---|---|
| S00–S01 | intake, project constraints, resource profile |
| S02–S05 | scope, concept dictionary, research lines, coverage map, anchor papers/bibliography/evidence |
| S06–S08 | candidate registry/genealogy, red-ocean constraints, preliminary threats, score rationale |
| S09–S10 | finalist versions, query graph, closest competitors, all T4/T5 evidence, claims, contradictions |
| S11–S12 | boundary/residual, mechanism claims, hypotheses, predictions, alternatives, falsifiers |
| S13–S15 | locked hypothesis version, diagnostics, experiments, baselines/confounders, resources/code evidence |
| S16–S17 | immutable dossier, independent reviewer reports/meta-review, hard gates, risks |
| S18 | G4 decision, all active dossier IDs/versions, freshness/integrity results, bibliography export status, handoff template |

## Loading Rules

- Load full primary-source passages only for the current decision; otherwise use evidence summaries plus locators.
- Include killed/superseded records only when genealogy, rollback, or reviewer risk needs them.
- A stale report cannot override a newer registry; mark synchronization debt.
- If the context cannot fit, prioritize fatal threats, blocking integrity, and decision dependencies over broad background.

## Output

Record loaded snapshot/version and context manifest in the task/decision log so worker results can be checked for staleness.
