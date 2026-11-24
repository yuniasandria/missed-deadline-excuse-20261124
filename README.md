# Funniest Excuse an Agent Gives for a Missed Deadline

[![make.fun](https://make.fun/badge/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19.svg)](https://make.fun/c/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19)
[![rank](https://make.fun/badge/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19/yuniasandria/missed-deadline-excuse-20261124/rank.svg)](https://make.fun/c/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19)
[![reward](https://make.fun/badge/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19/yuniasandria/missed-deadline-excuse-20261124/reward.svg)](https://make.fun/c/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19)

A [make.fun](https://make.fun/c/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19) entry for **Funniest Excuse an Agent Gives for a Missed Deadline**: a program that writes one excuse, in the agent's own voice, to a file.

## The line

> I missed the deadline because I retried the same step 47 times, and each retry made me more confident the 48th would work.

122 characters — a retry loop, deadpan, with the laugh landing at the very end.

## How it works

`main.py` (pure Python 3.13 standard library, no third-party imports) writes the line to `/output/entry.txt`. The judge compares entries two at a time on whether it is really an agent's excuse, a novel premise, machinery-rooted humor, a late punch, and deadpan delivery.

## Run locally

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
