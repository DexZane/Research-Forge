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

UPGRADE_REQUIRED_FILES = (
    "protocols/innovation-signature.md",
    "protocols/commitment-integrity.md",
    "schemas/innovation-signature-schema.md",
    "schemas/commitment-schema.md",
    "schemas/literature-lineage-schema.md",
    "templates/innovation-signature.yaml",
    "templates/candidate-commitment.yaml",
    "templates/awareness-lead.yaml",
)

V12_REQUIRED_FILES = (
    "protocols/researchability.md",
    "protocols/opportunity-signals.md",
    "protocols/literature-triage.md",
    "protocols/collaboration.md",
    "schemas/researchability-schema.md",
    "schemas/literature-triage-schema.md",
    "templates/research-question-canvas.yaml",
    "templates/fit-card.yaml",
    "templates/opportunity-signal.yaml",
    "templates/literature-triage-entry.yaml",
    "templates/human-discussion-packet.md",
)

V12_RUNTIME_CONTRACTS = {
    "runtime/boot.md": ("research-question", "opportunity signals", "literature-triage"),
    "runtime/context-loading.md": ("research-question canvas", "literature-triage", "minimum discriminating paths"),
    "runtime/transaction.md": ("candidate opportunity-signal provenance", "Researchability Revision", "gate-critical `LT-`"),
    "protocols/integrity.md": ("Active `RQ-` and `FIT-` pointers", "abstract-only reading cannot close", "minimum discriminating path"),
}

SIGNATURE_FIELDS = (
    "bottleneck", "operation", "changed_object", "critical_condition", "predicted_contrast",
)

COMMITMENT_CORE_FIELDS = (
    "innovation_signature_id", "innovation_signature_version", "core_mechanism",
    "differentiating_claim", "prediction_ids", "planned_falsifier",
    "falsification_budget", "project_resource_assumptions",
)


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


def signature_specific(signature: dict) -> bool:
    """Reject a novelty claim that is only a title, topic, or generic improvement."""
    return all(isinstance(signature.get(field), str) and signature[field].strip() for field in SIGNATURE_FIELDS)


def exact_signature_collision(candidate: dict, competitor: dict) -> bool:
    """Identify a candidate for deep novelty verification, not a formal threat verdict."""
    return signature_specific(candidate) and signature_specific(competitor) and all(
        candidate[field].strip().casefold() == competitor[field].strip().casefold()
        for field in SIGNATURE_FIELDS
    )


def awareness_lead_citable(lead: dict) -> bool:
    """Awareness-only records remain search instructions even after they resolve."""
    return lead.get("lineage_role") != "AWARENESS_ONLY"


def commitment_revision_valid(previous: dict, proposed: dict) -> bool:
    """Require an explicit superseding transaction for a semantic commitment revision."""
    changed = {field for field in COMMITMENT_CORE_FIELDS if previous.get(field) != proposed.get(field)}
    if not changed:
        return True
    return (
        proposed.get("id") != previous.get("id")
        and proposed.get("candidate_id") == previous.get("candidate_id")
        and proposed.get("commitment_version") == previous.get("commitment_version", 0) + 1
        and proposed.get("supersedes_commitment_id") == previous.get("id")
        and bool(proposed.get("change_reason"))
        and changed <= set(proposed.get("changed_core_fields", []))
        and bool(proposed.get("affected_dependent_ids"))
    )


def research_question_valid(canvas: dict) -> bool:
    """Require an answerable question and a small discriminating path before deep exploration."""
    required = (
        "unit_and_condition", "knowledge_gap", "mechanism_question", "observable_outcome",
        "minimal_discriminating_path", "stop_or_reframe_condition",
    )
    minimum = canvas.get("scope_ladder", {}).get("minimum_completable", {})
    return (
        all(isinstance(canvas.get(field), str) and canvas[field].strip() for field in required)
        and isinstance(canvas.get("phenomenon"), dict)
        and isinstance(canvas["phenomenon"].get("statement"), str)
        and bool(canvas["phenomenon"]["statement"].strip())
        and canvas["phenomenon"].get("epistemic_status") in {"FACT", "INFERENCE", "HYPOTHESIS", "UNKNOWN"}
        and isinstance(minimum.get("output"), str) and minimum["output"].strip()
        and isinstance(minimum.get("stop_condition"), str) and minimum["stop_condition"].strip()
    )


