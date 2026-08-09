# Architecture

## Diagnostic Questions

- What information path, receptive field, routing, recurrence, hierarchy, or bottleneck causes failure?
- Is a topology change necessary, or can training/objective expose the same capacity?
- Does the architecture alter representation, optimization, inference, or merely parameter budget?
- Which component is necessary and which is replaceable?

## Evidence Targets

Path/activation analyses, controlled rewiring, matched capacity/compute, component removal/replacement, receptive-field or routing diagnostics, and training/inference separation.

## Confounders

Parameters, FLOPs, memory, initialization, normalization, longer training, compiler/kernel efficiency, and hidden recipe changes.

## Stitching Risks

Generic “backbone + module” combinations are high-risk. Require dependency, new prediction, necessity, minimality, and a mathematical object beyond a block diagram.
