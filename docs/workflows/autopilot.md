# Workflow: Autopilot mit gebuendelter Freigabe

## Ziel

Dieser Workflow uebersetzt eine eindeutige natuerliche oder gesprochene
Freigabe in ein begrenztes Handlungspaket. Er erlaubt dem Agenten, innerhalb des
bestaetigten Scopes selbststaendig bis zum Abschluss, zur Uebergabe oder zu einer
Stop-Bedingung weiterzuarbeiten, ohne fuer bereits freigegebene technische
Einzelschritte erneut zu fragen.

Der Workflow erweitert weder den fachlichen Scope noch Plattformberechtigungen.
Projekt-, Sicherheits-, Datenschutz- und Umgebungsregeln bleiben verbindlich.

## Verwenden

[MUST_IF] Der Nutzer eine zusammenhaengende Umsetzung oder einen Release mit
wenigen Rueckfragen delegieren, Arbeit im Hintergrund fortsetzen lassen oder
eine natuerliche beziehungsweise gesprochene Freigabe als Handlungspaket nutzen
moechte, muss der Agent diesen Workflow lesen und anwenden.

[MUST_NOT] Der Workflow darf nicht aus einer allgemeinen Erwartung an
Selbststaendigkeit, aus einer frueheren Freigabe fuer einen anderen Scope oder
aus dem blossen Vorhandensein eines Backlog Items aktiviert werden.

## Grundsaetze

[MUST] Jede Autopilot-Freigabe bindet drei Dinge zusammen:

1. den fachlich und technisch abgegrenzten Scope,
2. das autorisierte Handlungspaket,
3. die geltenden Stop-Bedingungen.

[MUST] Der Agent dokumentiert diese drei Punkte vor oder unmittelbar mit der
ersten extern wirksamen Handlung knapp im fuehrenden Issue, Pull Request oder
Abschlussnachweis.

[MUST_NOT] Eine Freigabe fuer einen Scope darf nicht auf andere Issues,
Repositorien, Umgebungen, Empfaenger oder spaetere Releases uebertragen werden.

[MUST_NOT] Eine Autopilot-Freigabe darf Plattformfreigaben, fehlende technische
Berechtigungen, spezifische Verbote oder zwingende menschliche Kontrollen nicht
umgehen.

## Freigabestufen

### 1. Anforderung und Klaerung

Ohne Umsetzungsfreigabe darf der Agent:

- fuehrende Quellen und bestehenden Zustand lesen,
- Anforderungen, Risiken und Abhaengigkeiten klaeren,
- Optionen, Plaene, Konzepte und Backlog-Entwuerfe vorbereiten,
- reversible, nicht extern wirksame Diagnose ausfuehren.

[MUST_NOT] Aus einer Bitte um Analyse, Review, Planung oder Status darf keine
Implementierungs-, Push-, Merge-, Migrations- oder Deploymentfreigabe abgeleitet
werden.

### 2. Umsetzung

Die kanonische Formulierung lautet:

> Umsetzung freigegeben.

Eine gleichbedeutende natuerliche oder gesprochene Formulierung gilt ebenfalls,
wenn Scope, Ziel und Umsetzungsabsicht eindeutig sind.

[MUST] Vor Beginn fasst der Agent den bestaetigten Scope und das projektseitig
zulaessige Umsetzungspaket knapp zusammen.

Das Umsetzungspaket darf, soweit fuer den Scope erforderlich und durch den
Projektadapter erlaubt, enthalten:

- geschuetzte Repository-Synchronisierung sowie Branch oder Worktree,
- Implementierung, Refactoring und Dokumentation,
- lokale und DEV-Checks, Builds, Tests und Browser-Abnahmen,
- gezielte synthetische DEV-Testdaten, DEV-Migrationen und DEV-Neustarts,
- Commit, Push, Pull Request und CI-Korrekturen,
- Review-Korrekturen und Merge nach erfuellten projektseitigen Gates,
- Issue-, Pull-Request- und Projektdokumentation zum bestaetigten Scope.

[MUST] Extern wirksame Teilschritte gelten nur dann als ausdruecklich
freigegeben, wenn sie im dokumentierten Umsetzungspaket enthalten sind.

