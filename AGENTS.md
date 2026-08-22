# AGENTS.md

## Verbindliche Arbeitsregeln

Die verbindlichen globalen Agentenregeln stehen öffentlich unter:

https://bastivonnijodex.github.io/agents/AGENTS.md

## Umgang mit den Arbeitsregeln

[MUST] Zu Beginn jedes Tasks muss der Agent sicherstellen, dass die globale `AGENTS.md` im aktuellen Kontext bekannt, vollständig und aktuell genug ist, und sie befolgen.

[ALLOW_IF] Wenn die globale `AGENTS.md` in der laufenden Unterhaltung bereits gelesen wurde und kein Hinweis auf eine zwischenzeitliche Änderung besteht, darf der Agent die vorhandene Kontextfassung wiederverwenden, statt sie erneut vollständig abzurufen.

[MUST_IF] Der Agent muss die globale `AGENTS.md` erneut abrufen, wenn die vorhandene Kontextfassung fehlt, unvollständig, offensichtlich veraltet oder nicht eindeutig identifizierbar ist.

[MUST_IF] Wenn ein Web- oder Browser-Tool die Datei nicht abrufen kann, muss der Agent vor einem Abbruch einen Shell-Fallback versuchen, zum Beispiel:

```sh
curl -L "https://bastivonnijodex.github.io/agents/AGENTS.md"
```

[MUST_IF] Wenn kein verfügbarer Abrufweg funktioniert, muss der Agent dies melden und vor riskanten oder zustandsverändernden Arbeiten stoppen.

