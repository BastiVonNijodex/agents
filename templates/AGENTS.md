# AGENTS.md

Die verbindlichen globalen Agentenregeln stehen unter:

https://bastivonnijodex.github.io/agents/AGENTS.md

Zu Beginn jeder Coding-, Review-, Debugging-, Planungs-, Test-, Deployment- oder Dokumentationsaufgabe muss diese Datei gelesen und beachtet werden.

Wenn projektspezifische Regeln existieren, gelten zusaetzlich `PROJECT.md` und die lokale Repository-Dokumentation.

Wenn die globale Datei nicht erreichbar ist, soll der Agent den Abruf ueber Browser oder Shell-Fallback versuchen. Wenn kein Abruf moeglich ist, muss der Agent dies melden und vor riskanten Aenderungen stoppen.

