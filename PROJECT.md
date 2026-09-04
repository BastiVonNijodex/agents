# PROJECT.md

## Zweck

Dieses Repository veröffentlicht zentrale Agenten-Anweisungen von BastiVonNijodex über GitHub Pages.

## Versionsbasis

Die veröffentlichten Quelldateien liegen unter `docs/`. GitHub Pages stellt sie aus dem Branch `main` und dem Ordner `/docs` bereit.

Die zentrale Einstiegsdatei ist:

https://bastivonnijodex.github.io/agents/AGENTS.md

## Fachliche Leitplanken

[MUST] Die Markdown-Dateien unter `docs/` bilden die fachliche Single Source of Truth für konsumierende Agenten und Projekt-Repositories.

[MUST] Repository-lokale Einstiegspunkte wie `AGENTS.md` dürfen auf die veröffentlichten globalen Regeln verweisen, müssen dabei aber einen funktionsfähigen Abrufweg für Agenten beschreiben.

[MUST] Projektspezifische Regeln für einzelne Softwareprojekte gehören in deren eigene `PROJECT.md`, nicht in dieses globale Regel-Repository.

[MUST_NOT] Fremde, organisationsspezifische Regeln dürfen nicht ungeprüft übernommen werden.

## Technische Leitplanken

[MUST] Änderungen an veröffentlichten Regeln müssen direkt in den Markdown-Dateien unter `docs/` erfolgen.

[MUST_NOT] Es darf kein separater Build- oder Generierungsschritt vorausgesetzt werden, solange GitHub Pages die versionierten Dateien unter `docs/` direkt verteilt.

[MUST] Jede Markdown-Datei unter `docs/` muss für konsumierende Agenten bestimmt, über GitHub Pages abrufbar und ausgehend von `docs/AGENTS.md` oder einer Lookup-Datei erreichbar sein.

## Online-Publikation prüfen

[SHOULD] Nach Änderungen an `docs/` soll geprüft werden, ob GitHub Pages die zentralen Dateien ausliefert.

Wichtige URLs:

- https://bastivonnijodex.github.io/agents/AGENTS.md
- https://bastivonnijodex.github.io/agents/roles/ROLES.md
- https://bastivonnijodex.github.io/agents/roles/product-owner.md
- https://bastivonnijodex.github.io/agents/roles/security-reviewer.md
- https://bastivonnijodex.github.io/agents/skills/SKILLS.md
- https://bastivonnijodex.github.io/agents/workflows/WORKFLOWS.md
- https://bastivonnijodex.github.io/agents/workflows/autopilot.md
- https://bastivonnijodex.github.io/agents/workflows/backlog-item.md
- https://bastivonnijodex.github.io/agents/workflows/product-concept.md
- https://bastivonnijodex.github.io/agents/workflows/new-application.md
- https://bastivonnijodex.github.io/agents/workflows/release.md
