#!/usr/bin/env python3
"""Generate WUMRAQ logo, favicons and placeholder client logos with PIL."""
from PIL import Image, ImageDraw, ImageFont
import os

BOLD = "/home/z/my-project/site/original/fonts/Poppins-Bold.ttf"
REG = "/home/z/my-project/site/original/fonts/Poppins-Regular.ttf"
OUT = "/home/z/my-project/site/brand"
os.makedirs(OUT, exist_ok=True)

GREEN = (18, 128, 108, 255)       # accent teal green
DEEP = (5, 48, 43, 255)           # deep teal
GOLD = (201, 162, 39, 255)        # accent gold
WHITE = (255, 255, 255, 255)
GREY = (110, 117, 122, 255)


def shield(draw, cx, cy, r, fill, outline=None, ow=0):
    """Draw a shield shape centered (cx,cy) with radius r."""
    # shield: top corners rounded, pointed bottom
    pts = []
    import math
    steps = 40
    for i in range(steps + 1):
        a = math.pi * (1 + i / steps)  # left half top circle from 180 to 360
        x = cx + r * math.cos(a)
        y = cy - r * 0.75 + r * 0.75 * math.sin(a) * 0.0
    # simpler: polygon
    pts = [
        (cx - r, cy - r * 0.75), (cx + r, cy - r * 0.75),
        (cx + r, cy + r * 0.25),
        (cx, cy + r),
        (cx - r, cy + r * 0.25),
    ]
    draw.polygon(pts, fill=fill, outline=outline, width=ow)


def make_logo(scale=4):
    W, H = 248 * scale, 151 * scale
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    # emblem: solid green shield + white checkmark
    cx, cy = 58 * scale, 70 * scale
    r = 46 * scale
    shield(d, cx, cy, r, GREEN)
    shield(d, cx, cy, int(r * 0.86), DEEP)
    d.line([(cx - 22 * scale, cy - 2 * scale), (cx - 4 * scale, cy + 22 * scale), (cx + 26 * scale, cy - 22 * scale)],
           fill=WHITE, width=int(8 * scale), joint="curve")
    # small gold star top-right of shield
    sx, sy, sr = cx + 38 * scale, cy - 38 * scale, 10 * scale
    import math
    star = []
    for i in range(10):
        ang = -math.pi / 2 + i * math.pi / 5
        rad = sr if i % 2 == 0 else sr * 0.45
        star.append((sx + rad * math.cos(ang), sy + rad * math.sin(ang)))
    d.polygon(star, fill=GOLD)
    # text (auto-fit)
    tx = 114 * scale
    max_w = W - tx - 4 * scale
    size = int(28 * scale)
    while True:
        f_main = ImageFont.truetype(BOLD, size)
        if d.textlength("WUMRAQ", font=f_main) <= max_w or size < 10:
            break
        size -= 1
    size2 = int(9.5 * scale)
    while True:
        f_sub = ImageFont.truetype(REG, size2)
        if d.textlength("SECURITY SERVICES LTD", font=f_sub) <= max_w or size2 < 6:
            break
        size2 -= 1
    d.text((tx, 54 * scale), "WUMRAQ", font=f_main, fill=DEEP)
    tw = d.textlength("WUMRAQ", font=f_main)
    d.rectangle([tx, 84 * scale, tx + tw, 87 * scale], fill=GOLD)
    d.text((tx + 1 * scale, 93 * scale), "SECURITY SERVICES LTD", font=f_sub, fill=GREEN)
    img = img.resize((248, 151), Image.LANCZOS)
    img.save(os.path.join(OUT, "logo.png"))


def make_favicons():
    from PIL import ImageFilter
    # big master shield 400x400
    S = 4
    img = Image.new("RGBA", (400, 400), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    cx, cy, r = 200, 210, 150
    shield(d, cx, cy, r, GREEN)
    d.line([(cx - 70, cy - 15), (cx - 15, cy + 60), (cx + 78, cy - 70)], fill=WHITE, width=34, joint="curve")
    img.save(os.path.join(OUT, "favicon_master.png"))
    sizes = {"favicon.png": (57, 57),
             "apple-touch-icon-57-precomposed.png": (66, 47),
             "apple-touch-icon-72-precomposed.png": (72, 59),
             "apple-touch-icon-114-precomposed.png": (114, 94),
             "apple-touch-icon-144-precomposed.png": (114, 94)}
    for name, (w, h) in sizes.items():
        im = img.copy()
        im.thumbnail((w, h), Image.LANCZOS)
        canvas = Image.new("RGBA", (w, h), (0, 0, 0, 0))
        canvas.paste(im, ((w - im.width) // 2, (h - im.height) // 2), im)
        canvas.save(os.path.join(OUT, name))


def client_logo(name, initials, color, tagline, fname):
    W, H = 200, 140
    img = Image.new("RGB", (W, H), (255, 255, 255))
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W - 1, H - 1], outline=(225, 228, 230), width=2)
    # circle emblem
    cx, cy, r = 46, 52, 28
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color)
    f_in = ImageFont.truetype(BOLD, 22)
    bbox = d.textbbox((0, 0), initials, font=f_in)
    d.text((cx - (bbox[2] - bbox[0]) / 2, cy - (bbox[3] - bbox[1]) / 2 - 2), initials, font=f_in, fill=(255, 255, 255))
    # name (wrap 2 lines)
    f_name = ImageFont.truetype(BOLD, 15)
    f_tag = ImageFont.truetype(REG, 10)
    words = name.split()
    lines, cur = [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if d.textlength(t, font=f_name) > 118:
            lines.append(cur); cur = w_
        else:
            cur = t
    lines.append(cur)
    y = 88
    for ln in lines:
        d.text((14, y), ln, font=f_name, fill=(40, 45, 50))
        y += 18
    d.text((14, y + 2), tagline, font=f_tag, fill=(130, 138, 144))
    img.save(os.path.join(OUT, fname))


make_logo()
make_favicons()
client_logo("Goldleaf Properties Ltd", "GP", (14, 122, 55), "REAL ESTATE", "client1.jpg")
client_logo("Adom Facilities Services", "AF", (13, 74, 42), "FACILITY MANAGEMENT", "client2.jpg")
client_logo("Primegate Logistics Ltd", "PL", (32, 58, 96), "LOGISTICS & HAULAGE", "client3.jpg")
client_logo("Brightstar Finance Ltd", "BF", (176, 122, 20), "MICROFINANCE", "client4.jpg")
print("Brand assets OK:", sorted(os.listdir(OUT)))
