from pathlib import Path


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: expected 1 occurrence, found {count}")
    return text.replace(old, new)


path = Path('PTA運営適正化ガイドブック_第4版_改訂本文.html')
text = path.read_text(encoding='utf-8')

text = replace_once(text, '<body>', '<body class="guidebook-editorial">', 'body')

text = replace_once(
    text,
    '<h3>1-5　文部科学省が示す「学校が関与できる限界」──業務の3分類</h3>',
    '<h3>1-5　文部科学省が示す学校・教師の役割分担──業務の3分類と2025年通知</h3>',
    'mext heading',
)
text = replace_once(
    text,
    '<p>「学校徴収金の徴収・管理」でさえ「学校以外が担うべき業務」であり、地域ボランティア（PTAを含む）との「連絡調整」もまた「学校以外が担うべき業務」とされています。<em class="warn">学校がPTAに関与できるのは連絡調整まで</em>──これが国の示した境界線です。PTA会費の管理・PTA事務の代行はその限界を大幅に超えています。</p>',
    '<p>業務の3分類は、学校・教師が担ってきた業務の主たる担い手を整理し、負担軽減と役割分担を進める政策資料です。学校がPTAに関与できる法的上限を「連絡調整だけ」と定めた規定ではありません。ただし、会員管理、会費徴収、役員選出、会計等のPTA内部事務を学校が担う場合は、具体的作業、校務としての位置づけ、職務命令、個人情報利用、会計規程等の根拠が別途必要です。さらに文部科学省の2025年通知は、学校給食費以外の学校徴収金について、公会計化だけでなく、保護者から業者等への直接支払など学校を経由しない方法を示しました。</p>',
    'mext explanation',
)
text = replace_once(
    text,
    '<div class="principle-box">\n  <p>文部科学省は明示している。<br>学校がPTAに関与できるのは「連絡調整まで」である。<br>学校徴収金の徴収・管理でさえ「学校以外が担うべき業務」である。<br>PTA会費の管理・PTA事務の代行は、この限界を大幅に超えている。</p>\n</div>',
    '<div class="principle-box">\n  <p>学校教育に必要な学校徴収金であっても、徴収・管理を学校の外へ移す政策が進められています。PTA会費はこの通知の直接の対象ではありませんが、学校が恒常的に徴収・管理する場合には、加入契約、学校の事務権限、学校保有口座情報の利用、会計区分、教職員の作業をより明確に説明する必要があります。</p>\n</div>',
    'mext principle',
)

text = replace_once(
    text,
    '<p>入学手続と一体化した案内で「全員加入」が前提であるかのように扱い、任意加入であることを一切説明しない運用は、<em class="warn">「加入しなければならない」という誤認を生じさせる可能性</em>があり、消費者契約法上の取消しや条項の有効性が問題となり得ます。ただし、自動加入の運用だけで直ちに契約が無効になるとは限らず、会費納入などの具体的事情から黙示の合意が認定されることもあります。加入意思、会費、個人情報利用を分けて記録することが重要です。</p>',
    '<p>入学手続と一体化した案内で「全員加入」が前提であるかのように扱い、任意加入であることを説明しない運用は、<em class="warn">「加入しなければならない」という誤認を生じさせる可能性</em>があり、消費者契約法上の取消しや条項の有効性が問題となり得ます。学校への入学、PTAからの一方的通知、保護者の沈黙だけでは加入申込みを確認できません。個別紛争では後日の会費納入や活動参加が証拠として検討されることがありますが、それは恒常的なみなし加入制度を正当化するものではありません。制度としては本人の積極的な申込みとPTAの承諾を客観的に記録します。</p>',
    'consumer opt-in',
)

