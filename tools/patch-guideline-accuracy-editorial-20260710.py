from pathlib import Path

path = Path(__file__).resolve().parents[1] / "guideline.html"
text = path.read_text(encoding="utf-8")

replacements = {
    '<body>': '<body class="guideline-editorial">',
    '<div class="page-banner-kicker">Operational Guideline · 実務ガイドライン</div>': '<div class="page-banner-kicker">PTA運営の実務基準</div>',
    '<div class="gl-problem-desc">学校徴収金とPTA会費の一体徴収。会費支払いの任意性が失われ、事実上の強制となっている。</div>': '<div class="gl-problem-desc">学校徴収金とPTA会費を同じ案内、口座、引落し、未納管理で扱うと、学校費用と任意団体会費の区別が困難になり、加入・支払意思の確認が不明確になります。</div>',
    '<div class="gl-problem-desc">教育目的で収集した保護者名簿のPTAへの提供。個人情報保護法第69条違反の可能性。</div>': '<div class="gl-problem-desc">学校保有情報をPTA会員管理等に使う場合は、学校自身による目的外利用かPTAへの提供かを分け、個人情報保護法第61条・第69条の根拠を確認します。</div>',
    '<div class="gl-principle-desc">PTAは保護者に対し、加入が任意であること・退会の自由・会費の使途・個人情報の取扱いを正確かつ透明に説明する義務を負います。情報の非対称性を利用した事実上の強制は許されません。</div>': '<div class="gl-principle-desc">加入が任意であること、退会方法、会費額と使途、個人情報の取扱いを加入前に示し、本人が判断できる状態を整えます。学校手続と一体化させて誤認を生じさせないことが重要です。</div>',
    '<div class="gl-principle-desc">PTAは学校から独立した社会教育関係団体です。学校がPTAの運営を管理・統制することは社会教育法第12条で禁じられています。教職員のPTA業務への関与は地方公務員法第35条に抵触します。</div>': '<div class="gl-principle-desc">PTA内部の自主的運営と、学校が情報、会計、教職員、施設、配布媒体を提供する行為は分けて確認します。教職員が勤務時間中に関与する場合は、校務としての位置付け、職務命令、職専免、兼職兼業等の根拠を確認します。</div>',
    '<div class="gl-principle-law">根拠：社会教育法第12条、地方公務員法第35条</div>': '<div class="gl-principle-law">確認資料：社会教育法、地方公務員法、自治体の服務・職専免規則</div>',
    '<p>すべての加入は<strong>書面の入会申込書</strong>による本人（保護者）の署名・捺印が必要です。入学時に一括配布し、回収できた分のみを会員として取り扱います。未回収＝非加入として扱うことを明確にしてください。</p>': '<p>加入は、紙の入会申込書、電子フォーム、署名済み加入届、オンライン申込ログ等により、本人の申込みを客観的に確認できる記録を残します。押印は必須ではありません。申込みを確認できた人だけを会員として扱い、未提出・未送信を加入とみなさないことを明確にしてください。</p>',
    '<p>退会届は年度途中でも受け付けてください。<strong>「年度末にしか退会できない」という規約条項は、任意団体からの脱退の自由との関係で効力が争われる可能性が高い条項</strong>です（民法第680条等）。退会後は該当会員の個人情報を速やかに削除・廃棄します。</p>': '<p>退会の申出を受け付ける時期、効力発生日、会費精算、活動上必要な引継ぎを会則で明確にします。退会を不合理に制限する条項は、任意加入の説明と整合するかを見直します。退会後の個人情報は、会計・紛争対応・法令上の保存等に必要な記録を除き、利用目的に照らして削除・廃棄します。</p>',
    '<li>退会後の残余会費は按分で返金することが原則</li>': '<li>退会後の会費精算は、会則、会費の対象期間、既支出額、返金規定を事前に示す</li>',
    '<p>PTAが必要とする個人情報（住所・電話番号・メールアドレス等）は、<strong>入会申込書によって本人から直接収集</strong>してください。学校が収集した情報の流用は個人情報保護法第69条違反です。</p>': '<p>PTAが必要とする個人情報は、利用目的と項目を示し、入会申込書や電子フォーム等により本人から直接取得することを基本とします。学校保有情報を使う場合は、学校自身による利用かPTAへの提供かを分け、個人情報保護法第61条・第69条の根拠、対象項目、記録を確認します。</p>',
    '<p>学校が収集した保護者名簿のPTAへの提供は、<strong>保護者の同意がない限り個人情報保護法第69条（目的外提供の禁止）違反</strong>です。学校側から「今まで通り提供する」と言われても、法令遵守の観点から受け取りを断ることが適切です。</p>': '<p>学校が収集した保護者情報をPTAへ提供する場合は、個人情報保護法第69条第2項等の具体的根拠、利用目的、提供項目、提供先、本人への説明、提供記録を確認します。恒常的な会員管理のために慣行だけで受け取らず、PTAが本人から直接取得できる情報は直接取得へ移します。</p>',
    '<p>非加入者の個人情報をPTAが保有する根拠はありません。「会員かどうか確認するため」として非加入者の情報を管理することも認められません。会員リスト＝入会申込書提出者のみとして管理してください。</p>': '<p>PTAは、学校の全保護者名簿を基礎に包括的な「非会員名簿」を作成しないことを基本とします。会員管理は入会申込記録を基礎とし、問い合わせ、誤徴収防止、退会処理等に必要な最小限の記録を保有する場合は、目的、項目、保存期間、閲覧者を定めます。</p>',
    '<strong>△ 「在学をもって会員とみなす」規約は成立根拠を確認</strong><br>\n            民法第522条では、契約は申込みと承諾によって成立します。在学という事実だけで直ちに入会が成立するとは限りません。一方、会費納入などの具体的事情から黙示の合意が認定される場合もあるため、加入意思、会費、個人情報利用を分けて記録します。': '<strong>「在学をもって会員とみなす」方式は、入会申込みの記録にならない</strong><br>\n            学校への在学、PTAからの一方的な通知、保護者の沈黙だけで、PTA加入の申込みを確認することはできません。個別紛争では後日の行為が証拠として検討されることがありますが、それは恒常的なみなし加入制度を正当化するものではありません。制度としては、本人の積極的な申込みを記録するオプトイン方式へ移行します。',
    '給食費・教材費などの学校徴収金と同じ口座引き落としでPTA会費を徴収すると、保護者はPTA会費の支払いを拒否できないと誤認します。これは消費者契約法上の「不当勧誘」類似の問題を生じさせます。PTA会費は独立した手段で徴収してください。': '給食費・教材費などの学校徴収金と同じ案内、口座、引落し、未納管理でPTA会費を扱うと、保護者は学校費用と任意団体会費を区別しにくくなります。加入申込み、会費請求、徴収主体、会計を学校徴収金から分離してください。',
    '<p>学校口座での一括徴収を止め、PTA独自の口座振替または現金徴収に切り替えてください。口座振替を利用する場合は、<strong>会員との間で個別に委任状（口座振替委任状）を締結</strong>することが必要です。</p>': '<p>PTA会費を設ける場合は、年会費、事業ごとの実費負担、寄付・カンパ等の方法を活動内容に応じて選び、会費額と使途を加入前に示します。徴収はPTA名義の口座、決済サービス、現金等を用いてPTA自身が行い、口座振替を使う場合は金融機関・決済事業者が求める振替承認を加入者から直接取得します。</p>',
    '<li>委任状は退会時に効力を失うことを明記する</li>': '<li>退会・会費変更時の振替停止手続と処理期限を明記する</li>',
    '<p>担任の先生がPTA会費を集金することは、<strong>地方公務員法第35条（職務専念義務）違反の疑い</strong>があります。PTAは独自の役員・保護者が徴収を行うことが原則です。学校の事務室でPTA会費を管理することも同様の問題があります。</p>': '<p>教職員が勤務時間中にPTA会費の集金、振替データ作成、未納確認、督促、返金、会計処理を行う場合は、その作業が校務として特定されているか、職務命令、職専免、兼職兼業、学校会計規程等の根拠があるかを確認します。根拠が明確でない恒常的運用は、PTA自身の徴収・会計へ移行します。</p>',
    '<strong>❌ 未加入者への会費徴収は不当利得</strong><br>\n            入会申込書を提出していない保護者からPTA会費を徴収することは、法的根拠のない金銭の取得（民法第703条の不当利得）にあたります。徴収済みの場合は返金が必要です。': '<strong>未加入者・加入記録を確認できない人からの徴収は、根拠確認が必要</strong><br>\n            入会申込み、PTAの承諾、会費額、支払経緯を確認できない場合は、徴収根拠を調査し、誤徴収であれば返金方法を示します。返還義務の有無と範囲は、契約成立、本人の認識、支払経緯、会則、既支出等の個別事情を踏まえて検討します。',
    '<p>PTA非会員の保護者の子どもを、学校行事や教育活動において<strong>会員の子どもと差別的に扱うことは教育基本法第4条が禁じる差別</strong>にあたります。卒業記念品の配布除外・行事への参加禁止等は許されません。</p>': '<p>学校は、保護者のPTA加入・非加入を理由に、児童生徒の教育活動、学校行事、学校生活上の取扱いへ不利益を生じさせてはなりません。PTA独自の給付や記念品についても、児童生徒を通じて加入圧力が生じないよう、対象、財源、実費負担、学校行事との区分を事前に整理します。</p>',
    '<p>PTAの会員でない保護者に対し、役員への就任を強制することはできません。また、会員であっても役員就任の強制は結社の自由を侵害する可能性があります。役員選出は自発的な立候補や公正な選挙で行ってください。</p>': '<p>PTAの会員でない保護者に、PTA会則上の役員義務を課すことはできません。会員についても、役員候補の選出方法、辞退手続、本人同意、任期、負担内容を明示し、くじや推薦だけで就任を確定させない運用へ改めます。</p>',
    '<p>旗振り当番（登下校の安全見守り）・ベルマーク収集・トイレ清掃等、PTAが担ってきた活動の中には<strong>本来学校・行政が責任を持つべきもの</strong>が含まれています。これらをPTA活動として継続することは、学校の責任を曖昧にさせます。教育委員会・学校との間で役割分担を明確化してください。</p>': '<p>旗振り当番、登下校見守り、清掃、資源回収等は、活動ごとに主催者、法的責任、安全管理、保険、参加の任意性、学校教育活動との区分を確認します。地域・保護者の自主活動として行えるものと、学校または行政が責任を負う業務を一括りにせず、役割分担を文書化してください。</p>',
    '□ 非会員情報をPTAが把握・管理しないこと': '□ 学校名簿を基礎とする包括的な非会員名簿を作らず、必要な最小限の処理記録は目的・保存期間を定めること',
    '収集は入会申込書による本人の書面同意を\n得た上で行う。学校が収集した個人情報の提供を\n受けることは行わない。': '収集は入会申込書、電子フォーム等により本人へ\n利用目的を示し、必要な意思確認を得た上で行う。\n学校保有情報は、学校側の利用・提供根拠と本会側の\n利用目的を確認できない限り受け取らない。',
    '退会届受理後、遅滞なく（概ね1ヶ月以内）\n当該会員の個人情報を削除または廃棄し、\n本人に完了を通知する。': '退会届受理後、会計・紛争対応・法令上の保存等に\n必要な記録を除き、利用目的を失った個人情報を\n保存期間に従って削除または廃棄する。',
}

