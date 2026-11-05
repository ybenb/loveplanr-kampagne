#!/usr/bin/env python3
"""Schreibt Pin-Karten, Mockup und Funnel-Tabelle in index.html und erzeugt prozess/index.html aus docs/.
Aufruf: python3 -I tools/build_site.py
So bleiben Website, Pins, CSV und Dokumentation bei denselben Texten. Die Website selbst bleibt statisches HTML."""
import html, pathlib, re, sys
ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from pins_data import PINS, PRINZIP, SITE

NEXT = {
    "01-einmal-ja": "Pakete vergleichen, dann kostenlos starten",
    "02-einmal-reicht": "Komplettpaket verstehen, dann kostenlos starten",
    "03-mehr-vorfreude": "Konto erstellen und die Seite kostenlos bauen",
    "04-melek-rafael": "Sitzplan verstehen, Komplettpaket prüfen",
    "05-aline-josia": "Funktionen ansehen, dann kostenlos starten",
    "06-feierabend": "Funktionen ansehen, dann kostenlos starten",
    "07-partner": "Partner ansehen, Vertrauen aufbauen",
    "08-gratis-checkliste": "E-Mail-Adresse angeben, Checkliste erhalten",
    "09-fuenf-schritte": "Die Schritte nachlesen, dann kostenlos starten",
    "10-rueckmeldungen": "Funktion verstehen, dann kostenlos starten",
    "11-sitzplan": "Sitzplan verstehen, Komplettpaket prüfen",
    "12-onkel-peter": "Gästefotos verstehen, Einwand der Gäste ist weg",
    "13-sabine-markus": "Rückmeldungen verstehen, dann kostenlos starten",
}

def plain(s): return re.sub(r"\s+", " ", s.replace("<br>", " ")).strip()
def esc(s): return html.escape(s, quote=True)
def url(p): return p["path"] if p["path"].startswith("http") else SITE + p["path"]
def pin_no(p): return p["id"][:2]

def alt(p):
    bits = []
    if p.get("proof"): bits.append(p["proof"] + ".")
    bits.append(plain(p["head"]))
    if p.get("sub"): bits.append(plain(p["sub"]))
    if p.get("steps"): bits.append(", ".join(p["steps"]))
    if p.get("note"): bits.append(p["note"] + ".")
    return f"Pin {pin_no(p)}: " + " ".join(bits)

def label(p):
    pr, el = PRINZIP[p["id"]]
    return f'<p class="pz"><strong>{esc(pr)}</strong> → {esc(el)}</p>'

def card(p):
    note = f'<p class="pin-note">{esc(p["note"])}</p>' if p.get("note") else ""
    return f"""<article class="pin {p['board'].lower()}-p">
<a class="bild" href="assets/pins/{p['id']}.jpg" aria-label="Pin {pin_no(p)} in voller Grösse öffnen"><img src="assets/pins/{p['id']}-500.webp" width="500" height="750" loading="lazy" alt="{esc(alt(p))}"></a>
<p class="pin-tag">{pin_no(p)} · {p['board']}</p>
<h3>{esc(p['title'])}</h3>
{label(p)}
{note}<details><summary>Beschreibung und Keywords</summary>
<p>{esc(p['desc'])}</p>
<p><strong>Keywords:</strong> {esc(p['kw'])}</p>
</details>
</article>"""

def reserve(p):
    return f"""<aside class="reserve">
<a class="bild" href="assets/pins/{p['id']}.jpg" aria-label="Pin {pin_no(p)} in voller Grösse öffnen"><img src="assets/pins/{p['id']}-500.webp" width="500" height="750" loading="lazy" alt="{esc(alt(p))}"></a>
<div>
<p class="eyebrow">Pin {pin_no(p)} · {esc(p['status'])}</p>
<h3>{esc(p['title'])}</h3>
{label(p)}
<p>Dieser Pin ist gestaltet, aber nicht eingeplant. Er gehört zur Kampagne, sobald eine Zielseite die Checkliste gegen die E-Mail-Adresse abgibt.</p>
</div>
</aside>"""