text = replace_once(
    text,
    '<h2>第３章　個人情報保護法第69条──学校からPTAへの情報提供という根本問題</h2>',
    '<h2>第３章　学校保有情報のPTA目的利用・提供──第61条と第69条</h2>',
    'chapter 3 heading',
)
text = replace_once(text, '<h3>3-1　第69条の構造──原則禁止と例外</h3>', '<h3>3-1　第61条・第69条の構造──所掌事務、利用目的、例外</h3>', '3-1 heading')
text = replace_once(
    text,
    '<p>公立学校は行政機関であり、保有する個人情報については個人情報の保護に関する法律（個人情報保護法）の「行政機関等」に関する規定が適用されます。同法第69条は、目的外利用・提供を<em class="warn">原則として禁止</em>しています。</p>',
    '<p>公立学校が保有する個人情報には、個人情報保護法の「行政機関等」に関する規定が適用されます。第61条は、法令の定める所掌事務又は業務を遂行するために必要な場合に限って個人情報を保有できるとし、第62条は利用目的の明示を求め、第69条は利用目的外の利用・提供を原則として制限しています。</p>',
    '61 and 69 intro',
)
text = replace_once(
    text,
    '<p>学校が就学手続で取得した保護者・児童生徒の個人情報は、「就学・在籍管理・安全確保・教育活動」のために取得したものです。この情報をPTAに提供することは、<em class="warn">取得目的の範囲外の第三者提供</em>です。PTAは公立学校とは別の民間団体であり、「同一行政機関内部の利用」でも「他の行政機関への提供」でもありません。</p>',
    '<p>学校が教育目的で取得した保護者・児童生徒情報をPTA会員管理、会費徴収、役員選出等へ使う場合は、まず学校自身による目的外利用なのか、学校からPTAへの提供なのかを分けます。学校自身が口座振替データや名簿をPTA目的で使う場合も、第61条・第69条との関係が生じます。PTAへ情報を渡す場合は、別組織への提供として、利用目的と第69条第2項等の具体的根拠を確認します。</p>',
    'own use and provision',
)
text = replace_once(text, '<div class="notice-box-title">第27条ではなく、第69条で整理する</div>', '<div class="notice-box-title">第61条・第69条を中心に整理する</div>', 'notice heading')
text = replace_once(
    text,
    '<p style="font-size:13px; margin-bottom:8px;">この問題を検討する際、民間事業者を主な対象とする個人情報保護法第27条（第三者提供の制限）だけで整理しては足りません。公立学校が保有する児童生徒・保護者情報は、地方公共団体の機関が保有する<em class="blue">保有個人情報</em>として扱われるため、学校からPTAへの提供は、同法第69条（利用及び提供の制限）を中心に検討する必要があります。</p>',
    '<p style="font-size:13px; margin-bottom:8px;">民間事業者を主な対象とする第27条だけで整理しては足りません。公立学校が保有する児童生徒・保護者情報は、地方公共団体の機関が保有する<em class="blue">保有個人情報</em>です。学校自身によるPTA目的での利用は第61条・第69条、学校からPTAへの提供は第69条を中心に確認します。</p>',
    'notice body',
)

