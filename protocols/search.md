# Literature Search Protocol

## Search Intents

Declare one intent per search session:

- `SI1_LANDSCAPE`
- `SI2_BACKBONE`
- `SI3_MECHANISM`
- `SI4_CANDIDATE_GAP`
- `SI5_ADVERSARIAL_NOVELTY`
- `SI6_COMPETITOR`
- `SI7_DIAGNOSTIC`
- `SI8_CODE_IMPLEMENTATION`
- `SI9_FRESHNESS`

Record target decision, concepts, scope, cutoff date, source routes, queries, exclusions, results, and marginal decision impact.

## Concept Dictionary

For each core concept record canonical term, synonyms, historical terminology, mathematical terms, task-specific terms, neighbor mechanisms, and excluded homonyms. Expand temporally: older papers may use different language for the same mechanism.

## Query Graph

Decompose candidate `A+B+C+D` and search:

1. single concepts;
2. pairwise combinations;
3. selected triples;
4. full candidate;
5. problem, observation, mechanism, solution, and mathematical formulations;
6. venue-, author-, and code-specific variants.

Do not search only the full phrase. Deduplicate queries by semantic intent and keep the query that adds distinct coverage.

## Source Routing

Route by purpose:

- official proceedings/publisher and primary paper for claims;
- arXiv/OpenReview for freshness and version discovery;
- official project/code for implementation questions;
- scholarly indexes for discovery, citation chaining, and metadata cross-check;
- surveys for taxonomy and leads only;
- blogs/social posts for leads only.

Verify venue and publication year; distinguish preprint date, online date, conference year, and journal year.

## Discovery and Chaining

Search three circles: exact task, exact mechanism, mechanism intersection. For anchor and T4/T5 papers perform backward, forward, lateral, author, and sequel chaining. Group duplicate versions into paper families.

## Paper-family normalization

Merge paper records by normalized DOI first. If DOI is absent, use a normalized arXiv/OpenReview/PMID identifier; otherwise compare normalized title tokens and first-author surname, treating records as the same family only when the surnames match and title Jaccard similarity is at least `0.90`. Normalize DOI prefixes and case, remove punctuation/English stopwords from title tokens, and collapse whitespace. Preserve every source, version, and search-session provenance after a merge; unresolved metadata disagreement becomes a contradiction or reasoning debt.

## Mechanism-neighborhood Expansion

Cross domains only after writing a transfer question: what mathematical object or mechanism is shared, and which task assumptions differ? Cross-domain work can weaken mechanism originality while leaving task-specific question novelty intact.

## Threat-driven Search

For finalists, generate reviewer queries that could complete:

> This work is incremental because Paper X already …

Search exact collisions, terminology collisions, historical collisions, neighboring-domain collisions, and latest collisions. Search counter-claims and null results, not only supporting work.

## Freshness

Prioritize the most recent 24 months during S09 and run a final freshness sweep before G4. Check candidate title terms, core mechanism terms, closest-competitor citations, relevant proceedings, OpenReview, journals, arXiv, official projects, and code. Record an explicit cutoff date; never claim “latest” without a current search.

Reopen search when scope, candidate, hypothesis, novelty boundary, threat, new paper, or long project duration changes a decision-relevant query.

## Saturation

Use `ACTIVE → NEAR_SATURATION → SATURATED` or `BUDGET_EXHAUSTED`. Evaluate marginal decision impact, not result count. A batch has impact if it changes taxonomy, backbone, closest competitor, threat, boundary, hypothesis, falsifier, feasibility, or confidence.

Mark `NEAR_SATURATION` only when coverage cells are filled, critical chains are complete, recent sources are checked, and new queries mostly duplicate known families. Mark `SATURATED` only when two meaningfully different batches add no decision-relevant change and critical unknowns are non-searchable or explicitly bounded. `SATURATED` does not prove global novelty.

Use a safety cap to stop unbounded search; if it fires first, use `BUDGET_EXHAUSTED`, list uncovered cells, and downgrade confidence.

## Search Coverage Map

Track coverage over task, failure mode, mechanism, mathematical object, historical line, recent frontier, closest competitors, negative/counter evidence, code, and datasets. Record missing cells as reasoning debt.

## Reproducibility

Save exact query, date, source, filters, results reviewed, paper families added, decision impact, and next query. Never report a search as complete from memory or a single search engine.

## Bibliographic capture

During the same search pass, create or merge a `P-` paper record and capture its DOI/arXiv/OpenReview/PMID identifier, source URL, ordered authors, title, venue, publication-year semantics, and `SS-` search-session provenance. Apply [Bibliography](bibliography.md) immediately: provisional records may support discovery and threat search, but only `VERIFIED` records with no unresolved conflicts become `export_eligible` and enter the final `exports/references.bib` Zotero artifact. BibTeX export does not upgrade reading depth or evidence status.
