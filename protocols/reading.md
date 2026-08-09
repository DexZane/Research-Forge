# Tiered Reading Protocol

## Rule

Reading depth limits permissible judgments. Upgrade only when a decision requires it; do not perform expensive deep reads indiscriminately.

## R0 — Discovery Scan

Read title, abstract, venue/year metadata, and visible keywords. Classify relevance and paper family. May add a discovery lead. Must not assign formal T4/T5, quote exact novelty language, compare mechanisms, or create decision-grade evidence.

## R1 — Relevance Read

Read abstract, introduction, conclusion, figures/tables at a glance, and stated contributions. Determine problem, task, broad approach, and likely relevance. May assign preliminary T1–T3 and request R2. Must not claim detailed equivalence or absence.

## R2 — Mechanism Read

Read introduction, related work, method, core equations, algorithm, experiments, ablations, limitations, and task-specific details. Extract:

- problem and observation;
- explicit vs inferred hypothesis;
- mechanism chain and mathematical object;
- data, representation, assignment, loss, training, inference, and efficiency changes;
- evidence, limitations, failure cases, and what is not addressed (marked `INFERENCE`).

R2 is required for the formal paper matrix.

## R3 — Threat Deep Read

Use for T4/T5 and novelty-boundary-critical papers. Read the primary paper in full plus supplement/appendix and version history. Verify exact claim language, definitions, equations, pseudocode, training/inference distinction, ablations, controls, limitations, failure cases, and comparisons. Create evidence units with locators and a dimension-by-dimension overlap table.

R3 must answer whether overlap concerns problem, observation, hypothesis, task, formulation, mechanism, training, inference, or experiment—and what residual difference survives.

## R4 — Code/Replication Read

Start with a precise verification question. Inspect official code, configs, commits/releases, checkpoints, data processing, training recipe, inference path, and metric implementation only as needed. Record code locator/version and answer. Do not wander through code without a decision question.

Use R4 when implementation affects novelty, fairness, feasibility, reproducibility, or a paper–code contradiction.

## Upgrade Rules

- Backbone anchor or matrix entry: at least R2.
- Preliminary T4/T5: upgrade to R3 before formal threat status.
- Implementation-critical T4/T5 or feasibility issue: R4.
- Source inaccessible: retain `UNVERIFIED`, open debt, and limit judgment.

## Paper–Code Contradiction

Do not silently privilege either source. Create a contradiction record, identify version mismatch or undocumented behavior, lower affected confidence, and seek author clarification, release notes, or independent replication where material.

## Reading Output

Every read records paper ID/family, tier, scope, sections inspected, extracted evidence IDs, unresolved questions, contradictions, confidence, and recommended next depth. “Read” without a tier and coverage statement is invalid.
