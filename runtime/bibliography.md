# Bibliography Runtime

## Project bootstrap

The Skill repository contains only the contracts. A new project workspace creates:

```text
research-project/
├── state/research_state.yaml
├── state/paper_registry.yaml
├── state/evidence_ledger.yaml
├── state/search_registry.yaml
└── exports/references.bib
```

`state/paper_registry.yaml` is the source of truth for bibliography records, with evidence and search-session links resolved through the existing state ledgers. The `.bib` file is a generated, user-facing projection and may be regenerated at any time from the registry.

## Incremental runtime loop

During every literature search, the orchestrator:

1. normalizes each result into a `P-` record;
2. applies the deduplication and paper-family rules;
3. appends provenance and search-session links;
4. records metadata conflicts as reasoning debt;
5. verifies identifiers and type-specific required fields;
6. sets `export_eligible` only after verification; and
7. refreshes `exports/references.bib` transactionally when requested or when a state output requires it.

Workers may propose metadata and raw BibTeX, but only the orchestrator can merge records, resolve conflicts, set export eligibility, or commit the file. A worker must not edit `research_state.yaml`, the canonical paper registry, or the generated export directly.

## Export operation

The export operation reads all paper records, filters `export_eligible: true`, sorts by immutable `bib_key`, emits the entry type and verified fields in the canonical order, and validates balanced braces, required fields, unique keys, and entry count. It writes a temporary candidate and commits it only after validation succeeds. Excluded records and reasons are reported in the transaction log; they are not silently lost.

The operation is legal at any non-pending-gate state when explicitly requested and is mandatory during S18 final handoff. A pending human gate blocks forward scientific state mutation but does not prevent a read-only export of already committed records.

## Zotero handoff

The final dossier links `exports/references.bib` and states its record count, export timestamp, and excluded `P-` IDs. The user imports this single file into Zotero and performs full-text acquisition, annotation, and deep reading there or with another reading workflow. Research Forge does not claim that a BibTeX import downloaded papers or verified their scientific content.

## Recovery

If the export transaction fails, retain the last valid `.bib`, mark the transaction failed, list the affected records, and create reasoning debt for missing metadata or unresolved conflicts. Re-run after the registry is repaired; never reconstruct a citation from memory or a truncated temporary file.
