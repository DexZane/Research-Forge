#!/usr/bin/env python3
"""Deterministic acceptance checks for the public project README."""

from __future__ import annotations

import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
INSTALLATION_GUIDE = ROOT / "docs" / "guide" / "installation.md"


def check_installation_verifier(guide: str, failures: list[str]) -> None:
    match = re.search(
        r"## Verify before reporting success.*?```bash\n(.*?)\n```",
        guide,
        flags=re.DOTALL,
    )
    if not match:
        failures.append("installation guide verification block is missing")
        return

    verification_script = match.group(1)
    with tempfile.TemporaryDirectory(prefix="research-forge-install-check-") as temporary:
        target = Path(temporary) / "research-forge"
        target.mkdir()
        target.joinpath("SKILL.md").write_text("---\nname: research-forge\n---\n", encoding="utf-8")
        target.joinpath("LICENSE").write_text("fixture\n", encoding="utf-8")
        for directory in ("agents", "domain", "protocols", "runtime", "schemas", "states", "templates", "scripts"):
            target.joinpath(directory).mkdir()

        subprocess.run(["git", "-C", str(target), "init", "-q"], check=True)
        subprocess.run(
            [
                "git", "-C", str(target),
                "-c", "user.name=Research Forge Tests",
                "-c", "user.email=tests@example.invalid",
                "commit", "--allow-empty", "-qm", "fixture",
            ],
            check=True,
        )
        environment = os.environ.copy()
        environment["target"] = str(target)
        complete = subprocess.run(
            ["sh"], input=verification_script, text=True,
            capture_output=True, env=environment, check=False,
        )
        if complete.returncode != 0:
            failures.append("installation verifier rejects a complete package")

        target.joinpath("templates").rename(target.joinpath("templates-missing"))
        incomplete = subprocess.run(
            ["sh"], input=verification_script, text=True,
            capture_output=True, env=environment, check=False,
        )
        if incomplete.returncode == 0:
            failures.append("installation verifier accepts a package missing templates/")


def main() -> int:
    text = README.read_text(encoding="utf-8")
    failures: list[str] = []

    required_headings = (
        "# Research Forge",
        "## 中文简介",
        "## What it does",
        "## Why it is different",
        "## How to use",
        "### Install",
        "### Compatibility",
        "### Invoke",
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
        "`GO` means “worth testing,” not “guaranteed to work.”",
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
        ".cursor/rules/",
        "Do not copy only the raw `SKILL.md`",
        "implementation-leverage plan",
        "REUSE_AS_IS",
        "NEW_MINIMAL",
        "CAP-",
        "BL-",
        "baseline contract",
        "stops until you choose",
        "TRUST_REVIEWED",
        "exports/reading-queue.md",
        "scripts/validate_project.py",
        "https://raw.githubusercontent.com/DexZane/Research-Forge/main/docs/guide/installation.md",
    )
    for term in required_terms:
        if term not in text:
            failures.append(f"missing required term: {term}")

    if not INSTALLATION_GUIDE.is_file():
        failures.append("missing Agent installation guide")
    else:
        guide = INSTALLATION_GUIDE.read_text(encoding="utf-8")
        for term in (
            "# Research Forge installation guide",
            "`skill-only`",
            "overwrite, delete, or merge an existing",
            "verification_failed=1",
            "# Research Forge 安装指南（中文）",
            "只安装 raw `SKILL.md`",
        ):
            if term not in guide:
                failures.append(f"installation guide missing contract: {term}")
        check_installation_verifier(guide, failures)

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
    print("- Agent installation guide: complete package passes; missing directory fails")
    print("- prohibited claims: 0")
    print("- unresolved local links: 0")
    return 0


if __name__ == "__main__":
    sys.exit(main())
