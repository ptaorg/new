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

p = Path('claim-evidence-ledger.html')
s = p.read_text(encoding='utf-8')

s = replace_once(s, '<div class="submission-eyebrow">Evidence Ledger</div>', '', 'English eyebrow')
s = remove_once(s, r'<div class="submission-links">.*?</div>', 'hero jump links')
s = replace_once(s, '<h2>このページの位置づけ</h2>', '<h2>根拠台帳の目的</h2>', 'purpose heading')
s = replace_once(
    s,
    'この対応表では、主張ごとに「根拠資料」「確認すべき実物資料」「次に出す文書」「まだ断定しない点」を並べます。教育委員会や学校へ出す文章の前段階として、主張の強さを確認するページです。',
    'この対応表では、確認軸ごとに「根拠資料」「確認すべき実物資料」「提出文書」「留保事項」を並べます。教育委員会や学校へ文書を出す前に、事実と評価を区別するための台帳です。',
    'purpose paragraph',
)
s = replace_once(s, '<h2>根拠の強さを5段階で分ける</h2>', '<h2>資料の区分</h2>', 'grade heading')
for old, new in {
    '<strong>A 法令・公式資料</strong>': '<strong>法令・公式資料</strong>',
    '<strong>B 自治体通知・教育委員会回答</strong>': '<strong>自治体通知・教育委員会回答</strong>',
    '<strong>C 実物文書</strong>': '<strong>実物文書</strong>',
    '<strong>D 複数資料からの分析</strong>': '<strong>複数資料からの分析</strong>',
    '<strong>E 未確認事項</strong>': '<strong>未確認事項</strong>',
}.items():
    s = replace_once(s, old, new, old)

s = replace_once(
    s,
    '<td>学校保有情報をPTA会員管理へ当然に利用することはできない。</td>',
    '<td>学校保有情報をPTA目的で扱う場合は、学校自身による利用とPTAへの提供を分け、第61条・第69条の根拠を確認する。</td>',
    'privacy claim',
)
s = replace_once(
    s,
    '<td>提供目的、本人同意、マスキング、提供記録の有無を分ける。PTA加入同意と個人情報提供同意は別に確認する。</td>',
    '<td>学校自身の利用かPTAへの提供かを分け、所掌事務・業務、利用目的、第69条第2項の例外、本人同意、不同意者の除外、利用・提供記録を確認する。PTA加入意思と情報利用・提供への同意も区別する。</td>',
    'privacy reservation',
)
s = replace_once(
    s,
    '<td>民法上の会費債務整理、文部科学省の学校徴収金公会計化資料、横浜市通知、教育委員会回答。</td>',
    '<td>民法上の会員関係・会費債務、個人情報保護法61条・69条、学校側の校務・服務・会計規程、横浜市通知、教育委員会回答。2025年の学校徴収金通知は、PTA会費を直接規律するものではなく、学校教育関係費を学校外へ移す政策方向との比較資料として扱う。</td>',
    'fee sources',
)
s = replace_once(
    s,
    '<td>学校が単に配布したのか、徴収・督促・返金まで関与したのかで評価が変わる。口座名義と未納対応の主体を確認する。</td>',
    '<td>学校が単に配布したのか、口座情報を利用し、徴収・督促・返金まで関与したのかで評価が変わる。会員確認、口座名義、校務・服務、決裁、未納対応、会計責任を確認する。</td>',
    'fee reservation',
)
s = replace_once(
    s,
    'E-002,個人情報同意書・名簿提供記録,,,,,個人情報資料,学校保有情報のPTA利用,要原資料確認,,privacy.html,',
    'E-002,個人情報同意書・利用提供記録,,,,,個人情報資料,学校保有情報のPTA目的利用・提供,要原資料確認,,privacy.html,',
    'ledger privacy row',
)
s = replace_once(s, '<h2>表現の線引き</h2>', '<h2>事実・確認事項・評価の区別</h2>', 'phrasing heading')
s = replace_once(s, '<h2>根拠資料と関連ページ</h2>', '<h2>参照資料</h2>', 'sources heading')
s = replace_once(
    s,
    '<p>横浜市通知は、入会届、個人情報同意、会費説明を同時に整理する重要資料として扱います。公式資料は、現場の実物文書と対応させて使います。</p>',
    '<p>公式資料は、その対象と射程を確認したうえで、現場の会則、入会書類、情報利用・提供記録、会費資料、服務・施設関係文書と照合します。</p>',
    'sources intro',
)

extra_css = '''
<style id="claim-ledger-editorial-20260710">
body.submission-main .submission-hero{
  padding:62px 0 54px!important;
}
body.submission-main .submission-body>.submission-wrap{
  width:min(calc(100% - 40px),1120px)!important;
}
body.submission-main .evidence-grade-grid{
  display:block!important;
  border-top:2px solid #1e3a5f!important;
}
body.submission-main .evidence-grade{
  padding:20px 0!important;
  border:0!important;
  border-bottom:1px solid #dbe4ee!important;
  border-radius:0!important;
  box-shadow:none!important;
  background:#fff!important;
}
body.submission-main .evidence-grade strong{
  margin-bottom:5px!important;
}
body.submission-main .submission-grid{
  display:block!important;
  border-top:1px solid #dbe4ee!important;
}
body.submission-main .submission-card{
  padding:18px 0!important;
  border:0!important;
  border-bottom:1px solid #dbe4ee!important;
  border-radius:0!important;
  box-shadow:none!important;
  background:#fff!important;
}
body.submission-main .submission-source-list{
  border-top:1px solid #dbe4ee!important;
}
body.submission-main .submission-source-list a{
  display:block!important;
  padding:12px 0!important;
  border:0!important;
  border-bottom:1px solid #dbe4ee!important;
  border-radius:0!important;
  background:transparent!important;
  text-decoration:underline!important;
}
</style>
'''
s = replace_once(s, '</head>', extra_css + '</head>', 'extra css')
p.write_text(s, encoding='utf-8')
