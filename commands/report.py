import os
from datetime import datetime
from db import get_db
from utils.colors import Color
from utils.logger import logger
from utils.security import require_pin

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm


def register_report_command(subparsers):
    parser = subparsers.add_parser(
        "laporan",
        help="Generate laporan keuangan dalam bentuk PDF"
    )
    parser.set_defaults(func=run_report)


def run_report(args):
    # keamanan (export itu termasuk sensitif)
    require_pin()

    conn = get_db()
    c = conn.cursor()

    # Ambil semua transaksi
    c.execute("SELECT * FROM transactions ORDER BY date ASC")
    rows = c.fetchall()

    # Ambil summary total
    c.execute("SELECT SUM(amount) AS total FROM transactions")
    total_all = c.fetchone()["total"] or 0

    # Ambil summary per kategori
    c.execute("""
        SELECT category, SUM(amount) AS total
        FROM transactions
        GROUP BY category
        ORDER BY total DESC
    """)
    per_kategori = c.fetchall()

    conn.close()

    # Buat folder reports
    os.makedirs("reports", exist_ok=True)

    # Nama file PDF
    filename = f"reports/laporan_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.pdf"

    # Buat PDF
    pdf = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    y = height - 2*cm

    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawString(2*cm, y, "LAPORAN KEUANGAN")
    y -= 1.5*cm

    # Total umum
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(2*cm, y, f"Total Semua Transaksi: Rp {int(total_all):,}")
    y -= 1*cm

    # Ringkasan per kategori
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(2*cm, y, "Ringkasan Per Kategori:")
    y -= 1*cm

    pdf.setFont("Helvetica", 11)
    for r in per_kategori:
        pdf.drawString(2.5*cm, y, f"{r['category']:15}  Rp {int(r['total']):,}")
        y -= 0.6*cm
        if y < 2*cm:
            pdf.showPage()
            y = height - 2*cm

    y -= 1*cm
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(2*cm, y, "Daftar Transaksi:")
    y -= 1*cm

    # Tabel transaksi
    pdf.setFont("Helvetica", 10)
    for row in rows:
        line = f"{row['date']:12} | {row['category']:10} | Rp {int(row['amount']):,} | {row['description'] or '-'}"
        pdf.drawString(2*cm, y, line)
        y -= 0.5*cm

        if y < 2*cm:
            pdf.showPage()
            y = height - 2*cm

    pdf.save()

    print(Color.OK + f"✔ Laporan PDF berhasil dibuat: {filename}" + Color.RESET)
    logger.info(f"Generated PDF report: {filename}")
