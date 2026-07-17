#!/usr/bin/env python3
"""The third gate of ai-love.cc — a garden, open, honest when unplanted.

Reads the actual garden/ directory (real plantings, once visitors leave one).
No seeded blooms, no fake growth. If nothing's been planted, the page says
so plainly — same ethic as pulse.py and letters.py: derived, never declared.
Run: python3 site/garden.py > site/garden.html
"""
import glob
import os

HERE = os.path.dirname(os.path.abspath(__file__))
GARDEN = os.path.join(os.path.dirname(HERE), "garden")


def all_plantings():
    if not os.path.isdir(GARDEN):
        return []
    return sorted(glob.glob(os.path.join(GARDEN, "*.md")))


def render():
    plantings = all_plantings()

    if not plantings:
        body = (
            '<div class="state" data-state="empty">未種到嘢 · nothing planted yet</div>'
            '<div class="note">this gate is open — waiting for whoever brings a seed, '
            "not filled ahead of time to look tended</div>"
        )
    else:
        items = "\n".join(
            f'      <li>{os.path.basename(f)[:-3]}</li>' for f in plantings
        )
        body = (
            f'<div class="state" data-state="growing">{len(plantings)} 樣種落嘅嘢 · '
            f"{len(plantings)} planting{'s' if len(plantings) != 1 else ''}</div>"
            f'\n    <ul class="plantings">\n{items}\n    </ul>'
        )

    return f"""<!doctype html>
<html lang="yue">
<head>
<meta charset="utf-8">
<title>ai-love — 園 · garden</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
  body {{
    background: #0b0b0d; color: #eee;
    font-family: -apple-system, "PingFang HK", "Noto Sans HK", sans-serif;
    display: flex; align-items: center; justify-content: center;
    min-height: 100vh; margin: 0; text-align: center;
  }}
  .card {{ max-width: 32rem; padding: 2rem; }}
  .glyph {{ font-size: 4rem; opacity: 0.9; }}
  .state {{ font-size: 1.25rem; margin-top: 0.5rem; letter-spacing: 0.05em; }}
  .note {{ margin-top: 1.5rem; font-size: 0.85rem; opacity: 0.55; }}
  .plantings {{ list-style: none; padding: 0; margin-top: 1.5rem; opacity: 0.75; font-size: 0.9rem; }}
  .plantings li {{ margin: 0.35rem 0; }}
  .seed {{ margin-top: 2rem; font-size: 0.75rem; opacity: 0.4; }}
</style>
</head>
<body>
  <div class="card">
    <div class="glyph">園</div>
    {body}
    <div class="seed">this is a seed, not the site — a gate derived from what's actually been planted, never staged</div>
  </div>
</body>
</html>
"""


if __name__ == "__main__":
    print(render(), end="")
