# release.md

## Ziel

Dieser Workflow beschreibt die globale Release-Disziplin für Agenten. Projektspezifische Release-Regeln aus `PROJECT.md` oder der lokalen Repository-Dokumentation gelten zusätzlich.

## Verwenden

[MUST_IF] Dieser Workflow muss verwendet werden, wenn ein Commit, Tag, Push, GitHub Release, Release Notes, Deployment oder eine produktionsnahe Übergabe vorbereitet oder durchgeführt werden soll.

## Ablauf

[MUST] Der Agent prüft zuerst den aktuellen Arbeitsstand, Branch, offene Änderungen und die für das Projekt geltenden Release-Regeln.

[MUST] Der Agent klärt, welche extern wirksamen Schritte ausdrücklich freigegeben sind.

[MUST_NOT] Der Agent darf Tags, Releases, Pushes, produktionswirksame Deployments, Datenbankmigrationen, SSH-Zugriffe oder andere extern wirksame Schritte ohne ausdrückliche Freigabe nicht ausführen.

[MUST_IF] Der Nutzer den Produktionsserver selbst bedient oder kein ausdrücklich freigegebener SSH-Zugriff für den Agenten besteht, muss der Agent die Übergabe als kopierbaren Terminalblock formulieren. Der Block muss auf dem konkreten Projektkontext beruhen und darf keine erfundenen Versions-, Backup-, Migrations- oder Deploy-Kommandos enthalten.

[MUST] Der Agent führt die passenden Tests, Builds, Lints, Audits oder manuellen Prüfungen aus, bevor er eine Release-Freigabe als erledigt meldet.

[MUST_IF] Ein erforderlicher Check nicht ausführbar ist, muss der Agent den Grund und das verbleibende Risiko nennen.

[MUST] Release Notes müssen kurz, nutzerverständlich und am tatsächlichen Änderungsumfang ausgerichtet sein.

[MUST_IF] Eine getestete oder abgenommene Umsetzung betrifft eine Applikation und ist für Nutzer sichtbar, fachlich relevant oder bedienungsrelevant, muss der Agent Release Notes vorbereiten.

[MUST_IF] Die Applikation einen Nutzerbereich für neue Updates, Release-Hinweise oder Onboarding-Neuigkeiten besitzt, muss der Agent die projektspezifische Ablage oder Einspeisung der Release Notes berücksichtigen.

[MUST] Release Notes beschreiben den sichtbaren Nutzen oder die geänderte Bedienung, nicht nur interne Implementierungsdetails.

[MUST] Relevante Dokumentation muss aktualisiert werden, wenn sich Verhalten, Setup, API, Schema, Deployment, Release-Prozess oder Agentenregeln ändern.

[MUST] Vor Abschluss nennt der Agent enthaltene Änderungen, ausgeführte Checks, aktualisierte Dokumentation und verbleibende Risiken oder offene Punkte.

[MUST_IF] Der Agent den Produktionsserver nicht selbst bedient hat, muss er vor Abschluss ausdrücklich sagen, dass der Produktionsdeploy noch nicht ausgeführt wurde und die Serverbefehle noch durch den Nutzer laufen müssen.

## Grenzen

[MUST_NOT] Projektspezifische Versions-, Build-, Migrations-, Backup- oder Deployment-Kommandos dürfen nicht global erfunden werden.

[MUST_NOT] Der globale Workflow darf keinen konkreten App-internen Release-Note-Speicher erzwingen. Der Speicherort muss projektspezifisch definiert sein.

[MUST] Solche Details müssen aus `PROJECT.md`, lokaler Dokumentation, bestehendem Code, Skripten oder einer direkten Nutzeranweisung stammen.

## Endergebnis

[MUST] Ein Release-Workflow endet erst, wenn der freigegebene Scope abgeschlossen oder ein Blocker klar benannt ist.
