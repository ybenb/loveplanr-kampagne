#!/usr/bin/env python3
"""Schreibt Pin-Karten und Funnel-Tabelle aus tools/pins_data.py in index.html.
Aufruf: python3 -I tools/build_site.py
So bleiben Website, Pins und CSV bei denselben Texten. Die Website selbst bleibt statisches HTML."""
import html, pathlib, re, sys
ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from pins_data import PINS, SITE

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
}

def plain(s): return re.sub(r"\s+", " ", s.replace("<br>", " ")).strip()
def esc(s): return html.escape(s, quote=True)
def url(p): return p["path"] if p["path"].startswith("http") else SITE + p["path"]

def alt(p):
    bits = [plain(p["head"])]
    if p.get("proof"): bits.insert(0, p["proof"] + ".")
    if p.get("sub"): bits.append(plain(p["sub"]))
    if p.get("steps"): bits.append(", ".join(p["steps"]))
    return f"Pin {p['id'][:2]}: " + " ".join(bits)

def later(p):
    return f"\n<p><strong>Später:</strong> {esc(p['later'])}</p>" if p.get("later") else ""

def card(p):
    warn = f'<span class="warn">{esc(p["status"].split(":")[0])}</span>' if p["status"] else ""
    return f"""<article class="pin {p['board'].lower()}-p">
<a class="bild" href="assets/pins/{p['id']}.jpg" aria-label="Pin {p['id'][:2]} in voller Grösse"><img src="assets/pins/{p['id']}-500.jpg" width="500" height="750" loading="lazy" alt="{esc(alt(p))}"></a>
<p class="pin-tag"><span>{p['id'][:2]} · {p['board']}</span>{warn}</p>
<h3>{esc(p['title'])}</h3>
<details><summary>Beschreibung und Keywords</summary>
<p>{esc(p['desc'])}</p>
<p><strong>Keywords:</strong> {esc(p['kw'])}</p>
<p><strong>Prinzip:</strong> {esc(p['principle'])}</p>{later(p)}
</details>
</article>"""

def row(p):
    u = url(p)
    shown = u.replace("https://", "").replace("loveplanr.com", "", 1) if not "app." in u else u.replace("https://", "")
    if p["status"].startswith("Startfassung"): state = "Startfassung"
    elif p["status"].startswith("Freigabe"): state = '<span class="state-p">Zitat: Freigabe offen</span>'
    elif p["status"]: state = '<span class="state-p">Vorschlag: neue Zielseite</span>'
    else: state = "Bereit"
    return (f'<tr><th scope="row">{p["id"][:2]} {esc(plain(p["head"]))}</th>'
            f'<td data-l="Ziel"><a href="{esc(u)}">{esc(shown)}</a></td>'
            f'<td data-l="Danach">{esc(NEXT[p["id"]])}</td>'
            f'<td data-l="Stand" class="state">{state}</td></tr>')

def inject(src, name, content):
    pat = re.compile(rf"(<!-- {name}:START -->).*?(<!-- {name}:END -->)", re.S)
    assert pat.search(src), name
    return pat.sub(lambda m: m.group(1) + "\n" + content + "\n" + m.group(2), src)

def main():
    f = ROOT / "index.html"
    s = f.read_text(encoding="utf-8")
    s = inject(s, "PINS", "\n".join(card(p) for p in PINS))
    s = inject(s, "FUNNEL", "\n".join(row(p) for p in PINS))
    f.write_text(s, encoding="utf-8")

if __name__ == "__main__":
    main()
