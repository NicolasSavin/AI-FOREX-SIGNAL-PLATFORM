from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Разрешаем фронтенду обращаться к серверу
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Простейший маршрут для проверки работы
@app.get("/ai_signals")
def get_ai_signals():
    return [{
        "pair": "EURUSD",
        "timeframe": "1H",
        "probability": 75,
        "status": "active",
        "description": "Тестовый сигнал"
    }]

@app.get("/telegram_post")
def get_telegram_post():
    return {"post": "Это тестовый пост из Telegram"}
