# Stock Portfolio Optimization (Python)

## 📌 Overview
This project implements a Python-based stock analysis and portfolio optimization tool using historical equity data.  
It evaluates risk-adjusted returns, diversification benefits, and optimal asset allocation using modern portfolio theory.

The project fetches historical stock prices, calculates financial metrics such as returns, volatility, and correlations, and constructs an optimal portfolio by maximizing the Sharpe ratio.

---

## 🧠 Key Features
- Historical stock data retrieval using Yahoo Finance
- Return, volatility, and correlation analysis
- Portfolio optimization using Sharpe ratio maximization
- Clear, interpretable financial visualizations
- Modular, reusable Python code

---

## 📊 Visualizations

### Stock Prices Over Time
Shows historical adjusted closing prices for selected equities.

![Stock Prices Over Time](visuals/charts/stock_prices_over_time.png)

---

### Return Distributions
Histograms illustrating the distribution of daily returns for each asset.

![Returns Distributions](visuals/charts/returns_distributions.png)

---

### Correlation Matrix
Heatmap displaying correlations between stock returns to highlight diversification effects.

![Correlation Matrix](visuals/charts/correlation_matrix.png)

---

### Optimal Portfolio Allocation
Visualization of optimal asset weights derived from Sharpe ratio optimization.

![Optimal Portfolio Allocation](visuals/charts/optimal_portfolio_allocation.png)

---

## 📊 Example Optimization Results

Using historical daily price data from **January 1, 2023 to September 1, 2025**, the portfolio optimizer computed the following optimal asset allocation. The optimization objective was to **maximize the Sharpe Ratio**, balancing expected return against volatility.

### Optimal Portfolio Weights
AAPL : 0.25%
MSFT : 8.12%
GOOGL : 15.29%
AMZN : 49.93%
JPM : 26.40%

### Portfolio Performance Metrics
- **Expected Annual Return:** 35.54%
- **Annualized Volatility:** 18.87%
- **Sharpe Ratio:** 1.88
  
---

#### Key Insights
- **JPM exhibits relatively low correlation** with major technology stocks (ranging from ~0.26 to ~0.33), making it a strong diversification asset and explaining its significant portfolio weight (**26.40%**).
- **AMZN, MSFT, and GOOGL show higher mutual correlations**, particularly between AMZN and MSFT (**0.64**) and AMZN and GOOGL (**0.60**). Despite this, AMZN dominates the allocation (**49.93%**) due to its superior risk-adjusted returns over the analyzed period.
- **AAPL is moderately correlated** with the rest of the portfolio while contributing less to diversification or return enhancement, resulting in a minimal allocation (**0.25%**).

#### Overall Interpretation
The optimizer balances return maximization with diversification by:
- Concentrating capital in **high-performing growth assets** (AMZN),
- Offsetting correlated tech exposure with **lower-correlated financial exposure** (JPM),
- Reducing allocations to assets that do not materially improve the portfolio’s Sharpe Ratio.

This correlation structure helps explain the portfolio’s relatively high **Sharpe Ratio of 1.88**, demonstrating efficient risk-adjusted allocation.


> ⚠️ **Disclaimer:**  
> These results are based solely on historical performance and do not guarantee future returns. This tool is intended for educational and analytical purposes only.

---

## ⚙️ Project Structure
```bash
stock-portfolio-optimization/
│
├── data/ # Raw or processed data (optional)
├── notebooks/
│ └── portfolio_analysis.ipynb
├── src/
│ ├── data_loader.py
│ ├── analytics.py
│ └── optimization.py
├── visuals/
│ └── charts/ # Saved visualizations
├── summary/
│ └── executive_summary.pdf
├── requirements.txt
└── README.md
```
---

## 🚀 How to Run the Project

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/stock-portfolio-optimization.git
cd stock-portfolio-optimization
```

2. Run the analysis 
```bash
jupyter notebook notebooks/portfolio_analysis.ipynb
```

