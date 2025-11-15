import sys
import os
import requests
from datetime import datetime

JRAVIS_BACKEND = os.getenv("JRAVIS_BACKEND", "https://jravis-backend.onrender.com")

def send_daily():
    print("📅 Sending DAILY report request...")
    r = requests.get(f"{JRAVIS_BACKEND}/send_daily_report")
    print("Response:", r.text)

def send_weekly():
    print("📅 Sending WEEKLY report request...")
    r = requests.get(f"{JRAVIS_BACKEND}/send_weekly_report")
    print("Response:", r.text)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❌ No argument provided (use: daily or weekly)")
        sys.exit(1)

    mode = sys.argv[1]

    if mode == "daily":
        send_daily()
    elif mode == "weekly":
        send_weekly()
    else:
        print("❌ Invalid argument:", mode)
