from pathlib import Path

path = Path(__file__).resolve().parents[1] / "law-map.html"
text = path.read_text(encoding="utf-8")

replacements = {
    '<body class="law-page">': '<body class="law-page law-editorial">',
    '<div class="law-kicker">Legal Framework</div>': '<div class="law-kicker">PTAと学校関与の法制度</div>',
    '<div class="law-axis"><h3>入会手続</h3><div><span>憲法21条</span><span>民法521・522条</span><span>民法703条</span><span>消費者契約法</span></div></div>': '<div class="law-axis"><h3>入会手続</h3><div><span>憲法21条</span><span>民法521・522条</span><span>消費者契約法</span><span>申込記録・承諾記録</span></div></div>',
    '<div class="law-axis"><h3>個人情報</h3><div><span>個人情報保護法61・62・69条</span><span>地方公務員法34条</span><span>本人同意・提供記録</span></div></div>': '<div class="law-axis"><h3>個人情報</h3><div><span>個人情報保護法61・62・69条</span><span>学校自身の目的外利用</span><span>PTAへの提供</span><span>利用目的・例外根拠</span></div></div>',
    '<div class="law-axis"><h3>会費徴収</h3><div><span>民法113条</span><span>民法703条</span><span>地方財政法4条の5</span><span>学校徴収金会計</span></div></div>': '<div class="law-axis"><h3>会費徴収</h3><div><span>民法521・522条</span><span>個人情報保護法61・69条</span><span>学校の事務権限・決裁</span><span>2025年学校徴収金通知</span></div></div>',
    '<div class="law-axis"><h3>教職員関与</h3><div><span>地方公務員法30・35条</span><span>地方公務員法34条</span><span>教特法17条</span><span>職専免・兼職兼業</span></div></div>': '<div class="law-axis"><h3>教職員関与</h3><div><span>地方公務員法35条</span><span>校務としての位置付け</span><span>職務命令・職専免</span><span>兼職兼業</span></div></div>',
    '<div class="law-axis"><h3>施設利用</h3><div><span>学校教育法137条</span><span>学校管理規則</span><span>社会教育法12条</span><span>地方財政法4条の5</span></div></div>': '<div class="law-axis"><h3>施設利用</h3><div><span>学校教育法137条</span><span>自治体の財産管理規則</span><span>許可権者・使用条件</span><span>減免・寄附受入手続</span></div></div>',
    '<div class="law-card"><span class="tag">会費根拠</span><strong>民法113条・703条</strong><p>学校がPTA会費を請求・徴収するなら、誰の代理で、どの委任に基づき、どの会員に対して請求しているのかが問題になります。根拠がなければ返還・不当利得の論点に接続します。</p></div>': '<div class="law-card"><span class="tag">会費債務と学校関与</span><strong>民法521条・522条／個人情報保護法61条・69条</strong><p>PTA会費の請求は、本人の加入申込みとPTAの承諾が前提です。学校が徴収へ関与する場合は、学校保有口座情報の利用目的、学校の事務権限・決裁、会計区分、PTAからの依頼文書を分けて確認します。PTAから学校への依頼だけで、保護者の会費債務は生じません。</p></div><div class="law-card"><span class="tag">学校徴収金政策</span><strong>文部科学省2025年通知</strong><p>学校給食費以外の学校徴収金について、公会計化だけでなく、学校を経由しない直接支払まで示しました。PTA会費を直接規律する通知ではありませんが、学校教育に必要な費用ですら学校外へ移す政策方向を示す重要資料です。</p></div>',
    '<h3>3. 会費徴収</h3><p>PTA会費は学校徴収金ではありません。学校口座、学校徴収金通知、学校の未納管理に混ぜる場合、加入契約、委任、請求根拠、会計区分、返金処理を説明できる必要があります。</p>': '<h3>3. 会費徴収</h3><p>PTA会費は学校徴収金ではありません。まず加入契約と会費債務の成立を確認し、学校口座、学校徴収金通知、学校の未納管理へ混ぜる場合は、学校保有口座情報の利用目的、学校の事務権限・決裁、会計区分を確認します。文部科学省の2025年通知が、学校給食費以外の学校徴収金について公会計化と学校を経由しない直接支払を示したことは重要です。学校教育に必要な費用ですら学校外へ移す政策方向にある以上、PTA会費を学校が恒常的に扱うには、より強い固有の説明が必要です。</p>',
    '<h3>4. 教職員関与</h3><p>教職員が勤務時間中にPTAの名簿、会計、役員選出、配布回収、集金を担う場合、それが校務か、PTAの内部事務か、職専免か、兼職兼業かを分けて確認します。「校長判断」だけでは制度整理になりません。</p>': '<h3>4. 教職員関与</h3><p>教職員が勤務時間中にPTAの名簿、会計、役員選出、配布回収、集金を担う場合は、作業内容、校務としての位置付け、職務命令、職専免、兼職兼業を分けて確認します。校長判断という説明だけでなく、その判断を支える規則、決裁、対象者、時間、用務の記録が必要です。</p>',
    '<h3>5. 施設利用</h3><p>PTAの学校施設利用は、学校管理者の許可と条件設定の問題です。団体運営が任意加入・個人情報・会費の点で不適切な場合、学校は施設利用、校内配布、印刷、保管、児童経由回収の可否を再点検できます。</p>': '<h3>5. 施設利用</h3><p>学校教育法137条は、PTAに当然の使用権を与える規定ではありません。許可権者、使用目的、場所・時間、費用または減免、管理責任、取消し・停止条件を自治体規則と許可文書で確認します。施設利用や学校協力が、みなし加入、名簿流用、抱合せ徴収、教職員による内部事務代行を支える状態になった場合は、許可目的、公私分離、教育上の支障から見直しまたは一時停止を検討します。</p>',
    '<div class="law-caution"><strong>誤読3：</strong>同意欄があれば学校情報をPTAへ渡せる。<br>正しくは、利用目的、提供先、提供項目、自由な同意、提供記録が問題になります。</div>': '<div class="law-caution"><strong>誤読3：</strong>同意欄があれば、学校保有情報を恒常的なPTA会員管理へ使える。<br>正しくは、まず学校自身の利用かPTAへの提供かを分け、個人情報保護法61条の所掌事務・業務、69条の目的外利用・提供の制限、同意の自由性、利用目的、対象項目、記録を確認します。</div>',
    '<div class="law-caution"><strong>誤読4：</strong>校長判断なら勤務時間中のPTA事務も問題ない。<br>正しくは、職務か職務外か、職専免か兼職兼業か、根拠と記録を確認します。</div>': '<div class="law-caution"><strong>誤読4：</strong>校長判断なら勤務時間中のPTA事務も問題ない。<br>正しくは、校務としての位置付け、職務命令、職専免、兼職兼業、対象者、時間、用務を具体的な規則と記録で確認します。</div>',
}

