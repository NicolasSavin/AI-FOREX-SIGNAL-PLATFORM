from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import random

app = FastAPI()

# Статика для картинок
app.mount("/tradingview_images", StaticFiles(directory="signals_data"), name="images")

PAIRS = [
    "EURUSD","GBPUSD","USDJPY","AUDUSD","USDCAD","USDCHF","NZDUSD",
    "EURGBP","EURJPY","GBPJPY","AUDJPY","CADJPY","CHFJPY","NZDJPY",
    "AUDCAD","AUDCHF","AUDNZD","CADCHF","EURAUD","EURCAD","EURNZD",
    "GBPAUD","GBPCAD","GBPCHF","GBPNZD","NZDCAD","NZDCHF","USDNOK"
]

def generate_ai_signal(pair):
    prob = random.randint(60, 90)
    status = "active" if prob > 65 else "inactive"
    return {
        "pair": pair,
        "timeframe": "1H",
        "probability": prob,
        "status": status,
        "description": f"Прототип AI сигнал для {pair}: ордерблоки, FVG, дивергенции",
        "image_url": f"https://ai-forex-signal-platform.onrender.com/tradingview_images/{pair}_1H.png"
    }

@app.get("/ai_signals")
def get_ai_signals():
    return [generate_ai_signal(pair) for pair in PAIRS]

@app.get("/")
def root():
    return {"status": "server_running"}
