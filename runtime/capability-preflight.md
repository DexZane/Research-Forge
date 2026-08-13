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

## Integrity and Handoff

At G1, show capability limits that affect the minimum discriminating path. At G4/S18, record the active `CAP-` profile and all unresolved capability debt in the handoff. A downstream agent must re-run the preflight in its own host; it cannot inherit another host's permissions or execution authorization.
