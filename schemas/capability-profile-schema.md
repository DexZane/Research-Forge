# Capability Profile Schema

## Required Record

A `CAP-` record contains host label, checked timestamp, capability entries, routing consequences, debt IDs, lifecycle, and version. Each capability entry contains canonical capability name, status, check basis, checked timestamp, limitation, fallback, and required states.

Canonical names: `WEB_SEARCH`, `SCHOLARLY_METADATA`, `AUTHORIZED_FULL_TEXT`, `PDF_TEXT_EXTRACTION`, `PROJECT_WORKSPACE_WRITE`, `PYTHON_YAML_VALIDATION`, `GIT_REVISION_INSPECTION`, `BIBTEX_VALIDATION`, `ISOLATED_CODE_EXECUTION`, and `ZOTERO_WRITE_API`.

## Validity

- Status is one of `AVAILABLE`, `LIMITED`, `UNAVAILABLE`, `UNKNOWN`, or `NOT_REQUIRED`.
- `AVAILABLE` and `LIMITED` require a recorded check basis and timestamp; `LIMITED` also names its limitation.
- `UNKNOWN` and `UNAVAILABLE` name a fallback or reasoning-debt consequence when a current state requires the capability.
- The profile never stores credentials, tokens, private URLs, or secret values.
- The active profile is required from S01 onward. It is revalidated after host/tool/permission changes.
- Capability status is operational evidence only. It must not upgrade a paper, claim, threat, hypothesis, or novelty conclusion.
