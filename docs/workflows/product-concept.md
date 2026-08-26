# Workflow: Produktkonzept erstellen und entscheiden

## Zweck

Dieser Workflow definiert produktübergreifend, wie eine Idee vor ihrer
Umsetzung untersucht, dokumentiert, entschieden und in umsetzbare Backlog Items
überführt wird.

Ein Konzept ist weder automatisch ein umsetzungsreifes Backlog Item noch
implementierte Produktwahrheit. Es dokumentiert Problem, Nutzen, Optionen,
Auswirkungen und die Product-Owner-Entscheidung.

## Abgrenzung zum Backlog Item

[MUST_IF] Ziel, Nutzen, Scope und fachliches Verhalten bereits eindeutig sind
und keine materielle Produktentscheidung offen ist, muss direkt der Workflow
[Backlog Item erstellen und verfeinern](https://bastivonnijodex.github.io/agents/workflows/backlog-item.md)
verwendet werden.

[MUST_IF] Eine Idee mehrere sinnvolle Lösungsrichtungen, wesentliche offene
Produktentscheidungen, mehrere Produktbereiche oder erhebliche Datenschutz-,
Security-, Daten-, Provider- oder Betriebsfolgen besitzt, muss sie zuerst als
Produktkonzept behandelt werden.

[MUST_NOT] Ein angenommenes Konzept darf ohne Umsetzung und Verifikation als
bereits gültiges Produktverhalten dokumentiert oder kommuniziert werden.

## Ablage und Nachverfolgbarkeit

[MUST] Ein Konzept gehört in das Repository und Backlog-System des betroffenen
Produkts, sofern die projektspezifischen Regeln keinen anderen führenden Ort
festlegen.

[MUST_IF] Das Produkt GitHub Issues nutzt, muss jedes eigenständig
entscheidbare Konzept durch genau ein Concept-Issue nachverfolgt werden. Ein
übergeordnetes Tracking-Issue darf mehrere Konzepte zusammenfassen, ersetzt
aber nicht ihre einzelnen Entscheidungen und Status.

[SHOULD] Das Projekt soll Concepts durch einen eindeutigen Typ, ein Label oder
ein entsprechendes Metadatenfeld von umsetzungsreifen Backlog Items
unterscheiden.

[SHOULD] Wenn das Backlog-System gespeicherte Ansichten und eigene Felder
unterstützt, soll eine eigene Concept- oder Discovery-Ansicht verwendet werden.
Konzeptreife und Umsetzungsstatus sollen getrennte Felder bleiben.

[MUST] Konkrete Typen, Labels, Statuswerte, Boards, Felder und Prioritäten
werden aus den Regeln des jeweiligen Projekts übernommen und nicht global
erfunden.

## Konzept-Lebenszyklus

### 1. Idee erfassen

[MUST] Die erste Erfassung benennt mindestens Problem oder Chance, betroffene
Nutzer, erwarteten Produktnutzen und den bekannten Ausgangskontext.

[MUST] Der Agent prüft, ob die Idee bereits durch bestehendes Produktverhalten,
ein anderes Konzept oder ein vorhandenes Backlog Item abgedeckt wird.

### 2. Discovery durchführen

[MUST] Vor einer Empfehlung müssen die relevanten Produktregeln,
Dokumentation, bestehenden Funktionen, Issues und belegten technischen
Randbedingungen geprüft werden.

[MUST] Die Discovery betrachtet im erforderlichen Umfang:

- betroffene Nutzer und ihren konkreten Nutzen,
- belegten Ist-Zustand und bestehende Einschränkungen,
- sinnvolle Lösungsoptionen und Zielkonflikte,
- MVP, spätere Ausbaustufen und Nicht-Scope,
- betroffene Produktbereiche und Repositories,
- Daten, Schnittstellen, Berechtigungen und Workflows,
- Datenschutz, Security, Betrieb und Migration,
- externe Systeme, Anbieter, Freigaben oder Kosten sowie
- Abhängigkeiten zu anderen Konzepten und Backlog Items.

[MUST_NOT] Ein Konzept darf technische oder fachliche Tatsachen behaupten, die
nicht aus dem aktuellen Produktkontext oder ausdrücklich gekennzeichneten
Annahmen hervorgehen.

### 3. Entscheidungsvorlage formulieren

[MUST] Ein entscheidungsreifes Konzept verwendet mindestens die folgende
Struktur. Nicht relevante Punkte dürfen knapp als nicht zutreffend markiert
werden.

```md
## Problem oder Chance

Welches Problem soll gelöst oder welche Chance genutzt werden?

## Nutzer und Produktnutzen

Wer ist betroffen und welchen konkreten Nutzen erwarten wir?

## Bestehender Produktstand

Was existiert bereits und welche Quellen belegen den Ist-Zustand?

## Untersuchungsumfang

### Enthalten

- Gegenstand der Konzeptentscheidung

### Nicht enthalten

- Bewusst ausgeschlossene Fragestellungen oder Ausbaustufen

## Optionen

### Option A

- Beschreibung
- Vorteile
- Nachteile
- Auswirkungen und Risiken

### Option B

- Beschreibung
- Vorteile
- Nachteile
- Auswirkungen und Risiken

## Empfehlung

Welche Option wird warum empfohlen?

## Abhängigkeiten und Auswirkungen

- Produktbereiche, Repositories und verwandte Issues
- Daten, Schnittstellen, Berechtigungen und Workflows
- Datenschutz, Security, Betrieb, Migration oder externe Anbieter

## Offene Produktentscheidungen

- [ ] Entscheidung mit klaren Optionen

## Product-Owner-Entscheidung

- Status: offen
- Entscheidung:
- Begründung:
- Entscheidungsdatum und verantwortliche Instanz:

## Abgeleitete Backlog Items

- Noch keine

## Relevante Quellen

- Produktdokumentation, Code, Schema, Schnittstellen und verwandte Issues
```

[MUST] Optionen müssen echte entscheidungsrelevante Alternativen darstellen.
Scheinoptionen oder eine unbegründete Vorfestlegung sind nicht zulässig.

[MUST] Die Empfehlung muss Nutzen, Kosten, Risiken, Abhängigkeiten und
MVP-Tauglichkeit nachvollziehbar gegeneinander abwägen.

### 4. Product-Owner-Entscheidung dokumentieren

[MUST] Die Entscheidung muss mit Status, gewählter Richtung, Begründung,
Entscheidungsdatum und der nach Projektregeln verantwortlichen Instanz im
Concept-Issue oder verknüpften Konzeptdokument festgehalten werden.

[MUST_NOT] Der Agent darf eine materielle Produktentscheidung nicht als
freigegeben markieren, wenn die erforderliche Entscheidungsbefugnis oder
Bestätigung nicht belegt ist.

Projekte können eigene Statuswerte verwenden. Semantisch müssen mindestens
folgende Zustände unterscheidbar sein:

- Idee,
- in Ausarbeitung,
- Product-Owner-Entscheidung offen,
- angenommen,
- verworfen,
- durch ein anderes Konzept ersetzt und
- in umsetzbare Backlog Items überführt.

### 5. Angenommenes Konzept in Backlog Items überführen

[MUST_IF] Ein Konzept angenommen wurde, müssen daraus ein oder mehrere
eigenständig umsetzbare Items nach dem Workflow
[Backlog Item erstellen und verfeinern](https://bastivonnijodex.github.io/agents/workflows/backlog-item.md)
abgeleitet werden.

[MUST] Konzept und abgeleitete Backlog Items müssen sich gegenseitig
referenzieren. Das Konzept-Issue darf nicht als undifferenziertes
Sammel-Implementierungs-Issue verwendet werden.

[MUST] Abhängigkeiten, Reihenfolge, gemeinsame Produktentscheidungen und
bewusster Nicht-Scope müssen in den abgeleiteten Items erhalten bleiben.

### 6. Produktdokumentation aktualisieren

[MUST_IF] Eine angenommene Entscheidung bestehende Produktregeln verändert,
muss sie in die zuständige Produkt- oder Domain-Dokumentation überführt werden,
sobald sie nach den Projektregeln als verbindliche Produktentscheidung gilt.

[MUST_IF] Die Entscheidung erst mit der Implementierung gültig wird, muss die
Produktdokumentation spätestens gemeinsam mit der Umsetzung aktualisiert werden.

[MUST_NOT] Ein historisches Konzeptdokument darf nach Umsetzung anstelle von
Code, Schema, Schnittstellen oder aktueller Produktdokumentation als führende
Wahrheit behandelt werden.

## Ausführliches Konzeptdokument

[ALLOW_IF] Ein Concept-Issue allein darf ausreichen, wenn Scope, Optionen und
Auswirkungen darin vollständig und wartbar dokumentiert werden können.

[SHOULD] Ein zusätzliches versioniertes Konzeptdokument soll verwendet werden,
wenn mehrere Module oder Repositories, umfangreiche Nutzerabläufe, Datenmodelle,
Diagramme, externe Verträge oder langfristig relevante Herleitungen betroffen
sind.

[MUST_IF] Ein Konzeptdokument existiert, muss das Concept-Issue seinen
Lebenszyklus und seine Entscheidung nachverfolgen und auf das Dokument
verweisen. Das Dokument muss mindestens Status, Stand, zugehöriges Issue,
PO-Entscheidung und abgeleitete Backlog Items erkennen lassen.

[MUST_NOT] Ein in einem Issue verlinktes Konzeptdokument darf nicht dauerhaft
nur lokal oder unversioniert bleiben.

## Abschluss eines Concept-Issues

Ein Concept-Issue darf abgeschlossen werden, wenn einer dieser Fälle belegt ist:

- Das Konzept wurde angenommen, die Entscheidung ist dokumentiert und die
  erforderlichen Backlog Items wurden erstellt und verknüpft.
- Das Konzept wurde mit Begründung verworfen.
- Das Konzept wurde durch ein eindeutig verlinktes neueres Konzept ersetzt.

[MUST] Verbleibende offene Produktentscheidungen dürfen beim Abschluss nicht
verloren gehen. Sie müssen als Blocker oder neues Concept-Issue erhalten bleiben.
