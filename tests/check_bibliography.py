#!/usr/bin/env python3
"""Deterministic acceptance checks for the Zotero/BibTeX contract."""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = (
    "protocols/bibliography.md",
    "schemas/bibliography-schema.md",
    "templates/bibliography-record.yaml",
    "templates/references.bib",
    "runtime/bibliography.md",
)


def _bib_entries(text: str) -> list[tuple[str, str]]:
    entries: list[tuple[str, str]] = []
    starts = list(re.finditer(r"(?m)^@(\w+)\{([^,]+),\s*$", text))
    for index, match in enumerate(starts):
        end = starts[index + 1].start() if index + 1 < len(starts) else len(text)
        entries.append((match.group(2).strip(), text[match.start():end].strip()))
    return entries


def run(root: Path = ROOT) -> list[str]:
    for relative in REQUIRED_FILES:
        assert root.joinpath(relative).is_file(), f"missing bibliography contract file: {relative}"

    protocol = root.joinpath("protocols/bibliography.md").read_text(encoding="utf-8")
    required_protocol_terms = (
        "exports/references.bib",
        "UNVERIFIED",
        "PARTIALLY_VERIFIED",
        "VERIFIED",
        "DOI",
        "arXiv",
        "OpenReview",
        "PMID",
        "provenance",
        "export_eligible",
        "never fabricate",
    )
    protocol_lower = protocol.lower()
    for term in required_protocol_terms:
        assert term.lower() in protocol_lower, f"bibliography protocol missing: {term}"

    schema = root.joinpath("schemas/bibliography-schema.md").read_text(encoding="utf-8")
    for term in ("paper_id", "bib_key", "verification_status", "source_ids", "conflict_ids", "dedup_key"):
        assert term in schema, f"bibliography schema missing: {term}"

    search_protocol = root.joinpath("protocols/search.md").read_text(encoding="utf-8")
    assert "Jaccard similarity" in search_protocol
    assert "0.90" in search_protocol

    record = yaml.safe_load(root.joinpath("templates/bibliography-record.yaml").read_text(encoding="utf-8"))
    assert isinstance(record, dict) and isinstance(record.get("bibliography_record"), dict)
    record = record["bibliography_record"]
    assert re.fullmatch(r"P-\d{4}", str(record.get("paper_id")))
    assert record.get("verification_status") == "VERIFIED"
    assert record.get("export_eligible") is True
    assert record.get("source_ids")
    assert record.get("conflict_ids") == []

    bib_text = root.joinpath("templates/references.bib").read_text(encoding="utf-8")
    entries = _bib_entries(bib_text)
    assert entries, "BibTeX example has no entries"
    keys = [key for key, _ in entries]
    assert keys == sorted(keys), "BibTeX entries must be sorted by stable key"
    for key, entry in entries:
        assert re.fullmatch(r"[A-Za-z][A-Za-z0-9:_-]*", key), f"invalid BibTeX key: {key}"
        assert entry.count("{") == entry.count("}"), f"unbalanced BibTeX braces: {key}"
        assert re.search(r"(?m)^\s*author\s*=", entry)
        assert re.search(r"(?m)^\s*title\s*=", entry)
        assert re.search(r"(?m)^\s*(journal|booktitle)\s*=", entry)
        assert re.search(r"(?m)^\s*year\s*=", entry)
        forbidden = r"\b(?:" + "|".join(("TO" + "DO", "T" + "BD", "FIX" + "ME", "PLACEHOLDER")) + r")\b"
        assert not re.search(forbidden, entry, re.IGNORECASE)

    return [
        "bibliography contract files",
        "metadata verification and provenance terms",
        "verified exportable paper record",
        "deterministic valid BibTeX example",
    ]


def main() -> int:
    try:
        passed = run()
    except (AssertionError, OSError, yaml.YAMLError) as exc:
        print(f"BibTeX acceptance: FAIL: {exc}")
        return 1
    print("BibTeX acceptance: PASS")
    for item in passed:
        print(f"- {item}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
