# tests/test_full_simulation.py

from ai_simulator.simulation_service import run_simulation

def test_full_simulation():
    results, metrics = run_simulation(
        price_file_path='data/synthetic_prices.csv',
        strategy_type='min_volatility',
        save_results=False  # No need to save during simple test
    )

    assert not results.empty, "Backtest results should not be empty."
    assert 'returns' in results.columns, "'returns' column missing."
    assert 'equity' in results.columns, "'equity' column missing."

    assert metrics['APY'] is not None, "APY should not be None."
    assert metrics['Sharpe Ratio'] is not None, "Sharpe Ratio should not be None."
    assert metrics['Max Drawdown'] is not None, "Max Drawdown should not be None."

    print("Full simulation test passed ✅")

if __name__ == "__main__":
    test_full_simulation()
