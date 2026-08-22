# agents

Zentrale Agenten-Anweisungen für Repositories von BastiVonNijodex.

Dieses Repository ist ein GitHub-Pages-Projekt. Die veröffentlichten Markdown-Dateien liegen unter `docs/` und werden direkt aus dem Branch `main` bereitgestellt.

## GitHub Pages

Die zentrale Datei ist:

[AGENTS.md](https://bastivonnijodex.github.io/agents/AGENTS.md)

Weitere Einstiegspunkte:

- [ROLES.md](https://bastivonnijodex.github.io/agents/roles/ROLES.md)
- [SKILLS.md](https://bastivonnijodex.github.io/agents/skills/SKILLS.md)
- [WORKFLOWS.md](https://bastivonnijodex.github.io/agents/workflows/WORKFLOWS.md)
- [release.md](https://bastivonnijodex.github.io/agents/workflows/release.md)
- [COMMANDS.md](https://bastivonnijodex.github.io/agents/COMMANDS.md)
- [TECHNOLOGIES.md](https://bastivonnijodex.github.io/agents/TECHNOLOGIES.md)

## Verwendung in einem Repository

Lege im Ziel-Repository eine kurze lokale `AGENTS.md` an. Eine Vorlage liegt unter:

`templates/AGENTS.md`

Optional kann das Ziel-Repository zusätzlich eine `PROJECT.md` mit projektspezifischen Leitplanken enthalten:

`templates/PROJECT.md`

## Struktur

| Pfad | Zweck |
|---|---|
| `AGENTS.md` | Lokaler Einstiegspunkt dieses Repositories. |
| `PROJECT.md` | Projektbeschreibung und Pflege-Regeln für dieses Regel-Repository. |
| `docs/AGENTS.md` | Veröffentlichte globale Agentenregeln. |
| `docs/roles/ROLES.md` | Rollen-Lookup. |
| `docs/skills/SKILLS.md` | Skill-Lookup. |
| `docs/workflows/WORKFLOWS.md` | Workflow-Lookup. |
| `docs/workflows/release.md` | Globale Release-Disziplin. |
| `templates/` | Kopiervorlagen für andere Repositories. |

## Pflege

Änderungen an veröffentlichten Regeln erfolgen direkt unter `docs/`.

Änderungen sollten klein, nachvollziehbar und versioniert erfolgen, weil konsumierende Repositories auf die veröffentlichten URLs verweisen können.
