#!/usr/bin/env python3
"""Download every local asset referenced by the downloaded pages, preserving paths."""
import re, os, urllib.parse, urllib.request, time

OUT = "/home/z/my-project/site/original"
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0 Safari/537.36"}
BASE = "https://www.safenetsecuritygh.com/"

# 1. rescan all downloaded pages for ./ assets (covers page-specific images)
assets = set()
pages_dir = os.path.join(OUT, "pages")
page_files = ["index.html"] + [os.path.join("pages", f) for f in os.listdir(pages_dir)]
for rel_fn in page_files:
    fp = os.path.join(OUT, rel_fn)
    html = open(fp, encoding="utf-8", errors="replace").read()
    for m in re.findall(r'(?:src|href)="(\./[^"]+)"', html):
        assets.add(m)
    for m in re.findall(r"url\('\./([^']+)'\)", html):
        assets.add("./" + m)
    for m in re.findall(r'data-background="(\./[^"]+)"', html):
        assets.add(m)

print(f"{len(assets)} unique assets to download")
ok, fail = 0, []
for a in sorted(assets):
    rel = a[2:]  # strip ./
    # URL-decode (images with & in filename are stored encoded)
    rel_dec = urllib.parse.unquote(rel)
    url = BASE + rel_dec.replace("&", "%26")
    dest = os.path.join(OUT, rel_dec)
    if os.path.exists(dest) and os.path.getsize(dest) > 0:
        ok += 1
        continue
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, timeout=60) as r:
            data = r.read()
        with open(dest, "wb") as f:
            f.write(data)
        ok += 1
        print(f"OK   {rel_dec:65s} {len(data):>9d}B")
    except Exception as e:
        fail.append((rel_dec, str(e)))
        print(f"FAIL {rel_dec:65s} {e}")
    time.sleep(0.15)

print(f"\nDownloaded OK: {ok}   Failed: {len(fail)}")
for f_, e in fail:
    print("  FAILED:", f_, e)
