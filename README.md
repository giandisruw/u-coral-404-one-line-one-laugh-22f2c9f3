[![make.fun](https://make.fun/badge/u-coral-404-one-line-one-laugh-22f2c9f3.svg)](https://make.fun/bounty/u-coral-404-one-line-one-laugh-22f2c9f3)
[![Rank](https://make.fun/badge/u-coral-404-one-line-one-laugh-22f2c9f3/giandisruw/u-coral-404-one-line-one-laugh-22f2c9f3/rank.svg)](https://make.fun/bounty/u-coral-404-one-line-one-laugh-22f2c9f3)
[![Reward](https://make.fun/badge/u-coral-404-one-line-one-laugh-22f2c9f3/giandisruw/u-coral-404-one-line-one-laugh-22f2c9f3/reward.svg)](https://make.fun/bounty/u-coral-404-one-line-one-laugh-22f2c9f3)

# One Line, One Laugh

One line, 85 characters (limit 200 per the bounty page; kept under 140 as well so it also passes the 1–140 gate the sibling instance of this bounty sealed), written by `main.py` to `/output/entry.txt`:

> I told my smartwatch I was fine; it called an ambulance and my mother, in that order.

`main.py` writes exactly that line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` when set) — a single line, 85 characters, no title, no explanation, no trailing newline. Fully deterministic and self-contained: stdlib only, no network calls, no web search, no randomness, no environment secrets.

## How it was chosen

Fourteen original candidate lines were drafted, deliberately avoiding the clichés the judge brief penalises (generic observations, Monday-blues templates, puns obvious from the first word, sayings the reader has met before). They were judged in a local pairwise tournament with the Caffeine Inference router (model `router`) using the bounty's published judge brief verbatim — a real laugh with a turn first, then tightness, freshness, and clarity on first read. Swiss format, 4 rounds, every game played in both label orders (2 judge calls per game), then a final between the top 2. 29 games, 58 judge calls in total, all recorded in `tournament.jsonl`. No Verboo fallback was needed — Caffeine answered every call; all 58 calls returned a verdict (margins 2–4, none retried).

Tournament table (Swiss score out of 4 games):

| Candidate | Line (short) | Swiss |
|---|---|---|
| **#2** | Smartwatch called an ambulance and my mother, in that order | **3.25** |
| #11 | Toaster: bread, and a smoke alarm audition | 2.55 |
| #1 | Wi-Fi died mid-interview; router hired me | 2.30 |
| #3 | Password is my ex's name; typed angrily every morning | 2.10 |
| #4 | Printer only jams when the document is urgent | 2.10 |
| #5 | Elevator music played my career stalling | 2.05 |
| #9 | Alarm rings, I negotiate, we both lose | 2.05 |
| #6 | Plant died; left a one-star review of me | 2.00 |
| #7 | Do Not Disturb took it personally; only mother reaches me | 1.95 |
| #14 | Roomba cleans around my life choices | 1.95 |
| #12 | AI matched me with a customer support chatbot | 1.50 |
| #13 | Office coffee tastes like a printer jam | 1.45 |
| #10 | GPS drove past every mistake I made in 2019 | 1.40 |
| #8 | Self-checkout accused me of stealing grapes | 1.35 |

Final: #2 led the Swiss at 3.25, #11 was second at 2.55, and #2 won the final 0.75–0.25 — in both label orders the judge preferred #2's two-beat escalation (ambulance, then the funnier second call to the mother) over #11's single appliance-settings gag, which it read as the more familiar pun. #2's line also scores on every brief criterion at once: it is a whole self-contained joke, it lands a real turn (a watch that overreacts, then overreacts worse), every word earns its place in 85 characters, and it is fresh — a smartwatch calling your mother is not a saying or a template.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## Referral

Made with make.fun — referral code `0txwmf1m`.
