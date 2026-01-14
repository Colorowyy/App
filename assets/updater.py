import requests
import sys
import subprocess

def update_and_restart(
    github_url: str,
    headers: dict,
    local_file: str,
    version_file: str,
    version_id: str
):
    try:
        r = requests.get(github_url, headers=headers, timeout=10)

        if r.status_code == 200:
            # 1) Pobierz i zapisz nową wersję pliku
            with open(local_file, "w", encoding="utf-8") as f:
                f.write(r.text)

            # 2) Zapisz nową wersję lokalnie
            with open(version_file, "w", encoding="utf-8") as f:
                f.write(version_id)

            # 3) Uruchom ponownie aplikację
            python = sys.executable
            subprocess.Popen([python, local_file])

            sys.exit(0)

        else:
            print(f"Error downloading update (status {r.status_code})")

    except Exception as e:
        print(f"Update failed: {e}")