text = replace_once(text, '<h3>3-2　「本人の同意」という例外は、現場では機能しない</h3>', '<h3>3-2　本人同意を根拠とする場合の条件</h3>', '3-2 heading')
text = replace_once(
    text,
    '<p>まず、<em class="blue">同意が有効であるためには、保護者が「PTAへの情報提供に同意しない」という選択肢を実質的に行使できなければなりません</em>。しかし現状では、PTA加入が学校手続と一体化しており、「加入しない・情報提供に同意しない」ことで生じる不利益が明確でない、あるいは現実に不利益が生じる環境にあります。このような状況下での同意は、<em class="warn">自由な意思による同意とはいえません</em>。</p>',
    '<p><em class="blue">本人同意を根拠とする場合は、保護者が「PTAへの情報提供に同意しない」という選択肢を実質的に行使できることが重要です</em>。PTA加入や学校手続と一体化し、拒否した場合の取扱いが不明確な方式では、同意の自由性に疑問が生じます。提供先、情報項目、利用目的、保存期間、撤回方法を具体的に示し、不同意による学校教育上の不利益を生じさせない設計が必要です。</p>',
    'consent freedom',
)
text = replace_once(
    text,
    '<p>次に、PTAに加入しない保護者や、同意しない保護者の個人情報は、提供できません。全員から同意を得ることは、一部の保護者が拒否した瞬間に不可能になります。<em class="warn">同意を全員から得られると限らない以上、学校が一括してPTAへ情報提供する「同意ベース」の仕組みは、制度設計として根本的に成立しません</em>。</p>',
    '<p>同意しない保護者の情報は、同意を根拠として提供することはできません。一覧形式で提供する場合は、不同意者の情報を削除・マスキングする手順と提供記録が必要です。同意方式は技術的に構成できますが、恒常的な会員管理を学校名簿に依存させる設計は、不同意者の除外、更新、退会、目的変更のたびに学校側の処理を要し、PTA自身による直接取得よりも複雑で誤りを生じやすい方式です。</p>',
    'consent mechanism',
)
text = replace_once(text, '<div class="notice-box-title">「同意があれば提供できる」という理解の誤り</div>', '<div class="notice-box-title">同意があれば何でも提供できるわけではない</div>', 'consent notice heading')
text = replace_once(
    text,
    '<p style="font-size:13px; margin-bottom:0;">「本人同意があれば学校からPTAへ情報提供できる」という理解は半分しか正しくありません。同意しない保護者の情報は提供できず、同意しない保護者が一人でもいれば、その人の情報はPTA名簿から除外しなければなりません。「全員同意」を前提にした一括提供は、制度上ありえません。PTAが必要な情報は、PTAが入会申込書を通じて入会した会員本人から直接取得する以外に方法はありません。</p>',
    '<p style="font-size:13px; margin-bottom:0;">本人同意は第69条第2項の根拠の一つですが、同意の対象、提供項目、利用目的、提供先、不同意者の除外、提供記録まで具体化する必要があります。PTAが必要な情報を加入者本人から直接取得する方式は、加入記録と利用目的を一体で管理できるため、恒常的な会員管理の基本方式として最も明確です。</p>',
    'consent notice body',
)

text = replace_once(
    text,
    '<p>つまり、PTAが会員の個人情報を必要とするなら、<em class="blue">PTAが入会申込書を通じて入会した会員本人から直接取得する</em>のが正しい手順です。学校経由での一括取得は、この原則に反します。</p>',
    '<p>PTAが会員の個人情報を必要とするなら、<em class="blue">PTAが入会申込書や電子フォーム等を通じて加入者本人から直接取得する</em>ことを基本とします。学校経由の取得を行う場合は、学校自身の利用とPTAへの提供を分け、法的根拠、対象項目、不同意者の除外、更新・削除手順を別途説明しなければなりません。</p>',
    'direct acquisition',
)
text = replace_once(
    text,
    '<p>PTAがものごとを完結させなければならない──これが法令の要請です。<em class="warn">PTA加入の勧誘・入会申込の受付・個人情報の取得・会費の徴収・会計の管理・名簿の作成・退会の受付</em>、これらすべてをPTAが自ら行い、<em class="warn">学校はその一切に関与しない</em>。これが法令が示す正しい姿です。</p>',
    '<p>加入の勧誘、入会申込の受付、会員情報の取得、会費の請求・会計、名簿作成、退会受付は、PTA内部手続としてPTA自身が責任を持つことが基本です。学校が配布、施設利用、連絡調整等で協力する場合は、学校の情報、職員、施設、媒体をどの範囲で使うのか、その根拠と責任主体を文書で分けます。</p>',
    'PTA responsibility',
)

