"""Guitar lessons flyer with tear-off tabs + QR code. Outputs guitar-lessons-flyer.pdf next to this script."""
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.graphics.barcode.qr import QrCodeWidget
from reportlab.graphics.shapes import Drawing
from reportlab.graphics import renderPDF

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "guitar-lessons-flyer.pdf")
QR_PNG = os.path.join(HERE, "qr-arlingtonguitar.png")
PHONE = "(703) 239-4344"
EMAIL = "arlingtonguitar@pm.me"
SITE = "arlingtonguitar.live"
URL = "https://arlingtonguitar.live"

W, H = letter  # 612 x 792
MARGIN = 0.6 * inch
TAB_H = 2.3 * inch
TAB_TOP = MARGIN + TAB_H
N_TABS = 9


def draw_qr(c, cx, top, size):
    """Draw a QR code for URL centered at cx, with its top at `top`. Returns bottom y."""
    qr = QrCodeWidget(URL, barWidth=1, barHeight=1)
    x0, y0, x1, y1 = qr.getBounds()
    qw, qh = x1 - x0, y1 - y0
    scale = size / max(qw, qh)
    d = Drawing(size, size, transform=(scale, 0, 0, scale, -x0 * scale, -y0 * scale))
    d.add(qr)
    renderPDF.draw(d, c, cx - size / 2, top - size)
    return top - size


c = canvas.Canvas(OUT, pagesize=letter)

# ---------- Header ----------
y = H - 1.1 * inch
c.setFont("Helvetica-Bold", 54)
c.drawCentredString(W / 2, y, "Guitar Lessons")
y -= 0.45 * inch
c.setFont("Helvetica", 20)
c.drawCentredString(W / 2, y, "In-Person Lessons for Beginners & Beyond")
y -= 0.35 * inch
c.setFont("Helvetica-Bold", 18)
c.drawCentredString(W / 2, y, SITE)

# divider
y -= 0.3 * inch
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
y -= 0.35 * inch
for title, sub in details:
    c.setFont("Helvetica-Bold", 17)
    c.drawString(MARGIN + 0.25 * inch, y, "\u2022  " + title)
    c.setFont("Helvetica", 14)
    c.drawString(MARGIN + 0.55 * inch, y - 0.32 * inch, sub)
    y -= 0.64 * inch

# ---------- QR + contact ----------
y -= 0.1 * inch
qr_bottom = draw_qr(c, W / 2, y, 1.05 * inch)
y = qr_bottom - 0.18 * inch
c.setFont("Helvetica", 12)
c.drawCentredString(W / 2, y, "Scan to visit " + SITE)
y -= 0.32 * inch
c.setFont("Helvetica", 15)
c.drawCentredString(W / 2, y, f"Call or text: {PHONE}   •   {EMAIL}")

# ---------- Tear-off tabs ----------
c.setDash(6, 4)
c.setLineWidth(1)
c.line(MARGIN, TAB_TOP, W - MARGIN, TAB_TOP)
c.setFont("Helvetica", 14)
c.drawString(MARGIN + 2, TAB_TOP + 6, "\u2702")
c.drawRightString(W - MARGIN - 2, TAB_TOP + 6, "\u2702")

usable = W - 2 * MARGIN
tab_w = usable / N_TABS
for i in range(N_TABS + 1):
    x = MARGIN + i * tab_w
    c.line(x, MARGIN, x, TAB_TOP)

c.setDash()
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
