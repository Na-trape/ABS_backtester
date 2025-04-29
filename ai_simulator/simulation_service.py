# ai_simulator/simulation_service.py

import os
from ai_simulator.data_loader import load_price_data, convert_prices_to_returns
from ai_simulator.strategy_generator import generate_strategy_weights
from ai_simulator.backtest_engine import BacktestEngine
from ai_simulator.metrics import evaluate_backtest

def run_simulation(price_file_path, strategy_type='min_volatility', save_results=True, output_dir='results'):
    """
    Run a full simulation from start to finish.

    Args:
        price_file_path (str): Path to the CSV with prices.
        strategy_type (str): Strategy to use ('min_volatility', 'max_sharpe').
        save_results (bool): Whether to save results to files.
        output_dir (str): Where to save results.

    Returns:
        tuple: (results DataFrame, metrics dict)
    """

    # 1. Load and process data
    price_df = load_price_data(price_file_path)
    returns_df = convert_prices_to_returns(price_df)

    # 2. Generate strategy weights
    weights = generate_strategy_weights(returns_df, strategy_type=strategy_type)

    # 3. Run backtest
    backtest_engine = BacktestEngine(returns_df, weights)
    results = backtest_engine.run()

    # 4. Evaluate performance
    metrics = evaluate_backtest(results)

    # 5. Save results
    if save_results:
        os.makedirs(output_dir, exist_ok=True)
        strategy_name = strategy_type.replace(' ', '_')
        results.to_csv(os.path.join(output_dir, f"{strategy_name}_returns.csv"))

        with open(os.path.join(output_dir, f"{strategy_name}_metrics.txt"), "w") as f:
            for k, v in metrics.items():
                f.write(f"{k}: {v}\n")

    return results, metrics
