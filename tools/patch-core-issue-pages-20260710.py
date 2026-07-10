from pathlib import Path
import re


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: expected 1 occurrence, found {count}")
    return text.replace(old, new, 1)


def remove_once(text: str, pattern: str, label: str) -> str:
    text, count = re.subn(pattern, '', text, count=1, flags=re.S)
    if count != 1:
        raise SystemExit(f"{label}: expected 1 occurrence, found {count}")
    return text

# ============================================================
# fee-collection.html
# ============================================================
p = Path('fee-collection.html')
s = p.read_text(encoding='utf-8')
s = remove_once(s, r'<div class="issue-hero-toc">.*?</div>\s*</div>\s*</section>', 'fee hero toc') + ''
# The preceding regex consumes the hero wrappers; restore their closing structure before issue-content.
s = s.replace('\n\n  <div class="issue-content">', '\n    </div>\n  </section>\n\n  <div class="issue-content">', 1)
s = remove_once(s, r'<aside class="issue-sidebar">.*?</aside>', 'fee sidebar')
s = remove_once(s, r'<section class="editorial-brief fee-editorial-brief".*?</section>', 'fee editorial brief')
s = remove_once(s, r'<div class="related-links-section">.*?</div>\s*</div>\s*</main>', 'fee related links') + ''
s = s.replace('\n  </div>\n\n  <!-- Footer -->', '\n    </main>\n  </div>\n\n  <!-- Footer -->', 1)
fee_repls = {
    '無権代理 ― 委任契約なき代理徴収': '会員関係と会費債務の確認',
    '<span class="fee-law">民法113条</span><span class="fee-nsub">徴収業務の委任がなければ無権代理として効果の帰属が争点。</span>': '<span class="fee-law">民法521条・522条</span><span class="fee-nsub">加入申込み、承諾、会則上の会費額と徴収対象者を先に確認。</span>',
    '公私会計の混同': '学校側の事務権限・服務・決裁',
    '学校徴収金（準公金）とPTA会費（私費）の区別が消える。': '学校が私的団体会費を扱う根拠、担当、責任範囲を確認。',
    '割当寄付の禁止に抵触': '学校保有口座情報の利用根拠',
    '<span class="fee-law">地方財政法4条の5</span><span class="fee-nsub">全世帯一律の事実上の強制は、割当的寄付に接近する。</span>': '<span class="fee-law">個人情報保護法61条・69条</span><span class="fee-nsub">学校徴収金用に取得した情報をPTA会費へ使う根拠を確認。</span>',
    '出典：民法113条／地方財政法4条の5': '確認条文：民法521条・522条／個人情報保護法61条・69条／学校側の会計・服務規程',
    '<b>委任契約なき代理徴収（無権代理）</b><span>民法113条</span>': '<b>加入・会費債務・学校関与の根拠</b><span>民法521条・522条／学校側規程</span>',
    '<b>勤務時間中の私団体事務</b><span>地方公務員法35条</span>': '<b>校務・服務・決裁の確認</b><span>地方公務員法35条／自治体規程</span>',
    '学校が私的団体PTAの会費を代行徴収する構造は、<em>委任契約・会計・服務の三方向</em>で法的問題を抱える。': '学校がPTA会費の徴収へ関与する場合は、<em>加入契約・情報利用・校務服務・会計区分</em>を別々に確認する。',
    '出典：民法113条／個人情報保護法／地方公務員法35条': '確認条文・規程：民法521条・522条／個人情報保護法61条・69条／地方公務員法35条／自治体会計規程',
    '<div class="dc-problem">⚠️ この構造では保護者にとって「学校への支払い」と「PTA会費」の区別が不可能になり、事実上の強制加入・強制徴収となります。</div>': '<div class="dc-problem">学校徴収金とPTA会費が同じ通知・口座・未納管理に入ると、保護者が両者を区別しにくくなります。徴収主体、会員確認、情報利用、会計責任を文書で分ける必要があります。</div>',
    '文科省ガイドラインが示す <em>「2つの道」</em>': '2025年通知が示す <em>学校徴収金の整理</em>',
    '<div class="fee-branch ok"><h4>公会計化</h4><p>給食費等は自治体の歳入へ。</p><span class="fee-tag">✓ 適切な種目</span></div>': '<div class="fee-branch ok"><h4>公会計化</h4><p>対象となる学校徴収金を地方公共団体の会計で扱う。</p><span class="fee-tag">学校徴収金の選択肢</span></div>',
    '<div class="fee-branch ok"><h4>直接納付（直接購入）</h4><p>PTA会費はPTAが独自に集める。</p><span class="fee-tag">✓ PTAはこちら</span></div>': '<div class="fee-branch ok"><h4>学校を経由しない直接支払</h4><p>保護者と業者等の間で直接支払う。</p><span class="fee-tag">学校徴収金の選択肢</span></div>',
    '<div class="fee-branch ng"><h4>PTA会費を公会計化</h4><p>私的団体の会費は公金化できない。</p><span class="fee-tag">✗ 不可</span></div>': '<div class="fee-branch ng"><h4>PTA会費</h4><p>この通知の直接対象ではないため、加入、徴収主体、情報利用、会計区分を別に確認する。</p><span class="fee-tag">別途根拠確認</span></div>',
    'PTAは私的団体ゆえ公会計化の対象外。ガイドラインの文言どおりなら、<em>学校による代行徴収は廃止し、独自徴収へ移行</em>すべき。': '2025年通知はPTA会費を直接規律するものではない。学校教育に必要な費用ですら学校外へ移す政策方向と比較し、PTA会費への学校関与は<em>別個の根拠と記録</em>を確認する。',
    '出典：文科省「学校給食費等の徴収等の公会計化等の推進について（ガイドライン）」2019': '出典：文部科学省「学校徴収金の公会計化等の取組の一層の推進について」2025年4月30日',
    '<th>学校徴収金（学校預り金）</th>': '<th>学校が扱う教育活動関係費</th>',
    '<td class="ok">準公金（学校が管理責任）</td>': '<td class="ok">費目・制度により公会計、私費会計、直接支払等に分かれる</td>',
    '<td class="ok">教育活動への使用・児童への直接還元</td>': '<td class="ok">対象となる教育活動、購入又はサービスとの関係</td>',
    '<td class="ok">在籍する全児童に関係</td>': '<td class="ok">費目、対象者、購入・参加の条件による</td>',
    '<td class="ok">学校の責任下で管理可能</td>': '<td class="ok">自治体の制度・規程・費目に応じて管理主体を確認</td>',
    '<p>最も構造が明確なのは、PTAが加入者本人から必要な情報を取得し、自ら会費を請求・徴収する完全分離です。学校が関与する例外的な運用を残す場合は、学校側とPTA側の根拠を別々に文書化する必要があります。</p>': '<p>最も構造が明確なのは、PTAが加入者本人から必要な情報を取得し、自ら会費を請求・徴収する方式です。学校関与を残す場合は、PTA側の加入・会費債務と、学校側の情報利用・校務・服務・決裁・会計の根拠を別々に文書化します。</p>',
    '<div class="trans-label">✅ 推奨 — 完全分離</div>': '<div class="trans-label">基本方式 — PTAによる直接徴収</div>',
    '<div class="trans-label">⚠️ 経過措置 — 条件付き委託</div>': '<div class="trans-label">学校関与を残す場合 — 条件確認</div>',
}
for old, new in fee_repls.items():
    s = replace_once(s, old, new, f'fee replacement: {old[:35]}')
