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

| 25 | «ass sie ohne Kundenaussage funktionieren und mit de, du darfst auch kundenaussagen daraufpacken.» (nimmt Bezug auf eine Zwischennachricht der KI) | Echte Zitate wörtlich von loveplanr.com geholt und auf die Pins 04, 05 und 06 gesetzt, Fotos dort als «Symbolbild» markiert. Die Zitate stehen auch im Bereich 8 der Website. | `e425332` |
| 26 | «Die AUssage darf auf dem Pin platziert werden.» (Antwort auf die Rückfrage der KI zu «Bereits von 10’000+ Hochzeitspaaren genutzt») | Aussage wörtlich auf Pin 02 und in dessen Beschreibung gesetzt. Nicht auf Pin 01, weil dieser im Promoted-Test gegen Pin 09 läuft und nur die Botschaft Preis oder Hilfe vergleichen soll. | `41820a5` |
| 27 | Rollen-Prompt «Senior-Kampagnendesigner», Wortlaut unten | Widersprüche behoben, Pins ins Zentrum, Prozess auf Unterseite. Siehe Iteration 5 unten. | dieser Commit |

Die Prompts 20 bis 23 gehören zur selben Iteration, weil der Bau über Nacht unterbrochen wurde. Darum gibt es dafür einen gemeinsamen Commit.

## Was der Prompt 20 offenliess

«Sei kreativ» legte die Idee nicht fest. Diese Entscheide traf die KI selbst. Das Team sollte sie prüfen:

- Leitidee «Einmal reicht.» mit dem Motiv 1×, aus dem USP «einmaliger Preis» abgeleitet.
- Hub-Pins waren zuerst sichtbare Platzhalter, damit Stock-Fotos nicht als Paargeschichten erscheinen. Der Nutzer korrigierte das mit Prompt 24: Sie sind nun gestaltet, die Pins 04 bis 06 tragen seit Prompt 25 echte Zitate.
- Help-Pins erscheinen im Kalender vor den Hero-Pins.
- Der Promoted-Test vergleicht Preis gegen Hilfe, mit einer Nachfrist von vier Wochen für den Kauf. Die Nachfrist ist ein Vorschlag, kein Erfahrungswert.
- Die Geschichte «Ein Abend im Planungsfenster» ordnet die KPIs den Schritten eines fiktiven Paars zu.

## Iteration 5: Prompt 27 im Wortlaut

```
Rolle: Du bist Senior-Kampagnendesigner und UX-Writer für Social-Media-Kampagnen
im Schweizer Hochzeitsmarkt.

Kontext: Lies CLAUDE.md und den aktuellen Stand der Website. Die Seite wird von
unserem Dozenten nach dieser Rubric bewertet: (a) Professionalität und
Ausführungsqualität im Vergleich zu professionellen Standards, (b) die
Verhaltensprinzipien sind im Artefakt an konkreten Elementen erkennbar.

Aufgabe – in dieser Reihenfolge:

1. Widersprüche beheben:
   - Pin 08: ein einziger Status überall (Boards, Pin-Tabelle, Kalender, Test).
     Solange die Landingpage fehlt, raus aus Kalender und Test, Ersatz-Pin
     für Woche 5 vorschlagen.
   - Zielwert Kosten pro Kunde und Stoppregel angleichen (Ziel ≤ 25 CHF,
     Stopp > 30 CHF – oder begründet anders, aber konsistent).
   - KPI „Kosten pro Kunde“ dem Kauf-Schritt im Funnel zuordnen.
   - Darstellungsfehler „12963Hochzeit“ in der Ausgangslage finden und beheben.
   - Einheitlich den Begriff verwenden, den loveplanr.com selbst nutzt
     (Hochzeitswebsite oder Hochzeitswebseite).
   - Zitate: Freigabestatus konsistent; direkt am Pin vermerken
     „Zitat von loveplanr.com, Foto: Stock, zeigt nicht das Paar“.

2. Wirkung als Kampagne erhöhen:
   - Ganz oben eine Zusammenfassung, in 30 Sekunden lesbar:
     Bottleneck → warum Pinterest → Kampagnenidee → 3 Kern-KPIs.
   - Die 12 Pins als Herzstück: Masonry-Raster wie in einem Pinterest-Feed,
     plus ein Mockup „So erscheint Pin 09 bei der Suche
     ‚Hochzeitswebsite erstellen‘“ (klar als Mockup beschriftet, kein
     Pinterest-Logo).
   - Bei jedem Pin ein Prinzip-Label, das auf das konkrete Element zeigt,
     z. B. „Reciprocity → CTA ‚Checkliste gratis‘“.
   - Status-Labels, offene Punkte, Prompt-Log und AI-Fehler auf eine
     Unterseite /prozess verschieben; auf der Hauptseite nur ein Link dorthin.
   - Englische Fachbegriffe beim ersten Vorkommen kurz auf Deutsch erklären.

3. Qualität prüfen:
   - Mobile bei 390 px und Desktop bei 1280 px mit Playwright screenshoten,
     Layoutfehler beheben.
   - Lighthouse: Accessibility und Performance ≥ 90; Bilder als WebP,
     sinnvolle Alt-Texte.
   - Alle internen Links und den CSV-Download testen.

Einschränkungen:
- Keine neuen Zahlen, Statistiken oder Testimonials erfinden. Was fehlt,
  bleibt als offener Punkt auf /prozess.
- Schweizer Rechtschreibung (kein ß), Preise in CHF.
- Inhalte der Gründer (Preise, Zitate) nicht umformulieren.
- Vor dem Löschen ganzer Abschnitte zuerst fragen.

Output: Kurze Liste der Änderungen pro Punkt, Vorher/Nachher-Screenshots in
docs/iterationen/, dann committen als
„Iteration N: Widersprüche behoben, Pins ins Zentrum, Prozess auf Unterseite“.
```

