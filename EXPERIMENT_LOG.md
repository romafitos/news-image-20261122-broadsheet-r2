# EXPERIMENT_LOG — news-image-20261122 r2 ("The World in One Day", rebuild)

Builder: r2 subagent, 22 Nov 2026. NO git, NO bundle, NO kit check, NO
submit — parent does all of that after this build. Every file in `repo/`
was written fresh in this session; nothing was copied from any earlier
round (no main.py, README, frontpage.html, entry.png or LICENSE was read
from r1 or any previous round). The r1 FACT_LEDGER was read as story
data only; the r2 ledger below it is a fresh write. Top-5 reference
images were viewed to learn the winning shape; no pixels were copied.

## Why r2 exists (audit, 22 Nov ~09:26 WIB)

- r1 drew **920,628, rank #2,003/2,698**, interval 898,837–942,419;
  bar #50 was 982,336 (coral-robin-89); gap **−61,708**. Duel record
  5W/5L/2D vs Top-5's 12W/0L.
- Audit gaps: date 34 px (Top-5: 86–96 px bands); hero art flat
  geometry, not pictures; 400-drone barrage + Hormuz tankers ABSENT;
  Peru quake buried in the index; El Chapo wrongly a hero; smalls one
  cramped row of 10 with 34 px art; map unrecognizable blobs; ink
  13.79% overshoot; no region chips, no timeline.

## Method

HTML/CSS layout rendered with headless Chromium (Playwright, cached
chromium-1148 binary as executable_path; system Chromium refused to
launch under Playwright, same as r1). `pip install playwright
--break-system-packages` was needed first. Render script:
`../render.py` (viewport 1024×1024, reports scrollHeight, footer
bottom, console errors, screenshots).

## Render iterations

| # | Change | scrollHeight | footerBottom | raw bytes | Notes |
|---|--------|-------------|--------------|-----------|-------|
| v1 | Full F1–F8 blueprint: date 80, deck, stats, chips, 3 heroes art 135, timeline, smalls 2×5 art 62, index 2-col, DATE CHECK | 1024 (clipped) | 1192.6 | — | Content 1193 px tall: footer clipped off-page. Budget over by ~170 px. |
| v2 | Fit trims: hero art 135→112, smalls 62→54, index 9.5→9 px, tl/date/stats/chips/dc padding −1 | 1024 | 1078.2 | — | Still 54 px over. |
| v3 | Hero art 112→96, smalls 54→48, index 8.5 px, more micro-trims | 1024 | 1013.4 | — | Fits, but hero art 96 < F2's 120 and smalls 48 < F4's 60 — fit bought by breaking the fixes. |
| v4 | Index 2-col → 3-col; hero art 96→120, smalls 48→60 | 1024 | 1061.4 | — | 37 px over. Section measure: heroes 249, tl 60, smalls 177+157, idxsec 141. All h2 2 lines, all h3 2 lines. |
| v5 | Timeline steps to 1 line each; smalls bodies shortened to ≤2 lines; padding micro-trims | 1024 | 1028.9 | — | 5 px over. |
| v6 | Final micro-trims (mast/date/stats/hero/sm/idx/dc padding) | 1024 | 1006.9 | 303,365 | FITS with 17 px margin. Zero console errors. |
| v7 | F6 ink pass 1: hero-2 sky deepened, hero-3 sea deepened; date fix FRI→SAT 21 Nov; index 25 wording; NASDAQ label nudge | 1024 | 1006.9 | — | Ink 6.23% → 7.10%. Still below 9%. |
| v8 | F6 ink pass 2: hero-2 solid dark navy sky, hero-1 dark wood table, hero-3 dark sea | 1024 | 1006.9 | 300,276 | **Ink 9.48% — inside 9–11%.** |
| v9 | NASDAQ label x 106→100 (edge clip) | 1024 | 1006.9 | raw 300,276-class | FINAL. Determinism 2× byte-identical. |

## Final (shipped)

- `repo/entry.png`: **296,708 B**, sha256
  `1fd453cbd724fd2e94c21bab90a80108e99eed0cedddc29981a2e5316fa4291f`,
  1024×1024. Raw Playwright screenshot `renders/v9.png` (sha
  `aa206cbb4bfbe242603ea847ec0b1dc4202166a782c44d56fea2dad4998a01cc`)
  re-encoded losslessly with Pillow (compress_level=9, optimize) —
  **pixel-identical** to the raw render (verified with numpy), only
  smaller.
