from pathlib import Path
import re


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: expected 1 occurrence, found {count}")
    return text.replace(old, new, 1)


p = Path("reality.html")
s = p.read_text(encoding="utf-8")

replacements = {
    "<title>今、実際に何が行われているか | PTA適正化推進委員会</title>": "<title>学校とPTAの運用実例を点検する | PTA適正化推進委員会</title>",
    '<meta name="description" content="学校とPTAの関係で問題になりやすい文書・案内・徴収・名簿・教職員関与の構造を、実例型の再現資料を使って整理します。">': '<meta name="description" content="学校とPTAの関係で問題になりやすい入会案内、会費徴収、学校保有情報、教職員関与を、再現資料と確認事項から点検します。">',
    '<meta property="og:title" content="今、実際に何が行われているか | PTA適正化推進委員会">': '<meta property="og:title" content="学校とPTAの運用実例を点検する | PTA適正化推進委員会">',
    '<meta property="og:description" content="学校とPTAの関係で問題になりやすい文書・案内・徴収・名簿・教職員関与の構造を、再現資料を使って整理します。">': '<meta property="og:description" content="入会案内、会費徴収、学校保有情報、教職員関与の再現資料から、確認すべき文書と根拠を整理します。">',
    '<meta name="twitter:title" content="今、実際に何が行われているか | PTA適正化推進委員会">': '<meta name="twitter:title" content="学校とPTAの運用実例を点検する | PTA適正化推進委員会">',
    '<meta name="twitter:description" content="学校とPTAの関係で問題になりやすい文書・案内・徴収・名簿・教職員関与の構造を、再現資料を使って整理します。">': '<meta name="twitter:description" content="入会案内、会費徴収、学校保有情報、教職員関与の再現資料から、確認すべき文書と根拠を整理します。">',
    '<body>': '<body class="reality-editorial">',
    '<div class="reality-hero-kicker">実態調査</div>': '<div class="reality-hero-kicker">運用実例</div>',
    '<h1>今、実際に何が行われているか</h1>': '<h1>学校とPTAの運用実例を点検する</h1>',
    '学校とPTAの関係で問題になりやすい文書・案内・徴収・名簿・教職員関与の構造を、再現資料を使って整理します。<br>\n      これは「昔の話」ではありません。': '入会案内、会費徴収、学校保有情報、教職員関与について、再現資料から確認すべき事実と文書を整理します。再現例だけで個別の学校を評価せず、実際の文書と決裁記録を照合します。',
    '<h2>入会届なしに会員にされる「みなし加入」</h2>': '<h2>申込記録が確認できないまま会員扱いされる運用</h2>',
    '入学・転入のタイミングで、保護者の明示的な意思確認（入会申込書の記入・署名）を確認しにくいまま、PTA会員として扱われる運用があります。以下は、そのような運用で使われがちな案内文書のタイプを再現したものです。': '入学・転入時に、本人の申込みとPTAの承諾を確認できる記録がないまま、PTA会員として扱われる運用があります。以下は、確認を要する案内文の構造を再現したものです。',
    '悪い例：実際に流通しているタイプの書類': '再現例：確認を要する入会・会費案内',
    '【問題点④】問い合わせ先が「学校事務室」。学校とPTAが一体化しており、学校がPTAの業務を代行していることを示す。': '【確認点④】問い合わせ先が学校事務室である場合、単なる取次ぎか、学校がPTA内部事務を処理しているのか、校務・服務上の位置付けと責任分担を確認する。',
    '<strong>民法第522条（契約の成立）</strong>：契約は、契約の内容を示してその締結を申し入れる意思表示（申込み）に対して相手方が承諾をしたときに成立する。保護者の側から入会の意思表示がない限り、PTAとの会員契約は成立しない。<br><br>\n        <strong>憲法第21条（結社の自由）</strong>：いかなる団体への加入も、本人の意思に反して強制することはできない。「加入しない自由」は憲法上の権利として保障されている。': '<strong>民法第521条・第522条</strong>：学校への入学、PTAからの一方的な通知、保護者の沈黙だけでは、本人の申込みとPTAの承諾を確認できません。恒常的な会員管理は、会則、会費、活動内容、退会方法を示し、申込みと承諾を客観的に記録します。<br><br>\n        <strong>憲法第21条</strong>：公立学校や教育委員会が学校の権限、情報、職員、施設等を用いて加入を事実上強制している場合は、公権力による結社の自由への関与として別途検討します。',
    '<blockquote>みなし加入は不適切と明言</blockquote>': '<blockquote>自治体回答から入会意思の確認方法を検証する</blockquote>',
    '教育委員会回答の一例。回答本文・発出主体・対象範囲を確認し、他の自治体回答や学校別資料と照合して読む必要があります。': '自治体回答は、回答本文、質問文、担当部署、対象範囲、回答日を一式で確認し、各学校の入会案内、会則、申込記録と照合します。',
    '<h2>学校が「代理」でPTA会費を集める構造</h2>': '<h2>学校徴収金とPTA会費が同じ手続で扱われる構造</h2>',
    '悪い例：問題のある徴収案内': '再現例：学校徴収金とPTA会費が一体化した案内',
    'この構造では、PTAへの「加入・未加入」の区別なく引き落とされ、保護者は実質的に拒否できない状態に置かれます。学校（公的機関）がPTA（任意団体）の徴収業務を代行することは、双方の独立性を損なうものです。': 'この再現例では、加入者と非加入者の区分、会費債務、口座情報の利用、学校側の校務・決裁、PTA会計への送金が一つの手続に重なっています。学校が関与する場合は、それぞれの根拠と記録を分けて確認します。',
    '<blockquote>PTAが独自に徴収することが最もふさわしい方法</blockquote>': '<blockquote>自治体回答から徴収主体と学校関与の根拠を確認する</blockquote>',
    '厚木市教育委員会（令和8年4月）— 「代行徴収に法的位置づけはない」として、学校によるPTA会費代行徴収の問題性を間接的に認める。': '自治体回答は、質問内容、回答文言、対象校、制度の根拠文書を確認し、特定の回答だけから全国一律の結論を導かないようにします。',
    '<h2>保護者の同意なく学校名簿がPTAに渡される</h2>': '<h2>学校保有情報がPTA目的で利用・提供される場面</h2>',
    '学校が管理している児童・生徒の名簿（氏名・住所・電話番号等）が、PTA役員に渡されたのではないかと問題になることがあります。ここで確認すべきなのは、本人同意の有無、提供項目、不同意者の除外、提供記録、PTAが本人から直接取得した情報なのかどうかです。': '学校が保有する氏名、住所、電話番号、学級等の情報がPTA目的で使われる場合は、学校自身による利用か、学校からPTAへの提供か、PTAが加入者本人から直接取得した情報かを分けます。第61条の所掌事務・業務、第69条第1項又は第2項の根拠、対象項目、本人説明、利用・提供記録を確認します。',
    '<h4>PTA役員が学校から名簿を受け取る</h4>': '<h4>学校保有情報がPTA目的で利用・提供される</h4>',
    '<p>慣行として、PTA本部役員や地区委員が学校から「名簿のデータ」「クラス名簿」を受け取る。保護者への事前通知・同意取得なしに行われることが多い。</p>': '<p>学校が自らPTA事務に利用しているのか、PTA役員へ名簿又はデータを提供しているのか、利用・提供の主体、項目、目的、承認、記録を確認する。</p>',
    '<p>PTAに加入した覚えも、個人情報を提供した覚えもないのに、PTA役員から電話が来たり自宅に郵便物が届く——この時点で個人情報はすでに第三者に渡っている。</p>': '<p>PTA役員から連絡を受けた事実だけでは取得経路を断定できない。PTAによる直接取得、学校による配布・配信、学校からPTAへの提供等のどの経路かを文書で確認する。</p>',
    '<strong>個人情報保護法第69条（利用及び提供の制限）</strong>：行政機関等が保有する個人情報を、当初の収集目的を超えて第三者（PTAを含む）に提供するためには、法令の根拠、または本人の同意が必要。「学校の教育活動のため」として収集した個人情報を、任意団体であるPTAに提供することは、原則として本人の同意なしには認められない。': '<strong>個人情報保護法第61条・第69条</strong>：まず、学校の所掌事務・業務と保有の必要性、特定された利用目的の範囲を確認します。利用目的内で第69条第1項により扱えるのか、目的外であれば第2項のどの例外を根拠とするのかを確認し、学校自身による利用とPTAへの提供を別々に整理します。',
    '<h2>教員・事務職員が勤務中にPTA業務をしている</h2>': '<h2>教職員によるPTA事務の校務・服務上の位置付け</h2>',
    '公立学校の教員・事務職員は地方公務員であり、勤務時間中は職務に専念する義務があります。PTAは任意の民間団体であり、教職員がPTA業務を行う場合には「職務専念義務免除（職専免）」の申請・承認が必要です。しかし実態として、この手続きなしにPTA業務が行われているケースが複数の外部監査で指摘されています。': '勤務時間中のPTA関与は、時間帯だけで一律に判断しません。具体的な作業が学校とPTAの連絡調整か、会員管理、会費、役員選出等のPTA内部事務かを分け、校務としての位置付け、職務命令、職務専念義務免除、兼職・兼業、決裁記録を確認します。',
    '適正な例：正しく手続きされた職専免申請書': '確認資料の例：職務専念義務免除申請書',
    '適正な場合：事前に申請書を提出し、校長の承認を得た上でPTA業務を行う。日時・活動名称・承認者が明記されており、透明性がある。': '職専免を根拠とする場合は、適用規則、対象者、日時、用務、承認者を確認します。校務として処理している場合は、校務分掌、職務命令、決裁、費用負担を別に確認します。',
    'しかし実態は？': '確認が必要な運用',
    '申請書なしで、授業の合間や放課後にPTA書類の作成・連絡業務を行っている教職員がいる。': 'PTA書類の作成・連絡業務が行われている場合、作業内容、時間、校務としての位置付け、職務命令又は職専免等の根拠を確認する。',
    '学校の電話・コピー機・PCをPTA業務に使用しているケースがある（公費の私的使用の問題）。': '学校の電話、コピー機、PC等を使っている場合、使用許可、費用負担、情報管理、学校業務との区分を確認する。',
    '「包括的な職専免承認」（期間・活動名を特定せず一括承認）という形式で、実質的に無限定の免除が行われているケースが監査で指摘されている。': '包括的な職専免承認がある場合、根拠規則、対象用務、期間、承認権者、個別作業との対応が後から確認できるかを点検する。',
    'PTA業務は「当該地方公共団体がなすべき職務」ではない。勤務時間中にPTA業務を行うためには、正式な職専免の申請・承認が必要。': '勤務時間中の関与については、具体的作業が校務として特定され、職務命令の対象となっているのか、校務外の活動として職専免又は兼職・兼業等の根拠があるのかを確認します。PTA内部事務であること又は勤務時間中であることだけから、一律の結論を出しません。',
    '長野県包括外部監査：職専免の不適切な運用を指摘': '包括外部監査で確認された服務管理上の論点',
    '長野県の包括外部監査報告書において、学校教職員のPTA業務にかかる職務専念義務免除の運用実態が調査された。複数の学校で、申請・承認の記録が不十分であったり、活動の日時・内容が特定されないまま「一括承認」されているケースが確認され、法令上の問題が指摘された。': '包括外部監査等の資料を使う場合は、監査対象、年度、適用規則、指摘事項、措置状況を原文で確認します。別の自治体や学校へ当てはめるときは、各自治体の服務規程と実際の承認記録を照合します。',
}

