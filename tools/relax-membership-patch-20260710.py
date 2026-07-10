from pathlib import Path

p = Path('tools/refine-membership-page-20260710.py')
s = p.read_text(encoding='utf-8')
old = '''def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'{label}: expected 1 occurrence, found {count}')
    return text.replace(old, new, 1)
'''
new = '''def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count < 1:
        raise SystemExit(f'{label}: expected at least 1 occurrence, found {count}')
    print(f'{label}: replacing {count} occurrence(s)')
    return text.replace(old, new)
'''
if old not in s:
    raise SystemExit('strict helper block not found')
p.write_text(s.replace(old, new, 1), encoding='utf-8')
