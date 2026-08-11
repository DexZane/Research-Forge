# Integrity Protocol

Run these audits before gates, formal T4/T5 changes, candidate KILL, project decisions, and handoff.

## Epistemic Integrity

- Every consequential statement has `FACT`, `INFERENCE`, `HYPOTHESIS`, or `UNKNOWN` status.
- No unsupported promotion occurred.
- Evidence insufficiency is not described as disproof.
- Confidence and scope match available evidence.

## Evidence Integrity

- Primary sources support decision-critical claims.
- Evidence units have locators, scope, directness, strength, polarity, and independence.
- Paper families are deduplicated.
- Negative/counter evidence and unresolved contradictions are visible.

## Reference Integrity

- Authors, title, venue, year/version, DOI/URL/identifier, equations, and code commit are verified where used.
- Search snippets and secondary summaries are not cited as primary support.
- Freshness cutoff and source coverage are explicit.
- `AL-` awareness-only leads are never used as citations, BibTeX exports, evidence, formal paper-matrix entries, or novelty support.

## State Integrity

- Current state, iteration, pending gate, active IDs, and versions agree.
- Required entry artifacts exist and exit artifacts validate.
- Only legal transitions or recorded rollback/interrupt occurred.
- No partial transaction or stale snapshot remains.
- Active candidates resolve to their active signature and commitment; frozen commitment changes have explicit supersession and dependent-record consequences.

## Report Synchronization

- Human reports reference current registry IDs/versions.
- Killed/superseded claims are not presented as active.
- Threats, boundaries, hypotheses, decisions, and dossier agree with machine state.

## Gate Integrity

- Gate packet contains required evidence, uncertainty, alternatives, costs, and decision options.
- No approval is inferred from silence.
- Forward work is frozen while a gate or emergency is pending.

## Novelty Integrity

- Strongest competitors are steelmanned and T4/T5 are R3/R4 verified.
- Innovation peeling, stitching tests, negative boundary, and freshness sweep are complete.
- “First/never/unexplored” language does not exceed the safety ladder.
- Search saturation is not treated as proof of global novelty.
- Candidate/competitor signature comparisons cover bottleneck, operation, changed object, critical condition, and predicted contrast; a vague signature blocks advancement.
- Outcome-derived pattern frequency, acceptance, or citation statistics were not used as candidate evidence or ranking priors.

## Experimental Integrity

- Hypothesis is method-free and alternatives are credible.
- Diagnostics apply to baselines and have alternative operationalizations.
- Falsifiers and decision criteria were preregistered.
- Baselines, controls, budgets, and confounders are fair/visible.
- Scientific and execution decisions remain separate.
- The preregistered falsification plan and resource assumptions reference the active frozen commitment version.

## Failure Behavior

If a check fails, stop the affected transition. Create or update `RD-` reasoning debt with severity and blocking target. Roll back if an already-committed dependency is invalid. Never hide a failed check inside a summary score.
