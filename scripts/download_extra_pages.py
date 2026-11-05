#!/usr/bin/env python3
"""Download the 10 additional discovered pages + ../ assets, then rescan everything."""
import re, os, urllib.parse, urllib.request, time

BASE = "https://www.safenetsecuritygh.com/"
OUT = "/home/z/my-project/site/original"
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0 Safari/537.36"}

EXTRA_PAGES = [
    "5/1/5/tracy-naa-adoley-acquaye",
    "6/2/rebranding-private-security-companies",
    "9/1/integrity",
    "9/2/our-vision",
    "9/2/professionalism",
    "9/3/our-mission",
    "9/3/vigilance",
    "9/4/client-centered-service",
    "9/5/innovation",
    "9/6/respect",
]

def fetch(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()

for p in EXTRA_PAGES:
    try:
        data = fetch(BASE + p)
        safe = p.replace("/", "_")
        fp = os.path.join(OUT, "pages", safe + ".html")
        open(fp, "wb").write(data)
        print(f"OK  {p:50s} {len(data):>8d}B")
    except Exception as e:
        print(f"ERR {p}: {e}")
    time.sleep(0.3)

# now collect ALL ../ and ./ asset refs across all pages
assets = set()
for fn in ["index.html"] + [os.path.join("pages", f) for f in os.listdir(os.path.join(OUT, "pages"))]:
    fp = os.path.join(OUT, fn)
    html = open(fp, encoding="utf-8", errors="replace").read()
    for m in re.findall(r'(?:src|href)="((?:\.\./|\./)[^"]+\.(?:jpg|jpeg|png|gif|webp|svg|ico))"', html, re.I):
        assets.add(m)

print(f"\n{len(assets)} image assets:")
missing = []
for a in sorted(assets):
    rel = os.path.normpath(a)
    dest = os.path.join(OUT, rel)
    if os.path.exists(dest) and os.path.getsize(dest) > 0:
        continue
    missing.append(a)
    url = BASE + rel.replace("&", "%26")
    try:
        data = fetch(url)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        open(dest, "wb").write(data)
        print(f"OK   {rel:70s} {len(data):>9d}B")
    except Exception as e:
        print(f"FAIL {rel:70s} {e}")
    time.sleep(0.2)
if not missing:
    print("All already present.")
