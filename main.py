from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import json
import os

app = FastAPI()

# Подключаем папку со скриншотами
if os.path.exists("signals_data"):
    app.mount("/tradingview_images", StaticFiles(directory="signals_data"), name="images")

# Подключаем папку со звуком
if os.path.exists("frontend/alert.mp3"):
    app.mount("/sounds", StaticFiles(directory="frontend"), name="sounds")

@app.get("/")
def root():
    return {"status":"server_running"}

@app.get("/ai_signals")
def ai_signals():
    # Читаем JSON, который обновляет worker.py
    with open("signals_data/signals.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    return data
