#!/usr/bin/env python3
"""
Build the WUMRAQ site from the mirrored safenetsecuritygh.com clone.
- Keeps the design/template 100% intact (same HTML structure, CSS, JS).
- Replaces: brand, colors (green), services, contacts, images (new AI images).
- Removes SafeNet third-party integrations (tidio chat, GA ads, Elfsight WhatsApp).
"""
import os, re, shutil, glob
from PIL import Image

ORIG = "/home/z/my-project/site/original"
PAGES = os.path.join(ORIG, "pages")
DEST = "/home/z/my-project/site/wumraq-site"
AI = "/home/z/my-project/site/ai-img"
BRAND = "/home/z/my-project/site/brand"

# ---------------------------------------------------------------- services
# order: old slug -> new identity
SERVICES = [
    # (old_slug, new_slug, old_name, new_name)
    ("corporate-manned-guarding", "civil-engineering-earthworks",
     "Corporate Manned Guarding", "Civil Engineering &amp; Earthworks"),
    ("industrial-manned-guarding", "24-hour-security-guards",
     "Industrial Manned Guarding", "24-Hour Security Guards"),
    ("mobile-patrol-services", "renovation-maintenance-works",
     "Mobile Patrol Services", "Renovation &amp; Maintenance Works"),
    ("event-security-management", "building-construction-engineering",
     "Event Security Management", "Building Construction &amp; Engineering"),
    ("executive-protection", "road-construction-engineering",
     "Executive Protection", "Road Construction &amp; Engineering"),
    ("cctv-installation-and-monitoring", "warehouse-security-services",
     "CCTV Installation &amp; Monitoring", "Warehouse Security Services"),
    ("alarm-response-and-rapid-intervention", "residential-security-services",
     "Alarm Response &amp; Rapid Intervention", "Residential Security Services"),
    ("vehicle-tracking-solutions", "office-security-services",
     "Vehicle Tracking Solutions", "Office Security Services"),
    ("biometric-access-control-systems", "guard-dog-services",
     "Biometric Access Control Systems", "Guard Dog Services"),
]

CARD_DESCS = {
    "24-Hour Security Guards":
        "Our uniformed, vetted security guards protect your premises around the clock, with disciplined patrols, gatehouse control, and rapid response...",
    "Guard Dog Services":
        "Professional dog handlers and trained guard dogs provide a powerful visible deterrent for construction sites, warehouses, yards, and compounds...",
    "Office Security Services":
        "We secure offices and corporate premises with front-of-house officers, access control, visitor management, and after-hours protection...",
    "Residential Security Services":
        "Dedicated guards, gatehouse control, and rapid response protect homes, estates, and residential communities day and night...",
    "Warehouse Security Services":
        "We safeguard warehouses, factories, and storage yards against theft and unauthorized access, with gate control and disciplined patrols...",
    "Road Construction &amp; Engineering":
        "Wumraq Limited delivers road construction and engineering works — from earthworks and drainage to surfacing — built to specification...",
    "Building Construction &amp; Engineering":
        "Wumraq Limited undertakes building construction projects from foundations to finishes, with disciplined crews and strict safety standards...",
    "Renovation &amp; Maintenance Works":
        "From refurbishments to planned maintenance, our engineering teams keep your buildings and facilities in excellent condition...",
    "Civil Engineering &amp; Earthworks":
        "Site clearance, excavation, earthmoving, and civil works executed with modern plant and precise, safe, on-schedule delivery...",
}

