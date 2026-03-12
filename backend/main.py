from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "server running"}

@app.get("/ai_signals")
def ai_signals():
    # Тестовые сигналы
    return [
        {"pair": "EURUSD", "timeframe": "1H", "probability": 75, "status": "active", "description": "Test signal"},
        {"pair": "GBPUSD", "timeframe": "4H", "probability": 65, "status": "active", "description": "Test signal"}
    ]