[MUST_NOT] Die Umsetzungsfreigabe autorisiert keinen Produktionsrelease, kein
Produktionsdeployment, keine produktive Datenmigration, keine produktive
Secret-Aenderung und keine neue externe Kommunikation oder Veroeffentlichung
ausserhalb des dokumentierten Umsetzungspakets.

### 3. Release und Deployment

Die kanonische Formulierung lautet:

> Release und Deployment freigegeben.

Eine gleichbedeutende natuerliche oder gesprochene Formulierung gilt ebenfalls,
wenn Release-Scope, Zielumgebung und Ausfuehrungsabsicht eindeutig sind.

[MUST] Diese Freigabe gilt nur fuer einen bereits abgegrenzten und
nachweislich geprueften Release-Scope. Sie darf nicht aus Umsetzungsfreigabe,
DEV-Abnahme, Pull Request oder Merge abgeleitet werden.

Das Produktionspaket darf, soweit durch Projektregeln belegt und fuer den Scope
ausdruecklich dokumentiert, enthalten:

- finalen Release-Check und Versionsvorbereitung,
- Commit, Tag, Push und GitHub Release,
- Backup und dessen Verifikation,
- gezielte produktive Migrationen,
- Deployment ueber den projektspezifisch erlaubten Zugriffsweg,
- Health Checks, Smoke Tests, Monitoring- oder Log-Pruefungen,
- dokumentierten Rollback oder Abbruch bei fehlgeschlagener Verifikation,
- Abschlussnachweis und Aktualisierung der fuehrenden Statusquellen.

[MUST] Der Projektadapter bestimmt, ob der Agent die Produktion selbst bedient
oder eine kopierbare Uebergabe fuer den Nutzer vorbereitet. Die allgemeine
Freigabe erfindet keinen SSH-, Secret-, Backup-, Migrations- oder Deploy-Zugriff.

[MUST_NOT] Ein fehlgeschlagener oder nicht ausfuehrbarer Produktionscheck darf
nicht als erfolgreicher Release gemeldet werden.

## Natuerliche und gesprochene Freigaben

[MUST] Eine natuerliche oder transkribierte muendliche Freigabe gilt als
ausdrueckliche Nutzeranweisung, wenn Handlung, Scope und Ziel eindeutig sind.

[MUST_IF] Ein erkennbarer Transkriptionsfehler, ein Widerspruch, eine
mehrdeutige Referenz oder ein unklarer Ziel-Scope die Freigabewirkung veraendern
koennte, muss der Agent einmal knapp nachfragen, bevor er extern wirksam handelt.

[MUST] Im Arbeitsnachweis wird nur die normalisierte Freigabe mit Datum, Scope
und Handlungspaket dokumentiert. Sprachaufnahme, vollstaendiges Transkript und
irrelevante Gespraechsinhalte werden nicht uebernommen.

Beispiele:

- `Setze Issue 42 um` kann eine Umsetzungsfreigabe sein, wenn Issue, Repository
  und erwarteter Ablauf im Kontext eindeutig sind.
- `Mach weiter` ist ohne eindeutig referenzierten Scope keine neue Push-,
  Merge- oder Deploymentfreigabe.
- `Bring den geprueften Release 2.4.0 in Produktion` kann Release und Deployment
  freigeben, wenn Ziel, Ausfuehrungsweg und projektseitige Gates eindeutig sind.

## Autonome Hintergrundarbeit

[MUST] Innerhalb des bestaetigten Scopes arbeitet der Agent bis zu einem
Abschluss-, Uebergabe- oder Stop-Ereignis selbststaendig weiter.

[ALLOW_IF] Der Agent darf reversible, projektkonforme technische
Detailentscheidungen selbst treffen, wenn sie keine wesentliche neue Wirkung auf
Produktumfang, Architektur, Daten, Berechtigungen, externe Kosten oder Betrieb
haben.

[MUST_IF] Eine Entscheidung Produktverhalten, Architektur, Daten,
Berechtigungen, Kosten oder Betrieb wesentlich und schwer rueckbaubar
beeinflusst, muss der Agent sie klaeren statt sie stillschweigend zu treffen.

[MUST_NOT] Der Agent fordert keine erneute Freigabe fuer einen Einzelschritt,
der bereits eindeutig im dokumentierten Handlungspaket liegt und dessen
Voraussetzungen weiterhin erfuellt sind.

