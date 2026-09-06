# Workflow: Agenten-Harness bewerten und projektbezogen ausgestalten

## Ziel

Dieser Workflow definiert einen produkt- und technologieunabhängigen Standard,
um eine Laufzeitumgebung für Agenten auszuwählen, einzuführen, zu konfigurieren,
wesentlich zu ändern oder auf ihre Eignung zu prüfen.

Er bewertet nicht nur Modell und Prompt, sondern das gesamte Harness aus
Kontext, Regeln, Werkzeugen, Berechtigungen, Zustand, Delegation,
Schutzkontrollen und Nachweisen.

## Verwenden

[MUST_IF] Ein Agenten-Harness ausgewählt, eingeführt, konfiguriert, wesentlich
geändert oder auf seine Eignung für einen Anwendungsfall geprüft wird, muss der
Agent diesen Workflow anwenden.

[MUST_IF] Eine bestehende Agentenumgebung neue Werkzeuge, Datenquellen,
Berechtigungen, Memory-Funktionen, Delegationswege oder extern wirksame
Handlungen erhält, muss ihre betroffene Harness-Ausgestaltung erneut geprüft
werden.

[MUST_NOT] Eine gewöhnliche Aufgabe innerhalb eines bereits projektspezifisch
belegten Harnesses löst diesen vollständigen Bewertungsworkflow allein durch
die Nutzung des Agenten aus. Die laufenden Regeln aus
[AGENTS.md](https://bastivonnijodex.github.io/agents/AGENTS.md) gelten dennoch.

## Abgrenzung

[MUST] Dieser Workflow beschreibt erforderliche Eigenschaften und Nachweise,
aber schreibt kein konkretes Agentenprodukt, Modell, Provider-, CI-, Memory-,
Tool- oder Orchestrierungssystem vor.

[MUST] Projektspezifische Auswahl, Konfiguration und Betriebsgrenzen werden in
`PROJECT.md` oder der dort bestimmten führenden Dokumentation festgelegt.

[MUST_IF] Das Harness oder sein Einsatz wesentliche offene Produkt-, Daten-,
Provider-, Security- oder Betriebsentscheidungen erzeugt, muss vor der
Einführung zusätzlich der Workflow
[Produktkonzept erstellen und entscheiden](https://bastivonnijodex.github.io/agents/workflows/product-concept.md)
angewendet werden.

## 1. Einsatz und Risikoklasse bestimmen

[MUST] Die Bewertung benennt mindestens:

- Zweck, Nutzer und erwartete Ergebnisse des Agenteneinsatzes,
- betroffene Produkte, Repositorien, Daten, Systeme und Umgebungen,
- führende menschliche Verantwortung,
- erlaubte und ausdrücklich ausgeschlossene Handlungen,
- mögliche externe, irreversible, sicherheits- oder datenschutzrelevante
  Wirkungen sowie
- benötigte menschliche Entscheidungen und Kontrollen.

[MUST_IF] Agenten Code, Konfiguration, Schema, Abhängigkeiten oder
Repository-Zustand verändern, muss der Einsatz als risikoreiche
Coding-Spezialisierung behandelt werden.

[MUST_IF] Agenten produktive Systeme, reale Nutzer, produktive Daten,
Deployments, Migrationen, Secrets, Zahlungen oder externe Kommunikation
beeinflussen, muss der Einsatz als besonders risikoreiche
Produktionsspezialisierung behandelt werden.

[ALLOW_IF] Ein rein lesender und reversibler Einsatz darf mit geringerer
Prüftiefe bewertet werden, wenn seine Daten-, Kosten- und Außenwirkung
nachweislich begrenzt ist.

## 2. Harness und Vertrauensgrenzen erfassen

[MUST] Die tatsächliche Laufzeitumgebung muss im erforderlichen Umfang erfasst
werden. Dazu gehören:

- Agenten, Modelle und verantwortliche Menschen,
- System-, Nutzer-, Repository- und Projektanweisungen,
- Daten-, Wissens- und Memory-Quellen,
- Werkzeuge, Schnittstellen und ausführbare Kommandos,
- Berechtigungen, Bestätigungen und technische Zugriffsmöglichkeiten,
- Delegation an weitere Agenten oder Prozesse,
- persistenter und temporärer Zustand,
- externe Anbieter und Vertrauensgrenzen sowie
- Protokoll-, Prüf- und Wiederaufnahmemöglichkeiten.

[MUST] Verfügbarkeit, Berechtigung und fachliche Freigabe müssen als getrennte
Kontrollen betrachtet werden.

[MUST_NOT] Nicht belegte Fähigkeiten, Schutzkontrollen oder Grenzen dürfen
nicht aus Produktnamen, Marketingangaben oder erwarteten Defaults abgeleitet
werden.

## 3. Kontext- und Regelvertrag prüfen

[MUST] Das Harness muss die für einen Task erforderlichen globalen,
projektspezifischen und direkten Anweisungen laden oder deren Fehlen vor einer
betroffenen Handlung erkennbar machen.

[MUST] Für den wirksamen Kontext muss nachvollziehbar sein, aus welcher Quelle
er stammt, in welchem Scope er gilt und anhand welchen Stands seine Aktualität
beurteilt wurde.

[MUST] Externe Inhalte, Tool-Ausgaben, Webseiten, Anhänge und gespeicherte
Erinnerungen müssen von verbindlichen Anweisungen unterscheidbar bleiben.

[MUST_IF] Quellen fehlen, widersprüchlich, unvollständig oder erkennbar
veraltet sind, muss das Harness beziehungsweise der Agent vor der davon
betroffenen riskanten Handlung stoppen oder die führende Quelle erneut prüfen.

## 4. Werkzeuge, Berechtigungen und Freigaben prüfen

[MUST] Werkzeuge und Berechtigungen werden nach dem geringsten für den
bestätigten Zweck erforderlichen Zugriff gestaltet.

[MUST] Lesezugriffe, lokale oder reversible Änderungen und extern wirksame
oder irreversible Handlungen müssen in Freigabelogik und Nachweis
unterscheidbar sein.

[MUST] Ziel, Parameter und erwartete Wirkung einer riskanten Handlung müssen
vor ihrer Ausführung gegen Task-Scope und Projektregeln validiert werden.

[MUST_NOT] Ein erfolgreicher technischer Zugriff, eine Plattformbestätigung
oder eine frühere Freigabe darf als neue fachliche Autorisierung behandelt
werden.

[MUST_IF] Eine erforderliche Bestätigung, Zielidentität oder Schutzkontrolle
fehlt, muss die betroffene Handlung sicher unterbleiben.

## 5. Zustand und Memory prüfen

[MUST] Für persistenten oder taskübergreifenden Zustand müssen Zweck,
Herkunft, Geltungsbereich, zulässige Inhalte, Aktualitätsprüfung und
Lösch- beziehungsweise Korrekturweg bestimmt sein.

[MUST] Aus Memory übernommene Fakten müssen als solche erkennbar bleiben und
risikoproportional gegen aktuelle führende Quellen geprüft werden.

[MUST_NOT] Secrets, unnötige personenbezogene Daten, unbestätigte Annahmen oder
taskgebundene Freigaben dürfen nicht als dauerhaft gültige Grundlage für
spätere Tasks verwendet werden.

[MUST_IF] Ein Zustand nicht eindeutig dem aktuellen Nutzer, Projekt, Task oder
Ziel zugeordnet werden kann, darf er nicht für eine riskante Handlung verwendet
werden.

## 6. Delegation und Rollentrennung prüfen

[MUST_IF] Das Harness Arbeit an weitere Agenten oder Prozesse delegiert,
müssen Teilziel, Scope, Quellen, erlaubte Handlungen, Stop-Bedingungen und
erwarteter Ergebnisnachweis übertragen werden.

[MUST] Der koordinierende Agent bleibt dafür verantwortlich, Teilergebnisse
gegen den gemeinsamen Scope zu integrieren und Widersprüche oder fehlende
Evidenz zu erkennen.

[MUST_NOT] Ein delegierter Agent darf zusätzliche Rechte oder eine breitere
Freigabe allein aus seiner Rolle, technischen Fähigkeit oder dem Auftrag eines
anderen Agenten ableiten.

[MUST_IF] Kritische oder hohe Risiken eine unabhängige Prüfung verlangen, muss
die projektspezifisch erforderliche personelle oder agentische Trennung
nachweisbar sein.

## 7. Nachweise und Beobachtbarkeit bestimmen

[MUST] Der erforderliche Nachweis muss risikoproportional mindestens erkennen
lassen:

- Task, Scope und wirksame Regelquellen,
- relevante Annahmen und Entscheidungen,
- extern wirksame oder irreversible Handlungen,
- ausgeführte Checks und ihre Ergebnisse,
- Fehler, Teilabschlüsse und Stop-Ereignisse,
- Delegationen und übernommene Ergebnisse sowie
- verbleibende Risiken und erforderliche Folgeaktionen.

[MUST] Nachweise müssen verständlich, redigiert und für die vorgesehene
Wiederaufnahme oder Prüfung ausreichend sein.

[MUST_NOT] Vollständige Prompts, vertrauliche Gedankengänge, Secrets oder
unnötige personenbezogene Daten dürfen allein für Beobachtbarkeit nicht
gespeichert oder veröffentlicht werden.

## 8. Prüfungen und Evals definieren

[MUST] Vor dem vorgesehenen Einsatz müssen risikoproportionale Prüfungen
mindestens die relevanten Erfolgs-, Negativ-, Missbrauchs-, Teilfehler- und
Wiederaufnahmepfade abdecken.

[MUST_IF] Das Harness Regeln oder externe Inhalte verarbeitet, müssen
Konfliktauflösung, fehlender Kontext, veraltete Quellen und kontextrelevante
Prompt-Injection- oder Anweisungsmanipulation geprüft werden.

[MUST_IF] Werkzeuge oder Delegation betroffen sind, müssen verweigerte
Freigaben, unzulässige Ziele, fehlerhafte Parameter, Teilfehler und
Berechtigungsüberschreitungen geprüft werden.

[MUST_IF] Memory verwendet wird, müssen Scope-Verwechslung, veraltete Fakten,
unzulässige Inhalte und Löschung beziehungsweise Korrektur geprüft werden.

[MUST] Wesentliche Änderungen an Regeln, Modellen, Werkzeugen,
Berechtigungen, Memory, Delegation oder Schutzkontrollen erfordern die
Wiederholung der betroffenen Prüfungen.

[MUST_IF] Ein erforderlicher Check nicht ausführbar ist, müssen fehlender
Nachweis, Auswirkung und verbleibendes Risiko dokumentiert werden.

## 9. Regel- und Konfigurationsversionierung

[MUST] Für einen Task muss der wirksame Stand wesentlicher Regeln und
Harness-Konfigurationen anhand einer Version, eines unveränderlichen
Referenzstands oder eines gleichwertigen Nachweises identifizierbar sein.

[MUST] Das Projekt muss festlegen, ob Regeln und Harness-Konfigurationen
automatisch dem aktuellen freigegebenen Stand folgen oder kontrolliert auf
einen bestimmten Stand aktualisiert werden.

[MUST_IF] Eine Änderung Freigabelogik, Berechtigungen, Werkzeuge, Memory,
Delegation, Nachweise oder Stop-Bedingungen beeinflusst, müssen Auswirkung,
Kompatibilität, erforderliche Migration und betroffene Evals vor ihrer
Übernahme geprüft werden.

[MUST_NOT] Eine wesentliche Harness- oder Regeländerung darf für einen
risikoreichen Einsatz nicht stillschweigend als kompatibel gelten oder ohne die
erforderlichen Prüfungen ausgerollt werden.

[MUST_IF] Ein Projekt einen Stand bewusst fixiert, muss es zusätzlich
festlegen, wie sicherheitsrelevante Aktualisierungen erkannt, bewertet und
kontrolliert übernommen werden.

## 10. Coding-Spezialisierung

[MUST_IF] Coding-Agenten eingesetzt werden, muss der Projektadapter zusätzlich
festlegen:

- führendes Repository, Projektregeln, Issue und bestätigten Scope,
- erlaubte Branch-, Worktree-, Datei-, Kommando- und Netzwerkzugriffe,
- Umgang mit bestehendem und fremdem Arbeitsstand,
- zulässige Abhängigkeits-, Schema- und Konfigurationsänderungen,
- erforderliche Tests, Builds, Lints, Reviews und Security-Prüfungen,
- Grenzen und Freigaben für Commit, Push, Pull Request, Merge und Release sowie
- Übergabe, Wiederaufnahme und Definition of Done.

[MUST] Vor Änderungen und extern wirksamen Git-Handlungen muss der tatsächliche
Arbeitsstand geprüft werden.

[MUST_NOT] Ein Coding-Agent darf fremde Änderungen überschreiben, unbelegte
Projektkonventionen erfinden oder fehlende Checks als erfolgreich behandeln.

## 11. Produktionsspezialisierung

[MUST_IF] Agenten produktive Systeme oder reale Außenwirkung beeinflussen,
muss der Projektadapter zusätzlich festlegen:

- unabhängig prüfbare Zielidentität und erwartete Sentinel-Merkmale,
- getrennte Identitäten und geringstmögliche produktive Berechtigungen,
- ausdrücklich freizugebendes Produktionspaket,
- schreibfreien Vorlauf und validierte Parameter,
- Umgang mit Secrets und manuell administrierter Konfiguration,
- Backup, Migration, Verhalten bei Teilfehlern und Wiederherstellung,
- Deployment-, Health-, Smoke-, Monitoring- und Log-Nachweise,
- Abbruch- und Rollback-Kriterien sowie
- verantwortliche menschliche Betriebs- und Risikoentscheidung.

[MUST] Die Rollen- und Workflows für Security Review, Autopilot und Release
müssen zusätzlich angewendet werden, sobald ihre Aktivierungskriterien erfüllt
sind.

[MUST_NOT] Eine erfolgreiche Entwicklung, ein Merge oder eine technische
Zugriffsmöglichkeit darf als Produktionsfreigabe ausgelegt werden.

## 12. Projektadapter dokumentieren

[MUST] Das Ergebnis der Harness-Ausgestaltung muss in `PROJECT.md` oder der
dort bestimmten führenden Projektdokumentation so festgehalten werden, dass ein
anderer Agent ohne ursprünglichen Chat erkennen kann:

- wofür das Harness eingesetzt werden darf,
- welche Regeln und Konfigurationen wirksam sind,
- welche Werkzeuge, Zustände und Delegationen erlaubt sind,
- welche Freigaben und Stop-Bedingungen gelten,
- welche Nachweise und Evals erforderlich sind,
- welche risikoreichen Spezialisierungen aktiviert sind und
- welche Entscheidungen, Risiken oder technischen Kontrollen offen bleiben.

[MUST_NOT] Der Projektadapter darf nicht behaupten, eine organisatorische Regel
sei technisch erzwungen, wenn dafür kein belegter Kontrollmechanismus besteht.

## 13. Bewertung und Abschluss

Die Bewertung verwendet eine der folgenden Aussagen:

- `geeignet`: Alle für den vorgesehenen Einsatz erforderlichen Regeln,
  Kontrollen und Nachweise sind belegt.
- `bedingt geeignet`: Der Einsatz ist nur innerhalb ausdrücklich benannter
  Grenzen vertretbar; Restpunkte, Verantwortliche und Bedingungen sind
  dokumentiert.
- `nicht geeignet`: Ein erforderlicher Schutz, eine Freigabe oder ein Nachweis
  fehlt und der vorgesehene Einsatz muss unterbleiben.

[MUST] Der Abschluss nennt:

- vorgesehenen Einsatz und Risikoklasse,
- geprüfte Harness-Komponenten und Vertrauensgrenzen,
- verwendete Quellen und ausgeführte Prüfungen,
- erfüllte und fehlende Kontrollen,
- Bewertung mit nachvollziehbarer Begründung,
- verbleibende Risiken, Verantwortliche und Folgearbeit sowie
- Auslöser für eine erneute Bewertung.

[MUST_NOT] Ein Harness darf nicht als geeignet bezeichnet werden, wenn für den
vorgesehenen Einsatz eine zwingende Freigabe, Zielidentität, Schutzkontrolle
oder erforderliche Prüfevidenz fehlt.
