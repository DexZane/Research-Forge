# Research Forge（中文）

[English](README.md) · [简体中文](README.zh-CN.md)

<p align="center">
  <img src="assets/research-forge-banner-zh.png" alt="Research Forge——在实验前经受对抗式审查的研究方向" width="100%">
</p>

> **不要问一个想法“新不新”；先设法证明它并不新。**

## 概述

Research Forge 是面向 AI / 深度学习方法研究的 Agent Skill。它先要求明确一个精确 baseline model；若用户没有提供，就从研究方向搜索 2–5 个候选并停下来让用户选择。随后它把模糊主题或已有想法推进为可辩护的实验决策：先建证据，再主动攻击 novelty，提出可证伪机制，最后决定项目应当 `GO`、`HOLD`、`REFINE`、`HOLD_RESOURCE` 还是 `KILL`。

它不替你包装一个看似新颖的模块；它帮你在高成本训练前，尽早发现一个方向究竟值得做、该怎么证明、又会怎样失败。

## 与一般选题工作流的区别

常见选题流程倾向于收集“看起来可行”的点子。Research Forge 关注“能否经受反驳的决策”：

- 用 S00–S18 状态机保存研究记忆，而不是每次从头聊；
- 将主 baseline 固定为有版本、有证据、有配置的 `BL-` 比较契约；不自动选择，也不静默替换；
- 分离 Evidence、Claim、Threat、Hypothesis 与 Decision，避免把猜测写成事实；
- 用 T0–T5 对抗式 threat 和 R0–R4 阅读层级审查新颖性；
- 在代码规划前冻结科学承诺，并以机制签名、候选承诺、最小证伪实验约束漂移；
- 按 `REUSE_AS_IS` → `ADAPT_EXISTING` → `NEW_MINIMAL` 选择实现，复用不是创新；
- 规划阶段不执行第三方仓库。最终复用源必须 `TRUST_REVIEWED` 且 `NOT_EXECUTED`。

检索、全文、Git、沙箱或 Zotero 能力缺失会记录为访问债务或执行限制，绝不被解释为“没有先前工作”。`GO` 只表示“值得检验”，不表示结果必然成立。

## 快速使用

### 安装

