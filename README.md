# agents

Zentrale Agenten-Anweisungen für Repositories von BastiVonNijodex.

Dieses Repository ist ein GitHub-Pages-Projekt. Die veröffentlichten Markdown-Dateien liegen unter `docs/` und werden direkt aus dem Branch `main` bereitgestellt.

## GitHub Pages

Die zentrale Datei ist:

[AGENTS.md](https://bastivonnijodex.github.io/agents/AGENTS.md)

Weitere Einstiegspunkte:

- [Aktuelle Regelversion](https://bastivonnijodex.github.io/agents/VERSION.md)
- [Versionierung und Migration](https://bastivonnijodex.github.io/agents/VERSIONING.md)
- [Changelog](https://bastivonnijodex.github.io/agents/CHANGELOG.md)
- [Harness-Evals](https://bastivonnijodex.github.io/agents/EVALS.md)
- [ROLES.md](https://bastivonnijodex.github.io/agents/roles/ROLES.md)
- [Product Owner](https://bastivonnijodex.github.io/agents/roles/product-owner.md)
- [Security Reviewer](https://bastivonnijodex.github.io/agents/roles/security-reviewer.md)
- [SKILLS.md](https://bastivonnijodex.github.io/agents/skills/SKILLS.md)
- [WORKFLOWS.md](https://bastivonnijodex.github.io/agents/workflows/WORKFLOWS.md)
- [Agenten-Harness bewerten und projektbezogen ausgestalten](https://bastivonnijodex.github.io/agents/workflows/agent-harness.md)
- [Autopilot mit gebündelter Freigabe](https://bastivonnijodex.github.io/agents/workflows/autopilot.md)
- [Backlog Item erstellen und verfeinern](https://bastivonnijodex.github.io/agents/workflows/backlog-item.md)
- [Produktkonzept erstellen und entscheiden](https://bastivonnijodex.github.io/agents/workflows/product-concept.md)
- [new-application.md](https://bastivonnijodex.github.io/agents/workflows/new-application.md)
- [release.md](https://bastivonnijodex.github.io/agents/workflows/release.md)
- [COMMANDS.md](https://bastivonnijodex.github.io/agents/COMMANDS.md)
- [TECHNOLOGIES.md](https://bastivonnijodex.github.io/agents/TECHNOLOGIES.md)

## Verwendung in einem Repository

Jedes App-Projekt besitzt einen kanonischen lokalen Basisordner unter
`/Users/bastimeissner/vibecoding/<appname>`. Zusätzliche Worktrees dürfen
anderswo liegen, solange der Basis-Checkout erhalten bleibt.

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
| `docs/VERSION.md` | Deklarierte nächste beziehungsweise aktuelle Regelversion. |
| `docs/VERSIONING.md` | SemVer-, Referenz-, Kompatibilitäts- und Migrationsmodell. |
| `docs/CHANGELOG.md` | Release-Kandidaten, veröffentlichte Regelstände und Migrationshinweise. |
| `docs/EVALS.md` | Wiederverwendbare Harness-Evals und gemeinsames Ergebnisformat. |
| `docs/roles/ROLES.md` | Rollen-Lookup. |
| `docs/roles/product-owner.md` | Produktübergreifende Product-Owner-Verantwortung. |
| `docs/roles/security-reviewer.md` | Unabhängige adversariale Prüfung sicherheitsrelevanter Änderungen. |
| `docs/skills/SKILLS.md` | Skill-Lookup. |
| `docs/workflows/WORKFLOWS.md` | Workflow-Lookup. |
| `docs/workflows/agent-harness.md` | Allgemeiner Standard zur Bewertung und projektspezifischen Ausgestaltung von Agenten-Harnesses. |
| `docs/workflows/autopilot.md` | Gebündelte Umsetzungs- und Produktionsfreigaben mit klaren Stop-Bedingungen. |
| `docs/workflows/backlog-item.md` | Produktübergreifender Standard für Backlog Items. |
| `docs/workflows/product-concept.md` | Produktübergreifender Lebenszyklus für Produktkonzepte. |
| `docs/workflows/new-application.md` | Mindeststandard für neue Applikationen. |
| `docs/workflows/release.md` | Globale Release-Disziplin. |
| `evals/` | Maschinenlesbare Profile, Fälle und synthetische Referenzergebnisse. |
| `scripts/evaluate_harness.py` | Deterministischer Harness-Eval-Runner. |
| `templates/` | Kopiervorlagen für andere Repositories. |

## Pflege

Änderungen an veröffentlichten Regeln erfolgen direkt unter `docs/`.

Änderungen sollten klein, nachvollziehbar und versioniert erfolgen, weil konsumierende Repositories auf die veröffentlichten URLs verweisen können.

## Lokale Prüfung

Der Repository-Validator prüft interne Markdown-Ziele, die Erreichbarkeit aller
veröffentlichten Dokumente, Regelmarker und zentrale Bestandteile der Vorlagen:

```sh
python3 scripts/validate_repository.py
python3 -m unittest discover -s tests -v
python3 scripts/evaluate_harness.py --results evals/reference-results.json --profile general --profile coding --profile production
git diff --check
```

Eine ausgefüllte Regelreferenz in einem konsumierenden Projekt kann zusätzlich
geprüft werden:

```sh
python3 scripts/validate_repository.py --project-reference /pfad/zur/PROJECT.md
```

Der synthetische Referenzlauf prueft Struktur und Oracle-Vergleich, aber nicht
die Eignung eines realen Harnesses. Die inhaltliche Bewertung von Kontrollen,
Evidenz und Regelwirkungen bleibt zusätzlich erforderlich.
