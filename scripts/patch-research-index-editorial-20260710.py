from pathlib import Path

p = Path(__file__).resolve().parents[1] / 'research-index.html'
text = p.read_text(encoding='utf-8')

if '<body class="ri-page">' not in text:
    raise SystemExit('body marker not found')
text = text.replace('<body class="ri-page">', '<body class="ri-page ri-editorial">', 1)
text = text.replace('研究・資料ハブ', '根拠資料・調査方法')

old_lead = 'PTA問題を一次資料で検証するための入口です。まず法制度で論点を分け、研究方法で資料の読み方を確認し、資料検証チェックリストで文書の見方を揃えてから、判例・制度史・行政資料・教育委員会回答へ進みます。'
new_lead = 'PTA問題を一次資料で検証するために、法制度、資料の作成主体、文書の現行性、事実と評価の区別を順に整理します。そのうえで、判例、制度史、行政資料、教育委員会回答、学校・PTA文書を確認します。'
if old_lead not in text:
    raise SystemExit('hero lead marker not found')
text = text.replace(old_lead, new_lead, 1)

style = r'''
<style id="research-index-editorial-20260710">
body.ri-editorial{
  background:#fff!important;
}
body.ri-editorial .ri-wrap{
  width:min(calc(100% - 40px),920px)!important;
}
body.ri-editorial .ri-hero{
  background:linear-gradient(135deg,#071a30,#183858)!important;
  padding:76px 0 68px!important;
}
body.ri-editorial .ri-hero h1{
  line-height:1.4!important;
}
body.ri-editorial .ri-panel{
  margin:0!important;
  padding:38px 0 42px!important;
  background:#fff!important;
  border:0!important;
  border-top:1px solid #cfd8e2!important;
  border-radius:0!important;
  box-shadow:none!important;
}
body.ri-editorial .ri-wrap > .ri-panel:first-child{
  margin-top:64px!important;
  border-top:2px solid #1e3a5f!important;
}
body.ri-editorial .ri-panel h2{
  border-bottom:0!important;
  padding-bottom:0!important;
  line-height:1.5!important;
}
body.ri-editorial .ri-matrix{
  display:block!important;
  margin-top:20px!important;
}
body.ri-editorial .ri-box{
  margin:0!important;
  padding:18px 0!important;
  background:#fff!important;
  border:0!important;
  border-top:1px solid #dbe4ee!important;
  border-radius:0!important;
}
body.ri-editorial .ri-box:last-child{
  border-bottom:1px solid #dbe4ee!important;
}
body.ri-editorial .ri-grid{
  display:block!important;
  padding:8px 0 88px!important;
  border-top:2px solid #1e3a5f!important;
}
body.ri-editorial .ri-card{
  display:grid!important;
  grid-template-columns:240px minmax(0,1fr)!important;
  gap:22px!important;
  align-items:baseline!important;
  margin:0!important;
  padding:20px 0!important;
  background:#fff!important;
  border:0!important;
  border-bottom:1px solid #dbe4ee!important;
  border-radius:0!important;
  box-shadow:none!important;
  transform:none!important;
}
body.ri-editorial .ri-card strong{
  margin:0!important;
  line-height:1.6!important;
}
body.ri-editorial .ri-note{
  border-radius:0!important;
  box-shadow:none!important;
}
body.ri-editorial main a:hover{
  transform:none!important;
  box-shadow:none!important;
}
@media(max-width:700px){
  body.ri-editorial .ri-wrap{
    width:min(calc(100% - 30px),920px)!important;
  }
  body.ri-editorial .ri-card{
    grid-template-columns:1fr!important;
    gap:6px!important;
  }
}
</style>
'''
if 'research-index-editorial-20260710' not in text:
    text = text.replace('</head>', style + '</head>', 1)

p.write_text(text, encoding='utf-8')
