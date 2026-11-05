#!/usr/bin/env python3
"""Download all pages of safenetsecuritygh.com and all referenced local assets."""
import re, os, urllib.parse, urllib.request, time, sys

BASE = "https://www.safenetsecuritygh.com/"
OUT = "/home/z/my-project/site/original"
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0 Safari/537.36"}

PAGES = [
    "",  # home
    "2/about-us",
    "3/professional-security-services-in-ghana",
    "6/news",
    "7/our-clients",
    "5/team",
    "20/contacts",
    "3/1/corporate-manned-guarding",
    "3/2/mobile-patrol-services",
    "3/3/event-security-management",
    "3/4/executive-protection",
    "3/5/cctv-installation-and-monitoring",
    "3/6/alarm-response-and-rapid-intervention",
    "3/9/vehicle-tracking-solutions",
    "3/10/biometric-access-control-systems",
    "3/11/industrial-manned-guarding",
    "3/6/delivering-trusted-security-and-surveillance",
]

def fetch(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()

def save_page(path, content):
    # map "2/about-us" -> pages/2_about-us.html ; "" -> index.html
    if path == "":
        fp = os.path.join(OUT, "index.html")
    else:
        safe = path.replace("/", "_")
        fp = os.path.join(OUT, "pages", safe + ".html")
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    with open(fp, "wb") as f:
        f.write(content)
    return fp

assets = set()
page_reports = []
for p in PAGES:
    url = BASE + p
    try:
        data = fetch(url)
        fp = save_page(p, data)
        html = data.decode("utf-8", errors="replace")
        # collect local assets: img src, link href (css), script src, favicon
        for m in re.findall(r'(?:src|href)="(\./[^"]+)"', html):
            assets.add(m)
        n_imgs = len(re.findall(r'<img', html))
        page_reports.append((p or "index", len(data), fp, n_imgs))
        print(f"OK  {p or 'index':55s} {len(data):>8d}B  imgs:{n_imgs}  -> {os.path.basename(fp)}")
    except Exception as e:
        print(f"ERR {p}: {e}")
    time.sleep(0.3)

print("\n=== unique local assets referenced ===")
for a in sorted(assets):
    print(a)
open(os.path.join(OUT, "assets_list.txt"), "w").write("\n".join(sorted(assets)))