def mock(p):
    t = p["title"]
    short = t[:40].rstrip() + "…"
    return f"""<div class="mock">
<div class="mock-txt">
<p class="eyebrow">Mockup, kein Screenshot</p>
<h3>So erscheint Pin {pin_no(p)} bei der Suche «Hochzeitswebseite erstellen»</h3>
<p>Das Keyword steht vorne im Titel, damit es auch nach rund 40 Zeichen noch sichtbar ist. Der Text im Bild beantwortet die Suche auf den ersten Blick.</p>
<p class="klein">Vereinfachte Darstellung des Teams. Die grauen Flächen stehen für andere Treffer. Eine Position in den Resultaten ist damit nicht belegt.</p>
</div>
<figure class="mock-feed" aria-label="Mockup eines Suchresultats mit Pin {pin_no(p)} und grauen Flächen für andere Treffer">
<div class="mock-such" aria-hidden="true">Hochzeitswebseite erstellen</div>
<div class="mock-grid">
<div class="mock-leer h1" aria-hidden="true">Anderer Treffer</div>
<div class="mock-pin"><img src="assets/pins/{p['id']}-500.webp" width="500" height="750" loading="lazy" alt="{esc(alt(p))}"><p>{esc(short)}</p></div>
<div class="mock-leer h2" aria-hidden="true">Anderer Treffer</div>
<div class="mock-leer h3" aria-hidden="true">Anderer Treffer</div>
</div>
</figure>
</div>"""

def row(p):
    u = url(p)
    shown = u.replace("https://", "") if "app." in u else u.replace(SITE, "")
    extra = f' <em>({esc(p["status"])})</em>' if p.get("reserve") else ""
    return (f'<tr><th scope="row">{pin_no(p)} {esc(plain(p["head"])[:60] + ("…" if len(plain(p["head"])) > 60 else ""))}</th>'
            f'<td data-l="Ziel"><a href="{esc(u)}">{esc(shown)}</a></td>'
            f'<td data-l="Danach">{esc(NEXT[p["id"]])}{extra}</td></tr>')

def inject(src, name, content):
    pat = re.compile(rf"(<!-- {name}:START -->).*?(<!-- {name}:END -->)", re.S)
    assert pat.search(src), name
    return pat.sub(lambda m: m.group(1) + "\n" + content + "\n" + m.group(2), src)

# Kleiner Markdown-Wandler: genug für die Dateien in docs/
def inline(s):
    s = esc(s).replace("&#x27;", "'")
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(https?://[^\s|)»«]+?)([.,]?)(?=\s|$|<|»)", r'<a href="\1">\1</a>\2', s)
    return s

def md(text, shift=1):
    out, lines, i = [], text.split("\n"), 0
    while i < len(lines):
        l = lines[i]
        if not l.strip(): i += 1; continue
        m = re.match(r"(#+) (.*)", l)
        if m:
            lvl = min(len(m.group(1)) + shift, 4)
            out.append(f"<h{lvl}>{inline(m.group(2))}</h{lvl}>"); i += 1; continue
        if l.startswith("```"):
            j = i + 1; buf = []
            while not lines[j].startswith("```"): buf.append(lines[j]); j += 1
            out.append("<pre>" + esc("\n".join(buf)) + "</pre>"); i = j + 1; continue
        if l.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split(" | ")]); i += 1
            head, body = rows[0], rows[2:]
            t = '<div class="tbl-scroll" tabindex="0" role="region" aria-label="Tabelle"><table class="tbl doc-t"><thead><tr>' + "".join(f'<th scope="col">{inline(c)}</th>' for c in head) + "</tr></thead><tbody>"
            t += "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in body)
            out.append(t + "</tbody></table></div>"); continue
        if l.startswith("- "):
            buf = []
            while i < len(lines) and lines[i].startswith("- "):
                buf.append(f"<li>{inline(lines[i][2:])}</li>"); i += 1
            out.append("<ul>" + "".join(buf) + "</ul>"); continue
        out.append(f"<p>{inline(l)}</p>"); i += 1
    return "\n".join(out)

def doc(name):
    t = (ROOT / "docs" / name).read_text(encoding="utf-8")
    return md(re.sub(r"^# .*\n", "", t, count=1))

