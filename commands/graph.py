import os
import matplotlib.pyplot as plt
from db import get_db
from utils.colors import Color
from utils.logger import logger


def register_graph_command(subparsers):
    parser = subparsers.add_parser(
        "graph",
        help="Generate grafik pengeluaran ke file PNG"
    )

    parser.set_defaults(func=run_graph)


def run_graph(args):
    conn = get_db()
    c = conn.cursor()

    # Grafik per kategori
    c.execute("""
        SELECT category, SUM(amount) AS total
        FROM transactions
        GROUP BY category
        ORDER BY total DESC
    """)
    kategori_rows = c.fetchall()

    # Grafik per tanggal
    c.execute("""
        SELECT date, SUM(amount) AS total
        FROM transactions
        GROUP BY date
        ORDER BY date
    """)
    tanggal_rows = c.fetchall()

    conn.close()

    if not kategori_rows:
        print(Color.WARNING + "Tidak ada transaksi. Grafik tidak dapat dibuat." + Color.RESET)
        return

    # Siapkan folder graphs
    os.makedirs("graphs", exist_ok=True)

    # Mulai membuat grafik
    plt.figure(figsize=(10, 6))

    # Subplot 1 - grafik kategori
    plt.subplot(2, 1, 1)
    kategori = [row["category"] for row in kategori_rows]
    jumlah = [row["total"] for row in kategori_rows]
    plt.bar(kategori, jumlah)
    plt.title("Total Pengeluaran per Kategori")

    # Subplot 2 - grafik tanggal
    plt.subplot(2, 1, 2)
    tanggal = [row["date"] for row in tanggal_rows]
    total_per_tgl = [row["total"] for row in tanggal_rows]
    plt.plot(tanggal, total_per_tgl, marker="o")
    plt.title("Pengeluaran per Tanggal")
    plt.xticks(rotation=45)

    plt.tight_layout()
    save_path = "graphs/report.png"
    plt.savefig(save_path)

    print(Color.OK + f"✔ Grafik berhasil dibuat: {save_path}" + Color.RESET)
    logger.info("Generated graphic at graphs/report.png")
