# agents

Zentrale Agenten-Anweisungen fuer Repositories von BastiVonNijodex.

Die wichtigste Datei ist:

https://bastivonnijodex.github.io/agents/AGENTS.md

## Verwendung in einem Repository

Lege im Ziel-Repository eine kurze lokale `AGENTS.md` an:

```md
# AGENTS.md

Die verbindlichen globalen Agentenregeln stehen unter:

https://bastivonnijodex.github.io/agents/AGENTS.md

Zu Beginn jeder Aufgabe muss diese Datei gelesen und beachtet werden.

Wenn projektspezifische Regeln existieren, gelten zusaetzlich `PROJECT.md` und die lokale Repository-Dokumentation.
```

Optional kann das Repository eine `PROJECT.md` mit projektspezifischen Leitplanken enthalten.

## Dateien

- `AGENTS.md`: globale Agentenregeln
- `templates/AGENTS.md`: kurzer Wrapper fuer andere Repositories
- `templates/PROJECT.md`: Vorlage fuer projektspezifische Regeln

## Pflege

Aenderungen an `AGENTS.md` wirken auf alle Repositories, die auf diese Datei verweisen.

Deshalb sollten Aenderungen klein, nachvollziehbar und versioniert erfolgen.

