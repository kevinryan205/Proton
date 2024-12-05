import os
import re
import shutil
import time
import psutil
import subprocess


# Set up file paths
config_file = r"C:\Users\Kevin\AppData\Roaming\qBittorrent\qBittorrent.ini"
log_file = r"C:\Users\Kevin\AppData\Local\ProtonVPN\Logs\app-logs.txt"

# Custom error message
error_message = "An error occured:"

# Define function to simulate the passage of time
def simulate_time_passage(decimal_count):
    for i in range(decimal_count, 0, -1):
        print("." * i)
        time.sleep(1)


from ensure_vpn import ensure_vpn
from ensure_vpn.providers import ProtonVPN

ensure_vpn("ProtonVPN")
proto = ProtonVPN()._fetch_servers()
print(proto)
# def restart_progs():
#     # Check if programs are open
#     print("Checking program status...")
#     time.sleep(2)  # TIME_SIMULATION
#     print(".")

#     programs_running = False
#     process_names = ["JDownloader2.exe", "ProtonVPN.exe", "ProtonVPNService.exe"]

#     for proc in psutil.process_iter():
#         try:
#             if proc.name() in process_names:
#                 if proc.name() == "qbittorrent.exe":
#                     proc.terminate()
#                 elif proc.name() == "ProtonVPN.exe":
#                     proc.kill()
#                 elif proc.name() == "ProtonVPNService.exe":
#                     proc.kill()
#                 programs_running = True
#         except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
#             pass

#     if programs_running:
#         print("Instances found. Terminating now...")
#         time.sleep(3)  # Wait for 3 seconds before moving on

#         for proc in psutil.process_iter():
#             try:
#                 if proc.name() in process_names:
#                     if proc.name() == "JDownloader2.exe":
#                         proc.terminate()
#                     elif proc.name() == "ProtonVPN.exe":
#                         proc.kill()
#                     elif proc.name() == "ProtonVPNService.exe":
#                         proc.kill()
#             except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
#                 pass
                
#         time.sleep(1)  # TIME_SIMULATION
#         print(".")
        
#     else:
#         print("No instances found. Programs ready to start.")
#         time.sleep(1)
#         print(".")

#     # Start ProtonVPN
#     print("Initializing ProtonVPN...")
#     os.startfile(r"C:\Program Files\Proton\VPN\ProtonVPN.Launcher.exe")
#     time.sleep(5)  # TIME_SIMULATION
#     print(".")
#     time.sleep(5)  # TIME_SIMULATION
#     print(".")
#     time.sleep(1) # **NECESSARY** TIME_SIMULATION
#     print(".")
#     time.sleep(1) # **NECESSARY** TIME_SIMULATION
#     print(".")
#     time.sleep(1) # **NECESSARY** TIME_SIMULATION
#     print(".")
#     time.sleep(1) # **NECESSARY** TIME_SIMULATION
#     print(".")
#     time.sleep(1) # **NECESSARY** TIME_SIMULATION
#     print(".")
#     time.sleep(1) # **NECESSARY** TIME_SIMULATION
#     print(".")
#     time.sleep(1) # **NECESSARY** TIME_SIMULATION
#     print(".")
#     time.sleep(1) # **NECESSARY** TIME_SIMULATION
#     print(".")
#     time.sleep(1) # **NECESSARY** TIME_SIMULATION
#     print(".")

#     # Start J Downloader2
#     qbittorrent_exe = r"C:\Users\Kevin\AppData\Local\JDownloader v2.0\JDownloader2.exe"
#     if os.path.exists(qbittorrent_exe):
#         os.startfile(qbittorrent_exe)
#     else:
#         print("Error: JDownloader2 executable not found.")

#     print("Done!")
                        
#     time.sleep(3)
#     print("X_X")
#     time.sleep(1)
#     exit