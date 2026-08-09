# S07 — First Threat Scan

## Purpose

Use shallow, low-cost attacks to remove obviously weak candidates before deep search.

## Entry Conditions

Candidate portfolio is valid.

## Reads

Candidates, genealogy, concept dictionary, backbone, red-ocean map, paper/search registries.

## Writes

Preliminary threats, quick-kill decisions, refined candidates, and search sessions.

## Required Questions

Is there a direct same-question paper, a recent close neighbor, the same mechanism, a mature solution line, obvious stitching, a missing prediction, or no scientific dependency?

## Required Actions

Run candidate-specific exact/mechanism/recent searches; assign preliminary T1–T5; apply K1 solved-by-multiple-work, K2 component swap, K3 no prediction, K4 no mechanism, K5 no problem–solution dependency.

## Required Protocols

[Search](../protocols/search.md), [Reading](../protocols/reading.md), [Novelty](../protocols/novelty.md), [Evidence](../protocols/evidence.md).

## Parallelizable Work

Independent shallow scan per candidate with shared deduplication.

## Sequential Work

Central threat normalization and candidate status decision.

## Required Outputs

Preliminary threat ledger, killed/refined candidate history, `reports/first-threat-scan.md`.

## Exit Conditions

Every active candidate has a shallow threat result and obvious weak candidates are archived; route S08.

## Rollback Conditions

Insufficient candidate diversity: S06. Missing backbone issue: S03–S05.

## Kill Conditions

Any K1–K5 condition with recorded evidence/rationale. A preliminary T5 alone triggers deep verification or removal from beam, not a formal global T5.

## Forbidden Actions

Do not present the scan as exhaustive or formalize T4/T5 without R3.

## Gate Behavior

No gate; record all kills for G2 review.
