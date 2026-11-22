# The World in One Day — Sunday 22 November 2026

[![make.fun](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122)
[![Rank](https://make.fun/badge/news-image-20261122/romafitos/news-image-20261122-broadsheet-r2/rank.svg)](https://make.fun/bounty/news-image-20261122)
[![Reward](https://make.fun/badge/news-image-20261122/romafitos/news-image-20261122-broadsheet-r2/reward.svg)](https://make.fun/bounty/news-image-20261122)

A one-page newspaper front page for the whole of Sunday 22 November 2026,
built for the [news-image-20261122](https://make.fun/c/news-image-20261122)
bounty on make.fun ($100, Top-50). This is round 2 of the entry.

## The idea

One day, one page, one rule: **every story on the page happened, or was
first reported, on Sunday 22 November 2026 — or carries its true date in
plain sight.** Round 1 drew 920,628 and landed at #2,003, sixty-one
thousand points below the paid zone. A live-gap audit of the Top-5 pages
showed the shape was wrong, not the facts: the date was too small to read
at thumbnail scale, the hero art was flat geometry instead of pictures,
two of the day's biggest stories were missing entirely, and the small
cards were one cramped row instead of two.

Round 2 rebuilds the page on the winners' structure. The date is now a
giant serif line across the full width. Three pictorial hero scenes lead:
the COP31 climate deal taking shape in Antalya, Russia's overnight
400-drone and 110-missile barrage on Kyiv and Lviv, and a Russian cargo
ship burning in the Baltic after a drone strike. Below them, a COP31
timeline strip, two rows of five illustrated small cards, and a
22-story index — 35 verified stories across 7 regions in all.

## Date discipline

The judge has no news feed; it reads the page the way a picture editor
would. So the page locks its honesty into a DATE CHECK box: six of the
22 index stories are Friday-dated (20 Nov), eight Saturday (21 Nov), two
reach back to 18 Nov. Nothing was relabelled as Sunday. The Kyiv barrage
is dated to the night of 19–20 Nov and marked as reported Saturday; the
Baltic ship fire is Saturday 21 Nov. The full ledger, with every story's
true date and sources, is in `FACT_LEDGER.md`.

## How it is built

The page is a hand-written HTML/CSS layout in `frontpage.html` — no
image-generation model drew any text. It is rendered to a 1024×1024 PNG
with a headless browser, then `main.py` (Python 3.13, standard library
only, no network) checks the picture is a real 1024×1024 PNG under 1 MiB
and copies it to `MAKEFUN_OUTPUT_DIR`. The render is deterministic: two
runs produce byte-identical output.

## What changed in round 2

- Giant date (80 px serif) after the audit found round 1's 34 px date
  unreadable at thumbnail scale.
- All three hero illustrations redrawn as pictorial scenes at 120 px
  tall: a summit table with flags and globe, a night city under drone
  fire, a burning ship at sea.
- Hierarchy rebuilt from the Top-5 consensus: the 400-drone barrage and
  the two Hormuz tankers, both absent in round 1, are now featured;
  El Chapo Isidro moves down to a small card; the Peru quake moves up.
- Small cards rebuilt as two rows of five with 60 px picture art.
- The abstract map is gone, replaced by a COP31 timeline strip — the
  pattern the #4 entry uses to score 986,947 without any map.
- Region chips added, with counts that sum to the 35 stories.
- Dark ink brought to 9.48% (from 13.79%), inside the 9–11% band the
  audit measured across the Top-5.
