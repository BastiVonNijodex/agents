# WORKFLOWS.md

## Zweck

Diese Datei ist die Lookup-Datei für wiederkehrende Workflows. Workflows kombinieren Skills in einer sinnvollen Reihenfolge.

## Verwendung

[MUST] Ein Workflow wird nur verwendet, wenn der aktuelle Task seinem Ziel entspricht.

[MUST_NOT] Workflows dürfen Skill-, Rollen- oder Agentenregeln nicht duplizieren, abschwächen oder überschreiben.

## Workflow-Katalog

| Workflow | Verwenden, wenn | Ablauf |
|---|---|---|
| Änderung umsetzen | Code oder Doku geändert werden soll. | Kontext lesen, Änderung machen, passende Checks ausführen, Ergebnis zusammenfassen. |
| Autopilot mit gebündelter Freigabe | eine zusammenhängende Umsetzung oder ein Release mit wenigen Rückfragen delegiert, im Hintergrund fortgesetzt oder natürlich beziehungsweise gesprochen freigegeben werden soll. | [autopilot.md](https://bastivonnijodex.github.io/agents/workflows/autopilot.md) anwenden. |
| Backlog Item erstellen und verfeinern | eine Idee, Anforderung, ein Fehler oder technische Arbeit als belastbares Backlog Item vorbereitet, geprüft oder erstellt werden soll. | [backlog-item.md](https://bastivonnijodex.github.io/agents/workflows/backlog-item.md) anwenden. |
| Produktkonzept erstellen und entscheiden | eine Produktidee vor der Umsetzung untersucht, mit Optionen und Auswirkungen bewertet oder zur Product-Owner-Entscheidung vorbereitet werden soll. | [product-concept.md](https://bastivonnijodex.github.io/agents/workflows/product-concept.md) anwenden. |
| Neue Applikation erstellen | Eine neue App, ein neues Tool, Dashboard, Portal, internes System oder Webprodukt erstellt oder initialisiert werden soll. | [new-application.md](https://bastivonnijodex.github.io/agents/workflows/new-application.md) anwenden. |
| Review | eine Prüfung angefordert ist. | Befunde priorisieren, Risiken nennen, Tests oder fehlende Checks benennen; bei sicherheitsrelevantem Scope zusätzlich die Rolle [Security Reviewer](https://bastivonnijodex.github.io/agents/roles/security-reviewer.md) anwenden. |
| Release vorbereiten | Commit, Tag, Push, Release Notes oder Deployment vorbereitet werden soll. | [release.md](https://bastivonnijodex.github.io/agents/workflows/release.md) anwenden. |
| Dokumentation aktualisieren | Regeln, Projektwissen oder Produktverhalten dokumentiert werden soll. | Quelle prüfen, passende Doku ändern, Links und Wahrheit gegen Stand abgleichen. |

## Pflege

[SHOULD] Eigene Workflow-Dateien werden erst ergänzt, wenn ein Ablauf wiederkehrend genug ist und mehr Details benötigt.
