from db import get_connection
from utils.colors import Color
from utils.logger import logger
from utils.security import require_pin



def register_delete_command(subparsers):
    parser = subparsers.add_parser(
        "delete",
        help="Hapus transaksi berdasarkan ID"
    )
    parser.add_argument(
        "id",
        type=str,
        help="ID transaksi yang ingin dihapus"
    )
    parser.set_defaults(func=run_delete)


def run_delete(args):
    require_pin()   # PIN sebelum hapus
    
    # Validasi ID harus angka
    if not args.id.isdigit():
        print(Color.ERROR + "❌ ID harus berupa angka!" + Color.RESET)
        return

    trans_id = int(args.id)

    conn = get_connection()
    cur = conn.cursor()

    # cek apakah ID ada
    cur.execute("SELECT * FROM transactions WHERE id = ?", (trans_id,))
    row = cur.fetchone()

    if not row:
        print(Color.ERROR + f"❌ ID {trans_id} tidak ditemukan." + Color.RESET)
        conn.close()
        return

    # delete
    cur.execute("DELETE FROM transactions WHERE id = ?", (trans_id,))
    conn.commit()
    conn.close()

    print(Color.OK + f"✔ Transaksi dengan ID {trans_id} berhasil dihapus." + Color.RESET)
    logger.info(f"Deleted transaction ID: {trans_id}")
