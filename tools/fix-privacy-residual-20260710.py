from pathlib import Path
import re


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'{label}: expected 1 occurrence, found {count}')
    return text.replace(old, new, 1)


p = Path('privacy.html')
s = p.read_text(encoding='utf-8')

s = replace_once(
    s,
    '<h1>学校からPTAへの<br><em>個人情報提供</em></h1>',
    '<h1>学校保有情報の<br><em>PTA目的利用・提供</em></h1>',
    'hero title',
)

s = replace_once(
    s,
    '学校は入学手続き時に保護者の住所・電話番号・緊急連絡先といった個人情報を収集しています。これは教育活動、児童生徒の安全管理、学校事務のために取得された情報です。PTAは学校とは別の独立した任意団体ですから、学校がその情報をPTAに提供する場面では、個人情報保護法第5章、特に第69条の「利用目的以外の利用・提供」の問題として確認する必要があります。このページでは、学校自身が学校保有情報をPTA事務に利用する場合、学校からPTAへ提供する場合、PTAが加入者本人から直接取得する場合の三つを分け、現場で起きやすい問題を整理します。',
    '学校は入学手続等で保護者の住所、電話番号、緊急連絡先等の個人情報を取得します。学校保有情報をPTA目的で扱う場合は、学校自身による利用、学校からPTAへの提供、PTAによる加入者本人からの直接取得を分けます。学校側の利用・提供については、第61条の所掌事務・業務と保有の必要性、特定された利用目的の範囲、第69条第1項又は第2項の根拠、対象情報、本人説明、記録を確認します。',
    'lead paragraph',
)

# Delete the old red-X route, which had been visually hidden after the first pass.
pattern = r'\s*<p>スライド資料「ハードル②：個人情報保護法とみなし加入の罠」をもとに整理しています。</p>.*?<div class="alert alert-danger">.*?</div>\s*</section>'
replacement = '\n    </section>'
s, count = re.subn(pattern, replacement, s, count=1, flags=re.S)
if count != 1:
    raise SystemExit(f'old route block: expected 1, found {count}')

s = replace_once(
    s,
    '<p>私立学校は「行政機関等」ではありませんが、学校法人等として個人情報取扱事業者側の規律を受けます。そのため、利用目的の特定、目的外利用の制限、第三者提供の制限、安全管理措置などを、民間事業者側の条文体系で確認する必要があります。公立学校と私立学校では適用条文の体系が異なるため、同じ条文番号で一括りにせず、いずれの場合も<strong>PTAへ名簿を渡す根拠と本人同意の有無</strong>を確認します。</p>',
    '<p>私立学校は「行政機関等」ではありませんが、学校法人等として民間部門の個人情報保護法上の規律を受けます。そのため、利用目的の特定、目的外利用、第三者提供、安全管理措置等を民間部門の条文体系で確認します。公立学校と私立学校では適用条文が異なるため、同じ条文番号で一括りにせず、いずれの場合も<strong>学校による利用・提供の根拠、対象情報、本人説明、記録</strong>を確認します。</p>',
    'private school paragraph',
)

s = replace_once(
    s,
    '個人情報保護制度の一元化により、地方公共団体等の個人情報取扱いも個人情報保護法第5章の枠組みで確認する整理になりました。公立学校が保有する児童・保護者情報をPTAに提供する場合は、学校内部の事務ではなく、利用目的以外の利用・提供として第69条を中心に確認します。自治体ごとの旧条例だけを根拠に、現在の学校名簿提供を説明することはできません。',
    '個人情報保護制度の一元化により、地方公共団体等の個人情報取扱いも個人情報保護法第5章の枠組みで確認する整理になりました。公立学校が保有する児童・保護者情報をPTA目的で扱う場合は、学校自身による利用とPTAへの提供を分け、第61条の所掌事務・業務、特定された利用目的の範囲、第69条第1項又は第2項の根拠を確認します。自治体の条例・規則等は、現在の法体系との整合を含めて確認します。',
    'unification FAQ',
)

p.write_text(s, encoding='utf-8')
