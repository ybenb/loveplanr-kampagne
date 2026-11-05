# AI-Fehler

Hier stehen nur Fehler, die wirklich vorkamen, mit Output, Entdeckung und Korrektur. Teil A betrifft den Output der KI. Teil B betrifft Vorgaben, die sich beim Prüfen als veraltet oder ungenau zeigten. Das sind keine KI-Fehler.

## A. Fehler der KI

### 1. Login, der das Firmenkonto mit einbezogen hätte
- **Output:** Die KI schlug `gh auth login` per Browser mit dem Scope `repo` vor.
- **Bemerkt:** Der Nutzer sah auf der Autorisierungsseite die Organisation seines Arbeitgebers und meldete es, obwohl er zuvor verlangt hatte, sie nicht anzufassen.
- **Korrektur:** Login abgebrochen, Hintergrundbefehl gestoppt. Stattdessen ein Fine-grained Token, das nur dem privaten Konto gehört.
- **Lehre:** Die KI kannte die Regel und wählte trotzdem den bequemen Standardweg. Ohne den Blick des Nutzers wäre das durchgegangen.

### 2. `--with-token` ohne Eingabe
- **Output:** Die KI führte `gh auth login --with-token` ohne Eingabe aus, der Befehl fiel auf den Browser-Login zurück.
- **Bemerkt:** Durch die Ausgabe des Befehls.
- **Korrektur:** Token per `pbpaste` übergeben, ohne ihn anzuzeigen.

### 3. Falsche Angabe zu den Token-Rechten
- **Output:** Die KI bezeichnete «Administration» als Kontoberechtigung. Sie liegt aber bei den Repository-Rechten. Das Token hatte zunächst nur Leserechte, das Anlegen des Repos scheiterte mit Fehler 403.
- **Bemerkt:** Durch den Fehler 403 und einen Screenshot des Nutzers.
- **Korrektur:** Angabe berichtigt, der Nutzer stellte auf «Read and write».

### 4. Notiz geschrieben, bevor die Arbeit fertig war
- **Output:** Ein Skript zum Aktualisieren der Vorgaben suchte eine Textstelle in falscher Form und brach ab. Die Projektnotiz der KI war im selben Lauf schon aktualisiert worden und beschrieb etwas als erledigt, das nicht erledigt war.
- **Bemerkt:** Durch die Fehlermeldung des Skripts.
- **Korrektur:** Muster korrigiert, Skript erneut ausgeführt und das Ergebnis geprüft.

### 5. Pins: Fehler erst beim Anschauen sichtbar
Die Masse und Textlängen der ersten Pins bestanden die automatische Prüfung. Die visuelle Prüfung zeigte trotzdem:
- **Pin 12:** Überschrift lag über dem Gesicht, die Zeile brach unschön um. Korrektur: anderes Layout, Gesichter frei.
- **Pins 04 bis 07:** Grosse leere Fläche in der Mitte, Umbruch nach «[Ort]». Korrektur: Bildfläche mit Angabe, welches echte Material dort hinkommt.
- **Pin 09:** Umbruch «in 5 / Schritten». Korrektur: fester Umbruch.
- **Pins 08 und 12:** Weisser Text auf Altrosa war zu schwach. Korrektur: dunkler Text.
- **Pin 02:** Der neue 1×-Stempel überdeckte das Ende der Unterzeile. Das war ein Folgefehler der eigenen Korrektur und fiel erst in der Website-Ansicht auf. Korrektur: Zeile aufgeteilt.

### 6. Keyword ausserhalb des sichtbaren Teils
- **Output:** Die Titel von Pin 01 und Pin 02 begannen mit dem Slogan. Das Keyword stand deshalb hinter den ersten rund 40 Zeichen, die Pinterest im Feed oft zeigt.
- **Bemerkt:** Die KI selbst, beim Schreiben der Website-Regel «Keyword vorne».
- **Korrektur:** Titel umgestellt.

### 7. Website: Layoutfehler in der ersten Fassung
- **Handy:** Der Hero-Zuschnitt schnitt die Braut ab, der Text lag auf dem Gesicht des Bräutigams. Korrektur: Foto oben, Text darunter.
- **Keywords:** Die Überschrift «Hochzeitswebseite» stiess an die nächste Spalte, später blieb eine Spalte allein in der zweiten Zeile. Korrektur: kleinere Schrift, fünf feste Spalten.
- **Überschriften:** Zu schmal gesetzt, darum drei Zeilen. Korrektur: breiter gesetzt.