for old, new in replacements.items():
    s = replace_once(s, old, new, old[:55])

s = s.replace('https://ptaorg.github.io/donate/', '/support.html')
s = s.replace('運営チェックアプリ', '運営チェック')
s = s.replace('<a href="#" class="nav-link">立場別</a>', '<a href="/index.html#roles" class="nav-link">立場別</a>')
s = s.replace('<a href="#" class="nav-link">資料</a>', '<a href="/research-index.html" class="nav-link">根拠資料</a>')
s = s.replace('<a href="#" class="nav-link">研究論考</a>', '<a href="/journal.html" class="nav-link">論考・調査報告</a>')

# Remove the sticky in-page hub.
s, count = re.subn(r'\s*<nav class="anchor-nav".*?</nav>', '', s, count=1, flags=re.S)
if count != 1:
    raise SystemExit(f"anchor nav: expected 1, found {count}")

# Collapse three introductory hub sections into one concise explanation.
pattern = r'\s*<section class="editorial-section reality-reading-note".*?</section>\s*<section class="editorial-section reality-reading-note" id="reality-source-expansion">.*?</section>\s*<section class="editorial-section source-lens-panel" id="reality-request-map">.*?</section>'
intro = '''
<section class="editorial-section reality-intro" aria-labelledby="reality-intro-title">
  <h2 id="reality-intro-title">再現資料から確認する事項</h2>
  <p>このページの文書例は、個別の学校を評価するための証拠ではなく、実物資料を読む際の確認項目を示す再現です。入会申込記録、会費の請求主体、学校保有情報の利用・提供、教職員の校務・服務上の根拠を分けて確認します。</p>
  <p>実際の判断では、入会案内、会則、学校徴収金案内、口座振替資料、利用・提供記録、校務分掌、職務命令、職専免記録、会計資料を照合します。</p>
</section>'''
s, count = re.subn(pattern, intro, s, count=1, flags=re.S)
if count != 1:
    raise SystemExit(f"intro hubs: expected 1, found {count}")

