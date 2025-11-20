💰 Aplikasi Pengelola Keuangan Harian (CLI + SQLite)

Aplikasi ini adalah program Command Line Interface (CLI) berbasis Python untuk mencatat dan mengelola transaksi keuangan harian.
Menggunakan SQLite sebagai database utama, dilengkapi fitur modern seperti dashboard ringkasan, AI kategori otomatis, grafik pengeluaran, PDF laporan, backup otomatis, dan PIN keamanan.

Aplikasi ini cocok untuk pembelajaran Python tingkat menengah–lanjut serta penggunaan pribadi.

🚀 Fitur Utama
✔ 1. Tambah Transaksi
python main.py add <jumlah> <kategori> <tanggal> -d "catatan"


Contoh:

python main.py add 15000 jajan 2025-01-02 -d "beli snack"

✔ 2. Dashboard + Daftar Transaksi

Menampilkan:

Total pengeluaran hari ini

Total minggu ini

Total bulan ini

Kategori terbesar hari ini

Transaksi terbaru

Top kategori bulan ini

Tabel transaksi berwarna

Perintah:

python main.py list


Contoh output:

=== DASHBOARD KEUANGAN — RINGKASAN CEPAT ===
Hari ini      : Rp 15,000
Minggu ini    : Rp 15,000
Bulan ini     : Rp 15,000
Kategori terbesar hari ini: lainnya • Rp 15,000
Transaksi terakhir: [11] lainnya • Rp 15,000 • 2025-11-18 • beli susu jahe

✔ 3. Filter Transaksi

Filter berdasarkan:

tanggal tertentu

tanggal mulai

tanggal akhir

rentang tanggal

Contoh:

python main.py filter --tanggal 2025-01-01
python main.py filter --mulai 2025-01-01 --akhir 2025-01-31

✔ 4. Ringkasan Per Kategori (Summary)

Menampilkan:

total semua transaksi

total per kategori

persentase kontribusi

mendukung filter tanggal

Perintah:

python main.py summary
python main.py summary --mulai 2025-01-01 --akhir 2025-01-31

✔ 5. Update Transaksi
python main.py update <id> --amount 20000 --category makanan --description "edit"

✔ 6. Hapus Transaksi
python main.py delete <id>

✔ 7. Import / Export CSV

Import:

python main.py import data.csv


Export:

python main.py export output.csv

✔ 8. Grafik Pengeluaran (matplotlib)
python main.py graph


Output tersimpan di:
📁 graphs/expense_graph.png

✔ 9. AI Kategori Otomatis

Jika kategori dikosongkan, aplikasi akan menebak kategori dari deskripsi.

Contoh:

python main.py add 15000 "" 2025-01-01 -d "beli kopi"
→ otomatis kategori = minum

✔ 10. Backup Otomatis

Setiap aplikasi dijalankan:

database dibackup ke folder backup/

backup lama > 7 hari otomatis dihapus

✔ 11. PIN Keamanan

Saat menjalankan list, pengguna harus memasukkan PIN.

✔ 12. PDF Report
python main.py laporan


Output:
📁 reports/laporan_keuangan.pdf

📁 Struktur Folder
project/
│── commands/
│── utils/
│── backup/
│── graphs/
│── logs/
│── reports/
│── db.py
│── main.py
│── requirements.txt
│── README.md

🛠 Instalasi
1. (Opsional) Buat virtual environment
python -m venv venv

2. Aktifkan virtual environment

Windows:

venv\Scripts\activate


Linux/Mac:

source venv/bin/activate

3. Install dependency
pip install -r requirements.txt

4. Jalankan aplikasi
python main.py --help

🧩 Contoh Perintah Pemakaian

Tambah:

python main.py add 20000 makan 2025-01-01 -d "sarapan"


List:

python main.py list


Filter:

python main.py filter --mulai 2025-01-01 --akhir 2025-01-31


Summary:

python main.py summary


Grafik:

python main.py graph


Laporan PDF:

python main.py laporan

📄 Lisensi

Aplikasi ini dibuat untuk tujuan pembelajaran Python, CLI, dan SQLite.
Bebas digunakan, dimodifikasi, dan dikembangkan ulang.

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)