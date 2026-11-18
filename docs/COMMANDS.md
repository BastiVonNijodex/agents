# COMMANDS.md

## Zweck

Diese Datei beschreibt den Umgang mit dokumentierten Kommandos und Slash-Commands.

## Regeln

[MUST] Der Agent darf dokumentierte Kommandos nur ausführen, wenn Zweck, Ziel und Platzhalter im aktuellen Kontext eindeutig sind.

[MUST_NOT] Kommandos mit destruktiver, externer oder produktionswirksamer Wirkung dürfen ohne ausdrückliche Freigabe nicht ausgeführt werden.

[MUST] Wenn ein Kommando nicht sicher ausführbar ist, muss der Agent den Grund benennen und eine sichere Alternative vorschlagen.

## Aktueller Stand

[OPTIONAL] Dieses Regel-Repository definiert aktuell keine eigenen Slash-Commands.

## SSH-Aliase für freigegebene Produktionsarbeit

Diese Hilfe ergänzt die verbindliche Regel in [AGENTS.md](AGENTS.md). Sie enthält bewusst keine Zieladressen, Schlüssel, Benutzernamen, Ports, Host-Keys, Serverpfade oder Secrets.

Ein Alias ist nur auf einer lokalen Laufzeit verfügbar, deren persönliche SSH-Konfiguration ihn bereits enthält. Fehlt er, wird kein Ersatz konstruiert und keine SSH-Konfiguration verändert.

### Wo die Aliasnamen stehen

Der kanonische Alias eines Projekts steht in dessen eigener `PROJECT.md`. Er
folgt grundsätzlich dem Schema `<appname>-prod`; eine abweichende bestehende
Konvention gilt nur, wenn sie dort eindeutig belegt ist.

Nennt die `PROJECT.md` eines Projekts keinen verifizierten Alias, existiert für
dieses Projekt bewusst keiner. Der Agent nimmt dann keinen an, meldet den
fehlenden Nachweis und stoppt vor dem Produktionszugriff.

Der dokumentierte Alias bestätigt ausschließlich den Namen. Eine erfolgreiche SSH-Anmeldung, die Serveridentität und die Release-Berechtigung müssen bei jedem konkreten Einsatz separat geprüft werden.

### Sicherer Ablauf

1. Explizite Freigabe für genau den Release oder Produktionsschritt und die projektbezogenen Gates prüfen.
2. Den Alias lokal ohne Netzwerkzugriff mit `ssh -G <alias>` prüfen. Die Ausgabe wird nicht in Chat, Tickets oder Agenten-Memory kopiert.
3. Ausschließlich den projektspezifischen Release-Runbook folgen; ein Alias autorisiert weder Deployment noch Migration, Neustart oder Datenzugriff.
4. Preflight, Backup, Rollback und Verifikation gemäß dem jeweiligen Projekt nachweisbar abschließen.

Unbekannte Ziele, IP-Adressen als Ersatz, Änderungen an `~/.ssh/config` oder das automatische Akzeptieren eines unbekannten Host-Keys sind nicht zulässig.

