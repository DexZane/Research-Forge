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
topic or idea → evidence → novelty survivor → hypothesis → falsification → experiment-ready decision
```

It keeps the project in a separate `research-project workspace`, records S00–S18 state, evidence, claims, threats, hypotheses, decisions, and exports. Four human gates prevent silent escalation:

| Gate | Question |
|---|---|
| `G1_SCOPE_LOCK` | Is the question bounded and researchable? |
| `G2_PORTFOLIO_REVIEW` | Which candidates deserve deeper attack? |
| `G3_HYPOTHESIS_LOCK` | Is there a falsifiable mechanism to test? |
| `G4_PROJECT_LAUNCH` | `GO`, `HOLD`, `REFINE`, `HOLD_RESOURCE`, or `KILL`? |

## Why it is different

Most topic-selection prompts optimize for plausible ideas. Research Forge optimizes for *defensible decisions*:

- Treat absence of search access as access debt, never proof that prior work is absent.
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
Project workspace: /absolute/path/to/tiny-object-research

Build competing mechanism candidates. Search to reject them. Stop at every human gate.
Do not treat the starting observation as a verified cause.
```

Use `IDEA_VALIDATION` when you already have a specific idea, or resume from its workspace when continuing an existing project.

## Decisions and outputs

The S18 handoff contains the locked question, evidence and threat trail, residual novelty boundary, falsifiable predictions, diagnostics, controls, resource decision, reviewer attack, and first experiment action.

It also includes:

- `exports/references.bib`, containing only records with `verification_status: VERIFIED`;
- `exports/reading-queue.md`, a Zotero-oriented priority queue for deep reading;
- an implementation-leverage plan that separates infrastructure reuse from the scientific contribution; and
- a `CAP-` host-capability profile. Missing search, full text, Git, sandbox, or Zotero access is recorded as debt or a capability limit, not hidden.

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