完整仓库用于阅读、开发和贡献；实际安装可使用只保留 Skill 必需文件的 [`skill-only`](https://github.com/DexZane/Research-Forge/tree/skill-only) 分支：

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo DexZane/Research-Forge --ref skill-only --path . --name research-forge
```

raw [`SKILL.md`](https://raw.githubusercontent.com/DexZane/Research-Forge/skill-only/SKILL.md) 仅用于查看入口，不能单独安装。必须保留同级的 `protocols/`、`states/`、`schemas/`、`templates/`、`runtime/`、`scripts/` 和 `domain/`。

若交给 Agent 安装，直接提供[安装指南](docs/guide/installation.md)：

```text
读取并严格按照此指南安装 Research Forge：
https://raw.githubusercontent.com/DexZane/Research-Forge/main/docs/guide/installation.md

安装完整 skill-only 包；不要覆盖已有安装；最后报告目标路径、commit 与验证结果。
```

### Agent 适配

Research Forge 遵循目录型 Agent Skills：`SKILL.md` 位于 Skill 根目录，复制时必须携带完整目录。发现位置可能随运行时版本变化，以下为当前官方文档给出的常用位置。

| 运行时 | 常用位置 | 说明 |
|---|---|---|
| [Codex](https://developers.openai.com/codex/skills/) | `~/.codex/skills/research-forge/` | 原生目录型 Skill |
| [Claude Code](https://code.claude.com/docs/en/skills) | `~/.claude/skills/research-forge/` 或 `.claude/skills/research-forge/` | 原生 `SKILL.md` Skill |
| [Gemini CLI](https://geminicli.com/docs/cli/using-agent-skills/) | `~/.gemini/skills/research-forge/` 或 `.gemini/skills/research-forge/` | 原生 Agent Skills |
| [GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills) | `~/.copilot/skills/research-forge/` 或 `.github/skills/research-forge/` | 原生 `SKILL.md` Skill |
| [OpenCode](https://opencode.ai/docs/skills) | `~/.config/opencode/skills/research-forge/` 或 `.opencode/skills/research-forge/` | 原生 Agent Skills |
| [Cursor](https://docs.cursor.com/context/rules) | `.cursor/rules/` | 需改写入口为 MDC rule，并提供完整目录 |

### 调用

在支持 slash command 的主机中调用：

```text
/research-forge

Use EXPLORATION mode.
Topic: robust tiny-object detection for edge deployment.
Constraints: public datasets, two consumer GPUs, six-week validation window.
Baseline: ExampleDetector-S v1 with its official public configuration.
Project workspace: /absolute/path/to/tiny-object-research

Build competing mechanism candidates. Search to reject them. Stop at every human gate.
Do not treat the starting observation as a verified cause.
```

若没有提供 baseline，Research Forge 会按方向搜索候选，在 G1 提供选择包并停下等待；它不会自己挑一个。baseline 只固定实验比较对象，不能将先前工作检索缩窄为该模型的改进论文。早期行为应当是：S00 把观察记录为未核验信息，G1 锁定研究边界，S02–S08 建立并攻击多样候选组合，然后由 G2 选择 finalists。

#### 2. 验证已有想法

当你已经有候选方法或新颖性主张时，使用 `IDEA_VALIDATION`。

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

该模式不会假定想法新颖。它会保留原始候选，使后续的 refinement、被杀死的主张和替代机制候选都能够追踪。

#### 3. 恢复已有项目

从项目根目录恢复，而不是依靠记忆重新口述研究历史。

```text
/research-forge

Resume the Research Forge project at:
/absolute/path/to/tiny-object-research

Validate saved state and the latest immutable snapshot, load blocking threats,
contradictions, reasoning debt, search freshness, and the pending gate, then
continue from the current valid state. Do not silently reconstruct uncertain data.
```

运行时会按固定顺序加载 `state/research_state.yaml`、快照、活跃候选与假设、T4/T5 威胁、开放矛盾、阻塞债务、搜索状态和近期决策。

#### 4. 快速对抗审计

当你在顶会截稿前或灵感初期需要对一个具体想法或预印本草稿进行 10–15 分钟快速压力测试时，使用 `FAST_AUDIT`。

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

该模式跳过宽泛的候选组合构建（S02–S08），直接审计单一目标想法：运行对抗新颖性扫描（S09）、创新残余剥离（S10）、替代机制攻击（S12）、廉价杀手设计（S14）与三方快速盲审（S16），输出结构化的[快速审计报告](templates/fast-audit-report.md)。详见[快速审计示例](examples/fast-audit-mode.md)。

### 通过人工 Gate

Research Forge 必须在每个 Gate 停下来，等待明确决定：

| Gate | 人类决定 |
|---|---|
| `G1_SCOPE_LOCK` | 批准或修改任务、方法、时间、场所、资源和兴趣边界 |
| `G2_PORTFOLIO_REVIEW` | 审查 survivors、kills、威胁、成本和不确定性，最多选择 1–3 个 finalists |
| `G3_HYPOTHESIS_LOCK` | 锁定存活的无方法假设、替代解释、预测和证伪条件 |
| `G4_PROJECT_LAUNCH` | 根据 project-decision packet 选择 GO、HOLD、KILL 或 REVISE |

沉默不是批准。你可以批准、要求修改、暂缓项目或拒绝建议的状态转移。在 `G4_PROJECT_LAUNCH` 获得明确 GO 之前，S18 不可用。

## 决策与输出

四个人类 Gate 不允许静默越过：`G1_SCOPE_LOCK` 确定问题边界，`G2_PORTFOLIO_REVIEW` 选择深入攻击的候选，`G3_HYPOTHESIS_LOCK` 冻结可证伪机制，`G4_PROJECT_LAUNCH` 做项目决定。

S18 的 experiment-ready dossier 包含：范围、证据与威胁轨迹、残余 novelty boundary、假设和竞争解释、预测、诊断、控制和 baseline、公平性约束、资源判断、模拟审稿、首个实验动作，以及实现杠杆计划。

- `exports/references.bib`：仅导出 `verification_status: VERIFIED` 的文献；
- `exports/reading-queue.md`：供 Zotero 导入后安排精读优先级和标签；
- `CAP-`：当前主机的能力档案与未解决债务；
- `BL-`：用户选择的 baseline 模型/配置契约、证据、适配限制与候选相对差异；
- implementation-leverage plan：记录复用、适配或新代码的理由、来源、版本、许可证、信任和依赖边界。

## Zotero/BibTeX 文献导出

将 `exports/references.bib` 导入 Zotero，再按照 `exports/reading-queue.md` 的优先级和建议标签精读。Zotero 写入权限是可选能力；可复现的 `.bib` 导出才是唯一记录。Research Forge 不会伪造引用，也不会把未核验元数据升级成 Evidence。

## 验收

在完整仓库根目录运行：

```bash
python3 tests/run_acceptance.py --skill-root .
python3 tests/check_bibliography.py
python3 tests/check_readme.py
python3 tests/check_bilingual_readme.py
python3 tests/check_repository.py .
python3 scripts/validate_project.py /absolute/path/to/research-project
```

这些是协议与文件契约检查，不是模型能力或科研效果的实证 benchmark。

## 仓库结构

```text
SKILL.md                 入口与路由
protocols/               科研规则
states/                  S00–S18 状态机
schemas/ + templates/    持久化项目记录
runtime/                 boot、gate、事务与交接
scripts/                 确定性工作区验证
docs/                    安装指南
tests/                   契约检查
```

## 范围与非目标

Research Forge 面向实验前的研究决策。它不训练模型、不获取凭据、不绕过付费墙、不执行未信任第三方代码、不把弱 novelty 包装为贡献，也不代写一篇完整投稿论文。

## 贡献

欢迎提交 issue 或 PR。请说明具体科研失败模式、影响到的 protocol/state/template，并尽可能附上可复现的验收用例。

## 许可证

[Apache License 2.0](LICENSE)
