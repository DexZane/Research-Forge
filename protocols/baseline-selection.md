# Baseline-First Selection Protocol

## Purpose

Lock one exact primary baseline model before S02 so candidate deltas, fairness controls, and feasibility claims have a stable comparison target. A baseline is an experimental comparison contract, not proof of novelty, the best available model, or an implementation-leverage source.

## Intake Paths

1. **User-supplied baseline:** create a `BL-` record with `USER_PROPOSED` selection status. Verify the model identity, exact variant/configuration, intended task/setting, primary-source provenance, and material fit before marking it `SELECTED`.
2. **No baseline supplied:** in S01 search the declared direction for 2–5 plausible primary baselines. Create separate `BL-` records with `DISCOVERED` or `VERIFIED` status and a concise selection packet. Do not auto-select or silently use the top-ranked model: set G1 to `HOLD` with `BASELINE_SELECTION_REQUIRED` until the human explicitly chooses one, requests a different model, or reframes scope.

User selection is a constraint decision, not scientific evidence. A supplied or selected model that is incompatible, unidentifiable, unavailable, or outside the resource scope must be marked `UNSUITABLE` or held; do not silently substitute it.

## Selection Contract

The selected `BL-` profile must pin:

- model family and exact variant/checkpoint or initialization policy;
- task, data/split, metric, input/preprocessing, and evaluation protocol;
- primary paper/code/config provenance and verification evidence;
- compute/resource fit, known limitations, and baseline-specific fairness risks;
- user selection decision/rationale and immutable baseline-contract version.

Record `MATCHED`, `BORDERLINE`, `MISMATCH`, or `UNKNOWN` for task, data, metric, resource, and implementation fit. `UNKNOWN` cannot support G1 approval. A selected baseline may be an official model or a verified reproduction, but its status must make that distinction explicit.

## Research Consequences

After selection, every S06+ candidate records the active `BL-` ID and a bounded delta statement: what changes relative to the baseline, what remains matched, and what diagnostic or prediction distinguishes the change. The frozen `CM-` commitment inherits the same baseline ID and contract version.

Search broadly for task, mechanism, failure-mode, and competing-method prior art. The broader task/mechanism search must remain explicit. Do not search only for variants of the selected baseline or interpret an empty baseline-specific query as a novelty result. The selected baseline anchors comparison design; it never narrows the prior-art attack.

The primary baseline does not replace stronger-baseline controls. Apply [Baseline Fairness](baseline-fairness.md) to matched recipe, capacity, compute, data, tuning, and alternative-mechanism controls.

## Revision and Handoff

Changing the selected baseline, its pinned configuration, or a material fit assessment requires S01 re-entry, a delta search, a new baseline-contract version, and invalidation of dependent candidates, commitments, diagnostics, falsification plans, feasibility estimates, reviewer packets, and handoffs. S18 pins the selected `BL-` ID/version and downstream agents may not substitute it silently.

Research Forge may inspect authorized metadata, papers, configurations, and code structure to verify a baseline; it never executes third-party model code or downloads checkpoints during planning.
