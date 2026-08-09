# Efficiency

## Diagnostic Questions

- Is the bottleneck compute, memory, bandwidth, communication, routing imbalance, latency tail, or energy?
- Is computation allocated according to sample/token/region difficulty?
- Does theoretical cost predict measured serving performance?
- What quality loss appears at matched real cost?

## Evidence Targets

Measured latency/throughput/memory/energy with protocol, theoretical FLOPs/MACs, utilization, routing/load distribution, quality–cost Pareto frontier, and hardware sensitivity.

## Confounders

Hardware, software stack, kernels, precision, batch size, warm-up, compilation, I/O, and parameter count as a misleading proxy.

## Stitching Risks

Dynamic computation or pruning needs a mechanism for allocation and a prediction about where saved/added compute matters, not only average FLOPs.
