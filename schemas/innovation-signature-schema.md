# Innovation Signature Schema

## Required Fields

`IS-` ID, subject kind/ID/version, bottleneck, operation, changed object, critical condition, predicted contrast, scope, epistemic status, linked claims/evidence, lifecycle, and version.

## Validity

- Subject kind is `PAPER` or `CANDIDATE`; the linked subject/version must resolve.
- A paper signature at `FACT` has direct verified evidence for every factual field; normalized interpretation is `INFERENCE`.
- A candidate signature is `HYPOTHESIS` until an experiment supports a linked claim; it never turns the candidate into a fact.
- Empty or generic fields such as “improve performance” fail specificity.
- Candidate advancement requires all five signature fields to be material and linked to a core commitment.
- A revision creates a new signature/version with supersession lineage; never overwrite an audited signature.

## Comparison Invariants

Threat records that use a signature collision link both signature IDs/versions, dimension-level overlap cells, primary-source evidence, and the surviving contrast if any. Signature similarity alone cannot assign T4/T5.