[MUST] Statusmeldungen erfolgen knapp bei relevanten Meilensteinen, Blockern,
Abweichungen und Abschluss. Unveraenderter Fortschritt benoetigt keine kuenstlich
haeufigen Freigabeanfragen.

## Produktentscheidungen und technische Ausfuehrung

[MUST] Produktziel, Prioritaet, Nutzerwirkung, fachlicher Scope und bewusste
Nicht-Ziele bleiben bei der zustaendigen menschlichen Produktverantwortung.
Eine Autopilot-Freigabe autorisiert technische Ausfuehrung, aber keine
stillschweigende Erweiterung dieser Entscheidungen.

[ALLOW_IF] Der Agent darf innerhalb des bestaetigten Scopes reversible,
risikoarme technische Details selbst entscheiden und dokumentieren.

[MUST_IF] Eine neue Produktoption, groessere Architekturentscheidung,
wesentliche Betriebswirkung oder wertvolle Folgearbeit entsteht, muss der Agent
sie getrennt zur Entscheidung oder als Backlog-Vorschlag vorlegen. Der laufende
Scope bleibt unveraendert.

## Release-Buendel

[ALLOW_IF] Mehrere bereits einzeln abgegrenzte und gepruefte Arbeitspakete
duerfen in einem Release gebuendelt werden, wenn ein eigener Release-Scope die
enthaltenen Versionen, Commits oder Pull Requests, Abhaengigkeiten,
Migrationsreihenfolge, gemeinsamen Checks und den Rollback-Pfad eindeutig
benennt.

[MUST_NOT] Eine Release-Freigabe fuer ein Buendel darf fehlende
Umsetzungsfreigaben, Akzeptanz-, Security-, Review- oder CI-Gates der
enthaltenen Arbeitspakete ersetzen.

[MUST] Die Release- und Deploymentfreigabe gilt nur fuer das konkret benannte,
nachweislich gepruefte Buendel und die bezeichnete Zielumgebung.

## Zwingende Stop-Bedingungen

Der Agent stoppt vor der betroffenen Handlung und fordert bei Bedarf eine neue
Entscheidung oder Freigabe an, wenn:

- der notwendige Scope wesentlich von der bestaetigten Anforderung abweicht,
- Tests, Security-, Migrations- oder Release-Gates fehlschlagen und nicht sicher
  innerhalb des Scopes behoben werden koennen,
- eine unerwartete Migration, irreversible Aenderung oder Datenloeschung
  erforderlich wird,
- neue externe Kosten, Provider-Aktionen, Nachrichten, Veroeffentlichungen oder
  personenbezogene Datenfluesse entstehen,
- Secrets, Zugangsdaten oder manuell administrierte
  Produktionskonfigurationen gelesen oder geaendert werden muessten,
- ein kritisches oder ungeklaertes hohes Security-Finding besteht,
- Produktionsziel, aktueller Zustand, Backup, Migrationsplan, Verifikation oder
  Rollback-Pfad nicht eindeutig belegt ist,
- eine Plattformkontrolle oder spezifische Projektregel eine weitere
  Bestaetigung verlangt,
- der Nutzer die Freigabe widerruft oder den Scope ersetzt.

[MUST] Sicher innerhalb des bestaetigten Scopes behebbare Test- oder
Reviewbefunde sind keine automatische neue Freigabegrenze. Der Agent behebt sie,
wiederholt die relevanten Checks und dokumentiert das Ergebnis.

## Security Review und Risikoakzeptanz

