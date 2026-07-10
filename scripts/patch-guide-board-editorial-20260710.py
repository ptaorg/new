from pathlib import Path

p = Path(__file__).resolve().parents[1] / 'guide-board.html'
text = p.read_text(encoding='utf-8')

old_desc = 'PTAの任意加入、学校教育法137条、働き方改革3分類、学校徴収金、個人情報、教職員関与を学校管理上の点検事項として整理します。'
new_desc = 'PTAの任意加入、学校徴収金、個人情報、教職員関与、学校施設利用を、教育委員会・学校管理職が確認する学校管理上の事項として整理します。'
if old_desc not in text:
    raise SystemExit('description marker not found')
text = text.replace(old_desc, new_desc)

replacements = {
    '<body>': '<body class="guide-board-direct-fixed guide-board-editorial">',
    '<div class="page-hero-kicker">For School Boards</div>': '<div class="page-hero-kicker">教育委員会・学校管理職向け資料</div>',
    '<h1>教育委員会向け<br/><em>ガイド</em></h1>': '<h1>学校とPTAの境界を<br/><em>学校管理の問題として点検する</em></h1>',
    '<p>PTA内部を指揮するページではありません。学校がPTAの配布、回収、徴収、名簿、連絡、教職員事務、施設利用に関与した部分を、学校管理上の点検対象として切り分けます。</p>': '<p>教育委員会がPTA内部を指揮するための資料ではありません。学校がPTAの配布・回収、会費徴収、名簿、連絡ツール、教職員事務、施設利用に関与した部分を、学校管理と服務管理の対象として切り分けます。</p>',
}
for old, new in replacements.items():
    if old not in text:
        raise SystemExit(f'marker not found: {old[:90]}')
    text = text.replace(old, new, 1)

style = r'''
<style id="guide-board-editorial-20260710">
body.guide-board-editorial .page-hero-kicker{
  text-transform:none!important;
  letter-spacing:.03em!important;
  border-radius:3px!important;
}
body.guide-board-editorial .hero-actions,
body.guide-board-editorial .board-chain-direct{
  display:none!important;
}
body.guide-board-editorial .page-hero--photo .page-hero-inner{
  max-width:980px!important;
}
body.guide-board-editorial #board-executive-brief{
  background:#fff!important;
  padding:68px 0 76px!important;
}
body.guide-board-editorial .gbv-wrap,
body.guide-board-editorial .board-jp-shell{
  width:min(calc(100% - 40px),960px)!important;
}
body.guide-board-editorial .gbv-head,
body.guide-board-editorial .gbv-two,
body.guide-board-editorial .gbv-law-points,
body.guide-board-editorial .gbv-source,
body.guide-board-editorial .principal-risk-brief{
  grid-template-columns:1fr!important;
  gap:18px!important;
}
body.guide-board-editorial .gbv-head{
  align-items:start!important;
  margin-bottom:38px!important;
}
body.guide-board-editorial .gbv-principle{
  max-width:800px!important;
  padding:10px 0 10px 20px!important;
  border-left:4px solid #d6a724!important;
  background:transparent!important;
}
body.guide-board-editorial .gbv-stack{
  gap:34px!important;
}
body.guide-board-editorial .gbv-figure,
body.guide-board-editorial .principal-risk-main,
body.guide-board-editorial .principal-risk-evidence-card,
body.guide-board-editorial .gbv-statute,
body.guide-board-editorial .board-jp-article .primary-summary,
body.guide-board-editorial .board-jp-article .toc,
body.guide-board-editorial .board-jp-article .flow{
  border-radius:0!important;
  box-shadow:none!important;
}
body.guide-board-editorial .gbv-figure{
  border-left:0!important;
  border-right:0!important;
}
body.guide-board-editorial .gbv-two > *,
body.guide-board-editorial .gbv-source > *,
body.guide-board-editorial .gbv-law-points > div{
  border-radius:0!important;
  box-shadow:none!important;
}
body.guide-board-editorial #principal-liability{
  padding:60px 0!important;
}
body.guide-board-editorial .principal-risk-main,
body.guide-board-editorial .principal-risk-evidence-card{
  border-left:0!important;
  border-right:0!important;
}
body.guide-board-editorial .key-materials-grid{
  display:block!important;
  max-width:900px!important;
  margin-left:auto!important;
  margin-right:auto!important;
}
body.guide-board-editorial .key-materials-grid > a{
  display:grid!important;
  grid-template-columns:180px minmax(0,1fr)!important;
  min-height:0!important;
  margin:0!important;
  border:0!important;
  border-top:1px solid #cbd5e1!important;
  border-radius:0!important;
  box-shadow:none!important;
}
body.guide-board-editorial .key-materials-grid > a:last-child{
  border-bottom:1px solid #cbd5e1!important;
}
body.guide-board-editorial .key-materials-grid > a > img{
  height:100%!important;
  min-height:150px!important;
  border:0!important;
}
body.guide-board-editorial .key-materials-grid > a > div{
  padding:20px 24px!important;
}
body.guide-board-editorial main a:hover,
body.guide-board-editorial main summary:hover{
  transform:none!important;
  box-shadow:none!important;
}
@media(max-width:720px){
  body.guide-board-editorial .key-materials-grid > a{
    grid-template-columns:1fr!important;
  }
  body.guide-board-editorial .key-materials-grid > a > img{
    min-height:150px!important;
    height:150px!important;
  }
}
</style>
'''
if 'guide-board-editorial-20260710' not in text:
    text = text.replace('</head>', style + '</head>', 1)

p.write_text(text, encoding='utf-8')