for old, new in replacements.items():
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"Expected one marker, found {count}: {old[:90]}")
    text = text.replace(old, new)

style = '''
<style id="law-editorial-20260710">
body.law-editorial .law-actions,
body.law-editorial .law-toc{
  display:none!important;
}
body.law-editorial .law-kicker{
  border-radius:3px!important;
  text-transform:none!important;
  letter-spacing:.04em!important;
}
body.law-editorial .law-wrap{
  width:min(calc(100% - 40px),920px)!important;
  padding:64px 0 96px!important;
}
body.law-editorial .law-panel{
  margin:0!important;
  padding:40px 0 46px!important;
  background:#fff!important;
  border:0!important;
  border-top:1px solid #cfd8e2!important;
  border-radius:0!important;
  box-shadow:none!important;
}
body.law-editorial .law-panel:first-child{
  border-top:2px solid #1e3a5f!important;
}
body.law-editorial .law-grid,
body.law-editorial .law-matrix,
body.law-editorial .next-grid{
  display:block!important;
}
body.law-editorial .law-card,
body.law-editorial .law-axis,
body.law-editorial .next-grid a{
  margin:0!important;
  padding:22px 0!important;
  background:#fff!important;
  border:0!important;
  border-bottom:1px solid #dbe4ee!important;
  border-radius:0!important;
  box-shadow:none!important;
}
body.law-editorial .law-card .tag{
  display:none!important;
}
body.law-editorial .law-axis{
  display:grid!important;
  grid-template-columns:180px minmax(0,1fr)!important;
  gap:24px!important;
}
body.law-editorial .law-axis h3{
  margin:0!important;
  padding:0!important;
  background:#fff!important;
  color:#1e3a5f!important;
  text-align:left!important;
  font-family:'Noto Serif JP',serif!important;
  font-size:1.02rem!important;
}
body.law-editorial .law-axis div{
  padding:0!important;
}
body.law-editorial .law-axis span{
  display:inline!important;
  margin:0 .75em 0 0!important;
  padding:0!important;
  background:transparent!important;
  border:0!important;
  border-radius:0!important;
  color:#475569!important;
  font-size:.9rem!important;
  font-weight:700!important;
  line-height:1.9!important;
}
body.law-editorial .law-axis span::after{
  content:'／';
  margin-left:.75em;
  color:#94a3b8;
}
body.law-editorial .law-axis span:last-child::after{
  content:'';
  margin:0;
}
body.law-editorial .law-caution{
  border-radius:0!important;
  box-shadow:none!important;
}
body.law-editorial .source-links{
  display:block!important;
}
body.law-editorial .source-links a{
  display:block!important;
  margin:0!important;
  padding:12px 0!important;
  background:#fff!important;
  border:0!important;
  border-bottom:1px solid #dbe4ee!important;
  border-radius:0!important;
}
body.law-editorial main a:hover{
  transform:none!important;
  box-shadow:none!important;
}
@media(max-width:700px){
  body.law-editorial .law-wrap{
    width:min(calc(100% - 30px),920px)!important;
  }
  body.law-editorial .law-axis{
    grid-template-columns:1fr!important;
    gap:8px!important;
  }
}
</style>
'''

if 'id="law-editorial-20260710"' in text:
    raise SystemExit("Editorial style already exists")
text = text.replace('</head>', style + '</head>', 1)
path.write_text(text, encoding='utf-8')
