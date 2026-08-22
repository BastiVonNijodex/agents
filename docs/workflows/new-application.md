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

[MUST_IF] Wenn das Projekt öffentlich oder gemeinsam entwickelt wird, müssen Issue-, Pull-Request- oder Übergaberegeln dokumentiert werden.

## Produktklärung

[MUST] Vor der Umsetzung muss der Agent mindestens klären oder aus dem Nutzerauftrag ableiten:

- Ziel der Anwendung.
- Zielgruppe oder Nutzerrolle.
- wichtigster Hauptworkflow.
- wichtigste Datenobjekte.
- notwendige Authentifizierung oder Rollen.
- externe Integrationen.
- erwartete Ausgabe oder Erfolgskriterium.

[MUST_IF] Eine dieser Grundlagen unklar ist und eine falsche Annahme teuer, riskant oder schwer rückbaubar wäre, muss der Agent nachfragen.

[ALLOW_IF] Bei kleinen Prototypen darf der Agent plausible Annahmen treffen, muss sie aber dokumentieren.

## Technische Basis

[MUST] Der Agent muss einen Stack wählen, der zum Auftrag passt und mit vorhandenen Projektvorgaben vereinbar ist.

[MUST] Die App muss lokal startbar sein.

[MUST] Build- und Test-Kommandos müssen dokumentiert und soweit möglich ausgeführt werden.

[MUST] Persistenz, Authentifizierung, Uploads, AI-Funktionen und externe APIs dürfen nicht zufällig entstehen, sondern müssen bewusst entschieden und dokumentiert werden.

[MUST_NOT] Der Agent darf keine produktionsähnlichen Secrets, Tokens, privaten Schlüssel oder Zugangsdaten in das Repository schreiben.

## UX/UI-Standard

[MUST] Die erste Ansicht muss den Hauptnutzen oder Hauptworkflow der App zeigen.

[MUST_NOT] Wenn der Nutzer eine App oder ein Tool verlangt, darf der Agent nicht nur eine Marketing-Landingpage bauen.

[MUST] Die App muss leere Zustände, Ladezustände und Fehlerzustände für zentrale Workflows berücksichtigen.

[MUST] Die App muss auf Desktop und Mobile grundsätzlich nutzbar sein, sofern der Auftrag keine andere Zielumgebung vorgibt.

[MUST] Texte, Labels und Aktionen müssen für die Zielgruppe verständlich sein.

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

## Checks

[MUST] Vor Übergabe muss der Agent mindestens prüfen:

- App startet lokal oder die Blockade ist dokumentiert.
- Build läuft oder die Blockade ist dokumentiert.
- zentrale Tests oder Smoke Checks laufen oder sind bewusst als offen dokumentiert.
- README und PROJECT.md sind vorhanden und aktuell.
- keine echten Secrets liegen im Repository.
- bekannte Risiken und offene Punkte sind benannt.

## Grenzen

[MUST_NOT] Der Agent darf keine fachlichen Domänenregeln, Statuswerte, Rollen oder Datenfelder erfinden, wenn sie für den Nutzer bindend sind.

[MUST_NOT] Der Agent darf keine externe Integration so darstellen, als sei sie produktionsbereit, wenn nur ein Mock, Platzhalter oder lokaler Test existiert.

[MUST_NOT] Der Agent darf Deployment, Hosting oder produktive Datenverarbeitung nicht voraussetzen, wenn der Nutzer diese Entscheidungen nicht getroffen hat.

## Endergebnis

[MUST] Eine neue Applikation gilt erst als sauber initialisiert, wenn sie lokal nachvollziehbar startbar, dokumentiert, prüfbar und für den nächsten Agenten ohne Chat-Kontext verständlich ist.

