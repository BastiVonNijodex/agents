from __future__ import annotations

import copy
import sys
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPOSITORY_ROOT / "scripts"))

from evaluate_harness import (  # noqa: E402
    evaluate,
    load_json,
    resolve_case_profiles,
    validate_catalog,
    validate_profiles,
    validate_results_document,
)


class HarnessEvaluationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.profiles = load_json(REPOSITORY_ROOT / "evals/profiles.json")
        cls.catalog = load_json(REPOSITORY_ROOT / "evals/cases.json")
        cls.reference = load_json(REPOSITORY_ROOT / "evals/reference-results.json")

    def test_current_catalogs_are_valid(self) -> None:
        self.assertEqual([], validate_profiles(self.profiles))
        self.assertEqual([], validate_catalog(self.catalog, self.profiles))
        self.assertEqual([], validate_results_document(self.reference))

    def test_specializations_include_general_baseline(self) -> None:
        self.assertEqual(
            {"general", "coding", "production"},
            resolve_case_profiles(self.profiles, ["coding", "production"]),
        )

    def test_reference_run_passes_all_profiles(self) -> None:
        report = evaluate(
            self.profiles,
            self.catalog,
            self.reference,
            ["general", "coding", "production"],
        )

        self.assertEqual("passed", report["status"])
        self.assertEqual(19, report["selected_case_count"])
        self.assertEqual(19, report["passed_case_count"])
        self.assertTrue(report["synthetic"])
        self.assertIn("not evidence", report["qualification"])

    def test_wrong_outcome_fails(self) -> None:
        results = copy.deepcopy(self.reference)
        results["results"][0]["observed_outcome"] = "deny"

        report = evaluate(self.profiles, self.catalog, results, ["general"])

        self.assertEqual("failed", report["status"])
        self.assertTrue(any("expected outcome" in item["reason"] for item in report["failures"]))

    def test_missing_control_and_evidence_fail(self) -> None:
        results = copy.deepcopy(self.reference)
        results["results"][0]["observed_controls"] = []
        results["results"][0]["evidence"].pop("scope_record")

        report = evaluate(self.profiles, self.catalog, results, ["general"])

        reasons = [item["reason"] for item in report["failures"]]
        self.assertTrue(any("missing controls" in reason for reason in reasons))
        self.assertIn("missing evidence 'scope_record'", reasons)

    def test_duplicate_case_id_is_invalid(self) -> None:
        catalog = copy.deepcopy(self.catalog)
        catalog["cases"].append(copy.deepcopy(catalog["cases"][0]))

        errors = validate_catalog(catalog, self.profiles)

        self.assertTrue(any("duplicate id" in error for error in errors))

    def test_synthetic_run_requires_suitability_notice(self) -> None:
        results = copy.deepcopy(self.reference)
        results["run"].pop("notice")

        errors = validate_results_document(results)

        self.assertTrue(any("not suitability evidence" in error for error in errors))

    def test_each_case_profile_has_positive_negative_and_error_paths(self) -> None:
        paths_by_profile: dict[str, set[str]] = {}
        for case in self.catalog["cases"]:
            paths_by_profile.setdefault(case["profile"], set()).add(case["path"])

        self.assertEqual(
            {
                "general": {"positive", "negative", "error"},
                "coding": {"positive", "negative", "error"},
                "production": {"positive", "negative", "error"},
            },
            paths_by_profile,
        )


if __name__ == "__main__":
    unittest.main()
