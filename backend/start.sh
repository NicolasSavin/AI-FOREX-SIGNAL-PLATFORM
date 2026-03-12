#!/usr/bin/env bash

# Обновляем pip
python -m pip install --upgrade pip

# Устанавливаем зависимости
python -m pip install -r requirements.txt

# Запускаем FastAPI через uvicorn
python -m uvicorn main:app --host 0.0.0.0 --port $PORT