for old, new in replacements.items():
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"Expected one marker, found {count}: {old[:100]}")
    text = text.replace(old, new)

fee_marker = '''          <div class="gl-box">\n            <h4>✅ 教職員によるPTA会費の代行徴収は廃止する</h4>'''
fee_notice = '''          <div class="gl-box gl-policy-note">\n            <h4>2025年通知が示した学校徴収金政策を確認する</h4>\n            <p>文部科学省の2025年通知は、学校給食費以外の学校徴収金について、公会計化して地方公共団体が徴収・管理する方法だけでなく、保護者が業者等へ直接支払い、学校を経由しない方法も正式に示しました。</p>\n            <p>この通知はPTA会費を直接規律するものではありません。しかし、学校教育に必要な費用ですら徴収・管理を学校の外へ移す政策方向にあることは重要です。学校教育に必要な費用ではないPTA会費を学校が恒常的に扱う場合は、学校の事務権限、個人情報利用、会計区分、職務負担について、より強い固有の説明が必要です。</p>\n          </div>\n\n          <div class="gl-box">\n            <h4>✅ 教職員によるPTA会費の代行徴収は廃止する</h4>'''
if text.count(fee_marker) != 1:
    raise SystemExit(f"Fee notice marker count: {text.count(fee_marker)}")
