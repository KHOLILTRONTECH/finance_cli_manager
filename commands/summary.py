from db import get_db
from tabulate import tabulate
from utils.colors import Color
from utils.logger import logger
from utils.validation import validate_date



def register_summary_command(subparsers):
    parser = subparsers.add_parser(
        "summary",
        help="Menampilkan ringkasan transaksi per kategori"
    )

    parser.add_argument("--tanggal", help="Tanggal tertentu (YYYY-MM-DD)")
    parser.add_argument("--mulai", help="Tanggal mulai rentang (YYYY-MM-DD)")
    parser.add_argument("--akhir", help="Tanggal akhir rentang (YYYY-MM-DD)")

    parser.set_defaults(func=run_summary)


def run_summary(args):
    conn = get_db()
    c = conn.cursor()

    # Determine query condition
    if args.tanggal:
        validate_date(args.tanggal)
        where = "WHERE date = ?"
        params = (args.tanggal,)

    elif args.mulai and args.akhir:
        validate_date(args.mulai)
        validate_date(args.akhir)
        where = "WHERE date BETWEEN ? AND ?"
        params = (args.mulai, args.akhir)

    elif args.mulai:
        validate_date(args.mulai)
        where = "WHERE date >= ?"
        params = (args.mulai,)

    elif args.akhir:
        validate_date(args.akhir)
        where = "WHERE date <= ?"
        params = (args.akhir,)
        
    else:
        where = ""
        params = ()

    # Total keseluruhan
    c.execute(f"SELECT SUM(amount) AS total FROM transactions {where}", params)
    total_row = c.fetchone()
    total_all = total_row["total"] or 0

    if total_all == 0:
        print(Color.WARNING + "Tidak ada transaksi pada periode yang dipilih.")
        return

    print(Color.HEADER + "=== RINGKASAN TRANSAKSI ===")
    print(Color.OK + f"Total Semua Transaksi: Rp {int(total_all):,}\n")

    # Ringkasan per kategori
    c.execute(f"""
        SELECT category, SUM(amount) AS total
        FROM transactions
        {where}
        GROUP BY category
        ORDER BY total DESC
    """, params)

    rows = c.fetchall()
    conn.close()

    table_data = []
    for r in rows:
        percent = (r["total"] / total_all) * 100
        table_data.append([
            r["category"],
            f"Rp {int(r['total']):,}",
            f"{percent:.2f}%"
        ])

    print(Color.HEADER + tabulate(
        table_data,
        headers=["Kategori", "Total", "Persentase"],
        tablefmt="fancy_grid"
    ) + Color.RESET)

    logger.info(f"Summary command executed with params={args}")

