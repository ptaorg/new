from pathlib import Path

p = Path(__file__).resolve().parents[1] / 'facilities.html'
text = p.read_text(encoding='utf-8')

replacements = {
    '<body>': '<body class="facilities-editorial">',
    '<div class="page-hero-kicker">🏫 Issue 05 — Facilities</div>': '<div class="page-hero-kicker">学校施設・公有財産管理</div>',
    '<p>PTA室・印刷機・光熱費・鍵——学校という「公の場」を任意団体（私）が使うことには、学校教育法第137条に基づく許可と費用負担の整理が必要です。</p>': '<p>学校教育法第137条は、学校教育上の支障がない限り、学校施設を社会教育その他公共のために利用させることができると定めています。PTAに当然の使用権を与える規定ではなく、具体的な許可権者、手続、使用条件、費用、責任は自治体の条例・規則等に沿って確認します。</p>',
    '学校施設は、地方公共団体が管理する「公物」です。任意団体であるPTAが学校の施設・備品・電気を使う場合、そこには必ず<strong>正式な許可・費用負担・責任の明確化</strong>が必要です。「ずっとこうだった」「学校が許可してくれた」というだけでは、地方自治法上の公有財産管理や地方財政法上の問題は解消されません。このページでは、施設利用に関する公私の境界と、具体的な適正化の進め方を整理します。': '公立学校の施設・備品は、設置者である地方公共団体が管理する財産です。PTAが利用する場合は、使用目的、場所、時間、許可権者、管理責任、費用または免除の取扱いを、自治体の条例・規則・許可条件に沿って確認します。「従来から使っている」という慣行だけで、使用範囲や学校側の負担が確定するものではありません。',
    '<p>印刷費、光熱費、通信費、備品利用の負担が曖昧でないかを見ます。</p>': '<p>使用料、実費負担、減免・免除の根拠と決裁が記録されているかを見ます。</p>',
    '<p>学校設備をPTA費で補填する構造になっていないかを点検します。</p>': '<p>寄附の申出・受入手続と、学校予算をPTAへ定額・恒常的に肩代わりさせる構造を分けて点検します。</p>',
    '<p>問題の本質は「学校という公的空間に、任意団体という私的組織が境界なく入り込んでいること」です。財産の性格が根本的に異なります。</p>': '<p>学校とPTAは協力関係を持ち得ますが、学校施設・備品・職員・情報は公的管理の対象であり、PTA会費・会員情報・内部事務はPTA側の管理対象です。利用許可を介して接続し、境界を記録する必要があります。</p>',
    '<div class="wall-label">⚠️ ここが混ざると問題</div>': '<div class="wall-label">境界を確認すべき状態</div>',
    '<h4>学校のコピー機でPTA文書を印刷、光熱費をPTAが無償使用、教職員がPTA郵便を処理</h4>': '<h4>印刷機・光熱費・鍵・郵便・教職員事務の使用範囲と根拠が文書で確認できない</h4>',
    '<p>「学校教育上支障のない限り」「公共のために」という2つの条件が要件です。PTAはこれを根拠に施設を利用できますが、<strong>「利用できる」と「無制限に無償で使える」は別</strong>です。使用には①正式な使用許可、②費用負担の取り決め、③責任者の明示が最低限必要です。</p>': '<p>第137条は、学校側が一定の目的で施設利用を認めることができる根拠です。PTAに施設利用を請求できる権利を直接与えるものではありません。具体的には、教育上の支障、公共性、許可権者、使用目的、場所・時間、管理責任、費用または減免、取消し・停止条件を自治体の規定と許可文書で確認します。</p>',
    '<p>学校の施設・備品をPTAが継続的に使用する場合、無償利用が当然という前提ではなく、使用許可、使用範囲、費用負担、責任関係を確認する必要があります。</p>': '<p>無償利用が直ちに違法となるわけではありませんが、無償・減免を含め、許可権者と根拠規定、対象団体、使用範囲、管理責任を確認できなければなりません。</p>',
    '<h3>地方財政法と「割当的寄附」の問題</h3>': '<h3>学校への寄附は、受入手続と割当・強制の有無を分ける</h3>',
    '<div class="law-quote">\n        <div class="law-quote-label">地方財政法 第4条の5（寄附の強制禁止）</div>\n        国は、地方公共団体に対し、法令の規定に基づかず又は地方公共団体の自発的意思に基づかないで……寄附を行うことを強制してはならない。\n      </div>': '<div class="law-quote"><div class="law-quote-label">地方財政法第4条の5との関係</div>地方公共団体またはその機関が、住民に寄附金を割り当てて強制的に徴収するような運用となっていないかを確認します。</div>',
    '<p>PTAが学校の施設整備や備品購入に費用を拠出すること（例：PTA費でエアコン設置、印刷機購入）は、<strong>「割当的寄附」</strong>として地方財政法上問題になり得ます。学校が予算不足をPTAへの寄附で補填させる構造が固定化すると、この問題が顕在化します。このような場合は、寄附として処理できるかだけでなく、学校予算の不足を保護者団体に補わせる構造になっていないかを確認する必要があります。</p>': '<p>PTAから学校への寄附があるだけで、直ちに地方財政法第4条の5へ抵触するわけではありません。寄附者側の自発的申出、PTA内部の意思決定、自治体側の受入決裁、使途、資産計上を確認します。一方、学校や教育委員会が各家庭またはPTAへ一定額を割り当て、学校予算の不足を恒常的に補わせている場合は、行政の関与と強制性を具体的に確認します。</p>',
    '<p><strong>「善意の寄附」でも問題になる場合がある</strong></p>': '<p><strong>寄附の名称だけで判断しない</strong></p>',
    '<p>PTAが学校の設備整備に善意で寄附しても、それが実質的に<strong>学校が義務を負うべき費用をPTAに肩代わりさせている</strong>場合、地方財政法上の問題があります。PTAの規約に「学校への寄附」が明記されていても、強制加入・割当的性格があれば正当化されません。</p>': '<p>寄附と記載されていても、学校側からの要請、金額の割当、非加入・不払いへの圧力、毎年度の予算化、学校経費の恒常的肩代わりがある場合は、自発性と受入手続を確認します。PTA規約の記載だけで、行政側の手続や強制性の問題が解消されるものではありません。</p>',
    '<p>学校教育法137条関係の資料は、PTA利用を許すか否かだけを決める資料ではありません。学校教育上の支障がないか、使用目的が特定されているか、費用負担と責任主体が明確かを、許可条件として文章化するために使います。</p>': '<p>学校教育法137条は、PTAに当然の使用権を認める条文ではありません。教育上の支障、使用目的、公共性、許可権者、場所・時間、費用または減免、責任主体、取消し・停止条件を許可文書へ落とし込むために使います。</p>',
    '<div class="source-lens-item"><strong>費用負担</strong><p>印刷費、用紙代、光熱費、通信費、備品利用の負担方法を決めているか。</p></div>': '<div class="source-lens-item"><strong>費用・減免</strong><p>使用料、印刷費、用紙代、光熱費等の負担、減免・免除の根拠と決裁を定めているか。</p></div>',
    '<div class="source-lens-item"><strong>停止条件</strong><p>みなし加入、抱合せ徴収、名簿流用、教職員事務代行がある場合、施設協力を見直す条件を置いているか。</p></div>': '<div class="source-lens-item"><strong>見直し・停止条件</strong><p>施設利用や学校協力が、みなし加入、抱合せ徴収、学校名簿流用、教職員による内部事務代行を支える状態となった場合に、許可目的・条件、公私分離、教育上の支障の観点から見直しまたは一時停止できるか。</p></div>',
    '<p style="font-weight:800;margin-bottom:4px">適切な覚書の内容</p>': '<p style="font-weight:800;margin-bottom:4px">確認すべき条項</p>',
    '<li>光熱費の実費負担額・精算方法</li>': '<li>使用料・実費・減免・免除の取扱い</li>',
    '<p style="font-weight:800;margin-bottom:4px">問題のある覚書の内容</p>': '<p style="font-weight:800;margin-bottom:4px">別の根拠確認が必要な条項</p>',
    '<li>「学校職員がPTA事務を補助する」という条項</li>': '<li>学校職員によるPTA内部事務を当然の職務としている条項</li>',
    '<li>「学校印刷機を無償使用できる」という条項</li>': '<li>学校印刷機等の使用範囲・費用・管理責任が不明な条項</li>',
    '<li>「PTAが鍵を常時保管する」という条項</li>': '<li>鍵の管理権限、返却、事故時対応が不明な条項</li>',
    '<li>費用負担の定めがなく無償使用を固定化</li>': '<li>無償・減免の根拠と決裁を示さず固定化する条項</li>',
    '<li>PTAから学校への恒常的な備品寄附の取り決め</li>': '<li>学校予算をPTAへ定額・恒常的に肩代わりさせる条項</li>',
    '<p>覚書を作成する際は、地方自治法・地方財政法の観点から内容を精査し、教育委員会の指導も受けることを推奨します。</p>': '<p>覚書を作成する際は、自治体の財産管理規則、学校施設使用規程、使用料・減免規定、服務・個人情報・寄附受入手続と整合しているかを確認します。</p>',
    '<span class="badge badge-ok">OK</span>': '<span class="badge badge-ok">確認済</span>',
    '<span class="badge badge-ng">NG</span>': '<span class="badge badge-ng">要是正</span>',
    '<span class="badge badge-warn">要注意</span>': '<span class="badge badge-warn">要確認</span>',
    '使用料を学校に支払う、またはPTA専用機を持つ': '許可条件・自治体規則に従い、費用負担または減免を記録する',
    '学校の機器を無償で恒常使用': '使用許可・費用・管理責任の根拠が不明',
    '使用量に応じた費用負担の取り決めあり': '費用負担または減免・免除の根拠と決裁がある',
    '学校が全額負担、費用精算なし': '学校負担の根拠・決裁が確認できない',
    '年1回程度・入会案内など限定的な範囲': '配布目的・対象・学校関与の根拠とPTA文書であることを明示',
    '毎月の学校通知にPTA文書を常態的に同封': '入会・会員管理・役員選出文書を学校文書として恒常配布',
    '自発的・単発・少額のもの（校長への贈り物等）': '寄附申出、PTA内部決定、自治体の受入決裁、使途を確認',
    '予算不足の補填・恒常的な設備投資をPTAが担う': '学校予算の不足をPTAまたは各家庭へ定額・恒常的に割り当てる',
}

