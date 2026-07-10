from pathlib import Path
import re


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: expected 1 occurrence, found {count}")
    return text.replace(old, new, 1)

# research-index.html
p = Path('research-index.html')
s = p.read_text(encoding='utf-8')
s = replace_once(s, '<h2>資料を検証するときの4原則</h2>', '<h2>資料確認の基準</h2>', 'research heading')
s = replace_once(
    s,
    '資料の量より、論点・作成主体・根拠・次の照会を分けることが重要です。以下の4原則で読み方を揃えてから、必要な一次資料へ進みます。',
    '資料の量より、論点・作成主体・根拠・次の照会を分けることが重要です。各資料は、次の4点を確認して扱います。',
    'research intro',
)
for heading in ('読む順番', '資料ページの使い分け'):
    pattern = rf'<section class="ri-panel"><h2>{re.escape(heading)}</h2>.*?</section>'
    s, n = re.subn(pattern, '', s, count=1, flags=re.S)
    if n != 1:
        raise SystemExit(f'research section {heading}: expected 1 occurrence, found {n}')
s = replace_once(s, '<div class="ri-grid">', '<h2 class="ri-list-title">公開資料</h2><div class="ri-grid">', 'research list heading')
s = replace_once(s, '5論点と関連条文を整理する正本ページ。', '関連法令と確認順を整理。', 'research law description')
s = replace_once(s, 'PTA問題の全体像を5軸で読む。', '入会、個人情報、会費、教職員関与、施設利用を横断して整理。', 'research report description')
research_css = '''
<style id="research-index-final-simplify-20260710">
body.ri-editorial .ri-list-title{
  margin:58px 0 10px!important;
  padding:0 0 12px!important;
  border-bottom:2px solid #1e3a5f!important;
  color:#1e3a5f!important;
  font-family:'Noto Serif JP',serif!important;
  font-size:clamp(1.45rem,2.8vw,2rem)!important;
}
body.ri-editorial .ri-grid{
  padding-top:0!important;
  border-top:0!important;
}
</style>
'''
s = replace_once(s, '</head>', research_css + '</head>', 'research css')
p.write_text(s, encoding='utf-8')

# national-archive.html
p = Path('national-archive.html')
s = p.read_text(encoding='utf-8')
s = replace_once(s, '<body>', '<body class="archive-editorial">', 'archive body class')
s = replace_once(s, '<div class="kicker">NATIONAL ARCHIVE</div>', '', 'archive hero kicker')
old_buttons = '<div class="btns"><a class="btn gold" href="#archive-map">地図を見る</a><a class="btn gold" href="#national-list">自治体別資料へ</a><a class="btn outline" href="https://drive.google.com/drive/folders/1tbfpjRNJIhwQypk1vsAOaE7_qwW-lrm5">原本フォルダ</a></div>'
new_buttons = '<p class="archive-source-link"><a href="https://drive.google.com/drive/folders/1tbfpjRNJIhwQypk1vsAOaE7_qwW-lrm5">全国PTA資料の原本フォルダを開く</a></p>'
s = replace_once(s, old_buttons, new_buttons, 'archive hero links')
map_pattern = r'<section class="section" id="archive-map">.*?</section>'
map_replacement = '''<section class="section" id="archive-map"><div class="wrap"><h2 class="title">資料取得・掲載自治体マップ</h2><p class="lead">地図上のピンから各自治体の資料へ移動できます。地図が表示されない場合は、下の自治体別資料から確認できます。</p><div class="map" id="archiveJapanMap"></div></div></section>'''
s, n = re.subn(map_pattern, map_replacement, s, count=1, flags=re.S)
if n != 1:
    raise SystemExit(f'archive map section: expected 1 occurrence, found {n}')
list_pattern = r'<section class="section white" id="national-list">.*?</section>'
list_replacement = '''<section class="section white" id="national-list"><div class="wrap"><h2 class="title">自治体別資料</h2><p class="lead">自治体名を開くと、学校別資料、確認済み資料、原本フォルダを確認できます。</p><div class="archive-list" id="archiveList"></div></div></section>'''
s, n = re.subn(list_pattern, list_replacement, s, count=1, flags=re.S)
if n != 1:
    raise SystemExit(f'archive list section: expected 1 occurrence, found {n}')
related_pattern = r'<section class="section"><div class="wrap"><div class="kicker">RELATED PAGES</div><h2 class="title">関連論点</h2>.*?</section>'
s, n = re.subn(related_pattern, '', s, count=1, flags=re.S)
if n != 1:
    raise SystemExit(f'archive related section: expected 1 occurrence, found {n}')
archive_css = '''
<style id="national-archive-editorial-20260710">
.archive-editorial{background:#fff!important}
.archive-editorial .topbar b{
  padding:0!important;
  background:transparent!important;
  color:#fff!important;
  border-radius:0!important;
}
.archive-editorial .hero{
  padding:68px 0 58px!important;
  border-bottom:1px solid #071a30!important;
}
.archive-editorial .archive-source-link{
  margin:22px 0 0!important;
}
.archive-editorial .archive-source-link a{
  color:#f8e39b!important;
  font-weight:900!important;
  text-decoration:underline!important;
}
.archive-editorial .section{
  padding:58px 0!important;
  background:#fff!important;
}
.archive-editorial .map{
  width:100%!important;
  margin-top:24px!important;
  border-radius:0!important;
  box-shadow:none!important;
}
.archive-editorial .archive-list{
  margin-top:24px!important;
  border-top:2px solid var(--navy)!important;
}
.archive-editorial .city-fold summary::after{
  padding:0!important;
  border:0!important;
  border-radius:0!important;
  text-decoration:underline!important;
}
.archive-editorial .group{
  padding:24px 0!important;
  background:#fff!important;
  border:0!important;
  border-top:1px solid var(--line)!important;
  border-radius:0!important;
  box-shadow:none!important;
}
.archive-editorial .cards{
  display:block!important;
}
.archive-editorial .card{
  margin:0!important;
  padding:18px 0 18px 18px!important;
  border:0!important;
  border-left:4px solid var(--red)!important;
  border-bottom:1px solid #e5e7eb!important;
  border-radius:0!important;
  box-shadow:none!important;
}
.archive-editorial .card.y{border-left-color:#b08a00!important}
.archive-editorial .card.info-card{border-left-color:#0b66a3!important}
.archive-editorial .point{
  padding:10px 0!important;
  background:transparent!important;
  border:0!important;
  border-radius:0!important;
}
.archive-editorial .chip{
  padding:0!important;
  background:transparent!important;
  border:0!important;
  border-radius:0!important;
  text-decoration:underline!important;
}
.archive-editorial .badge{
  border-radius:0!important;
}
</style>
'''
s = replace_once(s, '</head>', archive_css + '</head>', 'archive css')
p.write_text(s, encoding='utf-8')
