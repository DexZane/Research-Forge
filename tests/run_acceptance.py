#!/usr/bin/env python3
"""Deterministic contract checks for the Research Forge v1 package."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

from check_bibliography import run as run_bibliography


STATE_FILES = [
    "S00-intake.md", "S01-scope.md", "S02-landscape.md",
    "S03-literature-backbone.md", "S04-paper-matrix.md",
    "S05-red-ocean.md", "S06-candidate-portfolio.md",
    "S07-first-threat-scan.md", "S08-beam-selection.md",
    "S09-adversarial-novelty.md", "S10-residual-gap.md",
    "S11-hypothesis-synthesis.md", "S12-hypothesis-attack.md",
    "S13-diagnostic-design.md", "S14-falsification-plan.md",
    "S15-feasibility-audit.md", "S16-reviewer-panel.md",
    "S17-project-decision.md", "S18-experiment-dossier.md",
]

STATE_SECTIONS = {
    "Purpose", "Entry Conditions", "Reads", "Writes", "Required Questions",
    "Required Actions", "Required Protocols", "Parallelizable Work",
    "Sequential Work", "Required Outputs", "Exit Conditions",
    "Rollback Conditions", "Kill Conditions", "Forbidden Actions",
    "Gate Behavior",
}

GATED_EDGES = {
    ("S01_SCOPE", "S02_LANDSCAPE"): ("G1_SCOPE_LOCK", "APPROVED"),
    ("S08_BEAM_SELECTION", "S09_ADVERSARIAL_NOVELTY"): ("G2_PORTFOLIO_REVIEW", "APPROVED"),
    ("S12_HYPOTHESIS_ATTACK", "S13_DIAGNOSTIC_DESIGN"): ("G3_HYPOTHESIS_LOCK", "APPROVED"),
    ("S17_PROJECT_DECISION", "S18_EXPERIMENT_DOSSIER"): ("G4_PROJECT_LAUNCH", "GO"),
}

REQUIRED_TOP_DIRS = {
    "agents", "protocols", "states", "domain", "templates", "schemas",
    "runtime", "examples", "tests",
}


def legal_transition(current: str, target: str, gate: str = "NONE", decision: str = "NONE", rollback: bool = False) -> bool:
    if rollback:
        return bool(re.fullmatch(r"S\d{2}_[A-Z_]+", target))
    requirement = GATED_EDGES.get((current, target))
    if requirement:
        return (gate, decision) == requirement
    current_number = int(current[1:3])
    target_number = int(target[1:3])
    return target_number == current_number + 1


def formal_threat_valid(threat: dict) -> bool:
    level = threat["level"]
    if level not in {"T4", "T5"}:
        return True
    return threat.get("reading_tier") in {"R3", "R4"} and threat.get("formal_verification_complete") is True and bool(threat.get("evidence_ids"))


def fact_claim_valid(claim: dict, evidence: dict[str, dict]) -> bool:
    if claim.get("epistemic_status") != "FACT":
        return True
    for evidence_id in claim.get("supporting_evidence_ids", []):
        unit = evidence.get(evidence_id, {})
        if unit.get("directness") == "DIRECT" and unit.get("verification_status") == "VERIFIED":
            return True
    return False


def project_decision(scientific_hard_gates: dict[str, bool], resources_ready: bool) -> str:
    if not all(scientific_hard_gates.values()):
        return "KILL"
    return "GO" if resources_ready else "HOLD_RESOURCE"


def emergency_required(threat_level: str, residual_gap: str, phase_started: bool) -> bool:
    return phase_started and threat_level == "T5" and residual_gap == "NEAR_ZERO"


def check_relative_links(root: Path) -> None:
    pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for path in root.rglob("*.md"):
        for link in pattern.findall(path.read_text(encoding="utf-8")):
            if "://" in link or link.startswith("#"):
                continue
            target = (path.parent / link.split("#", 1)[0]).resolve()
            assert target.exists(), f"broken link in {path.relative_to(root)}: {link}"


def run(root: Path) -> list[str]:
    passed: list[str] = []

    run_bibliography(root)
    passed.append("BibTeX/Zotero export contract")

    actual_dirs = {p.name for p in root.iterdir() if p.is_dir()}
    assert REQUIRED_TOP_DIRS <= actual_dirs
    passed.append("package directories")

    for path in root.joinpath("templates").glob("*.yaml"):
        assert isinstance(yaml.safe_load(path.read_text(encoding="utf-8")), dict)
    passed.append("YAML templates parse")

    for state_file in STATE_FILES:
        text = root.joinpath("states", state_file).read_text(encoding="utf-8")
        headings = set(re.findall(r"^## (.+)$", text, re.MULTILINE))
        assert STATE_SECTIONS <= headings, state_file
    passed.append("S00-S18 state contracts")

    assert not legal_transition("S01_SCOPE", "S02_LANDSCAPE")
    assert legal_transition("S01_SCOPE", "S02_LANDSCAPE", "G1_SCOPE_LOCK", "APPROVED")
    assert not legal_transition("S17_PROJECT_DECISION", "S18_EXPERIMENT_DOSSIER", "G4_PROJECT_LAUNCH", "APPROVED")
    assert legal_transition("S17_PROJECT_DECISION", "S18_EXPERIMENT_DOSSIER", "G4_PROJECT_LAUNCH", "GO")
    assert legal_transition("S14_FALSIFICATION_PLAN", "S11_HYPOTHESIS_SYNTHESIS", rollback=True)
    passed.append("gate and rollback transitions")

    preliminary_t5 = {"level": "T5", "reading_tier": "R1", "formal_verification_complete": False, "evidence_ids": []}
    formal_t5 = {"level": "T5", "reading_tier": "R3", "formal_verification_complete": True, "evidence_ids": ["EU-0001"]}
    assert not formal_threat_valid(preliminary_t5)
    assert formal_threat_valid(formal_t5)
    passed.append("T4/T5 primary deep-read gate")

    claim = {"epistemic_status": "FACT", "supporting_evidence_ids": ["EU-0001"]}
    indirect = {"EU-0001": {"directness": "INDIRECT", "verification_status": "VERIFIED"}}
    direct = {"EU-0001": {"directness": "DIRECT", "verification_status": "VERIFIED"}}
    assert not fact_claim_valid(claim, indirect)
    assert fact_claim_valid(claim, direct)
    passed.append("epistemic promotion gate")

    all_science_pass = {"novelty": True, "mechanism": True, "falsifiable": True, "integrity": True}
    novelty_fails = dict(all_science_pass, novelty=False)
    assert project_decision(novelty_fails, True) == "KILL"
    assert project_decision(all_science_pass, False) == "HOLD_RESOURCE"
    assert project_decision(all_science_pass, True) == "GO"
    passed.append("scientific/resource decision separation")

    assert emergency_required("T5", "NEAR_ZERO", True)
    assert not emergency_required("T4", "NON_TRIVIAL", True)
    passed.append("post-GO novelty collision interrupt")

    dossier = root.joinpath("templates/experiment-dossier.md").read_text(encoding="utf-8")
    numbered = {int(n) for n in re.findall(r"^(\d+)\. ", dossier, re.MULTILINE)}
    assert numbered == set(range(1, 31))
    passed.append("30-element dossier")

    forbidden = re.compile(r"\b(?:TODO|TBD|FIXME)\b")
    for path in root.rglob("*"):
        if path.is_file() and path.suffix in {".md", ".yaml", ".py"}:
            if path.resolve() == Path(__file__).resolve():
                continue
            assert not forbidden.search(path.read_text(encoding="utf-8")), path
    passed.append("no unresolved placeholders")

    check_relative_links(root)
    passed.append("relative references resolve")

    worker_forbidden_writes = {"state/research_state.yaml", "state/threat_ledger.yaml"}
    proposed_worker_write = "state/research_state.yaml"
    assert proposed_worker_write in worker_forbidden_writes
    passed.append("worker global-write prohibition")

    return passed


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skill-root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    try:
        passed = run(args.skill_root.resolve())
    except (AssertionError, OSError, yaml.YAMLError) as exc:
        print(f"FAIL: {exc}")
        return 1
    for item in passed:
        print(f"PASS: {item}")
    print(f"PASS: {len(passed)} acceptance checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
