# Workflow: Backlog Item erstellen und verfeinern

## Zweck

Dieser Workflow definiert einen produktübergreifenden Mindeststandard für
Backlog Items. Ein fertiges Item muss ohne den ursprünglichen Chat verständlich,
fachlich belastbar, klar abgegrenzt und prüfbar sein.

Projektspezifische Regeln bestimmen das konkrete Backlog-System, die Source of
Truth, Labels, Statuswerte, Boards, Prioritäten und Freigaben.

## Ablauf

### 1. Produktkontext bestimmen

[MUST] Vor der Formulierung muss der Agent das aktuelle Produkt und seine
führenden Quellen aus dem Repository-, Projekt- und Nutzerkontext bestimmen.

[MUST] Relevante Produktdokumentation, bestehendes Verhalten und belegte
fachliche oder technische Regeln müssen geprüft werden.

### 2. Bestand und Zusammenhänge prüfen

[MUST] Der Agent muss nach bestehenden oder überschneidenden Issues,
Entscheidungen, Funktionen und bekannten Einschränkungen suchen, soweit das
Backlog-System und der aktuelle Zugriff dies erlauben.

[MUST] Erkannte Abhängigkeiten, betroffene Produktbereiche, Datenflüsse,
Berechtigungen, Schnittstellen und Dokumentations- oder Release-Auswirkungen
müssen im erforderlichen Umfang berücksichtigt werden.

### 3. Produktentscheidung klären

[MUST_IF] Eine offene Entscheidung Ziel, Nutzen, Scope, Bedienung, Priorität oder
Risiko wesentlich verändert, muss vor dem finalen Backlog Item ein
Entscheidungsentwurf mit Ausgangslage, Optionen, Auswirkungen und begründeter
Empfehlung vorgelegt werden.

[ALLOW_IF] Ein Backlog Item darf offene Fragen enthalten, wenn sie die
Umsetzbarkeit nicht verhindern und ausdrücklich als offene Frage oder Blocker
gekennzeichnet sind.

### 4. Backlog Item formulieren

[MUST] Der Titel beschreibt knapp das fachliche Ziel oder das beobachtete
Problem. Ein technischer Lösungsweg gehört nur dann in den Titel, wenn genau
dieser Weg belegt und Teil des freigegebenen Scopes ist.

[MUST] Das Item verwendet die folgende Struktur. Nicht relevante Unterpunkte
dürfen knapp als nicht zutreffend gekennzeichnet werden; verpflichtende
Informationen dürfen nicht durch leere Überschriften ersetzt werden.

```md
## Ziel

Welcher fachliche oder technische Zustand soll nach Abschluss erreicht sein?

## Kontext und Nutzen

Warum wird das Item benötigt, welches Problem wird gelöst und wer profitiert?

## Anforderungen

- Konkrete fachliche oder technische Anforderungen
- Relevante Regeln, Randbedingungen und erwartetes Verhalten
- Wichtige Fehler-, Leer- und Grenzfälle

## Akzeptanzkriterien

- [ ] Beobachtbare und prüfbare Bedingung
- [ ] Relevanter Fehler- oder Grenzfall
- [ ] Bestehendes Verhalten bleibt erhalten, soweit keine Änderung beschrieben ist

## Scope

### Enthalten

- Ausdrücklich enthaltene Arbeit

### Nicht enthalten

- Bewusst ausgeschlossene Arbeit

## Abhängigkeiten und Auswirkungen

- Betroffene Produktbereiche oder Module
- Verwandte oder blockierende Issues
- Auswirkungen auf Daten, Schnittstellen, Berechtigungen oder Workflows
- Dokumentations- oder Release-Auswirkungen

## Checks

- Erwartete automatisierte Prüfungen
- Erforderliche manuelle Abnahme
- Relevante Rollen, Ansichten, Endgeräte oder Umgebungen

## Relevante Quellen

- Produktdokumentation, Code, Schema oder Schnittstellen
- Screenshots, Fehlermeldungen oder sonstige Belege
- Verwandte Issues und dokumentierte Entscheidungen

## Risiken und offene Fragen

- Bekannte Risiken, offene Entscheidungen, externe Abhängigkeiten oder Blocker
```

### 5. Typspezifische Angaben ergänzen

[MUST_IF] Bei einem Bug müssen beobachtetes Verhalten, erwartetes Verhalten und
reproduzierbare Ausgangsbedingungen enthalten sein, soweit sie bekannt oder
ermittelbar sind.

[MUST_IF] Bei technischer Schuld müssen der belegte Ist-Zustand, das konkrete
Risiko oder die Kosten des Fortbestands und der angestrebte Zielzustand enthalten
sein.

[MUST_IF] Bei sicherheits-, datenschutz-, migrations- oder produktionsrelevanter
Arbeit müssen die projektspezifischen Freigaben, Schutzmaßnahmen und
Verifikationsanforderungen berücksichtigt werden.

### 6. Metadaten und Ablage

[MUST] Typ, Priorität, Produktbereich, Status, Verantwortlichkeit und
Issue-Beziehungen werden nach den belegten Regeln des jeweiligen Projekts
gesetzt. Fehlende Werte dürfen nicht erfunden werden.

[MUST_IF] Der Nutzer die Erstellung des Issues beauftragt hat und der Agent
Schreibzugriff auf das autorisierte Backlog-System besitzt, muss das Item dort
erstellt oder aktualisiert werden. Andernfalls wird ein vollständiger,
kopierbarer Entwurf geliefert.

## Definition of Ready

Ein Backlog Item ist nur `Ready`, wenn:

- Ziel und Nutzen ohne Chat-Kontext verständlich sind,
- der relevante Produktbestand und mögliche Doppelungen geprüft wurden,
- Anforderungen und Akzeptanzkriterien beobachtbar und prüfbar sind,
- Scope und Nicht-Scope ausreichend abgegrenzt sind,
- bekannte Abhängigkeiten, Auswirkungen und Risiken genannt sind,
- offene Entscheidungen geklärt oder ausdrücklich als Blocker markiert sind,
- relevante Quellen verlinkt oder eindeutig benannt sind,
- keine unbelegten Produkt- oder Technikbehauptungen enthalten sind und
- ein anderer Agent oder Entwickler das Item eigenständig aufnehmen kann.

## Abschlussnachweis und Definition of Done

[MUST_IF] Ein Backlog Item als abgeschlossen gemeldet oder geschlossen werden
soll, muss der Abschlussnachweis mindestens die Umsetzung oder Entscheidung,
die ausgeführten Checks, die aktualisierte oder nicht betroffene Dokumentation,
verbleibende Risiken und den Abnahmestatus nennen.

Empfohlene Struktur:

```md
## Abschlussnachweis

- Umsetzung oder Entscheidung: <Commit, Pull Request oder Dokumentation>
- Erfüllte Akzeptanzkriterien: <Ergebnis>
- Ausgeführte Checks: <Kommandos und Ergebnis>
- Dokumentation und Release Notes: <aktualisiert oder nicht betroffen>
- Offene Risiken oder Folge-Issues: <Verweise oder keine>
- Abnahmestatus: <Status und belegte Freigabe>
```

Ein Item ist nur `Done`, wenn seine Akzeptanzkriterien erfüllt, erforderliche
Checks ausgeführt oder begründet, notwendige Dokumentation berücksichtigt und
verbleibende Arbeit als Folge-Issue erfasst oder ausdrücklich aus dem Scope
ausgeschlossen ist.
