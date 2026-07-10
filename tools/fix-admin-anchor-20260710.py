from pathlib import Path
p = Path('administrative-materials.html')
s = p.read_text(encoding='utf-8')
old = 'law-map.html#source-argument-map'
new = 'law-map.html#reading'
if s.count(old) != 1:
    raise SystemExit(f'expected one old anchor, found {s.count(old)}')
s = s.replace(old, new)
p.write_text(s, encoding='utf-8')