FULL_DESCS = {
    "24-Hour Security Guards": """<p>Wumraq Security Services Ltd provides trained, licensed, and disciplined security guards for round-the-clock protection of offices, homes, shops, and business premises. Our 24-hour security services focus on:</p>

<p>Day and night guarding by vetted, uniformed, and supervised officers.</p>

<p>Gatehouse management, access control, and visitor verification at every entry point.</p>

<p>Regular foot patrols and perimeter checks to detect and deter risks before they escalate.</p>

<p>Rapid escalation and emergency response coordinated with our operations team.</p>

<p>Our guards combine vigilance with professionalism and discretion, keeping your people, property, and assets protected 24 hours a day.<br />
&nbsp;</p>
""",
    "Guard Dog Services": """<p>Wumraq provides professional guard dog teams for sites that demand a strong and visible deterrent. Our guard dog services focus on:</p>

<p>Trained patrol dogs with licensed handlers for construction sites, warehouses, yards, and open compounds.</p>

<p>High-visibility deterrence that sharply reduces intrusion, trespass, and theft.</p>

<p>Night guarding and perimeter detection where CCTV and manpower alone are not enough.</p>

<p>Strict animal welfare, handling discipline, and public safety protocols at all times.</p>

<p>Every dog team is deployed under experienced handlers, adding a proven, humane, and highly effective layer of protection to your site.<br />
&nbsp;</p>
""",
    "Office Security Services": """<p>Wumraq protects offices, corporate premises, and administrative buildings with discreet, professional security officers. Our office security services focus on:</p>

<p>Reception and front-of-house officers trained to represent your brand.</p>

<p>Access control and visitor management to ensure only authorized persons enter.</p>

<p>After-hours locking routines, patrols, and alarm response for your premises.</p>

<p>Protection of staff, equipment, records, and sensitive company information.</p>

<p>Our officers combine security expertise with courtesy and presentation, creating a safe, welcoming, and well-managed environment for your office.<br />
&nbsp;</p>
""",
    "Residential Security Services": """<p>Wumraq secures homes, estates, and residential communities so families can live with complete peace of mind. Our residential security services focus on:</p>

<p>Dedicated guards for private residences, gated communities, and apartment blocks.</p>

<p>Gatehouse staffing, visitor registration, and vehicle access control.</p>

<p>Perimeter patrols and rapid response, day and night.</p>

<p>Courteous officers trained to protect families, guests, and household staff.</p>

<p>From single homes to entire estates, we design residential security around the way you live &mdash; visible where it deters, discreet where it matters.<br />
&nbsp;</p>
""",
    "Warehouse Security Services": """<p>Wumraq protects warehouses, factories, storage yards, and logistics facilities against theft and unauthorized access. Our warehouse security services focus on:</p>

<p>24-hour guarding of goods, equipment, and loading bays.</p>

<p>Gate control, vehicle search routines, and delivery verification.</p>

<p>Patrols of yards, perimeters, and high-risk storage zones.</p>

<p>Loss-prevention discipline that protects your stock and your margins.</p>

<p>Our officers understand industrial environments and work to your standard operating procedures, keeping operations moving while your assets stay protected.<br />
&nbsp;</p>
""",
    "Road Construction &amp; Engineering": """<p>Wumraq Limited delivers road construction and engineering works for public and private clients across Ghana. Our road engineering services cover:</p>

<p>Road construction, rehabilitation, and upgrades from earthworks to final surfacing.</p>

<p>Drainage systems, culverts, and ancillary road structures built to specification.</p>

<p>Site clearance, fills, and compaction with modern plant and experienced crews.</p>

<p>Quality control, materials testing, and supervision on every phase of the project.</p>

<p>Backed by our own plant and skilled engineers, we deliver durable roads built for Ghana&rsquo;s climate and traffic loads &mdash; safely, on time, and on budget.<br />
&nbsp;</p>
""",
    "Building Construction &amp; Engineering": """<p>Wumraq Limited undertakes building construction and engineering projects for residential, commercial, and institutional clients. Our building services cover:</p>

<p>New building construction from foundations to finishes.</p>

<p>Structural works, concreting, blockwork, and roofing delivered to plan.</p>

<p>Renovation, remodelling, and upgrading of existing structures.</p>

<p>Project management, site supervision, and strict safety standards.</p>

<p>With disciplined crews and hands-on supervision, we turn drawings into solid, lasting structures &mdash; delivered with the same discipline that defines our security operations.<br />
&nbsp;</p>
""",
    "Renovation &amp; Maintenance Works": """<p>Beyond new builds, Wumraq Limited keeps existing properties in excellent condition. Our renovation and maintenance services cover:</p>

<p>Renovation and remodelling of offices, homes, and commercial spaces.</p>

<p>Planned and preventive maintenance programmes for buildings and facilities.</p>

<p>Repairs to roofing, plumbing, electrical installations, and finishes.</p>

<p>Painting, tiling, and general beautification works.</p>

<p>One dependable partner for both security and engineering means faster response, simpler supervision, and works carried out by people you already trust.<br />
&nbsp;</p>
""",
    "Civil Engineering &amp; Earthworks": """<p>Wumraq Limited executes civil engineering and earthworks as the foundation of every successful project. Our civil works services cover:</p>

<p>Site clearance, demolition, and land preparation.</p>

<p>Excavation, earthmoving, filling, and compaction with modern plant.</p>

<p>Access roads, drainage, and paving for estates and industrial sites.</p>

<p>Concrete works, retaining structures, and general civil construction.</p>

<p>From clearing the first metre of ground to handing over a finished project, our crews work with precision, safety, and respect for schedule.<br />
&nbsp;</p>
""",
}

