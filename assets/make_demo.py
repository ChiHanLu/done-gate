"""Generate a terminal-style animated demo GIF for done-gate.

This is a *scripted recreation* of the done-gate flow (not a live screen capture),
suitable for the README. Re-run to regenerate: `python assets/make_demo.py`.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 880, 560
BG = (13, 17, 23)        # GitHub dark
BAR = (22, 27, 34)
FG = (201, 209, 217)
GRAY = (139, 148, 158)
DIM = (110, 118, 129)
GREEN = (63, 185, 80)
BLUE = (88, 166, 255)
PURPLE = (210, 168, 255)
ORANGE = (240, 136, 62)

FONT = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 19)
PADX, TOP = 26, 56
LH = 28  # line height

def render(lines):
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    # title bar
    d.rectangle([0, 0, W, 40], fill=BAR)
    for i, c in enumerate([(255, 95, 86), (255, 189, 46), (39, 201, 63)]):
        d.ellipse([18 + i * 22, 14, 30 + i * 22, 26], fill=c)
    d.text((W // 2 - 60, 12), "done-gate", font=FONT, fill=DIM)
    y = TOP
    for text, color in lines:
        d.text((PADX, y), text, font=FONT, fill=color)
        y += LH
    return img

# stable top block (the plain-language summary)
TOP_BLOCK = [
    ('$ claude  "Add a \'Remember me\' checkbox to the login page"', GREEN),
    ("", FG),
    ("✻ done-gate — acceptance gate", PURPLE),
    ("", FG),
    ("What was built", BLUE),
    ("  Remember me", FG),
    ("    • What it does:  stay logged in next time you open the app", GRAY),
    ("    • Where it is:   below the password field, login screen", GRAY),
    ('    • How to use:    tick "Remember me", then press Log in', GRAY),
    ("", FG),
]

VERIFY = ("Verify — check what's really done:", BLUE)

# each screen is a full snapshot; (lines, duration_ms)
screens = [
    ([TOP_BLOCK[0]], 700),
    (TOP_BLOCK[:3], 700),
    (TOP_BLOCK, 1700),
    (TOP_BLOCK + [VERIFY, ("  [ ] Remember me", GRAY), ("      (you leave it unchecked)", DIM)], 1600),
    (TOP_BLOCK + [VERIFY, ("  [ ] Remember me", GRAY), ("", FG),
                  ("  Why not?   ( ) bug    ( ) improve    ( ) custom", FG)], 1600),
    (TOP_BLOCK + [VERIFY, ("  [ ] Remember me", GRAY), ("", FG),
                  ('  Why not?   (•) bug  ←  "still asks me to log in again"', ORANGE)], 1900),
    (TOP_BLOCK + [VERIFY, ("  [ ] Remember me", GRAY), ("", FG), ("  … fixing …", DIM)], 1200),
    (TOP_BLOCK + [("Verify again:", BLUE), ("  [x] Remember me", GREEN),
                  ("      (you check it ✓)", DIM)], 1700),
    (TOP_BLOCK + [("✅ All verified — wrapping up.   → written to ACCEPTANCE.md", GREEN),
                  ("   done-gate never checks the box for you.", DIM)], 3000),
]

frames = [render(lines) for lines, _ in screens]
durations = [d for _, d in screens]
frames[0].save(
    "assets/demo.gif", save_all=True, append_images=frames[1:],
    duration=durations, loop=0, optimize=True, disposal=2,
)
print("wrote assets/demo.gif", W, "x", H, "frames:", len(frames))
