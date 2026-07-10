from pathlib import Path

path = Path('board-responses.html')
text = path.read_text(encoding='utf-8')

if text.count('<body>') != 1:
    raise SystemExit('body marker not found')
text = text.replace('<body>', '<body class="board-responses-editorial">', 1)

old = '<section class="compact-hero-section"><div class="wrap"><div class="hero-kicker">Board Responses</div><h1>全国教育委員会への照会結果</h1></div></section>'
new = '<section class="compact-hero-section"><div class="wrap"><div class="hero-kicker">教育委員会回答資料</div><h1>全国教育委員会への照会結果</h1></div></section>'
if text.count(old) != 1:
    raise SystemExit(f'hero marker count: {text.count(old)}')
text = text.replace(old, new, 1)

style = '''
<style id="board-responses-editorial-20260710">
.board-responses-editorial .compact-hero-section{
  padding:58px 0 52px!important;
  text-align:left!important;
  border-bottom:1px solid #071a30!important;
}
.board-responses-editorial .compact-hero-section .wrap{
  width:min(calc(100% - 40px),1040px)!important;
}
.board-responses-editorial .compact-hero-section .hero-kicker{
  display:block!important;
  width:max-content!important;
  margin:0 0 16px!important;
  padding:0 0 6px!important;
  background:transparent!important;
  border:0!important;
  border-bottom:1px solid rgba(212,175,55,.75)!important;
  border-radius:0!important;
  text-transform:none!important;
  letter-spacing:.05em!important;
}
.board-responses-editorial .response-trends-section .reading-body,
.board-responses-editorial .response-bodies-section>.wrap,
.board-responses-editorial .excluded-section>.wrap,
.board-responses-editorial .caution-section>.wrap{
  width:min(calc(100% - 40px),920px)!important;
}
.board-responses-editorial #responseMap,
.board-responses-editorial .region-map,
.board-responses-editorial .region-map-card{
  border-radius:0!important;
  box-shadow:none!important;
}
.board-responses-editorial .map-index-link{
  display:inline!important;
  padding:0!important;
  background:transparent!important;
  color:#174f7d!important;
  border-radius:0!important;
  text-decoration:underline!important;
  text-underline-offset:.18em!important;
}
.board-responses-editorial .region-map-panel{
  gap:22px!important;
}
.board-responses-editorial .region-map-card{
  padding:0 0 20px!important;
  background:transparent!important;
  border:0!important;
  border-bottom:1px solid #cfd8e2!important;
}
.board-responses-editorial #muniSearch{
  max-width:100%!important;
  border-radius:0!important;
  border-width:0 0 2px!important;
  padding:12px 2px!important;
}
.board-responses-editorial #regionIndex .municipality-list{
  display:block!important;
}
.board-responses-editorial #regionIndex .muni-link{
  display:inline!important;
  margin-right:1em!important;
  padding:0!important;
  background:transparent!important;
  border:0!important;
  border-radius:0!important;
  color:#174f7d!important;
  text-decoration:underline!important;
  text-underline-offset:.18em!important;
  line-height:2.2!important;
  white-space:normal!important;
}
.board-responses-editorial #regionIndex .muni-link:hover{
  background:transparent!important;
  color:#9a4c00!important;
}
.board-responses-editorial #regionIndex .muni-count{
  padding:0!important;
  background:transparent!important;
  color:#64748b!important;
  border-radius:0!important;
  font-weight:700!important;
}
.board-responses-editorial .type-label-badge{
  display:none!important;
}
.board-responses-editorial .response-item{
  margin:0!important;
  padding:24px 0!important;
  background:transparent!important;
  border:0!important;
  border-bottom:1px solid #cfd8e2!important;
  border-radius:0!important;
}
.board-responses-editorial .response-item:first-of-type{
  border-top:1px solid #cfd8e2!important;
}
.board-responses-editorial .response-item details summary{
  padding:8px 0!important;
  text-decoration:underline!important;
  text-underline-offset:.18em!important;
}
.board-responses-editorial .trend-example-list a,
.board-responses-editorial .back-to-index a{
  text-decoration:underline!important;
  text-underline-offset:.18em!important;
  border-bottom:0!important;
}
.board-responses-editorial main a:hover{
  transform:none!important;
  box-shadow:none!important;
}
@media(max-width:680px){
  .board-responses-editorial .compact-hero-section .wrap,
  .board-responses-editorial .response-trends-section .reading-body,
  .board-responses-editorial .response-bodies-section>.wrap,
  .board-responses-editorial .excluded-section>.wrap,
  .board-responses-editorial .caution-section>.wrap{
    width:min(calc(100% - 30px),920px)!important;
  }
}
</style>
'''
if 'board-responses-editorial-20260710' in text:
    raise SystemExit('editorial style already present')
text = text.replace('</head>', style + '</head>', 1)

path.write_text(text, encoding='utf-8')
