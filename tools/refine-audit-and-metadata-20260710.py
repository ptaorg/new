from pathlib import Path


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'{label}: expected 1 occurrence, found {count}')
    return text.replace(old, new, 1)

# Search-result metadata
p = Path('research-index.html')
s = p.read_text(encoding='utf-8')
s = replace_once(
    s,
    'PTA問題を一次資料で検証するための根拠資料・調査方法。法制度、研究方法、資料検証、判例、制度史、最重要資料、教育委員会回答を、照会・情報公開・記事作成へ接続します。',
    'PTA問題を一次資料で検証するため、法制度、行政回答、学校・PTA文書、判例、制度史、資料確認の基準を整理しています。',
    'research meta description',
)
s = replace_once(
    s,
    'PTA問題を一次資料で検証するための根拠資料・調査方法。法制度、研究方法、資料検証、判例、制度史、最重要資料、教育委員会回答へ接続します。',
    'PTA問題を一次資料で検証するため、法制度、行政回答、学校・PTA文書、判例、制度史、資料確認の基準を整理しています。',
    'research og description',
)
p.write_text(s, encoding='utf-8')

p = Path('key-materials.html')
s = p.read_text(encoding='utf-8')
s = replace_once(
    s,
    'PTA運営の適正化を確認する際に最初に見るべき行政通知・公的資料・法令本文を5件に絞り、資料の使い方、確認対象、学校・教育委員会への照会への落とし込みを整理します。',
    'PTA運営を確認する際に参照頻度の高い行政通知、公的資料、法令本文を、対象、射程、実物文書との照合事項とともに整理しています。',
    'key meta description',
)
s = replace_once(
    s,
    'PTA運営の適正化を確認する際に最初に見るべき行政通知・公的資料・法令本文を5件に絞って整理します。',
    'PTA運営を確認する際に参照頻度の高い行政通知、公的資料、法令本文と、その対象・射程を整理しています。',
    'key og description',
)
p.write_text(s, encoding='utf-8')

# Audit page
p = Path('audit/index.html')
s = p.read_text(encoding='utf-8')
s = s.replace('PTA運営チェックアプリ', 'PTA運営チェック')
s = replace_once(s, '<div class="audit-hero-eyebrow">Operation Check App</div>', '', 'audit English eyebrow')
s = replace_once(
    s,
    '<h1>立場別に確認する<br><span class="accent">PTA運営チェック</span></h1>',
    '<h1><span class="accent">PTA運営チェック</span></h1>',
    'audit hero title',
)
s = replace_once(s, '<span class="intro-section-kicker">Select Your Role</span>', '', 'audit role kicker')
s = replace_once(s, '<div class="assessment-kicker">Comprehensive Assessment</div>', '', 'audit assessment kicker')
s = replace_once(s, '<div class="assessment-title">総合評価書</div>', '<div class="assessment-title">確認結果</div>', 'audit assessment title')
s = replace_once(s, '<div class="assessment-loading-text">総合評価を生成しています…</div>', '<div class="assessment-loading-text">確認結果を整理しています…</div>', 'audit loading text')
s = replace_once(s, '<div class="assessment-loading-sub">法的観点からチェック結果を分析中</div>', '<div class="assessment-loading-sub">回答内容を項目別に整理しています</div>', 'audit loading sub')
s = replace_once(s, '<h3>5軸のリスク状況</h3>', '<h3>項目別の確認状況</h3>', 'audit result heading')
s = replace_once(s, '<div class="result-panel-sub">各軸の危険度を色で確認できます</div>', '<div class="result-panel-sub">回答から確認の優先度を整理します</div>', 'audit result sub')
s = replace_once(s, '<div class="result-panel-sub">各項目から関連法令・資料へ進めます</div>', '<div class="result-panel-sub">回答ごとの確認事項と参照資料を示します</div>', 'audit details sub')
s = replace_once(s, '<span>🔄</span><span>再生成</span>', '<span>結果を再表示</span>', 'audit regenerate label')

