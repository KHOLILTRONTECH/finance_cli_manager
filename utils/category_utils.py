from db import get_db

def ensure_category_exists(name: str):
    """Menambahkan kategori jika belum ada."""
    conn = get_db()
    c = conn.cursor()

    c.execute("SELECT id FROM categories WHERE name = ?", (name,))
    data = c.fetchone()

    if data:
        conn.close()
        return data["id"]  # kategori sudah ada

    # Jika belum ada → buat baru
    c.execute("INSERT INTO categories (name) VALUES (?)", (name,))
    conn.commit()
    new_id = c.lastrowid
    conn.close()

    return new_id
