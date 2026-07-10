from pathlib import Path

p = Path(__file__).resolve().parents[1] / 'guide-research.html'
text = p.read_text(encoding='utf-8')

replacements = {
    '<body class="research-page">': '<body class="research-page research-editorial">',
    '<div class="research-kicker">Research / Reporting</div>': '<div class="research-kicker">研究・報道向け資料</div>',
    '<h1>研究者・記者の方へ</h1>': '<h1>PTA問題を<br><em>一次資料から検証する</em></h1>',
}
for old, new in replacements.items():
    if old not in text:
        raise SystemExit(f'marker not found: {old}')
    text = text.replace(old, new, 1)

style = r'''
<style id="guide-research-editorial-20260710">
body.research-editorial{
  background:#fff!important;
}
body.research-editorial .research-inner,
body.research-editorial .research-wrap{
  width:min(calc(100% - 40px),920px)!important;
}
body.research-editorial .research-kicker{
  text-transform:none!important;
  letter-spacing:.03em!important;
  border-radius:3px!important;
}
body.research-editorial .research-hero h1 em{
  color:#fed7aa!important;
  font-style:normal!important;
}
body.research-editorial .research-actions,
body.research-editorial .research-toc{
  display:none!important;
}
body.research-editorial .research-wrap{
  padding:68px 0 92px!important;
}
body.research-editorial .research-panel{
  margin:0!important;
  padding:38px 0 42px!important;
  background:#fff!important;
  border:0!important;
  border-top:1px solid #cfd8e2!important;
  border-radius:0!important;
  box-shadow:none!important;
}
body.research-editorial .research-panel:first-child{
  border-top:2px solid #1e3a5f!important;
}
body.research-editorial .research-panel:last-child{
  border-bottom:1px solid #cfd8e2!important;
}
body.research-editorial .research-panel h2{
  border-bottom:0!important;
  padding-bottom:0!important;
  margin-bottom:18px!important;
  line-height:1.5!important;
}
body.research-editorial .method-grid,
body.research-editorial .next-grid{
  display:block!important;
  margin-top:20px!important;
}
body.research-editorial .method-card{
  margin:0!important;
  padding:20px 0!important;
  background:#fff!important;
  border:0!important;
  border-top:1px solid #dbe4ee!important;
  border-radius:0!important;
}
body.research-editorial .method-card:last-child{
  border-bottom:1px solid #dbe4ee!important;
}
body.research-editorial .method-card span{
  display:block!important;
  width:max-content!important;
  margin:0 0 6px!important;
  padding:0!important;
  background:transparent!important;
  border:0!important;
  border-radius:0!important;
  color:#9a3412!important;
  font-size:.74rem!important;
  letter-spacing:.04em!important;
}
body.research-editorial .next-grid a{
  display:grid!important;
  grid-template-columns:240px minmax(0,1fr)!important;
  gap:20px!important;
  align-items:baseline!important;
  margin:0!important;
  padding:18px 0!important;
  background:#fff!important;
  border:0!important;
  border-top:1px solid #dbe4ee!important;
  border-radius:0!important;
  box-shadow:none!important;
}
body.research-editorial .next-grid a:last-child{
  border-bottom:1px solid #dbe4ee!important;
}
body.research-editorial .next-grid span{
  margin:0!important;
}
body.research-editorial .caution{
  border-radius:0!important;
  box-shadow:none!important;
}
body.research-editorial main a:hover{
  transform:none!important;
  box-shadow:none!important;
}
@media(max-width:700px){
  body.research-editorial .next-grid a{
    grid-template-columns:1fr!important;
    gap:5px!important;
  }
  body.research-editorial .research-inner,
  body.research-editorial .research-wrap{
    width:min(calc(100% - 30px),920px)!important;
  }
}
</style>
'''
if 'guide-research-editorial-20260710' not in text:
    text = text.replace('</head>', style + '</head>', 1)

p.write_text(text, encoding='utf-8')
