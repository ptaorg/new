from pathlib import Path
import re


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'{label}: expected 1 occurrence, found {count}')
    return text.replace(old, new, 1)


p = Path('privacy.html')
s = p.read_text(encoding='utf-8')

# Page identity and search metadata
replacements = {
    '<meta name="description" content="学校からPTAへの個人情報提供——個人情報保護法第69条・第三者提供禁止・みなし加入の罠。全国教委の回答付き。">': '<meta name="description" content="公立学校が保有する児童・保護者情報をPTA目的で自ら利用し、又はPTAへ提供する場合の個人情報保護法61条・69条、本人同意、PTAによる直接取得を整理します。">',
    '<meta property="og:title" content="個人情報提供の問題 | PTA適正化推進委員会">': '<meta property="og:title" content="学校保有情報のPTA目的利用・提供 | PTA適正化推進委員会">',
    '<meta name="twitter:title" content="個人情報提供の問題 | PTA適正化推進委員会">': '<meta name="twitter:title" content="学校保有情報のPTA目的利用・提供 | PTA適正化推進委員会">',
    '<meta name="twitter:description" content="学校名簿をPTAへ提供する場合の個人情報保護法第69条、本人同意、第三者提供、PTAによる直接取得の整理。">': '<meta name="twitter:description" content="学校自身によるPTA目的利用とPTAへの提供を分け、個人情報保護法61条・69条、本人同意、PTAによる直接取得を整理します。">',
    '<title>個人情報提供の問題 | PTA適正化推進委員会</title>': '<title>学校保有情報のPTA目的利用・提供 | PTA適正化推進委員会</title>',
    '<body>': '<body class="privacy-editorial">',
}
for old, new in replacements.items():
    s = replace_once(s, old, new, old[:45])

# First explanation: replace the categorical visual with the actual three-way test.
old = '<h2>学校保有情報を使うルートと、PTAが直接取得するルート</h2>\n<figure style="margin:30px auto;max-width:860px"><img src="assets/diagrams/02_個人情報/01_情報取得の2ルート.svg" alt="図解：情報取得の2ルート" loading="lazy" style="display:block;width:100%;height:auto"></figure>'
new = '<h2>学校保有情報の利用・提供と、PTAによる直接取得</h2>\n<p>学校保有情報をPTA目的で扱う場面は、①学校が自ら利用する場合、②学校からPTAへ提供する場合、③PTAが加入者本人から直接取得する場合に分けます。①と②は、個人情報保護法第61条に基づく所掌事務・業務と保有の必要性、利用目的の範囲、第69条第1項又は第2項の根拠、対象情報、不同意者の処理、利用・提供記録を確認します。③は、PTAが利用目的を示し、加入者本人から必要な情報だけを取得する方式です。</p>'
s = replace_once(s, old, new, 'privacy three routes')

