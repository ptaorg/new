from pathlib import Path

path = Path('cases.html')
text = path.read_text(encoding='utf-8')

if '<body class="cases-editorial">' not in text:
    if text.count('<body>') != 1:
        raise SystemExit('body marker not found')
    text = text.replace('<body>', '<body class="cases-editorial">', 1)

old = '<div class="page-banner-kicker">Legal Cases · 判例整理</div>'
new = '<div class="page-banner-kicker">判例・裁判資料の整理</div>'
if old in text:
    text = text.replace(old, new, 1)
elif new not in text:
    raise SystemExit('kicker marker not found')

style = '''
<style id="cases-editorial-20260710">
.cases-editorial .report-layout-section{
  display:block!important;
  width:min(calc(100% - 40px),920px)!important;
  margin-inline:auto!important;
}
.cases-editorial .report-toc{
  display:none!important;
}
.cases-editorial .report-content-wrap{
  width:100%!important;
  max-width:none!important;
}
.cases-editorial .pta-report-container{
  max-width:none!important;
}
.cases-editorial .editorial-panel,
.cases-editorial .claim-evidence-box,
.cases-editorial .case-card,
.cases-editorial .report-related-links{
  border-radius:0!important;
  box-shadow:none!important;
}
.cases-editorial .case-card{
  margin:0!important;
  padding:34px 0!important;
  background:#fff!important;
  border:0!important;
  border-top:1px solid #cfd8e2!important;
}
.cases-editorial .case-card:last-child{
  border-bottom:1px solid #cfd8e2!important;
}
.cases-editorial .case-badge{
  display:none!important;
}
.cases-editorial .case-card-grid{
  display:block!important;
}
.cases-editorial .case-card-grid>div{
  padding:15px 0!important;
  border-bottom:1px solid #e2e8f0!important;
}
.cases-editorial .case-card-grid>div:last-child{
  border-bottom:0!important;
}
.cases-editorial .page-banner-kicker{
  text-transform:none!important;
  letter-spacing:.04em!important;
}
.cases-editorial main a:hover{
  transform:none!important;
  box-shadow:none!important;
}
@media(max-width:720px){
  .cases-editorial .report-layout-section{
    width:min(calc(100% - 30px),920px)!important;
  }
}
</style>
'''
if 'cases-editorial-20260710' not in text:
    text = text.replace('</head>', style + '</head>', 1)

path.write_text(text, encoding='utf-8')
