import os
import time
import requests
import threading
from fastapi import FastAPI
import uvicorn

app = FastAPI()

BRAIN_URL = os.getenv("BRAIN_URL", "https://jravis-brain.onrender.com")

@app.get("/")
def home():
    return {"status": "worker-running"}

@app.get("/healthz")
def health():
    return {"status": "ok"}

def worker_loop():
    print("🔥 Worker loop started")
    while True:
        try:
            r = requests.get(f"{BRAIN_URL}/healthz", timeout=5)
            print("🧠 Brain status:", r.status_code)
        except Exception as e:
            print("❌ Worker error:", e)
        time.sleep(10)

def start_worker():
    t = threading.Thread(target=worker_loop)
    t.daemon = True
    t.start()

if __name__ == "__main__":
    # Start worker in background thread
    start_worker()

    # Start dummy HTTP server so Render sees a port
    uvicorn.run(app, host="0.0.0.0", port=8000)
