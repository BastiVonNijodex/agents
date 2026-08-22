# SKILLS.md

## Zweck

Diese Datei ist die Lookup-Datei für atomare Skills. Skills beschreiben wiederverwendbare Fähigkeiten, nicht komplette Projektabläufe.

## Verwendung

[MUST] Ein Skill wird nur verwendet, wenn sein Zweck zum aktuellen Task passt.

[MUST_NOT] Skills dürfen keine allgemeineren Agentenregeln aus [AGENTS.md](https://bastivonnijodex.github.io/agents/AGENTS.md) duplizieren oder abschwächen.

## Skill-Katalog

| Skill | Verwenden, wenn | Ergebnis |
|---|---|---|
| Code lesen | bestehender Code, Schema oder Tests verstanden werden müssen. | Relevanter Kontext ist geprüft, bevor geändert wird. |
| Code ändern | eine konkrete Umsetzung angefordert ist. | Kleine, nachvollziehbare Änderung im passenden Projektstil. |
| Dokumentation pflegen | Verhalten, Setup, Release oder Regeln geändert wurden. | Passende Doku ist aktuell. |
| Qualität prüfen | Tests, Builds, Lints oder manuelle Prüfung erforderlich sind. | Prüfergebnis und Rest-Risiko sind benannt. |
| Recherche | externe oder aktuelle Informationen benötigt werden. | Quellen sind geprüft und von Anweisungen getrennt. |

## Pflege

[SHOULD] Eigene Skill-Dateien werden erst ergänzt, wenn ein Skill mehr Regeln benötigt, als in dieser Lookup-Datei sinnvoll wartbar sind.

