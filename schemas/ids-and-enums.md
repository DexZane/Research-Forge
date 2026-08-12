# IDs and Enums

This file is the canonical vocabulary. Templates illustrate records; other files must not invent synonyms.

## Stable ID Prefixes

| Prefix | Entity |
|---|---|
| `P-` | paper |
| `PF-` | paper family |
| `EU-` | evidence unit |
| `IG-` | evidence-independence group |
| `CL-` | claim |
| `C-` | candidate |
| `CM-` | candidate core commitment |
| `IS-` | innovation signature |
| `AL-` | awareness-only literature lead |
| `RQ-` | research-question canvas |
| `FIT-` | project fit card |
| `OP-` | opportunity signal |
| `LT-` | literature-triage entry |
| `TH-` | threat |
| `CT-` | contradiction |
| `H-` | hypothesis |
| `PR-` | prediction |
| `DM-` | diagnostic metric |
| `EX-` | experiment |
| `RD-` | reasoning debt |
| `SS-` | search session |
| `D-` | decision |
| `G-` | gate decision |
| `PV-` | peer-review report |
| `RISK-` | risk |
| `TX-` | transaction |
| `SNAP-` | immutable snapshot |

Use uppercase prefix, hyphen, and zero-padded project-local sequence. IDs are immutable and never reused.

The research project itself uses an immutable slug-like ID such as `research-project-0001`; it is not a `P-` paper record.

## Epistemic Status

`FACT`, `INFERENCE`, `HYPOTHESIS`, `UNKNOWN`.

Use `NONE` only as a field-level sentinel when the schema permits no active value; it is not a lifecycle or epistemic status.

## Record Lifecycle

`DRAFT`, `PRELIMINARY`, `ACTIVE`, `WEAKENED`, `INVALIDATED`, `SUPERSEDED`, `RESOLVED`, `ARCHIVED`. Hypotheses additionally use `SUPPORTED_NOT_PROVEN`; never `VERIFIED`.

Candidate commitment lifecycle: `DRAFT`, `FROZEN`, `SUPERSEDED`, `INVALIDATED`. Awareness-lead status: `OPEN`, `RESOLVED`, `ARCHIVED`; its lineage role is always `AWARENESS_ONLY` until a resolved `P-` record is independently verified.

## Confidence

`HIGH`, `MEDIUM`, `LOW` with mandatory rationale. No bare numeric probability.

- Confidence impact: `NONE`, `DOWNGRADE`, `BLOCK`.
- Record actor: `ORCHESTRATOR`, `WORKER`, `HUMAN`, `EXPERIMENT_AGENT`.

## Modes and Global Status

- Mode: `EXPLORATION`, `IDEA_VALIDATION`.
- Global status: `ACTIVE`, `WAITING_FOR_GATE`, `HOLD`, `COMPLETE`, `RECOVERY_REQUIRED`.
- Search: `ACTIVE`, `NEAR_SATURATION`, `SATURATED`, `BUDGET_EXHAUSTED`.
- Decision: `UNDECIDED`, `GO`, `HOLD`, `REFINE`, `HOLD_RESOURCE`, `KILL`.
- Execution: `UNDECIDED`, `READY`, `HOLD_RESOURCE`, `BLOCKED`.
- Publication tier: `UNASSESSED`, `T1`, `T2`, `T3`, `T4`.

## States and Gates

States are `S00_INTAKE` through `S18_EXPERIMENT_DOSSIER`. Gates: `NONE`, `G1_SCOPE_LOCK`, `G2_PORTFOLIO_REVIEW`, `G3_HYPOTHESIS_LOCK`, `G4_PROJECT_LAUNCH`, `EMERGENCY_NOVELTY_COLLISION`.

## Threat/Reading/Search

- Threat level: `T0`–`T5`.
- Reading tier: `R0`–`R4`.
- Search intent: `SI1_LANDSCAPE` through `SI9_FRESHNESS` as defined in search protocol.
- Directness: `DIRECT`, `INDIRECT`, `SPECULATIVE`.
- Strength: `STRONG`, `MODERATE`, `WEAK`.
- Polarity: `SUPPORTS`, `OPPOSES`, `LIMITS`, `NEUTRAL`.

## Papers and Evidence

- Publication: `PREPRINT`, `CONFERENCE`, `JOURNAL`, `WORKSHOP`, `PATENT`, `TECHNICAL_REPORT`.
- Source type: `PAPER`, `CODE`, `DATASET`, `PATENT`, `REPLICATION`, `OTHER_PRIMARY`.
- Evidence type: `TEXTUAL_CLAIM`, `EQUATION`, `ALGORITHM`, `EXPERIMENT`, `ABLATION`, `FIGURE`, `TABLE`, `LIMITATION`, `FAILURE_CASE`, `CODE`, `CONFIG`, `DATASET_SPEC`, `NEGATIVE_RESULT`, `REPLICATION`.
- Verification: `UNVERIFIED`, `PARTIALLY_VERIFIED`, `VERIFIED`.

## Bibliography

Bibliography records reuse the immutable `P-` paper ID and the existing verification enum. The canonical project artifact is `exports/references.bib`; `export_eligible` is a derived boolean, not a new epistemic or lifecycle status. A `VERIFIED` citation is bibliographic metadata only and does not promote evidence, claims, threats, hypotheses, or reading tier.

