# Experiment Handoff

## Preconditions

G4 explicitly approved GO; S18 dossier validates; final freshness/integrity checks pass; no unresolved fatal threat/contradiction/reviewer issue; scientific and execution decisions are explicit.

## Package

Deliver human dossier plus `experiment-handoff.yaml` with project/snapshot/version, candidate, locked hypotheses/predictions/diagnostics, first E0 experiment, controls, fair baselines, datasets, hooks, preregistered decisions, resource assumptions, unknowns, exact next action, and a link to the validated `exports/references.bib` plus its record count and excluded paper IDs.

## Downstream Contract

The experiment/coding agent may implement and execute the specified experiments, record environment/code/data versions, and return evidence-linked results. It must not silently change novelty boundary, locked hypotheses, primary predictions/metrics, or decision thresholds.

If implementation reveals an invalid assumption, inaccessible hook, new prior art, confounder, or required scientific change, stop and route back to Research Forge recovery/rollback/gate.

## Result Return

Return experiment ID/version, preregistration version, code/data/environment identifiers, raw artifact paths, validity outcome, metric results with uncertainty, deviations, negative evidence, and proposed claim/hypothesis updates. Research Forge remains the authority for scientific state changes.

## Completion

Handoff is complete when both artifacts resolve all referenced IDs/versions, the bibliography export is deterministic and metadata-only, and the downstream first action is executable without inventing scientific choices.
