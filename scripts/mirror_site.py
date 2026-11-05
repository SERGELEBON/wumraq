#!/usr/bin/env python3
"""Download all pages + assets from safenetsecuritygh.com (v2, proper urljoin)"""
import os, re, urllib.parse, urllib.request

BASE = "https://www.safenetsecuritygh.com/"
OUT = "/home/z/my-project/site_original"
os.makedirs(OUT, exist_ok=True)

HEADERS = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"}
PAGE_RE = re.compile(r'(?:href|data-bg|data-background)=["\']([^"\']+)["\']', re.I)
ASSET_RE = re.compile(r'(?:src|href|content)=["\']([^"\']+\.(?:css|js|png|jpe?g|gif|svg|webp|ico|woff2?|ttf|eot|mp4|webm|pdf|otf))["\']', re.I)
CSSURL_RE = re.compile(r'url\(["\']?([^"\')]+)["\']?\)')

def local_name(url):
    p = urllib.parse.urlparse(url)
    name = p.path.lstrip("/")
    name = name.replace("../", "")
    if name == "" or name.endswith("/"):
        name += "index.html"
    return urllib.parse.unquote(name)

def fetch(url):
    dest = local_name(url)
    path = os.path.join(OUT, dest)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if os.path.exists(path) and os.path.getsize(path) > 0:
        return dest
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=30) as r:
            data = r.read()
        with open(path, "wb") as f:
            f.write(data)
        print(f"OK  {len(data):>9}  {dest}")
        return dest
    except Exception as e:
        print(f"ERR {url} -> {e}")
        return None

def rel_url(attr_val, page_url):
    attr_val = attr_val.strip().strip('"\'')
    if attr_val.startswith(("#", "mailto:", "tel:", "javascript:", "data:")):
        return None
    absu = urllib.parse.urljoin(page_url, attr_val)
    p = urllib.parse.urlparse(absu)
    if p.netloc and "safenetsecuritygh.com" not in p.netloc:
        return None
    return urllib.parse.urlparse(absu).path or "/"

def scan_html(html, page_url):
    for m in ASSET_RE.findall(html):
        r = rel_url(m, page_url)
        if r:
            queue_assets.append(r)
    for m in PAGE_RE.findall(html):
        r = rel_url(m, page_url)
        if r and (r.endswith(".html") or r.endswith("/") or "." not in r.rstrip("/").split("/")[-1]):
            r = r.split("?")[0].split("#")[0]
            if r:
                queue_pages.append(r)

queue_pages = ["/"]
queue_assets = []
seen_p, seen_a = set(), set()

while queue_pages:
    path = queue_pages.pop(0)
    if path in seen_p:
        continue
    seen_p.add(path)
    dest = fetch(BASE.rstrip("/") + path)
    if not dest or not dest.endswith(".html"):
        continue
    html = open(os.path.join(OUT, dest), encoding="utf-8", errors="ignore").read()
    scan_html(html, BASE.rstrip("/") + path)

while queue_assets:
    a = queue_assets.pop(0)
    if a in seen_a:
        continue
    seen_a.add(a)
    adest = fetch(urllib.parse.urljoin(BASE, a))
    if adest and adest.endswith(".css"):
        try:
            css = open(os.path.join(OUT, adest), encoding="utf-8", errors="ignore").read()
        except Exception:
            continue
        for cm in CSSURL_RE.findall(cm if False else css):
            if cm.startswith("data:"):
                continue
            ca = urllib.parse.urljoin(urllib.parse.urljoin(BASE, a), cm)
            p = urllib.parse.urlparse(ca)
            if p.netloc and "safenetsecuritygh.com" not in p.netloc:
                continue
            queue_assets.append(p.path)

print("\nDONE. Pages:", len(seen_p), "Assets:", len(seen_a))
