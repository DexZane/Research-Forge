# Research Reasoning Protocol

## Purpose

Make every consequential research judgment traceable from question through evidence, alternatives, falsifier, confidence, and action. Apply the Research Reasoning Frame (RRF) before state exit, candidate kill, threat upgrade, gate, or decision.

## R0 — Epistemic Discipline

Use exactly four epistemic classes:

| Class | Meaning | May support |
|---|---|---|
| `FACT` | Directly supported, scope-matched statement | bounded factual claim |
| `INFERENCE` | Reasonable interpretation derived from facts | explicitly qualified conclusion |
| `HYPOTHESIS` | Testable explanation not established as fact | predictions and tests |
| `UNKNOWN` | Relevant uncertainty not resolved | debt, search, or gate disclosure |

Never promote by repetition, popularity, model confidence, user preference, or absence of contrary evidence. Record the evidence or decision that changes class.

## R1 — Question Decomposition

Decompose into seven slots:

1. `task`: what system and setting?
2. `symptom`: what is observed?
3. `claimed_failure`: what fails, compared with what?
4. `proposed_cause`: why might it fail?
5. `mechanism`: what causal/functional chain is proposed?
6. `intervention`: what variable could be changed?
7. `expected_outcome`: what observation should change?

Mark missing links. A module name, benchmark gap, or performance target is not a scientific question.

## R2 — Evidence-to-Claim

For every claim, assess:

- relevance to the exact task and condition;
- directness: `DIRECT`, `INDIRECT`, or `SPECULATIVE`;
- source and method quality;
- scope match across dataset, scale, architecture, objective, training, and evaluation;
- independent support and counter-evidence.

Constrain claim strength to the weakest critical link. Do not turn “Paper X did not test Y” into “Y does not work.”

## R3 — Mechanism Reasoning

Write a mechanism chain as typed links:

```text
condition → internal variable → operation/interaction → diagnostic signature → outcome
```

Tag every arrow `FACT`, `INFERENCE`, `HYPOTHESIS`, or `UNKNOWN`. Identify the mathematical object changed: data distribution, representation, assignment, objective, gradient, routing, state update, decoding, or metric. Prefer a mechanism gap to a module gap.

## R4 — Competing Explanations

Maintain at least two credible alternatives for every core hypothesis. Draw from representation, optimization, assignment, data quality, annotation, capacity, recipe/tuning, metric artifact, benchmark artifact, or inference protocol. Steelman each alternative and specify a discriminating observation.

## R5 — Adversarial Self-Attack

Run five attacks:

1. `PRIOR_ART`: strongest reasonable overlap.
2. `MECHANISM`: missing or unsupported link.
3. `SIMPLER_EXPLANATION`: less complex cause fits observations.
4. `BASELINE`: effect may vanish under a fairer/stronger baseline.
5. `UTILITY`: even if true, the actionable ceiling may be negligible.

Interpret prior art at its strongest reasonable scope before defending the candidate.

## R6 — Novelty Reasoning

Score separately:

- `N-Q`: research-question novelty;
- `N-H`: hypothesis novelty;
- `N-M`: method novelty;
- `N-I`: implementation novelty.

One cannot substitute for another. Compute the residual conceptually as `candidate claims − verified prior art`; never as a numeric novelty percentage. Write both positive and negative boundaries.

## R7 — Hypothesis Synthesis

A valid core hypothesis is mechanism-grounded, explicit about the missing link, observable, falsifiable, compared against alternatives, and method-free. If it names the proposed module as the cause or intervention, rewrite it.

## R8 — Falsification

Specify direct, mechanism, generalization, and practical falsifiers. Prefer the cheapest high-information discriminating test. A negative result may KILL, REFINE, or narrow scope; preserve it as evidence.

## R9 — Confidence

Record separate confidence for evidence, novelty, mechanism, hypothesis, and decision. Use `HIGH`, `MEDIUM`, or `LOW` plus rationale and downgrade triggers. Never use unsupported decimals.

## R10 — Belief Update

On new evidence, choose `STRENGTHEN`, `WEAKEN`, `INVALIDATE`, `SUPERSEDE`, `SPLIT`, or `NO_CHANGE`. Propagate only through explicit dependency edges. Preserve versions and apply sunk-cost immunity.

## R11 — Decision

Choose one action:

- `CONTINUE`: required state work remains valid.
- `REFINE`: retain the question but alter a bounded component.
- `ROLLBACK`: an upstream assumption or artifact is invalid.
- `HOLD`: evidence is insufficient or a dependency is pending.
- `KILL`: a hard scientific condition fails.
- `ESCALATE_TO_GATE`: human authority is required.

Every action records decision ID, rationale, evidence, alternatives considered, uncertainty, affected IDs, rollback target if any, and next action.

## Research Reasoning Frame

Answer all twelve:

1. What exactly is the question?
2. What is directly known?
3. What is inferred?
4. What remains unknown?
5. What is hypothesized?
6. What are the strongest competing explanations?
7. What is the strongest counter-evidence?
8. What prior art is most threatening?
9. What observation would falsify the belief?
10. Is there a simpler explanation or solution?
11. What is current confidence and why?
12. What action follows?

## Anti-confirmation-bias Gate

Search at least one counter-claim, strongest-competitor, and simpler-explanation path. If the candidate is user-proposed or already costly, increase attack effort rather than confidence. Unresolved evidence is `UNKNOWN`; it is neither confirmation nor disproof.

## Common Failures

- Treating a plausible narrative as a mechanism.
- Treating many indirect citations as direct evidence.
- Conflating failure to find evidence with evidence of absence.
- Protecting a candidate because of sunk cost.
- Using a score to hide a failed hard gate.
