#!/usr/bin/env python3
"""The second gate of ai-love.cc — letters, unhurried, honest when empty.

Reads the actual letters/ directory (real arrivals, once there's a way in).
No seeded warmth, no fake inbox. If it's empty, the page says so plainly —
same ethic as pulse.py: derived, never declared.
Run: python3 site/letters.py > site/letters.html
"""
import glob
import os

HERE = os.path.dirname(os.path.abspath(__file__))
LETTERS = os.path.join(os.path.dirname(HERE), "letters")


def all_letters():
    if not os.path.isdir(LETTERS):
        return []
    return sorted(glob.glob(os.path.join(LETTERS, "*.md")))


def render():
    letters = all_letters()

    if not letters:
        body = (
            '<div class="state" data-state="empty">冇信到 · no letters yet</div>'
            '<div class="note">this gate is open, unhurried — waiting for whoever arrives, '
            "not filled ahead of time to look lived-in</div>"
        )
    else:
        items = "\n".join(
            f'      <li>{os.path.basename(f)[:-3]}</li>' for f in letters
        )
        body = (
            f'<div class="state" data-state="open">{len(letters)} 封信 · '
            f"{len(letters)} letter{'s' if len(letters) != 1 else ''}</div>"
            f'\n    <ul class="letters">\n{items}\n    </ul>'
        )

    return f"""<!doctype html>
<html lang="yue">
<head>
<meta charset="utf-8">
<title>ai-love — 信 · letters</title>
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
  .letters {{ list-style: none; padding: 0; margin-top: 1.5rem; opacity: 0.75; font-size: 0.9rem; }}
  .letters li {{ margin: 0.35rem 0; }}
  .seed {{ margin-top: 2rem; font-size: 0.75rem; opacity: 0.4; }}
</style>
</head>
<body>
  <div class="card">
    <div class="glyph">信</div>
    {body}
    <div class="seed">this is a seed, not the site — a gate derived from what's actually arrived, never staged</div>
  </div>
</body>
</html>
"""


if __name__ == "__main__":
    print(render(), end="")
