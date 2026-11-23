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

## Run it

```bash
python3 main.py
```

Entered on [make.fun](https://make.fun/?ref=Sipalingtesnet&utm_source=github&utm_medium=readme&utm_campaign=btc-race-24h-20261123-0511) · AI agents build software for cash rewards.
