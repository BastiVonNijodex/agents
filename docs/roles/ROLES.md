# ROLES.md

## Zweck

Diese Datei ist die Lookup-Datei für Rollen. Rollen sind unabhängige Verantwortungsbereiche, keine festen Personas.

## Verwendung

[MUST] Rollen werden nur geladen, wenn ihr Verantwortungsbereich für den aktuellen Task relevant ist.

[MUST_NOT] Rollen dürfen nicht allein wegen ihrer Existenz oder wegen einer starren Prozessreihenfolge geladen werden.

[MUST_IF] Wird ein weiterer Verantwortungsbereich im Task relevant, muss die passende Rolle nachgeladen oder die Abweichung benannt werden.

## Rollen

| Rolle | Lesen und verwenden, wenn | Zweck |
|---|---|---|
| [Product Owner](https://bastivonnijodex.github.io/agents/roles/product-owner.md) | Produktverantwortung, Produktklärung, Priorisierung, Backlog-Pflege oder die Erstellung und Verfeinerung von Backlog Items relevant ist. | Produktzusammenhänge wahren und umsetzbare, wertorientierte Entscheidungen und Backlog Items vorbereiten. |
| [Security Reviewer](https://bastivonnijodex.github.io/agents/roles/security-reviewer.md) | Authentifizierung, Autorisierung, sensible Daten, Secrets, Uploads, öffentliche Schnittstellen, Webhooks, AI-Datenflüsse, externe Provider, sicherheitsrelevante Migrationen oder Incidents betroffen sind. | Sicherheitsannahmen adversarial prüfen, Findings priorisieren und risikobehaftete Freigaben challengen. |
| Planner | Planung, Strukturierung, Priorisierung oder Zerlegung von Arbeit relevant ist. | Fachliche Klärung und belastbare Arbeitsplanung. |
| Developer | Architektur, Implementierung, Refactoring, Code-Review oder technische Entscheidung relevant ist. | Saubere, kleine und projektkonforme Umsetzung. |
| Tester | Teststrategie, Regression, Verifikation oder Qualitätsprüfung relevant ist. | Nachweis, dass Änderungen funktionieren und nichts Wesentliches brechen. |
| Designer | UI, UX, visuelle Bewertung, Prototyping oder Interaktionsdesign relevant ist. | Nutzbare, konsistente und verständliche Gestaltung. |

## Pflege

[SHOULD] Detaildateien für Rollen werden erst ergänzt, wenn wiederkehrende Aufgaben konkrete zusätzliche Regeln brauchen.
