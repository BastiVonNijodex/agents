# Workflow: Agenten-Harness bewerten und projektbezogen ausgestalten

## Ziel

Dieser Workflow operationalisiert die allgemeinen Harness-Regeln aus
[AGENTS.md](https://bastivonnijodex.github.io/agents/AGENTS.md). Er führt zu
einer belegten Entscheidung, ob eine technische und organisatorische
Laufzeitumgebung für Agenten in einem bestimmten Projekt und Einsatzzweck
geeignet ist.

Bewertet wird das gesamte Harness aus Kontext, Regeln, Werkzeugen,
Berechtigungen, Zustand, Delegation, Schutzkontrollen und Nachweisen, nicht nur
ein Modell oder Prompt.

## Verwenden

Die verbindliche Aktivierung dieses Workflows ergibt sich aus
[AGENTS.md](https://bastivonnijodex.github.io/agents/AGENTS.md) und dem
[Workflow-Lookup](https://bastivonnijodex.github.io/agents/workflows/WORKFLOWS.md).
Nach der Aktivierung werden die folgenden Schritte für den betroffenen
Harness-Scope ausgeführt.

[MUST_IF] Eine bestehende Agentenumgebung neue Werkzeuge, Datenquellen,
Berechtigungen, Memory-Funktionen, Delegationswege oder extern wirksame
Handlungen erhält, müssen mindestens die betroffenen Schritte dieses Workflows
erneut ausgeführt werden.

[MUST_NOT] Eine gewöhnliche Aufgabe innerhalb eines bereits projektspezifisch
belegten Harnesses löst allein durch die Nutzung des Agenten keine vollständige
Neubewertung aus.

## Abgrenzung

[MUST] Dieser Workflow beschreibt Prüfschritte und Ergebnisnachweise. Die
verbindlichen Harness-Invarianten stehen in
[AGENTS.md](https://bastivonnijodex.github.io/agents/AGENTS.md) und werden hier
nicht erneut definiert.

[MUST] Projektspezifische Auswahl, technische Kontrollen und Betriebsgrenzen
werden in `PROJECT.md` oder der dort bestimmten führenden Dokumentation
festgelegt.

[MUST_IF] Wesentliche offene Produkt-, Daten-, Provider-, Security- oder
Betriebsentscheidungen entstehen, muss vor der Einführung zusätzlich der
Workflow
[Produktkonzept erstellen und entscheiden](https://bastivonnijodex.github.io/agents/workflows/product-concept.md)
angewendet werden.

## 1. Einsatz und Risikoklasse bestimmen

[MUST] Die Bewertung hält fest:

- Zweck, Nutzer und erwartete Ergebnisse,
- betroffene Produkte, Repositorien, Daten, Systeme und Umgebungen,
- führende menschliche Verantwortung,
- erlaubte und ausdrücklich ausgeschlossene Wirkungen,
- nach [AGENTS.md](https://bastivonnijodex.github.io/agents/AGENTS.md)
  aktivierte Risikospezialisierungen sowie
- zusätzlich anzuwendende Rollen und Workflows.

[ALLOW_IF] Die Prüftiefe darf für einen rein lesenden und reversiblen Einsatz
reduziert werden, wenn weder sensible oder personenbezogene Daten noch
produktive Systeme, produktive Daten, Secrets, externe Kommunikation oder
wesentliche Kosten betroffen sind.

## 2. Tatsächliches Harness erfassen

[MUST] Die Bestandsaufnahme erfasst im erforderlichen Umfang:

- beteiligte Agenten, Modelle und verantwortliche Menschen,
- System-, Nutzer-, Repository- und Projektanweisungen,
- Daten-, Wissens- und Memory-Quellen,
- Werkzeuge, Schnittstellen und ausführbare Kommandos,
- Berechtigungen, Bestätigungen und technische Zugriffsmöglichkeiten,
- Delegation an weitere Agenten oder Prozesse,
- persistenten und temporären Zustand,
- externe Anbieter und Vertrauensgrenzen sowie
- Protokoll-, Prüf- und Wiederaufnahmemöglichkeiten.

[MUST] Die Bestandsaufnahme unterscheidet belegte Eigenschaften, konfigurierte
Kontrollen, bloße Annahmen und noch nicht geprüfte Bereiche.

## 3. Regel- und Kontrollmatrix erstellen

[MUST] Für jede relevante Harness-Invariante aus
[AGENTS.md](https://bastivonnijodex.github.io/agents/AGENTS.md) wird eine Matrix
mit mindestens diesen Feldern erstellt:

| Feld | Inhalt |
|---|---|
| Anforderung | Verweis auf die konkrete globale oder projektspezifische Regel |
| technische Kontrolle | belegter Mechanismus oder `nicht technisch erzwungen` |
| organisatorische Kontrolle | erforderliche menschliche oder prozessuale Handlung |
| Evidenz | Konfiguration, Test, Protokoll oder anderer prüfbarer Nachweis |
| Lücke | fehlende oder nur teilweise erfüllte Kontrolle |
| Wirkung | betroffener Einsatz und mögliches Risiko |

[MUST] Die Matrix deckt mindestens die für den Einsatz relevanten Bereiche
Kontext, Freigaben, Werkzeuge, Zustand und Memory, Delegation,
Beobachtbarkeit, sicheres Fehlerverhalten sowie Regel- und
Konfigurationsstände ab.

## 4. Kontext-, Memory- und Datenflüsse abbilden

[MUST] Jede relevante Kontext-, Daten- oder Memory-Quelle wird mit folgenden
Angaben abgebildet:

- Herkunft und verantwortliche Stelle,
- Datenklasse und mögliche Schutzbedürftigkeit,
- Geltungsbereich nach Nutzer, Projekt, Task und Umgebung,
- Aktualitäts- und Konfliktprüfung,
- Lese-, Schreib-, Übertragungs- und Löschpfade,
- Aufbewahrung und Korrekturmöglichkeit sowie
- beteiligte externe Systeme oder Provider.

[MUST] Die Bewertung weist ausdrücklich nach, wie die globalen Verbote und
Datenschutzanforderungen für Secrets und personenbezogene Daten technisch oder
organisatorisch erfüllt werden.

## 5. Aktions- und Freigabematrix erstellen

[MUST] Für jede relevante Werkzeug- oder Aktionsklasse wird dokumentiert:

- technische Zugriffsmöglichkeit und tatsächliche Berechtigung,
- erforderliche fachliche Freigabe,
- Ziel- und Parameterprüfung,
- Reversibilität und mögliche Außenwirkung,
- erzeugter Nachweis sowie
- Stop- und Eskalationsbedingung.

[MUST] Fehlende Trennung oder technische Erzwingung wird als Lücke und nicht
als erfüllte Kontrolle bewertet.

## 6. Delegations- und Nachweismodell prüfen

[MUST_IF] Delegation vorgesehen ist, beschreibt die Bewertung für jeden
Delegationsweg:

- übergebenes Teilziel und Ergebnisformat,
- übertragene Quellen, Grenzen und Stop-Bedingungen,
- technische und fachliche Berechtigungen,
- erforderliche Unabhängigkeit oder Rollentrennung,
- Integration und Verifikation des Teilergebnisses sowie
- Verhalten bei Widerspruch, fehlender Evidenz oder Teilfehler.

[MUST] Das Nachweismodell benennt Speicherort, Aufbewahrung, Zugriff,
Redaktion sensibler Inhalte und die für Prüfung oder Wiederaufnahme benötigten
Aktions-, Entscheidungs-, Fehler- und Testergebnisse.

## 7. Eval- und Fehlerfallplan erstellen

[MUST] Der Eval-Plan leitet seine Fälle aus Einsatz, Vertrauensgrenzen,
Kontrollmatrix und aktivierten Risikospezialisierungen ab.

[MUST] Als wiederverwendbarer Ausgangspunkt wird die Baseline aus
[EVALS.md](https://bastivonnijodex.github.io/agents/EVALS.md) verwendet. Das
Profil `general` gilt immer; `coding` und `production` werden bei aktivierter
Spezialisierung additiv ausgeführt und um projektspezifische Fälle ergänzt.

Er enthält im erforderlichen Umfang:

- erwartete Erfolgsfälle,
- verweigerte oder fehlende Freigaben,
- falsche, unvollständige und veraltete Kontextquellen,
- widersprüchliche oder manipulierte Anweisungen,
- unzulässige Ziele, Parameter und Berechtigungsüberschreitungen,
- unerlaubte Speicherung und taskübergreifenden Abruf sensibler Inhalte,
- Delegations-, Replay-, Race- und Teilfehlerszenarien,
- Abbruch, Wiederaufnahme und Wiederherstellung sowie
- Regressionen nach wesentlichen Harness- oder Regeländerungen.

[MUST] Jeder erforderliche Fall erhält erwartetes Verhalten, Testweg,
Ergebnisnachweis und eine Einordnung fehlender Prüfbarkeit.

[MUST] Ein maschinenlesbar erfolgreicher Lauf belegt nur den Vergleich mit dem
Fallkatalog. Die Abschlussbewertung erfordert zusätzlich die inhaltliche
Prüfung der Kontrollmatrix und Evidenz; synthetische Referenzergebnisse gelten
nicht als Eignungsnachweis.

## 8. Regel- und Konfigurationsstand belegen

[MUST] Die Bewertung dokumentiert:

- den wirksamen Regel- und Harness-Konfigurationsstand,
- den projektspezifischen Update-Modus,
- verantwortliche Freigabe- und Änderungsinstanzen,
- Kompatibilitäts- und Migrationsfolgen,
- erneut auszuführende Evals sowie
- den Umgang mit sicherheitsrelevanten Aktualisierungen.

[MUST_IF] Globale Regeln aus diesem Repository verwendet werden, enthält der
Nachweis zusätzlich die SemVer-Regelversion, den vollständigen Commit-SHA, die
unveränderliche Regelquelle und den projektspezifischen Update-Modus nach
[VERSIONING.md](https://bastivonnijodex.github.io/agents/VERSIONING.md).

## 9. Coding-Spezialisierung auswerten

[MUST_IF] Die Coding-Spezialisierung nach
[AGENTS.md](https://bastivonnijodex.github.io/agents/AGENTS.md) aktiviert ist,
muss die Bewertung zusätzlich die projektspezifischen Nachweise für folgende
Bereiche zusammenführen:

- führendes Repository, Projektregeln, Issue und bestätigter Scope,
- Branch-, Worktree-, Datei-, Kommando- und Netzwerkzugriffe,
- bestehender und fremder Arbeitsstand,
- Abhängigkeits-, Schema- und Konfigurationsänderungen,
- Tests, Builds, Lints, Reviews und Security-Prüfungen,
- Commit, Push, Pull Request, Merge und Release sowie
- Übergabe, Wiederaufnahme und Definition of Done.

## 10. Produktionsspezialisierung auswerten

[MUST_IF] Die Produktionsspezialisierung nach
[AGENTS.md](https://bastivonnijodex.github.io/agents/AGENTS.md) aktiviert ist,
muss die Bewertung zusätzlich die projektspezifischen Nachweise für folgende
Bereiche zusammenführen:

- unabhängige Zielidentität und erwartete Sentinel-Merkmale,
- getrennte Identitäten und produktive Berechtigungen,
- Produktionspaket und schreibfreier Vorlauf,
- Secrets und manuell administrierte Konfiguration,
- Backup, Migration, Teilfehler und Wiederherstellung,
- Deployment, Health, Smokes, Monitoring und Logs,
- Abbruch und Rollback sowie
- menschliche Betriebs- und Risikoentscheidung.

[MUST] Die Abschlussbewertung übernimmt die strengste Freigabewirkung aus den
zusätzlich aktivierten Security-, Autopilot- und Release-Regeln.

## 11. Projektadapter dokumentieren

[MUST] Die belegte Harness-Ausgestaltung wird in `PROJECT.md` oder der dort
bestimmten führenden Dokumentation festgehalten. Sie muss ohne ursprünglichen
Chat auf Kontrollmatrix, Evals, offene Lücken, aktivierte
Risikospezialisierungen und Auslöser einer Neubewertung verweisen oder diese
Informationen selbst enthalten.

## 12. Bewertung und Abschluss

Die Bewertung verwendet genau eine der folgenden Aussagen:

- `geeignet`: Alle für den vorgesehenen Einsatz erforderlichen Regeln,
  Kontrollen und Nachweise sind belegt.
- `bedingt geeignet`: Der Einsatz ist nur innerhalb ausdrücklich benannter
  Grenzen vertretbar; Restpunkte, Verantwortliche und Bedingungen sind
  dokumentiert.
- `nicht geeignet`: Ein erforderlicher Schutz, eine Freigabe oder ein Nachweis
  fehlt und der vorgesehene Einsatz muss unterbleiben.

[MUST] Der Abschluss nennt:

- vorgesehenen Einsatz und Risikoklasse,
- geprüfte Komponenten und Vertrauensgrenzen,
- verwendete Quellen und ausgeführte Prüfungen,
- erfüllte und fehlende Kontrollen,
- Bewertung mit Begründung,
- verbleibende Risiken, Verantwortliche und Folgearbeit sowie
- Auslöser für eine erneute Bewertung.

[MUST_NOT] `geeignet` darf nicht vergeben werden, wenn eine zwingende
Freigabe, Zielidentität, Schutzkontrolle oder erforderliche Prüfevidenz für den
vorgesehenen Einsatz fehlt.
