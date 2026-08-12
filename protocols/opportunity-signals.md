# Opportunity Signal Protocol

## Purpose

Generate candidates from auditable research problems rather than from module substitution alone.

## Signal Unit

Create an `OP-` record for a source-grounded observation that may justify investigation. Permitted signal types:

- `BENCHMARK_SLICE_FAILURE`;
- `REPLICATION_ANOMALY`;
- `PAPER_LIMITATION`;
- `NEGATIVE_RESULT`;
- `DATASET_OR_EVALUATION_ARTIFACT`;
- `DEPLOYMENT_CONSTRAINT`;
- `OPEN_TECHNICAL_QUESTION`.

Record source/provenance, bounded observation, scope, epistemic status, competing explanations, candidate mechanism links, minimum verification action, and lifecycle. A user report or issue tracker can create a discovery lead but is not evidence until verified at the required reading/source depth.

## Generation Rule

S02–S05 may use signals to form candidate gaps. S06 creates a candidate only when it links an `OP-` signal to an RQ canvas, an initial mechanism question, and an observable contrast. A signal is not a gap, a claimed cause, a novelty claim, or a method prescription.

## Signal Quality Checks

- A benchmark average cannot stand in for a slice failure without a stated slice or diagnostic.
- A paper limitation is author context, not proof that the proposed response will work.
- A deployment constraint must identify the target environment and measurable constraint.
- An anomaly must have a reproducibility or artifact check before supporting a mechanism claim.
- At least one credible alternative explanation accompanies every active signal.

## Lifecycle

Use `DISCOVERY`, `VERIFICATION_PENDING`, `VERIFIED`, `WEAKENED`, `INVALIDATED`, or `ARCHIVED`. Only a verified signal can support an evidence-linked candidate gap. Preserve invalidated signals and their alternative explanations to prevent repeated rediscovery.
