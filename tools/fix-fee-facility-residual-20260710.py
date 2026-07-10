from pathlib import Path


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'{label}: expected 1 occurrence, found {count}')
    return text.replace(old, new, 1)

p = Path('fee-collection.html')
s = p.read_text(encoding='utf-8')
replacements = {
    '2つの集金ルート ― <em>適正と問題</em>': '会費徴収の方式と <em>確認事項</em>',
    '<p class="fee-ph">PTAの独自徴収</p>': '<p class="fee-ph">PTAによる直接徴収</p>',
    '<div class="fee-pli">学校事務の負担はゼロ</div>': '<div class="fee-pli">学校の徴収事務・口座情報を使わない</div>',
    '<div class="fee-pli">支払いの任意性が明確</div>': '<div class="fee-pli">会員と徴収対象者を対応させやすい</div>',
    '<span class="fee-verdict">✓ 適正</span>': '<span class="fee-verdict">構造が明確</span>',
    '<p class="fee-ph">抱き合わせ・代行徴収</p>': '<p class="fee-ph">学校が徴収へ関与する方式</p>',
    '<div class="fee-pli">委任契約なき代理（無権代理）</div>': '<div class="fee-pli">加入・会費債務・徴収対象者の確認</div>',
    '<div class="fee-pli">事実上の強制徴収</div>': '<div class="fee-pli">学校費用との誤認、情報・会計混在の防止</div>',
    '<span class="fee-verdict">✗ 問題</span>': '<span class="fee-verdict">根拠と記録を確認</span>',
    '<p class="fee-concl">問題は「金額」ではなく、<em>学校の徴収手続にPTA会費が混ざること</em>。</p>': '<p class="fee-concl">PTAによる直接徴収が最も明確です。学校が関与する場合は、<em>加入・情報利用・校務服務・会計区分</em>を文書で確認します。</p>',
    '／文科省 学校徴収金ガイドライン': '／文部科学省 2025年学校徴収金通知',
    '<title>2つの集金ルート：適正運用（青）と問題運用（赤）の対比フローチャート</title>': '<title>PTAによる直接徴収と学校関与方式の確認事項</title>',
    '<text x="580" y="148" text-anchor="middle" font-family="\'Noto Sans JP\',sans-serif" font-size="13" font-weight="700" fill="#7f1d1d">記録不在 /</text>': '<text x="580" y="148" text-anchor="middle" font-family="\'Noto Sans JP\',sans-serif" font-size="13" font-weight="700" fill="#7f1d1d">加入記録・</text>',
    '<text x="580" y="165" text-anchor="middle" font-family="\'Noto Sans JP\',sans-serif" font-size="13" font-weight="700" fill="#7f1d1d">黙示の入会</text>': '<text x="580" y="165" text-anchor="middle" font-family="\'Noto Sans JP\',sans-serif" font-size="13" font-weight="700" fill="#7f1d1d">徴収対象が不明</text>',
    '>職務専念義務違反</text>': '>校務・服務の根拠</text>',
    '>利益供与</text>': '>口座情報の利用</text>',
    '>無権代理</text>': '>会員・債務の確認</text>',
    '>PTA自身で会費請求</text>': '>PTAが会員へ直接請求</text>',
    '>［○ 適正］</text>': '>［構造が明確］</text>',
    '>学校に集金代行依頼</text>': '>学校が徴収へ関与</text>',
    '>［× 問題リスク高］</text>': '>［根拠確認が必要］</text>',
    '>現在の多くのPTAが歩む「赤の道」は</text>': '>学校が徴収へ関与する場合は</text>',
    '>最初から根拠確認が必要です</text>': '>加入・情報・校務・会計を確認</text>',
}
for old, new in replacements.items():
    s = replace_once(s, old, new, old[:40])
p.write_text(s, encoding='utf-8')

p = Path('facilities.html')
s = p.read_text(encoding='utf-8')
old = '年1回の入会案内など限定的な範囲であれば、渉外的な協力として許容されると考えられます。しかし毎月・毎週のように学校配布物にPTA文書を同封することは、①教職員の職務（配布・回収）を私的団体のために使う、②PTAの文書を学校公文書と混同させるという2つの問題をはらみます。PTAの連絡は原則としてPTA独自の経路（役員から保護者へ）で行うことが望ましいです。'
new = '配布頻度だけで許否は決まりません。学校がPTA文書を配布する場合は、発行主体、配布目的、対象者、学校職員が扱う根拠、学校保有情報の利用、回収の有無、学校文書との区別を確認します。PTA内部の継続的な連絡はPTA自身の連絡手段を基本とし、学校が協力する範囲を文書で定めます。'
s = replace_once(s, old, new, 'facility distribution FAQ')
p.write_text(s, encoding='utf-8')
