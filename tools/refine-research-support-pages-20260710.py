from pathlib import Path
import re


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'{label}: expected 1 occurrence, found {count}')
    return text.replace(old, new, 1)


def remove_once(text: str, pattern: str, label: str) -> str:
    text, count = re.subn(pattern, '', text, count=1, flags=re.S)
    if count != 1:
        raise SystemExit(f'{label}: expected 1 occurrence, found {count}')
    return text

# ------------------------------------------------------------
# guide-research.html
# ------------------------------------------------------------
p = Path('guide-research.html')
s = p.read_text(encoding='utf-8')
s = replace_once(
    s,
    'PTA問題を扱うときは、感想や単発事例ではなく、法令、行政回答、学校配布文書、PTA会則、会費資料、個人情報同意書を分けて読む必要があります。このページは、資料の入口ではなく、資料をどう検証するかの方法論です。',
    'PTA問題を検証するときは、法令、行政回答、学校配布文書、PTA会則、会費資料、個人情報関係文書を区別し、作成主体、対象時点、学校関与、根拠文書を確認します。',
    'research hero paragraph',
)
s = remove_once(s, r'<section class="research-panel" id="sources">.*?</section>', 'research sources hub')
s = replace_once(
    s,
    '<li>学校がPTAへ提供した個人情報の項目、利用目的、提供記録、本人説明はあるか。</li>',
    '<li>学校が保有情報をPTA目的で自ら利用し、又はPTAへ提供しているか。対象項目、利用目的、法的根拠、提供記録、本人説明はあるか。</li>',
    'research privacy question',
)
s = replace_once(
    s,
    '<li>PTA会費は学校徴収金と分離されているか。学校が徴収する場合、委任や同意はあるか。</li>',
    '<li>PTA会費は学校徴収金と分離されているか。学校が関与する場合、会員関係、口座情報の利用、校務・服務、決裁、会計区分を説明できるか。</li>',
    'research fee question',
)
research_css = '''
<style id="guide-research-final-20260710">
body.research-editorial .research-kicker,
body.research-editorial .method-card>span{display:none!important}
body.research-editorial .method-card{padding:20px 0!important}
</style>
'''
s = replace_once(s, '</head>', research_css + '</head>', 'research css')
p.write_text(s, encoding='utf-8')

# ------------------------------------------------------------
# evidence-checklist.html
# ------------------------------------------------------------
p = Path('evidence-checklist.html')
s = p.read_text(encoding='utf-8')
s = remove_once(s, r'<div class="ec-links">.*?</div>', 'evidence hero links')
s = replace_once(
    s,
    '<li>学校保有情報をPTA目的に使っていないか。</li>',
    '<li>学校が保有情報をPTA目的で自ら利用しているか、又はPTAへ提供しているかを分けて確認したか。</li>',
    'evidence privacy bullet',
)
s = replace_once(
    s,
    '<li>学校が徴収する場合、委任・同意・会員名簿があるか。</li>',
    '<li>学校が関与する場合、加入・会費債務、口座情報の利用、校務・服務、決裁、会計区分を確認できるか。</li>',
    'evidence fee bullet',
)
evidence_css = '''
<style id="evidence-checklist-editorial-20260710">
.ec-page{background:#fff!important}
.ec-wrap{width:min(calc(100% - 40px),920px)!important}
.ec-list{display:block!important;padding:0!important;border-top:2px solid #1e3a5f!important}
.ec-card,
.ec-section,
.ec-box,
.ec-note{
  border-radius:0!important;
  box-shadow:none!important;
  background:#fff!important;
}
.ec-card{
  padding:26px 0!important;
  border:0!important;
  border-bottom:1px solid #dbe4ee!important;
}
.ec-section{
  margin:0!important;
  padding:38px 0!important;
  border:0!important;
  border-bottom:1px solid #cfd8e2!important;
}
.ec-section h2{border-bottom:0!important;padding-bottom:0!important}
.ec-flow{gap:0!important;border-top:1px solid #dbe4ee!important}
.ec-flow li{
  padding:18px 0 18px 42px!important;
  background:#fff!important;
  border:0!important;
  border-bottom:1px solid #dbe4ee!important;
  border-radius:0!important;
}
.ec-flow li::before{left:0!important;border-radius:0!important}
.ec-matrix{display:block!important;border-top:1px solid #dbe4ee!important}
.ec-box{padding:18px 0!important;border:0!important;border-bottom:1px solid #dbe4ee!important}
</style>
'''
s = replace_once(s, '</head>', evidence_css + '</head>', 'evidence css')
p.write_text(s, encoding='utf-8')

