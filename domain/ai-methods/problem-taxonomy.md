# Problem Taxonomy

Classify the primary failure and plausible alternatives:

- `DATA_INSUFFICIENCY`: quantity, coverage, quality, imbalance, labels.
- `REPRESENTATION_FAILURE`: insufficient/inappropriate features or tokens.
- `ARCHITECTURE_BOTTLENECK`: information flow, receptive field, routing, capacity placement.
- `OPTIMIZATION_FAILURE`: convergence, gradients, instability, interference.
- `OBJECTIVE_MISMATCH`: loss/surrogate does not reflect desired behavior.
- `ASSIGNMENT_MATCHING_FAILURE`: supervision/correspondence/routing is wrong or unstable.
- `CALIBRATION_FAILURE`: confidence/uncertainty mismatches correctness.
- `GENERALIZATION_FAILURE`: transfer, shift, subgroup, long-tail, robustness.
- `INFERENCE_INEFFICIENCY`: decoding/post-processing/serving bottleneck.
- `COMPUTATIONAL_BOTTLENECK`: cost allocation, memory, latency, throughput.
- `BENCHMARK_ARTIFACT`: dataset, split, annotation, leakage, or metric creates the symptom.

For each class record symptom, construct, direct diagnostic, strongest alternative, manipulable variable, expected signature, and scope. Do not select a class from method branding; use evidence.

An observed aggregate metric gap may decompose into several classes. Preserve competing classes until diagnostics discriminate them.
