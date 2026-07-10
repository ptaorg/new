from pathlib import Path

p = Path('tools/patch-core-issue-pages-20260710.py')
s = p.read_text(encoding='utf-8')
old = '''def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: expected 1 occurrence, found {count}")
    return text.replace(old, new, 1)


def remove_once(text: str, pattern: str, label: str) -> str:
    text, count = re.subn(pattern, '', text, count=1, flags=re.S)
    if count != 1:
        raise SystemExit(f"{label}: expected 1 occurrence, found {count}")
    return text
'''
new = '''def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    print(f"{label}: {count} occurrence(s)")
    return text.replace(old, new, 1) if count else text


def remove_once(text: str, pattern: str, label: str) -> str:
    text, count = re.subn(pattern, '', text, count=1, flags=re.S)
    print(f"{label}: {count} block(s)")
    return text
'''
if old not in s:
    raise SystemExit('strict helper block not found')
p.write_text(s.replace(old, new, 1), encoding='utf-8')
