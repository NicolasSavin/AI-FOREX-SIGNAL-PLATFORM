from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import json, os

app = FastAPI()

signals_dir = os.path.join(os.getcwd(), "signals_data")
frontend_dir = os.path.join(os.getcwd(), "frontend")

# Картинки сигналов
if os.path.exists(signals_dir):
    app.mount("/tradingview_images", StaticFiles(directory=signals_dir), name="images")

# Звук
if os.path.exists(os.path.join(frontend_dir, "alert.mp3")):
    app.mount("/sounds", StaticFiles(directory=frontend_dir), name="sounds")

@app.get("/")
def root():
    return {"status": "server_running"}

@app.get("/ai_signals")
def ai_signals():
    signals_json = os.path.join(signals_dir, "signals.json")
    if os.path.exists(signals_json):
        with open(signals_json, "r", encoding="utf-8") as f:
            return json.load(f)
    return []
