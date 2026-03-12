import os, json, time, random
from datetime import datetime
import yfinance as yf
import openai
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller

# Валютные пары
PAIRS = ["EURUSD","GBPUSD","USDJPY","AUDUSD","USDCAD","USDCHF","NZDUSD",
         "EURGBP","EURJPY","GBPJPY","AUDJPY","CADJPY","CHFJPY","NZDJPY",
         "AUDCAD","AUDCHF","AUDNZD","CADCHF","EURAUD","EURCAD","EURNZD",
         "GBPAUD","GBPCAD","GBPCHF","GBPNZD","NZDCAD","NZDCHF","USDNOK"]

SIGNALS_DIR = "signals_data"
SIGNALS_JSON = os.path.join(SIGNALS_DIR, "signals.json")
PLACEHOLDER = os.path.join(SIGNALS_DIR, "placeholder.png")

if not os.path.exists(SIGNALS_DIR):
    os.makedirs(SIGNALS_DIR)

# Динамическое уникальное описание через GPT
def generate_unique_description(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role":"user","content":prompt}],
        temperature=0.8,
        max_tokens=50
    )
    return response.choices[0].message['content'].strip()

# Получение исторических свечей
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

# Скриншот TradingView через Selenium
def screenshot_tradingview(pair, timeframe="1H"):
    chromedriver_autoinstaller.install()
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    
    driver = webdriver.Chrome(options=options)
    url = f"https://www.tradingview.com/chart/?symbol=FX:{pair}"
    driver.get(url)
    time.sleep(5)
    
    path = os.path.join(SIGNALS_DIR, f"{pair}_{timeframe}.png")
    driver.save_screenshot(path)
    driver.quit()
    return path

# Генерация сигналов
def generate_signals():
    signals = []
    for pair in PAIRS:
        df = get_ohlcv(pair)
        last_price = df.iloc[-1]["Close"]
        last_three = df.tail(3)[["Open","High","Low","Close"]].to_dict('records')
        
        prompt = f"Создай уникальное описание торгового сигнала для {pair}. Текущая цена: {last_price}. Последние свечи: {last_three}. Используй термины ордер-блок, FVG, снятие ликвидности."
        desc = generate_unique_description(prompt)
        
        prob = random.randint(60, 90)
        screenshot_tradingview(pair)
        
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
