from pathlib import Path
import re


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'{label}: expected 1 occurrence, found {count}')
    return text.replace(old, new, 1)

p = Path('guide-research.html')
s = p.read_text(encoding='utf-8')
s = replace_once(s, '<h2>教育委員会回答の読み方</h2>', '<h2>教育委員会回答の確認事項</h2>', 'response heading')
s = replace_once(s, '<h2>学校・PTA文書の読み方</h2>', '<h2>学校・PTA文書の確認事項</h2>', 'school docs heading')
pattern = r'<section class="research-panel"><h2>取材・問い合わせ</h2>.*?</section>'
replacement = '<section class="research-panel"><h2>取材・資料提供</h2><p>資料の出所確認、照会文書、取材、共同調査については、<a href="contact.html">問い合わせ・情報提供窓口</a>へご連絡ください。</p></section>'
s, count = re.subn(pattern, replacement, s, count=1, flags=re.S)
if count != 1:
    raise SystemExit(f'contact section: expected 1, found {count}')
p.write_text(s, encoding='utf-8')

p = Path('key-materials.html')
s = p.read_text(encoding='utf-8')
s = replace_once(s, 'この5件は、結論を代替する資料ではありません。', 'これらの資料は、結論を代替するものではありません。', 'key materials residual count')
p.write_text(s, encoding='utf-8')

p = Path('timeline-issues.html')
s = p.read_text(encoding='utf-8')
s = replace_once(s, '社会教育関係団体としての自主性と、学校側の管理責任を分けることが中心です。', '任意団体としての自主性と、学校側の管理責任を分けることが中心です。', 'timeline hero qualification')
p.write_text(s, encoding='utf-8')
