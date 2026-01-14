from assets.update_app import UpdateWindow
from assets.version_checker import is_update_available
from assets.updater import update_and_restart
from pathlib import Path
import subprocess
import sys

BASE_DIR = Path(__file__).resolve().parent

# ======== KONFIGURACJA UPDATERA ========

GITHUB_CLIENT_URL = "https://raw.githubusercontent.com/USER/REPO/main/main.py"
HEADERS = {"User-Agent": "Updater"}

LOCAL_FILE = str(BASE_DIR / "main.py")
VERSION_FILE = str(BASE_DIR / "version.npc")
NEW_VERSION_ID = "1.0.0"   # ← aktualizuj przy każdej nowej wersji

# =======================================

def check_for_update():
    return is_update_available()

def download_update():
    update_and_restart(
        github_url=GITHUB_CLIENT_URL,
        headers=HEADERS,
        local_file=LOCAL_FILE,
        version_file=VERSION_FILE,
        version_id=NEW_VERSION_ID
    )

def start_main_app():
    subprocess.Popen([sys.executable, str(BASE_DIR / "main.py")])

if __name__ == "__main__":
    updater = UpdateWindow(
        check_update_callback=check_for_update,
        download_callback=download_update,
        continue_callback=start_main_app
    )
    updater.run()
