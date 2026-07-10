from pathlib import Path
import re


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: expected 1 occurrence, found {count}")
    return text.replace(old, new, 1)


def remove_once(text: str, pattern: str, label: str) -> str:
    text, count = re.subn(pattern, '', text, count=1, flags=re.S)
    if count != 1:
        raise SystemExit(f"{label}: expected 1 occurrence, found {count}")
    return text

# 保護者向け
p = Path('guide-parent.html')
s = p.read_text(encoding='utf-8')
s = remove_once(s, r'<div class="hero-actions">.*?</div>', 'parent hero actions')
s = remove_once(s, r'<section class="parent-chain-direct".*?</section>', 'parent chain section')
s = s.replace('入会手続き・オプトアウトの論点を読む →', '入会手続の論点を確認する')
s = s.replace('役員選出・強制化の論点を読む →', '役員選出・強制化の論点を確認する')
s = s.replace('個人情報提供の論点を読む →', '個人情報の取扱いを確認する')
parent_css = '''
<style id="parent-final-editorial-20260710">
.parent-page .mc-section{display:none!important}
.parent-page .lead-kicker,
.parent-page .section-kicker,
.parent-page .section-label{display:none!important}
.parent-page .case-section,
.parent-page .visual-section,
.parent-page .steps-section,
.parent-page .soudan-section,
.parent-page .faq-section,
.parent-page .howto-section{padding:68px 0!important}
.parent-page .case-note{text-align:left!important;max-width:900px!important}
.parent-page .case-list{gap:0!important;border-top:2px solid var(--navy)!important}
.parent-page .case-card{
  border:0!important;
  border-bottom:1px solid var(--line)!important;
  border-radius:0!important;
  box-shadow:none!important;
  background:#fff!important;
}
.parent-page .case-card.is-open{box-shadow:none!important;border-color:var(--line)!important}
.parent-page .case-top{padding:26px 0 8px!important}
.parent-page .case-tag{
  padding:0!important;
  background:transparent!important;
  color:var(--navy)!important;
  border-radius:0!important;
  font-size:.78rem!important;
}
.parent-page .case-toggle{
  justify-content:flex-start!important;
  padding:12px 0 20px!important;
  text-decoration:underline!important;
  text-underline-offset:.18em!important;
}
.parent-page .case-ans{padding:20px 0 32px!important}
.parent-page .case-quote{border-radius:0!important}
.parent-page .case-foot,
.parent-page .soudan-box,
.parent-page .faq2-item,
.parent-page .howto-step{
  border-radius:0!important;
  box-shadow:none!important;
}
.parent-page .faq-list{gap:0!important;border-top:1px solid var(--line)!important}
.parent-page .faq2-item{border:0!important;border-bottom:1px solid var(--line)!important}
.parent-page .faq2-q{padding:18px 0!important}
.parent-page .faq2-a{padding:0 0 22px!important}
.parent-page .howto-steps{gap:0!important;border-top:1px solid var(--line)!important}
.parent-page .howto-step{
  grid-template-columns:52px 1fr!important;
  padding:22px 0!important;
  border:0!important;
  border-bottom:1px solid var(--line)!important;
}
.parent-page .howto-num{border-radius:0!important}
.parent-page .parent-link-row a{
  padding:0!important;
  background:transparent!important;
  border:0!important;
  border-radius:0!important;
  color:var(--navy)!important;
  text-decoration:underline!important;
}
</style>
'''
s = replace_once(s, '</head>', parent_css + '</head>', 'parent css')
p.write_text(s, encoding='utf-8')

