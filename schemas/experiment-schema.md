# Experiment and Diagnostic Schema

## Experiment Required Fields

`EX-` ID, E0–E2 stage, F0–F4 cost, title, hypothesis/alternatives/predictions, frozen candidate commitment ID/version, variables, controls, baselines, diagnostics, primary setting/stratification, true/false expectations, GO/HOLD/KILL/REFINE rules, ambiguity action, cost, prerequisites, preregistration, and execution status.

## Diagnostic Required Fields

`DM-` ID, construct/definition/computation, scientific question, baseline applicability, method independence, boundary interpretation, true/false expectations, confounders, alternative metrics, predictions, hooks, construct-validity status, lifecycle.

## Validity

- E0 defaults to F0/F1 unless lower tiers cannot answer the question.
- Every experiment distinguishes the core hypothesis from an alternative or tests practical ceiling.
- Every primary prediction maps to a primary metric plus alternative operationalization.
- Controls address named confounders; baselines comply with fairness protocol.
- Decision rules are committed before execution; changes create a new preregistration version.
- The experiment references the active frozen commitment; a semantic commitment revision invalidates the experiment plan until a new preregistration version is committed.
- `GO` cannot depend only on p-value; include effect/utility, uncertainty, robustness, and validity appropriate to stage.
- `FAILED_VALIDITY` results cannot support/oppose the hypothesis but must be preserved.

## Handoff Invariants

S18 handoff references G4 GO, immutable dossier snapshot, frozen commitment/signature, locked hypotheses, first experiment, decision rules, resources, and forbidden silent scientific changes.
