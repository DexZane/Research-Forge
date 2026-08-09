# Loss and Objective

## Diagnostic Questions

- Which desired property is misrepresented by the surrogate objective?
- Does loss weighting reflect difficulty, uncertainty, calibration, imbalance, or assignment quality?
- Is the issue objective mismatch or simply optimization scale?
- Does a changed loss alter gradients in the predicted strata?

## Evidence Targets

Gradient decomposition, calibration/utility curves, controlled weighting, matched optimization, surrogate–task metric relationship, ablations, and alternative proper objectives.

## Confounders

Learning-rate retuning, loss scale, implicit regularization, changed positive set, longer convergence, and metric gaming.

## Stitching Risks

Combining named losses is not a mechanism. State the objective property, expected gradient/decision change, and falsifier.
