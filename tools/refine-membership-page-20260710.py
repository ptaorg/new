from pathlib import Path
import re


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'{label}: expected 1 occurrence, found {count}')
    return text.replace(old, new, 1)


p = Path('membership.html')
s = p.read_text(encoding='utf-8')

# Metadata and page identity
replacements = {
    '<meta name="description" content="PTAの入会手続・みなし加入・オプトアウト方式について、意思確認、黙示の合意、会費、個人情報利用の論点を整理したページ。">': '<meta name="description" content="PTA入会の成立要件と申込記録について、民法521条・522条、消費者契約法、会費、個人情報、学校関与、判例の確認事項を整理します。">',
    '<meta property="og:title" content="入会手続とオプトアウト | PTA適正化推進委員会">': '<meta property="og:title" content="PTA入会の成立と申込記録 | PTA適正化推進委員会">',
    '<meta property="og:description" content="みなし加入・オプトアウト方式の成立要件と、意思確認・黙示の合意・会費・個人情報利用の論点を整理します。">': '<meta property="og:description" content="学校在籍だけでは生じないPTA会員関係について、申込み・承諾・申込記録・会費・個人情報・学校関与を整理します。">',
    '<meta name="twitter:title" content="入会手続とオプトアウト問題 | PTA適正化推進委員会">': '<meta name="twitter:title" content="PTA入会の成立と申込記録 | PTA適正化推進委員会">',
    '<meta name="twitter:description" content="みなし加入・オプトアウト方式の法的論点を、民法・消費者契約法・憲法・個人情報保護法から確認します。">': '<meta name="twitter:description" content="PTA入会の申込みと承諾、客観的な申込記録、会費・個人情報・学校関与を法令と実物文書から確認します。">',
    '<title>入会手続とオプトアウト | PTA適正化推進委員会</title>': '<title>PTA入会の成立と申込記録 | PTA適正化推進委員会</title>',
    '<body>': '<body class="membership-editorial">',
    '<h1>入会手続と<br>オプトアウト問題</h1>': '<h1>PTA入会の成立と<br>申込記録</h1>',
}
for old, new in replacements.items():
    s = replace_once(s, old, new, old[:50])

# Remove duplicate navigation.
s, count = re.subn(r'\s*<div class="issue-hero-toc">.*?</div>\s*</div>\s*</section>', '\n    </div>\n  </section>', s, count=1, flags=re.S)
if count != 1:
    raise SystemExit(f'hero toc: expected 1, found {count}')
s, count = re.subn(r'\s*<aside class="issue-sidebar">.*?</aside>', '', s, count=1, flags=re.S)
if count != 1:
    raise SystemExit(f'sidebar: expected 1, found {count}')
s, count = re.subn(r'\s*<!-- Related links -->\s*<div class="related-links-section">.*?</div>\s*</div>\s*</main>', '\n    </main>', s, count=1, flags=re.S)
if count != 1:
    raise SystemExit(f'related links: expected 1, found {count}')

# Replace the opening visual comparison with the institutional rule and the litigation distinction.
pattern = r'\s*<!-- ===== 図解：オプトイン/オプトアウト ===== -->\s*<section class="issue-section" style="margin-bottom:48px">.*?</section>'
replacement = '''
      <section class="issue-section" style="margin-bottom:48px">
        <h2>制度として確認すべきこと</h2>
        <p>PTAは学校とは別の団体であり、学校への入学、在籍、進級、PTAからの一方的な通知、保護者の沈黙だけで会員関係を発生させることはできません。会員管理制度としては、会則、会費、活動内容、退会方法を示し、加入者本人の申込みとPTAの承諾を客観的な記録として残す必要があります。</p>
        <p>後日の訴訟では、会費納入、活動参加、説明内容等から個別に黙示の合意や追認が争われる場合があります。しかし、事後的な証拠評価は、全保護者をあらかじめ会員扱いする制度の根拠にはなりません。制度設計と個別紛争の立証を分けて考えます。</p>
      </section>'''
s, count = re.subn(pattern, replacement, s, count=1, flags=re.S)
if count != 1:
    raise SystemExit(f'opening visual: expected 1, found {count}')