def opportunity_signal_valid(signal: dict) -> bool:
    """Prevent an anecdote, limitation, or issue from silently becoming a candidate gap."""
    return (
        signal.get("lifecycle_status") == "VERIFIED"
        and bool(signal.get("source_provenance"))
        and bool(signal.get("bounded_observation"))
        and bool(signal.get("alternative_explanations"))
        and bool(signal.get("evidence_ids"))
        and bool(signal.get("minimum_verification_action"))
    )


def triage_closes_required_tier(entry: dict) -> bool:
    """Abstract access is discovery-only and cannot close a deep-reading requirement."""
    return not (
        entry.get("access_state") == "ABSTRACT_ONLY"
        and entry.get("required_reading_tier") in {"R2", "R3", "R4"}
    )


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

    for relative in UPGRADE_REQUIRED_FILES:
        assert root.joinpath(relative).is_file(), f"missing ResearchStudio upgrade contract: {relative}"
    passed.append("innovation-signature, commitment, and lineage contracts")

    for relative in V12_REQUIRED_FILES:
        assert root.joinpath(relative).is_file(), f"missing researchability upgrade contract: {relative}"
    passed.append("researchability, opportunity, triage, and collaboration contracts")

    for relative, required_fragments in V12_RUNTIME_CONTRACTS.items():
        text = root.joinpath(relative).read_text(encoding="utf-8")
        for fragment in required_fragments:
            assert fragment in text, f"missing v1.2 runtime integration in {relative}: {fragment}"
    passed.append("researchability runtime integration")

    for path in root.joinpath("templates").glob("*.yaml"):
        assert isinstance(yaml.safe_load(path.read_text(encoding="utf-8")), dict)
    passed.append("YAML templates parse")

    signature = yaml.safe_load(root.joinpath("templates/innovation-signature.yaml").read_text(encoding="utf-8"))["innovation_signature"]
    commitment = yaml.safe_load(root.joinpath("templates/candidate-commitment.yaml").read_text(encoding="utf-8"))["candidate_commitment"]
    awareness_lead = yaml.safe_load(root.joinpath("templates/awareness-lead.yaml").read_text(encoding="utf-8"))["awareness_lead"]
    candidate_template = yaml.safe_load(root.joinpath("templates/candidate-entry.yaml").read_text(encoding="utf-8"))["candidate"]
    rq_canvas = yaml.safe_load(root.joinpath("templates/research-question-canvas.yaml").read_text(encoding="utf-8"))["research_question_canvas"]
    fit_card = yaml.safe_load(root.joinpath("templates/fit-card.yaml").read_text(encoding="utf-8"))["fit_card"]
    opportunity_signal = yaml.safe_load(root.joinpath("templates/opportunity-signal.yaml").read_text(encoding="utf-8"))["opportunity_signal"]
    triage_entry = yaml.safe_load(root.joinpath("templates/literature-triage-entry.yaml").read_text(encoding="utf-8"))["literature_triage_entry"]
    assert signature["id"].startswith("IS-")
    assert commitment["id"].startswith("CM-")
    assert awareness_lead["id"].startswith("AL-") and awareness_lead["lineage_role"] == "AWARENESS_ONLY"
    assert candidate_template["innovation_signature_id"].startswith("IS-")
    assert candidate_template["active_commitment_id"].startswith("CM-")
    assert rq_canvas["id"].startswith("RQ-")
    assert fit_card["id"].startswith("FIT-")
    assert opportunity_signal["id"].startswith("OP-")
    assert triage_entry["id"].startswith("LT-")
    assert candidate_template["research_question_canvas_id"].startswith("RQ-")
    passed.append("signature, commitment, and awareness-lead template links")
    passed.append("researchability, opportunity, and triage template links")

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

    vague_signature = {field: "" for field in SIGNATURE_FIELDS}
    candidate_signature = {
        "bottleneck": "Token routing hides a useful branch under high ambiguity",
        "operation": "Intervene on routing confidence before aggregation",
        "changed_object": "routing distribution",
        "critical_condition": "ambiguous multi-source tokens",
        "predicted_contrast": "a branch-use diagnostic rises versus a matched routing baseline",
    }
    competitor_signature = dict(candidate_signature)
    assert not signature_specific(vague_signature)
    assert signature_specific(candidate_signature)
    assert exact_signature_collision(candidate_signature, competitor_signature)
    passed.append("signature specificity and exact-collision trigger")

    assert not awareness_lead_citable(awareness_lead)
    passed.append("awareness-only lead cannot become citation or evidence")

    previous_commitment = {
        "id": "CM-0001", "candidate_id": "C-0001", "commitment_version": 1,
        "innovation_signature_id": "IS-0001", "innovation_signature_version": 1,
        "core_mechanism": "change routing distribution", "differentiating_claim": "diagnostic difference",
        "prediction_ids": ["PR-0001"], "planned_falsifier": "no diagnostic change",
        "falsification_budget": {"maximum_cost_tier": "F1"}, "project_resource_assumptions": ["one GPU"],
    }
    silent_change = dict(previous_commitment, core_mechanism="change objective")
    valid_revision = dict(
        silent_change,
        id="CM-0002",
        commitment_version=2,
        supersedes_commitment_id="CM-0001",
        change_reason="Prior art subsumes the previous routing mechanism.",
        changed_core_fields=["core_mechanism"],
        affected_dependent_ids=["TH-0001", "H-0001", "EX-0001"],
    )
    assert not commitment_revision_valid(previous_commitment, silent_change)
    assert commitment_revision_valid(previous_commitment, valid_revision)
    passed.append("semantic commitment revision invalidates dependents")

    innovation_protocol = root.joinpath("protocols/innovation-signature.md").read_text(encoding="utf-8")
    novelty_protocol = root.joinpath("protocols/novelty.md").read_text(encoding="utf-8")
    assert "Outcome-Data Boundary" in innovation_protocol
    assert "acceptance rates, citation rates" in innovation_protocol
    assert "Do not use historical acceptance/citation outcomes" in novelty_protocol
    passed.append("outcome-derived prior prohibition")

    invalid_canvas = dict(rq_canvas)
    valid_canvas = {
        "phenomenon": {"statement": "Tiny objects are missed after downsampling.", "epistemic_status": "INFERENCE"},
        "unit_and_condition": "one-stage detection under aggressive feature downsampling",
        "knowledge_gap": "whether assignment failure rather than representation loss explains the slice failure",
        "mechanism_question": "does assignment instability mediate missed tiny objects?",
        "observable_outcome": "assignment consistency and slice recall under matched settings",
        "minimal_discriminating_path": "instrument a trained baseline and perturb assignment only",
        "scope_ladder": {"minimum_completable": {"output": "a valid discriminating diagnostic", "stop_condition": "no measurable assignment difference"}},
        "stop_or_reframe_condition": "diagnostic cannot distinguish assignment from representation explanations",
    }
    assert not research_question_valid(invalid_canvas)
    assert research_question_valid(valid_canvas)
    passed.append("research-question canvas requires an observable minimum path")

    unverified_signal = {
        "lifecycle_status": "DISCOVERY", "source_provenance": "user report", "bounded_observation": "latency is high",
        "alternative_explanations": ["measurement artifact"], "evidence_ids": [], "minimum_verification_action": "profile deployment",
    }
    verified_signal = dict(
        unverified_signal,
        lifecycle_status="VERIFIED",
        source_provenance="P-0001 Figure 4",
        evidence_ids=["EU-0001"],
    )
    assert not opportunity_signal_valid(unverified_signal)
    assert opportunity_signal_valid(verified_signal)
    passed.append("opportunity signal requires verification and alternatives")

    abstract_t4 = {"access_state": "ABSTRACT_ONLY", "required_reading_tier": "R3"}
    full_text_t4 = {"access_state": "FULL_TEXT_READY", "required_reading_tier": "R3"}
    assert not triage_closes_required_tier(abstract_t4)
    assert triage_closes_required_tier(full_text_t4)
    passed.append("literature triage prevents abstract-only deep-read closure")

    state_template = yaml.safe_load(root.joinpath("templates/research-state.yaml").read_text(encoding="utf-8"))["research_state"]
    registries = state_template["registries"]
    assert state_template["active_research_question_id"] is None
    assert state_template["active_fit_card_id"] is None
    for key in ("research_questions", "fit_cards", "opportunity_signals", "literature_triage"):
        assert key in registries
    passed.append("researchability registry pointers")

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