# Remove the unverified incident claim and replace it with a verification rule.
pattern = r'\s*<div class="incident-box">\s*<div class="incident-box-label">実際の事案</div>\s*<div class="incident-box-title">静岡市立20校・9,200人分の個人情報をPTAに根拠不明の提供.*?</div>\s*<div class="incident-box-body">.*?</div>\s*</div>'
incident = '''
    <div class="incident-box">
      <div class="incident-box-label">事実確認</div>
      <div class="incident-box-title">自治体・学校ごとの件数と経緯は一次資料で確認する</div>
      <div class="incident-box-body">報道や断片的な説明を引用するときは、対象校数、対象人数、情報項目、利用又は提供の主体、時期、本人説明、教育委員会の調査結果、再発防止措置を原資料で確認します。確認できない具体的数値や評価は掲載しません。</div>
    </div>'''
s, count = re.subn(pattern, incident, s, count=1, flags=re.S)
if count != 1:
    raise SystemExit(f"unverified incident: expected 1, found {count}")

# Replace the promotional ending with a conclusion, not another hub.
pattern = r'\s*<!-- =========================================\s*まとめ・CTAセクション\s*========================================= -->\s*<section class="reality-cta">.*?</section>'
summary = '''
<section class="reality-summary">
  <div class="wrap">
    <h2>再現例から、実物文書の確認へ進む</h2>
    <p>再現例と似た案内があるだけで、直ちに法令違反と断定することはできません。誰が作成し、誰が承認し、どの情報と口座を使い、どの会員記録・校務・服務・会計根拠に基づいているかを、実物文書で確認します。</p>
  </div>
</section>'''
s, count = re.subn(pattern, summary, s, count=1, flags=re.S)
if count != 1:
    raise SystemExit(f"final CTA: expected 1, found {count}")