text = replace_once(text, '<h3>3-4　学校連絡ツールの使用も認められない</h3>', '<h3>3-4　学校連絡ツールを使う場合の確認</h3>', 'school tool heading')
text = replace_once(
    text,
    '<p><em class="warn">学校連絡ツールによるPTA通知の配信は、学校とPTAの切り分けという観点から認められません</em>。PTAが会員に連絡したい場合は、PTAが自ら管理する連絡手段（PTAが自ら収集した会員の連絡先）を使う必要があります。学校のシステムを間借りすることは、情報の混同と目的外利用を構造的に生み出します。</p>',
    '<p>PTA内部連絡は、PTAが自ら取得した会員連絡先と自前の連絡手段で行うことが最も明確です。学校連絡ツールを利用する場合は、送信主体、対象者、利用目的、学校保有連絡先を使う根拠、承認者、配信記録、非会員への配信の必要性を確認し、学校の公式連絡とPTAの通知を明確に区別します。学校ツールを使うこと自体を一律に評価するのではなく、具体的な情報利用と責任主体を検証します。</p>',
    'school tool body',
)
text = replace_once(
    text,
    '<p style="font-size:13px; margin-bottom:8px;">個人情報保護委員会は令和8年3月、教育委員会・公立学校関係者・PTA関係者向けに、公立学校とPTAの間の個人情報のやり取りについての資料を公表しました。この資料は、学校からPTAへの個人情報提供が法律上いかに困難であるかを改めて明確にしています。</p>',
    '<p style="font-size:13px; margin-bottom:8px;">個人情報保護委員会は令和8年3月、教育委員会・公立学校関係者・PTA関係者向けに、公立学校とPTAの間の個人情報のやり取りについての資料を公表しました。この資料は、学校保有情報をPTA目的で利用・提供する際に、利用目的、第69条の例外根拠、本人同意、不同意者の削除・マスキング等を具体的に確認する必要があることを示しています。</p>',
    'PPC summary',
)

text = replace_once(
    text,
    '<p>入会申込記録がない場合、以下のすべてが法的根拠を失います：会員の確定・非会員の特定・会費請求の根拠・名簿の根拠・議決権の確認・役員選出の正当性・個人情報利用の根拠、そして「非会員への配慮」も。</p>',
    '<p>入会申込記録がない場合、会員の確定、会費請求、名簿、議決権、役員選出、個人情報利用の根拠を客観的に説明することが困難になります。後日の会費納入や活動参加が個別の証拠となる場合はありますが、恒常的な会員管理制度としては、申込みと承諾を記録する必要があります。</p>',
    'no membership record',
)
text = replace_once(text, '入会申込記録が保存されているか（存在しない場合は施設利用許可の見直しが必要）', '入会申込記録が保存されているか（存在しない場合は学校協力・施設利用の前提を再点検する）', 'facility record check')
text = replace_once(
    text,
    '<p>学校徴収金でさえ「学校以外が担うべき業務」（文科省業務の3分類）とされているのに、PTA会費（任意団体の私費）を学校が徴収・管理することは、さらに大きな問題です。学校徴収金とPTA会費が同じ口座振替で引き落とされることで、保護者はPTA会費を義務的費用と認識します。これはPTA加入の任意性を根底から覆し、消費者契約法上の問題とも連動します。</p>',
    '<p>文部科学省の業務の3分類は学校徴収金の徴収・管理を学校以外が担うべき業務として整理し、2025年通知は学校給食費以外の学校徴収金について、公会計化に加えて学校を経由しない直接支払を示しました。この通知はPTA会費を直接規律するものではありませんが、学校教育に必要な費用ですら学校外へ移す政策方向との対比は重要です。PTA会費を学校徴収金と同じ案内、口座、引落し、未納管理で扱う場合は、加入契約、学校保有口座情報の利用、学校の事務権限、決裁、会計区分を個別に説明する必要があります。</p>',
    '2025 fee context',
)
text = replace_once(
    text,
    '<p>第３章で詳述したとおり、学校からPTAへの個人情報提供は個人情報保護法第69条の原則禁止に服します。「本人の同意があれば提供できる」という理解も、同意しない保護者が一人でもいれば機能しません。<em class="warn">PTAが自ら入会申込書で取得する以外の方法はない</em>のです。</p>',
    '<p>学校保有情報をPTA目的で扱う場合は、学校自身による利用とPTAへの提供を分け、第61条・第69条の根拠を確認します。本人同意を根拠とする場合は、不同意者の情報を除外し、対象項目、利用目的、提供記録を明確にします。恒常的な会員管理は、PTAが加入者本人から直接取得する方式を基本とするのが最も明確です。</p>',
    '6-3 privacy',
)
text = replace_once(
    text,
    '<p>第３章で整理したとおり、学校アプリによるPTA通知配信は目的外利用・情報混同・非会員への配信の三つの問題を生じさせます。<em class="warn">学校連絡ツールはPTA通知に使わない</em>──これは交渉の余地のない原則です。</p>',
    '<p>学校アプリによるPTA通知配信では、学校保有連絡先の利用目的、送信主体、対象者、学校の公式連絡との区別、非会員への配信の必要性、承認・配信記録を確認します。PTA内部連絡は自前の連絡手段を基本としつつ、学校ツールを利用する場合は具体的な根拠と責任主体を明示します。</p>',
    '6-4 school tool',
)
text = replace_once(
    text,
    '<p>「昔からやっている」「PTAに頼まれた」「委任されている」は法的根拠になりません。勤務時間中のPTA事務には職専免が必要です。「委任されているから校務になる」という論理は法的に成立しません。</p>',
    '<p>「昔からやっている」「PTAに頼まれた」「委任されている」という事情だけで、勤務時間中の作業が当然に校務になるわけではありません。具体的作業が校務として特定されているか、職務命令があるか、職務外なら職専免又は兼職兼業等の手続があるか、対象者、時間、決裁を確認します。</p>',
    '6-5 personnel',
)
text = replace_once(
    text,
    '<p>PTAから委任を受けていることを理由に教職員がPTA事務を処理する運用が各地で見られますが、<em class="warn">委任の存在は教職員が勤務時間中にその業務を行える根拠になりません</em>。「委任されているから校務になる」という論理は法的に成立しません。</p>',
    '<p>PTAから学校又は教職員への依頼・委任は、PTA側の意思を示す資料にはなりますが、それだけで学校側の事務権限、校務としての位置づけ、職務命令、個人情報利用、会計処理の根拠が生じるわけではありません。委任文書と、学校側の規則・決裁・服務上の根拠を分けて確認します。</p>',
    'delegation',
)

