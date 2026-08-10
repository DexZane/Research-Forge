# BibTeX/Zotero Export Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make Research Forge capture verified literature metadata during search and emit one deterministic `references.bib` artifact that users can import into Zotero for downstream full-text reading.

**Architecture:** Keep bibliographic metadata as a paper-registry concern, linked to existing `P-` paper IDs and evidence/provenance records. Add a cross-state bibliography protocol and a runtime export contract; the Skill remains declarative, while the project workspace owns the generated `.bib` file. Export only verified, deduplicated records and preserve unresolved metadata conflicts as reasoning debt rather than silently choosing values.

**Tech Stack:** Markdown protocol/schema/templates, YAML record examples, BibTeX contract, Python stdlib deterministic acceptance checker.

## Global Constraints

- Produce exactly one user-facing citation artifact by default: `exports/references.bib`.
- BibTeX is bibliographic metadata for Zotero import; it is not evidence, full text, or a reading note.
- Never fabricate missing fields; omit unknown optional fields and block export when required fields are unresolved.
- Deduplicate by DOI, then arXiv/OpenReview/PMID identifiers, then normalized title + first-author + year; retain provenance from all sources.
- Keep `FACT`, `INFERENCE`, `HYPOTHESIS`, and `UNKNOWN` separate; search snippets cannot satisfy export verification.
- Generated project data stays outside the installed Skill repository.
- Do not add third-party runtime dependencies.

## File Map

- `protocols/bibliography.md`: canonical capture, verification, deduplication, keying, and export behavior.
- `schemas/bibliography-schema.md`: required fields, statuses, invariants, and record lifecycle.
- `templates/bibliography-record.yaml`: blank/example paper bibliography record.
- `templates/references.bib`: minimal valid output example.
- `runtime/bibliography.md`: project bootstrap, incremental export, final handoff, and recovery rules.
- `protocols/search.md`, `states/S03-literature-backbone.md`, `states/S04-paper-matrix.md`, `states/S09-adversarial-novelty.md`, `states/S18-experiment-dossier.md`: integrate bibliography lifecycle with existing states.
- `templates/paper-entry.yaml`, `templates/research-state.yaml`, `schemas/ids-and-enums.md`, `runtime/handoff.md`, `SKILL.md`: link the registry and artifact without changing ownership boundaries.
- `tests/check_bibliography.py`: deterministic structural/behavioral acceptance test.
- `tests/run_acceptance.py`, `tests/check_readme.py`, `tests/check_bilingual_readme.py`: include the new checker and user-facing contract.
- `README.md`, `README.zh-CN.md`: explain the Zotero workflow and its limits.

### Task 1: Write the failing acceptance test

**Files:** Create `tests/check_bibliography.py`; modify `tests/run_acceptance.py` to invoke it.

- [ ] Assert the required protocol/schema/template/runtime files exist.
- [ ] Assert the protocol explicitly requires provenance, verification, deduplication precedence, stable keys, and export path.
- [ ] Assert a provisional/unverified record is excluded from the example export and a verified record is exportable.
- [ ] Assert the BibTeX example has required fields, balanced braces, deterministic ordering, and no fabricated placeholder values.
- [ ] Run `python3 tests/check_bibliography.py`; expect failure because the feature files do not exist yet.

### Task 2: Implement the bibliography contract

**Files:** Create `protocols/bibliography.md`, `schemas/bibliography-schema.md`, `templates/bibliography-record.yaml`, `templates/references.bib`, and `runtime/bibliography.md`.

- [ ] Define `P-`-linked records, canonical identifiers, verification states, export eligibility, deterministic keys, and required/optional BibTeX fields.
- [ ] Define DOI → arXiv/OpenReview/PMID → normalized title/author/year deduplication, conflict preservation, and source union.
- [ ] Define incremental capture during search, export at S18 or explicit user request, and recovery for failed/partial writes.
- [ ] Keep `.bib` user-facing and provenance/reading state internal to the project workspace.

### Task 3: Integrate existing Research Forge contracts

**Files:** Modify `protocols/search.md`, `states/S03-literature-backbone.md`, `states/S04-paper-matrix.md`, `states/S09-adversarial-novelty.md`, `states/S18-experiment-dossier.md`, `templates/paper-entry.yaml`, `templates/research-state.yaml`, `schemas/ids-and-enums.md`, `runtime/handoff.md`, and `SKILL.md`.

- [ ] Route bibliography protocol from the Skill and relevant states.
- [ ] Add bibliography registry/artifact pointers to project state and paper records.
- [ ] Require capture of identifiers and provenance at discovery, verification before export, and final export in S18.
- [ ] Preserve the distinction between BibTeX metadata and evidence/reading depth.

### Task 4: Document the user workflow in both READMEs

**Files:** Modify `README.md`, `README.zh-CN.md`, `tests/check_readme.py`, and `tests/check_bilingual_readme.py`.

- [ ] Add the Zotero export capability, example invocation language, artifact path, import steps, and limitations.
- [ ] State that only verified metadata is exported and full-text access remains dependent on user/tool permissions.
- [ ] Keep English/Chinese sections aligned and local links valid.

### Task 5: Verify, refactor, and publish

- [ ] Run the new checker immediately after implementation.
- [ ] Run all existing repository/readme/acceptance checks.
- [ ] Inspect `git diff`, confirm no generated project data or credentials entered the Skill repository, commit, and push to `main` only after all checks pass.

## Self-review

- Search capture, paper metadata, evidence, and final handoff each have distinct owners.
- The user receives one `.bib` file; internal provenance remains available for audit.
- Unknown or conflicting metadata cannot be silently promoted into a citation.
- The plan covers the frozen S00–S18 lifecycle and the existing bilingual README/test contracts.
