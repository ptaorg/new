from pathlib import Path
import re

p = Path('journal.html')
s = p.read_text(encoding='utf-8')

# Update the short explanation and old navigation anchor/name.
s = s.replace(
    '掲載中の論考・調査報告です。PDF・スライド・関連ページは補助セクションに分けています。',
    '掲載中の論考・調査報告を年月順に掲載しています。題名と概要から個別記事へ進みます。',
    1,
)
s = s.replace('/index.html#audience-gateway', '/index.html#roles')
s = s.replace('運営チェックアプリ', '運営チェック')

# Remove category filters. The list is a bibliography, not an interactive hub.
s, count = re.subn(r'\s*<div class="category-bar">.*?</div>', '', s, count=1, flags=re.S)
if count != 1:
    raise SystemExit(f'category bar: expected 1, found {count}')

# Remove visual/status metadata from every bibliography entry.
s, thumb_count = re.subn(r'\s*<div class="ac-thumb".*?</div>', '', s, flags=re.S)
s, tag_count = re.subn(r'\s*<div class="ac-tags">.*?</div>', '', s, flags=re.S)
s, reading_count = re.subn(r'<span class="ac-reading">.*?</span>', '', s, flags=re.S)
s, status_count = re.subn(r'<span style="background:#e0f2fe;[^>]*>.*?</span>', '', s, flags=re.S)
if thumb_count < 5 or tag_count < 5 or reading_count < 5:
    raise SystemExit(f'entry cleanup too small: thumbs={thumb_count}, tags={tag_count}, readings={reading_count}, statuses={status_count}')

# Remove duplicate support cards and the full-text republication archive.
s, support_count = re.subn(r'\s*<section aria-labelledby="journal-support-title" class="journal-support-sections">.*?</section>', '', s, count=1, flags=re.S)
if support_count != 1:
    raise SystemExit(f'support section: expected 1, found {support_count}')
s, archive_count = re.subn(r'\s*<section aria-labelledby="journal-fulltext-title" class="journal-fulltext-archive" id="journal-fulltext-archive">.*?</section>', '', s, count=1, flags=re.S)
if archive_count != 1:
    raise SystemExit(f'fulltext archive: expected 1, found {archive_count}')

# Remove the right-hand category/related-links sidebar.
s, sidebar_count = re.subn(r'\s*<aside class="sidebar-section">.*?</aside>', '', s, count=1, flags=re.S)
if sidebar_count != 1:
    raise SystemExit(f'sidebar: expected 1, found {sidebar_count}')

# Remove the category-filter and obsolete slide-viewer script/modal.
s, script_count = re.subn(r'\s*<script>\s*function filterCat\(cat,btn\).*?</script>', '', s, count=1, flags=re.S)
if script_count != 1:
    raise SystemExit(f'filter/slide script: expected 1, found {script_count}')
s, modal_count = re.subn(r'\s*<!-- スライドビューワーモーダル -->.*?<script>\s*document\.getElementById\(\'slideModal\'\).*?</script>', '', s, count=1, flags=re.S)
if modal_count != 1:
    raise SystemExit(f'slide modal: expected 1, found {modal_count}')

# Remove CSS that only served the deleted full-text archive and older card pass.
s, fulltext_css_count = re.subn(r'\s*<style id="journal-fulltext-styles">.*?</style>', '', s, count=1, flags=re.S)
if fulltext_css_count != 1:
    raise SystemExit(f'fulltext css: expected 1, found {fulltext_css_count}')
s, old_card_css_count = re.subn(r'\s*<style id="journal-editorial-design">.*?</style>', '', s, count=1, flags=re.S)
if old_card_css_count != 1:
    raise SystemExit(f'old card css: expected 1, found {old_card_css_count}')

# Strengthen the final bibliography layout without adding another hub.
extra_css = '''
<style id="journal-index-final-20260710">
.journal-page .journal-layout{width:min(calc(100% - 40px),920px)!important;display:block!important;padding:64px 0 88px!important}
.journal-page .article-list{border-top:2px solid var(--navy)!important}
.journal-page .article-card{display:block!important;padding:25px 0 27px!important;border:0!important;border-bottom:1px solid #cfd8e2!important;border-radius:0!important;box-shadow:none!important;background:transparent!important;transform:none!important}
.journal-page .article-card:hover{background:#f7f9fb!important;box-shadow:none!important;transform:none!important}
.journal-page .ac-body{padding:0 10px!important}
.journal-page .ac-meta{margin:0 0 7px!important}
.journal-page .ac-date{font-size:.8rem!important;color:#64748b!important;font-weight:800!important}
.journal-page .ac-title{font-family:'Noto Serif JP',serif!important;font-size:clamp(1.06rem,2vw,1.3rem)!important;line-height:1.65!important;margin:0 0 8px!important}
.journal-page .ac-excerpt{max-width:820px!important;font-size:.93rem!important;line-height:1.9!important;color:var(--text-soft)!important}
.journal-page .page-hero-kicker{padding:0!important;border:0!important;border-radius:0!important;background:transparent!important;text-transform:none!important;letter-spacing:.04em!important}
@media(max-width:700px){.journal-page .journal-layout{width:min(calc(100% - 30px),920px)!important;padding:48px 0 64px!important}.journal-page .ac-body{padding:0!important}}
</style>
'''
if '</head>' not in s:
    raise SystemExit('head close missing')
s = s.replace('</head>', extra_css + '</head>', 1)

p.write_text(s, encoding='utf-8')