fee_css = '''
<style id="fee-final-editorial-20260710">
.fee-editorial .issue-hero-inner{grid-template-columns:1fr!important;max-width:960px!important}
.fee-editorial .issue-content{grid-template-columns:1fr!important;max-width:960px!important}
.fee-editorial .section-eyebrow,
.fee-editorial .section-kicker,
.fee-editorial .editorial-brief-band{display:none!important}
.fee-editorial .triple-problem,
.fee-editorial .transition-options{display:block!important}
.fee-editorial .triple-card,
.fee-editorial .trans-card,
.fee-editorial .double-commission,
.fee-editorial .alert-block,
.fee-editorial .law-quote-block,
.fee-editorial .mext-quote{
  margin:0!important;
  padding:22px 0!important;
  border:0!important;
  border-bottom:1px solid #d8dee8!important;
  border-radius:0!important;
  box-shadow:none!important;
  background:#fff!important;
  transform:none!important;
}
.fee-editorial .triple-law,
.fee-editorial .trans-label,
.fee-editorial .req-law{
  padding:0!important;
  background:transparent!important;
  border-radius:0!important;
}
.fee-editorial .req-step-num{border-radius:0!important;box-shadow:none!important}
.fee-editorial .related-links-section{display:none!important}
</style>
'''
s = replace_once(s, '</head>', fee_css + '</head>', 'fee css')
p.write_text(s, encoding='utf-8')

