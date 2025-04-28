# ai_simulator/metrics.py

import numpy as np

def compute_sharpe_ratio(returns, risk_free_rate=0):
    """
    Compute the Sharpe ratio of returns.

    Args:
        returns (pd.Series): Daily returns.
        risk_free_rate (float): Daily risk-free rate (default 0).

    Returns:
        float: Sharpe Ratio
    """
    excess_returns = returns - risk_free_rate
    return np.mean(excess_returns) / (np.std(excess_returns) + 1e-8) * np.sqrt(252)

def compute_apy(cumulative_returns, num_days):
    """
    Compute the annualized percentage yield (APY).

    Args:
        cumulative_returns (pd.Series): Cumulative equity curve.
        num_days (int): Number of days in the backtest.

    Returns:
        float: APY
    """
    final_return = cumulative_returns.iloc[-1]
    apy = (final_return) ** (252 / num_days) - 1
    return apy

def compute_max_drawdown(cumulative_returns):
    """
    Compute the maximum drawdown.

    Args:
        cumulative_returns (pd.Series): Cumulative equity curve.

    Returns:
        float: Max drawdown (as negative number)
    """
    peak = cumulative_returns.cummax()
    drawdown = (cumulative_returns - peak) / peak
    return drawdown.min()

def evaluate_backtest(results_df):
    """
    Evaluate a backtest output.

    Args:
        results_df (pd.DataFrame): Must have 'returns' and 'equity' columns.

    Returns:
        dict: Metrics (APY, Sharpe, Max Drawdown)
    """
    returns = results_df['returns']
    cumulative_returns = results_df['equity']
    num_days = len(results_df)

    metrics = {
        'APY': round(compute_apy(cumulative_returns, num_days) * 100, 2),
        'Sharpe Ratio': round(compute_sharpe_ratio(returns), 4),
        'Max Drawdown': round(compute_max_drawdown(cumulative_returns) * 100, 2)
    }

    return metrics
