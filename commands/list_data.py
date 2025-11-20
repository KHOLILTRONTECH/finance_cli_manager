from db import get_db
from tabulate import tabulate
from utils.colors import Color
from utils.logger import logger


def register_list_command(subparsers):
    parser = subparsers.add_parser(
        "list",
        help="Tampilkan semua transaksi"
    )
    parser.set_defaults(func=list_transactions)


def list_transactions(args):
    conn = get_db()
    c = conn.cursor()

    c.execute("SELECT id, amount, category, date, description FROM transactions ORDER BY id DESC")
    rows = c.fetchall()
    conn.close()

    if not rows:
        print(Color.WARNING + "Belum ada transaksi.")
        return

    table_data = []
    for row in rows:
        table_data.append([
            row["id"],
            f"Rp {int(row['amount']):,}",
            row["category"],
            row["date"],
            row["description"] or "-"
        ])

    print(Color.HEADER + "=== DAFTAR TRANSAKSI ===")
    print(Color.HEADER + tabulate(
        table_data,
        headers=["ID", "Jumlah", "Kategori", "Tanggal", "Catatan"],
        tablefmt="fancy_grid"
    ) + Color.RESET)

    logger.info("List command executed")