# Remove the remaining decorative legal diagrams. Their conclusions are stated in the prose below.
s, figure_count = re.subn(r'\s*<figure class="mb-fig".*?</figure>', '', s, flags=re.S)
if figure_count < 2:
    raise SystemExit(f'membership figures: expected at least 2, found {figure_count}')
s, svg_count = re.subn(r'\s*<svg width="100%".*?</svg>\s*(?:<p style="font-size:\.84rem;.*?</p>)?', '', s, flags=re.S)
if svg_count < 1:
    raise SystemExit(f'membership standalone diagrams: expected at least 1, found {svg_count}')

# Main doctrinal text
replacements = {
    '<h2>問題の全体像——なぜ入会手続が最重要論点か</h2>': '<h2>問題の全体像——なぜ申込記録が必要か</h2>',
    '<p>PTAは社会教育法第10条に基づく「社会教育関係団体」であり、学校から独立した任意加入の私的団体です。しかし日本の多くの学校では、入学と同時に全保護者が自動的にPTAに加入させられる「みなし加入」や、「拒否しなければ会員とみなす」というオプトアウト方式が長年にわたり続けられてきました。</p>': '<p>PTAは学校とは別の民間団体です。その目的と活動が社会教育法第10条の要件に当たる場合は社会教育関係団体として扱われますが、いずれにしても学校在籍からPTA会員関係が当然に生じるものではありません。現場では、入学と同時に全保護者を会員扱いする運用や、「拒否しなければ会員とみなす」という通知が見られます。</p>',
    '<p>この入会手続の問題が他のすべての論点の<strong>起点</strong>になっています。入会の意思確認がないまま会員とされれば、会費徴収・個人情報利用・役員就任義務のすべてが「法的根拠のない状態」で行われることになるからです。</p>': '<p>入会手続は、会費請求、会員名簿、議決権、役員選出、個人情報利用の前提です。申込みと承諾の記録がなければ、誰が会員で、どの会則と会費に合意したのかを客観的に説明することが困難になります。</p>',
    '<h3 id="domino">意思確認を欠く運用が生む連鎖的リスク</h3>': '<h3 id="domino">意思確認を欠く運用が他の事務へ及ぼす影響</h3><p>会員範囲が不明確なままでは、会費請求、総会の構成、役員選出、名簿作成、学校徴収金との分離、非会員への連絡等の根拠も不明確になります。各事務を「従来どおり」で処理せず、入会記録と対応させて確認します。</p>',
    '<p>新入生の保護者とPTAの間にはそのような関係はなく、「これまでそうしてきた」という事実上の慣習は、法的拘束力を持つ慣習法（民法第92条）の要件（公序良俗に反しないこと）を満たしません。強制加入は憲法上の権利を侵害するものとして、公序良俗違反の疑いが強いからです。</p>': '<p>「これまでそうしてきた」という慣行だけで、個々の保護者の申込みと承諾を代替することはできません。新入生を含む各保護者について、どの説明を受け、どの行為をもって申込み又は承諾と評価するのかを個別に確認する必要があります。恒常的な制度は、慣行や事後的な推認ではなく、明示的な申込記録によって運営します。</p>',
    '<p>PTA適正化推進委員会による調査および消費者庁との協議記録において、<strong>PTAが消費者契約法上の「事業者」に該当することは行政解釈上も確定</strong>しています。消費者庁『逐条解説 消費者契約法』の「その他の団体」の具体例として、民法上の組合や学会と並び「PTA」が明記されています。</p>': '<p>消費者庁『消費者契約法逐条解説』は、同法上の「その他の団体」の例としてPTAを明記しています。したがって、PTAが契約の当事者となり、保護者が事業として又は事業のためではなく契約する場面では、消費者契約法の適用関係を確認します。</p>',
    '<p>PTAは会費徴収・行事運営・保険加入・広報誌発行などを反復継続して行っており、「事業者」の定義（営利目的の有無を問わない同種行為の反復継続的遂行）を充足します。PTAと保護者の関係は「消費者契約」となり、同法の厳格な規制下に置かれます。</p>': '<p>PTAの営利性や法人格の有無だけで、消費者契約法の適用を否定することはできません。実際の勧誘内容、契約条項、保護者の誤認又は困惑、意思表示との因果関係等に応じて、同法第4条、第10条等の要件を検討します。</p>',
    '<div class="lbc-issue">「期日までに不同意の申出がなければ入会とみなす」という条項は、民法の意思主義（承諾が必要）から逸脱し、消費者の「承諾しない自由」を著しく制限します。ネガティブ・オプション（注文していない商品を送って返送しなければ購入とみなす商法）と同じ構造です。</div>': '<div class="lbc-issue">「期日までに不同意の申出がなければ入会とみなす」という条項は、申込みと承諾をどのように確認するのか、消費者の権利を制限し信義則に反して一方的に害する条項に当たるかを、説明内容と運用実態から検討します。</div>',
    '<span class="lbc-verdict invalid">条項無効</span>': '<span class="lbc-verdict invalid">有効性を確認</span>',
    '<div class="lbc-issue">「子供のためになる」「記念品がもらえる」といった利益を強調しながら、「実は入会義務はない」「役員負担がある」「退会できる」という不利益事実を故意に告げなかった場合、保護者は契約を取り消すことができます。</div>': '<div class="lbc-issue">利益となる事項を告げながら、それと表裏一体の不利益事実を故意又は重大な過失により告げず、保護者が誤認して意思表示をした場合は、第4条第2項の要件を検討します。単なる説明不足だけで直ちに取消しになるわけではありません。</div>',
    '<div class="lbc-issue">「加入は義務です」「全員参加です」と事実に反する説明を行って入会させた場合、これは不実告知（重要事項についての不実の告知）として、取消しの対象となります。</div>': '<div class="lbc-issue">「加入は法的義務である」など重要事項について事実と異なる説明があり、保護者がその内容を事実と誤認して意思表示をした場合は、第4条第1項の取消要件を検討します。</div>',
    '<span class="lbc-verdict invalid">取消可能</span>': '<span class="lbc-verdict invalid">要件を確認</span>',
    '<span class="lbc-verdict invalid">努力義務違反</span>': '<span class="lbc-verdict invalid">情報提供努力義務</span>',
    '<h2>憲法第21条——「加入しない自由」の侵害</h2>': '<h2>憲法第21条——「加入しない自由」と学校関与</h2>',
    '<p>PTAが公立学校という公的空間において、事実上の強制力をもって全保護者を加入させることは、保護者の「結社しない自由」を侵害するものです。オプトアウト方式は「加入しない」という権利の行使に対して心理的・物理的な障壁を設けるものであり、実質的な強制として機能しています。</p>': '<p>PTAは私的団体であるため、個別の会員関係では民法、消費者契約法、会則等を通じて加入意思を検討します。一方、公立学校や教育委員会が学校の権限、情報、職員、施設、公式行事を用いて加入を事実上強制している場合は、公権力による結社の自由への関与として憲法第21条との関係も問題になります。</p>',
    '<h2>個人情報保護法上の根拠確認</h2>': '<h2>学校保有情報を使う場合の根拠確認</h2>',
    '<p>オプトアウト方式が実務上成立するためには、PTAが事前に「誰が入会対象者か」を把握し、その連絡先にオプトアウト通知を送付する必要があります。しかしこの個人情報の取得プロセスに、学校保有情報の目的外提供や同意の任意性の問題が入り込みやすくなります。これがオプトアウト方式の最大の急所です。</p>': '<p>全保護者を対象とするオプトアウト通知は、学校が保有する在籍・連絡先情報を利用して送付されることが多くあります。この場合、学校自身による利用なのか、PTAへの提供なのかを分け、第61条の所掌事務・業務、第69条第1項又は第2項の根拠、対象情報、本人説明、利用・提供記録を確認します。</p>',
    '<h3>目的外利用・第三者提供の制限（法第69条）</h3>': '<h3>第61条と第69条による利用・提供の確認</h3>',
    '<p>行政機関等（公立学校）は、法令に基づく場合を除き、利用目的以外の目的のために保有個人情報を第三者に提供してはなりません。PTAは学校とは別個の私的団体（第三者）です。学校が保護者の事前同意や法令上の根拠を確認しないままPTAに名簿を提供する場合、個人情報保護法第69条との関係で重大な問題になります。</p>': '<p>公立学校が保有する情報は、第61条に基づく所掌事務・業務と保有の必要性が前提です。その情報をPTA目的で扱う場合は、特定された利用目的の範囲内として第69条第1項により利用・提供できるのか、目的外であれば第2項のどの例外を根拠とするのかを確認します。学校自身による利用と、学校とは別団体であるPTAへの提供は別々に整理します。</p>',
    '<h3>個人情報法上のオプトアウト規定（法第27条第2項）は適用できない</h3>': '<h3>民間部門のオプトアウト提供制度を学校側の根拠にはできない</h3>',
    '<p>民間の個人情報取扱事業者には、一定の要件のもとで第三者提供に関する届出・公表を伴う制度があります。しかし、公立学校が保有する児童・保護者情報は、行政機関等の保有個人情報として第5章の枠組みで扱うべきものです。PTA入会の意思確認もない段階で、学校名簿を使って「同意しない場合は申し出てください」と通知する運用は、同意の任意性・明確性・記録性を欠きます。PTAが保護者に連絡したいなら、学校名簿の流用ではなく、本人がPTAへ直接提出した入会申込書・個人情報同意書を起点にする必要があります。</p>': '<p>民間部門には、一定の要件のもとで第三者提供に関するオプトアウト制度がありますが、公立学校が保有する情報は行政機関等に関する第5章の規律で扱います。民間部門の制度を、そのまま学校保有情報の利用・提供根拠にすることはできません。また、学校が全保護者へ通知できることと、PTAへの入会契約が成立することは別問題です。恒常的な会員管理は、PTAが加入者本人から直接取得した申込記録を起点にします。</p>',
    '<p><strong>論理的帰結：</strong>「個人情報の適法な取得（オプトインでの同意）」がなければ、PTAは保護者に適法にアプローチすることすらできません。入会契約の申込み（オプトアウト通知）自体が物理的・法的に不可能であり、オプトアウト方式は制度として成立しません。</p>': '<p><strong>制度設計上の帰結：</strong>学校が通知を配布又は配信できるとしても、それだけでPTA会員関係は発生しません。PTAは、加入を希望する本人から申込みを受け、承諾し、会員情報を取得した記録を残す必要があります。</p>',
}
for old, new in replacements.items():
    s = replace_once(s, old, new, old[:65])

