#!/usr/bin/env bash

# Обновляем pip и ставим зависимости
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

# Запуск FastAPI через uvicorn
python -m uvicorn main:app --host 0.0.0.0 --port $PORT