for old, new in replacements.items():
    if old not in text:
        raise SystemExit(f'marker not found: {old[:130]}')
    text = text.replace(old, new)

style = r'''
<style id="facilities-editorial-20260710">
body.facilities-editorial .page-banner,
body.facilities-editorial .hero-actions{
  display:none!important;
}
body.facilities-editorial .page-hero-kicker,
body.facilities-editorial .badge{
  text-transform:none!important;
  letter-spacing:.03em!important;
  border-radius:3px!important;
}
body.facilities-editorial .pg{
  width:min(calc(100% - 40px),920px)!important;
  padding:68px 0 96px!important;
}
body.facilities-editorial .pg > section,
body.facilities-editorial .editorial-panel,
body.facilities-editorial .editorial-brief{
  margin:0!important;
  padding:40px 0 46px!important;
  background:#fff!important;
  border:0!important;
  border-top:1px solid #cfd8e2!important;
  border-radius:0!important;
  box-shadow:none!important;
}
body.facilities-editorial .editorial-brief-grid,
body.facilities-editorial .safes{
  display:block!important;
}
body.facilities-editorial .editorial-brief-point,
body.facilities-editorial .safe-box,
body.facilities-editorial .alert{
  margin:0!important;
  padding:20px 0!important;
  background:#fff!important;
  border:0!important;
  border-top:1px solid #dbe4ee!important;
  border-radius:0!important;
  box-shadow:none!important;
}
body.facilities-editorial .editorial-brief-point:last-child,
body.facilities-editorial .safes > .safe-box:last-child{
  border-bottom:1px solid #dbe4ee!important;
}
body.facilities-editorial .wall,
body.facilities-editorial .law-quote{
  border-radius:0!important;
  box-shadow:none!important;
}
body.facilities-editorial .check-table .badge-ok,
body.facilities-editorial .check-table .badge-ng,
body.facilities-editorial .check-table .badge-warn{
  background:transparent!important;
  color:#17345c!important;
  border:1px solid #94a3b8!important;
}
body.facilities-editorial main a:hover{
  transform:none!important;
  box-shadow:none!important;
}
@media(max-width:700px){
  body.facilities-editorial .pg{
    width:min(calc(100% - 30px),920px)!important;
  }
}
</style>
'''
if 'facilities-editorial-20260710' not in text:
    text = text.replace('</head>', style + '</head>', 1)

p.write_text(text, encoding='utf-8')
