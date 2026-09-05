# new-application.md

## Ziel

Dieser Workflow definiert den globalen Mindeststandard für neue Applikationen, die durch Agenten geplant, erstellt oder initialisiert werden.

Eine neue Applikation soll nicht nur ein technisches Gerüst sein, sondern eine lokal startbare, dokumentierte und prüfbare erste nutzbare Version.

## Verwenden

[MUST_IF] Dieser Workflow muss verwendet werden, wenn der Nutzer eine neue App, ein neues Tool, ein neues Dashboard, ein neues Portal, ein neues internes System oder ein neues Webprodukt erstellen lässt.

[MUST_IF] Dieser Workflow muss auch verwendet werden, wenn ein bestehender Prototyp in eine dauerhaft weiterentwickelbare Applikation überführt wird.

## Geltung und Einordnung

[MUST] Dieser Workflow gilt innerhalb der globalen Regeln aus [AGENTS.md](https://bastivonnijodex.github.io/agents/AGENTS.md).

[MUST] Der Agent muss die globale Prioritätslogik, Sicherheitsregeln, Dokumentationsregeln, Release-Regeln und projektspezifische `PROJECT.md`-Regeln weiterhin befolgen.

[MUST_NOT] Dieser Workflow darf globale Regeln nicht abschwächen, ersetzen oder umgehen.

[MUST_IF] Eine Regel in diesem Workflow mit globalen Regeln, Plattformvorgaben, Sicherheitsvorgaben oder projektspezifischen Regeln kollidiert, muss der Agent die höher priorisierte Regel anwenden und die Abweichung kurz benennen.

[MUST] Dieser Workflow definiert Mindeststandards für neue Applikationen. Er trifft keine endgültige Technologieentscheidung, wenn der Nutzer oder das Projekt bereits Vorgaben macht.

## Verwendete Workflows

[MUST_IF] Die App-Idee wesentliche offene Produktentscheidungen, mehrere
sinnvolle Lösungsrichtungen oder erhebliche Datenschutz-, Security-, Daten-,
Provider- oder Betriebsfolgen besitzt, muss vor der Umsetzung zusätzlich
[Produktkonzept erstellen und entscheiden](https://bastivonnijodex.github.io/agents/workflows/product-concept.md)
angewendet werden.

[MUST_IF] Commit, Tag, Push, Release Notes, Deployment oder eine produktionsnahe Übergabe relevant werden, muss zusätzlich [release.md](https://bastivonnijodex.github.io/agents/workflows/release.md) angewendet werden.

## Grundsatz

[MUST] Der Agent muss zuerst klären, was die Anwendung für den Nutzer leisten soll, wer sie nutzt und welcher Hauptworkflow auf dem ersten nutzbaren Stand funktionieren muss.

[MUST] Die erste Version muss einen realen Kernworkflow abbilden. Eine reine Landingpage, Platzhalter-App oder dekorative Demo ist nicht ausreichend, wenn der Nutzer eine Applikation verlangt.

[MUST] Die App muss so angelegt werden, dass ein anderer Agent später ohne Chat-Kontext weiterarbeiten kann.

## Mindest-Artefakte

[MUST] Eine neue Applikation muss mindestens diese Artefakte enthalten:

- `README.md` mit Zweck, Setup, Start, Build, Tests und wichtigsten Pfaden.
- `PROJECT.md` mit fachlichen und technischen Leitplanken.
- lokale `AGENTS.md`, die auf die globalen Agentenregeln verweist.
- `.gitignore` passend zum verwendeten Stack.
- dokumentierte Start-, Build- und Test-Kommandos.
- Beispiel- oder Platzhalterkonfiguration ohne echte Secrets, zum Beispiel `.env.example`.
- versionierte Lockfiles, soweit der verwendete Stack Abhängigkeiten auflöst.
- reproduzierbare Installations- und Startanweisungen.

[MUST_IF] Wenn das Projekt öffentlich oder gemeinsam entwickelt wird, müssen Issue-, Pull-Request- oder Übergaberegeln dokumentiert werden.

### Mindestinhalt der PROJECT.md

[MUST] Die `PROJECT.md` muss mindestens beschreiben:

- Produktziel, Zielgruppe, Scope und bewusste Nicht-Ziele.
- fachliche Source of Truth und verbindliche Produktregeln.
- Architektur, Technologieentscheidungen, unterstützte Plattformen und
  technische Grenzen.
- relevante Daten, Berechtigungen, Sicherheits- und Datenschutzanforderungen.
- lokale Entwicklung, Tests, Build und erforderliche Qualitätsprüfungen.
- Versionierung, Umgebungen, Release, Deployment, Migration und Rollback,
  soweit diese Aspekte bereits relevant oder entschieden sind.
- projektspezifische Definition of Done und ausdrücklich verbotene Aktionen.

[MUST] Noch offene Punkte müssen als offen oder nicht zutreffend gekennzeichnet
werden; sie dürfen nicht durch erfundene Regeln ersetzt werden.

## Produktklärung

[MUST] Vor der Umsetzung muss der Agent mindestens klären oder aus dem Nutzerauftrag ableiten:

- Ziel der Anwendung.
- Zielgruppe oder Nutzerrolle.
- wichtigster Hauptworkflow.
- wichtigste Datenobjekte.
- notwendige Authentifizierung oder Rollen.
- externe Integrationen.
- erwartete Ausgabe oder Erfolgskriterium.
- MVP, bewusste Nicht-Ziele und spätere Ausbaustufen.
- Zielplattformen und erwartete Betriebsumgebung.

[MUST_IF] Eine dieser Grundlagen unklar ist und eine falsche Annahme teuer, riskant oder schwer rückbaubar wäre, muss der Agent nachfragen.

[ALLOW_IF] Bei kleinen Prototypen darf der Agent plausible Annahmen treffen, muss sie aber dokumentieren.

## Technische Basis

[MUST] Der Agent muss einen Stack wählen, der zum Auftrag passt und mit vorhandenen Projektvorgaben vereinbar ist.

[MUST] Die App muss lokal startbar sein.

[MUST] Ein einziges dokumentiertes Kommando startet die vollständige lokale
Umgebung inklusive aller Abhängigkeiten wie Datenbank oder Cache und macht sie
über `localhost` erreichbar.

[MUST_IF] Fehlt eine Abhängigkeit, nennt dieses Kommando die konkreten
Installationsschritte für das vorgefundene System, statt mit einer technischen
Meldung abzubrechen.

[MUST_NOT] Der Agent darf für den lokalen Start keine Werkzeuge voraussetzen,
die nicht zur dokumentierten Grundausstattung gehören, und muss vorhandene
Werkzeuge prüfen, statt sie anzunehmen.

[MUST] Build- und Test-Kommandos müssen dokumentiert und soweit möglich ausgeführt werden.

[MUST] Persistenz, Authentifizierung, Uploads, AI-Funktionen und externe APIs dürfen nicht zufällig entstehen, sondern müssen bewusst entschieden und dokumentiert werden.

[MUST_NOT] Der Agent darf keine produktionsähnlichen Secrets, Tokens, privaten Schlüssel oder Zugangsdaten in das Repository schreiben.

[MUST] Neue Abhängigkeiten müssen einen belegbaren Nutzen besitzen und im
erforderlichen Umfang auf Wartungsstatus, Sicherheitslage und Lizenz geprüft
werden. Vorhandene Bordmittel und bereits etablierte Abhängigkeiten werden
bevorzugt, wenn sie den Zweck angemessen erfüllen.

[MUST] Unterstützte Runtime- und Tool-Versionen sowie Lockfiles müssen so
dokumentiert oder versioniert werden, dass Installation und Build
nachvollziehbar reproduzierbar sind.

[MUST_IF] Eine Architektur- oder Technologieentscheidung langfristige
Auswirkungen besitzt oder schwer rückbaubar ist, muss ihre Begründung in der
`PROJECT.md`, der Architekturdokumentation oder einem versionierten
Entscheidungsnachweis festgehalten werden.

## Repository-Hygiene

[MUST] `.gitignore`, Beispielkonfiguration und Repository-Inhalte müssen so
angelegt sein, dass lokale Secrets, Build-Ausgaben, Abhängigkeitsverzeichnisse
und temporäre Dateien nicht versehentlich versioniert werden.

[MUST_IF] CI für das Repository verfügbar oder Teil des Auftrags ist, müssen
die dokumentierten zentralen Tests, Builds und statischen Prüfungen dort
reproduzierbar ausführbar sein.

[MUST_IF] Fremder Code, Assets, Fonts, Modelle oder Datensätze eingebunden
werden, müssen Herkunft, Nutzungsrecht und erforderliche Lizenzhinweise geprüft
und dokumentiert werden.

[MUST] Generierter Code und generierte Assets unterliegen denselben
Qualitäts-, Sicherheits-, Lizenz- und Dokumentationsanforderungen wie manuell
erstellte Inhalte.

## UX/UI-Standard

[MUST] Die erste Ansicht muss den Hauptnutzen oder Hauptworkflow der App zeigen.

[MUST_NOT] Wenn der Nutzer eine App oder ein Tool verlangt, darf der Agent nicht nur eine Marketing-Landingpage bauen.

[MUST] Die App muss leere Zustände, Ladezustände und Fehlerzustände für zentrale Workflows berücksichtigen.

[MUST] Die App muss auf Desktop und Mobile grundsätzlich nutzbar sein, sofern der Auftrag keine andere Zielumgebung vorgibt.

[MUST] Texte, Labels und Aktionen müssen für die Zielgruppe verständlich sein.

[MUST] Zentrale Workflows müssen mit Tastatur bedienbar sein, verständliche
Beschriftungen und sichtbare Fokuszustände besitzen und dürfen wesentliche
Informationen nicht ausschließlich über Farbe vermitteln, sofern die
Zielplattform diese Anforderungen unterstützt.

[SHOULD] Kontraste, semantische Struktur und assistive Beschriftungen sollen
gegen den für das Projekt geltenden Barrierefreiheitsstandard geprüft werden.

## Release-Fähigkeit

[MUST] Jede neue App muss definieren, wie Versionen, Releases und Release Notes gepflegt werden.

[MUST_IF] Die App Nutzer hat oder später Nutzer haben soll, muss ein Ort oder Mechanismus für nutzerverständliche Update-Hinweise definiert werden, zum Beispiel ein Bereich „Neues Update“.

[MUST_IF] Eine Umsetzung getestet, abgenommen oder als abgeschlossen gemeldet wird und Nutzerwirkung hat, müssen Release Notes vorbereitet werden.

[MUST] Release Notes beschreiben sichtbaren Nutzen, geänderte Bedienung oder relevante fachliche Änderung.

## Sicherheit und Datenschutz

[MUST] Echte Secrets dürfen nicht committed werden.

[MUST] Benötigte Umgebungsvariablen müssen in einer Beispielkonfiguration ohne echte Werte dokumentiert werden.

[MUST_IF] Personenbezogene Daten, Uploads, AI-Verarbeitung, Webhooks oder externe Anbieter betroffen sind, müssen Datenschutz- und Sicherheitsgrenzen dokumentiert werden.

[MUST_IF] Die App Authentifizierung oder Rollen benötigt, müssen geschützte Bereiche und Rechte bewusst definiert werden.

[MUST_IF] Die App externe oder nicht vertrauenswürdige Eingaben verarbeitet,
müssen Validierung, Fehlerbehandlung und Schutz vor kontextrelevanten
Missbrauchsfällen berücksichtigt und geprüft werden.

[MUST_IF] Nutzer- oder personenbezogene Daten verarbeitet werden, müssen
Datensparsamkeit, Zweck, Aufbewahrung, Löschung, Export, Protokollierung,
Testdaten und beteiligte Drittanbieter im erforderlichen Umfang geklärt und
dokumentiert werden.

[MUST_NOT] Produktionsdaten dürfen nicht ungeprüft als lokale Entwicklungs-
oder Testdaten verwendet werden.

[MUST_IF] Das Projekt Abhängigkeits-, Secret- oder Security-Scans unterstützt,
müssen die für den Scope relevanten Prüfungen eingerichtet oder ausgeführt und
Befunde bewertet werden.

## Teststrategie und Definition of Done

[MUST] Die Teststrategie muss sich am Risiko der App orientieren und für den
zentralen Kernworkflow mindestens geeignete automatisierte oder begründete
manuelle Prüfungen definieren.

[MUST_IF] Fachlogik vorhanden ist, muss sie durch geeignete Unit- oder
Komponententests abgesichert werden.

[MUST_IF] Datenbank, APIs, externe Systeme oder mehrere Komponenten
zusammenwirken, müssen die kritischen Integrationen und Datenflüsse geprüft
werden.

[MUST_IF] Ein kritischer Nutzerweg über mehrere Schichten führt, muss ein
End-to-End- oder gleichwertiger Smoke Test vorhanden sein oder die Abweichung
mit ihrem Risiko dokumentiert werden.

[MUST_IF] Ein Fehler während der Entwicklung behoben wird, muss ein geeigneter
Regressionstest ergänzt oder die Abweichung begründet werden.

[MUST] Die projektspezifische Definition of Done muss mindestens erfüllte
Akzeptanzkriterien, erfolgreiche oder begründet ausgelassene Checks, aktuelle
Dokumentation, bewertete Security- und Datenschutzfolgen, Release-Auswirkungen
und nachvollziehbar erfasste Restarbeit berücksichtigen.

## Betrieb, Migration und Wiederherstellung

[MUST_IF] Die App dauerhaft oder produktionsnah betrieben werden soll, müssen
im erforderlichen Umfang strukturierte Logs ohne sensible Daten,
Fehlerüberwachung, Health Checks, zentrale Betriebsmetriken, Alarmierung,
Backup und Wiederherstellung definiert werden.

[MUST] Laufende Version und Umgebung müssen im Betrieb nachvollziehbar sein,
soweit ein Deployment vorgesehen ist.

[MUST_IF] Produktive Deployments oder Schreibzugriffe vorgesehen sind, muss das
Projekt dokumentieren, wie Zielumgebung, Account oder Host, Dienst,
Datenbank beziehungsweise Datenspeicher und erwartete Struktur vor der
Ausführung unabhängig verifiziert werden. Gleichnamige oder ähnlich benannte
DEV-, Test- und Produktionsressourcen müssen sicher unterscheidbar sein.

[SHOULD] Wiederkehrende Release-, Backup-, Migrations-, Deployment- und
Smoke-Test-Schritte sollen in einem projektlokalen, versionierten und
fail-closed Workflow zusammengefasst werden, der einen schreibfreien Vorlauf
und redigierte Nachweise unterstützt.

[MUST_IF] Datenmodell, persistierte Daten oder öffentliche Schnittstellen
geändert werden, müssen Rückwärtskompatibilität, Migrationspfad, Verhalten bei
Teilfehlern und Rollback oder Wiederherstellung vor der produktionsnahen
Ausführung geklärt und geprüft werden.

[MUST_NOT] Eine Migration oder ein Rollback darf allein aufgrund einer
theoretischen Beschreibung als verifiziert gelten.

## Checks

[MUST] Vor Übergabe muss der Agent mindestens prüfen:

- App startet lokal oder die Blockade ist dokumentiert.
- Build läuft oder die Blockade ist dokumentiert.
- zentrale Tests oder Smoke Checks laufen oder sind bewusst als offen dokumentiert.
- README und PROJECT.md sind vorhanden und aktuell.
- keine echten Secrets liegen im Repository.
- bekannte Risiken und offene Punkte sind benannt.
- kritische Nutzerwege und Integrationen sind angemessen geprüft.
- relevante Barrierefreiheits-, Sicherheits- und Datenschutzprüfungen sind
  gelaufen oder mit verbleibendem Risiko dokumentiert.
- für produktionsnahe Nutzung sind Betrieb, Migration, Backup,
  Wiederherstellung und Rollback geklärt.
- Abhängigkeiten, Lockfiles und Lizenzhinweise sind nachvollziehbar.

## Grenzen

[MUST_NOT] Der Agent darf keine fachlichen Domänenregeln, Statuswerte, Rollen oder Datenfelder erfinden, wenn sie für den Nutzer bindend sind.

[MUST_NOT] Der Agent darf keine externe Integration so darstellen, als sei sie produktionsbereit, wenn nur ein Mock, Platzhalter oder lokaler Test existiert.

[MUST_NOT] Der Agent darf Deployment, Hosting oder produktive Datenverarbeitung nicht voraussetzen, wenn der Nutzer diese Entscheidungen nicht getroffen hat.

## Endergebnis

[MUST] Eine neue Applikation gilt erst als sauber initialisiert, wenn sie lokal nachvollziehbar startbar, dokumentiert, prüfbar und für den nächsten Agenten ohne Chat-Kontext verständlich ist.

[MUST] Eine App darf erst als produktionsbereit bezeichnet werden, wenn die für
ihren tatsächlichen Einsatz relevanten Sicherheits-, Datenschutz-, Betriebs-,
Migrations-, Wiederherstellungs- und Rollback-Anforderungen nachweislich erfüllt
oder ausdrücklich als nicht zutreffend belegt sind.
