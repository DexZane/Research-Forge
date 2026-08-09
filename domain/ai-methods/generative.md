# Generative Methods

## Diagnostic Questions

- Is failure objective/score mismatch, conditioning, mode coverage, sampling, guidance, discretization, or evaluation artifact?
- Is the bottleneck model capacity or inference sampler?
- Does conditioning information reach generated outputs causally?
- Which metric reflects the claimed construct?

## Evidence Targets

Likelihood/score diagnostics where valid, controlled sampler steps, guidance/conditioning interventions, diversity–fidelity tradeoffs, mode/coverage tests, human/automatic metric triangulation, and compute matching.

## Confounders

Sampling budget, prompt selection, cherry-picking, metric bias, training data leakage, evaluator model, and seed variance.

## Stitching Risks

Sampler/model/conditioning combinations need a mechanistic prediction and fair compute/evaluation, not only attractive examples.
