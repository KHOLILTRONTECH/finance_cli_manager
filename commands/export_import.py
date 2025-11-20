import csv
from db import get_db, get_connection
from utils.validation import validate_amount, validate_date, validate_category
from utils.colors import Color
from utils.logger import logger
from utils.security import require_pin



def register_export_import_commands(subparsers):
    # EXPORT
    export_cmd = subparsers.add_parser(
        "export",
        help="Ekspor transaksi ke file CSV"
    )
    export_cmd.add_argument("filename", type=str, help="Nama file CSV output")
    export_cmd.set_defaults(func=run_export)

    # IMPORT
    import_cmd = subparsers.add_parser(
        "import",
        help="Impor transaksi dari file CSV"
    )
    import_cmd.add_argument("filename", type=str, help="Nama file CSV input")
    import_cmd.set_defaults(func=run_import)


def run_export(args):
    require_pin()

    filename = args.filename

    conn = get_db()
    c = conn.cursor()
    c.execute("SELECT amount, category, date, description FROM transactions ORDER BY id")
    rows = c.fetchall()
    conn.close()

    if not rows:
        print(Color.WARNING + "Tidak ada transaksi yang bisa diekspor!" + Color.RESET)
        return

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["amount", "category", "date", "description"])

        for row in rows:
            writer.writerow([row["amount"], row["category"], row["date"], row["description"]])

    print(Color.OK + f"✔ Data berhasil diekspor ke {filename}" + Color.RESET)
    logger.info(f"Exported CSV: {filename}")


def run_import(args):
    require_pin()
    
    filename = args.filename

    try:
        with open(filename, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
    except FileNotFoundError:
        print(Color.ERROR + f"File '{filename}' tidak ditemukan!" + Color.RESET)
        return

    if not rows:
        print(Color.WARNING + "File CSV kosong, tidak ada yang diimpor." + Color.RESET)
        return

    conn = get_connection()
    cur = conn.cursor()

    inserted = 0

    for r in rows:
        try:
            amount = validate_amount(r["amount"])
            category = validate_category(r["category"])
            date = validate_date(r["date"])
            description = r.get("description", "")
        except SystemExit:
            print(Color.ERROR + f"Baris dilewati (invalid): {r}" + Color.RESET)
            continue

        # Pastikan kategori ada
        cur.execute("INSERT OR IGNORE INTO categories(name) VALUES (?)", (category,))

        # Simpan transaksi
        cur.execute("""
            INSERT INTO transactions (amount, category, date, description)
            VALUES (?, ?, ?, ?)
        """, (amount, category, date, description))

        inserted += 1

    conn.commit()
    conn.close()

    print(Color.OK + f"✔ Import selesai! {inserted} transaksi berhasil ditambahkan." + Color.RESET)
    logger.info(f"Imported CSV: {filename}, total={inserted}")
