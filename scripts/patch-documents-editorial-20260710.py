from pathlib import Path

p = Path(__file__).resolve().parents[1] / 'documents.html'
text = p.read_text(encoding='utf-8')

replacements = {
    '<body>': '<body class="documents-editorial">',
    '<title>資料入口・索引 | PTA適正化推進委員会</title>': '<title>資料・文例索引 | PTA適正化推進委員会</title>',
    'content="資料入口・索引｜PTA適正化推進委員会" property="og:title"': 'content="資料・文例索引｜PTA適正化推進委員会" property="og:title"',
    '<span class="current">資料入口・索引</span>': '<span class="current">資料・文例索引</span>',
    '<h1>資料入口・索引</h1>': '<h1>資料・文例索引</h1>',
    '<p>当委員会が公開している一次資料、配布資料、データベースへの入口を、この1ページに整理しています。探している資料が決まっている場合は、ここから直接移動できます。</p>': '<p>一次資料、教育委員会回答、行政通知、提出用文例、調査報告を、資料の性質と用途ごとに整理しています。資料名と説明を確認し、必要な原文または文例へ直接進めます。</p>',
    '<p>検索で来た人がすぐ動けるように、根拠資料、確認事項、提出文書、関連ページを一列につなげました。任意加入の一般論ではなく、学校関与・名簿・会費・施設利用の実態を確認するための入口です。</p>': '<p>根拠資料、確認事項、提出文書を論点別に対応させています。学校関与、名簿、会費、施設利用の事実を、具体的な文書名で確認するために使用します。</p>',
    'href="guide-board.html#school-involvement-action-plan"': 'href="guide-board.html#board-executive-brief"',
}
for old, new in replacements.items():
    if old not in text:
        raise SystemExit(f'marker not found: {old[:100]}')
    text = text.replace(old, new, 1)

style = r'''
<style id="documents-editorial-20260710">
body.documents-editorial .doc-index{
  max-width:920px!important;
  padding:56px 22px 86px!important;
}
body.documents-editorial .doc-sec{
  margin:0!important;
  padding:38px 0 44px!important;
  border-top:1px solid #cfd8e2!important;
}
body.documents-editorial .doc-sec:first-of-type{
  border-top:2px solid #1e3a5f!important;
}
body.documents-editorial .doc-sec h2{
  border-bottom:0!important;
  padding-bottom:0!important;
  margin-bottom:10px!important;
  line-height:1.5!important;
}
body.documents-editorial .doc-sec h2::after{
  display:none!important;
}
body.documents-editorial .doc-grid{
  display:block!important;
  margin-top:18px!important;
  border-top:1px solid #dbe4ee!important;
}
body.documents-editorial .doc-item,
body.documents-editorial .doc-item.gold{
  display:grid!important;
  grid-template-columns:260px minmax(0,1fr)!important;
  gap:22px!important;
  align-items:baseline!important;
  margin:0!important;
  padding:18px 0!important;
  background:#fff!important;
  border:0!important;
  border-bottom:1px solid #dbe4ee!important;
  border-radius:0!important;
  box-shadow:none!important;
  transform:none!important;
}
body.documents-editorial .doc-item strong,
body.documents-editorial .doc-item span{
  margin:0!important;
}
body.documents-editorial .featured-pack{
  background:#fff!important;
  border-left:0!important;
  border-right:0!important;
  border-bottom:0!important;
  border-radius:0!important;
  box-shadow:none!important;
}
body.documents-editorial .doc-pack-layout{
  display:block!important;
  margin-top:22px!important;
}
body.documents-editorial .doc-pack-grid{
  display:block!important;
  border-top:1px solid #dbe4ee!important;
}
body.documents-editorial .doc-pack-card{
  display:grid!important;
  grid-template-columns:170px 230px minmax(0,1fr)!important;
  gap:18px!important;
  align-items:start!important;
  margin:0!important;
  padding:20px 0!important;
  background:#fff!important;
  border:0!important;
  border-bottom:1px solid #dbe4ee!important;
  border-radius:0!important;
  box-shadow:none!important;
}
body.documents-editorial .doc-pack-label{
  text-transform:none!important;
  letter-spacing:.02em!important;
  color:#7c2d12!important;
}
body.documents-editorial .doc-pack-card p{
  margin:0!important;
}
body.documents-editorial .doc-pack-links{
  grid-column:2 / -1!important;
  display:flex!important;
  gap:8px 18px!important;
  margin:0!important;
}
body.documents-editorial .doc-pack-links a{
  padding:0!important;
  background:transparent!important;
  border:0!important;
  border-radius:0!important;
  color:#174f7d!important;
  text-decoration:underline!important;
  text-underline-offset:3px!important;
}
body.documents-editorial .doc-pack-links a:hover{
  background:transparent!important;
  color:#0f2747!important;
}
body.documents-editorial .doc-diagram{
  max-width:680px!important;
  margin:34px auto 0!important;
  padding:0!important;
  background:#fff!important;
  border:0!important;
  border-radius:0!important;
  box-shadow:none!important;
}
body.documents-editorial main a:hover{
  transform:none!important;
  box-shadow:none!important;
}
@media(max-width:760px){
  body.documents-editorial .doc-item,
  body.documents-editorial .doc-item.gold,
  body.documents-editorial .doc-pack-card{
    grid-template-columns:1fr!important;
    gap:6px!important;
  }
  body.documents-editorial .doc-pack-links{
    grid-column:1!important;
    margin-top:8px!important;
  }
}
</style>
'''
if 'documents-editorial-20260710' not in text:
    text = text.replace('</head>', style + '</head>', 1)

p.write_text(text, encoding='utf-8')
