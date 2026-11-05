# Einmal reicht.

Pinterest-Kampagne für Loveplanr, Final Artefact im Kurs «Digital Marketing for Start-ups» (ZHAW, HS 2026, Team 4). Studentisches Projekt, kein offizieller Auftritt von Loveplanr.

Live: https://löve.ch

- `index.html`, `assets/site.css`: statische Website
- `assets/pins/`: zwölf Pins (1000 × 1500 px), Vorschauen und `pin-set.csv`
- `tools/pins_data.py`: Texte aller Pins, eine Quelle für Bilder, CSV und Website
- `tools/make_pins.py`: rendert die Pins, braucht die lokalen Originalfotos, Chrome und macOS
- `tools/make_webp.cjs`: wandelt Website-Bilder in WebP um, braucht das npm-Paket `sharp`
- `tools/build_site.py`: schreibt Pin-Karten, Mockup und Funnel-Tabelle in `index.html` und erzeugt `prozess/index.html` aus `docs/`
- `docs/`: Prompt-Log, AI-Fehler, offene Punkte, Quellen, Screenshots der Iterationen (auch sichtbar auf `/prozess/`)
