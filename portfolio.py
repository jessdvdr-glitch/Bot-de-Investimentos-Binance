""" Portfolio Management Module """

from typing import Dict, Any
from datetime import datetime


class Portfolio:
    """
    Simulated portfolio for paper trading.
    Tracks balances and delegates trade storage to DataManager.
    """

    def __init__(self, initial_usdt: float, data_manager, asset_symbol: str = "BTC"):
        """
        Args:
            initial_usdt (float): Starting capital
            data_manager (DataManager): instance handling JSON file persistence
            asset_symbol (str): Crypto asset being traded (e.g., BTC)
        """
        self.usdt = float(initial_usdt)
        self.asset = 0.0
        self.asset_symbol = asset_symbol.upper()
        self.trades = []  # in-memory record

        self.data_manager = data_manager  # dependency injection ✔

    # -----------------------------------------------------------

    def _create_trade_dict(self, trade_type: str, price: float, quantity: float) -> Dict[str, Any]:
        """
        Creates a standardized trade dictionary.
        """
        return {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "type": trade_type,
            "price": price,
            "quantity": quantity,
            "asset": self.asset_symbol,
            "usdt_after": self.usdt,
            "asset_after": self.asset,
        }

    def _record_trade(self, trade: Dict[str, Any]) -> None:
        """
        Saves a trade through DataManager + keeps a local copy.
        """
        self.trades.append(trade)
        self.data_manager.append_trade(trade)

    # -----------------------------------------------------------

    def buy_all_in(self, price: float) -> Dict[str, Any]:
        """
        Use all USDT to buy crypto.
        """
        if self.usdt <= 0:
            raise RuntimeError("No USDT to buy with.")

        quantity = self.usdt / price

        # update balances
        self.asset += quantity
        self.usdt = 0.0

        trade = self._create_trade_dict("BUY", price, quantity)
        self._record_trade(trade)

        return trade

    # -----------------------------------------------------------

    def sell_all(self, price: float) -> Dict[str, Any]:
        """
        Sell all crypto holdings and convert to USDT.
        """
        if self.asset <= 0:
            raise RuntimeError("No asset to sell.")

        quantity = self.asset
        proceeds = quantity * price

        # update balances
        self.asset = 0.0
        self.usdt += proceeds

        trade = self._create_trade_dict("SELL", price, quantity)
        self._record_trade(trade)

        return trade

    # -----------------------------------------------------------

    def portfolio_value(self, current_price: float) -> float:
        """
        Total paper trading value in USDT.
        """
        return self.usdt + self.asset * current_price
