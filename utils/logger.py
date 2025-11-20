import logging
from pathlib import Path

# pastikan folder logs/ ada
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "app.log"

# konfigurasi logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s  %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()  # tampilkan di terminal juga
    ]
)

logger = logging.getLogger("finance_app")
