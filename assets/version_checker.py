import requests
from pathlib import Path

GITHUB_RAW_URL = "https://raw.githubusercontent.com/Colorowyy/App/refs/heads/main/version.npc"

BASE_DIR = Path(__file__).resolve().parent.parent
LOCAL_VERSION_FILE = BASE_DIR / "version.npc"

def get_local_version():
    if not LOCAL_VERSION_FILE.exists():
        return "0.0.0"
    return LOCAL_VERSION_FILE.read_text(encoding="utf-8").strip()

def get_latest_version():
    response = requests.get(GITHUB_RAW_URL, timeout=5)
    response.raise_for_status()
    return response.text.strip()

def is_update_available():
    try:
        local_version = get_local_version()
        latest_version = get_latest_version()
        print(f"Local version: {local_version}")
        print(f"Latest version: {latest_version}")
        return local_version != latest_version
    except Exception as e:
        print(f"Update check failed: {e}")
        return False