# ------------------------------------------------------------
# key-materials.html
# ------------------------------------------------------------
p = Path('key-materials.html')
s = p.read_text(encoding='utf-8')
replacements = {
    '<title>最重要資料5件 | PTA適正化推進委員会</title>': '<title>主要な行政・法令資料 | PTA適正化推進委員会</title>',
    '<meta property="og:title" content="最重要資料5件 | PTA適正化推進委員会">': '<meta property="og:title" content="主要な行政・法令資料 | PTA適正化推進委員会">',
    '<h1>最重要資料5件</h1>': '<h1>主要な行政・法令資料</h1>',
    'PTA運営の適正化を確認するとき、最初に見るべき資料を5件に絞りました。長い資料一覧へ入る前に、任意加入、個人情報、会費徴収、教職員関与、学校施設利用の根拠をここで押さえます。': 'PTA運営を確認する際に参照頻度の高い行政通知、公的資料、法令本文をまとめています。各資料の対象と射程を確認し、実際の学校・PTA文書と照合します。',
    '公立学校とPTAの間で個人情報をやり取りする場合に、利用目的、本人説明、第三者提供、目的外利用、記録確認を検討するための資料です。学校が保有する児童・保護者情報を、PTAの加入管理や会費徴収に流用できるかを点検するときに使います。': '公立学校が保有情報をPTA目的で自ら利用し、又はPTAへ提供する場合に、利用目的、法第61条・第69条の根拠、本人説明、不同意者の除外、提供記録を確認するための資料です。',
    '学校徴収金の公会計化、学校・教師の負担軽減、学校以外が担うべき業務を確認する資料です。PTA会費を学校徴収金に混ぜる運用を点検する際に使います。': '学校給食費以外の学校徴収金について、公会計化に加え、保護者が業者等へ直接支払い学校を経由しない方法を示した資料です。PTA会費を直接規律する通知ではありませんが、学校徴収金とPTA会費の関与を比較する資料になります。',
    '<li>PTAが社会教育関係団体として、学校や教育委員会から統制的支配を受けていないか。</li>': '<li>PTAの目的・活動が社会教育法10条の社会教育関係団体に当たる場合、学校や教育委員会の関与が12条の不当な統制的支配に当たらないか。</li>',
    '<div class="km-note"><strong>使い方：</strong>': '<div class="km-note"><strong>確認時の注意：</strong>',
}
for old, new in replacements.items():
    s = replace_once(s, old, new, f'key materials: {old[:40]}')
s = remove_once(s, r'<div class="km-nav">.*?</div>', 'key materials nav')
s = remove_once(s, r'<section class="km-intro">.*?</section>', 'key materials intro')
key_css = '''
<style id="key-materials-editorial-20260710">
.km-page{background:#fff!important}
.km-wrap{width:min(calc(100% - 40px),920px)!important}
.km-list{gap:0!important;padding:48px 0 86px!important;border-top:2px solid #1e3a5f!important}
.km-card{
  padding:30px 0!important;
  border:0!important;
  border-bottom:1px solid #dbe4ee!important;
  border-radius:0!important;
  box-shadow:none!important;
}
.km-card::before{display:none!important}
.km-card h2{padding-left:0!important}
.km-links{gap:8px 18px!important}
.km-links a{
  padding:0!important;
  border:0!important;
  border-radius:0!important;
  background:transparent!important;
  color:#174f7d!important;
  text-decoration:underline!important;
}
</style>
'''
s = replace_once(s, '</head>', key_css + '</head>', 'key css')
p.write_text(s, encoding='utf-8')

# ------------------------------------------------------------
# case-reading.html
# ------------------------------------------------------------
p = Path('case-reading.html')
s = p.read_text(encoding='utf-8')
replacements = {
    '<title>判例の読み方 | PTA適正化推進委員会</title>': '<title>判例検証の基準 | PTA適正化推進委員会</title>',
    '<meta property="og:title" content="判例の読み方 | PTA適正化推進委員会">': '<meta property="og:title" content="判例検証の基準 | PTA適正化推進委員会">',
    '<h1>判例の読み方</h1>': '<h1>判例検証の基準</h1>',
    '<h2>判例を読む前提</h2>': '<h2>判例を検証する前提</h2>',
    '<h2>読む順番</h2>': '<h2>確認項目</h2>',
}
for old, new in replacements.items():
    s = replace_once(s, old, new, f'case reading: {old[:35]}')
