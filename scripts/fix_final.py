#!/usr/bin/env python3
"""Apply final fixes to the WUMRAQ static build:
1. Brand colors: green #0e8a3e/#052e18 -> teal #12806c/#05302b (+ tints)
2. Remove "Powered by Nero One Solutions" credit
3. Neutralize invented director -> generic "Managing Director" profile
4. Delete orphan SafeNet images
"""
import os, re, shutil, glob

BASE = "/home/z/my-project/download/wumraq-website"

# ---------- 1. colors ----------
COLOR_MAP = [
    ("#0e8a3e", "#12806c"),
    ("#052e18", "#05302b"),
    ("#dff2e4", "#dff0ec"),
    ("#e2f1e6", "#e2f1ee"),
    ("#0E8A3E", "#12806c"),
    ("#052E18", "#05302b"),
]
n_files = 0
for p in glob.glob(BASE + "/**/*.html", recursive=True) + glob.glob(BASE + "/css/*.css"):
    txt = open(p, encoding="utf-8", errors="replace").read()
    orig = txt
    for a, b in COLOR_MAP:
        txt = txt.replace(a, b)
    if txt != orig:
        open(p, "w", encoding="utf-8").write(txt)
        n_files += 1
print(f"colors: {n_files} files updated")

# ---------- 2. Nero credit ----------
CREDIT = " | Powered by <a href='http://neroonesolutions.com' target='_blank'>Nero One Solutions</a>"
n = 0
for p in glob.glob(BASE + "/**/index.html", recursive=True) + [BASE + "/index.html"]:
    if not os.path.exists(p):
        continue
    txt = open(p, encoding="utf-8", errors="replace").read()
    if CREDIT in txt:
        txt = txt.replace(CREDIT, "")
        open(p, "w", encoding="utf-8").write(txt)
        n += 1
print(f"nero credit removed from {n} pages")

# ---------- 3. director neutralization ----------
OLD_DIR = os.path.join(BASE, "5/1/5/kwabena-osei-bonsu")
NEW_DIR = os.path.join(BASE, "5/1/5/managing-director")
if os.path.exists(OLD_DIR):
    shutil.move(OLD_DIR, NEW_DIR)
OLD_IMG = os.path.join(BASE, "img/staff/kwabena_osei_bonsu.jpg")
NEW_IMG = os.path.join(BASE, "img/staff/managing_director.jpg")
if os.path.exists(OLD_IMG):
    shutil.move(OLD_IMG, NEW_IMG)

MEMBER_BIO = """<p>Wumraq Security Services Ltd is led by an experienced Managing Director supported by a dedicated management team. The Director oversees core operations in finance, client relations, marketing, and human capital, and works hand in hand with the road and building engineering division of Wumraq Limited to deliver consistent, measurable results for corporate and institutional clients across Ghana.</p>

<p><br />
Under this leadership, Wumraq operates as a combined security and engineering group: 24-hour security guards, professional guard dog services, and dedicated teams for offices, homes, and warehouses, alongside road and building engineering works. The management approach is strategic, disciplined, and focused on continuous improvement across teams&nbsp;and&nbsp;operations.</p>
"""

def fix_member_page():
    p = os.path.join(NEW_DIR, "index.html")
    txt = open(p, encoding="utf-8", errors="replace").read()
    txt = txt.replace("Wumraq Security Services Ltd - kwabena osei-bonsu",
                      "Wumraq Security Services Ltd - managing director")
    txt = txt.replace('src="../../../../img/staff/kwabena_osei_bonsu.jpg"',
                      'src="../../../../img/staff/managing_director.jpg"')
    txt = txt.replace('alt="Kwabena Osei-Bonsu "', 'alt="Managing Director of Wumraq Security Services Limited"')
    txt = txt.replace("<h3>Kwabena Osei-Bonsu </h3>", "<h3>Managing Director</h3>")
    txt = txt.replace("<h6>Managing Director</h6>", "<h6>Wumraq Security Services Ltd</h6>")
    i = txt.find('<div class="details">')
    j = txt.find('<div class="text-center mt-5">')
    assert i != -1 and j != -1
    txt = txt[:i] + '<div class="details">' + MEMBER_BIO + txt[j - len("</div>\n        </div>\n    </div>\n    <div class=\"seperator2 w-100 mb-4 mt-0\"></div>\n    "):]
    open(p, "w", encoding="utf-8").write(txt)
    print("member page fixed")

fix_member_page()

def fix_team_page():
    p = os.path.join(BASE, "5/team/index.html")
    txt = open(p, encoding="utf-8", errors="replace").read()
    txt = txt.replace('href="../../5/1/5/kwabena-osei-bonsu"', 'href="../../5/1/5/managing-director"')
    txt = txt.replace('src="../../img/staff/kwabena_osei_bonsu.jpg"', 'src="../../img/staff/managing_director.jpg"')
    txt = txt.replace('alt="Kwabena Osei-Bonsu "', 'alt="Managing Director of Wumraq Security Services Limited"')
    txt = txt.replace('<h5 class="text-capitalize">Kwabena Osei-Bonsu </h5>',
                      '<h5 class="text-capitalize">Managing Director</h5>')
    txt = txt.replace('<h4 class="name text-2">Managing Director</h4>',
                      '<h4 class="name text-2">Wumraq Security Services Ltd</h4>')
    open(p, "w", encoding="utf-8").write(txt)
    print("team page fixed")

fix_team_page()

# ---------- 4. orphan SafeNet images ----------
ORPHANS = [
    "img/services/biometric_access_control_systems1031152757.png",
    "img/services/corporate_manned_guarding2069672904.jpg",
    "img/services/event_security_management927651658.png",
    "img/services/mobile_patrol_services1940947803.png",
    "img/services/alarm_response_&_rapid_intervention22333877.jpg",
    "img/services/vip_escort_&_personal_protection587143962.jpg",
    "img/services/_industrial_manned_guarding1942854346.png",
    "img/services/cctv_installation_&_monitoring1586465675.jpg",
    "img/services/vehicle_tracking_solutions267077206.jpg",
    "img/staff/tracy_naa_adoley_acquaye_.jpg",
    "img/clients/Orchard_Asset_Financing.jpg",
    "img/clients/Premium_Purpose_Ltd.jpg",
    "img/clients/Cleanlife__Company_Ltd.jpg",
    "img/clients/East_Midas_Properties.jpg",
    "img/contents/safenet_security_services_ghana_1369868501.jpg",
]
n = 0
for rel in ORPHANS:
    p = os.path.join(BASE, rel)
    if os.path.exists(p):
        os.remove(p)
        n += 1
print(f"orphans deleted: {n}")

print("DONE")
