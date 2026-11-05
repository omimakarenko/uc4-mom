#!/usr/bin/env python3
"""Build the guide: UC4_EDITOR_GUIDE.md -> body HTML, put into index.html (drop-down panel) and UC4_EDITOR_GUIDE.html."""
import re, markdown, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
body = markdown.markdown((root / 'UC4_EDITOR_GUIDE.md').read_text(), extensions=['tables', 'fenced_code'])
idx = root / 'index.html'
s = idx.read_text()
s = re.sub(r'<!--GUIDE_START-->.*?<!--GUIDE_END-->', lambda m: '<!--GUIDE_START-->\n' + body + '\n<!--GUIDE_END-->', s, flags=re.S)
idx.write_text(s)
g = root / 'UC4_EDITOR_GUIDE.html'
h = g.read_text()
h = re.sub(r'<main>.*?</main>', lambda m: '<main>\n' + body + '\n</main>', h, flags=re.S)
g.write_text(h)
print('guide built')
