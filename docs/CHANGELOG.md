# Changelog

Dieses Changelog dokumentiert veröffentlichte Regelstände und vorbereitete
Release-Kandidaten. Änderungen folgen dem Modell aus
[VERSIONING.md](https://bastivonnijodex.github.io/agents/VERSIONING.md).

## Unreleased

- Kanonischer App-Basisordner neutral als `~/vibecoding/<appname>` statt mit
  absolutem Benutzerpfad formuliert. Auf dem Rechner des Nutzers zeigt der Pfad
  auf denselben Ordner; Validator, Test und Vorlage sind angepasst.
- README um einen kurzen Einstieg für Außenstehende ergänzt (Deutsch und
  Englisch).

### Migration

Keine Handlung nötig. Projekte, deren `PROJECT.md` noch den absoluten Pfad
nennt, bleiben gültig und können beim nächsten Update auf `~/vibecoding/<appname>`
umgestellt werden.

## 1.0.0 - 2026-09-06

Erste versionierte Baseline des allgemeinen Agenten-Frameworks:

- globale Regelmarker, Prioritäts-, Arbeits-, Qualitäts- und Dokumentationsregeln,
- Rollen für Product Owner und Security Reviewer,
- Workflows für Harness-Bewertung, Autopilot, Backlog, Produktkonzept, neue
  Applikationen und Releases,
- allgemeine Harness-Invarianten mit Coding- und Produktionsspezialisierungen,
- verbindlicher kanonischer App-Basisordner unter
  `/Users/bastimeissner/vibecoding/<appname>`,
- Repository-Selbstanwendung, struktureller Validator und GitHub-CI sowie
- wiederverwendbare, maschinenlesbare Harness-Evals mit allgemeiner Baseline,
  additiven Coding- und Produktionsprofilen und synthetischem Referenzlauf,
- SemVer-, Commit-SHA-, SECURITY- und Migrationsmodell sowie
- verbindliche priorisierte Empfehlungen für nächste Schritte am Ende jeder
  Agentenantwort.

### Migration

Konsumierende Projekte ergänzen die vier Referenzfelder aus `VERSIONING.md`,
verwenden `Regelversion: v1.0.0` mit dem vollständigen Release-Commit und
prüfen ihren Projektadapter gegen die Baseline. Der neue Stand wird erst nach
dem projektspezifischen Update-Review wirksam.

### SECURITY

Keine vertrauliche Schwachstelle wird mit diesem Release behoben.
Die wiederverwendbaren Evals ergänzen SECURITY-Regressionen für manipulierten
oder veralteten Kontext, fehlende Freigaben, Secrets, Zielverwechslungen,
Teilfehler und Wiederherstellung. Synthetische Referenzergebnisse bleiben
ausdrücklich von realer Eignungs- und Produktionsevidenz getrennt.
