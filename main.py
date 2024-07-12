import ctypes
import shutil
import sys
import requests
import os
import datetime
import subprocess

url = "https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/hosts/native.winoffice.txt"
local_filename = "hosts_temp"
hosts_file_path = r"C:\Windows\System32\drivers\etc\hosts"

def check_internet_connection():
    try:
        requests.get("http://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False

def check_is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def check_requirements():
    if not check_internet_connection():
        print("Fehler: Keine Internetverbindung vorhanden.")
        return False
    elif not check_is_admin():
        print("Fehler: Administratorrechte erforderlich.")
        return False
    else:
        return True

def download_file(url, local_filename):
    print("Es wird versucht, die Datei zu downloaden.")
    response = requests.get(url)
    if response.status_code == 200:
        with open(local_filename, "w", encoding="utf-8") as file:
            file.write(response.text)
        print(f"Die Datei wurde erfolgreich als '{local_filename}' gespeichert.")
        return True
    else:
        print(f"Fehler beim Herunterladen der Datei. Statuscode: {response.status_code}")
        return False

def remove_hosts_data():
    current_date = datetime.datetime.now().strftime("%d%m%Y")
    new_file_name = f"hosts_{current_date}.old"
    new_file_path = os.path.join(os.path.dirname(hosts_file_path), new_file_name)
    try:
        os.rename(hosts_file_path, new_file_path)
        print(f"Die Datei wurde erfolgreich umbenannt in '{new_file_name}'.")
        return True
    except FileNotFoundError:
        print("Fehler: Die Hosts-Datei wurde nicht gefunden.")
        return False
    except Exception as e:
        print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")
        return False

def move_data_to_destination(local_filename, hosts_file_path):
    try:
        print(f"Es wird versucht, die Datei '{local_filename}' nach '{hosts_file_path}' zu verschieben.")
        shutil.move(local_filename, hosts_file_path)
        print(f"Die Datei '{local_filename}' wurde erfolgreich nach '{hosts_file_path}' verschoben.")
        return True
    except Exception as e:
        print(f"Fehler: Die Datei '{local_filename}' konnte nicht verschoben werden: {e}")
        return False

def flush_dns():
    try:
        subprocess.run(["ipconfig", "/flushdns"], check=True)
        print("DNS-Cache erfolgreich geleert.")
    except subprocess.CalledProcessError as e:
        print(f"Fehler beim Leeren des DNS-Caches: {e}")

def main():
    if check_requirements():
        if download_file(url, local_filename):
            if remove_hosts_data():
                if move_data_to_destination(local_filename, hosts_file_path):
                    flush_dns()
                    print("Alle Schritte wurden erfolgreich abgeschlossen.")
                else:
                    print("Rollback: Wiederherstellung der alten Hosts-Datei.")
                    shutil.move(hosts_file_path, hosts_file_path.replace("hosts", f"hosts_{datetime.datetime.now().strftime('%d%m%Y')}.old"))
            else:
                print("Rollback: Wiederherstellung der alten Hosts-Datei.")
                shutil.move(hosts_file_path, hosts_file_path.replace("hosts", f"hosts_{datetime.datetime.now().strftime('%d%m%Y')}.old"))

if __name__ == "__main__":
    main()
