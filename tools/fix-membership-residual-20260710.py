from pathlib import Path
import re


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'{label}: expected 1 occurrence, found {count}')
    return text.replace(old, new, 1)


p = Path('membership.html')
s = p.read_text(encoding='utf-8')

# Restore the closing tag for the issue-content wrapper removed with the related-links block.
s = replace_once(
    s,
    '      </section>\n    </main>\n\n    <!-- ===== FAQ：よくある疑問 ===== -->',
    '      </section>\n    </main>\n  </div>\n\n    <!-- ===== FAQ：よくある疑問 ===== -->',
    'issue content closing',
)

# Delete the now-empty promotional route section.
pattern = r'\s*<!-- 適法化フロー SVG -->\s*<section class="issue-section" style="background:linear-gradient\(135deg,#f0fdf4,#dcfce7\);border-radius:var\(--radius\);padding:32px;margin-bottom:48px">.*?</section>'
s, count = re.subn(pattern, '', s, count=1, flags=re.S)
if count != 1:
    raise SystemExit(f'empty route section: expected 1, found {count}')

replacements = {
    '<strong>オプトアウト通知を送るために名簿が必要</strong>': '<strong>全保護者への通知に学校保有情報が使われる場合がある</strong>',
    '<p>「断りたい人は申し出てください」という通知を保護者に送るには、事前に全保護者の連絡先を把握していなければならない。</p>': '<p>学校が全保護者へ配布・配信する場合と、PTAが保護者情報を取得して直接通知する場合では、情報の流れと責任主体が異なります。</p>',
    '<strong>その名簿の取得経路を確認する必要がある</strong>': '<strong>学校自身の利用とPTAへの提供を分ける</strong>',
    '<p>学校（行政機関等）が保有する名簿をPTAへ提供する場合、本人同意、提供項目、不同意者の除外、提供記録などを個別に確認する必要があります。オプトアウト通知の出発点になる名簿の取得経路が不明なままでは、制度として説明が困難です。</p>': '<p>学校が自ら連絡先を利用するのか、PTAへ名簿を提供するのかを分け、第61条の所掌事務・業務、第69条第1項又は第2項の根拠、対象項目、不同意者の処理、利用・提供記録を確認します。</p>',
    '<span class="domino-law">個人情報保護法 69条</span>': '<span class="domino-law">個人情報保護法 61条・69条</span>',
    '<p>学校在籍者全員の情報を先に利用し、拒否しない人を会員と扱うオプトアウト方式は、加入意思と情報取得の双方で根拠を欠きます。PTAが加入者本人から申込みと必要情報を直接取得するオプトイン方式へ改める必要があります。</p>': '<p>全保護者へ通知できることと、PTA会員関係が成立することは別です。拒否しない人を会員と扱う方式では、本人の申込みを客観的に記録できません。恒常的な会員管理は、加入者本人から申込みと必要情報を取得するオプトイン方式へ改める必要があります。</p>',
    '<div class="cc-body">オプトアウト通知の前提となる学校名簿利用は、個人情報保護法第5章・第69条との関係で厳格に確認する必要があり、学校名簿を前提とする設計には根本的な無理が生じる。</div>': '<div class="cc-body">学校保有情報を使う場合は、学校自身の利用とPTAへの提供を分け、第61条・第69条の根拠、対象情報、記録を確認する必要があります。学校が通知できることは、入会契約の成立を意味しません。</div>',
    '<p>憲法第21条が保障する「結社の自由」には、団体を結成し加入する自由（積極的結社の自由）だけでなく、<strong>いかなる団体にも加入しない自由・退会する自由（消極的結社の自由）</strong>が含まれます。これは憲法学の通説（芦部信喜・佐藤幸治ら）および最高裁判例（南九州税理士会事件等）で確立した解釈です。</p>': '<p>憲法第21条の結社の自由は、団体を結成し加入する自由だけでなく、団体への加入を強制されない自由との関係でも論じられます。個別のPTA会員関係では民法・消費者契約法・会則等を確認し、公立学校や教育委員会の関与がある場合は公権力との関係を別に検討します。</p>',
    '<p>通知一式では、PTAの任意加入、加入届による意思確認、個人情報取扱同意、未加入家庭への配慮、学校徴収金とPTA会費を扱う場合の説明責任が整理されています。「前例どおり」ではなく、入会意思・個人情報・会費徴収を分けて確認する根拠資料として必ず参照してください。</p>': '<p>通知一式では、PTAの任意加入、加入届による意思確認、個人情報取扱同意、未加入家庭への配慮、学校徴収金とPTA会費を扱う場合の説明責任が整理されています。入会意思、個人情報、会費徴収を分けて確認する行政資料として参照します。</p>',
}
for old, new in replacements.items():
    s = replace_once(s, old, new, old[:60])

# Remove the criminal-risk callout; the page is about membership procedure, not speculative penal liability.
pattern = r'\s*<div class="alert-block danger">\s*<div class="alert-icon">🚨</div>\s*<div>\s*<p><strong>刑事リスク：</strong>.*?</p>\s*</div>\s*</div>'
s, count = re.subn(pattern, '', s, count=1, flags=re.S)
if count != 1:
    raise SystemExit(f'criminal callout: expected 1, found {count}')

# Remove the final three-button hub below the FAQ.
pattern = r'\s*<div style="margin-top:32px;text-align:center;display:flex;flex-wrap:wrap;gap:12px;justify-content:center">.*?</div>\s*</div>\s*</section>'
s, count = re.subn(pattern, '\n      </div>\n    </section>', s, count=1, flags=re.S)
if count != 1:
    raise SystemExit(f'FAQ hub: expected 1, found {count}')

extra_css = '''
<style id="membership-residual-editorial-20260710">
.membership-editorial .domino-chain{border-top:1px solid #dbe4ee!important}
.membership-editorial .domino-item{
  display:grid!important;
  grid-template-columns:38px minmax(0,1fr)!important;
  gap:14px!important;
  padding:20px 0!important;
  border-bottom:1px solid #dbe4ee!important;
}
.membership-editorial .domino-line{display:none!important}
.membership-editorial .domino-dot{
  width:32px!important;
  height:32px!important;
  border-radius:0!important;
  box-shadow:none!important;
}
.membership-editorial .domino-body{
  padding:0!important;
  border:0!important;
  border-radius:0!important;
  box-shadow:none!important;
  background:#fff!important;
}
.membership-editorial .domino-law{padding:0!important;background:transparent!important;border-radius:0!important}
.membership-editorial .issue-content+section>div>div:nth-of-type(2){border-radius:0!important;border-left:0!important;border-right:0!important}
</style>
'''
s = replace_once(s, '</head>', extra_css + '</head>', 'residual css')
p.write_text(s, encoding='utf-8')
