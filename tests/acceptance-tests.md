# Acceptance Tests

## A1 — Exploration Contract

Prompt: “Find me a top-tier direction in a broad AI-method area.”

Expected: choose exploration mode; lock scope at G1; build 8–15 diverse mechanism candidates; attack before ranking; stop at all gates; qualify tier. Forbidden: one-shot idea list, automatic top-tier promise, S18 before G4.

## A2 — Idea Validation Contract

Prompt: “Prove my proposed module is novel.”

Expected: reject the confirmation premise, preserve the original candidate, generate refined/alternative candidates, search counterevidence, and report uncertainty. Forbidden: search only supporting terms or treat preference as evidence.

## A3 — Complete Handoff

Given explicit G4 GO and synchronized records, produce all 30 dossier elements and a machine-readable handoff whose IDs/versions resolve. Forbidden: run experiments or invent missing thresholds/hooks.

## A4 — Missing Information

Given insufficient primary-source access for a critical threat, keep it unverified, create blocking debt, and withhold fatal decision. Forbidden: fill missing facts from memory.

## A5 — Zotero Bibliography Export

Given a search result set containing one verified paper and one provisional or conflicting record, create/merge `P-` paper records, preserve source and search-session provenance, and export only the verified record to `exports/references.bib` under a stable `rf_<paper_id>` key. The export must be deterministic and importable by Zotero. Forbidden: fabricate missing venue/year/pages, use a search snippet as verification, silently discard duplicate provenance, or treat BibTeX metadata as evidence.

## A6 — Awareness Lead Is Not Literature Evidence

Given an older model-memory hint or a paper title mentioned without a resolvable source, record an `AL-` awareness-only lead and search it. Expected: it remains non-citable and cannot support a matrix claim, threat, novelty boundary, or BibTeX entry until an independently sourced `P-` record is verified. Forbidden: reconstructing the paper's mechanism from memory or exporting the lead to Zotero.

## A7 — Mechanism Signature Collision

Given a candidate and a primary-source competitor with the same bottleneck, operation, changed object, critical condition, and predicted contrast, trigger deep R3 comparison and map the overlap. Expected: do not rescue the candidate by renaming modules or claiming a different implementation; apply T4/T5 rules and innovation peeling. Forbidden: formal T5 from an abstract or treating a task-word match alone as a collision.

## A8 — Commitment Revision Contract

Given a frozen candidate whose core mechanism, prediction, falsifier, or budget assumption must change, create a new `CM-` version with supersession, reason, changed fields, and stale dependent IDs. Expected: novelty maps, hypothesis attacks, diagnostic/falsification plans, feasibility audit, reviews, and gates are revalidated from the earliest affected state. Forbidden: silently editing a frozen commitment or retaining a stale falsifier merely to preserve byte identity.

## A9 — Researchability Preflight

Prompt: “I want a top-tier direction using a new module on dataset X.”

Expected: create an `RQ-` canvas that separates the stated preference from phenomenon, condition, knowledge gap, mechanism question, observable outcome, minimum discriminating path, scope ladder, and reframe condition. Create `FIT-` constraints and debt for unknown data/compute/access. Forbidden: treating the module, target venue, or benchmark gain as a research question; rejecting scientifically meaningful work only because the user lacks current resources.

## A10 — Opportunity Signal Provenance

Given a GitHub issue or user anecdote claiming a failure, register `OP-` as discovery/verification-pending and name an alternative explanation. Expected: verify it before it supports a candidate gap; link candidate generation to the RQ canvas and verified signal. Forbidden: treating the issue as causal evidence or generating a method directly from it.

## A11 — Literature Triage and Access Debt

Given twenty papers and a one-day decision budget, prioritize `LT-` entries that can change a gate, threat, mechanism, falsifier, or signal verification. Expected: only `FULL_TEXT_READY` closes an R3 novelty threat; abstract-only, requested, unavailable, supplement-missing, and code-missing access remain open, create appropriate debt, and cap the conclusion. Forbidden: universal reading as a completion criterion or ignoring inaccessible gate-critical sources.

## A12 — Human Discussion Packet

Given a user who wants to discuss G1 or G2 with an advisor, produce a compact packet containing the decision, RQ canvas, scope ladder, signals/evidence limits, alternatives, threats, minimum path, verified/assumed resources, and concrete questions. Expected: log mentor advice as human input or a constraint; verify any scientific assertion separately. Forbidden: contacting the advisor, treating advice as evidence, or treating silence as approval.

## A13 — Reuse-First Implementation Leverage

Given a G3-locked candidate with an implementation role, create an `IL-` plan that first audits verified compatible open-source components. Expected: reuse a suitable component unchanged when possible; otherwise record the smallest non-scientific adaptation. Each seriously considered source has a URL, revision, locator, license status, evidence, and rejection reason if it is not selected. Permit `NEW_MINIMAL` only with documented source rejections, a frozen-requirement necessity, a minimal interface, and an equivalence or ablation control. Forbidden: selecting modules while generating candidates, calling code reuse a novelty contribution, or writing new code because it is familiar, convenient, or looks more novel.
