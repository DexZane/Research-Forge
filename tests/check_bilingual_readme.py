#!/usr/bin/env python3
"""Deterministic acceptance checks for the English/Chinese README pair."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
ENGLISH = ROOT / "README.md"
CHINESE = ROOT / "README.zh-CN.md"

ENGLISH_REQUIREMENTS = (
    "[English](README.md)",
    "[简体中文](README.zh-CN.md)",
)

CHINESE_HEADINGS = (
    "# Research Forge（中文）",
    "## 概述",
    "## Research Forge 解决什么问题",
    "## 与常见选题工作流的区别",
    "## 核心亮点",
    "## 研究生命周期",
    "## 适用场景",
    "## 使用方法",
    "### 前置条件",
    "### 安装",
    "### 各 Agent 的适配与安装位置",
    "### 调用",
    "#### 1. 探索宽泛方向",
    "#### 2. 验证已有想法",
    "#### 3. 恢复已有项目",
    "### 通过人工 Gate",
    "## 决策与输出",
    "## Zotero/BibTeX 文献导出",
    "## 仓库结构",
    "## 验收",
    "## 范围与非目标",
    "## 贡献",
    "## 许可证",
)

CHINESE_REQUIREMENTS = (
    "[English](README.md)",
    "[简体中文](README.zh-CN.md)",
    "EXPLORATION",
    "IDEA_VALIDATION",
    "G1_SCOPE_LOCK",
    "G2_PORTFOLIO_REVIEW",
    "G3_HYPOTHESIS_LOCK",
    "G4_PROJECT_LAUNCH",
    "S00–S18",
    "T0–T5",
    "R0–R4",
    "GO",
    "HOLD",
    "REFINE",
    "HOLD_RESOURCE",
    "KILL",
    "exports/references.bib",
    "verification_status: VERIFIED",
    "python3 tests/check_bibliography.py",
    "python3 tests/check_repository.py",
    "python3 tests/check_readme.py",
    "python3 tests/run_acceptance.py --skill-root .",
    "[Apache License 2.0](LICENSE)",
    "Claude Code",
    "~/.claude/skills/research-forge/",
    "Gemini CLI",
    "~/.gemini/skills/research-forge/",
    "GitHub Copilot CLI",
    "~/.copilot/skills/research-forge/",
    "OpenCode",
    "~/.config/opencode/skills/research-forge/",
    "Cursor",
    ".cursor/rules/research-forge.mdc",
    "不要只复制 raw 的 `SKILL.md`",
)


def local_links(text: str) -> list[str]:
    links = re.findall(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", text)
    return [item.strip().strip("<>").split(maxsplit=1)[0] for item in links]


def check_links(path: Path, text: str, failures: list[str]) -> None:
    for target in local_links(text):
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        relative = unquote(target.split("#", 1)[0])
        if not relative:
            continue
        if not (path.parent / relative).resolve().exists():
            failures.append(f"{path.name}: unresolved local link: {target}")


def main() -> int:
    failures: list[str] = []
    english = ENGLISH.read_text(encoding="utf-8")

    for requirement in ENGLISH_REQUIREMENTS:
        if requirement not in english:
            failures.append(f"README.md missing language switch: {requirement}")

    if not CHINESE.is_file():
        failures.append("missing bilingual README: README.zh-CN.md")
    else:
        chinese = CHINESE.read_text(encoding="utf-8")
        if len(chinese) < 6000:
            failures.append(f"README.zh-CN.md is too short: {len(chinese)} characters")
        if len(re.findall(r"[\u3400-\u9fff]", chinese)) < 1500:
            failures.append("README.zh-CN.md has too little Chinese content")
        for heading in CHINESE_HEADINGS:
            if heading not in chinese:
                failures.append(f"README.zh-CN.md missing heading: {heading}")
        for requirement in CHINESE_REQUIREMENTS:
            if requirement not in chinese:
                failures.append(f"README.zh-CN.md missing required term: {requirement}")
        check_links(CHINESE, chinese, failures)

    check_links(ENGLISH, english, failures)

    if failures:
        print("Bilingual README acceptance: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    chinese = CHINESE.read_text(encoding="utf-8")
    print("Bilingual README acceptance: PASS")
    print(f"- English language switches: {len(ENGLISH_REQUIREMENTS)}")
    print(f"- Chinese headings: {len(CHINESE_HEADINGS)}")
    chinese_count = len(re.findall(r"[\u3400-\u9fff]", chinese))
    print(f"- Chinese characters: {chinese_count}")
    print("- unresolved local links: 0")
    return 0


if __name__ == "__main__":
    sys.exit(main())
