import os
import shutil
from datetime import datetime

BACKUP_DIR = "backup"
MAX_BACKUPS = 7


def auto_backup(db_path="project.db"):
    """
    Membuat backup database dengan timestamp dan melakukan cleanup.
    """

    # Jika DB belum ada → tidak usah backup
    if not os.path.exists(db_path):
        return

    # Pastikan folder backup ada
    os.makedirs(BACKUP_DIR, exist_ok=True)

    # Buat nama file backup
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_filename = f"project_{timestamp}.db"
    backup_path = os.path.join(BACKUP_DIR, backup_filename)

    # Copy database ke file backup
    shutil.copy(db_path, backup_path)

    # Cleanup backup lama
    cleanup_backups()


def cleanup_backups():
    """
    Menghapus backup lama, hanya menyisakan MAX_BACKUPS terbaru.
    """
    files = sorted(
        os.listdir(BACKUP_DIR)
    )

    # hanya file .db backup
    files = [f for f in files if f.endswith(".db")]

    if len(files) <= MAX_BACKUPS:
        return  # masih aman

    # Hitung file mana yang harus dihapus
    files_to_delete = files[0:len(files) - MAX_BACKUPS]

    for old_file in files_to_delete:
        os.remove(os.path.join(BACKUP_DIR, old_file))
