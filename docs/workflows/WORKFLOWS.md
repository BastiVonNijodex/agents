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
| Review | eine Prüfung angefordert ist. | Befunde priorisieren, Risiken nennen, Tests oder fehlende Checks benennen. |
| Release vorbereiten | Commit, Push, Release Notes oder Deployment vorbereitet werden soll. | Arbeitsstand prüfen, Checks ausführen, Version/Notes vorbereiten, erst nach Freigabe extern wirksam handeln. |
| Dokumentation aktualisieren | Regeln, Projektwissen oder Produktverhalten dokumentiert werden soll. | Quelle prüfen, passende Doku ändern, Links und Wahrheit gegen Stand abgleichen. |

## Pflege

[SHOULD] Eigene Workflow-Dateien werden erst ergänzt, wenn ein Ablauf wiederkehrend genug ist und mehr Details benötigt.

