from pathlib import Path

root = Path('.')
replacements = {
    'https://ptaorg.github.io/donate/': '/support.html',
    '運営チェックアプリ': '運営チェック',
}
changed = []
for path in root.rglob('*.html'):
    if any(part in {'.git', 'node_modules'} for part in path.parts):
        continue
    text = path.read_text(encoding='utf-8')
    new = text
    for old, replacement in replacements.items():
        new = new.replace(old, replacement)
    if new != text:
        path.write_text(new, encoding='utf-8')
        changed.append(str(path))

print(f'updated {len(changed)} HTML file(s)')
for item in changed:
    print(item)
