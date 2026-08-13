# Bibliography Record Schema

This schema defines the citation-metadata projection of a `P-` paper record. It is intentionally narrower than the evidence and reading schemas.

## Required record shape

```yaml
bibliography_record:
  paper_id: P-0001
  family_id: PF-0001
  bib_key: rf_p0001
  entry_type: article
  title: Verified paper title
  authors:
    - family: Surname
      given: Given name
  year: 2024
  venue: Journal or proceedings title
  identifiers:
    doi: null
    arxiv: null
    openreview: null
    pmid: null
    url: https://example.org/paper
  source_ids: [SS-0001]
  source_urls: [https://example.org/paper]
  dedup_key: doi:10.example/abc
  verification_status: VERIFIED
  reading_tier: R2
  evidence_ids: []
  conflict_ids: []
  export_eligible: true
  reading_plan:
    priority: IMMEDIATE
    decision_roles: [CLOSEST_NOVELTY_THREAT]
    required_verification_locators: []
    suggested_zotero_tags: [rf:read-next]
  captured_at: "2026-08-10T00:00:00Z"
  verified_at: "2026-08-10T00:00:00Z"
  notes: null
```

## Field rules

| Field | Rule |
|---|---|
| `paper_id` | Required immutable `P-` ID; links the export back to the paper registry. |
| `family_id` | Required `PF-` family ID; versions are not silently collapsed. |
| `bib_key` | Required stable `rf_<paper_id>` key; unique within the project. |
| `entry_type` | One of `article`, `inproceedings`, `phdthesis`, `book`, `misc`. |
| `title`, `authors`, `year` | Required for every exportable record; values must be verified. |
| `venue` | Required for articles/proceedings/books/theses; `misc` may use a report/preprint label only when sourced. |
| `identifiers` | DOI, arXiv, OpenReview, PMID, and URL are optional individually; at least one stable identifier or authoritative URL is required. |
| `source_ids`, `source_urls` | Required provenance union; at least one source is required. |
| `dedup_key` | Required normalized DOI/secondary ID/title key used during merge. |
| `verification_status` | Existing enum `UNVERIFIED`, `PARTIALLY_VERIFIED`, `VERIFIED`; only `VERIFIED` can export. |
| `reading_tier`, `evidence_ids` | Preserve scientific reading/evidence links; they do not imply citation export eligibility. |
| `conflict_ids` | Empty for export; unresolved conflicts create reasoning debt. |
| `export_eligible` | Must equal `true` only after all export preconditions pass. |
| `reading_plan` | Required project-reading projection: priority, decision roles, verification locators, and optional user-controlled Zotero tag suggestions. |
| `captured_at`, `verified_at` | Required timestamps for auditability; `verified_at` is null until verified. |

## Invariants

1. `bib_key` is unique and immutable within a project.
2. `export_eligible: true` implies `verification_status: VERIFIED`, non-empty required fields, a source, and `conflict_ids: []`.
3. `UNVERIFIED` and `PARTIALLY_VERIFIED` records may be searched, read, or threatened but never appear in `references.bib`.
4. Missing optional fields are omitted from BibTeX; nulls are not serialized as literal strings.
5. A duplicate merge unions provenance and evidence links and preserves a paper-family/version relation.
6. An export does not upgrade reading tier, evidence verification, claim status, threat level, or project decision.
7. Reading priority is one of `IMMEDIATE`, `NEXT`, `BACKGROUND`, or `DEFERRED`; it cannot promote metadata or evidence.
8. Suggested Zotero tags are workflow hints. They do not assert that tags/collections were created or transferred.
