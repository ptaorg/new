from pathlib import Path

p = Path(__file__).resolve().parents[1] / 'personnel.html'
text = p.read_text(encoding='utf-8')

replacements = {
    '<body>': '<body class="personnel-editorial">',
    '<div class="page-hero-kicker">👩‍🏫 Issue 04 — Personnel</div>': '<div class="page-hero-kicker">教職員関与・服務管理</div>',
    '<p>勤務時間中に教職員がPTA内部事務を担う運用は、地方公務員法第35条の職務専念義務との関係で確認が必要です。学校側の基本的な接点は「渉外業務（学校↔PTA間の連絡調整）」であり、名簿管理・会費処理・役員事務とは分けて整理する必要があります。</p>': '<p>勤務時間中に教職員がPTA関連作業を行う場合は、その作業が校務として特定されているか、職務命令があるか、職務専念義務免除や兼職等の根拠があるか、実際の内容が学校の連絡調整かPTA内部事務かを分けて確認します。</p>',
    '<p>学校行事や施設利用に必要な範囲の連絡は、渉外的な対応として整理できます。</p>': '<p>学校行事、施設利用、安全管理等に必要な連絡は、学校の職務として位置付けられている範囲を確認します。</p>',
    '<p>PTA会計、名簿、役員選出、会費徴収はPTA側で完結させるべき事務です。</p>': '<p>PTA会計、会員名簿、役員選出、会費徴収はPTA内部事務です。学校が関与する場合は、個別の職務上の根拠を確認します。</p>',
    '<p>「担任の先生がPTA封筒を配ってくれる」「事務室で会費の集計をしてもらっている」——多くの学校でこれが当たり前になっていますが、これらは<strong>地方公務員法第35条（職務専念義務）との関係で、職務上の根拠を確認すべき行為</strong>です。悪意があったわけではなく、長年の慣行として定着してきたものですが、制度上の線引きは必要です。このページでは、何が問題なのか・何はよくて何はダメなのか・どう改善するかを整理します。</p>': '<p>「担任がPTA文書を配布・回収する」「事務室がPTA会費を処理する」といった運用は、慣行だけで学校職務になるものではありません。地方公務員法第35条との関係では、作業の内容、校務としての位置付け、職務命令、職専免等の有無を文書で確認する必要があります。このページでは、連絡調整とPTA内部事務を分け、確認すべき根拠と移行方法を整理します。</p>',
    '<p>税金で支払われる勤務時間を、任意団体（PTA）の事務に充てることが問題の核心です。</p>': '<p>問題の核心は、勤務時間中の作業が当該地方公共団体の職務として位置付けられているか、それともPTAという別団体の内部事務なのかを確認できることです。</p>',
    '<p>PTAは学校とは別の任意団体です。教職員が勤務時間中にPTA内部事務を担う運用は、職務専念義務や公私分離の観点から確認が必要な<strong>便宜供与</strong>の問題になります。</p>': '<p>PTAは学校とは別の任意団体です。教職員が勤務時間中にPTA内部事務を担う場合は、校務としての位置付け、職務命令、職専免等の根拠、学校による便宜供与の範囲を確認します。</p>',
    '<h2>行政実例：「PTA事務は職務に含まれない」</h2>': '<h2>行政実例が示す、学校職務と任意団体事務の区別</h2>',
    '<p>この点は、法令の解釈として1960年代から一貫して確認されています。</p>': '<p>昭和39年の行政実例は、PTA等の任意団体の事務と教職員の職務上の事務を区別する資料の一つです。現在の具体的な運用は、現行の条例・規則、学校管理規則、職務命令、職専免等と合わせて確認します。</p>',
    '<p>この行政実例は、現在の運用を点検する際にも重要な手掛かりになります。当委員会が整理している教育委員会回答の中にも、<strong>PTA内部事務と学校職務を分けて考える趣旨の回答</strong>があります。「昔からやっていた」「暗黙の了解だった」は法的な正当化根拠にはなりません。</p>': '<p>この行政実例は、現在の運用を点検する際の重要な手掛かりです。ただし、個々の作業が学校職務に当たるかは、作業内容と現在の職務規程等に基づいて判断します。「昔から行っていた」「暗黙の了解だった」だけでは、職務上の根拠を説明したことにはなりません。</p>',
    '<p>地方公務員法第35条ただし書き・各自治体の条例に基づき、一定の場合には「職務に専念する義務の特例（服務免除）」が認められることがあります。ただし、この制度を使うためには条例・規則の根拠が必要で、PTAへの日常的な関与を包括的に免除することはできません。「服務免除を取れば問題ない」というわけでなく、その範囲と手続きが厳格に問われます。</p>': '<p>地方公務員法第35条ただし書きと各自治体の条例・規則により、一定の場合に職務専念義務が免除されることがあります。PTA関係で適用する場合は、対象者、用務、日時、承認権者、申請・承認記録を確認します。包括的・恒常的な取扱いが可能かは、各自治体の規定と実際の承認内容によります。</p>',
    '<h2>何はOKで、何はNGか</h2>': '<h2>学校の連絡調整とPTA内部事務を分ける</h2>',
    '✅ 渉外業務として許容される範囲': '学校職務として説明しやすい連絡調整',
    '❌ 渉外業務を超える・問題ある関与': 'PTA内部事務として個別の根拠確認が必要な作業',
    '担任がPTA封筒・配布物を配布・回収する': '担任がPTA入会届、会員向け文書、役員選出文書を恒常的に配布・回収する',
    '学校名簿をPTAに提供する（個人情報保護法69条にも抵触）': '学校名簿をPTAに提供・閲覧させる（個人情報保護法69条等の根拠確認が必要）',
    '勤務時間中にPTA関係の電話・メール対応をする': 'PTAの会員管理、会計、役員選出等の内部事務に関する電話・メール対応をする',
    '<p>「校長がPTA会長」「教頭がPTA副会長」という状態は各地で見られますが、これは複数の問題をはらんでいます。</p>': '<p>校長、教頭、教員がPTAの副会長、会計、書記等を兼ねる例があります。この場合は、学校職務上の立場とPTA役員としての立場を分け、次の点を確認します。</p>',
    '<li>勤務時間中の役員活動が職務専念義務違反になる（地公法35条）</li>': '<li>勤務時間中の役員活動について、校務、職務命令、職専免等の根拠があるか</li>',
    '<li>学校の公的権限とPTAの私的意思決定が混同される（社会教育法上の独立性の毀損）</li>': '<li>学校の公的権限とPTAの私的意思決定が混同されていないか</li>',
    '<li>「校長に反対できない」という心理的圧力が保護者に生じ、任意加入の実質を損なう</li>': '<li>管理職の役職が、加入や議決に対する心理的圧力を生じさせていないか</li>',
    '<p>社会教育法第12条の精神（行政からの自主性）からも、教職員がPTAの意思決定機関の中核を担うことは望ましくありません。</p>': '<p>社会教育法第12条との関係でも、行政・学校による統制的支配とならないよう、学校の公的権限とPTAの自主的意思決定を分ける役割設計が必要です。</p>',
    '会費管理にはクラウド会計ツール、配布物配付にはPTA役員による配付体制など、学校に依存しない方法を検討します。「不可能」なものはほとんどなく、ほぼすべてPTA側で担えます。': '会費管理、会員連絡、総会資料、役員選出等について、学校に依存しない方法を検討します。PTA内部事務の多くは、PTA側の口座、連絡手段、会計・会員管理体制へ移すことができます。',
    '「法令上の問題があるため、1年かけて切り離す」と校長に伝えます。教育委員会も同様の問題認識を持っているケースが多く、指針を共有することで協力を得やすくなります。': '現行運用の職務上の根拠を確認し、PTA内部事務を段階的にPTA側へ移す計画を、校長・教育委員会・PTAで共有します。',
    '学校とPTAの間で「渉外窓口覚書」を作成し、接点の範囲を明示します。これが適正化の完成形です。': '学校とPTAの連絡窓口、学校が扱う事項、PTAが自ら処理する内部事務、施設・情報・会計の責任範囲を文書化します。',
}

