from pathlib import Path

p = Path('audit/index.html')
s = p.read_text(encoding='utf-8')
s = s.replace('>運営チェックアプリ</a>', '>運営チェック</a>')
p.write_text(s, encoding='utf-8')

p = Path('audit/check-app.js')
s = p.read_text(encoding='utf-8')
old = "'個人情報提供記録', '学校名簿・クラス名簿の提供記録'"
new = "'個人情報利用・提供記録', '学校名簿・クラス名簿の利用・提供記録'"
if s.count(old) != 1:
    raise SystemExit(f'audit document labels: expected 1 occurrence, found {s.count(old)}')
s = s.replace(old, new, 1)
p.write_text(s, encoding='utf-8')