# ============================================================
# personnel.html
# ============================================================
p = Path('personnel.html')
s = p.read_text(encoding='utf-8')
s = remove_once(s, r'<div class="hero-actions">.*?</div>', 'personnel hero actions')
s = remove_once(s, r'<div class="page-banner".*?</div>\s*</div>', 'personnel page banner')
s = remove_once(s, r'<section class="pg-section">\s*<h2>関連導線</h2>.*?</section>', 'personnel related links')
s = replace_once(s, '切り離し後の「渉外業務のみ」体制を書面化する', '切り離し後の連絡調整と協力範囲を書面化する', 'personnel step heading')
personnel_css = '''
<style id="personnel-final-editorial-20260710">
.pg-main{max-width:920px!important}
.pg-main .section-kicker,
.pg-main .editorial-brief-band{display:none!important}
.pg-main .editorial-brief,
.pg-main .editorial-panel,
.pg-main .alert,
.pg-main .source-lens-item,
.pg-main .faq-item{
  border-radius:0!important;
  box-shadow:none!important;
}
.pg-main .editorial-brief{padding:0!important;background:#fff!important;border:0!important}
.pg-main .editorial-brief-body{padding:0!important}
.pg-main .editorial-brief-grid,
.pg-main .source-lens-grid{display:block!important}
.pg-main .editorial-brief-point,
.pg-main .source-lens-item{
  padding:18px 0!important;
  border:0!important;
  border-bottom:1px solid var(--line)!important;
  background:#fff!important;
}
.pg-main .editorial-brief-point>span{display:none!important}
.pg-main .faq-list{gap:0!important;border-top:1px solid var(--line)!important}
.pg-main .faq-item{border:0!important;border-bottom:1px solid var(--line)!important}
.pg-main .faq-q{padding:18px 0!important}
.pg-main .faq-a{padding-left:0!important;padding-right:0!important}
</style>
'''
s = replace_once(s, '</head>', personnel_css + '</head>', 'personnel css')
p.write_text(s, encoding='utf-8')

