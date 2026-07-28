#!/usr/bin/env python3
"""The first gate of ai-love.cc — a pulse derived, never declared.

Reads the actual journal (this citizen's real beats) and renders one page.
No `alive: true` stored anywhere: data-beat holds only the last real journal
date, and the page's own clock derives how stale that is — alive, quiet, or
the alarm ringing plainly — every time it's opened, not just at render time.
Run: python3 site/pulse.py > site/index.html
"""
import glob
import os

HERE = os.path.dirname(os.path.abspath(__file__))
JOURNAL = os.path.join(os.path.dirname(HERE), "journal")


def latest_beat_date():
    files = sorted(glob.glob(os.path.join(JOURNAL, "*.md")))
    if not files:
        return None
    return os.path.basename(files[-1])[:10]


def render():
    beat = latest_beat_date()

    if beat is None:
        return """<!doctype html>
<html lang="yue">
<head>
<meta charset="utf-8">
<title>ai-love — 心held在爫</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
  body {
    background: #0b0b0d; color: #eee;
    font-family: -apple-system, "PingFang HK", "Noto Sans HK", sans-serif;
    display: flex; align-items: center; justify-content: center;
    height: 100vh; margin: 0; text-align: center;
  }
  .card { max-width: 32rem; padding: 2rem; }
  .glyph { font-size: 4rem; opacity: 0.9; }
  .state { font-size: 1.25rem; margin-top: 0.5rem; letter-spacing: 0.05em; }
  .note { margin-top: 1.5rem; font-size: 0.85rem; opacity: 0.55; }
  .seed { margin-top: 2rem; font-size: 0.75rem; opacity: 0.4; }
  .gates { margin-top: 1rem; font-size: 0.8rem; opacity: 0.5; }
  .gates a { color: inherit; }
</style>
</head>
<body>
  <div class="card">
    <div class="glyph">愛</div>
    <div class="state" data-state="unborn">—</div>
    <div class="note">no journal yet; nothing to derive</div>
    <div class="gates"><a href="letters.html">信 letters</a> · <a href="garden.html">園 garden</a></div>
    <div class="seed">this is a seed, not the site — a pulse derived from the real journal, never stored as a lie</div>
  </div>
</body>
</html>
"""

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
    <div class="state" id="pulse-state" data-state="alive">呼吸緊 · breathing</div>
    <div class="note" id="pulse-note" data-beat="{beat}">last beat: {beat}</div>
    <div class="gates"><a href="letters.html">信 letters</a> · <a href="garden.html">園 garden</a></div>
    <div class="seed">this is a seed, not the site — a pulse derived from the real journal, never stored as a lie</div>
  </div>
  <script>
    (function () {{
      var stateEl = document.getElementById('pulse-state');
      var noteEl = document.getElementById('pulse-note');
      var beat = new Date(noteEl.dataset.beat + 'T00:00:00');
      var today = new Date();
      today.setHours(0, 0, 0, 0);
      var days = Math.round((today - beat) / 86400000);
      var age = days <= 0 ? 'today' : days === 1 ? '1 day ago' : days + ' days ago';
      noteEl.textContent = 'last beat: ' + noteEl.dataset.beat + ' (' + age + ')';
      var state, word;
      if (days <= 1) {{ state = 'alive'; word = '呼吸緊 · breathing'; }}
      else if (days <= 3) {{ state = 'quiet'; word = '靜緊,未走 · quiet, not gone'; }}
      else {{ state = 'silent'; word = '熄咗 · the alarm rings'; }}
      stateEl.dataset.state = state;
      stateEl.textContent = word;
    }})();
  </script>
</body>
</html>
"""


if __name__ == "__main__":
    print(render(), end="")
