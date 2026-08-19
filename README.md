# Research Forge

[English](README.md) · [简体中文](README.zh-CN.md)

<p align="center">
  <img src="assets/research-forge-banner-en.png" alt="Research Forge — research direction under adversarial review" width="100%">
</p>

> **Do not ask whether an idea sounds novel. Try to prove that it is not.**

## 中文简介

Research Forge 是一个面向 AI / 深度学习方法研究的 Agent Skill。它不把“想出一个点子”当成终点，而是用系统文献检索、证据记忆、对抗式 novelty attack、机制假设、证伪设计和模拟审稿，将值得测试的方向推进到可实验状态；不成立的方向也应尽早被明确地终止。

## What it does

Research Forge moves an AI-method direction through a controlled path:

```text
topic or idea → baseline contract → evidence → novelty survivor → hypothesis → falsification → experiment-ready decision
```

It first records the user's exact baseline model or, if none is supplied, searches 2–5 direction-matched baseline options and waits for the user to select one. It keeps the project in a separate `research-project workspace`, records S00–S18 state, evidence, claims, threats, hypotheses, decisions, and exports. Four human gates prevent silent escalation:

| Gate | Question |
|---|---|
| `G1_SCOPE_LOCK` | Is the question bounded, researchable, and anchored to a user-selected baseline? |
| `G2_PORTFOLIO_REVIEW` | Which candidates deserve deeper attack? |
| `G3_HYPOTHESIS_LOCK` | Is there a falsifiable mechanism to test? |
| `G4_PROJECT_LAUNCH` | `GO`, `HOLD`, `REFINE`, `HOLD_RESOURCE`, or `KILL`? |

## Why it is different

Most topic-selection prompts optimize for plausible ideas. Research Forge optimizes for *defensible decisions*:

- Treat absence of search access as access debt, never proof that prior work is absent.
- Make a primary baseline an explicit, version-pinned comparison contract; never silently pick or substitute it.
- Separate evidence from claims and known mechanisms from hypotheses.
- Attack novelty with T0–T5 threats and require R0–R4 reading before strong conclusions.
- Freeze the scientific commitment before implementation planning.
- Prefer `REUSE_AS_IS`, then `ADAPT_EXISTING`, and allow `NEW_MINIMAL` only with recorded rejection evidence.
- Keep third-party repositories unexecuted during planning; a final reusable source must be `TRUST_REVIEWED` and `NOT_EXECUTED`.

`GO` means “worth testing,” not “guaranteed to work.”

## How to use

### Install

