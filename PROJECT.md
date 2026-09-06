# PROJECT.md

## Zweck

Dieses Repository veröffentlicht zentrale Agenten-Anweisungen von BastiVonNijodex über GitHub Pages.

## Versionsbasis

Die veröffentlichten Quelldateien liegen unter `docs/`. GitHub Pages stellt sie aus dem Branch `main` und dem Ordner `/docs` bereit.

Die zentrale Einstiegsdatei ist:

https://bastivonnijodex.github.io/agents/AGENTS.md

Die deklarierte nächste Regelversion steht in `docs/VERSION.md`. Releases
verwenden SemVer, einen annotierten Git-Tag `v<major>.<minor>.<patch>`, einen
GitHub Release und den vollständigen Commit-SHA. Der Entwicklungsstand auf
`main` gilt bis zum zugehörigen Release nicht als veröffentlichter
SemVer-Regelstand und wird durch seinen Commit-SHA identifiziert.

Die Versions-, Kompatibilitäts- und Migrationsregeln stehen in
`docs/VERSIONING.md`; die Release-Historie steht in `docs/CHANGELOG.md`.

## Lokaler Projektpfad

Der stabile App- beziehungsweise Repository-Name ist `agents`.

Der kanonische lokale Basis-Checkout liegt unter:

`/Users/bastimeissner/vibecoding/agents`

[MUST] Zusätzliche Worktrees oder bestehende Arbeitskopien an anderen Orten
dürfen für isolierte Tasks verwendet werden, ersetzen den kanonischen
Basis-Checkout aber nicht.

[MUST] Vor einer zustandsverändernden Arbeit muss die verwendete Arbeitskopie
dem Repository `BastiVonNijodex/agents` eindeutig zugeordnet und ihr Git-Stand
geprüft werden.

## Fachliche Leitplanken

[MUST] Die Markdown-Dateien unter `docs/` bilden die fachliche Single Source of Truth für konsumierende Agenten und Projekt-Repositories.

[MUST] Repository-lokale Einstiegspunkte wie `AGENTS.md` dürfen auf die veröffentlichten globalen Regeln verweisen, müssen dabei aber einen funktionsfähigen Abrufweg für Agenten beschreiben.

[MUST] Projektspezifische Regeln für einzelne Softwareprojekte gehören in deren eigene `PROJECT.md`, nicht in dieses globale Regel-Repository.

[MUST_NOT] Fremde, organisationsspezifische Regeln dürfen nicht ungeprüft übernommen werden.

## Technische Leitplanken

[MUST] Änderungen an veröffentlichten Regeln müssen direkt in den Markdown-Dateien unter `docs/` erfolgen.

[MUST_NOT] Es darf kein separater Build- oder Generierungsschritt vorausgesetzt werden, solange GitHub Pages die versionierten Dateien unter `docs/` direkt verteilt.

[MUST] Jede Markdown-Datei unter `docs/` muss für konsumierende Agenten bestimmt, über GitHub Pages abrufbar und ausgehend von `docs/AGENTS.md` oder einer Lookup-Datei erreichbar sein.

## Projektadapter für Agenten-Harnesses

### Einsatz und wirksamer Stand

In diesem Repository arbeiten lokale Coding-Agenten an den öffentlichen
Agentenregeln, Vorlagen und den zugehörigen Repository-Prüfungen. Der für einen
Task wirksame Stand wird mindestens durch Repository, Branch oder Worktree,
Commit-SHA, führendes Issue und aktuelle Nutzeranweisung identifiziert.

[MUST] Führende Quellen sind in dieser Reihenfolge die aktuelle
Nutzeranweisung, diese `PROJECT.md`, die veröffentlichte `docs/AGENTS.md`, die
für den Task aktivierten Rollen und Workflows sowie der belegte
Repository-Stand.

[MUST] Vor Änderungen müssen Arbeitsstand, Branch, betroffene Regeln,
verwandte Issues und die Auswirkung auf konsumierende Projekte geprüft werden.

