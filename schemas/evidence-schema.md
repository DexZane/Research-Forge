# Evidence Schema

## Required Fields

ID, source type/ID/version, locator, evidence type, bounded summary, scope, directness, strength, polarity, epistemic interpretation, reading tier, verification status, independence group, affected claims, extractor, and timestamp.

## Validity

- `EU-` ID is immutable.
- Locator must resolve to page/section/figure/table/equation or code path+version as appropriate.
- Decision-grade paper evidence must reference a canonical paper-family member.
- `FACT` interpretation requires verified direct evidence and bounded scope; indirect/speculative evidence cannot alone establish it.
- T4/T5 evidence must be primary and R3/R4.
- `CODE` evidence requires repository and commit/release.
- Search snippets/secondary summaries cannot be marked primary verified.
- `AL-` awareness-only leads cannot be evidence sources; resolve them to a sourced `P-`/primary artifact before extracting evidence.

## Independence

Shared paper family, authorship lineage, data, code, benchmark result, or copied citation maps to the same independence group unless justified. Evidence count does not imply independence.

## Negative Semantics

Use polarity `OPPOSES` for observed counter-evidence. Absence from a paper is `NOT_EXPLICITLY_ADDRESSED` in interpretation, not a negative result. An empty search is `NO_EVIDENCE_FOUND`, never evidence of absence without a valid design.

## Cross-record Invariants

Every evidence unit must affect at least one claim, threat, contradiction, hypothesis, or decision. Every listed affected claim must exist. Contradictory direct units require a `CT-` record before affected high-confidence claims can remain active.
