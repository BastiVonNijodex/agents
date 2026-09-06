from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPOSITORY_ROOT / "scripts"))

from validate_repository import (  # noqa: E402
    validate_declared_version,
    validate_links,
    validate_markers,
    validate_pinned_rule_reference,
    validate_reachability,
    validate_repository,
    validate_templates,
)


class RepositoryValidatorTests(unittest.TestCase):
    def test_current_repository_is_valid(self) -> None:
        self.assertEqual([], validate_repository(REPOSITORY_ROOT))

    def test_unknown_rule_marker_fails(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            document = root / "rule.md"
            document.write_text("[REQUIRED] Unbekannter Marker.\n", encoding="utf-8")

            errors = validate_markers(root, [document])

            self.assertTrue(any("[REQUIRED]" in error for error in errors))

    def test_broken_internal_link_fails(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            document = root / "README.md"
            document.write_text("[Fehlt](missing.md)\n", encoding="utf-8")

            errors = validate_links(root, [document])

            self.assertTrue(any("ungültiges internes Linkziel" in error for error in errors))

    def test_unreachable_document_fails(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            docs = root / "docs"
            docs.mkdir()
            (docs / "AGENTS.md").write_text("# Einstieg\n", encoding="utf-8")
            (docs / "orphan.md").write_text("# Nicht verlinkt\n", encoding="utf-8")

            errors = validate_reachability(root)

            self.assertTrue(any("orphan.md" in error for error in errors))

    def test_project_template_requires_canonical_app_path(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            templates = root / "templates"
            templates.mkdir()
            (templates / "PROJECT.md").write_text(
                "## Lokaler Projektpfad\n\nApp-Name: `<appname>`\n",
                encoding="utf-8",
            )

            errors = validate_templates(root)

            self.assertTrue(
                any("/Users/bastimeissner/vibecoding/<appname>" in error for error in errors)
            )

    def test_synthetic_project_migrates_to_pinned_rule_reference(self) -> None:
        template = (REPOSITORY_ROOT / "templates/PROJECT.md").read_text(encoding="utf-8")
        commit = "a" * 40
        migrated = (
            template.replace("<regelversion>", "v1.0.0")
            .replace("<regel-commit-sha>", commit)
            .replace(
                "<regel-update-modus>",
                "monatliche Prüfung mit Kompatibilitätsreview und SECURITY-Bewertung",
            )
        )

        self.assertEqual([], validate_pinned_rule_reference(migrated, "synthetic/PROJECT.md"))

    def test_mismatched_immutable_rule_url_fails(self) -> None:
        commit = "a" * 40
        other_commit = "b" * 40
        project = (
            "Regelversion: `v1.0.0`\n"
            f"Regel-Commit: `{commit}`\n"
            "Unveränderliche Regelquelle: "
            f"`https://raw.githubusercontent.com/BastiVonNijodex/agents/{other_commit}/docs/AGENTS.md`\n"
            "Update-Modus: `monatliche Prüfung und SECURITY-Bewertung`\n"
        )

        errors = validate_pinned_rule_reference(project)

        self.assertTrue(any("passt nicht" in error for error in errors))

    def test_invalid_declared_semver_fails(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            docs = root / "docs"
            docs.mkdir()
            (docs / "VERSION.md").write_text(
                "Deklarierte Version: `Version eins`\n",
                encoding="utf-8",
            )
            (docs / "CHANGELOG.md").write_text(
                "## Version eins\n",
                encoding="utf-8",
            )

            errors = validate_declared_version(root)

            self.assertTrue(any("ungültige SemVer-Version" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
