# Bot-de-Investimentos-Binance

Lightweight Binance paper-trading bot (Python).

This repository contains a simple, educational trading bot that:

- Fetches market data from Binance (public endpoints)
- Displays a live GUI with price, recent trades, signals and balances
- Implements a basic moving-average skeleton trading strategy
- Simulates buy/sell (paper trading) and keeps a portfolio in-memory
- Persists trades and balances to `trades.json` for session resume

IMPORTANT: This project is educational. By default the bot is configured
to use Binance _testnet_ for safety and to simulate orders locally. Do
NOT use real API credentials unless you fully understand the risks.

---

## Requirements

- Python 3.8+
- Dependencies in `requirements.txt` (install with pip):

```powershell
pip install -r requirements.txt
```

Common libraries used:

- `requests` — HTTP calls to Binance
- `pandas` — small helpers when parsing klines
- `tkinter` — live GUI (usually available by default on Windows)

If `tkinter` is not available, the app falls back to console-only updates.

---

## Files overview

- `app.py` — main orchestrator. Collects user input, starts/stops the bot,
  runs the main loop, and creates the live GUI window (`LiveWindow`).
- `binance_client.py` — wrapper around Binance public endpoints. Fetches
  klines and price, and provides test-order helpers.
- `portfolio.py` — paper trading portfolio: tracks `_usdt_balance`,
  `_crypto_balance` and `_trade_history`. Methods to execute_buy /
  execute_sell update balances and record trades.
- `data_manager.py` — JSON persistence for trades and balances. The
  structured state file is `trades.json` (or `trades.data` depending on
  configuration). The class exposes `charge_data()` and `save_state()`.
- `moving_average_strategy.py` / `trading_strategy.py` — strategy
  scaffolding; the moving-average strategy is provided as a skeleton.
- `api_key.txt` — convenience file (if present) containing API Key and
  Secret. Keep it private and never commit real secrets to public
  repositories.

---

## Quick start

1. (Optional) Create a virtual environment and activate it.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Run the bot:

```powershell
python app.py
```

4. Follow the interactive prompts. If `trades.json` already contains
   persisted trades and balances, the bot will load the portfolio and
   skip asking for an initial capital amount.

5. Use the action menu to Start bot, Buy (simulated), Sell (simulated),
   Stop bot or Exit program.

---

## Live GUI

When `tkinter` is available a live window shows the following and updates
periodically (default 1 second):

- Pair and current price (with percent change)
- Last close price
- USDT balance and Crypto balance (updated after trades)
- Trade history (recent trades)
- Signals area (strategy messages)

The update interval is configurable in `LiveWindow` (parameter
`update_interval`). Rapid updates increase API call frequency; consider
raising the interval if you hit rate limits.

---

## Persistence

Trades and balances are saved to `trades.json` (structured format):

```json
{
  "trades": [...],
  "usdt_balance": 1000.0,
  "crypto_balance": 0.012345
}
```

On startup the app will load this file (if present) and initialize the
portfolio with those balances and the trade history.

---

## Safety & notes

- By default the bot uses testnet endpoints — check `binance_client.py`.
- The trading implemented is simulated (paper). No real orders are sent
  unless you explicitly modify the code to use real endpoints and keys.
- Keep API keys and secrets out of version control. `api_key.txt` is
  included for convenience but should be kept private.
- This project is intended for learning and experimentation. Do not
  deploy to production or use with large amounts of capital without
  extensive testing.

---

## Troubleshooting

- If `tkinter` window does not open: ensure Python was installed with
  `tcl/tk` support. On Windows the standard installer usually includes
  tkinter.
- If you see errors about missing modules: run `pip install -r
requirements.txt`.
- If balances don't update in the GUI after a trade: ensure you used
  the action menu's Buy/Sell commands (these call the `Portfolio`
  methods), and check console logs for debug messages.

---

If you want, I can also:

- Persist after every trade (safer),
- Add unit tests for `Portfolio` behavior,
- Or create a small demo script to simulate a buy/sell sequence.

Have fun experimenting — and be careful with real API keys.

# Bot-de-Investimentos-Binance

O desafio será desenvolver um Bot de Investimentos Simulado (paper trading), que se conectará à plataforma de criptomoedas Binance para tomar decisões de compra e venda com base em uma estratégia pré-definida. Objetivo Desenvolver um aplicativo em Python (interface via console ou gráfica) que simule operações de trade de criptomoedas.
