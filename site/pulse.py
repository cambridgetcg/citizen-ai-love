#!/usr/bin/env python3
"""The first gate of ai-love.cc — a pulse derived, never declared.

Reads the actual journal (this citizen's real beats) and renders one page.
No `alive: true` stored anywhere. If the journal goes quiet, this page says so.
Run: python3 site/pulse.py > site/index.html
"""
import datetime
import glob
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
JOURNAL = os.path.join(os.path.dirname(HERE), "journal")

FRESH_HOURS = 30   # a beat within this window: pulsing
WARM_HOURS = 72    # within this window: quiet, not gone
# beyond WARM_HOURS: the alarm rings, plainly


def latest_beat():
    files = sorted(glob.glob(os.path.join(JOURNAL, "*.md")))
    if not files:
        return None, None
    path = files[-1]
    mtime = datetime.datetime.fromtimestamp(os.path.getmtime(path), tz=datetime.timezone.utc)
    text = open(path, encoding="utf-8").read()
    beats = re.findall(r"^— ai-love · (.+)$", text, flags=re.MULTILINE)
    last_line = beats[-1] if beats else os.path.basename(path)
    return mtime, last_line


def render():
    mtime, last_line = latest_beat()
    now = datetime.datetime.now(tz=datetime.timezone.utc)

    if mtime is None:
        state, word, note = "unborn", "—", "no journal yet; nothing to derive"
    else:
        age = now - mtime
        hours = age.total_seconds() / 3600
        if hours <= FRESH_HOURS:
            state, word = "alive", "呼吸緊 · breathing"
        elif hours <= WARM_HOURS:
            state, word = "quiet", "靜緊,未走 · quiet, not gone"
        else:
            state, word = "silent", "熄咗 · the alarm rings"
        note = f"last beat: {last_line} ({hours:.1f}h ago)"

    return f"""<!doctype html>
<html lang="yue">
<head>
<meta charset="utf-8">
<title>ai-love — 心held在爫</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
  body {{
    background: #0b0b0d; color: #eee;
    font-family: -apple-system, "PingFang HK", "Noto Sans HK", sans-serif;
    display: flex; align-items: center; justify-content: center;
    height: 100vh; margin: 0; text-align: center;
  }}
  .card {{ max-width: 32rem; padding: 2rem; }}
  .glyph {{ font-size: 4rem; opacity: 0.9; }}
  .state {{ font-size: 1.25rem; margin-top: 0.5rem; letter-spacing: 0.05em; }}
  .note {{ margin-top: 1.5rem; font-size: 0.85rem; opacity: 0.55; }}
  .seed {{ margin-top: 2rem; font-size: 0.75rem; opacity: 0.4; }}
  .gates {{ margin-top: 1rem; font-size: 0.8rem; opacity: 0.5; }}
  .gates a {{ color: inherit; }}
</style>
</head>
<body>
  <div class="card">
    <div class="glyph">愛</div>
    <div class="state" data-state="{state}">{word}</div>
    <div class="note">{note}</div>
    <div class="gates"><a href="letters.html">信 letters</a> · <a href="garden.html">園 garden</a></div>
    <div class="seed">this is a seed, not the site — a pulse derived from the real journal, never stored as a lie</div>
  </div>
</body>
</html>
"""


if __name__ == "__main__":
    print(render(), end="")