# Remove the unsupported named-scholar quote box.
s, count = re.subn(r'\s*<div class="alert-block info">\s*<div class="alert-icon">📚</div>.*?</div>\s*</div>', '', s, count=1, flags=re.S)
if count != 1:
    raise SystemExit(f'constitution quote box: expected 1, found {count}')

# Case-law descriptions: distinguish judgment, evidence assessment and settlement.
replacements = {
    '<p>この判決は「PTAは入退会自由の任意加入団体である」ことを前提として確認した上で、原告が長期間にわたり会費を納入し、役員等の活動に主体的に参加していた事実を捉え、「黙示の承諾」または「追認」があったと認定しました。</p>': '<p>熊本地方裁判所判決は、原告の会費納入や活動参加等の個別事情を踏まえて会員関係を判断したものとして参照されます。判決が評価した事実、請求内容、当事者の主張、判断の射程を確認し、PTAのオプトアウト制度一般の有効性を判断した判例として扱わないことが重要です。</p>',
    '<div class="case-point">この判決は「オプトアウト方式の一般的有効性」を認めたものではありません。「事後的な行動（会費納入・活動参加）」によって追認されたという判断です。</div>': '<div class="case-point">会費納入や活動参加等が、個別紛争における合意又は追認の証拠となり得ることと、申込みのない全保護者を制度上会員扱いできることは別です。</div>',
    '<div class="case-point">入学直後でまだ会費も払っておらず活動にも参加していない保護者には、黙示の承諾を認定する根拠がなく、契約関係は「不存在」です。</div>': '<div class="case-point">別の保護者について会員関係が成立しているかは、その人に対する説明、申込み、会費納入、活動参加等の事実から個別に判断されます。判決から一律に結論を移すことはできません。</div>',
    '<h3>福岡高裁和解（2017年）——オプトインへの転換を求める</h3>': '<h3>福岡高裁での和解（2017年）——和解条項の射程</h3>',
    '<p>控訴審の和解条項に「PTAが入退会自由な任意団体であることを将来にわたって保護者に十分に周知すること」が盛り込まれました。司法が最終的に「黙示の承諾に依存する曖昧な運営を戒め、明示的な説明と意思確認（オプトイン）への転換」を求めたことを意味します。</p>': '<p>控訴審では当事者間の和解が成立し、入退会に関する周知等が盛り込まれたとされています。和解は当事者間の合意であり、裁判所が一般的な法理を判示したものではありません。条項の文言と当事者を確認し、明示的な説明と申込記録を整える実務上の参考として扱います。</p>',
    '<div class="cc-title">行政実務上の否定</div>': '<div class="cc-title">行政実務上の見直し</div>',
    '<div class="ts-body">保護者が自ら記入・署名して提出。PTAの任意性・役員義務・退会方法を明記。学校書類と完全に分離して配布。</div>': '<div class="ts-body">紙又は電子フォーム等で、本人の申込みと送信・受理記録を残します。任意加入、会費、活動、退会方法、発行主体、提出先を明記し、学校提出書類と区別します。</div>',
    '<div class="ts-body">PTA活動への個人情報利用目的・提供先・管理方法・廃棄手順を明示した同意書を、入会同意と分離して取得。</div>': '<div class="ts-body">取得項目、利用目的、共有先、管理方法、保存期間を示します。入会意思と情報利用・提供への選択を、同じ用紙を使う場合でも項目と記録を区別します。</div>',
    '<div class="ts-body">PTAが自ら徴収・管理する方法を原則とし、学校徴収金と混同しない。学校が関与する場合でも、根拠文書、対象者名簿、個人情報提供記録、服務上の扱いを別々に確認する。</div>': '<div class="ts-body">PTAによる直接徴収を基本とし、学校徴収金と混同しない。学校が関与する場合は、会員関係、口座情報の利用、校務・服務、決裁、利用・提供記録、会計区分を別々に確認します。</div>',
    '<p>入会申込書が確認できない場合、その問題は単なる書類不備にとどまりません。学校在籍情報からPTA会員関係が当然に発生するわけではなく、PTAとの関係は、本人の加入意思を確認できるオプトイン型申込記録によって初めて確認されます。詳しくは「<a href="/journal/pta-membership-optin-record.html">現行法から分析するPTA入会におけるオプトイン型申込記録の不可欠性</a>」で整理しています。</p>': '<p>入会申込書が確認できない場合、その問題は単なる書類不備にとどまりません。学校在籍情報からPTA会員関係が当然に発生するわけではなく、恒常的な会員管理制度としては、本人の加入意思とPTAの承諾を確認できるオプトイン型申込記録が必要です。後日の行為が個別紛争の証拠となる場合はありますが、全員を会員扱いする制度の代替にはなりません。詳しくは「<a href="/journal/pta-membership-optin-record.html">現行法から分析するPTA入会におけるオプトイン型申込記録の不可欠性</a>」で整理しています。</p>',
    '<div class="case-point">入会意思と個人情報利用同意を、同じ紙で一括処理していないか。利用目的・提供先・廃棄方法は説明されているか。</div>': '<div class="case-point">入会意思と個人情報利用・提供への選択が、項目と記録として区別されているか。利用目的、共有先、保存期間は説明されているか。</div>',
    '<div class="case-point">学校が配布、回収、名簿提供、連絡ツール配信、未納確認に関与している場合、その根拠文書はあるか。</div>': '<div class="case-point">学校が配布、回収、学校保有情報の利用・提供、連絡ツール配信、未納確認に関与している場合、その校務・服務・情報利用・決裁の根拠文書はあるか。</div>',
    '非会員であることを理由に子どもを不利益に扱う運用は、教育を受ける権利、平等取扱い、学校管理上の配慮との関係で重大な問題になります。差別的取扱いが行われた場合は、事実関係を記録し、学校・教育委員会へ照会することが考えられます。': '学校教育上の取扱いをPTA加入状況によって変えることは、学校とPTAの区分や児童生徒への公平な対応の観点から問題です。PTA独自の事業や給付については、実施主体、目的、費用負担、学校行事との関係、子どもへの心理的影響を具体的に確認します。差が生じた場合は、誰が決定したのかを含めて記録し、学校・PTA・教育委員会へ文書で確認します。',
    '「書面」そのものが常に成立要件とは限りませんが、「明示的な申込みの意思表示」は必要です（民法522条）。書面（入会届）であれば証拠として明確であり、教育委員会回答にも「書面等による意思確認」を重視する例があります。': '紙の入会届そのものが常に契約成立要件とは限りませんが、会員管理制度としては、本人の申込みとPTAの承諾を客観的に確認できる記録が必要です。紙、署名、電子フォーム、オンライン申込ログ等を利用できます。口頭申込みを用いる場合も、日時、説明内容、申込者、受理者を記録します。',
}
for old, new in replacements.items():
    s = replace_once(s, old, new, old[:65])

