# Hypothesis Protocol

## Gap Classification

Distinguish:

- `G_A_MISSING_OBSERVATION`: a phenomenon has not been measured reliably.
- `G_B_MISSING_EXPLANATION`: an observation exists but mechanism is unresolved.
- `G_C_MISSING_SOLUTION`: cause is sufficiently understood but intervention is inadequate.

Prefer G_B, then G_A, before G_C when building a scientific-method project. A missing solution alone easily becomes module search.

## Mechanism Bridge

Build:

```text
known relation A → missing link → known relation B
```

Tag both known relations with evidence IDs and status. The missing link must be a precise relationship, not a technique name.

## H0–H3 Ladder

- `H0_DESCRIPTIVE`: phenomenon exists under stated conditions.
- `H1_ASSOCIATIONAL`: diagnostic variable covaries with outcome.
- `H2_MECHANISTIC`: an internal mechanism explains the association.
- `H3_INTERVENTIONAL`: changing the mechanism variable changes the predicted outcome.

Do not jump from H0 to H3. Register the evidence and prediction required for each upgrade.

## Core Hypothesis Contract

A hypothesis records observation gap, known mechanism A/B, missing link, scope/conditions, mechanism chain, predictions, alternatives, falsifiers, evidence, unknowns, confidence, and status. It must be method-free: state what relationship should hold, not which new module should win.

## Predictions

Every active hypothesis needs at least one observable prediction that is more specific than the hypothesis. Record:

- construct and operationalization;
- condition/stratum;
- expected direction, ordering, or bounded pattern;
- expected outcome if false;
- diagnostic metric and acceptable alternatives;
- confounders;
- linked falsifier and decision impact.

Do not invent unjustified numeric thresholds. Project decision thresholds must be labeled as preregistered internal criteria, not field facts.

## Competing Hypotheses

Maintain 2–4 credible alternatives. At minimum include the simplest explanation and the strongest artifact/confounder explanation when applicable. Do not create straw alternatives; give each supporting evidence, prediction, and a distinguishing experiment.

## Conceptual Stitching

Apply the novelty protocol’s name-removal, dependency, prediction, necessity, minimality, reviewer-compression, and mathematical-object tests before activation. Failure to generate a new prediction is strong evidence of stitching.

## HARKing Prevention

Before examining new experiment results, freeze hypothesis version, primary predictions, primary stratification, metrics, falsifiers, and GO/HOLD/KILL criteria. Post-result explanations become new hypothesis versions marked `POST_HOC`; they cannot retroactively satisfy the original prediction.

## Lifecycle

Use `DRAFT`, `ACTIVE`, `WEAKENED`, `INVALIDATED`, `SUPERSEDED`, or `SUPPORTED_NOT_PROVEN`. Never use `VERIFIED` for a scientific hypothesis. Preserve scope refinements in genealogy.

## Activation Gate

Activate only if:

- residual gap and novelty boundary are explicit;
- mechanism bridge is understandable without method names;
- at least one prediction and falsifier exists;
- 2–4 alternatives exist;
- diagnostic access appears possible;
- claim language matches evidence and scope.

Otherwise return to S10/S11 or create blocking debt.
