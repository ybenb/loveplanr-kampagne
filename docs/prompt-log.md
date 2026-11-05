# Prompt-Log

Tool: Claude Code mit dem Modell Claude Opus 5.5. Die Prompts stehen im Wortlaut, Tippfehler inklusive.
Eckige Klammern markieren Ergänzungen oder Schwärzungen: `[Firmenkonto]` ersetzt den Namen eines Arbeitgebers,
und Angaben aus dem privaten Businessplan stehen nicht in diesem öffentlichen Log.

Die Projektvorgaben (`CLAUDE.md`) und das Material (`material/`) liegen nur lokal. Das Assessment Sheet schreibt das
Team selbst, ohne KI. Es gehört nicht zu diesem Log.

## Einrichtung

| Nr. | Prompt | Was passierte | Commit |
|---|---|---|---|
| 1 | «mkdir loveplanr-kampagne && cd loveplanr-kampagne» | Projektordner erstellt. | – |
| 2 | «Lies CLAUDE.md und die Dateien in material/. Richte das Projekt ein: git init, öffentliches GitHub-Repo "loveplanr-kampagne" mit gh anlegen, GitHub Pages aktivieren. Noch keine Website bauen.» | Vorgaben und Material gelesen, Git eingerichtet. Das Anlegen brauchte zuerst einen Login. | `4925004` |
| 3 | «Ich will nur auf meinem persönlich account, mein firmenaccount ([Firmenkonto]) resp. die organization darf nicht angefasst werden.» | Konto-Regel übernommen. | – |
| 4 | «[Screenshot Token-Formular] führe mich durch» | Schrittweise Anleitung für den Fine-grained Token. | – |
| 5 | «[lokal ausgeführter Login-Befehl] [Screenshot] aber da ist [Firmenkonto] auch darauf» | Der Nutzer entdeckte den Fehler 1 in `ai-fehler.md`. Login abgebrochen, Weg gewechselt. | – |
| 6 | «ich habe ihn nun in der zwischenablage, fahre fort» | Token aus der Zwischenablage an `gh` übergeben, ohne ihn anzuzeigen. | – |
| 7 | «[Screenshot Token Read-only]» | Fehlende Schreibrechte erkannt (Fehler 3). | – |
| 8 | «Habe ich gemacht» | Repo öffentlich angelegt, Pages aktiviert. | `4925004` |
| 9 | «ausschliesen, damit nicht sichtbar, weitere schritte ausführen» | `material/` per `.gitignore` ausgeschlossen. | `20849f4` |
| 10 | «/Users/[…]/Downloads/CLAUDE.md» | Aktuelle Vorgaben gelesen. Danach `CLAUDE.md` ausgeschlossen. | `000f74c` |
| 11 | «hier noch die originale Website: https://loveplanr.com/» | Website gelesen und mit den Vorgaben verglichen. Abweichungen siehe `ai-fehler.md`, Teil B. | – |
| 12 | «1. auschliessen, 2. ich gebe frei, 3. aktualisierne, 4. ich sende dir assets demnächst, die domain löve.ch ist gekauft aber noch nicht eingerichtet.» | Antworten auf vier Rückfragen: ausschliessen, öffentlicher Zielwert pro Kunde freigegeben, Vorgaben aktualisiert. | – |
| 13 | «Hier ein paar Assets» [11 Fotos] | Fotos lokal abgelegt, Originale ausgeschlossen. | `ad86ec2` |
| 14 | «[Screenshot Infomaniak] wo muss ich hier was machen? Ich besitze die Lizenzen (envato gekauft)» | Anleitung für die DNS-Einträge. | – |
| 15 | «[Screenshot] so?» | Eintrag geprüft. | – |
| 16 | «hä? was ist target?» | Begriff in einfachen Worten erklärt. | – |
| 17 | «Habe ich gemacht ist verified» | Domain-Verifikation geprüft. | – |
| 18 | «[Screenshot Infomaniak A-Record-Dialog]» | Werte für die A-Records genannt. | – |
| 19 | «alles gemacht» | DNS und Zertifikat geprüft, `CNAME` hinzugefügt, HTTPS erzwungen. | `fc8a485` |

## Website

| Nr. | Prompt | Was passierte | Commit |
|---|---|---|---|
| 20 | «gib den Startschuss, halte dich an alle Vorgaben wie besprochen und sei vor allem kreativ bei der Umsatzung. Alles muss dokumentiert werden.» | Kampagnenidee «Einmal reicht.» entwickelt, zwölf Pins als Daten, Generator und Bilder erstellt, erster Render. | `eb50468` |
| 21 | «Speichere den Stand unter "LOVE" ich werde jetzt den Laptop in den sleep modus umstellen und will das du in der zwischnzeit weiterarbeitest. Geht das?» | Stand gespeichert. Antwort: Im Ruhezustand läuft die Arbeit nicht weiter. | – |
| 22 | «ich mache morgen weiter» | Keine Arbeit im Hintergrund. | – |
| 23 | «let's go we are back» | Pins visuell geprüft und korrigiert, Website mit acht Bereichen gebaut, auf Desktop und Handy geprüft, Dokumentation geschrieben, veröffentlicht. | `eb50468` |

| 24 | «[12 Fotos] Hier hat es noch mehr fotos, du hast zu viele Placeholder verwendet» | Die vier Hub-Pins neu geschrieben und mit den neuen Fotos gestaltet. Sie behaupten nichts über Kunden und laufen als Startfassung, bis echtes Material vorliegt. Pins 09 und 10 mit passenderen Fotos, neue Fotos auf der Website bei Boards, Personas und in einem Bildstreifen. | `d007ae1` |

| 25 | «ass sie ohne Kundenaussage funktionieren und mit de, du darfst auch kundenaussagen daraufpacken.» (nimmt Bezug auf eine Zwischennachricht der KI) | Echte Zitate wörtlich von loveplanr.com geholt und auf die Pins 04, 05 und 06 gesetzt, Fotos dort als «Symbolbild» markiert. Die Zitate stehen auch im Bereich 8 der Website. | dieser Commit |

Die Prompts 20 bis 23 gehören zur selben Iteration, weil der Bau über Nacht unterbrochen wurde. Darum gibt es dafür einen gemeinsamen Commit.

## Was der Prompt 20 offenliess

«Sei kreativ» legte die Idee nicht fest. Diese Entscheide traf die KI selbst. Das Team sollte sie prüfen:

- Leitidee «Einmal reicht.» mit dem Motiv 1×, aus dem USP «einmaliger Preis» abgeleitet.
- Hub-Pins waren zuerst sichtbare Platzhalter, damit Stock-Fotos nicht als Paargeschichten erscheinen. Der Nutzer korrigierte das mit Prompt 24: Sie sind nun gestaltet, die Pins 04 bis 06 tragen seit Prompt 25 echte Zitate.
- Help-Pins erscheinen im Kalender vor den Hero-Pins.
- Der Promoted-Test vergleicht Preis gegen Hilfe, mit einer Nachfrist von vier Wochen für den Kauf. Die Nachfrist ist ein Vorschlag, kein Erfahrungswert.
- Die Geschichte «Ein Abend im Planungsfenster» ordnet die KPIs den Schritten eines fiktiven Paars zu.
