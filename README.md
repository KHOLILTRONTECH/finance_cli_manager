<p align="center"><img src="assets/banner.png" width="100%"></p>
<h1 align="center">💰 Aplikasi Pengelola Keuangan Harian (CLI + SQLite)</h1> <p align="center"> <img src="https://img.shields.io/badge/Python-3.10+-blue"> <img src="https://img.shields.io/badge/SQLite-Database-green"> <img src="https://img.shields.io/badge/CLI-Application-orange"> <img src="https://img.shields.io/badge/Status-Active-success"> </p> <p align="center"> Aplikasi CLI modern untuk mencatat transaksi keuangan, lengkap dengan dashboard, grafik, AI kategori otomatis, backup otomatis, dan laporan PDF. </p>
📸 Preview UI CLI
<p align="center"> <img src="assets/preview_dashboard.png" width="80%"> </p>
🚀 Fitur Utama
Fitur	Deskripsi
📥 Tambah Transaksi	Input cepat + deskripsi + tanggal
📊 Dashboard	Ringkasan harian, mingguan, bulanan
🔎 Filter Tanggal	Tanggal tertentu atau rentang
📁 Import / Export CSV	Untuk backup & migrasi data
📈 Grafik Pengeluaran	Matplotlib otomatis simpan PNG
🤖 AI Kategori Otomatis	Menebak kategori dari deskripsi
🔐 PIN Security	Melindungi akses list
📑 PDF Report	Laporan siap print
💾 Auto Backup	Backup harian + auto clean 7 hari
🧭 Demo Perintah
➕ Tambah Transaksi
python main.py add 15000 jajan 2025-01-02 -d "beli snack"

📋 Dashboard
python main.py list

🎯 Filter Transaksi
python main.py filter --mulai 2025-01-01 --akhir 2025-01-31

📈 Grafik
python main.py graph

<p align="center"> <img src="assets/graph_preview.png" width="70%"> </p>
🗂 Struktur Folder
project/
│── assets/               # gambar banner, preview
│── commands/
│── utils/
│── backup/
│── graphs/
│── reports/
│── db.py
│── main.py
│── requirements.txt
│── README.md

⚙️ Instalasi
1. Buat virtual environment
python -m venv venv

2. Aktifkan

Windows:

venv\Scripts\activate

3. Install dependency
pip install -r requirements.txt

4. Jalankan
python main.py --help

📄 Lisensi

Free to use, modify, redistribute.