# old service img filename -> new
IMG_MAP = {
    "corporate_manned_guarding2069672904.jpg": "civil_engineering_earthworks.jpg",
    "_industrial_manned_guarding1942854346.png": "24_hour_security_guards.jpg",
    "mobile_patrol_services1940947803.png": "renovation_maintenance_works.jpg",
    "event_security_management927651658.png": "building_construction_engineering.jpg",
    "vip_escort_&amp;_personal_protection587143962.jpg": "road_construction_engineering.jpg",
    "vip_escort_&_personal_protection587143962.jpg": "road_construction_engineering.jpg",
    "cctv_installation_&amp;_monitoring1586465675.jpg": "warehouse_security_services.jpg",
    "cctv_installation_&_monitoring1586465675.jpg": "warehouse_security_services.jpg",
    "alarm_response_&amp;_rapid_intervention22333877.jpg": "residential_security_services.jpg",
    "alarm_response_&_rapid_intervention22333877.jpg": "residential_security_services.jpg",
    "vehicle_tracking_solutions267077206.jpg": "office_security_services.jpg",
    "biometric_access_control_systems1031152757.png": "guard_dog_services.jpg",
    "tracy_naa_adoley_acquaye_.jpg": "kwabena_osei_bonsu.jpg",
    "East_Midas_Properties.jpg": "Goldleaf_Properties_Ltd.jpg",
    "Cleanlife__Company_Ltd.jpg": "Adom_Facilities_Services.jpg",
    "Premium_Purpose_Ltd.jpg": "Brightstar_Finance_Ltd.jpg",
    "Orchard_Asset_Financing.jpg": "Primegate_Logistics_Ltd.jpg",
    "safenet_security_services_ghana_1369868501.jpg": "wumraq_security_services_ghana.jpg",
    "wumraq_security_services_ghana_1369868501.jpg": "wumraq_security_services_ghana.jpg",  # post-brand-rename variant
}

# AI source images -> destination (old path kept where references unchanged)
AI_TARGETS = {
    "slider1.png": ("img/sliders/ddss474653686.jpg", (600, 600)),
    "slider3.png": ("img/sliders/aaaassa406111407.jpg", (600, 600)),
    "slider2.png": ("img/sliders/sas1278615737.jpg", (600, 600)),
    "service_24h.png": ("img/services/24_hour_security_guards.jpg", (600, 600)),
    "service_dog.png": ("img/services/guard_dog_services.jpg", (600, 600)),
    "service_office.png": ("img/services/office_security_services.jpg", (600, 600)),
    "service_residential.png": ("img/services/residential_security_services.jpg", (600, 600)),
    "service_warehouse.png": ("img/services/warehouse_security_services.jpg", (600, 600)),
    "service_road.png": ("img/services/road_construction_engineering.jpg", (600, 600)),
    "service_building.png": ("img/services/building_construction_engineering.jpg", (600, 600)),
    "service_renovation.png": ("img/services/renovation_maintenance_works.jpg", (600, 600)),
    "service_civil.png": ("img/services/civil_engineering_earthworks.jpg", (600, 600)),
    "whatwe.png": ("img/contents/what-we-image.jpg", (500, 600)),
    "about.png": ("img/contents/wumraq_security_services_ghana.jpg", (600, 600)),
    "crumb.png": ("img/images/crumb.jpg", (2560, 661)),
    "news.png": ("img/news/rebranding_private_security_companies_.jpeg", (474, 315)),
    "staff.png": ("img/staff/kwabena_osei_bonsu.jpg", (400, 400)),
}