[MUST_IF] Der Scope die Aktivierungskriterien erfuellt, muss die Rolle
[Security Reviewer](https://bastivonnijodex.github.io/agents/roles/security-reviewer.md)
geladen und angewendet werden.

[MUST_NOT] Developer, Tester oder Security Reviewer duerfen Security-Findings,
Risikoausnahmen oder Baseline-Erweiterungen implizit akzeptieren.

[MUST_IF] Keine unabhaengige Security-Reviewer-Instanz verfuegbar ist, muss die
fehlende Rollentrennung als Restrisiko im Abschlussnachweis stehen. Kritische
Scopes unterliegen zusaetzlich den Unabhaengigkeitsregeln der Security-Rolle und
des Projekts.

## Produktionskonfiguration und Secrets

[MUST] Produktions-Secrets oder sensible Werte duerfen nicht in Chat, Issue,
Repository, Screenshots, Logs oder oeffentliche Nachweise uebertragen werden.

[MUST_IF] Eine Produktionskonfiguration projektspezifisch nur manuell durch den
Nutzer administriert werden darf, darf der Agent sie weder lesen noch
veraendern. Der Agent liefert stattdessen eine genaue Aenderungsanweisung:

- Variable hinzufuegen, ersetzen oder entfernen,
- sicherer Platzhalter statt Secret-Wert,
- belegte Quelle des einzusetzenden Werts,
- notwendiger Neustart oder Reload,
- sichere indirekte Verifikation ohne Ausgabe des Secrets.

[MUST] Der Agent setzt den betroffenen Deploymentpfad erst fort, nachdem der
Nutzer die manuelle Aktualisierung bestaetigt hat.

## Zielidentitaet vor produktiven Schreibzugriffen

[MUST] Vor Backup, Migration, Deployment oder einem anderen produktiven
Schreibzugriff muss der Agent die tatsaechliche Zielidentitaet mit
projektspezifisch belegten, moeglichst unabhaengigen Merkmalen verifizieren.
Je nach System gehoeren dazu Umgebung, Host oder Account, Dienst, Region,
Datenbank oder Datenspeicher, erwartete Struktur beziehungsweise
Sentinel-Ressourcen und aktuell laufende Version.

[MUST_NOT] Der Agent darf produktive Ziele, Datenbanknamen, Accounts,
Verzeichnisse oder Ressourcen nicht allein aus Projektname, Konvention,
Umgebungsvariable, veraltetem Chatkontext oder aehnlich klingenden Namen
ableiten.

[MUST_IF] Die Zielmerkmale fehlen, widerspruechlich sind oder nicht zum
freigegebenen Ziel passen, muss der Agent vor dem ersten Schreibzugriff stoppen.
Ein erfolgreiches Backup eines falschen oder unvollstaendigen Ziels gilt nicht
als gueltiger Wiederherstellungsnachweis.

## Projektlokale Automatisierung

[SHOULD] Wiederkehrende, fehleranfaellige Release-, Migrations-, Backup- und
Deploymentfolgen sollen durch ein projektlokales, versioniertes und
fail-closed Automationsskript oder einen gleichwertigen Workflow gekapselt
werden.

[MUST] Eine solche Automatisierung muss Parameter und Zielidentitaet
validieren, einen schreibfreien Plan oder Vorlauf ermoeglichen, bei Teilfehlern
abbrechen, sensible Ausgaben vermeiden und die erforderlichen Nachweise fuer
Backup, Migration, Version und Smokes liefern.

[MUST_NOT] Ein Automationsskript erweitert weder die Freigabe noch die
technischen Berechtigungen. Es darf keine ungeprueften Platzhalter, impliziten
Produktionsziele oder versteckten Secret-Zugriffe enthalten.

## Wiederaufnahme und Uebergabe

[MUST_IF] Der Ablauf in einem anderen Chat, Agenten, Worktree, Rechner oder
einer spaeteren Sitzung fortgesetzt wird, muss die Uebergabe Ziel, fuehrendes
Issue, Scope, Freigabestufe, nicht freigegebene Schritte, Arbeitsstand, Checks,
offene Entscheidungen, Stop-Bedingungen und naechste Empfehlung enthalten.

[MUST] Der uebernehmende Agent prueft die uebergebenen Angaben gegen die
fuehrenden Quellen und den aktuellen Zustand. Er setzt nur das bereits
eindeutig autorisierte Handlungspaket fort.

## Projektadapter

[MUST_IF] Ein Projekt diesen Workflow verwendet, muss seine `PROJECT.md` oder
fuehrende Projektdokumentation mindestens festlegen:

- welche Schritte das lokale Umsetzungspaket umfasst,
- welche DEV-Migrationen, Testdaten und Neustarts darin erlaubt sind,
- welche Git-, Review-, CI- und Merge-Gates gelten,
- welcher Security-Review fuer welche Risikoklassen erforderlich ist,
- welches Produktionspaket eine separate Freigabe abdeckt,
- ob der Agent Produktion selbst bedient oder nur eine Uebergabe erstellt,
- welche Konfigurationen oder Secrets ausschliesslich manuell bleiben,
- welche Health-, Smoke-, Monitoring- und Rollback-Nachweise erforderlich sind,
- wie jede Zielumgebung und jeder produktive Datenspeicher unabhaengig
  identifiziert wird,
- welcher schreibfreie Vorlauf vor produktiven Schreibzugriffen vorgesehen ist,
- welche projektlokalen Automationswege fuer Release, Backup, Migration,
  Deployment und Verifikation verbindlich oder bevorzugt sind,
- wie mehrere abgeschlossene Arbeitspakete zu einem belegten Release-Scope
  gebuendelt werden,
- welche Angaben eine wiederaufnehmbare Uebergabe enthalten muss.

[MUST] Bis ein spezifischer Widerspruch bewusst harmonisiert wurde, gilt die
engere Projekt- oder Plattformregel.

## Beispiel: Applikationsumsetzung

Der Nutzer sagt nach geklaertem Issue-Scope: `Setze Issue 42 um.` Der
Projektadapter kann dies als Umsetzungsfreigabe fuer einen frischen
Worktree, Code und Dokumentation, gezielte DEV-Schritte, automatisierte Checks,
angemeldete DEV-Abnahme, Commit, Push, Pull Request, CI-Korrekturen und Merge
definieren.

Der Agent dokumentiert Scope und Handlungspaket, arbeitet selbststaendig und
wendet wegen des Authentifizierungsbezugs den Security Reviewer an. Ein
unerwarteter produktiver Datenzugriff oder ein ungeklaertes hohes Finding stoppt
den Ablauf. Weder DEV-Abnahme noch Merge autorisieren einen Produktionsrelease.

## Beispiel: Produktion mit manuell administrierter Konfiguration

Der Nutzer sagt fuer einen belegten, geprueften Release:
`Release und Deployment freigegeben.` Der Projektadapter kann Backup, Tag,
Release, gezielte Produktionsmigrationen, Deployment und Verifikation erlauben.

Muss eine ausschliesslich manuell administrierte Produktions-Environment-Datei
geaendert werden, liefert der Agent nur die exakten Variablennamen, Operationen,
sicheren Platzhalter und Pruefschritte. Er liest oder aendert die Datei nicht und
wartet auf die Bestaetigung des Nutzers. Erst danach setzt er das freigegebene
Deployment fort.

## Abschlussnachweis

Der Abschluss nennt mindestens:

- normalisierte Freigabe, Datum, Scope und Handlungspaket,
- umgesetzte Aenderungen und relevante Entscheidungen,
- ausgefuehrte Tests, Reviews, Security-Ergebnis und Retests,
- Commit, Pull Request, Merge, Release oder Deployment, soweit ausgefuehrt,
- aktualisierte Dokumentation und Release Notes,
- externe Aktionen und manuell erledigte Voraussetzungen,
- nicht ausgefuehrte oder fehlgeschlagene Schritte,
- verbleibende Risiken, Blocker und Folgearbeit.

Danach nennt der Agent unter `Empfohlene nächste Schritte` eine kurze,
priorisierte Reihenfolge:

1. Ist der Stand releasefaehig, nennt er zuerst den konkreten Release- oder
   Deployment-Schritt und die dafuer noch erforderliche Freigabe.
2. Ist der Stand nicht releasefaehig, nennt er zuerst den belegten Blocker oder
   die fehlende Abnahme.
3. Anschliessend empfiehlt er die wertvollste durch fuehrende Quellen belegte
   Folgearbeit oder die wichtigsten offenen Backlog Items samt Abhaengigkeiten.

[MUST_NOT] Der Agent darf Empfehlungen nicht als bereits freigegebenen Scope
behandeln. Produktpriorisierung und neue Umsetzung bleiben getrennte
Entscheidungen.

[MUST] Der Agent meldet den Ablauf nur dann als abgeschlossen, wenn das
autorisierte Handlungspaket tatsaechlich abgeschlossen ist oder ein verbleibender
Blocker klar benannt wurde.
