#!/usr/bin/env python3
"""Extract structured text content from the downloaded HTML pages (user's own site)."""
import re
from pathlib import Path
from bs4 import BeautifulSoup

SRC = Path('/home/z/my-project/site-analysis')

def clean(t):
    return re.sub(r'\s+', ' ', t).strip()

def extract(fname):
    html = (SRC / fname).read_text(encoding='utf-8', errors='ignore')
    soup = BeautifulSoup(html, 'lxml')
    for s in soup.select('script, style, nav.navbar, .navbar, header.header, footer.footer, .footer-area, .copyright-area'):
        s.decompose()
    out = []
    for main in soup.select('main, section, .section, div[class*="banner"], div[class*="about"], div[class*="service"], div[class*="news"], div[class*="blog"], div[class*="team"], div[class*="contact"], div[class*="client"], div[class*="slider"], div[class*="hero"]'):
        cls = ' '.join(main.get('class', []))
        txt = clean(main.get_text(' ', strip=True))
        if txt and len(txt) > 40:
            out.append({'class': cls[:80], 'text': txt[:2500]})
    return out

for f in ['home.html', 'about.html', 'services.html', 'contacts.html', 'team.html', 'news.html', 'clients.html']:
    data = extract(f)
    print(f"\n{'='*70}\nFILE: {f}\n{'='*70}")
    seen = set()
    for i, s in enumerate(data):
        key = s['text'][:100]
        if key in seen:
            continue
        seen.add(key)
        print(f"\n--- [{s['class']}] ---")
        print(s['text'][:1800])
