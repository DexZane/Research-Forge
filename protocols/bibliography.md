# Bibliography and Zotero Export Protocol

## Purpose

Capture bibliographic metadata while literature is being searched, preserve its provenance and verification state, and produce one deterministic citation file for user-controlled Zotero import. This protocol handles citation metadata only. It does not replace the evidence ledger, full-text acquisition, R0–R4 reading, or research notes.

## Canonical record

Every discovered paper is represented by one `P-` paper record in the project paper registry. Search results are merged into that record rather than copied into a separate citation list. A record keeps:

- `paper_id` and `family_id` for Research Forge identity;
- title, ordered authors, year, venue, publication type, and identifiers;
- `source_ids` and source URLs for provenance, plus the search session that found it;
- `verification_status` (`UNVERIFIED`, `PARTIALLY_VERIFIED`, or `VERIFIED`);
- `reading_tier`, `evidence_ids`, `conflict_ids`, and `dedup_key`;
- a stable `bib_key` and an `export_eligible` flag;
- a reading priority, decision role, required verification locators, and optional suggested Zotero tags; and
- optional raw/canonical BibTeX only after metadata normalization.

BibTeX fields are a projection of the paper record. They are never the source of truth for claims, threats, hypotheses, or evidence.

## Capture during search

For every result reviewed in a search session:

1. Create a provisional `P-` record or merge it into an existing paper family.
2. Store the exact identifier and source URL used to find it; a search snippet alone is not a verified citation.
3. Normalize title whitespace, author order, year semantics, DOI prefixes, and URL forms without inventing missing values.
4. Record the search session, intent, cutoff date, relevance decision, and any source conflict.
5. Upgrade `verification_status` only after the metadata is checked against an appropriate primary or authoritative index source. Never fabricate a field to make a record exportable.

Use the source routing and fallback chain in the academic-search workflow: CrossRef/publisher, arXiv/OpenReview, PubMed, and other scholarly indexes as appropriate to the paper type. Distinguish preprint date, online publication date, conference year, and journal year.

## Deduplication and conflicts

Merge records in this order:

1. normalized DOI;
2. normalized arXiv, OpenReview, or PMID identifier;
3. normalized title + first-author surname + year, using the deduplication rule in the search protocol (including the title similarity threshold).

When a publisher version and a preprint are related, keep one paper family with version metadata; do not erase the preprint provenance. Union all `source_ids`, search sessions, and evidence links. Prefer the most complete authoritative metadata, but preserve conflicting values in `conflict_ids` and reasoning debt until reconciled. Never silently overwrite a DOI, author list, venue, or year.

## Verification and export eligibility

`UNVERIFIED` and `PARTIALLY_VERIFIED` records remain useful for discovery and threat search but are not exported. A record may set `export_eligible: true` only when:

- the title and ordered author list are present;
- the year and the type-appropriate venue field are present;
- at least one stable identifier or authoritative source URL is present;
- the metadata has `verification_status: VERIFIED`;
- `conflict_ids` is empty or explicitly resolved;
- the record is not superseded by a canonical version.

Evidence verification and bibliographic verification are separate. A verified citation is not automatically evidence for any claim, and an R0/R1 paper may still be exportable if its citation metadata is authoritative; reading depth remains in the paper record.

## Stable BibTeX keys

Use `rf_<paper_id>` in lowercase, for example `rf_p0001`. The key is assigned once and never regenerated from a changing title or author string. This prevents duplicate keys when a paper gains a DOI or changes from preprint to published version.

## BibTeX projection

Select entry type from the verified publication type:

- `@article`: `author`, `title`, `journal`, `year`;
- `@inproceedings`: `author`, `title`, `booktitle`, `year`;
- `@phdthesis`: `author`, `title`, `school`, `year`;
- `@book`: `author` or `editor`, `title`, `publisher`, `year`;
- `@misc`: `author`, `title`, `year`, and a verified `url` for preprints or reports when no more specific type is justified.

Add `doi`, `url`, `eprint`, `archivePrefix`, `pmid`, `publisher`, `volume`, `number`, and `pages` only when verified. Preserve title case with braces when needed, escape BibTeX-special characters, use `and` between authors, and normalize page ranges to double hyphens. Do not include a guessed venue, page range, volume, issue, or year. Sort entries by `bib_key` and fields in the template order so repeated exports are byte-stable.

## Export contract

The default citation artifact is exactly:

```text
<research-project>/exports/references.bib
```

At S03/S04, export may be refreshed for inspection. At S18, after freshness and integrity checks, the orchestrator must regenerate the file from all `export_eligible` records, validate entry count and required fields, and link the artifact from the experiment dossier and handoff. An explicit user request may trigger the same export before S18, but it never bypasses verification or a pending human gate.

The `.bib` file contains citation metadata only. Research Forge keeps provenance, evidence IDs, conflicts, reading tiers, and reading priorities in the project registry/dossier so Zotero import cannot flatten scientific uncertainty.

## Reading Queue

Generate `exports/reading-queue.md` beside `exports/references.bib` whenever an export is refreshed for decision-critical reading and during S18. The queue projects verified or explicitly provisional paper records into `IMMEDIATE`, `NEXT`, `BACKGROUND`, or `DEFERRED` reading priority, required tier, decision role, and exact locators to verify. It may suggest portable workflow tags such as `rf:read-next`, but it must not claim that BibTeX created Zotero collections, downloaded PDFs, or verified evidence.

The user remains in control of Zotero import, collections, tags, annotations, and any API authorization. Do not write to a Zotero library unless the user explicitly authorizes a host with that capability; a file-based `.bib` handoff remains the portable default.

## Failure and recovery

If a record lacks a required field, has an unresolved conflict, or cannot be serialized safely, leave it out of `references.bib`, record the blocking debt, and report the excluded `P-` IDs. Keep such a paper visible in the reading queue only when the queue labels its metadata and evidence limitations. Never write a partial file over a known-good export: write a temporary candidate, validate it, then commit it as a transaction. A failed export sets the project to recovery handling without changing scientific decisions.
