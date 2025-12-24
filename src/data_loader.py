import yfinance as yf
import pandas as pd

def fetch_stock_data(tickers, start='2023-01-01', end='2025-09-01'):
    return yf.download(tickers, start=start, end=end, auto_adjust=True)['Close']