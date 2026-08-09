# Evidence Protocol

## Evidence Hierarchy

Prefer sources by the decision they can support:

1. Primary paper, supplement, official proceedings, official dataset/benchmark specification.
2. Official code, configuration, checkpoint metadata, author project page.
3. Independent replication or carefully matched empirical study.
4. Scholarly index, survey, or review for discovery and context.
5. Blog, social post, search snippet, or model recollection for leads only.

Venue prestige and citation count do not replace directness. Weak papers and preprints still count as prior-art existence.

## Evidence Unit

Create an `EU-` record for the smallest decision-relevant support or counter-evidence. Required fields are defined in [../schemas/evidence-schema.md](../schemas/evidence-schema.md). Always include source locator, exact scope, evidence type, directness, polarity, epistemic interpretation, extractor, verification status, and affected claims.

## Evidence Types

Use controlled values: `TEXTUAL_CLAIM`, `EQUATION`, `ALGORITHM`, `EXPERIMENT`, `ABLATION`, `FIGURE`, `TABLE`, `LIMITATION`, `FAILURE_CASE`, `CODE`, `CONFIG`, `DATASET_SPEC`, `NEGATIVE_RESULT`, or `REPLICATION`.

## Directness and Strength

- `DIRECT`: source directly measures or states the same construct under scope-matched conditions.
- `INDIRECT`: supports a mechanism link or adjacent scope.
- `SPECULATIVE`: suggests a possibility; cannot establish a factual claim.

Rate strength `STRONG`, `MODERATE`, or `WEAK` from source quality, construct validity, scope match, controls, and reproducibility. A direct poorly controlled result can remain weak.

## Primary-source Requirement

Require a primary source before:

- formal T4/T5 threat assignment;
- exact novelty-boundary statements;
- equation or algorithm comparisons;
- claims about training/inference differences;
- benchmark, venue, year, or authorship assertions;
- code-dependent feasibility decisions.

If unavailable, keep status `UNVERIFIED`, record a blocking debt, and avoid a fatal decision based solely on metadata or summaries.

## Paper Families

Group preprint, conference, journal extension, supplement, official code, erratum, and sequel under a `PF-` family. Do not count family members as independent evidence. Choose a canonical paper entry and preserve version-specific locators.

## Evidence Independence

Track whether sources share authors, data, code, benchmark, model outputs, or a common cited result. Multiple papers repeating the same unverified assertion are one evidence lineage, not independent confirmation.

## Claim-level Provenance

Each `CL-` claim links supporting, opposing, and scope-limiting evidence IDs. Each evidence unit lists affected claims. Reject orphan claims and evidence units with no source locator.

## Evidence Propagation

When evidence changes:

1. identify directly affected claims;
2. recalculate only explicit dependency descendants;
3. choose `WEAKENED`, `INVALIDATED`, `SUPERSEDED`, or unchanged;
4. recalculate dependent threats, candidates, hypotheses, predictions, and decisions;
5. open contradictions rather than overwriting conflicts;
6. append decision history and version links.

Never automatically KILL all descendants. Some dependencies are supportive, not necessary.

## Negative Evidence

Store genuine failed predictions, matched-baseline disappearance, replication failure, or contrary measurement as `NEGATIVE_RESULT`. Distinguish:

- `NEGATIVE_EVIDENCE`: an observation contradicts a prediction or claim.
- `NOT_EXPLICITLY_ADDRESSED`: a source did not investigate the issue.
- `NO_EVIDENCE_FOUND`: current search has not found support.
- `EVIDENCE_OF_ABSENCE`: a valid design supports bounded absence.

## Commit Checklist

- Source and locator resolve.
- Paper-family duplicate checked.
- Evidence type/directness/strength are justified.
- Scope and conditions are explicit.
- Interpretation is not stronger than content.
- Supporting and opposing evidence are both linked.
- Independence is recorded.
- Contradictions and debt are updated.
- Claim graph propagation is staged before commit.
