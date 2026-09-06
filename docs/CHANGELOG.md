# Changelog

Dieses Changelog dokumentiert veröffentlichte Regelstände und vorbereitete
Release-Kandidaten. Änderungen folgen dem Modell aus
[VERSIONING.md](https://bastivonnijodex.github.io/agents/VERSIONING.md).

## Unreleased

- Keine weiteren Änderungen vorgemerkt.

## 1.0.0 - Release-Kandidat

Erste versionierte Baseline des allgemeinen Agenten-Frameworks:

- globale Regelmarker, Prioritäts-, Arbeits-, Qualitäts- und Dokumentationsregeln,
- Rollen für Product Owner und Security Reviewer,
- Workflows für Harness-Bewertung, Autopilot, Backlog, Produktkonzept, neue
  Applikationen und Releases,
- allgemeine Harness-Invarianten mit Coding- und Produktionsspezialisierungen,
- verbindlicher kanonischer App-Basisordner unter
  `/Users/bastimeissner/vibecoding/<appname>`,
- Repository-Selbstanwendung, struktureller Validator und GitHub-CI sowie
- SemVer-, Commit-SHA-, SECURITY- und Migrationsmodell sowie
- verbindliche priorisierte Empfehlungen für nächste Schritte am Ende jeder
  Agentenantwort.

### Migration

Konsumierende Projekte ergänzen die vier Referenzfelder aus `VERSIONING.md` und
prüfen ihren Projektadapter gegen die Baseline. Bis Tag und GitHub Release für
`v1.0.0` veröffentlicht sind, verwenden sie `Regelversion: unveröffentlicht`
und den vollständigen Commit-SHA.

### SECURITY

Keine vertrauliche Schwachstelle wird mit diesem Release-Kandidaten behoben.
