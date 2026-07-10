from pathlib import Path

path = Path('journal.html')
text = path.read_text(encoding='utf-8')
before = len(text)

old = '<div class="page-hero-kicker">Journal</div>'
new = '<div class="page-hero-kicker">論考・調査報告</div>'
if text.count(old) != 1:
    raise RuntimeError(f'journal kicker: expected 1, found {text.count(old)}')
text = text.replace(old, new)

style = '''
<style id="journal-prose-index-20260710">
.journal-layout{
  width:min(calc(100% - 40px),960px)!important;
  grid-template-columns:minmax(0,1fr)!important;
  gap:0!important;
  padding:64px 0 88px!important;
}
.journal-layout .category-bar,
.journal-layout .sidebar-section{
  display:none!important;
}
.journal-list-heading{
  font-family:'Noto Serif JP',serif!important;
  font-size:clamp(1.65rem,3vw,2.25rem)!important;
  line-height:1.5!important;
  margin-bottom:10px!important;
}
.journal-list-lead{
  max-width:780px!important;
  font-size:.98rem!important;
  line-height:1.95!important;
  margin-bottom:34px!important;
}
.journal-layout .article-list{
  display:block!important;
  border-top:2px solid var(--navy)!important;
}
.journal-layout .article-card,
.journal-layout .article-card.ac-featured{
  display:block!important;
  margin:0!important;
  padding:26px 0 28px!important;
  border:0!important;
  border-bottom:1px solid #cfd8e2!important;
  border-radius:0!important;
  box-shadow:none!important;
  background:transparent!important;
  transform:none!important;
  overflow:visible!important;
}
.journal-layout .article-card:hover{
  border-color:#9aaabd!important;
  box-shadow:none!important;
  transform:none!important;
  background:#f8fafc!important;
}
.journal-layout .ac-thumb,
.journal-layout .ac-tags,
.journal-layout .ac-meta > *:not(.ac-date){
  display:none!important;
}
.journal-layout .ac-body{
  padding:0 12px!important;
}
.journal-layout .ac-meta{
  margin:0 0 8px!important;
}
.journal-layout .ac-date{
  display:block!important;
  color:#64748b!important;
  font-size:.8rem!important;
  font-weight:800!important;
  letter-spacing:.04em!important;
}
.journal-layout .ac-title{
  margin:0 0 9px!important;
  color:var(--navy)!important;
  font-family:'Noto Serif JP',serif!important;
  font-size:clamp(1.06rem,2vw,1.28rem)!important;
  line-height:1.65!important;
}
.journal-layout .ac-excerpt{
  max-width:820px!important;
  color:var(--text-soft)!important;
  font-size:.92rem!important;
  line-height:1.9!important;
}
.journal-support-sections{
  margin:48px 0 0!important;
  padding:32px 0 0!important;
  border:0!important;
  border-top:2px solid var(--navy)!important;
  border-radius:0!important;
  background:transparent!important;
}
.journal-support-grid{
  display:block!important;
}
.journal-support-card{
  padding:22px 0!important;
  border:0!important;
  border-bottom:1px solid #cfd8e2!important;
  border-radius:0!important;
  background:transparent!important;
}
.journal-support-card a{
  display:inline!important;
}
.page-hero-kicker{
  text-transform:none!important;
  letter-spacing:.03em!important;
  border-radius:3px!important;
}
@media(max-width:700px){
  .journal-layout{width:min(calc(100% - 30px),960px)!important;padding:48px 0 64px!important}
  .journal-layout .article-card,.journal-layout .article-card.ac-featured{padding:22px 0 24px!important}
  .journal-layout .ac-body{padding:0!important}
}
</style>
'''
if '</head>' not in text:
    raise RuntimeError('journal: closing head not found')
text = text.replace('</head>', style + '</head>', 1)

required = [
    '論考・調査報告</div>',
    'journal-prose-index-20260710',
    '.article-card.ac-featured',
]
for item in required:
    if item not in text:
        raise RuntimeError(f'journal: missing {item}')

path.write_text(text, encoding='utf-8')
print(f'journal.html: {before} -> {len(text)} bytes')
