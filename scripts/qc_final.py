#!/usr/bin/env python3
"""Comprehensive QC of the final static build (download/wumraq-website)."""
import os, re, glob

BASE = "/home/z/my-project/download/wumraq-website"
issues, notes = [], []

LEFTOVER = re.compile(r"safenet|0257942851|054 785 8573|055-287-3077|Trasacco|Adjetey Adjei|Adjirigano|Tracy Naa|Kwabena|tidio|elfsight|AW-1768|corporate-manned-guarding|mobile-patrol-services|event-security-management|executive-protection|cctv-installation|alarm-response|vehicle-tracking|biometric-access|industrial-manned|delivering-trusted-security|neroone|Nero One", re.I)

# 1. leftovers in text files
for p in glob.glob(BASE + "/**/*", recursive=True):
    if not os.path.isfile(p) or not p.endswith((".html", ".css", ".js", ".txt", ".xml")):
        continue
    txt = open(p, encoding="utf-8", errors="replace").read()
    for m in LEFTOVER.finditer(txt):
        s = max(0, m.start() - 50)
        issues.append(f"LEFTOVER {os.path.relpath(p, BASE)}: ...{txt[s:m.end()+50]!r}...")

# 2. broken internal refs
def resolve(ref, page_path):
    if ref.startswith(("http", "//", "mailto:", "tel:", "javascript", "data:", "#")):
        return None
    ref = ref.split("#")[0].split("?")[0]
    if not ref:
        return None
    return os.path.normpath(os.path.join(os.path.dirname(page_path), ref.replace("&amp;", "&")))

referenced = set()
for p in glob.glob(BASE + "/**/index.html", recursive=True) + [BASE + "/index.html"]:
    if not os.path.exists(p): continue
    html = open(p, encoding="utf-8", errors="replace").read()
    for attr, val in re.findall(r'(href|src|data-bg)="([^"]+)"', html):
        r = resolve(val, p)
        if r is None: continue
        referenced.add(r)
        if not os.path.exists(r):
            issues.append(f"BROKEN {os.path.relpath(p, BASE)} -> {val}")
# CSS url() refs
for p in glob.glob(BASE + "/css/*.css", recursive=True):
    css = open(p, encoding="utf-8", errors="replace").read()
    for val in re.findall(r'url\(["\']?([^"\')]+)["\']?\)', css):
        r = resolve(val, p)
        if r is None: continue
        referenced.add(r)
        if not os.path.exists(r):
            issues.append(f"BROKEN CSS {os.path.relpath(p, BASE)} -> {val}")

# 3. orphan image files (in img/, referenced by nobody)
for p in glob.glob(BASE + "/img/**/*", recursive=True):
    if not os.path.isfile(p): continue
    rp = os.path.normpath(p)
    if rp not in referenced and not rp.endswith((".html",)):
        notes.append(f"ORPHAN {os.path.relpath(p, BASE)} ({os.path.getsize(p)//1024} KB)")

# 4. pages inventory
pages = sorted(os.path.relpath(p, BASE) for p in glob.glob(BASE + "/**/index.html", recursive=True))
notes.append(f"PAGES ({len(pages)}): " + ", ".join(pages))

# 5. brand color audit
for p in glob.glob(BASE + "/css/*.css"):
    css = open(p, encoding="utf-8", errors="replace").read()
    greens = len(re.findall(r"#0e8a3e", css, re.I))
    deeps = len(re.findall(r"#052e18", css, re.I))
    if greens or deeps:
        notes.append(f"COLORS {os.path.relpath(p, BASE)}: #0e8a3e x{greens}, #052e18 x{deeps}")

# 6. key content spot-checks
CHECKS = {
    "index.html": ["0246029009", "0264019009", "info@wumraqlimited.com", "Wumraq"],
    "20/contacts/index.html": ["0246029009", "0264019009"],
    "5/team/index.html": ["Managing Director"],
}
for rel, needles in CHECKS.items():
    p = os.path.join(BASE, rel)
    if not os.path.exists(p):
        issues.append(f"MISSING PAGE {rel}"); continue
    html = open(p, encoding="utf-8", errors="replace").read()
    for nd in needles:
        if nd not in html:
            issues.append(f"MISSING '{nd}' in {rel}")

print("=" * 80)
for i in issues[:60]:
    print(i)
print(f"-- {len(issues)} issues --")
print("-" * 80)
for n in notes:
    print(n)