### 8. Überschrift versprach mehr, als da war
- **Output:** Der Titel von Bereich 4 lautete «Zwölf Pins, bereit zum Hochladen», obwohl vier Pins Platzhalter sind und einer eine fehlende Zielseite braucht.
- **Bemerkt:** Die KI selbst, beim Durchlesen der gerenderten Seite.
- **Korrektur:** Titel neutral formuliert, im Text steht nun: sieben fertig, vier Platzhalter, einer wartet auf seine Zielseite.

### 9. Zu viele Platzhalter
- **Output:** Vier von zwölf Pins waren leere Rahmen mit Text wie «[Paar]» und «[Creatorin]». Die KI las die Regel «keine erfundenen Testimonials» so, dass ohne echtes Material gar kein gestalteter Pin möglich sei.
- **Bemerkt:** Der Nutzer: «du hast zu viele Placeholder verwendet».
- **Korrektur:** Die Regel betrifft die Aussage, nicht die Gestaltung. Die Pins zeigen nun Stock-Fotos mit Texten, die nichts über Kunden behaupten, zum Beispiel «So kann eure Hochzeitsseite aussehen». Echte Geschichten ersetzen sie später. Mit dem nächsten Prompt erlaubte der Nutzer Kundenaussagen. Die KI übernahm echte Zitate von loveplanr.com statt welche zu formulieren und markierte die Fotos als «Symbolbild», weil sie nicht diese Paare zeigen. Der erste Umbau zu Pins ohne Kundenaussage war also nur ein Zwischenschritt: Die KI hätte die vorhandenen Zitate schon vorher zur Entscheidung vorlegen können.

### 10. Widersprüche über mehrere Bereiche
Die Prüfung nach der Rubric des Dozenten zeigte Fehler, die beim Bau jedes einzelnen Bereichs nicht auffielen:
- **Pin 08:** In den Boards, der Pin-Tabelle und im Kalender stand er unterschiedlich: «bereit», «Vorschlag», und trotz fehlender Zielseite in Woche 5 eingeplant. Korrektur: ein einziger Status, nicht im Kalender, Pin 13 als Ersatz.
- **Zielwert und Stoppregel passten nicht zusammen:** «≤ 20–30 CHF» gegen «Stopp über 30 CHF». Korrektur: Ziel ≤ 25 CHF, Stopp über 30 CHF.
- **Kosten pro Kunde** hing im Funnel am kostenlosen Start, obwohl die Kennzahl erst beim Kauf entsteht. Korrektur: eigener Schritt «Sie kaufen».
- **«12963Hochzeit»:** Die Zeitskala bestand aus Elementen ohne Leerraum. Im Browser sah das korrekt aus, im extrahierten Text standen die Zahlen zusammen. Die visuelle Prüfung konnte das nicht zeigen. Korrektur: echte Liste mit vollen Beschriftungen.
- **Begriffe gemischt:** «Hochzeitswebseite», «Hochzeitswebsite» und «Hochzeitsseite» standen nebeneinander. Korrektur: «Hochzeitswebseite», wie Loveplanr.
- **Bemerkt:** durch den Nutzer in Prompt 27. Die KI hatte Bereiche einzeln geprüft, nie einen Wert quer über alle Bereiche.

## B. Korrekturen an den Vorgaben (keine KI-Fehler)

Beim Abgleich mit loveplanr.com und der Hilfe von Pinterest zeigten sich Abweichungen in der ursprünglichen Projektvorgabe:

| Vorgabe | Geprüft | Umgang |
|---|---|---|
| Drei Pakete mit Preisspannen | `/preise/` nennt zwei Pakete: 149 und 249 | Aktuelle Preise verwendet |
| Hochzeitsquiz und Live-Fotogalerie | Auf `/preise/` und `/faq/` nicht genannt | Nicht beworben |
| «erst beim Veröffentlichen zahlen» | Die FAQ sagt: kostenlos erstellen und testen, Paket wählen, «wenn ihr bereit seid» | Wortlaut von Loveplanr verwendet |
| Gäste brauchen kein Konto | Belegt für Fotos, für Rückmeldungen nicht | Nur für Fotos behauptet, Rest als offene Frage |
| Idea Pins | Pinterest hat Idea Pins 2023 in normale Pins überführt | «Video-Pin» geschrieben |
| Checkliste gegen E-Mail | Heute kein Download und keine Anmeldung vorhanden | Als Vorschlag mit neuer Zielseite markiert |