# Add the 2025 school-fee policy context to the fee example.
needle = '''    <p class="reality-section-lead">
      本来、PTAは学校とは独立した任意団体です。しかし、給食費や教材費などの学校徴収金と同じ案内・同じ口座・同じ引落しの中でPTA会費が扱われると、保護者から見て学校費用とPTA会費の境界が分かりにくくなります。加入の有無、会費徴収の根拠、停止手続を分けて確認する必要があります。
    </p>'''
addition = needle + '''
    <p>2025年の文部科学省通知は、学校給食費以外の学校徴収金について、地方公共団体による公会計化に加え、学校を経由しない保護者から業者等への直接支払も示しています。PTA会費を直接規律する通知ではありませんが、学校教育に必要な費用ですら学校外へ移す政策方向との対比で、PTA会費を学校が恒常的に扱う根拠を確認します。</p>'''
s = replace_once(s, needle, addition, "2025 fee context")

extra_css = '''
<style id="reality-editorial-20260710">
.reality-editorial .reality-hero{text-align:left!important;background:linear-gradient(90deg,rgba(5,17,31,.82),rgba(5,17,31,.38)),url('assets/slides/1.jpg') center/cover!important}
.reality-editorial .reality-hero-kicker{padding:0!important;border:0!important;border-radius:0!important;background:transparent!important;animation:none!important;color:#f4e7a6!important}
.reality-editorial .reality-hero-kicker::before{display:none!important}
.reality-editorial .reality-hero-lead{margin-inline:0!important;max-width:820px!important}
.reality-editorial .editorial-section,.reality-editorial .reality-section>.wrap,.reality-editorial .reality-summary>.wrap{width:min(calc(100% - 40px),920px)!important;margin-inline:auto!important}
.reality-editorial .reality-intro{padding:58px 0!important;border-bottom:1px solid #dbe4ee!important}
.reality-editorial .reality-section{padding:68px 0!important}
.reality-editorial .section-badge,.reality-editorial .doc-mockup-label,.reality-editorial .law-box-label,.reality-editorial .incident-box-label,.reality-editorial .edu-quote-source{display:block!important;padding:0!important;border:0!important;border-radius:0!important;background:transparent!important;color:#6b7280!important;letter-spacing:.04em!important;text-transform:none!important}
.reality-editorial .doc-mockup,.reality-editorial .problem-note,.reality-editorial .good-note,.reality-editorial .law-box,.reality-editorial .edu-quote,.reality-editorial .incident-box{border-radius:0!important;box-shadow:none!important}
.reality-editorial .doc-mockup{background:#fff!important;border:1px solid #cfd8e2!important;border-left:5px solid #b78b2d!important}
.reality-editorial .problem-notes{gap:0!important;border-top:1px solid #dbe4ee!important}
.reality-editorial .problem-note,.reality-editorial .good-note{background:#fff!important;border:0!important;border-bottom:1px solid #dbe4ee!important;padding:15px 0!important;color:#26384b!important}
.reality-editorial .problem-note-text,.reality-editorial .good-note-text{color:#26384b!important;font-weight:500!important}
.reality-editorial .law-box,.reality-editorial .edu-quote,.reality-editorial .incident-box{background:#f6f8fa!important;color:#26384b!important;border:0!important;border-left:5px solid #1e3a5f!important;padding:22px 24px!important}
.reality-editorial .law-box-content,.reality-editorial .edu-quote blockquote,.reality-editorial .incident-box-body{color:#26384b!important}
.reality-editorial .edu-quote blockquote::before{display:none!important}
.reality-editorial .flow-box{border-radius:0!important;box-shadow:none!important}
.reality-editorial .flow-problem-note{border-radius:0!important;background:#f6f8fa!important;border-left:5px solid #b78b2d!important}
.reality-editorial .timeline{padding-left:0!important;border-top:1px solid #dbe4ee!important}
.reality-editorial .timeline::before,.reality-editorial .timeline-dot{display:none!important}
.reality-editorial .timeline-item{padding:20px 0!important;border-bottom:1px solid #dbe4ee!important}
.reality-editorial .reality-summary{padding:58px 0!important;background:#f5f7f9!important;border-top:1px solid #dbe4ee!important}
.reality-editorial .reality-summary h2{font-family:'Noto Serif JP',serif;color:#0f2742;margin:0 0 14px}
.reality-editorial .reality-summary p{line-height:2;margin:0;color:#334155}
@media(max-width:640px){.reality-editorial .editorial-section,.reality-editorial .reality-section>.wrap,.reality-editorial .reality-summary>.wrap{width:min(calc(100% - 30px),920px)!important}}
</style>
'''
s = replace_once(s, "</head>", extra_css + "</head>", "editorial css")

p.write_text(s, encoding="utf-8")
