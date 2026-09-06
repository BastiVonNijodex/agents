from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPOSITORY_ROOT / "scripts"))

from validate_repository import (  # noqa: E402
    validate_links,
    validate_markers,
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


if __name__ == "__main__":
    unittest.main()
