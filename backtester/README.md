# Quant Strategy Simulator — ABS Finance AI Module

This project is a modular, lightweight **strategy backtesting engine** built for the ABS Finance hackathon project, used in the **AI Strategy Playground**.

It is designed for **DeFi yield vault strategy simulation** on Solana assets, but structured cleanly to also support general quant research and trading strategies.

---

## 📈 Features

- Load and preprocess historical price data
- Generate portfolio strategies using Riskfolio-Lib (min volatility, max Sharpe)
- Simulate portfolio performance over historical data
- Evaluate key performance metrics (APY, Sharpe Ratio, Max Drawdown)
- Save backtest results and evaluation logs
- Modular, extensible, and research-ready

---

## 🚀 Quick Start

1. Install dependencies:

```bash
pip install -r requirements.txt