[MUST] Coding-Arbeit in diesem Repository ist eine risikoreiche
Spezialisierung. Ein Merge nach `main` veröffentlicht Änderungen unter den
GitHub-Pages-URLs und ist deshalb zusätzlich eine extern wirksame
Produktionshandlung für das Regelwerk.

### Werkzeuge, Berechtigungen und Freigaben

[ALLOW] Agenten dürfen Repository-Dateien, Git-Historie, öffentliche
GitHub-Metadaten und die veröffentlichten GitHub-Pages-Dokumente lesen sowie
risikoarme lokale Prüfungen ausführen.

[ALLOW_IF] Innerhalb eines bestätigten Umsetzungsscopes dürfen Agenten in
einem eigenen Branch oder Worktree Dateien ändern, synthetische Test-Fixtures
erzeugen und die in diesem Dokument genannten Checks ausführen.

[MUST_IF] Issues, Branches, Commits, Pushes, Pull Requests, Reviews oder Merges
erstellt beziehungsweise verändert werden, müssen diese extern wirksamen
Schritte durch den Nutzerauftrag oder ein dokumentiertes Autopilot-Paket
gedeckt sein.

[MUST_NOT] Agenten dürfen ohne ausdrückliche Release-Freigabe keine Tags oder
GitHub Releases erzeugen und keine Branchschutz-, Pages-, Repository-,
Organisations- oder Secret-Einstellungen verändern.

[MUST_NOT] Für reguläre Arbeit an diesem Repository dürfen keine Secrets,
privaten Schlüssel, produktiven Zugangsdaten oder personenbezogenen Testdaten
gelesen, erzeugt oder benötigt werden.

### Zustand, Memory, Delegation und Nachweise

[MUST] Persistenter Agentenkontext und frühere Chats sind keine führende
Quelle. Relevante Aussagen daraus müssen vor einer Handlung gegen Repository,
Issue, Pull Request oder aktuelle Nutzeranweisung geprüft werden.

[MUST_NOT] Secrets, Zugangsdaten oder private Schlüssel dürfen in keinem
agentengeführten Memory, Test-Fixture oder Arbeitsnachweis gespeichert werden.

[MUST_IF] Arbeit delegiert wird, müssen Teilziel, Scope, führende Quellen,
erlaubte Handlungen, Stop-Bedingungen und erwarteter Nachweis übertragen
werden. Erforderliche unabhängige Reviews dürfen nicht durch die
Implementierungsinstanz ersetzt werden.

[MUST] Issues, Pull Requests, Commits und CI-Ergebnisse bilden den dauerhaften
Arbeitsnachweis. Sie enthalten im erforderlichen Umfang Scope, Entscheidungen,
Änderungen, Checks, Findings und offene Punkte, aber keine sensiblen Werte.

### Kontrollen, Evals und sicheres Stoppen

[MUST] Änderungen müssen den lokalen Repository-Validator und dessen Tests
bestehen. Regeländerungen werden zusätzlich inhaltlich gegen betroffene Rollen,
Workflows, Vorlagen und konsumierende Projektadapter geprüft.

[MUST] Der Validator erzwingt nur strukturelle Kontrollen. Eine vollständige
semantische Harness-Eval-Suite ist noch nicht vorhanden und wird in GitHub
Issue #16 nachgeführt; bis dahin bleibt die inhaltliche Prüfung eine
dokumentierte Review-Kontrolle.

[MUST] Ein Agent stoppt vor der betroffenen Handlung bei unklarem Scope,
widersprüchlichem Regelstand, fremden nicht sicher abgrenzbaren Änderungen,
fehlender Freigabe, ausgefallenem Pflichtcheck oder einem nicht auflösbaren
hohen beziehungsweise kritischen Finding.

[MUST_IF] Freigabelogik, Regelmarker, Berechtigungen, Memory, Delegation,
Nachweise, Stop-Bedingungen oder Publikationswege wesentlich geändert werden,
müssen Harness-Auswirkung, Kompatibilität und relevante Regressionen erneut
bewertet werden.