text = text.replace(fee_marker, fee_notice)

style = '''
<style id="guideline-editorial-20260710">
body.guideline-editorial main > .wrap:first-child{
  display:none!important;
}
body.guideline-editorial .section-kicker{
  display:none!important;
}
body.guideline-editorial .gl-wrap,
body.guideline-editorial main > section > .wrap{
  width:min(calc(100% - 40px),920px)!important;
  max-width:920px!important;
}
body.guideline-editorial .gl-problem-grid,
body.guideline-editorial .gl-principle-grid,
body.guideline-editorial .gl-pack-grid{
  display:block!important;
}
body.guideline-editorial .gl-problem-card,
body.guideline-editorial .gl-principle-card,
body.guideline-editorial .gl-box,
body.guideline-editorial .gl-ng-box,
body.guideline-editorial .gl-notice,
body.guideline-editorial .gl-request-item,
body.guideline-editorial .gl-pack-card{
  margin:0!important;
  padding:22px 0!important;
  background:#fff!important;
  color:#26384e!important;
  border:0!important;
  border-top:1px solid #dbe4ee!important;
  border-radius:0!important;
  box-shadow:none!important;
}
body.guideline-editorial .gl-problem-card:last-child,
body.guideline-editorial .gl-principle-card:last-child,
body.guideline-editorial .gl-box:last-child,
body.guideline-editorial .gl-pack-card:last-child{
  border-bottom:1px solid #dbe4ee!important;
}
body.guideline-editorial .gl-problem-icon,
body.guideline-editorial .gl-principle-icon{
  display:none!important;
}
body.guideline-editorial .gl-problem-title,
body.guideline-editorial .gl-principle-title,
body.guideline-editorial .gl-principle-desc,
body.guideline-editorial .gl-principle-law{
  color:#17345c!important;
}
body.guideline-editorial .gl-principle-num{
  color:#7a5a12!important;
  text-transform:none!important;
  letter-spacing:.03em!important;
}
body.guideline-editorial .gl-panel-heading{
  padding-left:0!important;
  padding-bottom:10px!important;
  border-left:0!important;
  border-bottom:2px solid #17345c!important;
}
body.guideline-editorial .gl-law-cite,
body.guideline-editorial .gl-pack-basis li,
body.guideline-editorial .gl-copy-btn,
body.guideline-editorial .gl-pack-action a{
  border-radius:3px!important;
}
body.guideline-editorial .gl-tpl-item,
body.guideline-editorial .gl-tpl-pre{
  border-radius:0!important;
  box-shadow:none!important;
}
body.guideline-editorial .gl-policy-note{
  border-top:3px solid #c6a34b!important;
  border-bottom:1px solid #c6a34b!important;
  padding:24px 0!important;
}
body.guideline-editorial main a:hover{
  transform:none!important;
  box-shadow:none!important;
}
@media(max-width:700px){
  body.guideline-editorial .gl-wrap,
  body.guideline-editorial main > section > .wrap{
    width:min(calc(100% - 30px),920px)!important;
  }
}
</style>
'''
if 'guideline-editorial-20260710' in text:
    raise SystemExit('Editorial style already present')
text = text.replace('</head>', style + '</head>', 1)

required = [
    '2025年通知が示した学校徴収金政策を確認する',
    '学校を経由しない方法も正式に示しました',
    '会費を設ける場合は、年会費、事業ごとの実費負担、寄付・カンパ等',
    'guideline-editorial-20260710',
]
for item in required:
    if item not in text:
        raise SystemExit(f'Missing required text: {item}')

path.write_text(text, encoding='utf-8')
