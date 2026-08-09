# Threat Schema

## Required Fields

`TH-` ID, candidate/source/family IDs, T0–T5 level, lifecycle status, reading tier, dimension overlap, evidence IDs, affected claims, strongest reasonable interpretation, residual gap, confidence, formal-verification flag, and history.

## Validity

- Threat belongs to one candidate version and one source family.
- Level reflects core overlap and scope, not lexical similarity or venue prestige.
- Preliminary T4/T5 from R0–R2 cannot be formal.
- Formal T4/T5 requires R3 primary evidence; R4 when implementation is decision-critical.
- T5 additionally satisfies all conditions in novelty protocol and records which core claim/question/hypothesis/method collides.
- Level changes append old/new level, evidence, rationale, decision ID, and timestamp.

## Impact

T3 requires boundary review. T4 requires innovation peeling and dependent claim review. T5 freezes the candidate; near-zero residual triggers emergency gate. A weak paper can be T5 if prior-art existence and scope overlap are verified.

## Resolution

Use `WEAKENED`, `RESOLVED`, `SUPERSEDED`, or `INVALIDATED` only from verified evidence or changed candidate boundary. Age, inconvenience, citation count, or poor experiments do not decay threat level.
