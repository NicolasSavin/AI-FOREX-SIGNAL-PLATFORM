from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Статика для картинок
app.mount("/tradingview_images", StaticFiles(directory="signals_data"), name="images")

# Генерация тестовых сигналов для 28 пар
PAIRS = [
    "EURUSD","GBPUSD","USDJPY","AUDUSD","USDCAD","USDCHF","NZDUSD",
    "EURGBP","EURJPY","GBPJPY","AUDJPY","CADJPY","CHFJPY","NZDJPY",
    "AUDCAD","AUDCHF","AUDNZD","CADCHF","EURAUD","EURCAD","EURNZD",
    "GBPAUD","GBPCAD","GBPCHF","GBPNZD","NZDCAD","NZDCHF","USDNOK"
]

AI_SIGNALS = []
for pair in PAIRS:
    AI_SIGNALS.append({
        "pair": pair,
        "timeframe": "1H",
        "probability": 70,
        "status": "active",
        "description": f"Сигнал AI для {pair} по ордерблокам, FVG, дивергенции",
        "image_url": f"https://ai-forex-signal-platform.onrender.com/tradingview_images/{pair}_1H.png"
    })

@app.get("/ai_signals")
def get_ai_signals():
    return AI_SIGNALS

@app.get("/")
def root():
    return {"status":"server_running"}