text = replace_once(text, '<p>現在のPTA運営の状態は、<em class="warn">非常に訴訟リスクの高い状態</em>です。リスクはPTAだけでなく、学校・教育委員会にも及びます。</p>', '<p>学校手続とPTA内部事務が混在する運営には、契約、個人情報、会計、服務、施設管理にまたがる法的・行政管理上のリスクがあります。リスクの有無と責任範囲は、個別の事実と記録に基づいて確認します。</p>', 'risk intro')
text = replace_once(text, '<div class="risk-item"><strong>会費返還請求（不当利得）</strong>──入会申込記録なしに徴収した会費は、法律上の原因なく取得した不当利得（民法第703条）として返還請求の対象になる</div>', '<div class="risk-item"><strong>会費返還請求</strong>──入会申込み、PTAの承諾、会費額、本人の認識、支払経緯を確認できない場合は、民法第703条等に基づく返還の成否が争点となり得る</div>', 'refund risk')
text = replace_once(text, '<div class="risk-item"><strong>消費者契約法に基づく取消・返還請求</strong>──任意加入の説明なし・誤認を生じさせる勧誘・困惑させての契約締結は、消費者契約法第4条に基づく取消の対象</div>', '<div class="risk-item"><strong>消費者契約法に基づく取消し等</strong>──任意加入の説明、勧誘内容、誤認・困惑と意思表示の因果関係によっては、消費者契約法第4条等の適用が争点となり得る</div>', 'consumer risk')
text = replace_once(text, '<div class="risk-item"><strong>個人情報漏えいに対する損害賠償請求</strong>──無断取得・目的外利用・不適切な第三者提供は個人情報保護法違反となり、損害賠償請求および個人情報保護委員会による調査・勧告・命令の対象</div>', '<div class="risk-item"><strong>個人情報の利用・提供に関する責任</strong>──利用目的、例外根拠、安全管理、提供記録等に問題がある場合は、個人情報保護委員会による調査・指導等や、具体的損害に応じた賠償責任が検討され得る</div>', 'privacy risk')

