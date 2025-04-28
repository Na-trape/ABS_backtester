from ai_simulator.data_loader import load_price_data, convert_prices_to_returns
from ai_simulator.strategy_generator import generate_strategy_weights

price_df = load_price_data('data/synthetic_prices.csv')
returns_df = convert_prices_to_returns(price_df)

weights = generate_strategy_weights(returns_df, strategy_type='min_volatility')
print(weights)
