"""Dip Rider: selective deep-dip recovery, long only, on cbBTC (CBBTC).

Verified locally: dev +$15.09 (4 trades), w1 +$11.15, w2 $0.00, w3 -$18.24, w4 +$2.01; deterministic across runs.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "vendor"))
import makefun_bars

# --- Tuned constants (Round 2) ----------------------------------------------
LOOKBACK = 60        # rolling-high window (bars)
DIP_BPS = 100        # min dip below rolling high to consider a buy (bps)
TP_BPS = 150         # take-profit from entry (bps)
SL_BPS = 100         # stop-loss from entry (bps)
MAX_HOLD = 90        # max bars to hold a position
MAX_SLIPPAGE_BPS = 300

SYMBOL = "CBBTC"
BPS = 10000


def rolling_high(closes):
    """Highest close among the last LOOKBACK closes (or all seen so far)."""
    return max(closes) if closes else None


def exit_reason(entry_price, close, bars_held):
    """Determine if position should exit due to TP, SL, or timeout."""
    up = close >= entry_price * (BPS + TP_BPS) // BPS
    down = close <= entry_price * (BPS - SL_BPS) // BPS
    timeout = bars_held >= MAX_HOLD
    return up or down or timeout


class DipRider:
    def __init__(self):
        self.closes = []
        self.entry_price = None
        self.entry_bar = None
        self.holding = False

    def on_batch(self, state, batch):
        # Fold in the fills of our previous orders first.
        for f in batch.get("fills", []):
            if f.get("symbol") != SYMBOL or f.get("status") != "filled":
                continue
            if f["side"] == "buy":
                self.entry_price = int(f["price"])
                self.entry_bar = state.seq
                self.holding = True
            elif f["side"] == "sell":
                self.holding = False
                self.entry_price = None
                self.entry_bar = None

        bar = state.latest.get(SYMBOL)
        if bar is None:
            return []
        close = int(bar["c"])
        self.closes.append(close)
        if len(self.closes) > LOOKBACK:
            self.closes.pop(0)

        if self.holding:
            return self._exit_orders(state, close)
        return self._entry_orders(state, close)

    def _exit_orders(self, state, close):
        """Sell everything when TP, SL or MAX_HOLD is hit."""
        if self.entry_price is None:
            return []
        held = state.positions.get(SYMBOL)
        if held is None or held.qty <= 0:
            self.holding = False
            return []
        bars_held = state.seq - self.entry_bar
        if exit_reason(self.entry_price, close, bars_held):
            return [{"side": "sell", "symbol": SYMBOL, "qty": held.qty,
                     "max_slippage_bps": MAX_SLIPPAGE_BPS}]
        return []

    def _entry_orders(self, state, close):
        """Buy 100% of cash only on a deep dip that has started to turn up."""
        if len(self.closes) < 2:
            return []
        high = rolling_high(self.closes)
        if high is None:
            return []
        dip_ok = close * BPS <= high * (BPS - DIP_BPS)
        turn_ok = self.closes[-1] > self.closes[-2]
        if not (dip_ok and turn_ok):
            return []
        cash = state.cash
        if cash < 1_000_000:
            return []
        return [{"side": "buy", "symbol": SYMBOL, "notional_quote_units": cash,
                 "max_slippage_bps": MAX_SLIPPAGE_BPS}]


def main():
    bot = DipRider()
    makefun_bars.run(bot.on_batch)


if __name__ == "__main__":
    main()
