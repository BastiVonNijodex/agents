# AGENTS.md

Die verbindlichen globalen Agentenregeln stehen unter:

https://bastivonnijodex.github.io/agents/AGENTS.md

Zu Beginn jeder Coding-, Review-, Debugging-, Planungs-, Test-, Deployment- oder Dokumentationsaufgabe muss diese Datei gelesen und beachtet werden.

Wenn projektspezifische Regeln existieren, gelten zusätzlich `PROJECT.md` und die lokale Repository-Dokumentation.

Wenn die globale Datei nicht erreichbar ist, soll der Agent den Abruf über Browser oder Shell-Fallback versuchen:

```sh
curl -L "https://bastivonnijodex.github.io/agents/AGENTS.md"
```

Wenn kein Abruf möglich ist, muss der Agent dies melden und vor riskanten oder zustandsverändernden Arbeiten stoppen.

