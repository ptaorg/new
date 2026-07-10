from pathlib import Path
import re

p = Path('documents.html')
s = p.read_text(encoding='utf-8')

# Remove the duplicated featured pack and diagram. All useful destinations are
# retained below as direct entries in the document/form section.
pattern = r'<section class="doc-sec featured-pack" id="legal-template-pack">.*?</section>'
s, count = re.subn(pattern, '', s, count=1, flags=re.S)
if count != 1:
    raise SystemExit(f'featured pack: expected 1 section, found {count}')

s = s.replace('<h2>配布資料・テンプレート</h2>', '<h2 id="legal-template-pack">提出文書・書式</h2>', 1)
s = s.replace(
    '<p>そのまま印刷・提出・配布できる形に整えた資料です。</p>',
    '<p>提出先と確認目的に応じて、必要な文書または書式を直接開けます。</p>',
    1,
)

old_grid = '''<div class="doc-grid">
<a class="doc-item gold" href="submission-kit.html"><strong>提出文書キット</strong><span>学校・PTA・教育委員会への確認文例、会費分離申入書、個人情報確認書、根拠整理メモ。</span></a>
<a class="doc-item" href="claim-evidence-ledger.html"><strong>主張と根拠の対応表</strong><span>主張、根拠条文、公式資料、実物文書、提出文例を一列につなげ、断定を避けて精度を保つ台帳。</span></a>
<a class="doc-item gold" href="guide-board.html#board-jp-guideline"><strong>教育委員会・学校管理職向け分離資料</strong><span>学校とPTAの分離原則を整理した行政向けガイドライン本文、通知ひな形、学校別実態調査票（PDF・Excel配布）。</span></a>
<a class="doc-item" href="PTA運営適正化ガイドブック_第4版_改訂本文.html"><strong>PTA運営適正化ガイドブック 第4版</strong><span>保護者・役員・学校向けの総合ガイドブック本文（HTML版）。</span></a>
<a class="doc-item" href="PTA運営適正化ガイドブック_第4版_改訂版.pdf"><strong>PTA運営適正化ガイドブック 第4版 PDF</strong><span>印刷・配布・保存用のPDF版。全文を紙面で確認する場合はこちらを使います。</span></a>
<a class="doc-item" href="guideline.html"><strong>PTA運営適正化ガイドライン・書式テンプレート</strong><span>入会申込書、同意書、通知文など、適正運営に必要な書式のテンプレート集。</span></a>
<a class="doc-item" href="audit/index.html"><strong>PTA運営チェックアプリ</strong><span>自校・自PTAの運営状況を設問に沿って点検できるセルフチェックツール。</span></a>
</div>'''
new_grid = '''<div class="doc-grid">
<a class="doc-item gold" href="submission-kit.html"><strong>提出文書キット</strong><span>学校、PTA、教育委員会への確認文例、会費分離申入書、個人情報確認書、根拠整理メモ。</span></a>
<a class="doc-item" href="guideline.html#tpl-board-inquiry"><strong>学校・教育委員会への確認照会書</strong><span>入会記録、学校保有情報、会費徴収、教職員関与、施設利用について、保有文書と事実関係を確認する書式。</span></a>
<a class="doc-item" href="guideline.html#tpl-fee-separation"><strong>PTA会費徴収分離申入書</strong><span>学校徴収金とPTA会費の通知、口座、引落し、未納管理を分けるための申入書。</span></a>
<a class="doc-item" href="guideline.html#template-pack"><strong>入会・個人情報関係の書式</strong><span>入会申込、利用目的の説明、本人同意等を記録する書式を確認。</span></a>
<a class="doc-item gold" href="guide-board.html#board-jp-guideline"><strong>教育委員会・学校管理職向け分離資料</strong><span>学校とPTAの関与範囲を確認する行政向け本文、通知ひな形、学校別実態調査票。</span></a>
<a class="doc-item" href="PTA運営適正化ガイドブック_第4版_改訂本文.html"><strong>PTA運営適正化ガイドブック 第4版</strong><span>保護者、役員、学校向けの総合ガイドブック本文。</span></a>
<a class="doc-item" href="PTA運営適正化ガイドブック_第4版_改訂版.pdf"><strong>PTA運営適正化ガイドブック 第4版 PDF</strong><span>印刷、配布、保存用のPDF版。</span></a>
<a class="doc-item" href="guideline.html"><strong>PTA運営適正化ガイドライン</strong><span>入会、個人情報、会費、教職員関与、施設利用の確認事項と書式をまとめた実務資料。</span></a>
<a class="doc-item" href="audit/index.html"><strong>PTA運営チェック</strong><span>現在の運営状況を設問に沿って点検するチェックツール。</span></a>
</div>'''
if old_grid not in s:
    raise SystemExit('template grid not found')
s = s.replace(old_grid, new_grid, 1)

# Remove obsolete CSS for the deleted featured-pack components, and keep the
# remaining index as a simple vertical bibliography.
extra_css = '''
<style id="documents-final-index-20260710">
body.documents-editorial .doc-sec.featured-pack,
body.documents-editorial .doc-pack-layout,
body.documents-editorial .doc-pack-grid,
body.documents-editorial .doc-pack-card,
body.documents-editorial .doc-diagram{display:none!important}
body.documents-editorial .doc-index{max-width:920px!important}
body.documents-editorial .doc-sec>p{max-width:780px!important}
body.documents-editorial .doc-item,
body.documents-editorial .doc-item.gold{
  grid-template-columns:minmax(220px,280px) minmax(0,1fr)!important;
}
@media(max-width:760px){
  body.documents-editorial .doc-item,
  body.documents-editorial .doc-item.gold{grid-template-columns:1fr!important}
}
</style>
'''
if '</head>' not in s:
    raise SystemExit('head end not found')
s = s.replace('</head>', extra_css + '</head>', 1)
p.write_text(s, encoding='utf-8')
