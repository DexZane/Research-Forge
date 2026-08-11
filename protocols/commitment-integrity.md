# Candidate Commitment Integrity Protocol

## Purpose

Protect the scientific commitments that make a candidate auditable while allowing a legitimate reframe to create a transparent new version.

## Core Commitment

Use a `CM-` record to bind a candidate version to its innovation signature, mechanism statement, differentiating claim, predicted observations, planned falsifier, and falsification/resource budget assumptions. A commitment is `DRAFT` in S06–S12 and becomes `FROZEN` when S14 preregisters the related falsification plan.

The commitment is not proof of the candidate. It makes later changes inspectable.

## Protected Changes

Changing any of these is a scientific change, not an editorial correction:

- bottleneck, operation, changed object, or critical condition;
- core mechanism or differentiating claim;
- primary predicted contrast;
- planned falsifier, primary decision rule, or maximum falsification budget assumption.

Create a new `CM-` version, link `supersedes_commitment_id`, record a reason and changed fields, and preserve the older record. Do not mutate a frozen record in place.

## Dependency Effects

- A change to signature or core mechanism invalidates dependent hypothesis attacks, novelty mappings, diagnostics, falsification plans, feasibility estimates, reviewer reports, and gate packets until revalidated.
- A change to prediction or falsifier invalidates the dependent preregistration and reviewer/decision records.
- A change only to wording, locator, or formatting may retain the version only when an integrity check records that semantic fields are byte-for-byte unchanged.

Do not preserve a stale falsifier merely to satisfy a frozen-field check. A scientifically necessary change must explicitly supersede and revalidate its downstream contracts.

## Audit Separation

Search, novelty, and reviewer workers may identify a required change but must return a revision cue; they never edit the commitment. The orchestrator either rejects the cue or creates a new commitment transaction and routes the candidate to the earliest affected state.

## Gate Requirements

Before G3, G4, or handoff, verify that every active hypothesis, experiment, feasibility estimate, reviewer report, and dossier points to the active commitment version. A pending or stale dependent record blocks advancement.
