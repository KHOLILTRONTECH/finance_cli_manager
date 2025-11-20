from db import get_db
from tabulate import tabulate
from utils.colors import Color
from utils.logger import logger
from utils.validation import validate_date



def register_filter_command(subparsers):
    parser = subparsers.add_parser(
        "filter",
        help="Filter transaksi berdasarkan tanggal"
    )

    parser.add_argument("--tanggal", help="Tanggal tertentu (YYYY-MM-DD)")
    parser.add_argument("--mulai", help="Tanggal mulai rentang (YYYY-MM-DD)")
    parser.add_argument("--akhir", help="Tanggal akhir rentang (YYYY-MM-DD)")

    parser.set_defaults(func=filter_transactions)


def filter_transactions(args):
    conn = get_db()
    c = conn.cursor()

    # Tentukan query berdasarkan input user
    if args.tanggal:
        validate_date(args.tanggal)
        query = "SELECT * FROM transactions WHERE date = ? ORDER BY date DESC"
        params = (args.tanggal,)

    elif args.mulai and args.akhir:
        validate_date(args.mulai)
        validate_date(args.akhir)
        query = "SELECT * FROM transactions WHERE date BETWEEN ? AND ? ORDER BY date DESC"
        params = (args.mulai, args.akhir)

    elif args.mulai:
        validate_date(args.mulai)
        query = "SELECT * FROM transactions WHERE date >= ? ORDER BY date DESC"
        params = (args.mulai,)

    elif args.akhir:
        validate_date(args.akhir)
        query = "SELECT * FROM transactions WHERE date <= ? ORDER BY date DESC"
        params = (args.akhir,)

    else:
        print(Color.ERROR + "❌ Kamu harus memberikan minimal satu parameter tanggal." + Color.RESET)
        print(Color.INFO + "Contoh:")
        print(Color.INFO + "  python main.py filter --tanggal 2025-01-01")
        print(Color.INFO + "  python main.py filter --mulai 2025-01-01 --akhir 2025-01-31")
        return

    # Eksekusi query
    c.execute(query, params)
    rows = c.fetchall()
    conn.close()

    # Jika tidak ada hasil
    if not rows:
        print(Color.WARNING + "Tidak ada transaksi yang cocok dengan filter." + Color.RESET)
        return

    # Susun tabel
    table_data = []
    for r in rows:
        table_data.append([
            r["id"],
            f"Rp {int(r['amount']):,}",
            r["category"],
            r["date"],
            r["description"] or "-"
        ])

    # Tampilkan tabel berwarna seperti versi kamu sebelumnya
    print(Color.HEADER + "=== HASIL FILTER ===")
    print(Color.HEADER + tabulate(
        table_data,
        headers=["ID", "Jumlah", "Kategori", "Tanggal", "Catatan"],
        tablefmt="fancy_grid"
    ) + Color.RESET)

    logger.info(f"Filter: params={args}")
    

