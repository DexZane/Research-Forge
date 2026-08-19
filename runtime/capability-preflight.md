# Agent Capability Preflight

## Purpose

Establish what the current host can actually do before research work relies on it. Installation success, a remembered tool name, or a user expectation is not capability evidence.

## Timing

Create or refresh one active `CAP-` profile during BOOT/S00, before S01 scope lock. Recheck it when the host, credentials, network, permissions, or available tools change. This is a host-execution record, not evidence about the research question.

## Required Capability Checks

Record a status, check basis, timestamp, limitation, fallback, and required states for:

- web search and current-page retrieval;
- scholarly metadata lookup;
- authorized full-text access;
- PDF/text extraction;
- project-workspace read/write access;
- Python/YAML validation;
- Git/revision inspection;
- BibTeX generation/validation;
- isolated code execution; and
- optional Zotero write access.

Use only `AVAILABLE`, `LIMITED`, `UNAVAILABLE`, `UNKNOWN`, or `NOT_REQUIRED`. Do not obtain credentials, log in, invoke paid services, install software, execute external code, or modify Zotero merely to make a capability look available.

## Routing

- `UNKNOWN` never counts as `AVAILABLE`.
- Missing web/search/full-text capability creates access debt and caps novelty or evidence conclusions; it does not make prior art absent.
- Missing project-write/Python/YAML capability blocks local artifact validation and creates execution debt.
- Missing Git/revision inspection blocks a final reused/adapted component selection.
- Missing isolated execution does not block scientific analysis, but blocks any downstream request to run third-party code and may yield `HOLD_RESOURCE`.
- Missing Zotero write access never blocks the deterministic `.bib` export; leave user-controlled import/sync manual.

Record scientific and execution consequences separately. A host limitation may produce `HOLD_RESOURCE`, never a scientific KILL.

## Tool & Companion Skill Auto-Discovery Matrix

During BOOT / S00 Preflight, the orchestrator inspects the host's active tool registry and installed companion skills. When detected, capabilities are promoted to `AVAILABLE` with specific `check_basis` provenance:

| Capability | Detected Native MCPs / Tools | Detected Companion Skills | Promoted Status & Provenance |
|---|---|---|---|
| `SCHOLARLY_METADATA` | `paper-search`, `academic-mcp`, `semanticscholar`, `arxiv`, `pubmed`, `crossref`, `doi-mcp` | `nature-academic-search`, `anysearch` | `AVAILABLE` (`check_basis: "mcp:<name>"` or `"companion_skill:<name>"`) |
| `AUTHORIZED_FULL_TEXT` | `academic-mcp`, `paper-search` (with fulltext download) | `nature-downloader` | `AVAILABLE` (`check_basis: "mcp:academic-mcp"` or `"companion_skill:nature-downloader"`) |
| `PDF_TEXT_EXTRACTION` | Local PDF parser / converter tools | `nature-reader` | `AVAILABLE` (`check_basis: "companion_skill:nature-reader"`) |
| `BIBTEX_VALIDATION` & Verification | `doi-mcp`, `academic-mcp` | `nature-ref-verifier`, `nature-citation` | `AVAILABLE` (`check_basis: "companion_skill:nature-ref-verifier"`) |
| `WEB_SEARCH` | `search_web`, `google_search`, `brave_search`, `tavily` | `anysearch` | `AVAILABLE` (`check_basis: "native_tool:<name>"`) |

When companion skills or MCP tools are detected, the orchestrator routes subtasks directly to them during S02–S05 (landscape/backbone) and S09 (adversarial novelty). If none are available, the preflight marks them `LIMITED` / `UNAVAILABLE` and prompts the user for manual ingestion or MCP configuration.

## Human Ingestion Fallback Protocol

When automated tools for scholarly metadata, full-text retrieval, or PDF parsing are `LIMITED` or `UNAVAILABLE`:

1. **Standard Ingestion Directory Structure**: The project workspace maintains dedicated input directories:
   - `<project>/inputs/papers/<P-ID>.md` or `<project>/inputs/papers/<P-ID>.pdf` (for primary paper texts and appendices);
   - `<project>/inputs/code/<repo-name>/` (for inspected official implementations or configs).
2. **Transparent User Prompting**: When an R3/R4 deep-read or T4/T5 threat audit is blocked by a capability gap, the orchestrator explicitly requests:
   > *"Automated full-text retrieval for prior art `P-<xxxx>` is limited. Please provide the paper text, markdown export, or place the PDF at `<project>/inputs/papers/P-<xxxx>.pdf` to enable deep verification."*
3. **Structured Ingestion Record**: Upon user delivery, record a [templates/manual-source-drop.yaml](../templates/manual-source-drop.yaml) entry, assign `source_type: USER_SUPPLIED_PRIMARY`, verify text coverage, and resolve the corresponding `CAPABILITY_GAP` reasoning debt.

## Integrity and Handoff

At G1, show capability limits that affect the minimum discriminating path. At G4/S18, record the active `CAP-` profile and all unresolved capability debt in the handoff. A downstream agent must re-run the preflight in its own host; it cannot inherit another host's permissions or execution authorization.