for old, new in replacements.items():
    if old not in text:
        raise SystemExit(f'marker not found: {old[:120]}')
    text = text.replace(old, new, 1)

style = r'''
<style id="personnel-editorial-20260710">
body.personnel-editorial .page-banner,
body.personnel-editorial .hero-actions{
  display:none!important;
}
body.personnel-editorial .page-hero-kicker,
body.personnel-editorial .section-kicker,
body.personnel-editorial .scope-label{
  text-transform:none!important;
  letter-spacing:.03em!important;
  border-radius:3px!important;
}
body.personnel-editorial .pg-main{
  width:min(calc(100% - 40px),920px)!important;
  padding:68px 0 96px!important;
}
body.personnel-editorial .pg-section,
body.personnel-editorial .editorial-panel,
body.personnel-editorial .editorial-brief{
  margin:0!important;
  padding:40px 0 46px!important;
  background:#fff!important;
  border:0!important;
  border-top:1px solid #cfd8e2!important;
  border-radius:0!important;
  box-shadow:none!important;
}
body.personnel-editorial .editorial-brief-grid,
body.personnel-editorial .scope-grid{
  display:block!important;
}
body.personnel-editorial .editorial-brief-point,
body.personnel-editorial .scope-ok,
body.personnel-editorial .scope-ng{
  margin:0!important;
  padding:20px 0!important;
  background:#fff!important;
  border:0!important;
  border-top:1px solid #dbe4ee!important;
  border-radius:0!important;
  box-shadow:none!important;
}
body.personnel-editorial .scope-grid > div:last-child,
body.personnel-editorial .editorial-brief-point:last-child{
  border-bottom:1px solid #dbe4ee!important;
}
body.personnel-editorial .scope-label{
  color:#17345c!important;
}
body.personnel-editorial .ok-dot,
body.personnel-editorial .ng-dot{
  color:#64748b!important;
}
body.personnel-editorial .alert,
body.personnel-editorial .law-quote,
body.personnel-editorial .ed-resource-list > div{
  border-radius:0!important;
  box-shadow:none!important;
}
body.personnel-editorial main a:hover{
  transform:none!important;
  box-shadow:none!important;
}
@media(max-width:700px){
  body.personnel-editorial .pg-main{
    width:min(calc(100% - 30px),920px)!important;
  }
}
</style>
'''
if 'personnel-editorial-20260710' not in text:
    text = text.replace('</head>', style + '</head>', 1)

p.write_text(text, encoding='utf-8')
