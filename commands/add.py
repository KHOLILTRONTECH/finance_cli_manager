import argparse
from db import get_connection
from utils.validation import validate_amount, validate_date
from utils.category_utils import ensure_category_exists
from utils.colors import Color
from utils.logger import logger
from utils.validation import validate_category
from utils.ai_category import predict_category


def register_add(subparsers):
    parser = subparsers.add_parser(
        "add",
        help="Menambahkan transaksi baru (pemasukan/pengeluaran)"
    )
    parser.add_argument("amount", type=float, help="Nominal uang")
    parser.add_argument("category", type=str, help="Kategori transaksi")
    parser.add_argument("date", type=str, help="Tanggal (format YYYY-MM-DD)")
    parser.add_argument(
        "-d", "--description",
        type=str,
        default="",
        help="Deskripsi tambahan"
    )

    parser.set_defaults(func=run_add)


def run_add(args):
    amount = validate_amount(args.amount)
    date = validate_date(args.date)

    # Jika kategori = auto → prediksi otomatis
    if args.category.lower() in ["auto", "-", ""]:
        predicted = predict_category(args.description)
        category = predicted
        print(Color.WARNING + f"Kategori otomatis diprediksi: {predicted}" + Color.RESET)
    else:
        category = args.category

    # pastikan kategori ada di tabel categories
    ensure_category_exists(category)

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO transactions (amount, category, date, description)
        VALUES (?, ?, ?, ?)
    """, (amount, category, date, args.description))

    conn.commit()
    conn.close()

    print(Color.OK + "✔ Transaksi berhasil ditambahkan!" + Color.RESET)
    print(Color.INFO + f"Jumlah     : Rp {int(amount):,}")
    print(Color.INFO + f"Kategori   : {category}")
    print(Color.INFO + f"Tanggal    : {date}")
    print(Color.INFO + f"Catatan    : {args.description or '-'}" + Color.RESET)

    logger.info(f"Add: amount={amount} category={category} date={date}")