# PTA役員向け
p = Path('guide-pta.html')
s = p.read_text(encoding='utf-8')
s = remove_once(s, r'<div class="hero-actions">.*?</div>', 'officer hero actions')
s = remove_once(s, r'<section class="officer-chain-direct".*?</section>', 'officer chain section')
repls = {
    '<h4 style="font-size:.95rem;font-weight:700;color:#1e3a5f;margin:20px 0 8px">6-1　学校職員にPTA事務をさせてはなりません</h4>': '<h4 style="font-size:.95rem;font-weight:700;color:#1e3a5f;margin:20px 0 8px">6-1　学校職員がPTA事務を担う場合の確認</h4>',
    '<p>PTAの入会受付、退会受付、会員台帳管理、会費管理、文書作成、印刷、配布、回収、集計、問い合わせ対応を、教頭、学校事務職員、担任が勤務時間中に行っている場合、学校とPTAの境界は崩れています。学校がやってくれないと回らないPTA活動は、活動規模が大きすぎます。PTAだけで処理できる規模まで活動を削る必要があります。</p>': '<p>PTAの入会受付、退会受付、会員台帳管理、会費管理、文書作成、印刷、配布、回収、集計、問い合わせ対応を学校職員が勤務時間中に行っている場合は、具体的作業、校務としての位置づけ、職務命令、職専免、個人情報利用、費用負担、決裁を確認します。PTAから依頼されたというだけでは学校側の職務上の根拠にはなりません。PTA内部事務はPTA自身が処理することを基本とし、学校が協力する範囲は文書で区分します。</p>',
    '<h4 style="font-size:.95rem;font-weight:700;color:#1e3a5f;margin:20px 0 8px">6-2　学校アプリ・学校メールをPTA連絡に使ってはなりません</h4>': '<h4 style="font-size:.95rem;font-weight:700;color:#1e3a5f;margin:20px 0 8px">6-2　学校アプリ・学校メールを使う場合の確認</h4>',
    '<p>学校アプリ、学校メール、学校公式連絡網は、学校が保護者に対して学校業務に関する連絡を行うための仕組みです。PTAの連絡網ではありません。学校アプリでPTAの入会案内を送れば、保護者はそれを学校手続の一部として受け取りやすくなります。PTAの連絡は、PTAが本人から直接取得した会員連絡先を用いて、PTA自身の責任で行うべきです。</p>': '<p>学校アプリ、学校メール、学校公式連絡網は、学校が保護者へ学校業務に関する連絡を行うための仕組みです。PTA内部連絡は、PTAが本人から直接取得した会員連絡先を用いることが最も明確です。学校の連絡手段を利用する場合は、送信主体、対象者、利用目的、学校保有連絡先を使う根拠、承認者、配信記録、非会員への配信の必要性を確認し、学校の公式連絡とPTA通知を区別します。</p>',
    '<h4 style="font-size:.95rem;font-weight:700;color:#1e3a5f;margin:20px 0 8px">6-3　入学説明会・入学式でPTA勧誘をしてはなりません</h4>': '<h4 style="font-size:.95rem;font-weight:700;color:#1e3a5f;margin:20px 0 8px">6-3　入学説明会・入学式で案内する場合の区分</h4>',
    '<p>入学説明会や入学式は、学校が学校生活や就学手続を説明する公式な場です。そこにPTAの入会案内を組み込むと、保護者はPTA加入を学校手続の一部と受け取りやすくなります。PTAが入会案内を行う場合は、学校手続から切り離し、PTAが発行主体として行います。</p>': '<p>入学説明会や入学式は、学校が学校生活や就学手続を説明する公式な場です。その場でPTAが案内する場合は、学校手続とは別であること、加入は任意であること、発行主体と提出先がPTAであることを明示し、学校による提出強制や一括回収と誤認されない方法を取ります。</p>',
    '<h4 style="font-size:.95rem;font-weight:700;color:#1e3a5f;margin:20px 0 8px">6-4　学校配布物とPTA配布物を混ぜてはなりません</h4>': '<h4 style="font-size:.95rem;font-weight:700;color:#1e3a5f;margin:20px 0 8px">6-4　学校配布物とPTA配布物を区別する</h4>',
    '<p>学校提出書類の封筒に、PTA入会案内を混ぜてはいけません。PTA文書には、発行主体がPTAであること、学校の提出書類ではないこと、加入は任意であること、未加入でも児童生徒に不利益がないことを明確に示す必要があります。</p>': '<p>学校提出書類とPTA入会案内を同じ機会に配布する場合でも、文書の発行主体、提出先、提出義務の有無を明確に区別します。PTA文書には、学校の提出書類ではないこと、加入は任意であること、未加入でも児童生徒に不利益がないことを明示します。</p>',
    '<p>PTA会費は、任意団体であるPTAの会費です。教材費、給食費、修学旅行積立金などの学校徴収金とは性質が異なります。PTA会費を学校徴収金と一緒に引き落とすと、保護者はPTA会費を義務的費用と誤認します。PTA会費は、入会した会員から、PTAが直接徴収する必要があります。</p>': '<p>PTA会費は、任意団体であるPTAの会費です。教材費、給食費、修学旅行積立金などの学校徴収金とは性質が異なります。PTA会費を学校徴収金と同じ案内、口座、引落し、未納管理で扱うと、保護者はPTA会費を義務的費用と誤認しやすくなります。PTAが入会した会員から直接徴収する方式が最も明確です。学校が徴収事務に関与する場合は、加入記録、委任、口座情報の利用、校務・服務、決裁、会計区分を個別に説明します。</p>',
    '<p>「学校教育上支障がない」とは、空き教室があるという意味だけではありません。学校施設を使うPTAほど、学校とは別の任意団体であることを厳格に示す必要があります。学校施設利用については、利用目的、利用日時、責任者、使用許可・届出の有無、個人情報を扱う作業の有無を確認する必要があります。学校施設を使いながら、任意加入を曖昧にし、入会申込記録もなく、学校の信用を借りて加入・会費・役員を処理する運営は、137条の趣旨に反します。</p>': '<p>「学校教育上支障がない」とは、空き教室があるという意味だけではありません。学校施設を使うPTAほど、学校とは別の任意団体であることを明確に示す必要があります。施設利用については、利用目的、利用日時、責任者、使用許可・届出、個人情報を扱う作業の有無を確認します。任意加入、入会記録、会費、役員選出、学校関与に問題がある場合は、公共性、教育上の支障、許可条件、公私分離の観点から使用範囲を見直します。</p>',
    '<p>最初の30日で、会則、総会資料、入会申込記録、会員台帳、会費徴収方法、学校徴収金との混在、学校から受け取っている個人情報、学校アプリや学校メールでのPTA通知、学校職員によるPTA事務、学校施設利用の許可・届出・実態を確認します。入会申込記録のない人からの会費徴収、学校アプリでのPTA加入・会費・役員通知、学校職員によるPTA会員管理は、ただちに停止または停止協議に入る必要があります。</p>': '<p>最初の30日で、会則、総会資料、入会申込記録、会員台帳、会費徴収方法、学校徴収金との混在、学校から受け取っている個人情報、学校アプリや学校メールでのPTA通知、学校職員によるPTA事務、学校施設利用の許可・届出・実態を確認します。加入、情報利用、会費徴収、学校職員の事務について根拠を確認できない場合は、当該運用の停止を含む見直しと、学校・教育委員会との協議を行います。</p>',
}
for old, new in repls.items():
    s = replace_once(s, old, new, 'officer legal text')
