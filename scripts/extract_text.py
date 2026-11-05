#!/usr/bin/env python3
"""Extract all visible text + structure from downloaded pages for analysis"""
import os, re, html
from html.parser import HTMLParser

ROOT = "/home/z/my-project/site_original"
OUT = "/home/z/my-project/analysis"
os.makedirs(OUT, exist_ok=True)

PAGES = ["index.html", "2/about-us", "3/professional-security-services-in-ghana",
         "3/1/corporate-manned-guarding", "3/2/mobile-patrol-services", "3/3/event-security-management",
         "3/4/executive-protection", "3/5/cctv-installation-and-monitoring",
         "3/6/alarm-response-and-rapid-intervention", "3/9/vehicle-tracking-solutions",
         "3/10/biometric-access-control-systems", "3/11/industrial-manned-guarding",
         "3/6/delivering-trusted-security-and-surveillance", "5/team", "6/news", "7/our-clients", "20/contacts"]

class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.texts = []
        self.skip = 0
        self.imgs = []
        self.title = ""
        self.in_title = False
    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if tag in ("script", "style", "noscript"):
            self.skip += 1
        if tag == "img":
            self.imgs.append(d.get("src", "") + " | alt=" + d.get("alt", ""))
        if tag == "title":
            self.in_title = True
    def handle_endtag(self, tag):
        if tag in ("script", "style", "noscript") and self.skip:
            self.skip -= 1
        if tag == "title":
            self.in_title = False
    def handle_data(self, data):
        if self.in_title:
            self.title += data
        if self.skip:
            return
        t = data.strip()
        if t:
            self.texts.append(t)

report = []
for p in PAGES:
    fp = os.path.join(ROOT, p)
    raw = open(fp, encoding="utf-8", errors="ignore").read()
    ex = TextExtractor()
    ex.feed(raw)
    title = html.unescape(ex.title.strip())
    # unique lines preserving order
    seen, uniq = set(), []
    for t in ex.texts:
        if t not in seen:
            seen.add(t)
            uniq.append(t)
    imgs = [i for i in ex.imgs if not i.startswith("data:")]
    report.append(f"\n{'='*90}\nPAGE: {p}\nTITLE: {title}\n--- TEXT ---\n" + "\n".join(uniq) + f"\n--- IMAGES ({len(imgs)}) ---\n" + "\n".join(imgs))

open(os.path.join(OUT, "all_text.txt"), "w", encoding="utf-8").write("\n".join(report))
print("written", os.path.join(OUT, "all_text.txt"), os.path.getsize(os.path.join(OUT, "all_text.txt")))