[MUST] Jeder Task belegt den verwendeten Regelstand durch Commit-SHA und, wenn
vorhanden, veröffentlichte SemVer-Version. Sicherheitsrelevante Änderungen
werden als eigenes Issue und Pull Request geprüft, im Changelog hervorgehoben
und kontrolliert in konsumierende Projekte übernommen.

## Checks

Vor einem Commit oder Pull Request müssen mindestens folgende Befehle
erfolgreich laufen:

```sh
python3 scripts/validate_repository.py
python3 -m unittest discover -s tests -v
git diff --check
```

[MUST_IF] Ein Check nicht ausgeführt werden kann, müssen Grund, Auswirkung und
verbleibendes Risiko im Pull Request dokumentiert werden.

## Review, Merge und Veröffentlichung

[MUST] Änderungen erfolgen über einen fachlich benannten Branch oder Worktree
und einen Pull Request mit Bezug auf das führende Issue.

[MUST] Vor dem Merge müssen die erforderlichen lokalen Checks und GitHub-CI
erfolgreich sein, Review-Befunde aufgelöst und Dokumentationsauswirkungen
berücksichtigt werden.

[MUST_IF] Eine Änderung Sicherheits-, Datenschutz-, Berechtigungs-,
Freigabe- oder andere Schutzkontrollen betrifft, muss die Rolle Security
Reviewer nach ihren Aktivierungs- und Unabhängigkeitsregeln angewendet werden.

[MUST] Nach einem Merge mit Änderungen unter `docs/` müssen die betroffenen
GitHub-Pages-URLs auf Erreichbarkeit und den erwarteten Inhalt geprüft werden.
Ein fehlerhafter Pages-Stand wird nicht als erfolgreiche Veröffentlichung
gemeldet.

[MUST] Ein fehlgeschlagener Merge oder eine fehlerhafte Veröffentlichung wird
durch Abbruch weiterer Veröffentlichungsschritte und einen nachvollziehbaren
Revert-Pull-Request oder eine korrigierende Änderung auf Basis des belegten
letzten funktionierenden Commits behandelt. Direkte destruktive Git-Befehle
sind kein Rollback-Weg.

## Übergabe und Wiederaufnahme

[MUST_IF] Die Arbeit in einem anderen Task, Agenten, Worktree oder Rechner
fortgesetzt wird, enthält die führende Übergabe mindestens Issue, Scope,
Freigabestufe, Repository, Branch oder Worktree, Commit-SHA, Änderungen,
Checks, offene Findings, Stop-Bedingungen und nächsten empfohlenen Schritt.

## Definition of Done

Ein Arbeitspaket ist abgeschlossen, wenn Scope und Akzeptanzkriterien erfüllt,
Validator, Tests und Diff-Check erfolgreich, erforderliche Reviews beendet,
Dokumentation aktualisiert, verbleibende Arbeit als Issue erfasst und alle
freigegebenen externen Schritte wahrheitsgemäß nachgewiesen sind.

## Online-Publikation prüfen

[SHOULD] Nach Änderungen an `docs/` soll geprüft werden, ob GitHub Pages die zentralen Dateien ausliefert.

Wichtige URLs:

- https://bastivonnijodex.github.io/agents/AGENTS.md
- https://bastivonnijodex.github.io/agents/roles/ROLES.md
- https://bastivonnijodex.github.io/agents/roles/product-owner.md
- https://bastivonnijodex.github.io/agents/roles/security-reviewer.md
- https://bastivonnijodex.github.io/agents/skills/SKILLS.md
- https://bastivonnijodex.github.io/agents/workflows/WORKFLOWS.md
- https://bastivonnijodex.github.io/agents/workflows/agent-harness.md
- https://bastivonnijodex.github.io/agents/workflows/autopilot.md
- https://bastivonnijodex.github.io/agents/workflows/backlog-item.md
- https://bastivonnijodex.github.io/agents/workflows/product-concept.md
- https://bastivonnijodex.github.io/agents/workflows/new-application.md
- https://bastivonnijodex.github.io/agents/workflows/release.md