def status_table():
    rows = []
    for p in PINS:
        rows.append(f'<tr><th scope="row">{pin_no(p)}</th><td>{esc(p["board"])}</td><td>{esc(p["title"])}</td><td>{esc(p["status"] or "Bereit")}</td><td>{esc(p.get("later", ""))}</td></tr>')
    return ('<div class="tbl-scroll" tabindex="0" role="region" aria-label="Stand der Pins"><table class="tbl doc-t"><thead><tr><th scope="col">Pin</th><th scope="col">Board</th><th scope="col">Titel</th><th scope="col">Stand</th><th scope="col">Später</th></tr></thead><tbody>'
            + "".join(rows) + "</tbody></table></div>")

def prozess():
    return f"""<!doctype html>
<html lang="de-CH">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Prozess: Einmal reicht. Pinterest-Kampagne für Loveplanr</title>
<meta name="description" content="Stand der Pins, offene Punkte, Prompt-Log, AI-Fehler und Quellen der Kampagne «Einmal reicht.».">
<meta name="robots" content="noindex">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 29'%3E%3Cpath fill='%23db7f74' d='M16 29S0 19 0 8.5C0 3.7 3.7 0 8.3 0 11.4 0 14.3 1.7 16 4.4 17.7 1.7 20.6 0 23.7 0 28.3 0 32 3.7 32 8.5 32 19 16 29 16 29z'/%3E%3C/svg%3E">
<link rel="stylesheet" href="../assets/site.css">
</head>
<body>
<a class="skip" href="#inhalt">Zum Inhalt</a>
<header class="top">
  <a class="mark" href="../">Einmal reicht<span aria-hidden="true">.</span></a>
  <nav aria-label="Bereiche">
    <a href="#stand">Stand der Pins</a>
    <a href="#offen">Offene Punkte</a>
    <a href="#log">Prompt-Log</a>
    <a href="#fehler">AI-Fehler</a>
    <a href="#quellen">Quellen</a>
    <a href="../">Zur Kampagne</a>
  </nav>
</header>
<main id="inhalt" class="prozess">
<div class="wrap">
<h1>Prozess</h1>
<p class="lead">Die Website ist mit KI entstanden, mit Claude Code. Die Prompts stehen im Wortlaut im Log, jede Änderung ist als <a href="https://github.com/ybenb/loveplanr-kampagne/commits/main/">Commit</a> belegt, jeder auffällige Fehler ist festgehalten. Screenshots der Iterationen liegen in <a href="https://github.com/ybenb/loveplanr-kampagne/tree/main/docs/iterationen">docs/iterationen</a>.</p>
<section id="stand"><h2>Stand der Pins</h2>{status_table()}</section>
<section id="offen"><h2>Offene Punkte</h2>{doc("offene-punkte.md")}</section>
<section id="log"><h2>Prompt-Log</h2>{doc("prompt-log.md")}</section>
<section id="fehler"><h2>AI-Fehler</h2>{doc("ai-fehler.md")}</section>
<section id="quellen"><h2>Quellen</h2>{doc("quellen-und-platzhalter.md")}</section>
</div>
</main>
<footer class="foot"><div class="wrap"><p><strong>Studentisches Projekt.</strong> Kurs «Digital Marketing for Start-ups», ZHAW, HS 2026, Team 4. Kein offizieller Auftritt von Loveplanr.</p></div></footer>
</body>
</html>
"""

def main():
    f = ROOT / "index.html"
    s = f.read_text(encoding="utf-8")
    wall = [p for p in PINS if not p.get("reserve")]
    assert len(wall) == 12
    s = inject(s, "PINS", "\n".join(card(p) for p in wall))
    s = inject(s, "RESERVE", "\n".join(reserve(p) for p in PINS if p.get("reserve")))
    s = inject(s, "MOCK", mock(next(p for p in PINS if p["id"].startswith("09"))))
    s = inject(s, "FUNNEL", "\n".join(row(p) for p in PINS))
    f.write_text(s, encoding="utf-8")
    d = ROOT / "prozess"
    d.mkdir(exist_ok=True)
    (d / "index.html").write_text(prozess(), encoding="utf-8")

if __name__ == "__main__":
    main()
