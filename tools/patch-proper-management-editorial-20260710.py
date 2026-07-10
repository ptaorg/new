from pathlib import Path

path = Path(__file__).resolve().parents[1] / "proper-management.html"
text = path.read_text(encoding="utf-8")

replacements = {
    '<body>': '<body class="proper-management-editorial">',
    '<div class="pm-kicker">Core Policy</div>': '<div class="pm-kicker">適正運営の基本</div>',
    '<p class="pm-lead">適正化とは、PTAをなくすことではありません。PTAを、学校に溶け込んだ慣行から切り離し、保護者が納得して参加できる任意団体として立て直すことです。</p>': '<p class="pm-lead">適正化とは、PTAをなくすことでも、会費をゼロにすることでもありません。PTAを、学校に溶け込んだ慣行から切り離し、保護者が納得して参加できる任意団体として立て直すことです。</p>',
    '<div class="pm-hero-note">学校とPTAの関係をあいまいにしたままでは、入会意思、会費徴収、個人情報、教職員関与、学校施設利用の根拠が見えなくなります。適正化は、善意の活動を法令に沿って持続可能にするための線引きです。</div>': '<div class="pm-hero-note">年会費制、必要時の都度負担、寄付・カンパ型など、資金調達の方法は一つではありません。重要なのは、加入意思、会費額と使途、請求主体、徴収方法、会計責任、退会後の取扱いをPTA自身が説明できることです。</div>',
}

for old, new in replacements.items():
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"Expected one marker, found {count}: {old[:100]}")
    text = text.replace(old, new)

marker = '''</section>\n<section class="pm-section" id="principles">'''
insert = '''</section>\n<section class="pm-section" id="fees">\n  <h2>会費ゼロは、適正化の必須条件ではない</h2>\n  <p>会費ゼロは、役員負担や会計事務を小さくする一つの設計例です。しかし、すべてのPTAにその形を要求できるわけではありません。活動内容と必要経費に応じて、年会費制、事業ごとの実費負担、任意の寄付・カンパなどを選択できます。</p>\n  <p>年会費を設ける場合でも、本人が入会を申し込み、会費額と使途が加入前に示され、PTA自身が請求・徴収・会計・監査を行い、学校徴収金や学校保有口座情報へ当然に依存せず、非会員家庭や児童を不利益に扱わない運営であれば、会費があること自体が不適正なのではありません。</p>\n  <p>反対に、会費をゼロにしても、みなし加入、学校名簿の利用、役員強制、教職員による内部事務、学校連絡ツールへの依存が残れば、適正化したことにはなりません。問われるのは会費の有無ではなく、加入と負担が本人の意思に基づき、学校手続と分離され、団体自身の責任で説明できるかです。</p>\n</section>\n<section class="pm-section" id="principles">'''
if text.count(marker) != 1:
    raise SystemExit(f"Fee section marker count: {text.count(marker)}")
text = text.replace(marker, insert)

style = '''
<style id="proper-management-editorial-20260710">
body.proper-management-editorial .breadcrumb-bar{
  display:none!important;
}
body.proper-management-editorial .pm-kicker{
  border-radius:3px!important;
  text-transform:none!important;
  letter-spacing:.04em!important;
}
body.proper-management-editorial .pm-wrap{
  max-width:920px!important;
  padding:64px 24px 96px!important;
}
body.proper-management-editorial .pm-section{
  margin:0!important;
  padding:40px 0 48px!important;
  border-top:1px solid #cfd8e2!important;
}
body.proper-management-editorial .pm-section:first-child{
  border-top:2px solid #17345c!important;
}
body.proper-management-editorial .pm-section h2{
  border-left:0!important;
  padding-left:0!important;
  padding-bottom:12px!important;
  border-bottom:2px solid #17345c!important;
}
body.proper-management-editorial .pm-rule-list{
  display:block!important;
}
body.proper-management-editorial .pm-rule-list li{
  margin:0!important;
  padding:24px 0 24px 58px!important;
  background:#fff!important;
  border:0!important;
  border-top:1px solid #dbe4ee!important;
  border-radius:0!important;
  box-shadow:none!important;
}
body.proper-management-editorial .pm-rule-list li:last-child{
  border-bottom:1px solid #dbe4ee!important;
}
body.proper-management-editorial .pm-rule-list li::before{
  left:0!important;
  top:22px!important;
  width:34px!important;
  height:34px!important;
  border-radius:2px!important;
}
body.proper-management-editorial .pm-table{
  border-radius:0!important;
  box-shadow:none!important;
}
body.proper-management-editorial .pm-step{
  margin:0!important;
  padding:22px 0!important;
  background:#fff!important;
  border:0!important;
  border-top:1px solid #dbe4ee!important;
  border-radius:0!important;
}
body.proper-management-editorial .pm-step:last-child{
  border-bottom:1px solid #dbe4ee!important;
}
body.proper-management-editorial .pm-link-band{
  margin-top:0!important;
  padding:40px 0 0!important;
  background:#fff!important;
  color:#26384e!important;
  border-radius:0!important;
  border-top:1px solid #cfd8e2!important;
}
body.proper-management-editorial .pm-link-band h2{
  color:#0b2545!important;
}
body.proper-management-editorial .pm-link-band p{
  color:#334155!important;
}
body.proper-management-editorial .pm-actions{
  display:block!important;
  margin-top:18px!important;
}
body.proper-management-editorial .pm-actions a,
body.proper-management-editorial .pm-actions a.secondary{
  display:block!important;
  width:auto!important;
  padding:14px 0!important;
  background:#fff!important;
  color:#174f7d!important;
  border:0!important;
  border-bottom:1px solid #dbe4ee!important;
  border-radius:0!important;
  box-shadow:none!important;
  text-decoration:underline!important;
  text-underline-offset:.18em!important;
}
body.proper-management-editorial main a:hover{
  transform:none!important;
  box-shadow:none!important;
}
@media(max-width:720px){
  body.proper-management-editorial .pm-wrap{
    padding:48px 18px 72px!important;
  }
  body.proper-management-editorial .pm-rule-list li{
    padding:22px 0 22px 50px!important;
  }
}
</style>
'''
if 'proper-management-editorial-20260710' in text:
    raise SystemExit('Editorial style already present')
text = text.replace('</head>', style + '</head>', 1)

required = [
    '会費ゼロは、適正化の必須条件ではない',
    '年会費制、事業ごとの実費負担、任意の寄付・カンパ',
    '会費をゼロにしても、みなし加入',
    'proper-management-editorial-20260710',
]
for item in required:
    if item not in text:
        raise SystemExit(f'Missing required text: {item}')

path.write_text(text, encoding='utf-8')
