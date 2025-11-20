# project/utils/dashboard.py
from db import get_db
from datetime import datetime, date, timedelta
from tabulate import tabulate
from utils.colors import Color


def _iso(d: date) -> str:
    return d.isoformat()


def display_dashboard():
    """
    Tampilkan ringkasan cepat saat program dijalankan.
    Menampilkan:
     - Total hari ini
     - Total minggu ini
     - Total bulan ini
     - Kategori terbesar hari ini (jika ada)
     - Transaksi terakhir
     - Top 5 kategori (table)
    """
    try:
        conn = get_db()
        c = conn.cursor()

        today_dt = date.today()
        today = _iso(today_dt)

        # minggu ini: mulai Senin
        start_week_dt = today_dt - timedelta(days=today_dt.weekday())
        end_week_dt = start_week_dt + timedelta(days=6)
        start_week = _iso(start_week_dt)
        end_week = _iso(end_week_dt)

        # bulan ini (YYYY-MM-01) and use LIKE for month
        month_start = _iso(today_dt.replace(day=1))
        month_like = today_dt.strftime("%Y-%m-")  # e.g. "2025-01-"

        # Totals
        c.execute("SELECT IFNULL(SUM(amount), 0) AS total FROM transactions WHERE date = ?", (today,))
        total_today = c.fetchone()["total"] or 0

        c.execute(
            "SELECT IFNULL(SUM(amount), 0) AS total FROM transactions WHERE date BETWEEN ? AND ?",
            (start_week, end_week)
        )
        total_week = c.fetchone()["total"] or 0

        c.execute("SELECT IFNULL(SUM(amount), 0) AS total FROM transactions WHERE date LIKE ?",
                  (f"{month_like}%",))
        total_month = c.fetchone()["total"] or 0

        # Kategori terbesar hari ini
        c.execute("""
            SELECT category, SUM(amount) AS total
            FROM transactions
            WHERE date = ?
            GROUP BY category
            ORDER BY total DESC
            LIMIT 1
        """, (today,))
        top_cat_row = c.fetchone()

        if top_cat_row:
            top_category = top_cat_row["category"]
            top_category_total = top_cat_row["total"]
        else:
            top_category = None
            top_category_total = 0

        # Transaksi terakhir
        c.execute("SELECT id, amount, category, date, description FROM transactions ORDER BY id DESC LIMIT 1")
        last = c.fetchone()

        # Top 5 kategori (bulan ini)
        c.execute("""
            SELECT category, SUM(amount) AS total
            FROM transactions
            WHERE date LIKE ?
            GROUP BY category
            ORDER BY total DESC
            LIMIT 5
        """, (f"{month_like}%",))
        top_categories = c.fetchall()

    except Exception as e:
        # jika DB belum siap atau error, jangan crash aplikasi
        print(Color.ERROR + "Gagal mengambil data dashboard: " + str(e) + Color.RESET)
        return
    finally:
        try:
            conn.close()
        except:
            pass

    # Tampilkan dashboard (ringkas)
    print(Color.HEADER + "=== DASHBOARD KEUANGAN — RINGKASAN CEPAT ===" + Color.RESET)
    print(Color.OK + f"Hari ini      : Rp {int(total_today):,}" + Color.RESET)
    print(Color.OK + f"Minggu ini    : Rp {int(total_week):,}" + Color.RESET)
    print(Color.OK + f"Bulan ini     : Rp {int(total_month):,}" + Color.RESET)

    if top_category:
        print(Color.INFO + f"Kategori terbesar hari ini: {top_category} • Rp {int(top_category_total):,}" + Color.RESET)
    else:
        print(Color.WARNING + "Kategori terbesar hari ini: - (tidak ada transaksi hari ini)" + Color.RESET)

    if last:
        print(Color.INFO + f"Transaksi terakhir: [{last['id']}] {last['category']} • Rp {int(last['amount']):,} • {last['date']} • {last['description'] or '-'}" + Color.RESET)
    else:
        print(Color.WARNING + "Transaksi terakhir: - (belum ada transaksi)" + Color.RESET)

    # Tampilkan top kategori table kalau ada
    if top_categories:
        table = []
        for r in top_categories:
            table.append([r["category"], f"Rp {int(r['total']):,}"])
        print()
        print(Color.HEADER + "Top kategori (bulan ini)" + Color.RESET)
        print(tabulate(table, headers=["Kategori", "Total"], tablefmt="fancy_grid"))
    print()  # newline
