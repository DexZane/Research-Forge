# Novelty Threat and Innovation Peeling Protocol

## Threat Unit

A threat is `Paper/Artifact × Candidate`, not a property of a paper alone. Record overlap dimensions, reading tier, evidence, residual gap, confidence, and affected claim IDs.

## T0–T5

| Level | Meaning | Consequence |
|---|---|---|
| `T0` | irrelevant after review | archive rationale |
| `T1` | background/context | cite; no claim damage |
| `T2` | adjacent problem or mechanism | bound context |
| `T3` | meaningful overlap in one contribution dimension | narrow or defend claim |
| `T4` | strong overlap that removes a major claim or sharply reduces generality | R3 required; peel and reassess |
| `T5` | fatal/near-fatal overlap in core question, hypothesis, or method contribution | freeze affected candidate; emergency gate if residual gap is near zero |

At S07, T5 is only `PRELIMINARY_T5`. Formal T4/T5 requires R3 primary-source evidence, exact overlap mapping, strongest reasonable interpretation, and explicit surviving residual. Use R4 when code behavior is decision-critical.

## T5 Conditions

Assign T5 only when all applicable conditions hold:

1. The source predates or otherwise counts as prior art for the intended claim.
2. Overlap concerns a core claimed contribution, not vocabulary alone.
3. Scope and assumptions substantially match or subsume the candidate.
4. The overlap is verified from primary content at R3/R4.
5. After strongest reasonable interpretation, no non-trivial research question, hypothesis, or mechanism claim survives without a major reframe.

Poor empirical quality does not erase prior-art existence. Distinguish claim collision from execution quality.

## Threat Dimensions

Compare problem, observation, hypothesis, task, mathematical formulation, mechanism, data, representation, assignment, objective/loss, training, inference, experiment, and claimed contribution. Identify the strongest competitor set; do not average threats across many weak neighbors.

## Signature Specificity and Collision

Use `protocols/innovation-signature.md` for every finalist. A candidate signature must name a bottleneck, operation, changed object, critical condition, and predicted contrast. Compare each closest competitor signature along all five fields and link exact evidence. A vague “new framework,” a newly named combination, or a task-level difference cannot be a novelty survivor.

An exact or subsuming signature collision does not automatically mean T5: apply the full T5 conditions. Conversely, a different implementation does not prevent T4/T5 when the competitor already establishes the claimed mechanism and contrast under equal or broader conditions.

Do not use historical acceptance/citation outcomes, pattern frequency, or pattern labels as novelty evidence or candidate ranking priors.

## Innovation Peeling

For each verified overlap, apply one or more:

- `P1_CLAIM_NARROWING`: remove already-known claims.
- `P2_CONDITION_NARROWING`: restrict the setting where the question survives.
- `P3_MECHANISM_NARROWING`: separate the untested mechanism link.
- `P4_METHOD_REMOVAL`: drop a method claim while retaining a scientific question/hypothesis.

Record killed claim, killing source/evidence, rationale, surviving claim, and genealogy relation. Stop peeling and KILL or return to S06 if the survivor lacks scientific generality, mechanistic depth, impact, reviewer clarity, or a non-trivial optimization space.

## Residual Gap Classes

- `RG_A_STRONG_SCIENTIFIC`: unresolved question and mechanism with broad value.
- `RG_B_CONDITIONAL`: meaningful only under explicit conditions.
- `RG_C_METHODOLOGICAL`: method space remains but question/hypothesis novelty is weak.
- `RG_D_EMPIRICAL`: observation missing; explanation unclear.
- `RG_E_COMBINATION`: only a combination appears untried.

`RG_E` does not qualify for top-tier status without a new dependency, prediction, or mechanism.

## Conceptual Stitching Tests

Run all seven:

1. `NAME_REMOVAL`: explain the idea without paper/module names.
2. `DEPENDENCY`: explain why components must connect scientifically.
3. `PREDICTION`: state a new observable prediction created by the connection.
4. `NECESSITY`: identify whether every component is needed.
5. `MINIMALITY/REPLACEABILITY`: test a simpler or interchangeable component.
6. `REVIEWER_COMPRESSION`: can the contribution be dismissed accurately as “X + Y”?
7. `MATHEMATICAL_OBJECT`: identify what object or operation is actually changed.

High stitching risk requires refinement or kill; implementation novelty alone cannot rescue it.

## Novelty Boundary

Write:

```text
We are not the first to study X.
We are not the first to introduce Y.
Existing work A establishes …
Existing work B addresses …
The remaining unresolved question is specifically … under conditions …
```

Separate positive boundary (what may survive) from negative boundary (what is explicitly not claimed). Link every sentence to claim and evidence IDs.

## Claim Safety Ladder

- `N0`: descriptive difference only.
- `N1`: “we investigate whether …”
- `N2`: “to our knowledge, prior work has not directly tested … within searched scope/cutoff.”
- `N3`: first claim within explicit task, assumptions, formulation, sources, and cutoff after global check.
- `N4`: global “first/never/unexplored” claim; avoid unless exhaustive verification and human approval justify it.

Search saturation never automatically licenses N3/N4.

## Adversarial Search

Attack exact, terminological, historical, neighbor-domain, and latest collisions. Generate reviewer queries and counter-claim searches. Finish only when threat-critical coverage is saturated or budget-exhausted with explicit confidence limits.

## Emergency Novelty Collision

Trigger when newly found, provisionally strong prior art may overlap the core claim and reduce residual gap to near zero. Freeze forward work. Verify at R3/R4; stage impact propagation; snapshot; then classify:

- `E_N1_LOCAL_DAMAGE`: peel bounded claims and resume at S10.
- `E_N2_MAJOR_REFRAME`: rollback to S06/S10 and reopen search.
- `E_N3_FULL_COLLISION`: KILL affected candidate after human gate.

Do not continue experiments or dossier work while the emergency gate is open.

## Threat Lifecycle

Threats may be `PRELIMINARY`, `ACTIVE`, `WEAKENED`, `RESOLVED`, `SUPERSEDED`, or `INVALIDATED`. Never decay a threat because it is old, inconvenient, poorly cited, or from a weak venue. Only new verified evidence or a changed candidate boundary can change it, with history preserved.

## Novelty versus Value

Novelty risk and scientific value are separate. A highly valuable question can be non-novel; a novel difference can be scientifically trivial. Publication tier is a downstream judgment, not evidence of novelty.
