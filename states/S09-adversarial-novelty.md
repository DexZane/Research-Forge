# S09 — Adversarial Novelty Attack

## Purpose

Make the strongest practical attempt to prove each finalist non-novel.

## Entry Conditions

G2 explicitly selected 1–3 finalists and search scope/cutoff are current.

## Reads

Version-pinned finalist signatures/commitments, genealogy, claims, all search/paper/bibliography/evidence/threat records, concept dictionary, latest snapshot.

## Writes

Combination query graph, verified competitor citation metadata, deep evidence, signature collision maps, closest-competitor set, formal T0–T5 threats, saturation state, contradictions, emergency packet if triggered.

## Required Questions

Who already studied each component/combination, same question, hypothesis, formulation, mechanism, training/inference behavior, and experiment? Can a reviewer accurately say “incremental because X already…”?

## Required Actions

Pin the candidate signature/commitment version for this audit without changing its lifecycle to `FROZEN`; decompose A+B+C+D; expand synonyms/history/neighbors; prioritize last 24 months; search proceedings/OpenReview/journals/arXiv/projects/code; compare bottleneck, operation, changed object, condition, and predicted contrast against every closest competitor; R3 all T4/T5 and R4 when critical; steelman competitors; run saturation and freshness checks.

## Required Protocols

[Search](../protocols/search.md), [Bibliography](../protocols/bibliography.md), [Reading](../protocols/reading.md), [Innovation Signature](../protocols/innovation-signature.md), [Commitment Integrity](../protocols/commitment-integrity.md), [Novelty](../protocols/novelty.md), [Evidence](../protocols/evidence.md), [Contradiction](../protocols/contradiction.md), [Integrity](../protocols/integrity.md).

## Parallelizable Work

Independent exact, historical, neighbor-domain, latest, citation-chain, and code verification tasks from one frozen candidate version.

## Sequential Work

Verification, contradiction reconciliation, threat assignment, impact propagation, and saturation decision.

## Required Outputs

Threat matrix with signature collision maps, closest competitors, adversarial search log/coverage, formal evidence units, `reports/adversarial-novelty.md`.

## Exit Conditions

Critical threat coverage is `SATURATED` or `BUDGET_EXHAUSTED` with explicit limitations; all formal T4/T5 are R3/R4; route S10.

## Rollback Conditions

Candidate framing changes: S06/S08. Missing backbone: S03/S04. New scope: S01.

## Kill Conditions

Verified T5 with near-zero residual gap after peeling; freeze and route emergency gate before final kill.

## Forbidden Actions

Do not search to confirm, downgrade inconvenient prior art, count duplicate families as independent, or equate saturation with proof of novelty.

## Gate Behavior

Trigger `EMERGENCY_NOVELTY_COLLISION` immediately when conditions hold; no forward work until resolved.
