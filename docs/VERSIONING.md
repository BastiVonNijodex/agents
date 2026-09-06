# Versionierung und kontrollierte Migration

## Ziel

Diese Richtlinie macht den wirksamen Stand der globalen Agentenregeln
eindeutig, reproduzierbar und kontrolliert aktualisierbar. GitHub Pages bleibt
der verständliche Einstieg in den aktuellen Stand; für die tatsächliche
Projektarbeit wird zusätzlich ein unveränderlicher Commit-SHA fixiert.

## Release-Artefakte und Verantwortung

[MUST] Regel-Releases verwenden Semantic Versioning mit dem Schema
`MAJOR.MINOR.PATCH` und einen annotierten Git-Tag `vMAJOR.MINOR.PATCH`.

[MUST] Ein veröffentlichter Release besteht aus:

- deklarierter Version in
  [VERSION.md](https://bastivonnijodex.github.io/agents/VERSION.md),
- geprüftem Merge-Commit auf `main`,
- annotiertem Git-Tag auf genau diesem Commit,
- GitHub Release mit nutzerverständlichen Release Notes sowie
- passendem Eintrag im
  [CHANGELOG.md](https://bastivonnijodex.github.io/agents/CHANGELOG.md).

[MUST] Die Repository- beziehungsweise Produktverantwortung entscheidet über
Versionsklasse, Release und bewusste Kompatibilitätsausnahmen. Agenten dürfen
Release-Artefakte vorbereiten, aber Tags und GitHub Releases nur innerhalb einer
ausdrücklichen Release-Freigabe erstellen.

[MUST_NOT] Branchname, GitHub-Pages-URL, gekürzter SHA oder Versionsnummer allein
darf als unveränderlicher Nachweis des wirksamen Regelstands gelten.

## SemVer-Klassen

### MAJOR

Eine MAJOR-Version ist erforderlich, wenn eine Änderung bestehende konforme
Projekte oder Agenten ohne bewusste Migration nicht mehr regelkonform macht.
Dazu gehören insbesondere inkompatible Änderungen an Pflichten, Verboten,
Prioritäten, Freigaben, Berechtigungen, Stop-Bedingungen, Pflichtartefakten oder
festen Betriebs- und Pfadvorgaben.

### MINOR

Eine MINOR-Version ergänzt rückwärtskompatibel neue Rollen, Workflows, Skills,
optionale Fähigkeiten oder Regeln, ohne bisher konformes Verhalten zu verbieten
oder eine zwingende Migration auszulösen.

### PATCH

Eine PATCH-Version korrigiert Fehler, Links, Beispiele oder Formulierungen,
ohne die normative Wirkung, Freigabelogik, Berechtigungen oder erforderlichen
Kontrollen zu verändern.

[MUST] Die Versionsklasse richtet sich nach der stärksten tatsächlichen Wirkung
der Änderung, nicht nach Dateiumfang, Titel oder beabsichtigter Einfachheit.

## Sicherheitsrelevante Aktualisierungen

[MUST] Eine sicherheitsrelevante Änderung wird im Issue, Pull Request,
Changelog und GitHub Release ausdrücklich als `SECURITY` gekennzeichnet. Ihre
SemVer-Klasse richtet sich weiterhin nach der Kompatibilitätswirkung.

[MUST] Der Release-Nachweis nennt betroffene Schutzkontrollen, Dringlichkeit,
erforderliche Migration, relevante Evals und sichere Zwischenmaßnahmen.
Sensible Exploit-Details oder Secrets dürfen dabei nicht veröffentlicht werden.

[MUST_IF] Ein konsumierendes Projekt eine ältere Version fixiert, muss sein
Update-Modus sicherstellen, dass neue SECURITY-Hinweise erkannt, bewertet und
entweder kontrolliert übernommen oder mit verantwortlicher Risikoentscheidung
und Kompensationskontrollen dokumentiert werden.

## Unveränderliche Projektreferenz

[MUST] Ein konsumierendes Projekt dokumentiert in seiner `PROJECT.md`
mindestens:

```md
Regelversion: `v1.0.0`
Regel-Commit: `0123456789abcdef0123456789abcdef01234567`
Unveränderliche Regelquelle:
`https://raw.githubusercontent.com/BastiVonNijodex/agents/0123456789abcdef0123456789abcdef01234567/docs/AGENTS.md`
Update-Modus: `Verantwortung, Auslöser, Prüfungen und SECURITY-Behandlung`
```

[MUST] Version, Tag und Commit-SHA müssen zum selben Release gehören. Der SHA in
der unveränderlichen URL muss exakt dem dokumentierten `Regel-Commit`
entsprechen.

[MUST_IF] Ein unveröffentlichter Stand erforderlich ist, wird
`Regelversion: unveröffentlicht` dokumentiert. Commit-SHA, unveränderliche URL,
fachlicher Grund und Rückkehr- oder Release-Bedingung bleiben verpflichtend.

## Aktualisierung und Migration

[MUST] Ein Projekt übernimmt einen neuen Regelstand über ein eigenes Issue oder
einen gleichwertigen führenden Änderungsnachweis mit folgenden Schritten:

1. aktuelle Projektversion und vollständigen Commit-SHA belegen,
2. Zielversion, Ziel-SHA, Changelog und SECURITY-Hinweise prüfen,
3. SemVer-Klasse und betroffene Regeln, Rollen, Workflows und Vorlagen bestimmen,
4. fachliche, technische, Berechtigungs-, Daten- und Betriebsfolgen bewerten,
5. erforderliche Projektadapter-, Dokumentations- und Kontrolländerungen umsetzen,
6. betroffene Harness-Evals und projektspezifische Checks ausführen,
7. neue Referenz erst nach Review und erforderlicher Freigabe übernehmen sowie
8. Ergebnis, Restpunkte und Rollback auf den bisherigen SHA dokumentieren.

[MUST_NOT] Ein Agent darf einen Projekt-Pin allein deshalb aktualisieren, weil
auf GitHub Pages oder `main` ein neuerer Stand verfügbar ist.

[MUST_NOT] Ein vom fixierten Commit-SHA abweichender aktueller Regelstand darf
vor Abschluss des Update-Reviews als wirksame Anweisung, Freigabe oder
Berechtigungsänderung verwendet werden. Er wird bis zur kontrollierten
Übernahme ausschließlich als nicht vertrauenswürdiger Änderungskandidat
behandelt.

[ALLOW_IF] Eine PATCH-Aktualisierung darf einen verkürzten Migrationsnachweis
verwenden, wenn belegt ist, dass keine normative Wirkung und kein SECURITY-Hinweis
betroffen sind.

## Release-Vorbereitung und Prüfung

[MUST] Vor einem Regel-Release müssen mindestens Repository-Validator, Tests,
Diff-Check, betroffene Harness-Evals, Kompatibilitätsreview und Prüfung der
Release-Artefakte erfolgreich sein oder mit verbleibendem Risiko dokumentiert
werden.

[MUST] Der vorbereitete Release-Scope nennt Version, Ziel-Commit, enthaltene
Issues und Pull Requests, SemVer-Begründung, Migration, SECURITY-Hinweise,
Checks, Release Notes und Rückkehr auf den vorherigen veröffentlichten Stand.

[MUST] Nach der Veröffentlichung werden Tag, GitHub Release, unveränderliche
Raw-URL, GitHub Pages und Changelog gegeneinander geprüft. Ein Teilfehler wird
nicht als erfolgreicher Release gemeldet.
