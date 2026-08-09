# S10 — Residual Gap

## Purpose

Subtract verified prior art from the candidate, record killed claims, and stabilize an honest novelty boundary.

## Entry Conditions

S09 threat-critical search completed or an emergency collision resolved to local damage/major reframe.

## Reads

Candidate, claims, formal threats/evidence, closest competitors, genealogy, contradictions, search coverage.

## Writes

Killed claims, peeling operations, updated genealogy, residual-gap class, positive/negative novelty boundary, confidence and debt.

## Required Questions

Which exact claims died, which source/evidence killed each, why is overlap direct, what specifically survives, and is the survivor still scientifically meaningful?

## Required Actions

Apply P1–P4 peeling; update dependent claims/candidates; run stitching and residual-quality tests; write “not first” statements and the one precise remaining question.

## Required Protocols

[Novelty](../protocols/novelty.md), [Evidence](../protocols/evidence.md), [Reasoning](../protocols/reasoning.md), [Transaction](../runtime/transaction.md), [Integrity](../protocols/integrity.md).

## Parallelizable Work

Dimension-by-dimension overlap proposals per closest competitor; central peeling is sequential.

## Sequential Work

Verify threats → kill claims → propagate → assess residual → commit boundary.

## Required Outputs

`reports/residual-gap.md`, `reports/novelty-boundary.md`, killed-claim list, genealogy, updated claim/candidate/threat ledgers.

## Exit Conditions

Remaining question is precise, boundary stable for searched scope/cutoff, no unresolved fatal contradiction, and residual is non-trivial; route S11.

## Rollback Conditions

Residual vanishes or becomes trivial: S06; major reframe: S06/S09; search gap: S09.

## Kill Conditions

No meaningful residual after strongest prior art, or survivor is only RG_E combination/implementation trivia without new prediction.

## Forbidden Actions

Do not use unqualified first/never/unexplored language or hide killed claims.

## Gate Behavior

No normal gate; near-zero residual from new prior art invokes emergency gate.
