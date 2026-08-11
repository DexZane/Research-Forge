# Literature Lineage Schema

## Awareness Lead

An `AL-` awareness lead records a possible historical term, paper, mechanism, or lineage suggested by model memory, a user, a secondary reference, or an incomplete search result. It is a search instruction, not evidence.

Required fields: `AL-` ID, hint, provenance type, capture time, status, linked search-session IDs, resolution notes, and optional resolved `P-` IDs.

## Rules

- An awareness lead is always `AWARENESS_ONLY`, never citable, exportable, evidence-bearing, or sufficient for a novelty claim.
- Resolve it through a source before creating or linking a canonical `P-` paper record. Keep the lead and its resolution trail rather than silently replacing it.
- Paper records and source-backed evidence are `CITABLE` only after their existing bibliographic/evidence verification requirements are met.
- A method lineage may show both lead and citable nodes, but only citable nodes may support a claim, threat, bibliography export, or formal comparison.

## Bottleneck Grounding Gate

Before deriving a decision-critical bottleneck from a paper, complete R2 coverage of its method, evidence, and limitations. For a threat-critical bottleneck, use R3/R4 under the reading protocol. An unresolved lead creates reasoning debt rather than a reconstructed claim from memory.