audit_css = '''
<style id="audit-editorial-20260710">
body{
  background:#fff!important;
}
.audit-hero{
  padding:68px 0 58px!important;
  background:linear-gradient(135deg,#071a30,#183858)!important;
}
.audit-hero::before,
.audit-hero::after{display:none!important}
.audit-hero-inner{
  width:min(calc(100% - 40px),920px)!important;
  display:block!important;
}
.audit-hero h1{
  font-size:clamp(2rem,4vw,3rem)!important;
  text-shadow:none!important;
}
.audit-hero h1 .accent{
  background:none!important;
  -webkit-text-fill-color:#fff!important;
  color:#fff!important;
}
.audit-hero-lede{max-width:820px!important;margin-bottom:0!important}
.audit-hero-meta,
.audit-hero-axes{display:none!important}
.audit-shell{
  width:min(calc(100% - 40px),920px)!important;
  margin:0 auto!important;
  padding:54px 0 96px!important;
}
.intro-section-header{
  text-align:left!important;
  margin:0 0 30px!important;
}
.intro-section-title{font-size:clamp(1.55rem,3vw,2rem)!important}
.intro-section-lead{max-width:800px!important;margin:0!important}
.mode-grid{
  display:block!important;
  border-top:2px solid var(--color-navy)!important;
}
.mode-card{
  width:100%!important;
  display:block!important;
  margin:0!important;
  padding:24px 0!important;
  text-align:left!important;
  background:#fff!important;
  border:0!important;
  border-bottom:1px solid var(--color-line)!important;
  border-radius:0!important;
  box-shadow:none!important;
  transform:none!important;
}
.mode-card:hover{transform:none!important;box-shadow:none!important;background:#f8fafc!important}
.mode-card-image,
.mode-card-kicker,
.mode-check-list{display:none!important}
.mode-card-body{padding:0!important}
.mode-card-title{margin:0 0 8px!important}
.mode-card-desc{max-width:760px!important;margin-bottom:12px!important}
.mode-start-btn{
  display:inline!important;
  padding:0!important;
  background:transparent!important;
  color:var(--color-navy)!important;
  border-radius:0!important;
  text-decoration:underline!important;
  text-underline-offset:.18em!important;
}
.mode-start-btn .arrow{display:none!important}
.q-card,
.assessment-panel,
.result-panel,
.result-risk-banner,
.answer-card,
.assessment-error,
.modal-content{
  border-radius:0!important;
  box-shadow:none!important;
}
.q-card,
.assessment-panel,
.result-panel{
  background:#fff!important;
  border:0!important;
  border-top:2px solid var(--color-navy)!important;
  padding:28px 0!important;
}
.q-axis-badge,
.answer-risk-pill,
.axis-bar-risk-label,
.banner-count-chip{
  border-radius:0!important;
}
.result-layout{grid-template-columns:1fr!important;gap:44px!important}
.result-panel-icon,
.assessment-seal{display:none!important}
.result-panel-sub{padding-left:0!important}
.answer-cards{max-height:none!important;overflow:visible!important;gap:0!important}
.answer-card{
  padding:20px 0!important;
  background:#fff!important;
  border:0!important;
  border-bottom:1px solid var(--color-line)!important;
  border-left:4px solid currentColor!important;
  padding-left:18px!important;
  transform:none!important;
}
.answer-card:hover{transform:none!important;box-shadow:none!important}
.axis-bar-track,
.axis-bar-fill{border-radius:0!important;box-shadow:none!important}
.risk-count-grid{gap:0!important;border-top:1px solid var(--color-line)!important}
.risk-count-cell{
  border-radius:0!important;
  border:0!important;
  border-right:1px solid var(--color-line)!important;
  transform:none!important;
}
.btn-share,
.btn-regenerate{display:none!important}
.check-result-links ul{display:block!important}
.check-result-links a{
  display:inline!important;
  padding:0!important;
  border:0!important;
  border-radius:0!important;
  background:transparent!important;
  text-decoration:underline!important;
}
@media(max-width:768px){
  .audit-hero{padding:52px 0 46px!important}
  .audit-shell{margin:0 auto!important}
  .risk-count-grid{grid-template-columns:1fr 1fr!important}
}
</style>
'''
s = replace_once(s, '</head>', audit_css + '</head>', 'audit css')
p.write_text(s, encoding='utf-8')