# ============================================================
# facilities.html
# ============================================================
p = Path('facilities.html')
s = p.read_text(encoding='utf-8')
s = remove_once(s, r'<div class="hero-actions">.*?</div>', 'facilities hero actions')
s = remove_once(s, r'<div class="page-banner".*?</div>\s*</div>', 'facilities page banner')
s = remove_once(s, r'<section class="editorial-brief facilities-editorial-brief".*?</section>', 'facilities editorial brief')
s = remove_once(s, r'<section>\s*<h2>関連導線</h2>.*?</section>', 'facilities related links')
facility_repls = {
    '「いつからOK」という規定はありません。学校教育法137条は公共目的の施設利用を認めていますが、特定団体への恒常的な無償提供まで当然に正当化するものではありません。使用料・責任者・使用範囲を書面で定め、学校長から正式な使用許可を得ることが必要です。': '学校教育法137条は公共目的の施設利用を認めていますが、特定団体への恒常的な無償提供まで当然に正当化するものではありません。許可権者や校長への委任の有無は自治体の条例・規則によって異なります。使用目的、使用範囲、費用・減免、責任者、決裁を許可文書で確認します。',
    '学校施設の鍵は学校が管理主体であるべきです。PTAが常時鍵を保管する状態は、学校の公物管理義務の観点から問題があります。緊急時の責任所在も不明確になります。学校側と協議し、「使用時に借用・返却」する運用に移行することをお勧めします。': '鍵の管理方法は、自治体の施設管理規程と許可条件に沿って確認します。PTAが常時保管する場合でも、貸与記録、保管責任者、複製禁止、紛失時対応、返却条件、学校側の緊急アクセスを明確にする必要があります。根拠や記録がない場合は、使用時の借用・返却を含めて見直します。',
    '本来であれば教育委員会・自治体の予算で整備すべき学校設備を、PTAが資金拠出することは「割当的寄附」として地方財政法上問題になり得ます。単発・少額の場合は直ちに違法とはなりませんが、「PTAが費用を出さないと整備されない」という構造が固定化すれば、実質的に強制加入会費を公費の補填に使っていることになります。教育委員会への予算要望として要求することが本来の対応です。': 'PTAから学校設備への資金拠出だけで、直ちに地方財政法4条の5へ抵触するわけではありません。寄附の自発的申出、PTA内部の意思決定、自治体の受入決裁、資産計上、使途を確認します。一方、学校側が金額を割り当て、毎年度の予算不足を恒常的に補わせ、非加入・不払いへ圧力を加えている場合は、行政の関与と強制性を具体的に点検します。',
    'できます。地方教育行政の組織及び運営に関する法律（地教行法）第23条に基づき、教育委員会は学校の管理・運営に関する事務を所掌しています。施設の公私境界が曖昧な状態の改善を、教育委員会に対して文書で要望することが可能です。当委員会の「全国教育委員会回答DB」には、こうした照会に対する各自治体の回答が収録されています。': 'できます。教育委員会は、地教行法と自治体の条例・規則に基づき、所管学校の施設・財産管理や学校運営を確認する立場にあります。使用許可、許可権者、費用・減免、責任、鍵・備品管理、停止条件を具体的に示して文書で照会します。全国教育委員会への照会結果も、自治体ごとの判断例として確認できます。',
}
for old, new in facility_repls.items():
    s = replace_once(s, old, new, f'facility replacement: {old[:35]}')
facility_css = '''
<style id="facilities-final-editorial-20260710">
.pg{max-width:920px!important}
.pg .section-kicker{display:none!important}
.pg .safes,
.pg .source-lens-grid{display:block!important}
.pg .safe-box,
.pg .wall,
.pg .alert,
.pg .source-lens-item,
.pg .faq-item{
  border-radius:0!important;
  box-shadow:none!important;
}
.pg .safe-box,
.pg .source-lens-item{
  padding:22px 0!important;
  border:0!important;
  border-bottom:1px solid var(--line)!important;
  background:#fff!important;
}
.pg .wall{
  padding:20px 0!important;
  background:#fff!important;
  border:0!important;
  border-top:2px solid var(--navy)!important;
  border-bottom:1px solid var(--line)!important;
}
.pg .wall-label,
.pg .badge{
  padding:0!important;
  background:transparent!important;
  color:inherit!important;
  border-radius:0!important;
}
.pg .faq-list{gap:0!important;border-top:1px solid var(--line)!important}
.pg .faq-item{border:0!important;border-bottom:1px solid var(--line)!important}
.pg .faq-q{padding:18px 0!important}
.pg .faq-a{padding-left:0!important;padding-right:0!important}
</style>
'''
s = replace_once(s, '</head>', facility_css + '</head>', 'facilities css')
p.write_text(s, encoding='utf-8')
