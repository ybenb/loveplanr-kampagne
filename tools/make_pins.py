#!/usr/bin/env python3
"""Rendert die Pins (1000x1500 px) mit Chrome headless aus den lokalen Originalfotos.
Aufruf: python3 tools/make_pins.py  (braucht assets/originals/, Chrome und macOS sips)"""
import csv, html, pathlib, shutil, subprocess, sys, tempfile
ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from pins_data import PINS, PRINZIP, pin_url
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
ORIG, OUT = ROOT / "assets/originals", ROOT / "assets/pins"
HEART = '<svg class="h" viewBox="0 0 32 29" aria-hidden="true"><path fill="currentColor" d="M16 29S0 19 0 8.5C0 3.7 3.7 0 8.3 0 11.4 0 14.3 1.7 16 4.4 17.7 1.7 20.6 0 23.7 0 28.3 0 32 3.7 32 8.5 32 19 16 29 16 29z"/></svg>'
LOGO = f'<div class="logo">L{HEART}VEPLANR</div>'
CSS = """*{box-sizing:border-box;margin:0}html,body{width:1000px;height:1500px;overflow:hidden}
body{font-family:"Avenir Next",Avenir,Helvetica,sans-serif;color:#262626;position:relative;background:#fff6f3}
h1{font-family:Didot,"Bodoni 72",Georgia,serif;font-weight:400;line-height:1.04;letter-spacing:-.01em}
.logo{font-weight:600;letter-spacing:.24em;font-size:30px;display:flex;align-items:center}.h{width:30px;height:27px;margin:0 .22em 0 .2em;color:#db7f74}
.sub{font-size:39px;line-height:1.28;font-weight:500}
img.bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.photo .shade{position:absolute;inset:0}.photo.top .shade{background:linear-gradient(180deg,rgba(25,18,16,.68),rgba(25,18,16,.12) 52%,rgba(25,18,16,.5))}
.photo.bottom .shade{background:linear-gradient(0deg,rgba(25,18,16,.88),rgba(25,18,16,.62) 42%,rgba(25,18,16,0) 70%)}
.photo .txt{position:absolute;left:68px;right:68px;color:#fff}.photo.top .txt{top:90px}.photo.bottom .txt{bottom:150px}
.photo h1{font-size:112px;margin-bottom:28px}.photo .logo{position:absolute;left:68px;bottom:62px;color:#fff}.photo .h{color:#f0a79e}
.split .pic{position:absolute;inset:0 0 auto 0;height:840px;overflow:hidden}.split .pic img{width:100%;height:100%;object-fit:cover;display:block}
.split .block{position:absolute;inset:840px 0 0 0;padding:66px 68px}.split h1{font-size:92px;margin-bottom:26px}.split .logo{position:absolute;left:68px;bottom:56px}
.rose .block{background:#db7f74;color:#262626}.rose .h{color:#fff}.ink .block{background:#262626;color:#fff6f3}.sand .block{background:#eee7e4}
.list .pic{position:absolute;inset:0 0 auto 0;height:430px;overflow:hidden}.list .pic img{width:100%;height:100%;object-fit:cover;display:block}
.list .block{position:absolute;inset:430px 0 0 0;padding:56px 68px;background:#fff6f3}.list h1{font-size:84px;margin-bottom:38px}
.list ol{list-style:none;padding:0}.list li{font-size:42px;font-weight:500;display:flex;align-items:center;gap:30px;padding:17px 0;border-top:2px solid #e8d8d2}
.list b{font:400 58px Didot,Georgia,serif;color:#db7f74;width:48px}.list .logo{position:absolute;left:68px;bottom:50px}
.proof{display:inline-block;background:#fff6f3;color:#262626;font-size:32px;font-weight:600;padding:10px 20px;margin-bottom:26px}
.sym{position:absolute;top:30px;right:30px;font-size:23px;font-weight:600;letter-spacing:.04em;color:#fff;background:rgba(25,18,16,.6);padding:7px 14px}
.stamp{position:absolute;right:68px;bottom:44px;width:128px;height:128px;border-radius:50%;display:flex;align-items:center;justify-content:center;font:400 68px Didot,Georgia,serif;background:#fff6f3;color:#262626;box-shadow:0 0 0 3px #fff6f3,0 0 0 6px #db7f74}
"""
def stamp(p): return '<div class="stamp">1×</div>' if p.get("stamp") else ""
def proof(p): return f'<p class="proof">{p["proof"]}</p>' if p.get("proof") else ""
def sym(p): return f'<div class="sym">{p["note"]}</div>' if p.get("note") else ""
def hs(p): return f' style="font-size:{p["hsize"]}px;line-height:1.14"' if p.get("hsize") else ""
def body(p, photo):
    e = lambda s: s  # Inhalte stammen aus pins_data.py und enthalten bewusst <br>
    if p["layout"] == "photo":
        return f'<body class="photo {p["place"]}"><img class="bg" src="{photo}" style="object-position:{p["pos"]}"><div class="shade"></div><div class="txt">{proof(p)}<h1{hs(p)}>{e(p["head"])}</h1><p class="sub">{e(p["sub"])}</p></div>{LOGO}{stamp(p)}{sym(p)}</body>'
    if p["layout"] == "split":
        return f'<body class="split {p["color"]}"><div class="pic"><img src="{photo}" style="object-position:{p["pos"]}"></div><div class="block"><h1{hs(p)}>{e(p["head"])}</h1><p class="sub">{e(p["sub"])}</p>{LOGO}{stamp(p)}</div>{sym(p)}</body>'
    if p["layout"] == "list":
        items = "".join(f"<li><b>{i}</b>{html.escape(s)}</li>" for i, s in enumerate(p["steps"], 1))
        return f'<body class="list"><div class="pic"><img src="{photo}" style="object-position:{p["pos"]}"></div><div class="block"><h1>{e(p["head"])}</h1><ol>{items}</ol>{LOGO}</div></body>'