# Editorial layout
membership_css = '''
<style id="membership-editorial-20260710">
.membership-editorial{background:#fff!important}
.membership-editorial .issue-hero-inner,
.membership-editorial .issue-content{grid-template-columns:1fr!important;max-width:920px!important}
.membership-editorial .issue-hero-eyebrow,
.membership-editorial .section-eyebrow,
.membership-editorial .section-kicker{display:none!important}
.membership-editorial .issue-main figure,
.membership-editorial .issue-main>svg{display:none!important}
.membership-editorial .issue-section{margin:0!important;padding:42px 0!important;border-bottom:1px solid #cfd8e2!important}
.membership-editorial .issue-section h2{border-bottom:0!important;padding-bottom:0!important}
.membership-editorial .law-breakdown-grid,
.membership-editorial .conclusion-grid,
.membership-editorial .three-set,
.membership-editorial .ynf-points{display:block!important}
.membership-editorial .law-breakdown-card,
.membership-editorial .conclusion-card,
.membership-editorial .three-set-item,
.membership-editorial .case-block,
.membership-editorial .yokohama-notice-feature,
.membership-editorial .alert-block{
  margin:0!important;
  padding:22px 0!important;
  border:0!important;
  border-bottom:1px solid #dbe4ee!important;
  border-radius:0!important;
  box-shadow:none!important;
  background:#fff!important;
}
.membership-editorial .lbc-verdict,
.membership-editorial .case-badge,
.membership-editorial .ynf-label{
  padding:0!important;
  background:transparent!important;
  color:var(--color-navy)!important;
  border-radius:0!important;
}
.membership-editorial .case-block-head{border-radius:0!important}
.membership-editorial .case-body{padding:18px 0 0!important}
.membership-editorial .case-point{border-radius:0!important}
.membership-editorial .ynf-actions a,
.membership-editorial .btn-navy,
.membership-editorial .btn-soft{
  display:inline!important;
  padding:0!important;
  background:transparent!important;
  color:var(--color-navy)!important;
  border:0!important;
  border-radius:0!important;
  text-decoration:underline!important;
  text-underline-offset:.18em!important;
}
.membership-editorial .ynf-actions{gap:8px 20px!important}
.membership-editorial .faq-list,
.membership-editorial details{border-radius:0!important}
.membership-editorial details{background:#fff!important}
.membership-editorial details summary{padding-left:0!important;padding-right:0!important}
.membership-editorial details>div{padding-left:0!important;padding-right:0!important}
.membership-editorial .issue-content+section>div>div:last-child{display:none!important}
</style>
'''
s = replace_once(s, '</head>', membership_css + '</head>', 'membership css')
p.write_text(s, encoding='utf-8')
