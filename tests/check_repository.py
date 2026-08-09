#!/usr/bin/env python3
"""Deterministic acceptance checks for public repository metadata."""

from __future__ import annotations

import hashlib
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LICENSE_PATH = ROOT / "LICENSE"
GITIGNORE_PATH = ROOT / ".gitignore"
README_PATH = ROOT / "README.md"

LICENSE_SHA256 = "cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30"

REQUIRED_IGNORES = {
    ".DS_Store",
    ".AppleDouble",
    ".LSOverride",
    "__pycache__/",
    "*.py[cod]",
    "*$py.class",
    ".pytest_cache/",
    ".mypy_cache/",
    ".ruff_cache/",
    ".coverage",
    ".coverage.*",
    "htmlcov/",
    ".venv/",
    "venv/",
    "env/",
    "build/",
    "dist/",
    "*.egg-info/",
    ".idea/",
    ".vscode/",
    "*.swp",
    "*.swo",
    "*~",
    "*.log",
    "*.tmp",
    "*.temp",
}

FORBIDDEN_IGNORES = {
    "LICENSE",
    "README.md",
    "SKILL.md",
    "protocols/",
    "states/",
    "schemas/",
    "templates/",
    "runtime/",
    "domain/",
    "examples/",
    "tests/",
    "state/",
    "reports/",
    "snapshots/",
    "registries/",
    "research-project/",
}

README_REQUIREMENTS = {
    "Licensed under the [Apache License 2.0](LICENSE).",
    "python3 tests/check_repository.py",
}

README_STALE_TEXT = {
    "does not currently include a `LICENSE` file",
    "both validation commands",
}


def active_ignore_patterns(text: str) -> set[str]:
    """Return active positive patterns without comments or negations."""
    patterns: set[str] = set()
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or line.startswith("!"):
            continue
        patterns.add(line)
    return patterns


def canonical_pattern(pattern: str) -> str:
    """Normalize a root-anchored pattern for responsibility-boundary checks."""
    return pattern[1:] if pattern.startswith("/") else pattern


def main() -> int:
    failures: list[str] = []
    license_hash = "MISSING"
    active_patterns: set[str] = set()

    if not LICENSE_PATH.is_file():
        failures.append("missing repository file: LICENSE")
    else:
        license_hash = hashlib.sha256(LICENSE_PATH.read_bytes()).hexdigest()
        if license_hash != LICENSE_SHA256:
            failures.append(
                "LICENSE does not match the pinned official Apache-2.0 text: "
                f"expected {LICENSE_SHA256}, got {license_hash}"
            )

    if not GITIGNORE_PATH.is_file():
        failures.append("missing repository file: .gitignore")
    else:
        active_patterns = active_ignore_patterns(GITIGNORE_PATH.read_text(encoding="utf-8"))
        for pattern in sorted(REQUIRED_IGNORES - active_patterns):
            failures.append(f"missing required .gitignore pattern: {pattern}")

        canonical_patterns = {canonical_pattern(pattern) for pattern in active_patterns}
        for pattern in sorted(FORBIDDEN_IGNORES & canonical_patterns):
            failures.append(f"forbidden .gitignore pattern hides repository contract: {pattern}")

    readme = README_PATH.read_text(encoding="utf-8")
    for requirement in sorted(README_REQUIREMENTS):
        if requirement not in readme:
            failures.append(f"README missing repository metadata statement: {requirement}")
    for stale_text in sorted(README_STALE_TEXT):
        if stale_text in readme:
            failures.append(f"README contains stale repository metadata text: {stale_text}")

    if failures:
        print("Repository metadata acceptance: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Repository metadata acceptance: PASS")
    print(f"- Apache-2.0 SHA-256: {license_hash}")
    print(f"- required ignore patterns: {len(REQUIRED_IGNORES)}")
    print("- forbidden ignore patterns: 0")
    print("- README license and validation language: consistent")
    return 0


if __name__ == "__main__":
    sys.exit(main())
