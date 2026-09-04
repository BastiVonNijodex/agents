# agents

Zentrale Agenten-Anweisungen für Repositories von BastiVonNijodex.

Dieses Repository ist ein GitHub-Pages-Projekt. Die veröffentlichten Markdown-Dateien liegen unter `docs/` und werden direkt aus dem Branch `main` bereitgestellt.

## GitHub Pages

Die zentrale Datei ist:

[AGENTS.md](https://bastivonnijodex.github.io/agents/AGENTS.md)

Weitere Einstiegspunkte:

- [ROLES.md](https://bastivonnijodex.github.io/agents/roles/ROLES.md)
- [Product Owner](https://bastivonnijodex.github.io/agents/roles/product-owner.md)
- [Security Reviewer](https://bastivonnijodex.github.io/agents/roles/security-reviewer.md)
- [SKILLS.md](https://bastivonnijodex.github.io/agents/skills/SKILLS.md)
- [WORKFLOWS.md](https://bastivonnijodex.github.io/agents/workflows/WORKFLOWS.md)
- [Autopilot mit gebündelter Freigabe](https://bastivonnijodex.github.io/agents/workflows/autopilot.md)
- [Backlog Item erstellen und verfeinern](https://bastivonnijodex.github.io/agents/workflows/backlog-item.md)
- [Produktkonzept erstellen und entscheiden](https://bastivonnijodex.github.io/agents/workflows/product-concept.md)
- [new-application.md](https://bastivonnijodex.github.io/agents/workflows/new-application.md)
- [release.md](https://bastivonnijodex.github.io/agents/workflows/release.md)
- [COMMANDS.md](https://bastivonnijodex.github.io/agents/COMMANDS.md)
- [TECHNOLOGIES.md](https://bastivonnijodex.github.io/agents/TECHNOLOGIES.md)

## Verwendung in einem Repository

Lege im Ziel-Repository eine kurze lokale `AGENTS.md` an. Eine Vorlage liegt unter:

`templates/AGENTS.md`

Ein Ziel-Repository kann zusätzlich eine `PROJECT.md` mit projektspezifischen
Leitplanken enthalten. Für neue Applikationen ist sie nach dem Workflow
[Neue Applikation erstellen](https://bastivonnijodex.github.io/agents/workflows/new-application.md)
verpflichtend:

`templates/PROJECT.md`

## Struktur

| Pfad | Zweck |
|---|---|
| `AGENTS.md` | Lokaler Einstiegspunkt dieses Repositories. |
| `PROJECT.md` | Projektbeschreibung und Pflege-Regeln für dieses Regel-Repository. |
| `docs/AGENTS.md` | Veröffentlichte globale Agentenregeln. |
| `docs/roles/ROLES.md` | Rollen-Lookup. |
| `docs/roles/product-owner.md` | Produktübergreifende Product-Owner-Verantwortung. |
| `docs/roles/security-reviewer.md` | Unabhängige adversariale Prüfung sicherheitsrelevanter Änderungen. |
| `docs/skills/SKILLS.md` | Skill-Lookup. |
| `docs/workflows/WORKFLOWS.md` | Workflow-Lookup. |
| `docs/workflows/autopilot.md` | Gebündelte Umsetzungs- und Produktionsfreigaben mit klaren Stop-Bedingungen. |
| `docs/workflows/backlog-item.md` | Produktübergreifender Standard für Backlog Items. |
| `docs/workflows/product-concept.md` | Produktübergreifender Lebenszyklus für Produktkonzepte. |
| `docs/workflows/new-application.md` | Mindeststandard für neue Applikationen. |
| `docs/workflows/release.md` | Globale Release-Disziplin. |
| `templates/` | Kopiervorlagen für andere Repositories. |

## Pflege

Änderungen an veröffentlichten Regeln erfolgen direkt unter `docs/`.

Änderungen sollten klein, nachvollziehbar und versioniert erfolgen, weil konsumierende Repositories auf die veröffentlichten URLs verweisen können.
