from datetime import datetime
from utils.colors import Color


def validate_amount(amount):
    try:
        amount = float(amount)
    except ValueError:
        raise SystemExit(Color.ERROR + "Nominal harus berupa angka!" + Color.RESET)

    if amount <= 0:
        raise SystemExit(Color.ERROR + "Nominal harus lebih dari 0!" + Color.RESET)

    return amount


def validate_date(date_str):
    try:
        # format wajib
        datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise SystemExit(
            Color.ERROR +
            "Tanggal tidak valid! Gunakan format YYYY-MM-DD (contoh: 2025-01-05)" +
            Color.RESET
        )

    return date_str


def validate_category(category):
    if not category or category.strip() == "":
        raise SystemExit(Color.ERROR + "Kategori tidak boleh kosong!" + Color.RESET)

    if category.isdigit():
        raise SystemExit(Color.ERROR + "Kategori tidak boleh berupa angka saja!" + Color.RESET)

    return category.strip()
