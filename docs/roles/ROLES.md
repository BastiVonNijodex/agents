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
| Planner | Planung, Strukturierung, Priorisierung oder Zerlegung von Arbeit relevant ist. | Fachliche Klärung und belastbare Arbeitsplanung. |
| Developer | Architektur, Implementierung, Refactoring, Code-Review oder technische Entscheidung relevant ist. | Saubere, kleine und projektkonforme Umsetzung. |
| Tester | Teststrategie, Regression, Verifikation oder Qualitätsprüfung relevant ist. | Nachweis, dass Änderungen funktionieren und nichts Wesentliches brechen. |
| Designer | UI, UX, visuelle Bewertung, Prototyping oder Interaktionsdesign relevant ist. | Nutzbare, konsistente und verständliche Gestaltung. |

## Pflege

[SHOULD] Detaildateien für Rollen werden erst ergänzt, wenn wiederkehrende Aufgaben konkrete zusätzliche Regeln brauchen.

