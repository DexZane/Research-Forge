# Boot Protocol

## New Project

1. Select a separate project root; never write project state inside the Skill.
2. Instantiate `project-bootstrap.yaml` and required directories/registries, including research-question, fit, opportunity-signal, literature-triage, implementation-leverage, paper bibliography fields, and the `exports/references.bib` artifact path.
3. Create `PROJECT.md`, `research_state.yaml` at S00, initial decision log, and immutable bootstrap snapshot.
4. Validate IDs, paths, schema version, and permissions.

## Existing Project

Load research state, latest immutable snapshot, active research-question canvas and fit card, verified and decision-critical opportunity signals, gate-critical literature-triage entries/access debt, active implementation-leverage plan/source revisions, active candidates/hypotheses, T4/T5 threats, active claims, contradictions, blocking debt, search status/cutoff, bibliography registry/export status, and last decisions. Compare state/registry/report versions and pending gate. Resume only after validation.

## Corrupted or Partial Project

Set `RECOVERY_REQUIRED`; do not guess missing facts. Inventory files, parseability, versions, snapshots, transaction markers, and reports. Follow recovery protocol and write a recovery decision before state work.

## Boot Output

Produce an Active Research Context with project/state/version, pending gate, decision-critical IDs, blocking integrity problems, and the next legal action. If a gate is pending, return `WAITING_FOR_GATE` without dispatching forward work.
