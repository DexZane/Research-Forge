#!/usr/bin/env python3
"""Deterministic acceptance checks for the public project README."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"


def main() -> int:
    text = README.read_text(encoding="utf-8")
    failures: list[str] = []

    required_headings = (
        "# Research Forge",
        "## 中文简介",
        "## Why Research Forge",
        "## How Research Forge differs",
        "## What makes it different",
        "## How to use",
        "### Install",
        "### Agent compatibility and install locations",
        "### Invoke",
        "#### 1. Explore a broad direction",
        "#### 2. Validate an existing idea",
        "#### 3. Resume a project",
        "### Work through the human gates",
        "## Decisions and outputs",
        "## Zotero/BibTeX reference export",
        "## Repository architecture",
        "## Validation",
        "## Scope and non-goals",
        "## Contributing",
        "## License",
    )
    for heading in required_headings:
        if heading not in text:
            failures.append(f"missing heading: {heading}")

    required_terms = (
        "EXPLORATION",
        "IDEA_VALIDATION",
        "/research-forge",
        "G1_SCOPE_LOCK",
        "G2_PORTFOLIO_REVIEW",
        "G3_HYPOTHESIS_LOCK",
        "G4_PROJECT_LAUNCH",
        "GO",
        "HOLD",
        "REFINE",
        "HOLD_RESOURCE",
        "KILL",
        "S00–S18",
        "T0–T5",
        "R0–R4",
        "research-project workspace",
        "exports/references.bib",
        "verification_status: VERIFIED",
        "python3 tests/check_bibliography.py",
        "GO means “worth testing,” not “guaranteed to work.”",
        "python3 tests/check_readme.py",
        "python3 tests/run_acceptance.py --skill-root .",
        "This is a contract comparison, not an empirical benchmark.",
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
        "Do not copy only the raw `SKILL.md`",
    )
    for term in required_terms:
        if term not in text:
            failures.append(f"missing required term: {term}")

    chinese_chars = re.findall(r"[\u3400-\u9fff]", text)
    if len(chinese_chars) < 80:
        failures.append("Chinese overview is missing or too short (need at least 80 CJK characters)")

    prohibited_claims = (
        r"\bthe\s+(?:world['’]s\s+)?best\b",
        r"\bthe\s+(?:world['’]s\s+)?first\b",
        r"\bthe\s+only\b",
        r"\bmost\s+comprehensive\b",
        r"全球最(?:好|强)",
        r"业界最(?:好|强)",
    )
    for pattern in prohibited_claims:
        match = re.search(pattern, text, flags=re.IGNORECASE)
        if match:
            failures.append(f"unsupported superlative claim: {match.group(0)!r}")

    link_pattern = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
    for raw_target in link_pattern.findall(text):
        target = raw_target.strip().strip("<>").split(maxsplit=1)[0]
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        path_part = unquote(target.split("#", 1)[0])
        if not path_part:
            continue
        resolved = (ROOT / path_part).resolve()
        if not resolved.exists():
            failures.append(f"unresolved local link: {target}")

    if failures:
        print("README acceptance: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("README acceptance: PASS")
    print(f"- required headings: {len(required_headings)}")
    print(f"- required contract terms: {len(required_terms)}")
    print(f"- Chinese overview characters: {len(chinese_chars)}")
    print("- prohibited claims: 0")
    print("- unresolved local links: 0")
    return 0


if __name__ == "__main__":
    sys.exit(main())