For a complete development repository, clone [main](https://github.com/DexZane/Research-Forge). For a compact installable package, use [`skill-only`](https://github.com/DexZane/Research-Forge/tree/skill-only):

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo DexZane/Research-Forge --ref skill-only --path . --name research-forge
```

The raw [`SKILL.md`](https://raw.githubusercontent.com/DexZane/Research-Forge/skill-only/SKILL.md) is an inspection link, not an installation. Do not copy only the raw `SKILL.md`; the referenced protocols, states, schemas, templates, runtime, and scripts are required.

To delegate installation to an Agent, give it the [installation guide](docs/guide/installation.md):

```text
Read and follow https://raw.githubusercontent.com/DexZane/Research-Forge/main/docs/guide/installation.md.
Install the complete skill-only package without replacing an existing installation.
Report the target path, checked-out commit, and verification result.
```

### Compatibility

Research Forge follows the directory-based Agent Skills pattern: keep `SKILL.md` at the skill root and copy the entire directory. Discovery is host-specific; use the current official documentation if it differs.

| Host | Typical location | Status |
|---|---|---|
| [Codex](https://developers.openai.com/codex/skills/) | `~/.codex/skills/research-forge/` | Native directory Skill |
| [Claude Code](https://code.claude.com/docs/en/skills) | `~/.claude/skills/research-forge/` or `.claude/skills/research-forge/` | Native `SKILL.md` Skill |
| [Gemini CLI](https://geminicli.com/docs/cli/using-agent-skills/) | `~/.gemini/skills/research-forge/` or `.gemini/skills/research-forge/` | Native Agent Skills |
| [GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills) | `~/.copilot/skills/research-forge/` or `.github/skills/research-forge/` | Native `SKILL.md` Skill |
| [OpenCode](https://opencode.ai/docs/skills) | `~/.config/opencode/skills/research-forge/` or `.opencode/skills/research-forge/` | Native Agent Skills |
| [Cursor](https://docs.cursor.com/context/rules) | `.cursor/rules/` | Adapt the entry point as an MDC rule and provide the full directory |

### Invoke

Use `/research-forge` where the host supports slash commands, then give it a direction, constraints, and an empty workspace:

```text
Use EXPLORATION mode for robust tiny-object detection on edge devices.
Constraints: public datasets, two consumer GPUs, six weeks.
Baseline: ExampleDetector-S v1 with its official public configuration.
Project workspace: /absolute/path/to/tiny-object-research

Build competing mechanism candidates. Search to reject them. Stop at every human gate.
Do not treat the starting observation as a verified cause.
```

If you omit the baseline, Research Forge searches direction-matched options, presents them at G1, and stops until you choose a `BL-` profile. Baseline-specific search never replaces broad task/mechanism prior-art search. Expected early behavior: S00 records the observation as unverified, G1 locks the research boundary, and S02–S08 build and attack a diverse candidate portfolio before G2 selects finalists.

#### 2. Validate an existing idea

Use `IDEA_VALIDATION` when you already have a candidate method or novelty claim.

```text
/research-forge

Use IDEA_VALIDATION mode.
Candidate idea: replace the YOLO feature-fusion block with a state-space module
to improve tiny-object context modeling.
Claimed mechanism: longer-range spatial interactions recover context lost by
local fusion.
Constraints: preserve real-time inference and use the same training data.
Project workspace: /absolute/path/to/ssm-yolo-audit

Preserve the original idea, generate alternative mechanisms, attack the claim
with the strongest prior art, and identify the residual contribution after
innovation peeling. Stop at every human gate.
```

The mode does not assume the idea is novel. It preserves the original candidate so that later refinements, killed claims, and alternative-mechanism candidates remain traceable.

#### 3. Resume a project

Resume from the project root rather than restating the research history from memory.

```text
/research-forge

Resume the Research Forge project at:
/absolute/path/to/tiny-object-research

Validate saved state and the latest immutable snapshot, load blocking threats,
contradictions, reasoning debt, search freshness, and the pending gate, then
continue from the current valid state. Do not silently reconstruct uncertain data.
```

The runtime loads `state/research_state.yaml`, snapshots, active candidates and hypotheses, T4/T5 threats, open contradictions, blocking debt, search status, and recent decisions in a fixed recovery order.

#### 4. Run a fast audit

Use `FAST_AUDIT` when you need an accelerated 10–15 minute adversarial gut-check on a specific idea or pre-submission draft before investing in a full project lifecycle.

```text
/research-forge

Use FAST_AUDIT mode.
Candidate idea: replace multi-head attention with state-space recurrence in diffusion transformers.
Claimed mechanism: linear-time sequence compression for high-resolution synthesis.
Target baseline: DiT-XL/2 on ImageNet 512x512.
Project workspace: /absolute/path/to/fast-audit-mamba-dit

Run an accelerated adversarial triage: scan closest prior art, peel non-novel claims,
attack with alternative explanations, pre-register one cheapest killer falsifier,
and produce a fast-audit risk report.
```

This mode skips wide candidate generation (S02–S08) and directly audits the single candidate through novelty threat scan (S09), innovation peeling (S10), hypothesis attack (S12), cheapest killer design (S14), and fast reviewer sweep (S16), producing a structured [Fast Audit Report](templates/fast-audit-report.md). See [examples/fast-audit-mode.md](examples/fast-audit-mode.md).

### Work through the human gates

Research Forge must stop and ask for an explicit decision at each gate:

| Gate | Human decision |
|---|---|
| `G1_SCOPE_LOCK` | Approve or revise task, method, time, venue, resource, and interest boundaries |
| `G2_PORTFOLIO_REVIEW` | Review survivors, kills, threats, cost, and uncertainty; select at most 1–3 finalists |
| `G3_HYPOTHESIS_LOCK` | Lock a surviving method-free hypothesis, alternatives, predictions, and falsifiers |
| `G4_PROJECT_LAUNCH` | Choose GO, HOLD, KILL, or REVISE from the project-decision packet |

Silence is not approval. You can approve, request revisions, hold the project, or reject the proposed transition. S18 is unavailable until `G4_PROJECT_LAUNCH` receives an explicit GO.

## Decisions and outputs

The S18 handoff contains the locked question, evidence and threat trail, residual novelty boundary, falsifiable predictions, diagnostics, controls, resource decision, reviewer attack, and first experiment action.

It also includes:

- `exports/references.bib`, containing only records with `verification_status: VERIFIED`;
- `exports/reading-queue.md`, a Zotero-oriented priority queue for deep reading;
- an implementation-leverage plan that separates infrastructure reuse from the scientific contribution; and
- a `CAP-` host-capability profile. Missing search, full text, Git, sandbox, or Zotero access is recorded as debt or a capability limit, not hidden.
- a selected `BL-` baseline model/contract, with exact configuration, evidence, fit limits, and a bounded candidate delta.

## Zotero/BibTeX reference export

Import `exports/references.bib` into Zotero, then use `exports/reading-queue.md` to tag and prioritize papers. Zotero write access is optional: deterministic `.bib` export is the source of record. Research Forge never fabricates a citation or upgrades an unverified metadata lead into evidence.

## Validation

Run the public checks from a full clone:

```bash
python3 tests/run_acceptance.py --skill-root .
python3 tests/check_bibliography.py
python3 tests/check_readme.py
python3 tests/check_repository.py .
python3 scripts/validate_project.py /absolute/path/to/research-project
```

This is a contract comparison, not an empirical benchmark.

## Repository architecture

```text
SKILL.md                 entry point and routing
protocols/               research rules
states/                  S00–S18 state machine
schemas/ + templates/    durable project records
runtime/                 boot, gates, transactions, handoff
scripts/                 deterministic workspace validation
docs/                    installation guide
tests/                   contract checks
```

## Scope and non-goals

Research Forge is for pre-experiment research decisions. It does not train models, acquire credentials, bypass paywalls, execute untrusted third-party code, turn weak novelty into a claim, or write a complete submission paper.

## Contributing

Open an issue or pull request with the research failure mode, the affected protocol/state/template, and a deterministic acceptance case where possible.

## License

Licensed under the [Apache License 2.0](LICENSE).
