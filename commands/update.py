from db import get_connection
from utils.colors import Color
from utils.validation import validate_amount, validate_date, validate_category
from utils.logger import logger
from utils.security import require_pin



def register_update_command(subparsers):
    parser = subparsers.add_parser(
        "update",
        help="Update transaksi berdasarkan ID"
    )

    parser.add_argument("id", type=str, help="ID transaksi yang ingin diupdate")

    # Opsional: user boleh update satu atau banyak field
    parser.add_argument("--amount", type=str, help="Nominal baru")
    parser.add_argument("--category", type=str, help="Kategori baru")
    parser.add_argument("--date", type=str, help="Tanggal baru (YYYY-MM-DD)")
    parser.add_argument("--description", type=str, help="Catatan baru")

    parser.set_defaults(func=run_update)


def run_update(args):
    require_pin()   # PIN sebelum update
    
    # Validasi ID harus angka
    if not args.id.isdigit():
        print(Color.ERROR + "❌ ID harus berupa angka!" + Color.RESET)
        return

    trans_id = int(args.id)

    # Pastikan ada minimal 1 field yang diupdate
    if not (args.amount or args.category or args.date or args.description):
        print(Color.ERROR + "❌ Tidak ada data yang diupdate. Berikan minimal satu parameter." + Color.RESET)
        return

    conn = get_connection()
    cur = conn.cursor()

    # cek apakah ID ada
    cur.execute("SELECT * FROM transactions WHERE id = ?", (trans_id,))
    existing = cur.fetchone()

    if not existing:
        print(Color.ERROR + f"❌ ID {trans_id} tidak ditemukan." + Color.RESET)
        conn.close()
        return

    # Data existing — jika field tidak diupdate, gunakan value lama
    amount = existing["amount"]
    category = existing["category"]
    date = existing["date"]
    description = existing["description"]

    # Update field jika diberikan user
    if args.amount:
        amount = validate_amount(args.amount)

    if args.category:
        category = validate_category(args.category)

    if args.date:
        date = validate_date(args.date)

    if args.description is not None:
        description = args.description

    # Simpan perubahan
    cur.execute("""
        UPDATE transactions
        SET amount = ?, category = ?, date = ?, description = ?
        WHERE id = ?
    """, (amount, category, date, description, trans_id))

    conn.commit()
    conn.close()

    print(Color.OK + f"✔ Transaksi dengan ID {trans_id} berhasil diperbarui." + Color.RESET)

    logger.info(f"Updated transaction ID={trans_id} amount={amount}, category={category}, date={date}")