text = replace_once(text, 'PTA会計書類の保管場所──学校が保管している場合は問題', 'PTA会計書類の保管場所──学校が保管する場合の根拠、管理責任、閲覧権限、引継ぎ記録', 'account document check')
text = replace_once(text, '兼職・兼業届出文書（校長・教頭等がPTA役員に就く場合は必須）', '兼職・兼業、職専免その他の服務関係文書（校長・教頭等がPTA役員に就く場合の適用関係を確認）', 'outside work check')

text = replace_once(text, '<li>学校連絡ツールはPTA通知配信に使えない</li>', '<li>学校連絡ツールをPTA通知へ使う場合は、利用目的、送信主体、対象者、承認・配信記録を確認する</li>', 'training school tool')
text = replace_once(text, '<li>校長・教頭のPTA役員就任は利益相反であり、社会教育法第12条との関係で問題がある</li>', '<li>校長・教頭がPTA役員を兼ねる場合は、学校管理職としての権限とPTA役員としての立場、勤務時間、決裁、利益相反を分ける</li>', 'training officers')
text = replace_once(text, '<li>学校がPTAに関与できるのは連絡調整まで（文科省業務の3分類）</li>', '<li>文科省の業務の3分類は役割分担の政策資料であり、PTA内部事務を学校が担う場合は別途、校務・服務・情報・会計上の根拠を確認する</li>', 'training mext')

text = replace_once(
    text,
    '<p>学校からPTAへの個人情報提供が疑われる場合、確認すべき中心条文は個人情報保護法第69条です。保護者は、学校がどの利用目的で情報を取得し、PTAにどの情報を、どの根拠で、どの範囲で提供したのかを確認する必要があります。</p>',
    '<p>学校保有情報がPTA目的で使われている場合は、学校自身による利用とPTAへの提供を分けます。第61条の所掌事務・業務、第62条の利用目的、第69条の利用・提供制限を中心に、学校がどの情報を、何の目的で、どの根拠により、どの範囲で利用又は提供したのかを確認します。</p>',
    '11-2 privacy',
)

text = replace_once(
    text,
    '<div class="qa-a"><span class="qa-a-label">A</span>理論上は同意があれば提供できますが（個人情報保護法第69条第2項第1号）、「全員から同意を取る」ことは、一人でも拒否した時点で不可能になります。同意しない保護者の情報は提供できず、削除・マスキングが必要です（個人情報保護委員会・令和8年3月）。「全員同意」を前提にした一括提供の仕組みは制度設計として成立しません。PTAが必要な情報は、PTAが入会申込書を通じて会員本人から直接取得するしかありません。</div>',
    '<div class="qa-a"><span class="qa-a-label">A</span>本人同意は第69条第2項の根拠の一つです。ただし、同意しない人の情報を除外し、提供項目、利用目的、提供先、保存期間、撤回方法、提供記録を具体化する必要があります。一覧の削除・マスキングを含む同意方式は構成できますが、恒常的な会員管理ではPTAが加入者本人から直接取得する方式の方が明確で、学校側の継続的処理も減らせます。</div>',
    'FAQ consent',
)
text = replace_once(
    text,
    '<div class="qa-a"><span class="qa-a-label">A</span>三つの問題があります。①学校アプリで収集した保護者の連絡先情報をPTA通知配信に使うことは、収集目的外の利用（個人情報保護法上の問題）。②学校公式システムとPTA通知が混在することで、保護者がPTA通知を学校の公式連絡と誤認する構造が生まれる（消費者契約法上の誤認を助長）。③PTA非加入者にもPTA通知が届くことで「全員がPTA会員」という前提が強化される（任意加入の形骸化）。これらは「協力」ではなく「公私混同」であり、法令上の問題です。</div>',
    '<div class="qa-a"><span class="qa-a-label">A</span>学校アプリを使う場合は、①学校保有連絡先をPTA目的に使う根拠、②送信主体と承認者、③学校の公式連絡との表示上の区別、④非会員を含む配信対象と必要性、⑤配信記録を確認します。これらを説明できない運用は公私混同と目的外利用の問題を生じさせます。PTA内部連絡はPTA自身の連絡手段を基本とする方が明確です。</div>',
    'FAQ school tool',
)
text = replace_once(
    text,
    '<div class="qa-a"><span class="qa-a-label">A</span>慣行は法律を上書きしません。入会申込記録がない場合、誰が会員かを証明できず、会費請求・名簿・議決権・役員選出・個人情報利用のすべての根拠が失われます。さらに、消費者契約法上の取消リスク・不当利得返還リスクも生じます。「長年続いてきた」ことは正当であることの証明にはなりません。長年問題が放置されてきたことを意味するだけです。</div>',
    '<div class="qa-a"><span class="qa-a-label">A</span>慣行だけでは入会申込みを客観的に確認できません。会費納入や活動参加等が個別の証拠として検討される場合はありますが、会員、会費、議決権、役員選出、個人情報利用を恒常的に管理する制度としては、申込みと承諾の記録が必要です。過去分の返還や取消しは、本人の認識、支払経緯、会則、説明内容等の個別事情に基づいて検討します。</div>',
    'FAQ no record',
)