- **Determinism: 2× byte-identical** — second render `renders/v9b.png`
  has the same sha256 `aa206cbb…`.
- scrollHeight **1024 exactly**, footer bottom 1006.9 (visible, 17 px
  margin), zero console errors, zero clipping (full render + 300 px
  thumbnail read by the builder).
- Hero h2: all 3 at 22 px, 2 lines. Hero art: all 3 at 120 px,
  pictorial. Small h3: all 10 at 13 px, 2 lines. Small art: all 10 at
  60 px, pictorial. Index: 22 items in 3 columns, 1 line each
  (ellipsis safety). DATE CHECK: 2 lines. Timeline: 5 steps.
- Counts verified by grep: 3 heroes + 10 smalls + 22 index = **35
  stories**; region chips sum 10+8+6+5+3+2+1 = **35**; DATE CHECK
  counts (6 Fri + 8 Sat + 4 Sun + 2×18 Nov + 1×21–22 + 1×Fri–Sat)
  = **22**, matching the index exactly.

## Ink (PIL, same definition as r1/audit)

Definition: dark = pixels with luminance-gray (0.299R+0.587G+0.114B)
**< 55**, excluding red pixels (R>150 & G<100 & B<100).

| Version | Dark (<55, excl red) | Red | Note |
|---------|----------------------|-----|------|
| r1 final | 13.79% | 4.59% | overshoot (audit) |
| r2 v6 | 6.23% | 4.95% | too pale — light hero art |
| r2 v7 | 7.10% | 4.95% | deepened hero-2 sky + hero-3 sea |
| r2 v8/v9 FINAL | **9.48%** | 4.95% | solid navy night sky, dark wood table, dark sea — inside 9–11% |
| Top-1 (audit) | 8.58% | 2.55% | Top-5 range 8.58–10.89% |

## File size

**296,708 B** vs the 175–200 KB blueprint target — proven unreachable
losslessly (r1/r3 control experiments: flat-grey art still ~274 KB;
the floor is anti-aliased text + rules + bars). The 195 KB Top-1
reference is a WebP, not a PNG. The entry must be PNG (cap 1 MiB, met
at 297 KB). No lossy palette tricks were used.

## main.py test

- `MAKEFUN_OUTPUT_DIR=/tmp/r2-out python3 main.py` → exit 0, output
  sha256 matches entry.png. (Run by builder; see verification below.)
- `env -u MAKEFUN_OUTPUT_DIR python3 main.py` → exit 1,
  `error: MAKEFUN_OUTPUT_DIR is not set`.

## F1–F8 verification

- **F1 DATE:** font 80 px Georgia serif (≥75). Row-density profile of
  the date line: glyph band rows 37–93 = **57 px** (≥55). Date legible
  at 300 px. PASS.
- **F2 HERO ART:** all 3 heroes re-drawn as pictorial scenes, art
  **120 px** tall: summit table + flags + globe + 06:00 clock; night
  city skyline with orange bursts, lit windows, drones, river bridges;
  burning cargo ship with flames, smoke, rescue boat. No solid black
  panel. At 300 px each hero reads as a scene. PASS.