# Core legal explanation and source panels.
replacements = {
    '<h2>名簿提供は「PTAが公益的か」ではなく、学校保有情報を目的外に使う根拠の問題です</h2>': '<h2>学校保有情報のPTA目的利用・提供は、学校側の根拠を確認する問題です</h2>',
    '<p>学校が保有する児童・保護者情報をPTAの会員管理、役員選出、会費徴収、地区班編成、連絡網に使う場合は、個人情報保護法第5章の保有個人情報として、利用目的、提供項目、本人同意、提供記録、不参加者の除外、保存・廃棄を確認する必要があります。</p>': '<p>学校が保有する児童・保護者情報をPTAの会員管理、役員選出、会費徴収、地区班編成、連絡網に使う場合は、学校自身による利用とPTAへの提供を分けます。個人情報保護法第61条・第69条に照らし、所掌事務・業務、利用目的、利用・提供項目、例外根拠、本人同意、不同意者の除外、利用・提供記録、保存・廃棄を確認します。</p>',
    '<p>学校からPTAへの個人情報提供を検討する場合は、学校が保有する児童・保護者情報をPTAに提供することが、利用目的、本人同意、第三者提供、目的外利用のどの問題として整理されるかを確認します。</p>': '<p>学校保有情報をPTA目的で扱っている場合は、学校自身が利用しているのか、PTAへ提供しているのかを先に分けます。そのうえで、所掌事務・業務、利用目的、第69条第1項又は第2項の根拠、本人説明、不同意者の除外、利用・提供記録を確認します。</p>',
    '<h2>資料から作る確認質問：名簿提供を「同意書の有無」だけで終わらせない</h2>': '<h2>資料から作る確認質問：学校自身の利用とPTAへの提供を分ける</h2>',
    '<p>個人情報保護委員会資料や自治体通知は、単に「同意書を取ったか」を見るためだけの資料ではありません。学校が持っている情報をPTAが使う場合、どの情報を、誰が、どの目的で、どの記録に基づいて渡したのかを分けて確認するために使います。</p>': '<p>個人情報保護委員会資料や自治体通知は、単に「同意書を取ったか」を見るためだけの資料ではありません。学校が保有する情報を、学校がPTA目的で自ら利用したのか、PTAへ提供したのか、どの情報を、誰が、どの目的と根拠で扱ったのかを分けて確認するために使います。</p>',
    '<div class="source-lens-item"><strong>提供項目</strong><p>児童名、保護者名、住所、電話番号、クラス、きょうだい情報など、どの項目をPTAに渡したのか。</p></div>': '<div class="source-lens-item"><strong>利用・提供項目</strong><p>児童名、保護者名、住所、電話番号、クラス、きょうだい情報など、どの項目を学校が利用し、又はPTAへ提供したのか。</p></div>',
    '<div class="source-lens-item"><strong>記録管理</strong><p>提供日時、提供先、提供項目、根拠、担当者が記録され、後から説明できるか。</p></div>': '<div class="source-lens-item"><strong>記録管理</strong><p>利用又は提供の日時、対象者、項目、根拠、担当者、承認者が記録され、後から説明できるか。</p></div>',
    '<p>PTAが管理できるのは、原則として入会申込書や個人情報同意書により本人から直接取得した会員情報です。非会員の氏名、児童名、住所、連絡先、クラスを学校情報から割り出して「非会員リスト」を作る運用は、学校保有情報の目的外利用・第三者提供の問題に直結します。</p>': '<p>PTAの恒常的な会員管理は、入会申込書や電子フォーム等により加入者本人から直接取得した情報を基本にします。非会員の氏名、児童名、住所、連絡先、クラスを学校情報から割り出して「非会員リスト」を作る場合は、学校自身の利用かPTAへの提供かを分け、第61条・第69条の根拠と必要性を確認します。</p>',
    'https://www.ppc.go.jp/files/pdf/202603_school_pta_pd_point.pdf': 'https://www.ppc.go.jp/files/pdf/260325_shiryou-3.pdf',
}
for old, new in replacements.items():
    s = replace_once(s, old, new, old[:55])

# Four recurring problem patterns: remove unsupported categorical conclusions.
replacements = {
    '<p>入学時に学校へ提出した緊急連絡先届の情報が、保護者の知らないうちにPTA名簿として使用されている。目的外利用（同法69条）かつ第三者提供にあたる。</p>': '<p>入学時に学校へ提出した緊急連絡先届の情報がPTA名簿へ使われている場合は、学校自身による利用かPTAへの提供かを分け、第61条・第69条の根拠、対象項目、利用・提供記録を確認します。</p>',
    '<p>学校への届出書にPTA名簿登録が抱き合わせになっている。「緊急連絡」と「PTA活動」は別目的であり、包括同意は無効。</p>': '<p>学校への緊急連絡先届とPTA名簿登録が一体になっている場合は、学校提出部分とPTA提出部分、利用目的、任意性、提出先、拒否した場合の扱いが明確に区分されているかを確認します。一体化だけで直ちに同意が無効になるわけではありませんが、自由で具体的な意思表示として評価できるかが問題になります。</p>',
    '<p>「PTAへの情報提供に同意しない場合はご連絡ください」という記載。行政機関等の第三者提供においてオプトアウトは不可。</p>': '<p>「同意しない場合は申し出てください」という方式は、本人が積極的に同意した記録を残しません。第69条第2項第1号の本人同意を根拠とするなら、対象情報、目的、提供先を示し、本人が自由に選択した明示的な同意として記録できる方式かを確認します。</p>',
    '<p>退会・非加入の意思を示した後もPTA名簿に氏名・連絡先が残り続ける。保有個人情報の削除・利用停止請求（同法90条以下）の対象。</p>': '<p>退会後もPTAが氏名・連絡先を保持する場合は、利用目的、保存期間、会計・紛争対応等の保持理由、アクセス権限、削除又は匿名化の時期を確認します。学校が保有する情報とPTAが保有する情報では、適用される請求手続が異なるため、同じ条文で一括して扱いません。</p>',
}
for old, new in replacements.items():
    s = replace_once(s, old, new, old[:60])

