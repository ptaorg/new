from pathlib import Path
import re

p = Path('journal.html')
s = p.read_text(encoding='utf-8')

# Remove the original card/filter/sidebar style block.
s, count = re.subn(
    r'<style>\s*\.journal-layout\{.*?</style>',
    '',
    s,
    count=1,
    flags=re.S,
)
if count != 1:
    raise SystemExit(f'original journal style block: expected 1, found {count}')

# Remove the two accumulated override blocks and replace them with one concise index stylesheet.
for style_id in ('journal-prose-index-20260710', 'journal-index-final-20260710'):
    s, count = re.subn(
        rf'\s*<style id="{style_id}">.*?</style>',
        '',
        s,
        count=1,
        flags=re.S,
    )
    if count != 1:
        raise SystemExit(f'{style_id}: expected 1, found {count}')

clean_css = r'''
<style id="journal-index-20260711">
.journal-page .journal-layout{
  width:min(calc(100% - 40px),920px);
  margin-inline:auto;
  padding:64px 0 88px;
}
.journal-page .journal-list-heading{
  margin:0 0 10px;
  color:var(--navy);
  font-family:'Noto Serif JP',serif;
  font-size:clamp(1.65rem,3vw,2.25rem);
  line-height:1.5;
}
.journal-page .journal-list-lead{
  max-width:780px;
  margin:0 0 34px;
  color:var(--text-soft);
  font-size:.98rem;
  line-height:1.95;
}
.journal-page .article-list{border-top:2px solid var(--navy)}
.journal-page .article-card{
  display:block;
  padding:25px 10px 27px;
  border-bottom:1px solid #cfd8e2;
  color:inherit;
  text-decoration:none;
}
.journal-page .article-card:hover{background:#f7f9fb}
.journal-page .ac-meta{margin:0 0 7px}
.journal-page .ac-date{color:#64748b;font-size:.8rem;font-weight:800;letter-spacing:.04em}
.journal-page .ac-title{
  margin:0 0 8px;
  color:var(--navy);
  font-family:'Noto Serif JP',serif;
  font-size:clamp(1.06rem,2vw,1.3rem);
  line-height:1.65;
  font-weight:900;
}
.journal-page .ac-excerpt{
  max-width:820px;
  color:var(--text-soft);
  font-size:.93rem;
  line-height:1.9;
}
.journal-page .journal-support-sections{
  margin:48px 0 0;
  padding:32px 0 0;
  border-top:2px solid var(--navy);
}
.journal-page .journal-support-grid{display:block}
.journal-page .journal-support-card{padding:22px 0;border-bottom:1px solid #cfd8e2}
.journal-page .journal-support-card h3{margin:0 0 8px;color:var(--navy);font-size:1.05rem}
.journal-page .journal-support-card p{margin:0 0 12px;color:var(--text-soft);font-size:.9rem;line-height:1.8}
.journal-page .journal-support-card a{color:var(--blue);font-weight:800;text-decoration:none}
.journal-page .page-hero-kicker{padding:0!important;border:0!important;border-radius:0!important;background:transparent!important;text-transform:none!important;letter-spacing:.04em!important}
@media(max-width:700px){
  .journal-page .journal-layout{width:min(calc(100% - 30px),920px);padding:48px 0 64px}
  .journal-page .article-card{padding:22px 0 24px}
}
</style>
'''
if '</head>' not in s:
    raise SystemExit('closing head not found')
s = s.replace('</head>', clean_css + '</head>', 1)

# Remove obsolete filter metadata and emphasis classes from the list items.
s = re.sub(r'\s+data-cat="[^"]+"', '', s)
s = s.replace('class="article-card ac-featured"', 'class="article-card"')
s = s.replace('<!-- Sidebar -->', '')

p.write_text(s, encoding='utf-8')
