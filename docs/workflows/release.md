# release.md

## Ziel

Dieser Workflow beschreibt die globale Release-Disziplin für Agenten. Projektspezifische Release-Regeln aus `PROJECT.md` oder der lokalen Repository-Dokumentation gelten zusätzlich.

## Verwenden

[MUST_IF] Dieser Workflow muss verwendet werden, wenn ein Commit, Tag, Push, GitHub Release, Release Notes, Deployment oder eine produktionsnahe Übergabe vorbereitet oder durchgeführt werden soll.

## Ablauf

[MUST] Der Agent prüft zuerst den aktuellen Arbeitsstand, Branch, offene Änderungen und die für das Projekt geltenden Release-Regeln.

[MUST] Der Agent klärt, welche extern wirksamen Schritte ausdrücklich freigegeben sind.

[MUST_NOT] Der Agent darf Tags, Releases, Pushes, produktionswirksame Deployments, Datenbankmigrationen, SSH-Zugriffe oder andere extern wirksame Schritte ohne ausdrückliche Freigabe nicht ausführen.

[MUST] Der Agent führt die passenden Tests, Builds, Lints, Audits oder manuellen Prüfungen aus, bevor er eine Release-Freigabe als erledigt meldet.

[MUST_IF] Ein erforderlicher Check nicht ausführbar ist, muss der Agent den Grund und das verbleibende Risiko nennen.

[MUST] Release Notes müssen kurz, nutzerverständlich und am tatsächlichen Änderungsumfang ausgerichtet sein.

[MUST] Relevante Dokumentation muss aktualisiert werden, wenn sich Verhalten, Setup, API, Schema, Deployment, Release-Prozess oder Agentenregeln ändern.

[MUST] Vor Abschluss nennt der Agent enthaltene Änderungen, ausgeführte Checks, aktualisierte Dokumentation und verbleibende Risiken oder offene Punkte.

## Grenzen

[MUST_NOT] Projektspezifische Versions-, Build-, Migrations-, Backup- oder Deployment-Kommandos dürfen nicht global erfunden werden.

[MUST] Solche Details müssen aus `PROJECT.md`, lokaler Dokumentation, bestehendem Code, Skripten oder einer direkten Nutzeranweisung stammen.

## Endergebnis

[MUST] Ein Release-Workflow endet erst, wenn der freigegebene Scope abgeschlossen oder ein Blocker klar benannt ist.

