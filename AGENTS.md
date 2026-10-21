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

## Produktionszugang über SSH-Aliase

[MUST] Für einen ausdrücklich freigegebenen Produktionszugriff darf ein Agent ausschließlich einen dokumentierten kanonischen SSH-Alias verwenden. Eine nicht aufgelöste oder nicht dokumentierte Zielidentität blockiert den Zugriff.

[MUST] Vor einer Verbindung muss der Agent lokal und ohne Netzwerkzugriff `ssh -G <alias>` prüfen. Die Ausgabe muss zum beabsichtigten Projekt passen; Hostnamen, IP-Adressen, Benutzernamen, Ports, Schlüsselpfade, Host-Keys, Secrets und Serverkonfigurationen dürfen weder in Chat, Agenten-Memory, Repository-Dokumentation noch Tickets übernommen werden.

[MUST_NOT] Ein Agent darf keinen Produktionshost erraten, keinen Alias durch eine IP-Adresse ersetzen, keine SSH-Konfiguration schreiben oder verändern und keinen unbekannten Host-Key automatisch akzeptieren.

[MUST] Ein SSH-Alias ist ausschließlich eine Zielreferenz, keine Freigabe für Release, Deployment, Migration, Neustart, Datenzugriff oder sonstige Produktionsänderung. Es gelten zusätzlich die projektbezogenen Freigaben, Backup-, Preflight-, Rollback- und Verifikations-Gates.

Aktuell verifizierte Aliasnamen:

- `finja3-prod` für FINJA 3
- `finja3-mcp-prod` für FINJA-MCP
- `nijodex-website-prod` für nijodexWebsite
- `meinpensum-prod` für MeinPensum

[MUST_NOT] Für Tipolingo und jedes weitere Repository ohne vollständig verifizierte produktive Zielidentität darf kein Alias angenommen oder genutzt werden. Der Agent meldet den fehlenden Nachweis und stoppt vor Produktionszugriff.
