# Research Forge installation guide

This guide is written for an AI coding agent or a human operator installing Research Forge. It installs the complete, minimal `skill-only` package; a raw `SKILL.md` file alone is not a usable installation.

## Task and safety boundary

Install `research-forge` from:

```text
Repository: https://github.com/DexZane/Research-Forge.git
Branch:     skill-only
```

Before writing anything, identify the host's documented Skill directory and confirm that the host supports a directory-based `SKILL.md` Skill. Do not:

- overwrite, delete, or merge an existing `research-forge` installation without the user's explicit approval;
- store a live `research-project` workspace inside the installed Skill directory;
- install only the raw `SKILL.md` file;
- claim that installation or host discovery succeeded without verification.

If the host, target directory, network permission, or write permission is unavailable, report the specific blocker and stop.

## Choose the target directory

Use the host's current official documentation when it is available. Common locations include:

| Host | User-level target | Project-level target |
|---|---|---|
| Codex | `~/.codex/skills/research-forge/` | Host-specific |
| Claude Code | `~/.claude/skills/research-forge/` | `.claude/skills/research-forge/` |
| Gemini CLI | `~/.gemini/skills/research-forge/` or `~/.agents/skills/research-forge/` | `.gemini/skills/research-forge/` or `.agents/skills/research-forge/` |
| GitHub Copilot CLI | `~/.copilot/skills/research-forge/` or `~/.agents/skills/research-forge/` | `.github/skills/research-forge/`, `.agents/skills/research-forge/`, or `.claude/skills/research-forge/` |
| OpenCode | `~/.config/opencode/skills/research-forge/` or `~/.agents/skills/research-forge/` | `.opencode/skills/research-forge/`, `.agents/skills/research-forge/`, or `.claude/skills/research-forge/` |

For Cursor and API-only agents, there is no verified universal install location. Use that runtime's documented rules/commands mechanism and give it access to the entire cloned directory, not only `SKILL.md`.

## Install a new copy

Set `target` to the selected full path. If it already exists, stop and report its path and state rather than replacing it. Otherwise, clone the minimal package:

```bash
mkdir -p "$(dirname "$target")"
git clone --depth 1 --branch skill-only \
  https://github.com/DexZane/Research-Forge.git "$target"
```

If the host provides a native installer, it may be used only when it can install the complete repository at the `skill-only` ref and preserve the directory structure.

## Verify before reporting success

Run the following after cloning:

```bash
(
  if [ -z "${target:-}" ]; then
    printf '%s\n' 'Set target to the full installation path before verification.' >&2
    exit 1
  fi

  verification_failed=0
  for file in SKILL.md LICENSE; do
    if [ ! -f "$target/$file" ]; then
      printf 'Missing required file: %s\n' "$target/$file" >&2
      verification_failed=1
    fi
  done
  for directory in agents domain protocols runtime schemas states templates; do
    if [ ! -d "$target/$directory" ]; then
      printf 'Missing required directory: %s\n' "$target/$directory" >&2
      verification_failed=1
    fi
  done

  if [ "$verification_failed" -ne 0 ]; then
    exit 1
  fi
  git -C "$target" rev-parse --short HEAD
)
```

Then reload or restart the host if its documentation requires it. Confirm only what the host actually exposes: for example, that `research-forge` is listed, or that `/research-forge` can be invoked.

## Report back

Report the target path, checked-out commit, verification result, host refresh result, and any unresolved blocker. Do not report a research project as created; installation and creating a separate research-project workspace are distinct operations.

---

# Research Forge 安装指南（中文）

本指南供 AI 编程 Agent 或人工安装者使用。它安装完整且最小的 `skill-only` 包；单独下载 raw `SKILL.md` 不是可运行安装。

## 任务与安全边界

从以下位置安装 `research-forge`：

```text
仓库： https://github.com/DexZane/Research-Forge.git
分支： skill-only
```

写入前，先根据当前主机的官方文档确定 Skill 目录，并确认主机支持目录型 `SKILL.md` Skill。不要：

- 未获用户明确许可就覆盖、删除或合并已有 `research-forge` 安装；
- 将实时 `research-project` workspace 放入已安装 Skill 的目录；
- 只安装 raw `SKILL.md`；
- 未完成验证就声称安装或主机发现成功。

若无法确认主机、目标目录、网络权限或写入权限，请说明具体阻塞并停止。

## 选择目标目录

优先采用主机当前官方文档。常见位置见上方表格；该表不是所有运行时的通用保证。Cursor 和仅 API Agent 没有统一且经核实的安装位置，应使用对应运行时的 rules/commands 机制，并让 Agent 能访问整个克隆目录，而不只是 `SKILL.md`。

## 安装新副本

将 `target` 设置为选定的完整路径。若该路径已存在，不要替换；报告其路径和状态。否则克隆最小安装包：

```bash
mkdir -p "$(dirname "$target")"
git clone --depth 1 --branch skill-only \
  https://github.com/DexZane/Research-Forge.git "$target"
```

若主机带有原生安装器，只有当它能从 `skill-only` 获取完整仓库并保持目录结构时才可使用。

## 成功前验证

克隆完成后运行上方验证命令，随后根据主机文档重新加载或重启。只报告主机实际暴露的结果，例如 `research-forge` 已出现在列表中，或 `/research-forge` 可以调用。

## 最终汇报

汇报目标路径、检出的 commit、验证结果、主机刷新结果及尚未解决的阻塞。不要把安装完成说成已创建研究项目：研究项目应位于独立的 workspace。
