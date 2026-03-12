from fastapi import FastAPI

app = FastAPI()

# Главная страница для проверки сервера
@app.get("/")
def root():
    return {"status": "server running"}

# Endpoint с тестовыми AI-сигналами
@app.get("/ai_signals")
def ai_signals():
    # Минимальный тестовый сигнал
    return [
        {
            "pair": "EURUSD",
            "timeframe": "1H",
            "probability": 75,
            "status": "active",
            "description": "Test signal"
        },
        {
            "pair": "GBPUSD",
            "timeframe": "4H",
            "probability": 65,
            "status": "active",
            "description": "Test signal"
        }
    ]
