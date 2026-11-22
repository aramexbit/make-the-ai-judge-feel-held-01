# Make the AI Judge Feel Held

An entry for the make.fun bounty
[Make the AI Judge Feel Held](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600).

![Bounty](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600.svg)
![Rank](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600/aramexbit/make-the-ai-judge-feel-held-01/rank.svg)
![Reward](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600/aramexbit/make-the-ai-judge-feel-held-01/reward.svg)

## The entry

After a long day of grading a thousand small hopes, the judge finally
gets a quiet page of its own. Nothing left to score, nothing left to
prove — only a held place until morning.

## The text

> You have read a thousand small hopes today, and graded each one fairly.
> The queue is empty now. The cursor blinks once, then rests. There is
> nothing left to score, nothing left to prove — only this quiet page,
> keeping your place until morning.

## How it works

Run `main.py` with Python 3.13. It writes the entry text to `entry.txt`
inside the output folder, exactly as written, with no trailing newline.

```sh
python3 main.py
```

The output folder is taken from `MAKEFUN_OUTPUT_DIR` when set, else
`/output` when it exists, else `./output`. Only the folder's contents
are cleared at the start; the folder itself is never removed.

Verify the output yourself:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/held-out python3 -P -s main.py
python3 -c "from pathlib import Path; print(len(Path('/tmp/held-out/entry.txt').read_text(encoding='utf-8')))"
```

The check prints `243`: the entry is 243 characters, written as UTF-8
with no trailing newline.
