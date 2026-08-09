# S05 — Red-Ocean Mapping

## Purpose

Identify problem, mechanism, module, and terminology zones unlikely to support a strong primary contribution.

## Entry Conditions

Paper matrix and coverage map are decision-usable.

## Reads

Landscape, backbone, paper matrix, paper families, recent search sessions.

## Writes

Red-ocean map with `RED`, `ORANGE`, `YELLOW`, and `BLUE_CANDIDATE`; saturation rationale and warnings.

## Required Questions

Is the module saturated, is the scientific mechanism saturated despite different modules, and is terminology reused across unrelated lines? Which intersections remain worth investigation?

## Required Actions

Distinguish publication density from mechanism maturity; inspect current work; mark uncertainty and evidence; identify cheap-to-reject clichés such as generic component swaps.

## Required Protocols

[Search](../protocols/search.md), [Reasoning](../protocols/reasoning.md), [Evidence](../protocols/evidence.md), [Novelty](../protocols/novelty.md).

## Parallelizable Work

Independent saturation checks by research line/mechanism.

## Sequential Work

Normalize terminology before classification; reconcile with paper matrix before commit.

## Required Outputs

`reports/red-ocean-map.md`, saturation evidence, candidate-generation constraints.

## Exit Conditions

Major red/orange zones and provisional blue candidates are evidence-bounded; route S06.

## Rollback Conditions

Recent/foundational gap: S03/S04.

## Kill Conditions

Kill only a proposed direction whose sole contribution is a verified saturated module/mechanism; preserve rationale.

## Forbidden Actions

Do not call “nobody used this module here” a blue ocean or confuse low result count with novelty.

## Gate Behavior

No gate.
