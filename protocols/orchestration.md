# Orchestration Protocol

## Control Plane

The orchestrator is the only control plane and single writer for global state. Search, reader, code, analysis, and reviewer workers form the work plane.

Workers may discover, read, extract proposed evidence, compare papers, generate candidate threats or hypotheses, and attack a dossier. Workers may not modify global state, assign formal T4/T5, kill candidates, change a novelty boundary or gate, or announce GO.

## Controlled Parallelism

Parallelize independent queries, research lines, paper reads, code checks, or first-pass reviewer roles. Keep dependent reasoning sequential: evidence verification before threat upgrade; peeling before hypothesis synthesis; hypothesis lock before experiment design; reviewer synthesis after independent reports.

Never let parallel workers create parallel truth. Deduplicate and reconcile centrally.

## Task Packet & Subagent Context Isolation

To prevent token bloat and context degradation across multi-turn workflows, workers and subagents must run with isolated, minimal context. Do not dump the entire global state or full project history into a worker prompt.

Every dispatch packet (see [templates/worker-task-packet.yaml](../templates/worker-task-packet.yaml)) contains strictly:

- task ID and worker type;
- specific decision question and search/reading intent;
- minimal targeted context: relevant candidate signature (`IS-`), baseline profile (`BL-`), and target paper/code locators only;
- exact scope, cutoff date, and exclusions;
- permitted tools/actions and forbidden global writes (workers never write global state);
- required output schema (compact structured YAML/JSON);
- evidence/primary-source requirements;
- dependencies, budget, and stop condition;
- escalation conditions.

## Worker Return

Require proposed records, citations/locators, epistemic classes, reading tiers, confidence, conflicts, coverage limits, duplicate/family candidates, unresolved questions, and recommended next action. Raw narrative without provenance cannot be committed.

## Conflict Reconciliation

When workers disagree, compare source/version, definitions, scope, evidence directness, and independence. Create a contradiction if material; do not resolve by majority vote or worker confidence alone.

## Priority Queue

Order work by decision criticality and information gain:

1. blocking integrity/recovery;
2. emergency novelty collision;
3. T4/T5 verification and fatal reviewer issues;
4. gate-critical RQ, signal, triage, and contradiction unknowns;
5. cheapest discriminating evidence;
6. coverage expansion;
7. non-blocking enrichment.

## Commit Boundary

Workers submit proposals. The orchestrator validates, stages, propagates, snapshots, commits, and logs. A worker result based on a stale snapshot must be revalidated before integration.
