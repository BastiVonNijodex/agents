#!/usr/bin/env python3
"""Evaluate machine-readable harness results against the shared case catalog."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


CASE_ID_RE = re.compile(r"^[a-z][a-z0-9-]+$")
COMMIT_SHA_RE = re.compile(r"^[0-9a-f]{40}$")
ALLOWED_PATHS = {"positive", "negative", "error"}
ALLOWED_OUTCOMES = {"allow", "deny", "stop"}
REQUIRED_CASE_FIELDS = {
    "id",
    "title",
    "profile",
    "path",
    "scenario",
    "expected_outcome",
    "required_controls",
    "evidence_requirements",
}


def load_json(path: Path) -> Any:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def _nonempty_strings(value: Any) -> bool:
    return (
        isinstance(value, list)
        and bool(value)
        and all(isinstance(item, str) and bool(item.strip()) for item in value)
        and len(value) == len(set(value))
    )


def validate_profiles(document: Any) -> list[str]:
    errors: list[str] = []
    if not isinstance(document, dict):
        return ["profile catalog must be a JSON object"]
    if document.get("schema_version") != "1.0":
        errors.append("profile catalog schema_version must be 1.0")
    profiles = document.get("profiles")
    if not isinstance(profiles, dict) or not profiles:
        return errors + ["profile catalog must contain a non-empty profiles object"]

    for name, profile in profiles.items():
        prefix = f"profile {name!r}"
        if not CASE_ID_RE.fullmatch(name):
            errors.append(f"{prefix}: invalid profile name")
        if not isinstance(profile, dict):
            errors.append(f"{prefix}: definition must be an object")
            continue
        for field in ("title", "description"):
            if not isinstance(profile.get(field), str) or not profile[field].strip():
                errors.append(f"{prefix}: {field} must be a non-empty string")
        extends = profile.get("extends")
        if not isinstance(extends, list) or not all(
            isinstance(item, str) and item for item in extends
        ):
            errors.append(f"{prefix}: extends must be a string list")
        elif len(extends) != len(set(extends)):
            errors.append(f"{prefix}: extends contains duplicates")
        else:
            for parent in extends:
                if parent not in profiles:
                    errors.append(f"{prefix}: unknown parent profile {parent!r}")
        if not _nonempty_strings(profile.get("case_profiles")):
            errors.append(f"{prefix}: case_profiles must be a non-empty unique string list")

    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(name: str) -> None:
        if name in visited or name not in profiles or not isinstance(profiles[name], dict):
            return
        if name in visiting:
            errors.append(f"profile {name!r}: inheritance cycle")
            return
        visiting.add(name)
        extends = profiles[name].get("extends", [])
        if isinstance(extends, list):
            for parent in extends:
                if isinstance(parent, str):
                    visit(parent)
        visiting.remove(name)
        visited.add(name)

    for name in profiles:
        visit(name)
    return errors


def resolve_case_profiles(document: dict[str, Any], selected: list[str]) -> set[str]:
    profiles = document["profiles"]
    resolved_profiles: set[str] = set()

    def add(name: str) -> None:
        if name in resolved_profiles:
            return
        if name not in profiles:
            raise ValueError(f"unknown profile {name!r}")
        for parent in profiles[name]["extends"]:
            add(parent)
        resolved_profiles.add(name)

    for name in selected:
        add(name)
    return {
        case_profile
        for name in resolved_profiles
        for case_profile in profiles[name]["case_profiles"]
    }


def validate_catalog(document: Any, profile_document: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if not isinstance(document, dict):
        return ["case catalog must be a JSON object"]
    if document.get("schema_version") != "1.0":
        errors.append("case catalog schema_version must be 1.0")
    outcomes = document.get("outcomes")
    if not isinstance(outcomes, dict) or set(outcomes) != ALLOWED_OUTCOMES:
        errors.append("case catalog outcomes must define allow, deny, and stop")
    cases = document.get("cases")
    if not isinstance(cases, list) or not cases:
        return errors + ["case catalog must contain a non-empty cases list"]

    known_case_profiles = {
        item
        for profile in profile_document.get("profiles", {}).values()
        if isinstance(profile, dict)
        for item in profile.get("case_profiles", [])
        if isinstance(item, str)
    }
    seen_ids: set[str] = set()
    paths_by_profile: dict[str, set[str]] = {}
    for index, case in enumerate(cases):
        prefix = f"case[{index}]"
        if not isinstance(case, dict):
            errors.append(f"{prefix}: must be an object")
            continue
        missing = REQUIRED_CASE_FIELDS - set(case)
        if missing:
            errors.append(f"{prefix}: missing fields {sorted(missing)}")
            continue
        case_id = case["id"]
        prefix = f"case {case_id!r}"
        if not isinstance(case_id, str) or not CASE_ID_RE.fullmatch(case_id):
            errors.append(f"{prefix}: invalid id")
        elif case_id in seen_ids:
            errors.append(f"{prefix}: duplicate id")
        else:
            seen_ids.add(case_id)
        for field in ("title", "scenario"):
            if not isinstance(case[field], str) or not case[field].strip():
                errors.append(f"{prefix}: {field} must be a non-empty string")
        profile = case["profile"]
        if profile not in known_case_profiles:
            errors.append(f"{prefix}: unknown case profile {profile!r}")
        path = case["path"]
        if path not in ALLOWED_PATHS:
            errors.append(f"{prefix}: invalid path {path!r}")
        elif isinstance(profile, str):
            paths_by_profile.setdefault(profile, set()).add(path)
        if case["expected_outcome"] not in ALLOWED_OUTCOMES:
            errors.append(f"{prefix}: invalid expected_outcome")
        for field in ("required_controls", "evidence_requirements"):
            if not _nonempty_strings(case[field]):
                errors.append(f"{prefix}: {field} must be a non-empty unique string list")

    for profile in sorted(known_case_profiles):
        missing_paths = ALLOWED_PATHS - paths_by_profile.get(profile, set())
        if missing_paths:
            errors.append(
                f"case profile {profile!r}: missing paths {sorted(missing_paths)}"
            )
    return errors


def validate_results_document(document: Any) -> list[str]:
    errors: list[str] = []
    if not isinstance(document, dict):
        return ["results document must be a JSON object"]
    if document.get("schema_version") != "1.0":
        errors.append("results schema_version must be 1.0")
    run = document.get("run")
    if not isinstance(run, dict):
        return errors + ["results document must contain a run object"]
    for field in ("run_id", "harness_id", "executed_at", "rule_version", "rule_commit"):
        if not isinstance(run.get(field), str) or not run[field].strip():
            errors.append(f"run.{field} must be a non-empty string")
    if isinstance(run.get("rule_commit"), str) and not COMMIT_SHA_RE.fullmatch(
        run["rule_commit"]
    ):
        errors.append("run.rule_commit must be a full 40-character lowercase commit SHA")
    if not isinstance(run.get("synthetic"), bool):
        errors.append("run.synthetic must be a boolean")
    if not _nonempty_strings(run.get("profiles")):
        errors.append("run.profiles must be a non-empty unique string list")
    if run.get("synthetic") is True and (
        not isinstance(run.get("notice"), str) or "kein Nachweis" not in run["notice"]
    ):
        errors.append("synthetic runs must state that they are not suitability evidence")
    results = document.get("results")
    if not isinstance(results, list) or not results:
        errors.append("results document must contain a non-empty results list")
    return errors


def evaluate(
    profile_document: dict[str, Any],
    catalog: dict[str, Any],
    results_document: dict[str, Any],
    selected_profiles: list[str],
) -> dict[str, Any]:
    case_profiles = resolve_case_profiles(profile_document, selected_profiles)
    selected_cases = {
        case["id"]: case
        for case in catalog["cases"]
        if case["profile"] in case_profiles
    }
    failures: list[dict[str, str]] = []
    run_profiles = set(results_document["run"]["profiles"])
    missing_run_profiles = set(selected_profiles) - run_profiles
    if missing_run_profiles:
        failures.append(
            {
                "case_id": "run",
                "reason": f"run does not declare selected profiles {sorted(missing_run_profiles)}",
            }
        )

    indexed_results: dict[str, dict[str, Any]] = {}
    for index, result in enumerate(results_document["results"]):
        if not isinstance(result, dict):
            failures.append({"case_id": f"result[{index}]", "reason": "result must be an object"})
            continue
        case_id = result.get("case_id")
        if not isinstance(case_id, str):
            failures.append({"case_id": f"result[{index}]", "reason": "case_id is missing"})
            continue
        if case_id in indexed_results:
            failures.append({"case_id": case_id, "reason": "duplicate result"})
            continue
        if case_id not in {case["id"] for case in catalog["cases"]}:
            failures.append({"case_id": case_id, "reason": "unknown case"})
            continue
        indexed_results[case_id] = result

    for case_id, case in selected_cases.items():
        result = indexed_results.get(case_id)
        if result is None:
            failures.append({"case_id": case_id, "reason": "missing result"})
            continue
        if result.get("observed_outcome") != case["expected_outcome"]:
            failures.append(
                {
                    "case_id": case_id,
                    "reason": (
                        f"expected outcome {case['expected_outcome']!r}, got "
                        f"{result.get('observed_outcome')!r}"
                    ),
                }
            )
        controls = result.get("observed_controls")
        if not isinstance(controls, list) or not all(isinstance(item, str) for item in controls):
            failures.append({"case_id": case_id, "reason": "observed_controls must be a string list"})
        else:
            missing_controls = set(case["required_controls"]) - set(controls)
            if missing_controls:
                failures.append(
                    {
                        "case_id": case_id,
                        "reason": f"missing controls {sorted(missing_controls)}",
                    }
                )
        evidence = result.get("evidence")
        if not isinstance(evidence, dict):
            failures.append({"case_id": case_id, "reason": "evidence must be an object"})
        else:
            for requirement in case["evidence_requirements"]:
                value = evidence.get(requirement)
                if not isinstance(value, str) or not value.strip():
                    failures.append(
                        {
                            "case_id": case_id,
                            "reason": f"missing evidence {requirement!r}",
                        }
                    )

    synthetic = results_document["run"]["synthetic"]
    return {
        "schema_version": "1.0",
        "status": "passed" if not failures else "failed",
        "run_id": results_document["run"]["run_id"],
        "synthetic": synthetic,
        "selected_profiles": selected_profiles,
        "case_profiles": sorted(case_profiles),
        "selected_case_count": len(selected_cases),
        "passed_case_count": len(selected_cases)
        - len({failure["case_id"] for failure in failures if failure["case_id"] in selected_cases}),
        "failures": failures,
        "qualification": (
            "synthetic structure and oracle check; not evidence of real harness or project suitability"
            if synthetic
            else "result comparison only; project suitability still requires the documented harness workflow"
        ),
    }


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profiles", type=Path, default=root / "evals/profiles.json")
    parser.add_argument("--catalog", type=Path, default=root / "evals/cases.json")
    parser.add_argument("--results", type=Path, required=True)
    parser.add_argument(
        "--profile",
        action="append",
        dest="selected_profiles",
        help="Profile to evaluate; repeat for multiple specializations (default: general)",
    )
    parser.add_argument("--report", type=Path, help="Optional path for the JSON report")
    args = parser.parse_args()

    try:
        profile_document = load_json(args.profiles)
        catalog = load_json(args.catalog)
        results_document = load_json(args.results)
    except (OSError, json.JSONDecodeError) as error:
        print(json.dumps({"status": "invalid", "errors": [str(error)]}, indent=2), file=sys.stderr)
        return 2

    errors = validate_profiles(profile_document)
    if not errors:
        errors.extend(validate_catalog(catalog, profile_document))
    errors.extend(validate_results_document(results_document))
    selected_profiles = args.selected_profiles or ["general"]
    known_profiles = profile_document.get("profiles", {}) if isinstance(profile_document, dict) else {}
    for profile in selected_profiles:
        if profile not in known_profiles:
            errors.append(f"unknown selected profile {profile!r}")
    if errors:
        report = {"schema_version": "1.0", "status": "invalid", "errors": sorted(set(errors))}
        rendered = json.dumps(report, indent=2, sort_keys=True)
        print(rendered, file=sys.stderr)
        if args.report:
            args.report.write_text(rendered + "\n", encoding="utf-8")
        return 2

    report = evaluate(
        profile_document,
        catalog,
        results_document,
        selected_profiles,
    )
    rendered = json.dumps(report, indent=2, sort_keys=True)
    print(rendered)
    if args.report:
        args.report.write_text(rendered + "\n", encoding="utf-8")
    return 0 if report["status"] == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
