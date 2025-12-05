<p align="center">
  <img src="Screenshot 2025-11-21 104934.png" width="50%">
</p>

<h1 align="center">💰 Aplikasi Pengelola Keuangan Harian (CLI + SQLite)</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue">
  <img src="https://img.shields.io/badge/SQLite-Database-green">
  <img src="https://img.shields.io/badge/CLI-Application-orange">
  <img src="https://img.shields.io/badge/Status-Active-success">
</p>

<p align="center">
  Aplikasi CLI modern untuk mencatat transaksi keuangan, lengkap dengan dashboard, grafik pengeluaran, AI kategori otomatis,
  backup otomatis, import/export CSV, PIN keamanan, dan laporan PDF.
</p>

---

## 🎬 Video Presentasi
<p align="center">
  👉 <a href="https://youtu.be/1W2tmPaFEys?si=cnNEt1nz7DuWP4cJ" target="_blank"><b>Tonton Presentasi di YouTube</b></a> 👈
</p>

---

## 📸 Preview UI CLI
<p align="center">
  <img src="image.png" width="55%">
</p>

---

## 🚀 Fitur Utama

| Fitur | Deskripsi |
|------|-----------|
| 📥 **Tambah Transaksi** | Input cepat + kategori + deskripsi + tanggal |
| 📊 **Dashboard Lengkap** | Ringkasan harian, mingguan, bulanan & top kategori |
| 🔎 **Filter Tanggal** | Filter tanggal tertentu atau rentang |
| 📁 **Import / Export CSV** | Backup dan migrasi data sangat mudah |
| 📈 **Grafik Pengeluaran** | Grafik otomatis tersimpan sebagai PNG |
| 🤖 **AI Kategori Otomatis** | Mendeteksi kategori dari deskripsi |
| 🔐 **PIN Security** | Melindungi akses perintah list |
| 📑 **PDF Report** | Laporan keuangan dalam format PDF |
| 💾 **Auto Backup Database** | Backup harian & auto clean backup > 7 hari |

---

## 🧭 Contoh Perintah CLI

### ➕ Tambah Transaksi
```sh
python main.py add 15000 jajan 2025-01-02 -d "beli snack"
📋 Dashboard (List Transaksi)
sh
Copy code
python main.py list
🎯 Filter Transaksi
sh
Copy code
python main.py filter --mulai 2025-01-01 --akhir 2025-01-31
📈 Grafik Pengeluaran
sh
Copy code
python main.py graph
<p align="center"> <img src="grap.png" width="60%"> </p>
📥 Import CSV
sh
Copy code
python main.py import data.csv
📤 Export CSV
sh
Copy code
python main.py export output.csv
📝 PDF Report
sh
Copy code
python main.py laporan
🗂 Struktur Folder
txt
Copy code
📁 project/
│── commands/
│── utils/
│── backup/
│── graphs/
│── reports/
│── logs/
│── db.py
│── main.py
│── requirements.txt
│── README.md
⚙️ Instalasi
1️⃣ Buat virtual environment
sh
Copy code
python -m venv venv
2️⃣ Aktifkan environment
Windows

sh
Copy code
venv\Scripts\activate
Linux/MacOS

sh
Copy code
source venv/bin/activate
3️⃣ Install dependencies
sh
Copy code
pip install -r requirements.txt
4️⃣ Jalankan aplikasi
sh
Copy code
python main.py --help
📄 Lisensi
Free to use, modify, and redistribute for educational and personal projects.

<p align="center"><b>Developed by:</b></p> <p align="center"> ALFARIZI MAULANA HIDAYAT (2410631160003) • MUHAMMAD RIFKY DWINOVA AKBAR (2410631160028) • MUHAMMAD KHOLILUR ROHMAN (2410631160079) • HAFIZH HUSNULLABIB ACHMAD (2410631160119) • ADAM FIRMAN </p> <p align="center">🔥 Terima kasih sudah menggunakan aplikasi ini! 🔥</p> ```
