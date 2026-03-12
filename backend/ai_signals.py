import pandas as pd
import numpy as np
import pickle
import os
from order_blocks import detect_order_block
from sklearn.ensemble import RandomForestClassifier

class AISignalEngine:
    def __init__(self, model_path="ai_model.pkl"):
        self.model_path = model_path
        self.model = self.load_model()

    def load_model(self):
        if os.path.exists(self.model_path):
            with open(self.model_path, "rb") as f:
                return pickle.load(f)
        else:
            return RandomForestClassifier(n_estimators=100)

    def extract_features(self, df):
        # Фичи: количество OB, изменение цены, волатильность
        df['OB'] = [len(detect_order_block(df.iloc[:i+1])) for i in range(len(df))]
        df['delta'] = df['close'].diff().fillna(0)
        df['volatility'] = df['high'] - df['low']
        return df[['OB','delta','volatility']]

    def predict(self, df):
        features = self.extract_features(df)
        if hasattr(self.model, "predict_proba"):
            return self.model.predict_proba(features)[-1][1]  # вероятность последнего сигнала
        return 0.5

    def train(self, X, y):
        self.model.fit(X, y)
        with open(self.model_path, "wb") as f:
            pickle.dump(self.model, f)
