#!/usr/bin/env python3
"""Scan downloaded CSS files for url() references and download missing sub-assets (fonts, images)."""
import re, os, urllib.parse, urllib.request, time

OUT = "/home/z/my-project/site/original"
BASE = "https://www.safenetsecuritygh.com/"
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0 Safari/537.36"}

refs = {}
for root, _, files in os.walk(OUT):
    for fn in files:
        if not fn.endswith((".css", ".js")):
            continue
        fp = os.path.join(root, fn)
        rel_dir = os.path.relpath(os.path.dirname(fp), OUT)
        try:
            txt = open(fp, encoding="utf-8", errors="replace").read()
        except Exception:
            continue
        for m in re.findall(r"""url\(\s*['"]?([^'")]+)['"]?\s*\)""", txt):
            if m.startswith(("data:", "http://", "https://", "#")):
                continue
            # resolve relative to the css file dir
            full = os.path.normpath(os.path.join(rel_dir, m.split("?")[0].split("#")[0])).replace("\\", "/")
            refs.setdefault(full, set()).add(fp)

print(f"{len(refs)} referenced sub-assets")
need = []
for rel, srcs in sorted(refs.items()):
    dest = os.path.join(OUT, rel)
    if os.path.exists(dest) and os.path.getsize(dest) > 0:
        continue
    need.append(rel)
    url = BASE + urllib.parse.quote(rel)
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, timeout=60) as r:
            data = r.read()
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, "wb") as f:
            f.write(data)
        print(f"OK   {rel:60s} {len(data):>9d}B")
    except Exception as e:
        print(f"FAIL {rel:60s} {e}")
    time.sleep(0.1)

# stubs for dead links
for stub in ["css/form.css", "css/calendar/style.css", "cs/calendar/js/main.js"]:
    dest = os.path.join(OUT, stub)
    if not os.path.exists(dest):
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        open(dest, "w").write("/* original file missing on source site (404) - empty stub */")
        print("STUB", stub)
