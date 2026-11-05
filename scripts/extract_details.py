#!/usr/bin/env python3
"""Extract full detailed content from service/news detail pages of the user's own site."""
import re
import json
from pathlib import Path
from bs4 import BeautifulSoup

SRC = Path('/home/z/my-project/site-analysis')

def clean(t):
    return re.sub(r'\s+', ' ', t).strip()

def extract_main(fname):
    html = (SRC / fname).read_text(encoding='utf-8', errors='ignore')
    soup = BeautifulSoup(html, 'lxml')
    for s in soup.select('script, style, nav.navbar, .navbar, header.header, footer.footer, .footer-area, .copyright-area, .top-footer, .contact-form-wrap'):
        s.decompose()
    # find main article / detail area
    details = soup.select('.blog-details, .service-details, .services-details, .details, article, .row .col-lg-8, .col-lg-9, .col-md-12.detail')
    if details:
        for d in details:
            cls = ' '.join(d.get('class', []))
            print(f"\n### [{cls}]")
            print(clean(d.get_text(' ', strip=True))[:6000])
    else:
        body = soup.find('body')
        print(clean(body.get_text(' ', strip=True))[:6000])

files = ['svc-corporate.html', 'svc-industrial.html', 'svc-mobile-patrol.html', 'svc-event.html',
         'svc-executive.html', 'svc-cctv.html', 'svc-alarm.html', 'svc-vehicle.html',
         'svc-biometric.html', 'post-trusted.html']
for f in files:
    print(f"\n{'='*70}\nFILE: {f}\n{'='*70}")
    extract_main(f)