Entscheide der KI in Iteration 5, die das Team prüfen sollte:

- **Begriff:** Auf den acht geprüften Seiten von loveplanr.com steht 114-mal «Hochzeitswebseite» und 6-mal «Hochzeitswebsite». Darum heisst auch die Suche im Mockup «Hochzeitswebseite erstellen», nicht wie im Prompt «Hochzeitswebsite erstellen». Die zweite Schreibweise bleibt nur als Keyword-Variante.
- **Ersatz-Pin für Woche 5:** neuer Pin 13 mit einem weiteren echten Zitat von Sabine & Markus. So bleiben es zwölf einplanbare Pins, Pin 08 steht separat als Vorschlag.
- **Ein Status bleibt auf der Hauptseite:** Pin 08 trägt dort «Vorschlag: neue Zielseite nötig». Die Vorgaben verlangen diese Kennzeichnung, und ohne sie wäre die Hauptseite irreführend. Alle anderen Status stehen nur auf der Unterseite Prozess.
- **Zielwert:** ≤ 25 CHF und Stopp über 30 CHF wie im Prompt. Dazwischen wird beobachtet. Die Hauptseite nennt die frühere Spanne nicht mehr.
- **Abschnitte:** Keiner wurde gelöscht. Verschoben wurden der Prozess-Bereich und die Hinweise «Noch zu prüfen» und «Die fehlende Seite» auf die Unterseite Prozess.

## Iteration 6: Logo und Hintergrundvideo

Prompts im Wortlaut. Der Link zu loveplanr.com stand mit Tracking-Parametern einer Anzeige im Prompt. Er ist hier gekürzt, die lokalen Pfade sind ebenfalls gekürzt.

```
löve.ch (haben wir zusammen gebaut)
```

```
https://loveplanr.com/hochzeitswebsite/?[Tracking-Parameter] Hier siehst du die Website, das logo soll darauf sein (evtl. kann man das übernehmen) Zudem sende ich dir anbei mehrere Videos. Ich will, dass du diese einbaust (zb. als Hero im Hintergrund) verwende dafür gängige Design best practices. [Downloads]/wedding-couple-holding-hands-at-outdoor-ceremony-….mov [Downloads]/bride-showing-off-ring-hugging-groom-in-bridal-sho-….mov [Downloads]/aerial-view-of-couple-dancing-on-grassy-field-….zip
```

```
DU sollst nicht ein hero aus dem Video nehmen, sondern die videos als Background einsetzen. wie bei deplo.io (dort hat es ebenfalls ein Video im Hintergrund).
```

```
Öffne mir local host damit ich sehe, wie es aussehen könnte
```

```
[Screenshot der Startseite, Pfeil auf das Hero-Foto] Hier soll das Video laufen, damit du dir das richtig vorstellen kanns
```

```
Ich finde das Bild vom Tanzenden paar super, nehmen wir das.
```

Ergebnis und Entscheide der KI, die das Team prüfen sollte:

- **Logo:** Die Wortmarke in der Kopfzeile ist die Originaldatei von loveplanr.com, als WebP verkleinert. Die Pins tragen weiterhin die Rekonstruktion.
- **Video:** Die Drohnenaufnahme des tanzenden Paars ersetzt das Hero-Foto. Aufbau, Höhe und Verlauf bleiben gleich. In einer lokalen Vorschau standen zwei Varianten zur Wahl: alle drei Clips nacheinander oder ein Clip pro Bereich. Gewählt hat der Nutzer nur den Tanz. Die beiden anderen Clips sind nicht im Repo.
- **Gespiegelt:** Der Clip läuft horizontal gespiegelt. So steht das Paar rechts, und der weisse Text liegt nicht auf dem weissen Kleid.
- **Best Practices:**
  - Das Standbild erscheint sofort, das Video wird erst danach geladen.
  - Es gibt zwei Grössen: 1280 px (2,2 MB) und 720 px fürs Handy (0,8 MB). Das Video läuft ohne Ton und pausiert ausserhalb des Bildschirms.
  - Bei «Bewegung reduzieren» und im Datensparmodus bleibt das Standbild stehen.
  - Ein Pause-Knopf erfüllt WCAG 2.2.2 (bewegte Inhalte über 5 Sekunden müssen sich anhalten lassen).
