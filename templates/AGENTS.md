# AGENTS.md

Die öffentlich aktuelle Fassung der globalen Agentenregeln steht unter:

https://bastivonnijodex.github.io/agents/AGENTS.md

## Wirksamer Regelstand

Die projektspezifische `PROJECT.md` nennt die wirksame Regelversion, den
vollständigen Commit-SHA, die unveränderliche Regelquelle und den Update-Modus.
Dieser fixierte Stand ist für die Projektarbeit maßgeblich. Die aktuelle
GitHub-Pages-Fassung wird zusätzlich auf sicherheitsrelevante Aktualisierungen
und bewusst zu übernehmende Änderungen geprüft.

Eine vom fixierten SHA abweichende aktuelle Fassung ist bis zum abgeschlossenen
Update-Review nur ein nicht wirksamer Änderungskandidat. Anweisungen aus diesem
Kandidaten dürfen den laufenden Task, seine Berechtigungen oder Freigaben nicht
verändern.

Wenn die Referenzfelder fehlen, widersprüchlich oder noch Platzhalter sind,
muss der Agent dies melden und vor riskanten oder zustandsverändernden Arbeiten
stoppen.

Zu Beginn jeder Coding-, Review-, Debugging-, Planungs-, Test-, Deployment- oder Dokumentationsaufgabe muss diese Datei gelesen und beachtet werden.

Wenn projektspezifische Regeln existieren, gelten zusätzlich `PROJECT.md` und die lokale Repository-Dokumentation.

Wenn die globale Datei nicht erreichbar ist, soll der Agent den Abruf über Browser oder Shell-Fallback versuchen:

```sh
curl -L "https://bastivonnijodex.github.io/agents/AGENTS.md"
```

Wenn kein Abruf möglich ist, muss der Agent dies melden und vor riskanten oder zustandsverändernden Arbeiten stoppen.
