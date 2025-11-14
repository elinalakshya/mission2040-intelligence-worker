import os
import time
import requests

BRAIN_URL = os.getenv("BRAIN_URL", "https://jravis-brain.onrender.com")

def ping_brain():
    try:
        res = requests.get(f"{BRAIN_URL}/healthz", timeout=5)
        if res.status_code == 200:
            print("[Worker] ✅ Connected to JRAVIS Brain")
        else:
            print("[Worker] ⚠️ Brain error:", res.text)
    except Exception as e:
        print("[Worker] ❌ Cannot reach Brain:", e)

def run():
    print("[Worker] 🚀 Mission 2040 Intelligence Worker Started")
    while True:
        ping_brain()
        time.sleep(60)

if __name__ == "__main__":
    run()
