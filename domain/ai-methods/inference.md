# Inference

## Diagnostic Questions

- Is failure introduced by decoding, thresholding, NMS, sampling, beam/search, caching, quantization, or deployment constraints?
- Does training optimize the same decision used at inference?
- Can an oracle decode reveal headroom?
- Is the claimed gain a changed evaluation or post-processing protocol?

## Evidence Targets

Oracle decoding, threshold/temperature sweeps, matched post-processing, raw-output diagnostics, calibration, latency/memory, and end-to-end versus post-hoc comparisons.

## Confounders

Test-time augmentation, batch size, hardware/kernels, precision, compiler, metric implementation, and changed latency target.

## Stitching Risks

Deployment tricks can be valuable but should not be presented as a new training/mechanism hypothesis unless evidence supports that scope.