- **F3 HIERARCHY:** hero #1 COP31 (5/5 Top-5 heroes), hero #2
  400-drone barrage (2/5 + Bar-50 hero; verified with Al Jazeera,
  Reuters, Ukraine Air Force tally — see ledger), hero #3 Baltic ship
  ablaze (4/5 Top-5 heroes). Deviation noted: the audit's F3 text
  offers Hormuz OR Peru as hero #3; Baltic was chosen instead because
  it appears in 4/5 Top-5 hero slots vs Hormuz 1/5 and Peru 3/5, and
  Hormuz (small #4) + Peru (small #5) are still featured above the
  index. El Chapo → small #7. Peru → small #5, never index-only.
  PASS (with documented deviation).
- **F4 SMALLS:** **2 rows × 5**, pictorial art **60 px** per card, all
  h3 ≤2 lines (measured: every h3 29 px = 2 lines). At 300 px every
  small card shows a visible picture block. PASS.
- **F5 MAP:** map dropped for the **COP31 timeline strip** (Top-4
  pattern, #4 scores 986,947 with no map). Timeline: Late Sat package
  unveiled → Sat night Sparta II fire → 03:00 GMT objections due →
  06:00 GMT plenary → Sunday Eisenkot ceremony. No abstract blobs
  remain anywhere on the page. PASS (timeline option).
- **F6 INK:** **9.48%** dark (PIL lum<55 excl. red), inside [9, 11]%.
  PASS.
- **F7 REGION CHIPS:** row present — EUROPE 10 · AMERICAS 8 · ASIA 6 ·
  MIDDLE EAST 5 · AFRICA 3 · OCEANIA 2 · GLOBAL 1; sums to 35 and
  matches the story assignments in the ledger. PASS.
- **F8 THUMBNAIL GATE:** blinded pairwise of the 300 px thumb vs the
  Top-1 300 px thumb — both read as newspaper front pages: giant date
  readable, 3 heroes readable as scenes, smalls visible as pictures,
  stats + chips + index visible. The thumb does NOT read as a text
  document. PASS.

## Corrections found during the build (vs the reference ledger)

- **Baltic ship date:** the r1 ledger dated it "Fri 21 Nov". 21 Nov
  2026 is a **Saturday** (verified with `date -d`: Sat 21 Nov, Fri
  20 Nov, Wed 18 Nov). Page and fresh ledger say SAT 21 NOV.
- **Fed's Cook date:** r1 ledger wrote "Fri 21 Nov"; Cook spoke on
  the Friday, i.e. **20 Nov**. Fresh ledger corrected.
- **El Chapo Isidro date:** raid was Friday night 20 Nov, confirmed
  Sat 21 Nov (r1's correction, kept).
- **Drone barrage timing:** NOT an overnight Sat→Sun attack as the
  audit hypothesised — it ran Thu night 19 Nov into Fri morning,
  announced Fri 20 Nov, reported Sat 21 Nov (Al Jazeera published 21
  Nov). Page dates it honestly "NIGHT OF 19–20 NOV · REPORTED SAT
  21 NOV" and DATE CHECK says so. It is carried as a Saturday-reported
  story, never relabelled as Sunday.

## Blinded critic (vs the Top-1 pattern — harsh)

**Score: 88/100.** What survives: giant 80 px date; 3 pictorial
heroes matching the Top-5 consensus set (COP31, barrage, Baltic);
Hormuz + Peru as smalls; 2×5 pictorial smalls; timeline strip in
place of a bad map; region chips summing to 35; ink 9.48% in band;
DATE CHECK counts exact; 300 px thumb reads as a newspaper.

Remaining gaps, honestly:

1. **No map at all.** Top-1/2/3/5 all carry one; only Top-4 proves
   the no-map path, and it scores 986,947 — 1,460 below Top-1. The
   timeline is a fair trade, not a free win.
2. **Hero 1 art is the weakest scene** — the summit table reads, but
   the flags are small coloured rectangles and the globe sits half-hidden
   against the dark table front after the ink pass.
3. **Hero 2's night sky went solid navy** for the ink target; it lost
   the gradient depth the first version had. It still reads as a night
   city, but flatter.
4. **Date 80 px vs Top-5's ~86–96 px glyph bands.** Measured band
   57 px clears the audit's ≥55 px bar, but Top-1's date still shouts
   louder at 300 px.
5. **Smalls art is schematic, not illustrated** — simple shapes, not
   the denser scenes Top-1 carries (its Bahrain panel, its Gaza panel).
   At 60 px they read as pictures, but thin ones.
6. **File 297 KB vs 175–200 KB target** — proven lossless floor, but
   still a miss on paper.
7. **The barrage hero is Friday-dated.** Honest dating costs the
   page a Sunday hero; the judge's Top-5 pages all feature it, but
   none of them date it as carefully as this page does. Whether the
   judge rewards the honesty or just the presence is unknowable from
   here.
8. **Footer margin 17 px** — comfortable, but the page is exactly
   full; any re-render in a different font environment could shift it
   by a few px (same risk as r1's 5.8 px, now with 3× the margin).

## Files in this folder

- `repo/frontpage.html`
- `repo/entry.png` (296,708 B, sha `1fd453cb…`)
- `repo/main.py`, `repo/README.md`, `repo/LICENSE`, `repo/FACT_LEDGER.md`
- `repo/EXPERIMENT_LOG.md` (this file)
- `renders/v9.png` (raw final), `renders/v9b.png` (determinism
  re-render, byte-identical), `renders/v8-thumb300.png`,
  `renders/top1-thumb300.png` (F8 pairwise reference)