COLORS = {
    "#df3e35": "#0e8a3e",
    "#05224c": "#052e18",
    "#13325e": "#134a2a",
    "#fee6e6": "#dff2e4",
    "#fadfdf": "#d7efdd",
    "#f4eadd": "#e2f1e6",
    "#ceb486": "#9fd6a9",
    "#e3eaed": "#e4f0e7",
    "#0c346d": "#0d5c2c",
    "rgba(223, 62, 53, 1)": "rgba(14, 138, 62, 1)",
    "rgba(223, 62, 53,": "rgba(14, 138, 62,",
}

# flat page file -> destination path in tree
TREE = {
    "index.html": "index.html",
    "2_about-us.html": "2/about-us/index.html",
    "3_professional-security-services-in-ghana.html": "3/professional-security-services-in-ghana/index.html",
    "6_news.html": "6/news/index.html",
    "7_our-clients.html": "7/our-clients/index.html",
    "5_team.html": "5/team/index.html",
    "20_contacts.html": "20/contacts/index.html",
    "3_1_corporate-manned-guarding.html": "3/1/civil-engineering-earthworks/index.html",
    "3_2_mobile-patrol-services.html": "3/2/renovation-maintenance-works/index.html",
    "3_3_event-security-management.html": "3/3/building-construction-engineering/index.html",
    "3_4_executive-protection.html": "3/4/road-construction-engineering/index.html",
    "3_5_cctv-installation-and-monitoring.html": "3/5/warehouse-security-services/index.html",
    "3_6_alarm-response-and-rapid-intervention.html": "3/6/residential-security-services/index.html",
    "3_9_vehicle-tracking-solutions.html": "3/9/office-security-services/index.html",
    "3_10_biometric-access-control-systems.html": "3/10/guard-dog-services/index.html",
    "3_11_industrial-manned-guarding.html": "3/11/24-hour-security-guards/index.html",
    "3_6_delivering-trusted-security-and-surveillance.html": "3/6/delivering-trusted-security-and-surveillance/index.html",
    "5_1_5_tracy-naa-adoley-acquaye.html": "5/1/5/kwabena-osei-bonsu/index.html",
    "6_2_rebranding-private-security-companies.html": "6/2/rebranding-private-security-companies/index.html",
    "9_1_integrity.html": "9/1/integrity/index.html",
    "9_2_our-vision.html": "9/2/our-vision/index.html",
    "9_2_professionalism.html": "9/2/professionalism/index.html",
    "9_3_our-mission.html": "9/3/our-mission/index.html",
    "9_3_vigilance.html": "9/3/vigilance/index.html",
    "9_4_client-centered-service.html": "9/4/client-centered-service/index.html",
    "9_5_innovation.html": "9/5/innovation/index.html",
    "9_6_respect.html": "9/6/respect/index.html",
}

DEPTH_FIX = []  # obsolete: uniform +1 ../ applied to every sub-page below