# Direct collection is the clearest basic design, but school cooperation is not categorically forbidden.
replacements = {
    '<h2>適正な情報取得の手順</h2>': '<h2>会員情報を取得・管理する基本手順</h2>',
    '<p>解決策はシンプルです。PTAが学校名簿に頼らず、独自に情報を取得する体制を作るだけです。</p>': '<p>恒常的な会員管理は、PTAが加入者本人から必要な情報を直接取得する方式が最も明確です。学校が配布・回収等に協力する場合でも、発行主体、提出先、学校職員の役割、学校保有情報を利用しないことを明確にします。</p>',
    '<p>任意性の明示・個人情報の利用目的・利用範囲・第三者提供の有無を明記。</p>': '<p>任意加入、利用目的、取得項目、利用範囲、第三者提供の有無、保存期間、問い合わせ先を明記します。紙だけでなく、本人の申込みと送信記録が残る電子フォームも利用できます。</p>',
    '<strong>保護者が自署して提出する（オプトイン）</strong>': '<strong>加入者本人が明示的に申し込む</strong>',
    '<p>PTAが直接配布し、PTAが直接回収。学校の配布・回収ルートを使わない。</p>': '<p>提出先はPTAとし、学校提出書類とは区別します。学校が配布・回収に協力する場合は、学校が加入意思を強制又は選別する運用にならないよう、役割と取扱記録を定めます。</p>',
    '<p>学校保有情報とは完全に切り離した独立した名簿。退会時は速やかに削除。</p>': '<p>情報源、利用目的、アクセス権限、保存期間、役員交代時の引継ぎを定めます。退会後は保持が必要な情報と不要な情報を分け、不要となった情報を削除又は匿名化します。</p>',
}
for old, new in replacements.items():
    s = replace_once(s, old, new, old[:55])

# Remove the last redundant hub section.
pattern = r'\s*<!-- 関連リンク -->\s*<section>\s*<h2>関連導線</h2>.*?</section>'
s, count = re.subn(pattern, '', s, count=1, flags=re.S)
if count != 1:
    raise SystemExit(f'related links section: expected 1, found {count}')

# FAQ corrections: distinguish school-held data from PTA-held data and avoid unsupported absolute conclusions.
faq_replacements = {
    '規約への「同意」が個人情報保護法上の有効な同意になるためには、①同意が自由な意思に基づくこと、②利用目的が特定されていること、③同意の証拠が残っていることが必要です。入学時に「学校の提出書類と一体化した書類」への記名は、優越的立場による強制的同意とみなされる可能性があります。全国の教育委員会への照会でも「規約同意のみでは不十分」との回答が得られています。': '規約への同意だけで足りるかは、対象情報、利用・提供目的、提供先、任意性、拒否方法、記録の内容によります。学校提出書類と一体化している場合は、保護者がPTAへの情報利用・提供を自由に拒否できたか、学校手続と誤認しなかったかを確認します。規約への包括的な記名だけで、すべての利用・提供に同意したと直ちに扱うことはできません。',
    '個人情報保護法に基づき、PTAに対して「保有個人情報の利用停止・削除請求」ができます。書面でPTAに請求し、合理的期間内に対応されない場合は所轄の個人情報保護委員会に相談することができます。学校保有情報や学校連絡ツールの利用を確認する場合は、<a href="guideline.html#tpl-school-info-stop">学校名簿・学校アプリ利用確認書</a>を使えます。': 'まずPTAに対し、情報の取得元、利用目的、保存期間、共有先を確認し、利用停止、訂正、削除又は匿名化を求めます。法定の請求権が成立するかは、PTAに適用される民間部門の規律と具体的な保有・利用状況によります。一方、学校が保有する情報や学校連絡ツールの利用については、行政機関等の制度に基づく開示・訂正・利用停止手続の対象となるかを学校・教育委員会に確認します。<a href="guideline.html#tpl-school-info-stop">学校名簿・学校アプリ利用確認書</a>も利用できます。',
    '非加入を理由とした不利な扱いは、任意加入の原則を根底から覆す行為として問題があります。教育の機会均等（教育基本法4条）の観点からも許されません。具体的な不利益（配布物が届かない、行事への参加が制限されるなど）は記録に残し、校長・教育委員会に文書で申し入れることを推奨します。当委員会への相談も受け付けています。': '学校教育上の取扱いをPTA加入状況によって変えることは、学校とPTAの区分や児童生徒への公平な対応の観点から問題です。PTA独自の事業や給付については、実施主体、目的、費用負担、学校行事との関係、子どもへの心理的影響を具体的に確認します。配布物、行事参加、記念品等で差が生じた場合は、誰が決めたのかを含めて記録し、学校・PTA・教育委員会へ文書で確認します。',
    'PTAも一定規模以上であれば個人情報取扱事業者として個人情報保護法の規律に服します。名前・住所・電話番号をLINEグループ等に掲示することは、入会届の利用目的として明示されていない場合、目的外利用（法18条）にあたる可能性があります。また第三者の目に触れる可能性があるSNSへの掲載は、情報の「提供」に相当する場合があります。入会届で利用範囲を明確化し、当事者の同意なくSNSに掲載しないルールを設けるべきです。': 'PTAが個人情報データベース等を事業の用に供している場合は、法人格や営利性の有無にかかわらず、民間部門の個人情報保護法上の規律を確認します。氏名、住所、電話番号、写真等をLINEグループやSNSで共有する場合は、取得時に示した利用目的の範囲、閲覧できる者、再共有の可否、安全管理、本人説明を確認します。公開範囲の広いSNS等へ掲載する場合は、対象者ごとの同意を得る運用が最も明確です。',
}
for old, new in faq_replacements.items():
    s = replace_once(s, old, new, old[:65])

