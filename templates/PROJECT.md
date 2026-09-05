# PROJECT.md

## Zweck

Beschreibe kurz, wofür dieses Repository existiert.

## Produktziel und Scope

Beschreibe Zielgruppe, wichtigsten Nutzen, MVP, enthaltenen Scope und bewusste
Nicht-Ziele.

Beschreibe, welche Produktentscheidungen menschlich bleiben und welche
reversiblen technischen Detailentscheidungen Agenten innerhalb eines
bestätigten Scopes selbst treffen dürfen.

## Versionsbasis

Beschreibe relevante Versionen, Deployments, Umgebungen oder Release-Regeln.

## Source of Truth

[MUST] Definiere, welche Repository-Dokumentation, Issues, Systeme und
Produktquellen verbindlich sind.

## Fachliche Leitplanken

[MUST] Beschreibe verbindliche fachliche Regeln dieses Projekts.

[MUST_NOT] Beschreibe fachliche Dinge, die Agenten nicht tun oder nicht erfinden dürfen.

## Technische Leitplanken

[MUST] Beschreibe technische Regeln, Frameworks, unterstützte Plattformen,
Runtime-Versionen, Setup-, Start-, Test- und Build-Kommandos sowie
Architekturgrenzen.

[SHOULD] Beschreibe bevorzugte Patterns und Konventionen.

## Architektur und Daten

Beschreibe zentrale Komponenten, Datenobjekte, Schnittstellen, Persistenz,
Rollen und schwer rückbaubare Technologieentscheidungen.

## Sicherheit und Datenschutz

Beschreibe Secrets, Berechtigungen, sensible oder personenbezogene Daten,
Aufbewahrung, Löschung, externe Anbieter und erforderliche Prüfungen.

## Checks

Beschreibe, welche Tests, Builds oder manuellen Prüfungen nach Änderungen erforderlich sind.

## Release, Deployment und Betrieb

Beschreibe Versionierung, Umgebungen, Release Notes, Deployment, Monitoring,
Backup, Migration, Wiederherstellung und Rollback, soweit relevant.

[MUST_IF] Produktive Ausführung vorgesehen ist, beschreibe die unabhängigen
Merkmale, mit denen Zielumgebung, Account oder Host, Dienst, Datenbank oder
Datenspeicher und erwartete Struktur vor jedem Schreibzugriff verifiziert
werden.

[SHOULD] Benenne den projektlokalen, versionierten Automationsweg für
schreibfreien Vorlauf, Release, Backup, Migration, Deployment und
Verifikation.

[MUST_IF] Mehrere Arbeitspakete in einem Release gebündelt werden können,
beschreibe, wie der gemeinsame Release-Scope, Abhängigkeiten, Reihenfolge,
Checks und Rollback belegt werden.

## Übergabe und Wiederaufnahme

Beschreibe, welche führende Quelle Issue, Scope, Freigabestufe, Arbeitsstand,
Checks, offene Entscheidungen, Stop-Bedingungen und nächsten Schritt für einen
Wechsel zwischen Chats, Agenten, Worktrees oder Rechnern festhält.

## Definition of Done

Beschreibe, welche Akzeptanzkriterien, Checks, Dokumentations-, Security-,
Datenschutz- und Release-Anforderungen für einen Abschluss erfüllt sein müssen.

## Verbotene Aktionen

Beschreibe projektspezifische Aktionen, die Agenten nicht ohne ausdrückliche
Freigabe ausführen dürfen, zum Beispiel als konkrete `[MUST_NOT]`-Regeln.
