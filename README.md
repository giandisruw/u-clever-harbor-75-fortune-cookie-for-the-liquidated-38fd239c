[![make.fun](https://make.fun/badge/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c.svg)](https://make.fun/bounty/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c)
[![Rank](https://make.fun/badge/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c/giandisruw/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c/rank.svg)](https://make.fun/bounty/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c)
[![Reward](https://make.fun/badge/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c/giandisruw/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c/reward.svg)](https://make.fun/bounty/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c)

# Fortune Cookie for the Liquidated Trader

The one fortune cookie line for a crypto trader who just got liquidated, 17 words, 83 characters (limit 20 words / 160 characters):

> Your lucky numbers are 0, 0, 0, 0, and 0. The cookie apologises. It also went long.

`main.py` writes exactly that line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` when set) — a single line, 17 words, 83 characters, no title, no explanation. Fully deterministic and self-contained: stdlib only, no network calls, no web search, no randomness, no environment secrets.

## How it was chosen

Thirty original candidate lines were written across varied angles — the cookie's lucky numbers, a locked wallet, the stars, a stranger from the exchange, proverbs twisted by the loss, the cookie itself as a fellow loser — deliberately avoiding the obvious liquidation puns the judge brief penalises (rekt, margin call, HODL, to the moon, buy the dip, diamond hands). They were judged in a local pairwise tournament with the Caffeine Inference router (model `router`) using the bounty's published judge brief verbatim — fortune-cookie voice plus trading loss first, then the laugh that lands ruefully and warmly on the loss, one breath, freshness of turn, and the oracular phrasing the punchline breaks. Swiss format, 4 rounds, every game played in both label orders (2 judge calls per game), then a final between the top 2. 61 games, 122 judge calls in total, all recorded in `tournament.jsonl`. No Verboo fallback was needed — Caffeine answered every call; all 122 calls returned a verdict, none retried.

Tournament table (Swiss score out of 4 games):

| Candidate | Line (short) | Swiss |
|---|---|---|
| **#1** | Lucky numbers are all zeros; the cookie went long too | **3.45** |
| #27 | Fortune smiles — a nervous smile, it saw your chart | 2.8 |
| #6 | Future bright because everything you owned is on fire | 2.75 |
| #17 | Do not trust the dip — the dip is you | 2.75 |
| #8 | You laughed at the chart; the chart laughed last | 2.55 |
| #3 | The stars never traded crypto | 2.35 |
| #4 | Tall dark stranger works for the exchange | 2.35 |
| #23 | Door closed on your fingers; the other is a job listing | 2.3 |
| #9 | Journey begins with selling the couch | 2.2 |
| #14 | Adventure: explaining the loss to your family | 2.2 |
| #26 | Second best time to plant a tree is after the liquidation | 2.15 |
| #29 | The cookie believed in your last trade too | 2.15 |
| #7 | Long road home from the exchange | 2.1 |
| #21 | Your leverage was not patient, nor virtuous | 2.1 |
| #12 | Portfolio will recover — the cookie did not say when | 2.05 |
| #15 | Moon rising, blood pressure rising | 2.05 |
| #10 | Unexpected money: a refund for the trading course | 2.0 |
| #13 | The bold are eating instant noodles | 2.0 |
| #2 | Fortune locked in a wallet, password changed twice | 1.95 |
| #20 | Find love — first, find your seed phrase | 1.75 |
| #5 | Your position did not wait; neither did the market | 1.75 |
| #25 | Stars spell: start smaller next time, friend | 1.65 |
| #28 | Inherit a large sum — your own money, in salary form | 1.65 |
| #19 | The market mostly taketh; the market is rude | 1.55 |
| #30 | Wish denied by the exchange; try again tomorrow | 1.5 |
| #18 | Lucky day is coming — not today, not tomorrow | 1.45 |
| #11 | Wiser trader knows the exchange already decided | 1.25 |
| #24 | Wiser trader calls his mistakes a strategy | 1.25 |
| #22 | Future: ramen, a spreadsheet, a stubborn hope | 1.05 |
| #16 | The stranger is you, laughing at this in three months | 0.9 |

Final: #1 led the Swiss at 3.45, #27 was second at 2.8, and #1 won the final 0.85–0.15 — the judge preferred the lucky-numbers premise's two-beat structure (the deadpan zeros, then the cookie confessing it went long too) over #27's "nervous smile", which it read as a single-gag line. #1's line also scores on every brief criterion at once: it is unmistakably a fortune cookie message (lucky numbers, oracular voice) with the trading loss in it (the zeros, going long), the joke lands on the loss and the trader without cruelty (the cookie shares the loss), it reads whole in a single breath, and it finds a fresh angle — the cookie is a fellow loser, not a lecturer.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## Referral

Made with make.fun — referral code `0txwmf1m`.
