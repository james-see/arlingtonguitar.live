"""Guitar lessons flyer with tear-off tabs. Outputs guitar-lessons-flyer.pdf next to this script."""
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "guitar-lessons-flyer.pdf")
PHONE = "(703) 239-4344"
EMAIL = "arlingtonguitar@pm.me"
SITE = "arlingtonguitar.live"

W, H = letter  # 612 x 792
MARGIN = 0.6 * inch
TAB_H = 2.5 * inch
TAB_TOP = MARGIN + TAB_H
N_TABS = 9

c = canvas.Canvas(OUT, pagesize=letter)

# ---------- Header ----------
y = H - 1.1 * inch
c.setFont("Helvetica-Bold", 54)
c.drawCentredString(W / 2, y, "Guitar Lessons")
y -= 0.55 * inch
c.setFont("Helvetica", 20)
c.drawCentredString(W / 2, y, "In-Person Lessons for Beginners & Beyond")
y -= 0.45 * inch
c.setFont("Helvetica-Bold", 18)
c.drawCentredString(W / 2, y, SITE)

# divider
y -= 0.35 * inch
c.setStrokeColorRGB(0.2, 0.2, 0.2)
c.setLineWidth(1.5)
c.line(MARGIN, y, W - MARGIN, y)

# ---------- Details ----------
details = [
    ("In-person lessons", "Learn face-to-face with hands-on guidance."),
    ("Guitar provided", "No guitar? No problem — we provide one during the lesson."),
    ("Flexible hours", "Available daily, including weekends — pick a time that works for you."),
    ("Starting at $25", "30-minute lessons starting at just $25."),
    ("Easy payment", "Pay per lesson with mobile pay options, or save with monthly discounts."),
]
y -= 0.45 * inch
for title, sub in details:
    c.setFont("Helvetica-Bold", 17)
    c.drawString(MARGIN + 0.25 * inch, y, "\u2022  " + title)
    c.setFont("Helvetica", 14)
    c.drawString(MARGIN + 0.55 * inch, y - 0.32 * inch, sub)
    y -= 0.72 * inch

# ---------- Contact block ----------
y -= 0.15 * inch
c.setFont("Helvetica", 16)
c.drawCentredString(W / 2, y, f"Call or text: {PHONE}")
y -= 0.4 * inch
c.drawCentredString(W / 2, y, f"Email: {EMAIL}")
y -= 0.4 * inch
c.setFont("Helvetica-Bold", 16)
c.drawCentredString(W / 2, y, f"Visit: https://{SITE}")

# ---------- Tear-off tabs ----------
c.setDash(6, 4)
c.setLineWidth(1)
c.line(MARGIN, TAB_TOP, W - MARGIN, TAB_TOP)
# scissors hint
c.setFont("Helvetica", 14)
c.drawString(MARGIN + 2, TAB_TOP + 6, "\u2702")
c.drawRightString(W - MARGIN - 2, TAB_TOP + 6, "\u2702")

usable = W - 2 * MARGIN
tab_w = usable / N_TABS
for i in range(N_TABS + 1):
    x = MARGIN + i * tab_w
    c.line(x, MARGIN, x, TAB_TOP)

c.setDash()  # solid again
for i in range(N_TABS):
    cx = MARGIN + (i + 0.5) * tab_w
    c.saveState()
    c.translate(cx, MARGIN + 0.15 * inch)
    c.rotate(90)
    c.setFont("Helvetica-Bold", 10.5)
    c.drawCentredString(TAB_H / 2 - 0.15 * inch, 8, PHONE)
    c.setFont("Helvetica", 9.5)
    c.drawCentredString(TAB_H / 2 - 0.15 * inch, -6, EMAIL)
    c.restoreState()

c.showPage()
c.save()
print("wrote", OUT)
