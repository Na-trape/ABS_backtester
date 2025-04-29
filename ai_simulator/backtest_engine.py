# ai_simulator/backtest_engine.py

import pandas as pd

class BacktestEngine:
    def __init__(self, returns_df, weights, rebalance_frequency='M'):
        """
        Initialize the backtest engine.

        Args:
            returns_df (pd.DataFrame): Asset returns (daily).
            weights (pd.Series or pd.DataFrame): Portfolio weights.
            rebalance_frequency (str): Rebalancing frequency ('M' for monthly, 'W' for weekly, etc.)
        """
        self.returns_df = returns_df
        self.weights = weights
        self.rebalance_frequency = rebalance_frequency

    def run(self):
        """
        Run the backtest.

        Returns:
            pd.DataFrame: Daily strategy returns and cumulative equity curve.
        """

        # If weights are a Series (one-time allocation), expand it across all dates
        if isinstance(self.weights, pd.Series):
            expanded_weights = pd.DataFrame(
                [self.weights.values] * len(self.returns_df),
                index=self.returns_df.index,
                columns=self.weights.index
            )
        else:
            expanded_weights = self.weights

        # Handle rebalancing if needed
        expanded_weights = expanded_weights.resample(self.rebalance_frequency).ffill().reindex(self.returns_df.index, method='ffill')

        # Portfolio daily returns
        portfolio_returns = (self.returns_df * expanded_weights).sum(axis=1)

        # Equity curve
        equity_curve = (1 + portfolio_returns).cumprod()

        # Final output
        results = pd.DataFrame({
            'returns': portfolio_returns,
            'equity': equity_curve
        })

        return results
