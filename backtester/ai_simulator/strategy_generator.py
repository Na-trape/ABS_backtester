# ai_simulator/strategy_generator.py

import riskfolio.Portfolio as pf

def generate_strategy_weights(returns_df, strategy_type='min_volatility'):
    """
    Generate portfolio weights using Riskfolio-Lib based on the given strategy type.

    Args:
        returns_df (pd.DataFrame): Historical returns for each asset.
        strategy_type (str): Strategy type - 'min_volatility' or 'max_sharpe'.

    Returns:
        pd.Series: Portfolio weights.
    """

    port = pf.Portfolio(returns=returns_df)
    port.assets_stats(method_mu='hist', method_cov='hist')

    if strategy_type == 'min_volatility':
        weights = port.optimization(model='Classic', obj='MinRisk', rm='MV')
    elif strategy_type == 'max_sharpe':
        weights = port.optimization(model='Classic', obj='Sharpe', rm='MV')
    else:
        raise ValueError(f"Unsupported strategy type: {strategy_type}")

    return weights
