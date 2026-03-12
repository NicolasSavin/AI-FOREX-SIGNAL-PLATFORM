from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from ai_signals import AISignalEngine

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

ai_engine = AISignalEngine()

@app.get("/ai_signals")
def get_ai_signals():
    # Генерация тестовых данных свечей
    df = pd.DataFrame({
        'timestamp': pd.date_range('2026-01-01', periods=50, freq='H'),
        'open': np.random.random(50),
        'high': np.random.random(50)+1,
        'low': np.random.random(50),
        'close': np.random.random(50)
    })
    prob = ai_engine.predict(df)
    signal_card = {
        "pair": "EURUSD",
        "timeframe": "1H",
        "probability": round(prob*100,2),
        "status": "active",
        "description": "SMC + OB + Divergence + FVG"
    }
    return [signal_card]
