# ai_simulator/data_loader.py

import pandas as pd

def load_price_data(file_path):
    """Loads price data from CSV and returns a DataFrame."""
    df = pd.read_csv(file_path, index_col=0, parse_dates=True)
    return df

def convert_prices_to_returns(price_df):
    """Converts price data into daily returns."""
    returns = price_df.pct_change().dropna()
    return returns