## Claims, Threats, and Contradictions

- Claim type: `FACTUAL`, `INTERPRETIVE`, `MECHANISTIC`, `NOVELTY`, `FEASIBILITY`, `DECISION`, `BOUNDARY`.
- Dependency edge: `SUPPORTS`, `REQUIRES`, `LIMITS`, `CONTRADICTS`, `SPECIALIZES`, `DERIVES_FROM`.
- Overlap cell: `NONE`, `PARTIAL`, `HIGH`, `SUBSUMES`.
- Contradiction type: `EVIDENCE_CONFLICT`, `PAPER_DISAGREEMENT`, `PAPER_CODE_CONTRADICTION`, `BENCHMARK_CONFLICT`, `VERSION_CONFLICT`, `SCOPE_CONFLICT`.
- Contradiction result: `OPEN`, `RECONCILED`, `CONDITIONED`, `SOURCE_ERROR`, `UNRESOLVED`, `SUPERSEDED`.

## Candidates and Hypotheses

- Genealogy relation: `ORIGIN`, `REFINES`, `NARROWS`, `PIVOTS`, `MERGES`, `SPLITS`, `REVIVES`.
- Candidate novelty: `UNVERIFIED`, `PRELIMINARY_SURVIVOR`, `BOUNDED_SURVIVOR`, `INVALIDATED`.
- Residual gap: `UNASSESSED`, `RG_A_STRONG_SCIENTIFIC`, `RG_B_CONDITIONAL`, `RG_C_METHODOLOGICAL`, `RG_D_EMPIRICAL`, `RG_E_COMBINATION`.
- Hypothesis ladder: `H0_DESCRIPTIVE`, `H1_ASSOCIATIONAL`, `H2_MECHANISTIC`, `H3_INTERVENTIONAL`.
- Prediction pattern: `DIRECTIONAL`, `ORDERING`, `BOUNDED`, `NULL_EXPECTED`, `INTERACTION`.
- Diagnostic validity: `UNASSESSED`, `VALID`, `LIMITED`, `INVALID`.
- Signature subject kind: `PAPER`, `CANDIDATE`.
- Opportunity signal: `BENCHMARK_SLICE_FAILURE`, `REPLICATION_ANOMALY`, `PAPER_LIMITATION`, `NEGATIVE_RESULT`, `DATASET_OR_EVALUATION_ARTIFACT`, `DEPLOYMENT_CONSTRAINT`, `OPEN_TECHNICAL_QUESTION`.
- Opportunity signal lifecycle: `DISCOVERY`, `VERIFICATION_PENDING`, `VERIFIED`, `WEAKENED`, `INVALIDATED`, `ARCHIVED`.
- Fit classification: `HARD_CONSTRAINT`, `PREFERENCE`, `ASSUMPTION`.
- Fit scope feasibility: `READY`, `HOLD_RESOURCE`, `UNKNOWN`, `NOT_APPLICABLE`.
- Literature access: `FULL_TEXT_READY`, `ABSTRACT_ONLY`, `SUPPLEMENT_MISSING`, `CODE_MISSING`, `ACCESS_REQUESTED`, `UNAVAILABLE`, `NOT_APPLICABLE`.

## Experiments

- Experimental stage: `E0`, `E1`, `E2`.
- Cost tier: `F0`, `F1`, `F2`, `F3`, `F4`.
- Execution: `NOT_RUN`, `RUNNING`, `COMPLETED`, `FAILED_VALIDITY`, `CANCELLED`.
- Preregistration: `DRAFT`, `PREREGISTERED`, `SUPERSEDED`.

## Review, Debt, and Search Impact

- Reviewer role: `R_N_NOVELTY`, `R_M_MECHANISM`, `R_E_EXPERIMENT`, `R_X_META`.
- Reviewer verdict: `ACCEPTABLE`, `MINOR_CONCERNS`, `MAJOR_CONCERNS`, `FATAL_CONCERN`.
- Reasoning debt severity: `BLOCKING`, `HIGH`, `MEDIUM`, `LOW`.
- Common debt type: `MISSING_PRIMARY_SOURCE`, `MISSING_FULL_TEXT`, `UNCLEAR_RESEARCH_QUESTION`, `UNCLEAR_SCOPE`, `UNRESOLVED_CONTRADICTION`, `MISSING_CONTROL`, `FRESHNESS_GAP`, `BROKEN_PROVENANCE`, `RESOURCE_UNKNOWN`, `CAPABILITY_GAP`.
- Search decision impact: `NONE`, `LOW`, `MEDIUM`, `HIGH`, `FATAL`.
- Gate outcome: `APPROVED`, `REVISE`, `HOLD`, `KILL`, `GO`.

## Human Input

- Human input class: `CONSTRAINT_DECISION`, `DOMAIN_JUDGMENT`, `MENTORSHIP_ADVICE`, `ARTIFACT_POINTER`.
- Human input is neither evidence nor a claim until a linked primary artifact is independently verified under the evidence protocol.

## Forbidden Synonym Drift

Do not create `DEAD`, `REJECTED`, `REMOVED`, or `KILLED` as lifecycle values. Use `INVALIDATED`, `SUPERSEDED`, or `ARCHIVED` plus a decision record explaining KILL.