text = replace_once(text, '<strong>学校の管理職（校長・副校長・教頭）は、本会の役員に就任しない</strong>ものとする。', '<strong>学校の管理職が本会の役員を兼ねる場合は、学校管理職としての権限とPTA役員としての権限、勤務時間、決裁及び利益相反を明確に区分する</strong>ものとする。', 'appendix officers')
text = replace_once(text, '第○条　会員への連絡は、<strong>本会が管理する連絡手段</strong>を用いる。学校が管理する連絡ツール（学校アプリ等）は、本会の通知配信に使用しない。', '第○条　会員への内部連絡は、<strong>本会が管理する連絡手段</strong>を基本とする。学校が管理する連絡ツールを利用する場合は、送信主体、対象者、利用目的、承認・配信記録及び学校公式連絡との区別を定める。', 'appendix communications')

start_marker = '<!-- ======== 第12章 ======== -->'
end_marker = '<h2>第13章　よくある質問（Q&amp;A）</h2>'
start = text.find(start_marker)
end = text.find(end_marker)
if start == -1 or end == -1 or end <= start:
    raise SystemExit('chapter 12 markers not found')
text = text[:start] + '<h2>第12章　よくある質問（Q&amp;A）</h2>' + text[end + len(end_marker):]

style = '''
<style id="guidebook-editorial-20260710">
.guidebook-editorial .cover-tag{display:none}
.guidebook-editorial .principle-box,
.guidebook-editorial .risk-box,
.guidebook-editorial .case-box,
.guidebook-editorial .social-box,
.guidebook-editorial .mext-box,
.guidebook-editorial .judgment-box,
.guidebook-editorial .paradox-box,
.guidebook-editorial .ppc-box,
.guidebook-editorial .check-box,
.guidebook-editorial .notice-box,
.guidebook-editorial .info-box,
.guidebook-editorial .flow-box{
  background:#fff!important;
  border:0!important;
  border-left:3px solid #1a4a8a!important;
  border-radius:0!important;
  padding:16px 0 16px 20px!important;
}
.guidebook-editorial .risk-box-title,
.guidebook-editorial .case-box-title,
.guidebook-editorial .social-box-title,
.guidebook-editorial .mext-box-title,
.guidebook-editorial .judgment-box-title,
.guidebook-editorial .paradox-box-title,
.guidebook-editorial .ppc-box-title,
.guidebook-editorial .check-box-title,
.guidebook-editorial .notice-box-title,
.guidebook-editorial .info-box-title{
  display:block!important;
  padding:0 0 7px!important;
  background:transparent!important;
  color:#1a3060!important;
  letter-spacing:.04em!important;
}
.guidebook-editorial .risk-item::before,
.guidebook-editorial .case-item::before{content:'—'!important;color:#64748b!important}
.guidebook-editorial .flow-num{border-radius:2px!important}
</style>
'''
if 'guidebook-editorial-20260710' not in text:
    text = text.replace('</head>', style + '</head>', 1)

path.write_text(text, encoding='utf-8')
