#!/usr/bin/env python3
"""Validate a Research Forge project workspace without changing it."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections.abc import Iterator
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment failure
    raise SystemExit("PyYAML is required: install pyyaml in the validation environment.") from exc


CAPABILITY_STATUSES = {"AVAILABLE", "LIMITED", "UNAVAILABLE", "UNKNOWN", "NOT_REQUIRED"}
REQUIRED_CAPABILITIES = {
    "WEB_SEARCH", "SCHOLARLY_METADATA", "AUTHORIZED_FULL_TEXT", "PDF_TEXT_EXTRACTION",
    "PROJECT_WORKSPACE_WRITE", "PYTHON_YAML_VALIDATION", "GIT_REVISION_INSPECTION",
    "BIBTEX_VALIDATION", "ISOLATED_CODE_EXECUTION", "ZOTERO_WRITE_API",
}
TRUST_STATUSES = {"TRUST_UNVERIFIED", "TRUST_REVIEWED", "TRUST_BLOCKED"}
FINAL_STATES = {"S18_EXPERIMENT_DOSSIER", "COMPLETE"}
STATE_REQUIRED_FIELDS = {
    "project_id", "schema_version", "state", "state_iteration", "status", "mode",
    "pending_gate", "registries", "bibliography", "version", "updated_at",
}


def load_yaml(path: Path, errors: list[str]) -> Any:
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        errors.append(f"{path}: cannot parse YAML ({exc})")
        return None


def walk_records(value: Any) -> Iterator[dict[str, Any]]:
    if isinstance(value, dict):
        if isinstance(value.get("id"), str):
            yield value
        for child in value.values():
            yield from walk_records(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk_records(child)


def safe_relative_path(root: Path, raw_path: Any, errors: list[str], label: str) -> Path | None:
    if not isinstance(raw_path, str) or not raw_path.strip():
        errors.append(f"{label}: missing relative path")
        return None
    candidate = (root / raw_path).resolve()
    try:
        candidate.relative_to(root.resolve())
    except ValueError:
        errors.append(f"{label}: path escapes project root: {raw_path}")
        return None
    return candidate


def selected_source_valid(source: dict[str, Any]) -> bool:
    return (
        isinstance(source.get("repository_url"), str)
        and bool(source["repository_url"].strip())
        and isinstance(source.get("revision_or_release"), str)
        and bool(source["revision_or_release"].strip())
        and isinstance(source.get("component_locator"), str)
        and bool(source["component_locator"].strip())
        and source.get("license_status") == "LICENSE_COMPATIBLE"
        and source.get("trust_status") == "TRUST_REVIEWED"
        and source.get("execution_status") == "NOT_EXECUTED"
    )


def validate_capability_profile(record: dict[str, Any], errors: list[str]) -> None:
    if not str(record.get("id", "")).startswith("CAP-"):
        return
    capabilities = record.get("capabilities")
    if not isinstance(capabilities, list) or not capabilities:
        errors.append(f"{record['id']}: capability profile has no capability entries")
        return
    names = {entry.get("name") for entry in capabilities if isinstance(entry, dict)}
    missing = sorted(REQUIRED_CAPABILITIES - names)
    if missing:
        errors.append(f"{record['id']}: missing capability entries: {', '.join(missing)}")
    for entry in capabilities:
        if not isinstance(entry, dict):
            errors.append(f"{record['id']}: malformed capability entry")
            continue
        status = entry.get("status")
        name = entry.get("name", "<unnamed>")
        if status not in CAPABILITY_STATUSES:
            errors.append(f"{record['id']}/{name}: invalid capability status {status!r}")
        if status in {"AVAILABLE", "LIMITED"} and not entry.get("check_basis"):
            errors.append(f"{record['id']}/{name}: available capability lacks check basis")
        if status == "LIMITED" and not entry.get("limitation"):
            errors.append(f"{record['id']}/{name}: limited capability lacks limitation")


def validate_final_implementation_plan(record: dict[str, Any], errors: list[str]) -> None:
    if not str(record.get("id", "")).startswith("IL-"):
        return
    for component in record.get("components", []):
        if not isinstance(component, dict):
            errors.append(f"{record['id']}: malformed implementation component")
            continue
        decision = component.get("decision")
        key = component.get("component_key", "<unnamed>")
        if decision == "DEFERRED":
            errors.append(f"{record['id']}/{key}: final plan contains DEFERRED component")
        if decision in {"REUSE_AS_IS", "ADAPT_EXISTING"} and not selected_source_valid(component.get("selected_source", {})):
            errors.append(
                f"{record['id']}/{key}: selected source needs URL, revision, locator, compatible license, "
                "TRUST_REVIEWED status, and NOT_EXECUTED status"
            )


def validate_bibliography(path: Path, errors: list[str]) -> None:
    if not path.is_file():
        errors.append(f"bibliography export missing: {path}")
        return
    text = path.read_text(encoding="utf-8")
    entries = re.findall(r"(?m)^@\w+\{([^,]+),[ \t]*$", text)
    if not entries:
        errors.append(f"bibliography export has no parseable entries: {path}")
    if len(entries) != len(set(entries)):
        errors.append(f"bibliography export has duplicate keys: {path}")


def validate_project(root: Path) -> list[str]:
    errors: list[str] = []
    root = root.resolve()
    state_path = root / "state" / "research_state.yaml"
    if not state_path.is_file():
        return [f"missing state file: {state_path}"]

    state = load_yaml(state_path, errors)
    if not isinstance(state, dict):
        return errors or [f"{state_path}: expected a YAML mapping"]
    state = state.get("research_state", state)
    if not isinstance(state, dict):
        return errors + [f"{state_path}: missing research_state mapping"]

    missing = sorted(STATE_REQUIRED_FIELDS - state.keys())
    if missing:
        errors.append(f"research state missing required fields: {', '.join(missing)}")

    registry_paths: list[Path] = []
    registries = state.get("registries", {})
    if not isinstance(registries, dict):
        errors.append("research state registries must be a mapping")
    else:
        for name, raw_path in registries.items():
            path = safe_relative_path(root, raw_path, errors, f"registry {name}")
            if path is not None:
                registry_paths.append(path)
                if not path.is_file():
                    errors.append(f"registry {name} is missing: {path}")

    all_records: dict[str, dict[str, Any]] = {}
    for path in [state_path, *registry_paths]:
        if not path.is_file():
            continue
        payload = load_yaml(path, errors)
        for record in walk_records(payload):
            record_id = record["id"]
            if record_id in all_records:
                errors.append(f"duplicate record ID: {record_id}")
            else:
                all_records[record_id] = record

    for record in all_records.values():
        validate_capability_profile(record, errors)

    active_pointers = {
        key: value for key, value in state.items()
        if key.startswith("active_") and key.endswith("_id") and value is not None
    }
    for key, record_id in active_pointers.items():
        if record_id not in all_records:
            errors.append(f"{key} does not resolve to a record: {record_id}")

    state_name = state.get("state")
    capability_id = state.get("active_capability_profile_id")
    if state_name not in {"S00_INTAKE", None} and not capability_id:
        errors.append("active_capability_profile_id is required from S01 onward")
    if capability_id and capability_id not in all_records:
        errors.append(f"active_capability_profile_id does not resolve to a record: {capability_id}")
    elif capability_id and not str(capability_id).startswith("CAP-"):
        errors.append(f"active_capability_profile_id must reference a CAP- record: {capability_id}")

    bibliography = state.get("bibliography", {})
    if state_name in FINAL_STATES or state.get("status") == "COMPLETE":
        if not isinstance(bibliography, dict):
            errors.append("final state requires bibliography mapping")
        else:
            export_path = safe_relative_path(root, bibliography.get("export_path"), errors, "bibliography export")
            if export_path is not None:
                validate_bibliography(export_path, errors)
            queue_path = safe_relative_path(root, bibliography.get("reading_queue_path"), errors, "reading queue")
            if queue_path is not None and not queue_path.is_file():
                errors.append(f"reading queue missing: {queue_path}")
        plan_id = state.get("active_implementation_leverage_plan_id")
        if not plan_id:
            errors.append("final state requires active_implementation_leverage_plan_id")
        elif plan_id in all_records:
            if not str(plan_id).startswith("IL-"):
                errors.append(
                    "active_implementation_leverage_plan_id must reference an IL- record: "
                    f"{plan_id}"
                )
            else:
                validate_final_implementation_plan(all_records[plan_id], errors)

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_root", type=Path, help="Research Forge project workspace to validate")
    parser.add_argument("--json", action="store_true", help="Emit a JSON validation report")
    args = parser.parse_args()

    errors = validate_project(args.project_root)
    report = {"project_root": str(args.project_root.resolve()), "valid": not errors, "errors": errors}
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    elif errors:
        print("Research Forge project validation: FAIL")
        for error in errors:
            print(f"- {error}")
    else:
        print("Research Forge project validation: PASS")
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