def run(*a): subprocess.run(a, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
def main():
    OUT.mkdir(parents=True, exist_ok=True)
    tmp = pathlib.Path(tempfile.mkdtemp())
    for p in PINS:
        photo = ""
        if p.get("photo"):
            src = tmp / p["photo"]
            if not src.exists(): run("sips", "-Z", "2200", str(ORIG / p["photo"]), "--out", str(src))
            photo = src.as_uri()
        f = tmp / f'{p["id"]}.html'
        f.write_text(f'<!doctype html><meta charset="utf-8"><style>{CSS}</style>{body(p, photo)}', encoding="utf-8")
        png = tmp / f'{p["id"]}.png'
        run(CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--allow-file-access-from-files", f"--user-data-dir={tmp}/chrome", "--force-device-scale-factor=1", "--window-size=1000,1500", f"--screenshot={png}", f.as_uri())
        run("sips", "-s", "format", "jpeg", "-s", "formatOptions", "84", str(png), "--out", str(OUT / f'{p["id"]}.jpg'))
        run("sips", "-z", "750", "500", "-s", "format", "jpeg", "-s", "formatOptions", "74", str(png), "--out", str(OUT / f'{p["id"]}-500.jpg'))
    with open(OUT / "pin-set.csv", "w", newline="", encoding="utf-8-sig") as c:
        w = csv.writer(c, delimiter=";")
        w.writerow(["Datei", "Board", "Titel", "Beschreibung", "Keywords", "Ziel-URL mit UTM", "Prinzip → Element", "Status"])
        for p in PINS: w.writerow([p["id"] + ".jpg", p["board"], p["title"], p["desc"], p["kw"], pin_url(p), " → ".join(PRINZIP[p["id"]]), p["status"] or "bereit"])
    shutil.rmtree(tmp, ignore_errors=True)
if __name__ == "__main__": main()
