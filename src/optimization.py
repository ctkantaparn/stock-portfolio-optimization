import numpy as np
from scipy.optimize import minimize

def portfolio_metrics(weights, returns):
    mean_returns = returns.mean()
    cov_matrix = returns.cov()

    port_return = np.sum(weights * mean_returns) * 252
    port_vol = np.sqrt(np.dot(weights.T, np.dot((cov_matrix* 252), weights)))
    sharpe_ratio = port_return / port_vol

    return port_return, port_vol, sharpe_ratio

def optimize_portfolio(returns):
    num_assets = returns.shape[1]

    mean_returns = returns.mean()
    cov = returns.cov()

    def neg_sharpe(weights):
        return -portfolio_metrics(weights, returns)[2]

    constraints = {'type': 'eq', 'fun': lambda w: np.sum(w) - 1}
    bounds = tuple((0, 1) for _ in range(num_assets))
    init_guess = num_assets * [1 / num_assets]

    result = minimize(
        neg_sharpe,
        init_guess,
        method='SLSQP',
        bounds=bounds,
        constraints=constraints
    )

    return result.x