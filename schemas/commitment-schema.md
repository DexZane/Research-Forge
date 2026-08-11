# Candidate Commitment Schema

## Required Fields

`CM-` ID, candidate/version, innovation signature ID/version, core mechanism, differentiating claim, prediction IDs, planned falsifier, falsification budget, project-resource assumptions, lifecycle, commitment version, supersession, reason, and affected dependent IDs.

## Validity

- `DRAFT`, `FROZEN`, `SUPERSEDED`, and `INVALIDATED` are the permitted commitment lifecycle values.
- One active candidate has one active commitment. A frozen commitment is immutable except for non-semantic metadata correction recorded by integrity audit.
- S06 candidate records include a draft commitment; S14 freezes the commitment only when it links to a preregistered experiment and budget assumptions.
- A semantic core-field change creates a new commitment/version, supersedes the old record, and invalidates/revalidates dependent artifacts before a gate.
- A commitment must not promise an unverified novelty result or use outcome-derived pattern statistics as evidence.

## Handoff Invariant

S18 references the active frozen `CM-` record. The downstream experiment agent cannot change its core fields without returning a revision request to Research Forge.
