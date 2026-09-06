#!/usr/bin/env python3
"""Validate the structural integrity of the agents repository."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


PAGES_BASE = "https://bastivonnijodex.github.io/agents/"
ALLOWED_MARKERS = {
    "MUST",
    "MUST_IF",
    "MUST_NOT",
    "MUST_NOT_IF",
    "ALLOW",
    "ALLOW_IF",
    "SHOULD",
    "OPTIONAL",
    "PRIORITY",
}
REQUIRED_FILES = {
    "AGENTS.md",
    "PROJECT.md",
    "README.md",
    "docs/AGENTS.md",
    "docs/COMMANDS.md",
    "docs/TECHNOLOGIES.md",
    "docs/roles/ROLES.md",
    "docs/skills/SKILLS.md",
    "docs/workflows/WORKFLOWS.md",
    "templates/AGENTS.md",
    "templates/PROJECT.md",
}
REQUIRED_TEMPLATE_HEADINGS = {
    "## Source of Truth",
    "## Projektadapter für Agenten-Harnesses",
    "## Checks",
    "## Release, Deployment und Betrieb",
    "## Übergabe und Wiederaufnahme",
    "## Definition of Done",
    "## Verbotene Aktionen",
}

MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
PAGES_URL_RE = re.compile(re.escape(PAGES_BASE) + r"[^\s)>\"]+")
MARKER_RE = re.compile(r"\[([A-Z][A-Z_]{2,})\]")


def markdown_files(root: Path) -> list[Path]:
    return sorted(
        path
        for path in root.rglob("*.md")
        if ".git" not in path.parts and ".venv" not in path.parts
    )


def link_targets(text: str) -> list[str]:
    targets = [match.group(1).strip().split(maxsplit=1)[0] for match in MARKDOWN_LINK_RE.finditer(text)]
    targets.extend(match.group(0).rstrip(".,;:") for match in PAGES_URL_RE.finditer(text))
    return targets


def internal_target(root: Path, source: Path, target: str) -> Path | None:
    if target.startswith(PAGES_BASE):
        relative = unquote(urlsplit(target).path.removeprefix("/agents/")).lstrip("/")
        return root / "docs" / relative

    parsed = urlsplit(target)
    if parsed.scheme or parsed.netloc or target.startswith("#"):
        return None

    relative = unquote(parsed.path)
    if not relative:
        return None
    return (source.parent / relative).resolve()


def validate_required_files(root: Path) -> list[str]:
    return [f"Fehlende Pflichtdatei: {relative}" for relative in sorted(REQUIRED_FILES) if not (root / relative).is_file()]


def validate_text_quality(root: Path, files: list[Path]) -> list[str]:
    errors: list[str] = []
    for path in files:
        text = path.read_text(encoding="utf-8")
        relative = path.relative_to(root)
        if text and not text.endswith("\n"):
            errors.append(f"{relative}: Datei endet nicht mit einem Zeilenumbruch")
        for line_number, line in enumerate(text.splitlines(), start=1):
            if line.rstrip() != line:
                errors.append(f"{relative}:{line_number}: nachgestellte Leerzeichen")
    return errors


def validate_markers(root: Path, files: list[Path]) -> list[str]:
    errors: list[str] = []
    for path in files:
        text = path.read_text(encoding="utf-8")
        for line_number, line in enumerate(text.splitlines(), start=1):
            for marker in MARKER_RE.findall(line):
                if marker not in ALLOWED_MARKERS:
                    errors.append(
                        f"{path.relative_to(root)}:{line_number}: unbekannter Regelmarker [{marker}]"
                    )
    return errors


def validate_links(root: Path, files: list[Path]) -> list[str]:
    errors: list[str] = []
    for path in files:
        text = path.read_text(encoding="utf-8")
        for target in link_targets(text):
            resolved = internal_target(root, path, target)
            if resolved is None:
                continue
            try:
                resolved.relative_to(root.resolve())
            except ValueError:
                errors.append(f"{path.relative_to(root)}: Link verlässt Repository: {target}")
                continue
            if not resolved.exists():
                errors.append(f"{path.relative_to(root)}: ungültiges internes Linkziel: {target}")
    return errors


def documentation_graph(root: Path) -> dict[Path, set[Path]]:
    docs_root = (root / "docs").resolve()
    graph: dict[Path, set[Path]] = {}
    for path in sorted(docs_root.rglob("*.md")):
        source = path.resolve()
        graph[source] = set()
        for target in link_targets(path.read_text(encoding="utf-8")):
            resolved = internal_target(root, path, target)
            if resolved is None:
                continue
            resolved = resolved.resolve()
            if resolved.suffix == ".md" and resolved.is_relative_to(docs_root):
                graph[source].add(resolved)
    return graph


def validate_reachability(root: Path) -> list[str]:
    entrypoint = (root / "docs/AGENTS.md").resolve()
    if not entrypoint.is_file():
        return []

    graph = documentation_graph(root)
    visited: set[Path] = set()
    pending = [entrypoint]
    while pending:
        current = pending.pop()
        if current in visited:
            continue
        visited.add(current)
        pending.extend(graph.get(current, set()) - visited)

    return [
        f"{path.relative_to(root.resolve())}: nicht von docs/AGENTS.md aus erreichbar"
        for path in sorted(set(graph) - visited)
    ]


def validate_templates(root: Path) -> list[str]:
    errors: list[str] = []
    agents_template = root / "templates/AGENTS.md"
    project_template = root / "templates/PROJECT.md"

    if agents_template.is_file():
        text = agents_template.read_text(encoding="utf-8")
        for required in (PAGES_BASE + "AGENTS.md", "PROJECT.md", "curl -L"):
            if required not in text:
                errors.append(f"templates/AGENTS.md: erforderlicher Inhalt fehlt: {required}")

    if project_template.is_file():
        text = project_template.read_text(encoding="utf-8")
        for heading in sorted(REQUIRED_TEMPLATE_HEADINGS):
            if heading not in text:
                errors.append(f"templates/PROJECT.md: erforderliche Überschrift fehlt: {heading}")
    return errors


def validate_repository(root: Path) -> list[str]:
    root = root.resolve()
    files = markdown_files(root)
    errors: list[str] = []
    errors.extend(validate_required_files(root))
    errors.extend(validate_text_quality(root, files))
    errors.extend(validate_markers(root, files))
    errors.extend(validate_links(root, files))
    errors.extend(validate_reachability(root))
    errors.extend(validate_templates(root))
    return sorted(set(errors))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "root",
        nargs="?",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Repository-Root (Standard: Elternordner dieses Skripts)",
    )
    args = parser.parse_args()
    errors = validate_repository(args.root)
    if errors:
        print("Repository-Validierung fehlgeschlagen:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("Repository-Validierung erfolgreich.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
