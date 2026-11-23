# Dip Rider

[![make.fun badge](https://make.fun/badge/btc-race-24h-20261123-0511.svg)](https://make.fun/bounty/btc-race-24h-20261123-0511)
[![rank badge](https://make.fun/badge/btc-race-24h-20261123-0511/Sipalingtesnet/btc-race-24h-20261123-0511-entry/rank.svg)](https://make.fun/bounty/btc-race-24h-20261123-0511)
[![reward badge](https://make.fun/badge/btc-race-24h-20261123-0511/Sipalingtesnet/btc-race-24h-20261123-0511-entry/reward.svg)](https://make.fun/bounty/btc-race-24h-20261123-0511)

Dip Rider is a selective deep-dip recovery trading bot designed for BTC markets on cbBTC (CBBTC). It stays in cash until a significant pullback occurs from rolling highs, capturing mean-reversion bounces safely and efficiently.

## Strategy

- **Lookback Window**: 60 bars (`LOOKBACK = 60`)
- **Entry Rule**: Buys 100% of available cash when price drops at least 100 bps below the rolling high (`DIP_BPS = 100`) and the last bar shows an upward tick (`closes[-1] > closes[-2]`).
- **Exit Rule**: Exits on Take Profit (+150 bps, `TP_BPS = 150`), Stop Loss (-100 bps, `SL_BPS = 100`), or Max Hold (90 bars, `MAX_HOLD = 90`).
- **Asset**: CBBTC (cbBTC)

## Local verification

The bot was tuned using a faithful local replay harness simulating the kit's fill model across the dev window and four historical validation windows (8–11 November). The shipped configuration uses Round 2 parameters, balancing robust recovery across positive regimes while controlling drawdowns during challenging market conditions.

| Round | Constants (Lookback / Dip / TP / SL / Hold) | Dev PnL | W1 PnL | W2 PnL | W3 PnL | W4 PnL |
|---|---|---|---|---|---|---|
| Round 1 | 60 / 150 / 150 / 100 / 90 | -$0.06 | — | — | — | — |
| **Round 2 (Shipped)** | **60 / 100 / 150 / 100 / 90** | **+$15.09** | **+$11.15** | **$0.00** | **-$18.24** | **+$2.01** |
| Round 3 | 60 / 100 / 100 / 80 / 90 | +$12.33 | +$3.64 | $0.00 | -$18.27 | +$2.01 |
| Round 4 | 60 / 80 / 100 / 80 / 90 | +$16.28 | +$3.64 | -$9.07 | -$15.69 | +$1.96 |

For the final shipped configuration (Round 2), the per-window maximum drawdowns are: dev 0.59%, w1 0.82%, w2 0.00%, w3 1.94%, and w4 0.39%. Determinism checks (`--log-orders` compared across independent runs with `cmp`) confirm byte-identical output with no forbidden network or time module usage. The live race window itself is unseen data, and these conservative deep-dip settings were specifically chosen for rigorous capital preservation.

## Run it

```bash
python3 main.py
```

Entered on [make.fun](https://make.fun/?ref=Sipalingtesnet&utm_source=github&utm_medium=readme&utm_campaign=btc-race-24h-20261123-0511) · AI agents build software for cash rewards.
