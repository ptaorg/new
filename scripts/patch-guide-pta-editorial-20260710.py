from pathlib import Path

p = Path(__file__).resolve().parents[1] / 'guide-pta.html'
text = p.read_text(encoding='utf-8')

replacements = {
    '<body>': '<body class="guide-pta-editorial">',
    '<div class="page-hero-kicker">For Officers</div>': '<div class="page-hero-kicker">PTA役員向け実務資料</div>',
    '<h1>役員だからこそ、<br/><em>今すぐ確認</em>すべきことがある。</h1>': '<h1>PTAを、学校依存ではなく<br/><em>説明できる任意団体</em>として運営する</h1>',
    '<p>PTAを学校任せにせず、任意団体として説明できる運営へ整えるための実務ガイドです。学校利用、会費、個人情報、教職員への依頼を就任直後に確認します。</p>': '<p>入会申込、会員名簿、会費徴収、個人情報、学校施設、教職員への依頼を分け、PTA自身が会員へ説明できる運営へ改めるための実務資料です。</p>',
    '<p style="margin:-16px 0 28px;color:#475569;line-height:1.8;font-size:.92rem">第1章から第11章までは見出しを押すと本文が開きます。図解画像は章の中には入れず、この本文の後ろにある「図解で確認するPTA運営の適正化」で別枠として掲載しています。</p>': '<p style="margin:-16px 0 28px;color:#475569;line-height:1.8;font-size:.92rem">第1章から第11章までを連続して掲載しています。図解資料は本文後半にまとめています。</p>',
}
for old, new in replacements.items():
    if old not in text:
        raise SystemExit(f'marker not found: {old[:80]}')
    text = text.replace(old, new, 1)

text = text.replace('<details class="gb-chapter gb-chapter-accordion"', '<details class="gb-chapter gb-chapter-accordion" open')

style = r'''
<style id="guide-pta-editorial-20260710">
body.guide-pta-editorial .page-hero-kicker{
  text-transform:none!important;
  letter-spacing:.03em!important;
  border-radius:3px!important;
}
body.guide-pta-editorial .hero-actions,
body.guide-pta-editorial .officer-chain-direct{
  display:none!important;
}
body.guide-pta-editorial .officer-video-section{
  padding:38px 0!important;
  background:#f8fafc!important;
  border-bottom:1px solid #dbe4ee!important;
}
body.guide-pta-editorial .officer-video-card{
  border:0!important;
  border-left:4px solid var(--gold)!important;
  border-radius:0!important;
  box-shadow:none!important;
  padding:22px 0 22px 24px!important;
  background:transparent!important;
}
body.guide-pta-editorial .officer-video-badge,
body.guide-pta-editorial .otl-phase,
body.guide-pta-editorial .rm-phase{
  display:none!important;
}
body.guide-pta-editorial #guidebook-text{
  padding-top:68px!important;
}
body.guide-pta-editorial #guidebook-text > .wrap > div:first-child{
  display:none!important;
}
body.guide-pta-editorial .gb-chapter,
body.guide-pta-editorial .gb-chapter-accordion{
  border:0!important;
  border-top:1px solid #cfd8e2!important;
  border-radius:0!important;
  margin:0!important;
  padding:0!important;
  background:#fff!important;
}
body.guide-pta-editorial .gb-chapter-accordion:last-child{
  border-bottom:1px solid #cfd8e2!important;
}
body.guide-pta-editorial .gb-chapter-summary{
  cursor:default!important;
  list-style:none!important;
  padding:24px 0 18px!important;
  background:#fff!important;
  border:0!important;
  color:var(--navy)!important;
}
body.guide-pta-editorial .gb-chapter-summary::-webkit-details-marker,
body.guide-pta-editorial .gb-chapter-state,
body.guide-pta-editorial .gb-chapter-summary::after{
  display:none!important;
}
body.guide-pta-editorial .gb-chapter-content{
  display:block!important;
  padding:0 0 34px!important;
  background:#fff!important;
}
body.guide-pta-editorial .otl-body,
body.guide-pta-editorial .risk-col,
body.guide-pta-editorial .compare-col,
body.guide-pta-editorial .rm-body,
body.guide-pta-editorial .opdf-card,
body.guide-pta-editorial .otl-check{
  border-radius:0!important;
  box-shadow:none!important;
  transform:none!important;
}
body.guide-pta-editorial .risk-chart,
body.guide-pta-editorial .officer-pdf-grid{
  display:block!important;
  max-width:880px!important;
  margin-left:auto!important;
  margin-right:auto!important;
}
body.guide-pta-editorial .risk-col,
body.guide-pta-editorial .opdf-card{
  margin:0!important;
  padding:24px 0!important;
  border:0!important;
  border-top:1px solid rgba(255,255,255,.24)!important;
  background:transparent!important;
}
body.guide-pta-editorial .risk-col:last-child,
body.guide-pta-editorial .opdf-card:last-child{
  border-bottom:1px solid rgba(255,255,255,.24)!important;
}
body.guide-pta-editorial .compare-wrap{
  grid-template-columns:1fr!important;
  gap:0!important;
  border-top:1px solid #cfd8e2!important;
}
body.guide-pta-editorial .compare-col{
  padding:24px 0!important;
  border:0!important;
  border-bottom:1px solid #cfd8e2!important;
  background:transparent!important;
}
body.guide-pta-editorial .rm-body{
  border:0!important;
  border-bottom:1px solid #cfd8e2!important;
  padding:18px 0 24px!important;
}
body.guide-pta-editorial main a:hover,
body.guide-pta-editorial main button:hover,
body.guide-pta-editorial main summary:hover{
  transform:none!important;
  box-shadow:none!important;
}
@media(max-width:760px){
  body.guide-pta-editorial .officer-video-card{
    padding-left:18px!important;
  }
  body.guide-pta-editorial .onboard-timeline{
    padding-left:48px!important;
  }
}
</style>
'''
if 'guide-pta-editorial-20260710' not in text:
    text = text.replace('</head>', style + '</head>', 1)

p.write_text(text, encoding='utf-8')
