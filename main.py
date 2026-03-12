from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import json, os

app = FastAPI()

# Путь к картинкам в signals_data (относительно корня репозитория)
signals_dir = os.path.join(os.getcwd(), "signals_data")

if os.path.exists(signals_dir):
    app.mount("/tradingview_images", StaticFiles(directory=signals_dir), name="images")

# Путь к звуку
frontend_dir = os.path.join(os.getcwd(), "frontend")
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
            data = json.load(f)
        return data
    return []