s = remove_once(s, r'<section class="panel"><h2>関連ページ</h2>.*?</section>', 'case related links')
case_css = '''
<style id="case-reading-editorial-20260710">
.simple-article{background:#fff!important}
.simple-wrap{width:min(calc(100% - 40px),920px)!important}
.panel{
  margin:0!important;
  padding:38px 0!important;
  border:0!important;
  border-bottom:1px solid #cfd8e2!important;
  border-radius:0!important;
  box-shadow:none!important;
}
.panel h2{border-bottom:0!important;padding-bottom:0!important}
.grid{display:block!important;border-top:1px solid #dbe4ee!important}
.card{padding:18px 0!important;border:0!important;border-bottom:1px solid #dbe4ee!important;border-radius:0!important;background:#fff!important}
.case-flow{gap:0!important;border-top:1px solid #dbe4ee!important}
.case-flow li{padding:18px 0 18px 42px!important;border:0!important;border-bottom:1px solid #dbe4ee!important;border-radius:0!important;background:#fff!important}
.case-flow li::before{left:0!important;border-radius:0!important}
.notice{border-radius:0!important;box-shadow:none!important}
</style>
'''
s = replace_once(s, '</head>', case_css + '</head>', 'case css')
p.write_text(s, encoding='utf-8')

# ------------------------------------------------------------
# timeline-issues.html
# ------------------------------------------------------------
p = Path('timeline-issues.html')
s = p.read_text(encoding='utf-8')
replacements = {
    '<title>制度史から現在の論点へ | PTA適正化推進委員会</title>': '<title>PTA制度史と現在の学校関与 | PTA適正化推進委員会</title>',
    '<meta property="og:title" content="制度史から現在の論点へ | PTA適正化推進委員会">': '<meta property="og:title" content="PTA制度史と現在の学校関与 | PTA適正化推進委員会">',
    '<h1>制度史から現在の論点へ</h1>': '<h1>PTA制度史と現在の学校関与</h1>',
    'PTAは社会教育関係団体として整理されます。ここから導かれるのは、行政がPTA内部を統制してよいという結論ではありません。': 'PTAの目的・活動が社会教育法10条の要件に当たる場合、社会教育関係団体として扱われます。ここから導かれるのは、行政がPTA内部を統制してよいという結論ではありません。',
    '<div class="ti-note"><strong>使い方：</strong>': '<div class="ti-note"><strong>確認時の注意：</strong>',
}
for old, new in replacements.items():
    s = replace_once(s, old, new, f'timeline issues: {old[:40]}')
s = remove_once(s, r'<div class="ti-nav">.*?</div>', 'timeline nav')
s, link_count = re.subn(r'<div class="ti-linkbox">.*?</div>', '', s, flags=re.S)
if link_count != 4:
    raise SystemExit(f'timeline linkboxes: expected 4, found {link_count}')
timeline_css = '''
<style id="timeline-issues-editorial-20260710">
.ti-page{background:#fff!important}
.ti-wrap{width:min(calc(100% - 40px),920px)!important}
.ti-intro,
.ti-card,
.ti-box,
.ti-note{
  border-radius:0!important;
  box-shadow:none!important;
  background:#fff!important;
}
.ti-intro{margin:0!important;padding:42px 0!important;border:0!important;border-bottom:1px solid #cfd8e2!important}
.ti-grid{display:block!important;border-top:1px solid #dbe4ee!important}
.ti-box{padding:18px 0!important;border:0!important;border-bottom:1px solid #dbe4ee!important}
.ti-list{gap:0!important;padding:0 0 86px!important}
.ti-card{padding:34px 0!important;border:0!important;border-bottom:1px solid #cfd8e2!important}
.ti-card h2{border-bottom:0!important;padding-bottom:0!important}
</style>
'''
s = replace_once(s, '</head>', timeline_css + '</head>', 'timeline css')
p.write_text(s, encoding='utf-8')
