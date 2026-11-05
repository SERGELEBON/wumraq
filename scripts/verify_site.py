#!/usr/bin/env python3
"""Verify the built WUMRAQ site: no SafeNet leftovers, all links/images resolve."""
import os, re, glob

BASE = "/home/z/my-project/site/wumraq-site"
issues = []

# 1. SafeNet leftovers
for p in glob.glob(BASE + "/**/*.*", recursive=True):
    if not p.endswith((".html", ".css", ".js", ".txt")):
        continue
    txt = open(p, encoding="utf-8", errors="replace").read()
    for m in re.finditer(r"safenet|0257942851|054 785 8573|055-287-3077|Trasacco|Adjetey Adjei|Adjirigano|Tracy Naa|tidio|elfsight|AW-17680564122", txt, re.I):
        issues.append(f"LEFTOVER {os.path.relpath(p, BASE)}: ...{txt[max(0,m.start()-40):m.end()+40]}...")

# 2. internal links + images resolve
def resolve(ref, page_path):
    if ref.startswith(("http", "//", "mailto:", "tel:", "javascript", "data:", "#")):
        return None
    ref = ref.split("#")[0]
    if not ref:
        return None
    base_dir = os.path.dirname(page_path)
    return os.path.normpath(os.path.join(base_dir, ref.replace("&amp;", "&")))

for p in glob.glob(BASE + "/**/index.html", recursive=True):
    html = open(p, encoding="utf-8", errors="replace").read()
    for attr, val in re.findall(r'(href|src)="([^"]+)"', html):
        r = resolve(val, p)
        if r is None:
            continue
        if not os.path.exists(r):
            issues.append(f"BROKEN {os.path.relpath(p, BASE)}: {val}")

# 3. spot-check new content present
checks = {
    "index.html": ["Wumraq Security Services Ltd", "24-Hour Security Guards", "Guard Dog Services",
                   "0246029009", "0264019009", "info@wumraqlimited.com", "Civil Engineering &amp; Earthworks",
                   "0e8a3e"],
    "2/about-us/index.html": ["Wumraq Limited", "guard dog teams"],
    "3/11/24-hour-security-guards/index.html": ["24-hour security services focus on"],
    "3/4/road-construction-engineering/index.html": ["road construction and engineering works"],
    "5/1/5/kwabena-osei-bonsu/index.html": ["Kwabena Osei-Bonsu", "Managing Director"],
    "20/contacts/index.html": ["0246029009", "0264019009", "wumraqlimited.com"],
    "6/news/index.html": ["Rebranding private security companies"],
}
for rel, needles in checks.items():
    html = open(os.path.join(BASE, rel), encoding="utf-8", errors="replace").read()
    for nd in needles:
        if nd not in html:
            issues.append(f"MISSING in {rel}: {nd}")

# 4. images sanity (non-empty, not blank)
from PIL import Image
import numpy as np
for p in glob.glob(BASE + "/img/**/*.jpg", recursive=True) + glob.glob(BASE + "/img/**/*.png", recursive=True):
    try:
        im = Image.open(p)
        arr = np.asarray(im.convert("L"))
        if arr.std() < 5:
            issues.append(f"BLANK IMAGE: {p}")
        if os.path.getsize(p) < 1000:
            issues.append(f"TINY IMAGE: {p}")
    except Exception as e:
        issues.append(f"BAD IMAGE {p}: {e}")

print(f"{len(issues)} issues")
for i in issues[:60]:
    print(" -", i)
