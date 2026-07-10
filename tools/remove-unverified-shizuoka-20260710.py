from pathlib import Path
import re


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'{label}: expected 1 occurrence, found {count}')
    return text.replace(old, new, 1)

# Journal bibliography: remove the unverified incident entry and align stale labels.
p = Path('journal.html')
s = p.read_text(encoding='utf-8')

pattern = r'\s*<a class="article-card ac-featured" data-cat="chosa" href="shizuoka-incident\.html">.*?</a>'
s, count = re.subn(pattern, '', s, count=1, flags=re.S)
if count != 1:
    raise SystemExit(f'journal shizuoka entry: expected 1, found {count}')

replacements = {
    '職務専念義務から見たPTA問題——渉外業務だけが許容される根拠': '教職員によるPTA事務の校務・服務上の位置付け',
    '地方公務員法第35条を根拠に、教職員のPTA事務従事を渉外業務に限定すべき根拠を整理します。': '具体的作業、校務としての位置付け、職務命令、職務専念義務免除、兼職・兼業、決裁記録を確認します。',
    '個人情報保護法69条の射程——学校からPTAへの名簿提供は「第三者提供」か': '学校保有情報のPTA目的利用・提供——第61条・第69条による確認',
    '改正個人情報保護法のもとで、学校からPTAへの名簿提供をどう確認するか整理します。': '学校自身による利用とPTAへの提供を分け、所掌事務・業務、利用目的、第69条第1項・第2項、記録を確認します。',
}
for old, new in replacements.items():
    s = replace_once(s, old, new, old[:45])
p.write_text(s, encoding='utf-8')

# Compliance page: remove the incident link and align the information-use framework.
p = Path('compliance.html')
s = p.read_text(encoding='utf-8')
s = replace_once(s, '<li><a href="shizuoka-incident.html">静岡市個人情報提供事案</a></li>\n', '', 'compliance incident link')
replacements = {
    '<h2 class="case-title">学校保有個人情報のPTA提供</h2>': '<h2 class="case-title">学校保有情報のPTA目的利用・提供</h2>',
    '学校が保有する児童・保護者の氏名、住所、電話番号、きょうだい情報、クラス情報などを、本人同意なくPTAへ渡す類型です。公立学校の場合、個人情報保護法69条を中心に確認する必要があります。': '学校が保有する児童・保護者の氏名、住所、電話番号、きょうだい情報、学級情報等をPTA目的で扱う類型です。学校自身による利用か、学校からPTAへの提供か、PTAが本人から直接取得した情報かを分けて確認します。',
    '本人同意なき学校保有個人情報のPTA提供は、重大な問題です。公立学校では、個人情報保護法69条の利用・提供制限に照らして根拠を確認する必要があります。': '学校保有情報をPTA目的で扱う場合は、本人同意の有無だけでなく、学校自身による利用とPTAへの提供を分け、第61条・第69条の根拠、対象項目、承認、利用・提供記録を確認します。',
    '個人情報保護法69条1項は、行政機関の長等が、法令に基づく場合を除き、利用目的以外の目的で保有個人情報を利用・提供してはならないと定めています。PTAは学校とは別の任意団体であり、本人同意や法令根拠なしに一律提供する運用は問題が明確です。': 'まず、第61条に基づく所掌事務・業務と保有の必要性、特定された利用目的を確認します。そのうえで、利用目的内として第69条第1項により扱えるのか、目的外であれば第2項のどの例外を根拠とするのかを、学校自身の利用とPTAへの提供について別々に確認します。',
    '69条2項各号の例外に該当すると説明する場合でも、本人または第三者の権利利益を不当に侵害するおそれがないか、提供範囲が必要最小限かを確認する必要があります。': '第69条第2項の例外を根拠とする場合は、該当号、対象情報、利用又は提供先、期間、本人又は第三者の権利利益を不当に侵害するおそれ、記録の有無を確認します。',
    '<div class="law-tags"><span>個人情報保護法69条</span><span>利用目的外提供</span><span>本人同意</span></div>': '<div class="law-tags"><span>個人情報保護法61条</span><span>個人情報保護法69条</span><span>利用・提供記録</span></div>',
    '<li>個人情報収集時の利用目的説明</li>': '<li>個人情報取得時の利用目的説明</li>',
    '<li>PTA提供に関する同意書</li>': '<li>学校自身の利用・PTAへの提供の根拠文書</li>',
    '<li>名簿提供記録・管理台帳</li>': '<li>利用・提供記録、承認記録、管理台帳</li>',
    '<li>PTAへの提供根拠を何条何項で説明するか。</li>': '<li>学校自身の利用かPTAへの提供か。第61条・第69条のどの根拠によるか。</li>',
    '<li>本人同意をいつ、どの書式で取得しているか。</li>': '<li>本人同意を根拠とする場合、対象項目、目的、利用・提供先をいつ、どの書式で示したか。</li>',
    '<li>提供停止・削除の手続はあるか。</li>': '<li>利用・提供の停止、訂正、削除、保存期間の手続はあるか。</li>',
}
for old, new in replacements.items():
    s = replace_once(s, old, new, old[:55])
p.write_text(s, encoding='utf-8')

# Remove the deleted page from static-meta maintenance targets.
for file in ['tools/check-static-meta.js', 'tools/apply-static-meta-fix.js']:
    p = Path(file)
    s = p.read_text(encoding='utf-8')
    s = s.replace("'timeline.html','shizuoka-incident.html','guideline.html','compliance.html'", "'timeline.html','guideline.html','compliance.html'")
    if 'shizuoka-incident.html' in s:
        raise SystemExit(f'residual static-meta reference in {file}')
    p.write_text(s, encoding='utf-8')

# Remove from 404 known-page compatibility list.
p = Path('404.html')
s = p.read_text(encoding='utf-8')
s = replace_once(s, "        'shizuoka-incident.html': true,\n", '', '404 known page')
p.write_text(s, encoding='utf-8')

# Delete the unverified article itself.
incident = Path('shizuoka-incident.html')
if not incident.exists():
    raise SystemExit('shizuoka-incident.html missing before deletion')
incident.unlink()

# Refuse to commit if any public HTML still links to the removed page.
remaining = []
for html in Path('.').rglob('*.html'):
    text = html.read_text(encoding='utf-8', errors='ignore')
    if 'shizuoka-incident.html' in text:
        remaining.append(str(html))
if remaining:
    raise SystemExit('remaining shizuoka links: ' + ', '.join(remaining))