# Audit logic and wording
p = Path('audit/check-app.js')
s = p.read_text(encoding='utf-8')
replacements = {
    "0: { label: '問題なしに近い', shortLabel: 'OK', color: '#15803D', cls: 'lv0', barPct: 100 },": "0: { label: '大きな問題は見えにくい', shortLabel: '確認済', color: '#15803D', cls: 'lv0', barPct: 10 },",
    "1: { label: '確認が必要', shortLabel: '要確認', color: '#2563EB', cls: 'lv1', barPct: 76 },": "1: { label: '資料確認が必要', shortLabel: '要確認', color: '#2563EB', cls: 'lv1', barPct: 40 },",
    "2: { label: '運用リスクあり', shortLabel: 'リスク', color: '#D97706', cls: 'lv2', barPct: 52 },": "2: { label: '運用の見直しを検討', shortLabel: '見直し', color: '#D97706', cls: 'lv2', barPct: 70 },",
    "3: { label: '早急な見直しが必要', shortLabel: '見直し', color: '#C2410C', cls: 'lv3', barPct: 28 }": "3: { label: '優先して確認・見直し', shortLabel: '優先確認', color: '#C2410C', cls: 'lv3', barPct: 100 }",
    "'学校が保有する児童・保護者情報をPTAへ提供していますか。'": "'学校が保有する児童・保護者情報をPTA目的で自ら利用し、又はPTAへ提供していますか。'",
    "'学校保有個人情報のPTA提供実態を確認する。'": "'学校保有情報のPTA目的利用とPTAへの提供実態を分けて確認する。'",
    "'PTAが自ら会員管理・会費徴収を行う体制へ移行させる。'": "'PTA自身が会員管理・会費徴収を行えるよう、学校関与の範囲を整理する。'",
    "'学校保有の個人情報をPTAへ提供している実態はありますか。'": "'学校保有情報をPTA目的で自ら利用し、又はPTAへ提供している実態はありますか。'",
    "note: 'PTA固有事務を校務、職専免、兼職承認等で処理している場合、学校とPTAの分離がかえって不明確になるおそれがあります。確認すべき点は、PTA文書の配布・回収、会費処理、名簿管理、役員選出などを学校職員が恒常的に担っていないかです。'": "note: 'PTA関係事務を学校職員が行う場合は、具体的作業を分け、校務・職務命令・職専免・兼職兼業のどの整理によるのか、個人情報、費用、決裁、責任主体とともに確認します。PTAから依頼されたという事実だけでは、学校側の職務上の根拠にはなりません。'",
    "makeCheck({ cat: '制度処理', axis: 'personnel', q: 'PTA固有事務を、校務、職専免、兼職承認等の名目で学校側が恒常的に処理していますか。', riskOn: 'yes', severity: 2, risk: 'PTA固有事務の学校処理', advice: '形式上の処理根拠があるかではなく、PTA固有事務を学校から分離できているかを確認してください。' })": "makeCheck({ cat: '制度処理', axis: 'personnel', q: 'PTA関係事務について、校務、職務命令、職専免、兼職兼業の区分と対象作業が文書化されていますか。', riskOn: 'no', severity: 2, risk: '学校側の職務・服務整理が不明確', advice: '具体的作業ごとに、校務としての根拠、職務命令、職専免、兼職兼業、勤務時間、費用負担、決裁を確認してください。' })",
    "makeCheck({ cat: '個人情報提供', axis: 'privacy', q: '学校保有の児童・保護者情報を、PTA会員管理、役員選出、地区班、登校班、当番表、協力金依頼等に利用・提供していますか。', riskOn: 'yes', severity: 3, risk: '学校保有個人情報のPTA利用', advice: '公立学校が保有する個人情報をPTA用途へ使う場面では、個人情報保護法第69条の目的外利用・提供の問題として確認が必要です。', links: [{ label: '個人情報', url: '../privacy.html' }] })": "makeCheck({ cat: '個人情報利用・提供', axis: 'privacy', q: '学校保有の児童・保護者情報を、PTA会員管理、役員選出、地区班、登校班、当番表、協力金依頼等のために学校が自ら利用し、又はPTAへ提供していますか。', riskOn: 'yes', severity: 3, risk: '学校保有情報のPTA目的利用・提供', advice: '学校自身による利用とPTAへの提供を分け、個人情報保護法第61条・第69条の根拠、対象情報、不同意者の除外、利用・提供記録を確認してください。', links: [{ label: '個人情報', url: '../privacy.html' }] })",
    "makeCheck({ cat: '教育委員会基準', axis: 'personnel', q: '教育委員会として、学校がPTA会費徴収、PTA個人情報提供、PTA文書配布回収、PTA事務従事を行わないための基準・通知・点検項目を整備していますか。', riskOn: 'no', severity: 2, risk: '教育委員会通知・点検基準の不足', advice: '学校ごとの慣行に任せず、教育委員会として学校向けの基準・通知・点検項目を整備する必要があります。' })": "makeCheck({ cat: '教育委員会基準', axis: 'personnel', q: '教育委員会として、学校によるPTA会費徴収、個人情報の利用・提供、文書配布回収、PTA関係事務の関与範囲を確認する基準・通知・点検項目を整備していますか。', riskOn: 'no', severity: 2, risk: '教育委員会通知・点検基準の不足', advice: '学校ごとの慣行に任せず、教育委員会として学校関与の根拠と範囲を確認する基準・通知・点検項目を整備する必要があります。' })",
    "eyebrow: '見直し優先',": "eyebrow: '優先確認',",
    "title: '早急な見直しが必要な項目があります',": "title: '優先して確認・見直す項目があります',",
    "title: '運用リスクがあります',": "title: '運用の見直しを検討する項目があります',",
    "title: '問題なしに近い状態です',": "title: '今回の回答では大きな問題は見えにくい状態です',",
    '<h2>総合評価：${escapeHtml(overall.title)}</h2>': '<h2>確認結果：${escapeHtml(overall.title)}</h2>',
    '<h3>重点リスク</h3>': '<h3>優先して確認する事項</h3>',
    '<h3>次にやること</h3>': '<h3>次の確認事項</h3>',
    '<h3>関連ページ</h3>': '<h3>参照資料</h3>',
    'PTA適正化推進委員会の運営チェックアプリで確認しました。': 'PTA適正化推進委員会の運営チェックで確認しました。',
}
for old, new in replacements.items():
    count = s.count(old)
    if count != 1:
        raise SystemExit(f'check-app replacement failed ({count}): {old[:70]}')
    s = s.replace(old, new, 1)
p.write_text(s, encoding='utf-8')
