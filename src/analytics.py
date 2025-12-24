import pandas as pd
import numpy as np

def calculate_returns(prices):
    return prices.pct_change().dropna()

def calculate_volatility(returns):
    return returns.std() * np.sqrt(252)

def calculate_correlation(returns):
    return returns.corr()