def save_img(src, dest, size, quality=85):
    im = Image.open(src).convert("RGB")
    tw, th = size
    # cover-crop to target ratio then resize
    ratio = tw / th
    w, h = im.size
    if w / h > ratio:
        nw = int(h * ratio)
        im = im.crop(((w - nw) // 2, 0, (w + nw) // 2, h))
    else:
        nh = int(w / ratio)
        im = im.crop((0, (h - nh) // 2, w, (h + nh) // 2))
    im = im.resize((tw, th), Image.LANCZOS)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    im.save(dest, quality=quality)


def main():
    if os.path.exists(DEST):
        shutil.rmtree(DEST)
    # 1. copy full asset tree
    shutil.copytree(ORIG, DEST, ignore=shutil.ignore_patterns("pages", "assets_list.txt", "index_raw.html", "index_utf8.html"))
    os.remove(os.path.join(DEST, "index.html")) if os.path.exists(os.path.join(DEST, "index.html")) else None

    # 2. brand assets
    shutil.copy(os.path.join(BRAND, "logo.png"), os.path.join(DEST, "img/images/logo.png"))
    for f in glob.glob(os.path.join(BRAND, "*")):
        b = os.path.basename(f)
        if b.startswith("apple-touch") or b == "favicon.png":
            shutil.copy(f, os.path.join(DEST, "img/favicon", b))

    # 3. AI images (cover-crop to original dimensions)
    for src, (rel, size) in AI_TARGETS.items():
        save_img(os.path.join(AI, src), os.path.join(DEST, rel), size)

    # 4. client logos
    for i, name in enumerate(["Goldleaf_Properties_Ltd", "Adom_Facilities_Services",
                              "Primegate_Logistics_Ltd", "Brightstar_Finance_Ltd"], 1):
        shutil.copy(os.path.join(BRAND, f"client{i}.jpg"),
                    os.path.join(DEST, "img/clients", name + ".jpg"))

    # 5. remove old images that were replaced (no SafeNet-era leftovers)
    for old in IMG_MAP:
        p = os.path.join(DEST, "img", old.replace("&amp;", "&"))
        if os.path.exists(p):
            os.remove(p)

    # 5b. recolor the curved.png decoration (red -> brand green)
    import numpy as np
    cp = os.path.join(DEST, "img/images/curved.png")
    a = np.array(Image.open(cp).convert("RGBA")).astype(int)
    green = (14, 138, 62)
    red = (a[:, :, 3] > 100) & (a[:, :, 0] > 90) & (a[:, :, 0] > a[:, :, 1] * 1.25) & (a[:, :, 0] > a[:, :, 2] * 1.25)
    a[red, 0], a[red, 1], a[red, 2] = green
    Image.fromarray(a.astype("uint8")).save(cp)

    print("Assets done. Building pages...")
    build_pages()
    print("Pages done.")


def global_replacements(html):
    # ---- SafeNet third-party integrations removal (their chat/ads/whatsapp)
    html = re.sub(r'<script[^>]*src="[^"]*code\.tidio\.co[^"]*"\s*>\s*</script>\s*', "", html)
    html = re.sub(r'<!--\s*<script[^>]*code\.tidio\.co[^>]*></script>\s*-->\s*', "", html)
    html = re.sub(r'<script>\s*window\.dataLayer[^<]*?AW-[^<]*?</script>\s*', "", html, flags=re.S)
    html = re.sub(r'<script async src="https://www\.googletagmanager\.com/gtag/js[^"]*"></script>\s*', "", html)
    html = re.sub(r'<!-- Elfsight WhatsApp Chat[^>]*-->\s*', "", html)
    html = re.sub(r'<script[^>]*src="https://elfsightcdn\.com/platform\.js"[^>]*>\s*</script>\s*', "", html)
    html = re.sub(r'<div class="elfsight-app-[^"]*"[^>]*></div>\s*', "", html)

    # ---- meta / titles (specific first)
    html = html.replace(
        "Safenet Security Service - SafeNet Security Ghana | #1 Security Company in Accra | Manned Guards, CCTV & Patrol Services, Event Security.",
        "Wumraq Security Services Ltd - Wumraq Security Ghana | #1 Security Company in Accra | Security Guards, Guard Dogs & Office, Residential & Warehouse Security, Road & Building Engineering.")
    html = html.replace("https://https://www.safenetsecuritygh.com/", "https://www.wumraqlimited.com/")
    html = html.replace(
        "SafeNet Security Services - Leading security company in Ghana. Professional manned guards, CCTV monitoring, access control, mobile patrols. Serving Accra, Tema, Kumasi. Licensed & trusted by top banks, mines, hotels. 24/7 protection. Call 055-287-3077",
        "Wumraq Security Services Ltd - Trusted security and engineering company in Ghana. 24-hour security guards, guard dog services, office, residential and warehouse security, plus road and building construction. Serving Accra and across Ghana. Licensed & trusted. 24/7 protection. Call 0246029009")
    m = re.search(r'<meta name="keywords" content="[^"]*"', html)
    if m:
        html = html.replace(m.group(0),
            '<meta name="keywords" content="wumraq, wumraq limited, security, services,security company ghana,security services ghana,security guards accra,security company Accra,guard dog services Ghana,24 hour security guards Ghana,office security Ghana,residential security Ghana,warehouse security Ghana,road construction company Ghana,building construction Ghana, Integrity, Professionalism, Vigilance, Client-Centered, Innovation, Respect, monitoring, evaluation"')

    # ---- contacts
    html = html.replace("contact@safenetsecuritygh.com", "info@wumraqlimited.com")
    html = html.replace("safenetsecuritygh.com", "wumraqlimited.com")
    html = html.replace("0257942851", "0246029009")
    html = html.replace("054 785 8573", "0264019009")
    html = html.replace("055-287-3077", "0246029009")

    # ---- addresses (footer multi-line, contacts line, map infowindow)
    html = re.sub(r"Adjetey Adjei Sueley Street\s*<br>\s*Trasacco Valley\s*<br>.{0,3}Accra",
                  "Head Office, Accra<br>Greater Accra Region<br>Ghana", html)
    html = re.sub(r"Adjetey Adjei Sueley Street,?\s*Trasacco Valley,?.{0,3}Accra",
                  "Accra, Greater Accra Region, Ghana", html)

    # ---- brand names (longest first)
    for old, new in [
        ("SafeNet Security Services Ltd", "Wumraq Security Services Ltd"),
        ("SafeNet Security Services", "Wumraq Security Services"),
        ("SafeNet Security", "Wumraq Security"),
        ("SafeNet", "Wumraq"),
        ("Safenet Security Service", "Wumraq Security Services Ltd"),
        ("Safenet Security", "Wumraq Security"),
        ("Safenet", "Wumraq"),
        ("safenet", "wumraq"),
    ]:
        html = html.replace(old, new)

    html = html.replace("based in Adjirigano, Accra, Ghana", "based in Accra, Ghana")

    # ---- service names (display text incl. form values) — plain &amp; variants
    for old_slug, new_slug, old_name, new_name in SERVICES:
        html = html.replace(old_name, new_name)
        # unescaped variant (alt attributes etc.)
        plain_old = old_name.replace("&amp;", "&")
        plain_new = new_name.replace("&amp;", "&")
        if plain_old != old_name:
            html = html.replace(plain_old, plain_new)

    # ---- service slugs in links + page titles (dashed)
    for old_slug, new_slug, old_name, new_name in SERVICES:
        html = html.replace(old_slug, new_slug)
    html = html.replace("tracy-naa-adoley-acquaye", "kwabena-osei-bonsu")

    # ---- page <title> suffixes (space versions)
    title_map = {
        "- corporate manned guarding": "- civil engineering and earthworks",
        "- industrial manned guarding": "- 24 hour security guards",
        "- mobile patrol services": "- renovation and maintenance works",
        "- event security management": "- building construction and engineering",
        "- executive protection": "- road construction and engineering",
        "- cctv installation and monitoring": "- warehouse security services",
        "- alarm response and rapid intervention": "- residential security services",
        "- vehicle tracking solutions": "- office security services",
        "- biometric access control systems": "- guard dog services",
        "- tracy naa adoley acquaye": "- kwabena osei-bonsu",
    }
    for o, n in title_map.items():
        html = html.replace(o, n)

    # ---- staff name
    html = html.replace("Tracy Naa Adoley Acquaye", "Kwabena Osei-Bonsu")

    # ---- image filenames
    for old, new in IMG_MAP.items():
        html = html.replace(old, new)

    # ---- footer / home label
    html = html.replace("Professional Security Services in Ghana",
                        "Professional Security &amp; Engineering Services in Ghana")

    # ---- colours (CSS accent + inline styles)
    for old, new in COLORS.items():
        html = html.replace(old, new).replace(old.upper(), new)

    return html


def page_replacements(html, flat_name):
    # ----- home page specifics
    if flat_name == "index.html":
        html = html.replace(
            "To become the most trusted and technologically advanced private security provider in Ghana and West Africa, known for...",
            "To become the most trusted private security and engineering company in Ghana and West Africa, known for...")
        html = html.replace(
            "To deliver high-quality, customized security solutions that protect lives, assets, and reputations through disciplined...",
            "To deliver high-quality, customized security and engineering solutions that protect lives, assets, and reputations through disciplined...")
        html = re.sub(
            r"At our core, we are dedicated to delivering trusted security and surveillance solutions.*?ensures high-definition\.\.\.",
            "At our core, we are dedicated to delivering trusted security solutions that provide peace of mind for homes and businesses alike. Our expertise spans 24-hour guarding, guard dog services, and the protection of offices, residences, and warehouses.\n\n"
            "We understand that every property is unique, which is why we offer tailored solutions designed to meet your specific needs. Our disciplined officers and proven methods ensure reliable...",
            html, flags=re.S)

    # ----- about page specifics
    if flat_name == "2_about-us.html":
        html = html.replace(
            "From deploying trained guards and mobile patrols to managing high-profile events, monitoring surveillance systems, and responding to emergencies, we deliver peace of mind backed by integrity, vigilance, and client&nbsp;satisfaction.",
            "From deploying trained guards and guard dog teams to securing offices, residences, and warehouses &mdash; and delivering road and building engineering works through Wumraq Limited &mdash; we deliver peace of mind backed by integrity, vigilance, and client&nbsp;satisfaction.")
        html = html.replace(
            "To become the most trusted and technologically advanced private security provider in Ghana and West Africa, known for integrity, rapid response, and exceptional client service.",
            "To become the most trusted private security and engineering company in Ghana and West Africa, known for integrity, rapid response, and exceptional client service.")
        html = html.replace(
            "To deliver high-quality, customized security solutions that protect lives, assets, and reputations through disciplined personnel, advanced technology, and unmatched client service.",
            "To deliver high-quality, customized security and engineering solutions that protect lives, assets, and reputations through disciplined personnel, advanced technology, and unmatched client service.")

    # ----- service detail pages: full body content
    for old_slug, new_slug, old_name, new_name in SERVICES:
        # h3 may contain &amp; (inserted with new name) or &
        name_pat = re.escape(new_name).replace("&amp;", "&(?:amp;)?")
        pat = re.compile(
            r'(<h3 class="text-uppercase">\s*' + name_pat +
            r'\s*</h3>\s*<div class="seperator mb-3"></div>\s*<div class="details mb-4">).*?(</div>)',
            re.S)
        new_content = FULL_DESCS[new_name]
        html, n = pat.subn(lambda m: m.group(1) + "\n" + new_content + "\n" + m.group(2), html, count=1)
        if n:
            break  # only one h3 per page

    # ----- team member bio
    if flat_name == "5_1_5_tracy-naa-adoley-acquaye.html":
        bio = ("<p>Kwabena Osei-Bonsu is the Managing Director of Wumraq Security Services Ltd. "
               "He leads core operations in finance, client relations, marketing, and human capital, and oversees "
               "the company&rsquo;s road and building engineering division. His leadership strengthens performance "
               "and delivers consistent results for corporate and institutional clients.</p>\n\n"
               "<p><br />\n"
               "He brings extensive leadership experience shaped by strong results in revenue growth, client "
               "retention, and operational improvement. Under his direction, Wumraq has grown into a combined "
               "security and engineering group, serving corporate clients, residential communities, and public and "
               "private construction projects across Ghana.</p>\n\n"
               "<p><br />\n"
               "His leadership approach is strategic, disciplined, and focused on measurable improvement across "
               "teams&nbsp;and&nbsp;operations.</p>\n")
        html, n = re.subn(
            r'(Managing Director</h6>\s*<div class="seperator2 mb-4 mt-2"></div>\s*<div class="details">).*?(</div>)',
            lambda m: m.group(1) + "\n" + bio + m.group(2), html, count=1, flags=re.S)

    # ----- card descriptions (all pages, keyed by new name)
    for new_name, desc in CARD_DESCS.items():
        pat = re.compile(
            r'(<h4 class="text-capitalize">\s*' + re.escape(new_name) +
            r'\s*</h4>\s*</a>\s*<div class="details mb-2">).*?(</div>)', re.S)
        html = pat.sub(lambda m: m.group(1) + desc + m.group(2), html)

    return html


def build_pages():
    for flat, dest_rel in TREE.items():
        src = os.path.join(ORIG if flat == "index.html" else PAGES, flat)
        html = open(src, encoding="utf-8", errors="replace").read()
        if flat != "index.html":
            # static tree serves /a/b/index.html at /a/b/ -> every local ref needs one more ../
            html = html.replace('href="../', 'href="../../')
            html = html.replace('src="../', 'src="../../')
        html = global_replacements(html)
        html = page_replacements(html, flat)
        dest = os.path.join(DEST, dest_rel)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        open(dest, "w", encoding="utf-8").write(html)

    # CSS colour updates
    for css in ["css/style.css", "css/menu.css"]:
        p = os.path.join(DEST, css)
        txt = open(p, encoding="utf-8", errors="replace").read()
        for old, new in COLORS.items():
            txt = txt.replace(old, new).replace(old.upper(), new)
        open(p, "w", encoding="utf-8").write(txt)


if __name__ == "__main__":
    main()
