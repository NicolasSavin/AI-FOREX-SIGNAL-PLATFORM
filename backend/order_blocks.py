import pandas as pd
import numpy as np

def detect_order_block(data, window=20, threshold=0.002):
    """
    Находит Order Blocks (OB) в данных.
    data: DataFrame с колонками ['timestamp','open','high','low','close']
    window: сколько свечей смотреть назад
    threshold: минимальная разница high-low для OB
    """
    order_blocks = []
    highs = data['high'].values
    lows = data['low'].values
    closes = data['close'].values

    for i in range(window, len(data)):
        high_window = highs[i-window:i]
        low_window = lows[i-window:i]
        if np.max(high_window) - np.min(low_window) < threshold:
            ob = {
                'timestamp': data['timestamp'].iloc[i],
                'high': np.max(high_window),
                'low': np.min(low_window),
                'type': 'bullish' if closes[i] > closes[i-1] else 'bearish'
            }
            order_blocks.append(ob)
    return order_blocks