# Editorial layout: remove the old categorical diagrams and card-heavy navigation.
privacy_css = '''
<style id="privacy-editorial-20260710">
.privacy-editorial{background:#fff!important}
.privacy-editorial .hero-actions,
.privacy-editorial .page-hero-kicker,
.privacy-editorial .section-kicker,
.privacy-editorial .pg figure,
.privacy-editorial .flow-row,
.privacy-editorial .result-row,
.privacy-editorial .alert-danger{display:none!important}
.privacy-editorial .pg{width:min(calc(100% - 40px),920px)!important}
.privacy-editorial .pg section{margin-bottom:0!important;padding:42px 0!important;border-bottom:1px solid #cfd8e2!important}
.privacy-editorial .pg h2{border-bottom:0!important;padding-bottom:0!important;line-height:1.5!important}
.privacy-editorial .editorial-panel,
.privacy-editorial .source-lens-panel{
  margin:0!important;
  padding:42px 0!important;
  border:0!important;
  border-bottom:1px solid #cfd8e2!important;
  border-radius:0!important;
  box-shadow:none!important;
  background:#fff!important;
}
.privacy-editorial .source-lens-grid{display:block!important;border-top:1px solid #dbe4ee!important}
.privacy-editorial .source-lens-item{
  padding:18px 0!important;
  border:0!important;
  border-bottom:1px solid #dbe4ee!important;
  border-radius:0!important;
  box-shadow:none!important;
  background:#fff!important;
}
.privacy-editorial .steps{border-top:1px solid #dbe4ee!important}
.privacy-editorial .step-r{
  display:grid!important;
  grid-template-columns:44px minmax(0,1fr)!important;
  gap:14px!important;
  padding:20px 0!important;
  border-bottom:1px solid #dbe4ee!important;
}
.privacy-editorial .step-r::before{display:none!important}
.privacy-editorial .step-num{width:34px!important;height:34px!important;border-radius:0!important;background:var(--navy)!important}
.privacy-editorial .step-body{
  padding:0!important;
  border:0!important;
  border-radius:0!important;
  box-shadow:none!important;
  background:#fff!important;
}
.privacy-editorial .faq-list{gap:0!important;border-top:1px solid var(--line)!important}
.privacy-editorial .faq-item{border:0!important;border-bottom:1px solid var(--line)!important;border-radius:0!important}
.privacy-editorial .faq-q{padding:18px 0!important}
.privacy-editorial .faq-a{padding-left:0!important;padding-right:0!important}
.privacy-editorial .btn-soft,
.privacy-editorial .btn-navy,
.privacy-editorial .ed-link-buttons a{
  display:inline!important;
  padding:0!important;
  background:transparent!important;
  color:var(--navy)!important;
  border:0!important;
  border-radius:0!important;
  text-decoration:underline!important;
  text-underline-offset:.18em!important;
}
</style>
'''
s = replace_once(s, '</head>', privacy_css + '</head>', 'privacy css')
p.write_text(s, encoding='utf-8')
