import os, json, time, random
from datetime import datetime
import yfinance as yf

PAIRS = [
    "EURUSD","GBPUSD","USDJPY","AUDUSD","USDCAD","USDCHF","NZDUSD",
    "EURGBP","EURJPY","GBPJPY","AUDJPY","CADJPY","CHFJPY","NZDJPY",
    "AUDCAD","AUDCHF","AUDNZD","CADCHF","EURAUD","EURCAD","EURNZD",
    "GBPAUD","GBPCAD","GBPCHF","GBPNZD","NZDCAD","NZDCHF","USDNOK"
]

SIGNALS_JSON = "signals_data/signals.json"
SIGNALS_DIR = "signals_data"

if not os.path.exists(SIGNALS_DIR):
    os.makedirs(SIGNALS_DIR)

PLACEHOLDER = os.path.join(SIGNALS_DIR, "placeholder.png")  # можно один PNG для всех пар

def get_ohlcv(pair):
    ticker = pair.replace("/", "") + "=X"
    df = yf.download(ticker, interval="1h", period="30d")
    return df

def analyze_signal(df):
    last = df.iloc[-1]
    if last["Close"] < last["Open"]:
        return "Возврат к ордер-блоку", random.randint(70, 90)
    else:
        return "Снятие ликвидности", random.randint(60, 80)

def screenshot_placeholder(pair):
    path = os.path.join(SIGNALS_DIR, f"{pair}_1H.png")
    if not os.path.exists(path) and os.path.exists(PLACEHOLDER):
        import shutil
        shutil.copyfile(PLACEHOLDER, path)

def generate_signals():
    signals = []
    for pair in PAIRS:
        df = get_ohlcv(pair)
        desc, prob = analyze_signal(df)
        screenshot_placeholder(pair)
        signals.append({
            "pair": pair,
            "timeframe": "1H",
            "probability": prob,
            "status": "active" if prob>65 else "inactive",
            "description": desc,
            "image_url": f"/tradingview_images/{pair}_1H.png",
            "sound_url": "/sounds/alert.mp3"
        })
    with open(SIGNALS_JSON, "w", encoding="utf-8") as f:
        json.dump(signals, f, ensure_ascii=False, indent=2)

# Обновление каждые 5 минут
while True:
    generate_signals()
    print(f"[{datetime.now()}] Signals updated")
    time.sleep(300)
