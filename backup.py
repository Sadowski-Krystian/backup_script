import os
import tarfile
import logging
from datetime import datetime
import shutil


SOURCE_PATHS = ["/home/gulgulglut/Documents", "/nieistniejaca/sciezka/test"] 
BACKUP_DIR = "/backup" 
LOG_FILE = "/backup/backup_log.log" 


logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def create_backup():
    try:
        
        if not os.path.exists(BACKUP_DIR):
            os.makedirs(BACKUP_DIR)
            logging.info(f"Stworzono katalog docelowy: {BACKUP_DIR}")

        timestamp = datetime.now().strftime("%Y-%m-%d")
        backup_name = f"backup_{timestamp}.tar.gz"
        backup_path = os.path.join(BACKUP_DIR, backup_name)

        with tarfile.open(backup_path, "w:gz") as tar:
            for path in SOURCE_PATHS:
                if os.path.exists(path):
                    tar.add(path, arcname=os.path.basename(path))
                    logging.info(f"Dodano do archiwum: {path}")
                else:
                    logging.warning(f"Ścieżka nie istnieje: {path}")

        logging.info(f"Utworzono kopię zapasową: {backup_path}")
    except Exception as e:
        logging.error(f"Błąd podczas tworzenia kopii zapasowej: {e}")

if __name__ == "__main__":
    create_backup()
