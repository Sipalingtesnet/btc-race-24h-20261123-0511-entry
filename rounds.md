# Dip Rider — evaluation rounds

Harness: `python3 /home/hatch/workspace/makefun/btc-race-24h-20261123-0511-work/replay.py --bot "python3 -P -s /home/hatch/workspace/makefun/btc-race-24h-20261123-0511-entry/main.py" --window all`

Format per config: constants | dev net PnL | dev trades | w1/w2/w3/w4 net PnL | maxDD per window (dev,w1,w2,w3,w4)

## Round 1 — baseline
LOOKBACK=60 DIP_BPS=150 TP_BPS=150 SL_BPS=100 MAX_HOLD=90
dev: netPnL=-0.06 trades=2 maxDD=0.59%## Round 2
LOOKBACK=60 DIP_BPS=100 TP_BPS=150 SL_BPS=100 MAX_HOLD=90
dev: netPnL=+15.09 trades=4 maxDD=0.59%
w1: +11.15 w2: +0.00 w3: -18.24 w4: +2.01
maxDD: dev=0.59% w1=0.82% w2=0.00% w3=1.94% w4=0.39%## Round 3
LOOKBACK=60 DIP_BPS=100 TP_BPS=100 SL_BPS=80 MAX_HOLD=90
dev: netPnL=+12.33 trades=4 maxDD=0.59%
w1: +3.64 w2: +0.00 w3: -18.27 w4: +2.01
maxDD: dev=0.59% w1=0.82% w2=0.00% w3=1.96% w4=0.39%## Round 4
LOOKBACK=60 DIP_BPS=80 TP_BPS=100 SL_BPS=80 MAX_HOLD=90
dev: netPnL=+16.28 trades=11 maxDD=1.54%
w1: +3.64 w2: -9.07 w3: -15.69 w4: +1.96
maxDD: dev=1.54% w1=0.82% w2=1.93% w3=2.41% w4=0.99%
## Takeover verification (Round 2 finalized config)
LOOKBACK=60 DIP_BPS=100 TP_BPS=150 SL_BPS=100 MAX_HOLD=90
dev: netPnL=+$15.09 trades=4 maxDD=0.59%
w1: +$11.15 trades=3 maxDD=0.82%
w2: +$0.00 trades=0 maxDD=0.00%
w3: -$18.24 trades=4 maxDD=1.94%
w4: +$2.01 trades=1 maxDD=0.39%

Determinism check: two independent runs with `--log-orders` on `--window dev` produced byte-identical JSONL files (`cmp` exit code 0). No forbidden network or time modules imported.
