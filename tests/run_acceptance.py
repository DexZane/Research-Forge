#!/usr/bin/env python3
"""Deterministic contract checks for the Research Forge v1 package."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
import tempfile
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
    "runtime", "scripts", "examples", "tests",
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

V13_REQUIRED_FILES = (
    "protocols/implementation-leverage.md",
    "schemas/implementation-leverage-schema.md",
    "templates/implementation-leverage-plan.yaml",
)

V14_REQUIRED_FILES = (
    "runtime/capability-preflight.md",
    "schemas/capability-profile-schema.md",
    "templates/capability-profile.yaml",
    "templates/reading-queue.md",
    "scripts/validate_project.py",
    "tests/behavioral-evals.md",
)

V12_RUNTIME_CONTRACTS = {
    "runtime/boot.md": ("research-question", "opportunity signals", "literature-triage"),
    "runtime/context-loading.md": ("research-question canvas", "literature-triage", "minimum discriminating paths"),
    "runtime/gates.md": ("FIT card/preflight outcome", "`PROCEED` may be approved", "`REFRAME` maps to `REVISE`"),
    "runtime/transaction.md": ("candidate opportunity-signal provenance", "Researchability Revision", "gate-critical `LT-`"),
    "protocols/integrity.md": ("Active `RQ-` and `FIT-` pointers", "non-full-text access cannot close", "minimum discriminating path"),
}

V13_RUNTIME_CONTRACTS = {
    "runtime/boot.md": ("implementation-leverage", "active implementation-leverage plan/source revisions"),
    "runtime/context-loading.md": ("implementation-leverage source scan", "finalized implementation-leverage plan/pinned source revisions"),
    "runtime/transaction.md": ("implementation-leverage source/revision/license/trust/dependency fields", "Implementation-Leverage Revision"),
    "runtime/handoff.md": ("finalized implementation-leverage plan ID", "must follow each pinned `REUSE_AS_IS`"),
}

V14_RUNTIME_CONTRACTS = {
    "runtime/boot.md": ("capability profile", "reading-queue"),
    "runtime/gates.md": ("active `CAP-` capability profile", "source trust/dependency findings"),
    "runtime/transaction.md": ("active research-question/fit/capability pointers", "Capability Revision"),
    "runtime/handoff.md": ("active capability profile", "own capability preflight"),
    "protocols/implementation-leverage.md": ("`TRUST_REVIEWED`", "never clone, install, execute"),
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


def preflight_outcome_valid(fit_card: dict) -> bool:
    """Keep researchability assessment values in the canonical vocabulary."""
    return fit_card.get("preflight_outcome") in {
        "PROCEED", "HOLD_SCOPE", "HOLD_RESOURCE", "REFRAME",
    }


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


def candidate_signal_trace_valid(candidate: dict, signals: dict[str, dict]) -> bool:
    """Require every active candidate to trace to an RQ canvas and a verified OP signal."""
    research_question_id = candidate.get("research_question_canvas_id")
    signal_ids = candidate.get("opportunity_signal_ids", [])
    return (
        isinstance(research_question_id, str)
        and research_question_id.startswith("RQ-")
        and bool(signal_ids)
        and any(opportunity_signal_valid(signals.get(signal_id, {})) for signal_id in signal_ids)
    )


def triage_closes_required_tier(entry: dict) -> bool:
    """Fail closed when a required reading tier lacks its required source access."""
    access_state = entry.get("access_state")
    if entry.get("required_reading_tier") in {"R2", "R3", "R4"}:
        return access_state == "FULL_TEXT_READY"
    return access_state in {"FULL_TEXT_READY", "ABSTRACT_ONLY", "NOT_APPLICABLE"}


def dependency_assessment_valid(assessment: dict) -> bool:
    """Keep source-audit coverage explicit without claiming code safety."""
    return (
        assessment.get("assessment_scope") == "METADATA_ONLY"
        and assessment.get("transitive_dependency_visibility") in {
            "KNOWN_DIRECT_ONLY", "KNOWN_TRANSITIVE", "UNKNOWN", "NOT_APPLICABLE",
        }
        and assessment.get("vulnerability_check_status") in {
            "NOT_RUN", "NO_FINDINGS_RECORDED", "FINDINGS_RECORDED", "UNAVAILABLE", "NOT_APPLICABLE",
        }
        and isinstance(assessment.get("known_finding_ids"), list)
    )


def capability_profile_valid(profile: dict) -> bool:
    """Require checked, secret-free host capability records."""
    entries = profile.get("capabilities", [])
    allowed_statuses = {"AVAILABLE", "LIMITED", "UNAVAILABLE", "UNKNOWN", "NOT_REQUIRED"}
    required_names = {
        "WEB_SEARCH", "SCHOLARLY_METADATA", "AUTHORIZED_FULL_TEXT", "PDF_TEXT_EXTRACTION",
        "PROJECT_WORKSPACE_WRITE", "PYTHON_YAML_VALIDATION", "GIT_REVISION_INSPECTION",
        "BIBTEX_VALIDATION", "ISOLATED_CODE_EXECUTION", "ZOTERO_WRITE_API",
    }
    names = {entry.get("name") for entry in entries if isinstance(entry, dict)}
    return (
        isinstance(profile.get("id"), str)
        and profile["id"].startswith("CAP-")
        and required_names <= names
        and all(
            entry.get("status") in allowed_statuses
            and (
                entry.get("status") not in {"AVAILABLE", "LIMITED"}
                or bool(entry.get("check_basis"))
            )
            and (
                entry.get("status") != "LIMITED"
                or bool(entry.get("limitation"))
            )
            for entry in entries
            if isinstance(entry, dict)
        )
    )


def considered_source_valid(source: dict) -> bool:
    """Require enough provenance to reproduce a source-scan decision."""
    return (
        source.get("source_kind") in {
            "OFFICIAL_CODE", "MAINTAINED_LIBRARY", "REPRODUCTION", "OTHER_OPEN_SOURCE",
        }
        and isinstance(source.get("repository_url"), str)
        and bool(source["repository_url"].strip())
        and isinstance(source.get("revision_or_release"), str)
        and bool(source["revision_or_release"].strip())
        and isinstance(source.get("component_locator"), str)
        and bool(source["component_locator"].strip())
        and isinstance(source.get("declared_license_identifier"), str)
        and bool(source["declared_license_identifier"].strip())
        and source.get("license_status") in {
            "LICENSE_COMPATIBLE", "LICENSE_REVIEW_REQUIRED", "LICENSE_INCOMPATIBLE", "LICENSE_UNKNOWN",
        }
        and source.get("verification_status") == "VERIFIED"
        and bool(source.get("evidence_ids"))
        and isinstance(source.get("maintenance_or_reproducibility_limits"), str)
        and bool(source["maintenance_or_reproducibility_limits"].strip())
        and source.get("trust_status") in {
            "TRUST_UNVERIFIED", "TRUST_REVIEWED", "TRUST_BLOCKED",
        }
        and source.get("execution_status") == "NOT_EXECUTED"
        and dependency_assessment_valid(source.get("dependency_assessment", {}))
        and (
            source.get("trust_status") != "TRUST_REVIEWED"
            or bool(source.get("trust_evidence_ids"))
        )
    )


def implementation_component_valid(component: dict, final: bool = False) -> bool:
    """Enforce reuse-first provenance and a narrow, auditable new-code fallback."""
    decision = component.get("decision")
    considered_sources = component.get("considered_sources", [])
    common_valid = (
        isinstance(component.get("component_key"), str)
        and bool(component["component_key"].strip())
        and isinstance(component.get("frozen_role"), str)
        and bool(component["frozen_role"].strip())
        and isinstance(component.get("required_capability"), str)
        and bool(component["required_capability"].strip())
        and isinstance(considered_sources, list)
    )
    if not common_valid or decision not in {"REUSE_AS_IS", "ADAPT_EXISTING", "NEW_MINIMAL", "DEFERRED"}:
        return False
    if decision == "DEFERRED":
        return not final
    if not considered_sources or not all(considered_source_valid(source) for source in considered_sources):
        return False

    selected = component.get("selected_source", {})
    selected_valid = (
        selected.get("source_kind") in {
            "OFFICIAL_CODE", "MAINTAINED_LIBRARY", "REPRODUCTION", "OTHER_OPEN_SOURCE",
        }
        and isinstance(selected.get("repository_url"), str)
        and bool(selected["repository_url"].strip())
        and isinstance(selected.get("revision_or_release"), str)
        and bool(selected["revision_or_release"].strip())
        and isinstance(selected.get("component_locator"), str)
        and bool(selected["component_locator"].strip())
        and isinstance(selected.get("declared_license_identifier"), str)
        and bool(selected["declared_license_identifier"].strip())
        and selected.get("license_status") == "LICENSE_COMPATIBLE"
        and selected.get("verification_status") == "VERIFIED"
        and bool(selected.get("evidence_ids"))
        and selected.get("trust_status") == "TRUST_REVIEWED"
        and bool(selected.get("trust_evidence_ids"))
        and selected.get("execution_status") == "NOT_EXECUTED"
        and dependency_assessment_valid(selected.get("dependency_assessment", {}))
    )
    selected_is_considered = any(
        source.get("repository_url") == selected.get("repository_url")
        and source.get("revision_or_release") == selected.get("revision_or_release")
        and source.get("component_locator") == selected.get("component_locator")
        for source in considered_sources
    )
    adaptation = component.get("adaptation", {})
    no_scientific_delta = (
        adaptation.get("changes_frozen_mechanism") is False
        and adaptation.get("changes_primary_metric_or_budget") is False
    )
    if decision == "REUSE_AS_IS":
        return selected_valid and selected_is_considered and no_scientific_delta
    if decision == "ADAPT_EXISTING":
        return (
            selected_valid
            and selected_is_considered
            and no_scientific_delta
            and isinstance(adaptation.get("exact_delta"), str)
            and bool(adaptation["exact_delta"].strip())
            and bool(adaptation.get("fairness_control_ids"))
        )

    new_code = component.get("new_minimal_code", {})
    return (
        bool(new_code.get("source_rejection_reasons"))
        and all(
            isinstance(source.get("rejection_reason"), str) and bool(source["rejection_reason"].strip())
            for source in considered_sources
        )
        and isinstance(new_code.get("necessity_for_frozen_requirement"), str)
        and bool(new_code["necessity_for_frozen_requirement"].strip())
        and isinstance(new_code.get("minimal_public_interface"), str)
        and bool(new_code["minimal_public_interface"].strip())
        and bool(new_code.get("equivalence_or_ablation_experiment_ids"))
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

    for relative in V13_REQUIRED_FILES:
        assert root.joinpath(relative).is_file(), f"missing implementation-leverage contract: {relative}"
    passed.append("implementation-leverage contracts")

    for relative in V14_REQUIRED_FILES:
        assert root.joinpath(relative).is_file(), f"missing v1.4 execution contract: {relative}"
    passed.append("capability, trust, reading-queue, validator, and behavioral-eval contracts")

    for relative, required_fragments in V12_RUNTIME_CONTRACTS.items():
        text = root.joinpath(relative).read_text(encoding="utf-8")
        for fragment in required_fragments:
            assert fragment in text, f"missing v1.2 runtime integration in {relative}: {fragment}"
    passed.append("researchability runtime integration")

    for relative, required_fragments in V13_RUNTIME_CONTRACTS.items():
        text = root.joinpath(relative).read_text(encoding="utf-8")
        for fragment in required_fragments:
            assert fragment in text, f"missing v1.3 runtime integration in {relative}: {fragment}"
    passed.append("implementation-leverage runtime integration")

    for relative, required_fragments in V14_RUNTIME_CONTRACTS.items():
        text = root.joinpath(relative).read_text(encoding="utf-8")
        for fragment in required_fragments:
            assert fragment in text, f"missing v1.4 runtime integration in {relative}: {fragment}"
    passed.append("capability and source-trust runtime integration")

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
    capability_profile = yaml.safe_load(root.joinpath("templates/capability-profile.yaml").read_text(encoding="utf-8"))["capability_profile"]
    leverage_plan = yaml.safe_load(root.joinpath("templates/implementation-leverage-plan.yaml").read_text(encoding="utf-8"))["implementation_leverage_plan"]
    assert signature["id"].startswith("IS-")
    assert commitment["id"].startswith("CM-")
    assert awareness_lead["id"].startswith("AL-") and awareness_lead["lineage_role"] == "AWARENESS_ONLY"
    assert candidate_template["innovation_signature_id"].startswith("IS-")
    assert candidate_template["active_commitment_id"].startswith("CM-")
    assert rq_canvas["id"].startswith("RQ-")
    assert fit_card["id"].startswith("FIT-")
    assert fit_card["preflight_outcome"] is None
    assert opportunity_signal["id"].startswith("OP-")
    assert triage_entry["id"].startswith("LT-")
    assert capability_profile_valid(capability_profile)
    unavailable_capability = yaml.safe_load(
        yaml.safe_dump(capability_profile, sort_keys=False),
    )
    unavailable_capability["capabilities"][0]["status"] = "AVAILABLE"
    unavailable_capability["capabilities"][0]["check_basis"] = None
    assert not capability_profile_valid(unavailable_capability)
    assert leverage_plan["id"].startswith("IL-")
    assert leverage_plan["decision_policy"] == "REUSE_ADAPT_NEW_MINIMAL"
    assert candidate_template["research_question_canvas_id"].startswith("RQ-")
    passed.append("signature, commitment, and awareness-lead template links")
    passed.append("researchability, opportunity, and triage template links")
    passed.append("capability profile template links")
    passed.append("implementation-leverage template links")

    behavioral_evals = root.joinpath("tests/behavioral-evals.md").read_text(encoding="utf-8")
    for case in ("B1", "B2", "B3", "B4", "B5", "B6", "TRUST_UNVERIFIED", "HOLD_RESOURCE"):
        assert case in behavioral_evals
    passed.append("behavioral eval contract covers capability, source trust, novelty, Zotero, and handoff")

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

    canonical_enums = root.joinpath("schemas/ids-and-enums.md").read_text(encoding="utf-8")
    researchability_protocol = root.joinpath("protocols/researchability.md").read_text(encoding="utf-8")
    scope_state = root.joinpath("states/S01-scope.md").read_text(encoding="utf-8")
    assert "Researchability preflight outcome: `PROCEED`, `HOLD_SCOPE`, `HOLD_RESOURCE`, `REFRAME`" in canonical_enums
    assert preflight_outcome_valid(dict(fit_card, preflight_outcome="PROCEED"))
    assert not preflight_outcome_valid(dict(fit_card, preflight_outcome="APPROVED"))
    for routing_phrase in ("carry unknowns into S02", "remain at G1", "return to S00/S01"):
        assert routing_phrase not in researchability_protocol
    assert "`PROCEED` plus explicit G1 `APPROVED` transitions to S02" in scope_state
    passed.append("preflight outcomes are canonical and routing stays in S01/runtime")

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

    untraced_candidate = dict(candidate_template, opportunity_signal_ids=[])
    unverified_candidate = dict(candidate_template, opportunity_signal_ids=["OP-0001"])
    verified_candidate = dict(candidate_template, opportunity_signal_ids=["OP-0002"])
    signals = {"OP-0001": unverified_signal, "OP-0002": verified_signal}
    assert not candidate_signal_trace_valid(untraced_candidate, signals)
    assert not candidate_signal_trace_valid(unverified_candidate, signals)
    assert candidate_signal_trace_valid(verified_candidate, signals)
    for relative in (
        "schemas/candidate-schema.md", "schemas/state-schema.md",
        "protocols/integrity.md", "states/S06-candidate-portfolio.md",
    ):
        contract = root.joinpath(relative).read_text(encoding="utf-8")
        assert "explicitly bounded evidence" not in contract
    passed.append("active candidates require verified opportunity-signal provenance")

    blocked_access_states = (
        "ABSTRACT_ONLY", "UNAVAILABLE", "ACCESS_REQUESTED", "SUPPLEMENT_MISSING", "CODE_MISSING",
    )
    full_text_t4 = {"access_state": "FULL_TEXT_READY", "required_reading_tier": "R3"}
    for access_state in blocked_access_states:
        assert not triage_closes_required_tier({"access_state": access_state, "required_reading_tier": "R3"})
    assert triage_closes_required_tier(full_text_t4)
    passed.append("literature triage fails closed without full-text access")

    reused_component = {
        "component_key": "baseline_encoder",
        "frozen_role": "shared baseline infrastructure",
        "required_capability": "extract frozen encoder features",
        "decision": "REUSE_AS_IS",
        "considered_sources": [{
            "source_kind": "OFFICIAL_CODE",
            "repository_url": "https://github.com/example/official-code",
            "revision_or_release": "abc123",
            "component_locator": "models/encoder.py:Encoder",
            "declared_license_identifier": "Apache-2.0",
            "license_status": "LICENSE_COMPATIBLE",
            "verification_status": "VERIFIED",
            "evidence_ids": ["EU-0001"],
            "rejection_reason": None,
            "maintenance_or_reproducibility_limits": "Pin the revision because main may change.",
            "trust_status": "TRUST_REVIEWED",
            "trust_evidence_ids": ["EU-0002"],
            "execution_status": "NOT_EXECUTED",
            "dependency_assessment": {
                "manifest_or_lockfile": "requirements.txt",
                "transitive_dependency_visibility": "KNOWN_DIRECT_ONLY",
                "vulnerability_check_status": "UNAVAILABLE",
                "known_finding_ids": [],
                "assessment_scope": "METADATA_ONLY",
            },
        }],
        "selected_source": {
            "source_kind": "OFFICIAL_CODE",
            "repository_url": "https://github.com/example/official-code",
            "revision_or_release": "abc123",
            "component_locator": "models/encoder.py:Encoder",
            "declared_license_identifier": "Apache-2.0",
            "license_status": "LICENSE_COMPATIBLE",
            "verification_status": "VERIFIED",
            "evidence_ids": ["EU-0001"],
            "trust_status": "TRUST_REVIEWED",
            "trust_evidence_ids": ["EU-0002"],
            "execution_status": "NOT_EXECUTED",
            "dependency_assessment": {
                "manifest_or_lockfile": "requirements.txt",
                "transitive_dependency_visibility": "KNOWN_DIRECT_ONLY",
                "vulnerability_check_status": "UNAVAILABLE",
                "known_finding_ids": [],
                "assessment_scope": "METADATA_ONLY",
            },
        },
        "adaptation": {
            "exact_delta": None,
            "changes_frozen_mechanism": False,
            "changes_primary_metric_or_budget": False,
            "fairness_control_ids": [],
        },
        "new_minimal_code": {},
    }
    adapted_component = dict(
        reused_component,
        decision="ADAPT_EXISTING",
        adaptation={
            "exact_delta": "Expose an existing intermediate activation through the documented hook.",
            "changes_frozen_mechanism": False,
            "changes_primary_metric_or_budget": False,
            "fairness_control_ids": ["EX-0002"],
        },
    )
    new_minimal_component = dict(
        reused_component,
        decision="NEW_MINIMAL",
        considered_sources=[{
            "source_kind": "OFFICIAL_CODE",
            "repository_url": "https://github.com/example/official-code",
            "revision_or_release": "abc123",
            "component_locator": "models/encoder.py:Encoder",
            "declared_license_identifier": "Apache-2.0",
            "license_status": "LICENSE_COMPATIBLE",
            "verification_status": "VERIFIED",
            "evidence_ids": ["EU-0001"],
            "rejection_reason": "The component cannot expose the frozen intervention boundary.",
            "maintenance_or_reproducibility_limits": "Pin the revision because main may change.",
            "trust_status": "TRUST_REVIEWED",
            "trust_evidence_ids": ["EU-0002"],
            "execution_status": "NOT_EXECUTED",
            "dependency_assessment": {
                "manifest_or_lockfile": "requirements.txt",
                "transitive_dependency_visibility": "KNOWN_DIRECT_ONLY",
                "vulnerability_check_status": "UNAVAILABLE",
                "known_finding_ids": [],
                "assessment_scope": "METADATA_ONLY",
            },
        }],
        selected_source={},
        new_minimal_code={
            "source_rejection_reasons": ["Official and library components cannot expose the required intervention boundary."],
            "necessity_for_frozen_requirement": "The locked mechanism requires a local intervention at the assignment boundary.",
            "minimal_public_interface": "forward(assignments, intervention_mask) -> assignments",
            "equivalence_or_ablation_experiment_ids": ["EX-0003"],
        },
    )
    convenience_new_code = dict(
        new_minimal_component,
        new_minimal_code={
            "source_rejection_reasons": [],
            "necessity_for_frozen_requirement": "A custom module looks more novel.",
            "minimal_public_interface": "forward(x) -> y",
            "equivalence_or_ablation_experiment_ids": [],
        },
    )
    unknown_license_source = dict(
        reused_component["considered_sources"][0],
        license_status="LICENSE_UNKNOWN",
        rejection_reason="License status is unresolved and blocks reuse.",
    )
    unknown_license_component = dict(
        reused_component,
        considered_sources=[unknown_license_source],
        selected_source=dict(reused_component["selected_source"], license_status="LICENSE_UNKNOWN"),
    )
    unscanned_selection_component = dict(
        reused_component,
        selected_source=dict(
            reused_component["selected_source"],
            repository_url="https://github.com/example/different-code",
        ),
    )
    untrusted_selection_component = dict(
        reused_component,
        selected_source=dict(reused_component["selected_source"], trust_status="TRUST_UNVERIFIED"),
    )
    executed_selection_component = dict(
        reused_component,
        selected_source=dict(reused_component["selected_source"], execution_status="SANDBOX_AUTHORIZED"),
    )
    deferred_component = dict(reused_component, decision="DEFERRED")
    assert implementation_component_valid(reused_component, final=True)
    assert implementation_component_valid(adapted_component, final=True)
    assert implementation_component_valid(new_minimal_component, final=True)
    assert not implementation_component_valid(convenience_new_code, final=True)
    assert not implementation_component_valid(unknown_license_component, final=True)
    assert not implementation_component_valid(unscanned_selection_component, final=True)
    assert not implementation_component_valid(untrusted_selection_component, final=True)
    assert not implementation_component_valid(executed_selection_component, final=True)
    assert implementation_component_valid(deferred_component)
    assert not implementation_component_valid(deferred_component, final=True)
    implementation_protocol = root.joinpath("protocols/implementation-leverage.md").read_text(encoding="utf-8")
    assert "Do not search for components while generating candidates" in implementation_protocol
    assert "It is easier" in implementation_protocol
    passed.append("implementation leverage reuses first and constrains new code")

    state_template = yaml.safe_load(root.joinpath("templates/research-state.yaml").read_text(encoding="utf-8"))["research_state"]
    registries = state_template["registries"]
    assert state_template["active_research_question_id"] is None
    assert state_template["active_fit_card_id"] is None
    assert state_template["active_capability_profile_id"] is None
    assert state_template["active_implementation_leverage_plan_id"] is None
    assert state_template["bibliography"]["reading_queue_path"] == "exports/reading-queue.md"
    for key in (
        "research_questions", "fit_cards", "opportunity_signals", "literature_triage",
        "capability_profiles", "implementation_leverage",
    ):
        assert key in registries
    passed.append("researchability registry pointers")

    with tempfile.TemporaryDirectory(prefix="research-forge-project-validator-") as temporary:
        project_root = Path(temporary)
        state_directory = project_root / "state"
        exports_directory = project_root / "exports"
        state_directory.mkdir()
        exports_directory.mkdir()
        final_state = {
            "project_id": "research-project-0001",
            "schema_version": "1.5",
            "state": "S18_EXPERIMENT_DOSSIER",
            "state_iteration": 1,
            "status": "ACTIVE",
            "mode": "EXPLORATION",
            "pending_gate": "NONE",
            "active_capability_profile_id": "CAP-0001",
            "active_implementation_leverage_plan_id": "IL-0001",
            "registries": {
                "capability_profiles": "state/capability_profile_registry.yaml",
                "implementation_leverage": "state/implementation_leverage_registry.yaml",
            },
            "bibliography": {
                "export_path": "exports/references.bib",
                "reading_queue_path": "exports/reading-queue.md",
            },
            "version": 1,
            "updated_at": "2026-08-13T00:00:00Z",
        }
        state_directory.joinpath("research_state.yaml").write_text(
            yaml.safe_dump({"research_state": final_state}, sort_keys=False), encoding="utf-8",
        )
        state_directory.joinpath("capability_profile_registry.yaml").write_text(
            yaml.safe_dump({"records": [capability_profile]}, sort_keys=False), encoding="utf-8",
        )
        final_plan = {
            "id": "IL-0001",
            "components": [reused_component],
        }
        state_directory.joinpath("implementation_leverage_registry.yaml").write_text(
            yaml.safe_dump({"records": [final_plan]}, sort_keys=False), encoding="utf-8",
        )
        exports_directory.joinpath("references.bib").write_text(
            "@article{rf_p0001,\n  author = {Example, Agent},\n  title = {Example},\n  year = {2026}\n}\n",
            encoding="utf-8",
        )
        exports_directory.joinpath("reading-queue.md").write_text("# Reading queue\n", encoding="utf-8")
        validator = root / "scripts" / "validate_project.py"
        valid_result = subprocess.run(
            [sys.executable, str(validator), str(project_root)],
            text=True, capture_output=True, check=False,
        )
        assert valid_result.returncode == 0, valid_result.stdout + valid_result.stderr

        json_result = subprocess.run(
            [sys.executable, str(validator), str(project_root), "--json"],
            text=True, capture_output=True, check=False,
        )
        assert json_result.returncode == 0, json_result.stdout + json_result.stderr
        assert yaml.safe_load(json_result.stdout)["valid"] is True

        final_state["active_capability_profile_id"] = "IL-0001"
        state_directory.joinpath("research_state.yaml").write_text(
            yaml.safe_dump({"research_state": final_state}, sort_keys=False), encoding="utf-8",
        )
        invalid_pointer_result = subprocess.run(
            [sys.executable, str(validator), str(project_root)],
            text=True, capture_output=True, check=False,
        )
        assert invalid_pointer_result.returncode != 0
        assert "must reference a CAP- record" in invalid_pointer_result.stdout
        final_state["active_capability_profile_id"] = "CAP-0001"
        state_directory.joinpath("research_state.yaml").write_text(
            yaml.safe_dump({"research_state": final_state}, sort_keys=False), encoding="utf-8",
        )

        final_plan["components"][0]["selected_source"]["trust_status"] = "TRUST_UNVERIFIED"
        state_directory.joinpath("implementation_leverage_registry.yaml").write_text(
            yaml.safe_dump({"records": [final_plan]}, sort_keys=False), encoding="utf-8",
        )
        invalid_result = subprocess.run(
            [sys.executable, str(validator), str(project_root)],
            text=True, capture_output=True, check=False,
        )
        assert invalid_result.returncode != 0
        assert "TRUST_REVIEWED" in invalid_result.stdout
    passed.append("project workspace validator accepts valid state and rejects invalid pointers/untrusted final source")

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
