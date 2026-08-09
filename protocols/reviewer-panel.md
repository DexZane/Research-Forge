# Adversarial Reviewer Panel Protocol

## Roles

- `R_N_NOVELTY`: strongest prior art, T5, terminology overlap, latest work, stitching, contribution compression.
- `R_M_MECHANISM`: unsupported links, correlation/causation, simpler explanations, metric artifacts, mathematical mechanism, hypothesis-to-intervention coherence.
- `R_E_EXPERIMENT`: baseline fairness, controls, data, seeds, tuning, compute, negative results, reproducibility, statistical and construct validity.
- `R_X_META`: reconcile independent reports, classify fatal/resolvable issues, estimate ceiling, and recommend a decision.

## Independence

R_N, R_M, and R_E must receive the same frozen dossier and produce first-pass reports without seeing one another. Freeze those reports before meta-review. Shared language or conclusions do not count as independent evidence.

## Reviewer Output

Each reviewer provides verdict, strongest attack, fatal issues, major/minor issues, required evidence, candidate defense if evidence-backed, confidence, and recommendation. Every issue links affected claim/hypothesis/experiment IDs.

## Reject Simulation

For top-tier candidates, complete and defend against:

```text
This work is incremental because …
The central hypothesis is unsupported because …
The experimental evidence would be insufficient because …
```

Defenses must use evidence, boundary, controls, or a changed claim—not rhetoric.

## Meta-review

Classify issues:

- `FATAL`: cannot be resolved without eliminating the project’s core.
- `RESOLVABLE_BLOCKING`: must be fixed before GO.
- `RESOLVABLE_NONBLOCKING`: plan and disclose.
- `DISAGREEMENT`: reviewer conclusions conflict and need explicit adjudication.

Do not average verdicts. A single verified fatal issue overrides favorable scores. Reviewer disagreement is information; preserve it and identify the discriminating evidence.

## Re-entry

Novelty fatality returns to S09/S10 or KILL; mechanism failure returns to S11/S12; diagnostic/experimental failure returns to S13/S14; resource failure may become `HOLD_RESOURCE`. Rerun only affected reviewers after changes, with versioned dossiers.
