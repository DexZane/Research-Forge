# Claim Schema

## Required Fields

`CL-` ID, statement, claim type, epistemic status, explicit scope, supporting/opposing/limiting evidence, dependencies, lifecycle status, confidence+rationale, version, and supersession pointer.

## Claim Types

Use `FACTUAL`, `INTERPRETIVE`, `MECHANISTIC`, `NOVELTY`, `FEASIBILITY`, `DECISION`, or `BOUNDARY`.

## Validity

- Statement is atomic enough that one evidence update can affect it coherently.
- Claim strength/scope cannot exceed the weakest necessary evidence.
- `FACT` requires at least one verified direct supporting evidence unit and no unresolved blocking contradiction.
- `NOVELTY` includes searched scope, cutoff, boundary, and safe-language level.
- `MECHANISTIC` distinguishes observed relation from causal/interventional support.
- `SUPERSEDED` identifies successor; `INVALIDATED` keeps history and decision rationale.

## Dependency Edges

Use `SUPPORTS`, `REQUIRES`, `LIMITS`, `CONTRADICTS`, `SPECIALIZES`, or `DERIVES_FROM`. Only failure of `REQUIRES` automatically invalidates a descendant; other edges trigger review.

## Propagation

Evidence change stages claim update, explicit descendant recalculation, threat/candidate/hypothesis impact, report synchronization, and decision log before commit.
