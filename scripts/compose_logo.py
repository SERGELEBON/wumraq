#!/usr/bin/env python3
"""Compose the WUMRAQ logo lockup, favicon and client wordmarks."""
from PIL import Image, ImageDraw, ImageFont, ImageOps
import os

SRC = "/home/z/my-project/scripts/gen-images"
OUT = "/home/z/my-project/scripts/brand-assets"
os.makedirs(OUT, exist_ok=True)

TEAL = (15, 123, 112, 255)          # #0F7B70 brand teal
TEAL_DARK = (10, 92, 84, 255)
GRAY_TEXT = (96, 122, 118, 255)     # muted teal-gray for client logos

F_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
F_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def recolor_teal(img: Image.Image) -> Image.Image:
    """Recolor a dark-on-white emblem to brand teal, preserving antialiasing."""
    img = img.convert("RGBA")
    alpha = ImageOps.invert(img.convert("L"))
    # boost alpha a bit for full opacity of dark strokes
    alpha = alpha.point(lambda a: min(255, int(a * 1.15)))
    out = Image.new("RGBA", img.size, (0, 0, 0, 0))
    solid = Image.new("RGBA", img.size, TEAL)
    out = Image.composite(solid, out, alpha)
    return out


# ---------- 1. Main logo (emblem + wordmark) ----------
emblem = Image.open(f"{SRC}/logo-emblem.png")
emblem = recolor_teal(emblem)

W, H = 1200, 760
logo = Image.new("RGBA", (W, H), (0, 0, 0, 0))

# emblem: 560px wide, centered, top area
em_w = 560
em = emblem.resize((em_w, int(emblem.height * em_w / emblem.width)), Image.LANCZOS)
logo.paste(em, ((W - em.width) // 2, 10), em)

d = ImageDraw.Draw(logo)

def text_w(draw, txt, font, spacing=0):
    w = 0
    for ch in txt:
        w += draw.textlength(ch, font=font) + spacing
    return w - spacing if txt else 0

def draw_tracked(draw, xy_center_x, y, txt, font, fill, spacing=0):
    total = text_w(draw, txt, font, spacing)
    x = xy_center_x - total / 2
    for ch in txt:
        draw.text((x, y), ch, font=font, fill=fill)
        x += draw.textlength(ch, font=font) + spacing
    return total

f1 = ImageFont.truetype(F_BOLD, 128)   # WUMRAQ
f2 = ImageFont.truetype(F_BOLD, 46)    # SECURITY SERVICES LIMITED

draw_tracked(d, W / 2, 585, "WUMRAQ", f1, TEAL_DARK, spacing=6)
draw_tracked(d, W / 2, 640 + 78, "SECURITY SERVICES LIMITED", f2, TEAL, spacing=4)

logo.save(f"{OUT}/logo.png")
print("logo.png", logo.size)

# ---------- 2. Square emblem-only (favicon / offcanvas) ----------
sq = Image.new("RGBA", (760, 760), (0, 0, 0, 0))
em2 = emblem.resize((700, int(emblem.height * 700 / emblem.width)), Image.LANCZOS)
sq.paste(em2, ((760 - em2.width) // 2, (760 - em2.height) // 2), em2)
sq.save(f"{OUT}/emblem-square.png")
for size, name in [(64, "favicon.png"), (144, "apple-144.png"), (57, "apple-57.png"),
                   (72, "apple-72.png"), (114, "apple-114.png")]:
    sq.resize((size, size), Image.LANCZOS).save(f"{OUT}/{name}")
print("favicons done")

# ---------- 3. Client sector wordmarks (placeholder logos) ----------
def client_logo(fname, line1, line2):
    c = Image.new("RGBA", (560, 340), (255, 255, 255, 0))
    d = ImageDraw.Draw(c)
    # simple shield-building icon
    cx = 280
    # shield outline
    d.polygon([(cx, 40), (cx + 90, 75), (cx + 90, 150), (cx, 205), (cx - 90, 150), (cx - 90, 75)],
              outline=GRAY_TEXT, width=8)
    # building bars inside shield
    d.rectangle([cx - 45, 120, cx - 25, 165], fill=GRAY_TEXT)
    d.rectangle([cx - 10, 95, cx + 10, 165], fill=GRAY_TEXT)
    d.rectangle([cx + 25, 130, cx + 45, 165], fill=GRAY_TEXT)
    fa = ImageFont.truetype(F_BOLD, 40)
    fb = ImageFont.truetype(F_REG, 26)
    draw_tracked(d, cx, 245, line1, fa, GRAY_TEXT, spacing=2)
    draw_tracked(d, cx, 295, line2, fb, GRAY_TEXT, spacing=2)
    c.save(f"{OUT}/{fname}")
    print(fname)

client_logo("residential-estates.png", "RESIDENTIAL", "ESTATES  PARTNER")
client_logo("logistics-warehousing.png", "LOGISTICS &", "WAREHOUSING  PARTNER")
client_logo("corporate-offices.png", "CORPORATE", "OFFICES  PARTNER")
client_logo("retail-commerce.png", "RETAIL &", "COMMERCE  PARTNER")

print("ALL BRAND ASSETS DONE")