officer_css = '''
<style id="officer-final-editorial-20260710">
body.guide-pta-editorial .page-hero-kicker{display:none!important}
body.guide-pta-editorial .risk-bar-track{display:none!important}
body.guide-pta-editorial .risk-bar-label{justify-content:flex-start!important;gap:12px!important}
body.guide-pta-editorial .risk-bar-label span:last-child{display:none!important}
body.guide-pta-editorial .compare-label{
  text-transform:none!important;
  letter-spacing:0!important;
}
body.guide-pta-editorial .otl-dot,
body.guide-pta-editorial .rm-num{
  border-radius:0!important;
  box-shadow:none!important;
}
body.guide-pta-editorial .otl-body,
body.guide-pta-editorial .otl-check{
  background:#fff!important;
  border-left:0!important;
  border-right:0!important;
}
</style>
'''
s = replace_once(s, '</head>', officer_css + '</head>', 'officer css')
p.write_text(s, encoding='utf-8')

# 教育委員会・学校管理職向け
p = Path('guide-board.html')
s = p.read_text(encoding='utf-8')
s = remove_once(s, r'<div class="hero-actions">.*?</div>', 'board hero actions')
s = remove_once(s, r'<section class="board-chain-direct".*?</section>', 'board chain section')
board_repls = {
    '是正方向：PTAが自前で取得・徴収・連絡し、学校は教育活動上必要な連絡調整に限る': '是正方向：PTA内部事務はPTAが担い、学校の協力は校務・服務・情報・施設の根拠を明確にする',
    '<h2 id="s5">5　個人情報保護法第69条ではPTA通常事務を正当化できない</h2>': '<h2 id="s5">5　学校保有情報をPTA目的で扱う場合の第61条・第69条</h2>',
    '<p>公立学校が保有する児童・保護者情報は、学校教育上の目的のために取得・保有されるものです。これをPTAの入会管理、会費徴収、役員選出、連絡、免除審査、非会員把握、応援金・支援金・協力金・協賛金の依頼に利用する場合、個人情報保護法第69条の目的外利用又は目的外提供の問題が生じます。</p>': '<p>公立学校が保有する児童・保護者情報をPTAの入会管理、会費徴収、役員選出、連絡、免除審査、非会員把握等に用いる場合は、学校自身による利用とPTAへの提供を分けます。そのうえで、第61条の所掌事務・業務と保有の必要性、第69条の利用目的内か目的外か、目的外であれば第2項のどの例外を根拠とするのかを確認します。</p>',
    '<h3>5-1　第69条第1項では処理できない</h3>': '<h3>5-1　第61条と第69条第1項を先に確認する</h3>',
    '<p>PTAは学校とは別組織の任意団体です。PTAの会員管理、会費徴収、役員選出、免除審査、非会員把握、応援金・支援金依頼は、学校教育上の児童生徒管理ではなく、PTA自身が担うべき本来事務です。これらを学校の保有個人情報の利用目的内であると扱うことはできません。</p>': '<p>PTAは学校とは別組織の任意団体です。PTAの会員管理、会費徴収、役員選出、免除審査、非会員把握等は、通常はPTA内部の事務です。これらを学校の所掌事務・業務又は学校保有情報の利用目的内として扱うのであれば、法令上の根拠、具体的な校務上の位置づけ、必要性、対象情報を文書で示す必要があります。</p>',
    '<h3>5-3　第69条第2項第1号の本人同意では一括処理できない</h3>': '<h3>5-3　第69条第2項第1号の本人同意を根拠とする場合</h3>',
    '<p>第69条第2項第1号は、本人の同意があるとき、又は本人に提供するときを例外として扱います。しかし、ここでいう同意は、包括的・黙示的な同意で足りるものではありません。PTA入会、学校名簿のPTA提供、PTA会費の徴収、役員選出対象化、学校連絡ツール利用、非会員把握への利用は、それぞれ別個の意思表示として確認される必要があります。</p>': '<p>第69条第2項第1号は、本人の同意があるとき、又は本人に提供するときを例外として扱います。同意を根拠とする場合は、対象情報、利用又は提供の目的、提供先、利用方法を具体的に示し、PTA入会、学校名簿のPTA提供、PTA会費の徴収、役員選出、学校連絡ツール利用等を区別して説明する必要があります。</p>',
    '<p>PTA加入案内、役員希望調査、免除申請、会費徴収、会費督促、応援金・支援金依頼、非会員向け連絡は、学校の所掌事務ではなく、PTAの本来事務です。「学校が送っているだけでPTAに提供していない」という形式を取っても、目的外提供の問題が目的外利用の問題に変わるだけです。同号によって、PTA通常事務を学校の情報基盤で処理することを正当化することはできません。</p>': '<p>PTA加入案内、役員希望調査、免除申請、会費徴収、会費督促、応援金・支援金依頼、非会員向け連絡は、通常はPTA内部の事務です。学校が送信主体となる場合は、PTAに情報を渡していないとしても、学校が保有する連絡先をPTA目的で利用していることになります。第2号を根拠とするなら、学校の所掌事務・業務、必要性、対象者、配信内容、承認記録を具体的に示す必要があります。</p>',
    '<h3>5-6　第69条第2項第4号の特別の理由では通常事務を包括処理できない</h3>': '<h3>5-6　第69条第2項第4号の特別の理由を用いる場合</h3>',
    '<p>PTAの入会管理、会費徴収、役員選出、免除審査、応援金・支援金依頼、非会員把握は、毎年度反復されるPTAの通常事務です。これらは統計作成又は学術研究ではなく、本人以外の者に提供することが明らかに本人の利益になる場合でもありません。</p>': '<p>PTAの入会管理、会費徴収、役員選出、免除審査、応援金・支援金依頼、非会員把握は、毎年度反復されるPTAの通常事務です。第4号は例外規定であり、このような恒常的事務を包括的に処理する一般的根拠としてではなく、個別具体的な事情と特別の理由を示して限定的に検討する必要があります。</p>',
    '<p>PTAは本来、入会申込により会員情報を独自に取得すべき団体です。PTAが自ら入会申込を取り、会員から必要な情報を取得すれば足りる以上、学校保有情報を用いなければならない特別の理由があるとはいえません。PTAにとって便利であること、従来そのように運用していたこと、学校を通じた方が回収率が高いことは、特別の理由ではありません。</p>': '<p>PTAが入会申込を通じて加入者本人から必要な情報を取得できることは、特別の理由の有無を判断する重要な事情です。PTAにとって便利であること、従来そのように運用していたこと、学校を通じた方が回収率が高いことだけでは、恒常的な利用又は提供を支える説明として不十分です。</p>',
}
for old, new in board_repls.items():
    s = replace_once(s, old, new, 'board legal text')
board_css = '''
<style id="board-final-editorial-20260710">
body.guide-board-editorial .board-jp-article .toc{display:none!important}
body.guide-board-editorial .gbv-figure,
body.guide-board-editorial .board-jp-article .primary-summary,
body.guide-board-editorial .board-jp-article .flow{
  border-radius:0!important;
  box-shadow:none!important;
}
body.guide-board-editorial .gbv-scroll{padding:14px 0!important}
body.guide-board-editorial .board-jp-article .primary-summary,
body.guide-board-editorial .board-jp-article .flow{
  background:transparent!important;
  border-top:1px solid #d8dee8!important;
  border-bottom:1px solid #d8dee8!important;
  border-left:0!important;
  padding:20px 0!important;
}
</style>
'''
s = replace_once(s, '</head>', board_css + '</head>', 'board css')
p.write_text(s, encoding='utf-8')
