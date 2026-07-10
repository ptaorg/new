from pathlib import Path


def replace_required(text: str, old: str, new: str, label: str, expected: int | None = 1) -> str:
    count = text.count(old)
    if count == 0:
        raise RuntimeError(f"{label}: replacement source not found")
    if expected is not None and count != expected:
        raise RuntimeError(f"{label}: expected {expected}, found {count}")
    print(f"{label}: {count} replacement(s)")
    return text.replace(old, new)


def replace_optional(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    print(f"{label}: {count} replacement(s)")
    return text.replace(old, new)


def patch_membership() -> None:
    path = Path("membership.html")
    text = path.read_text(encoding="utf-8")
    before = len(text)

    text = replace_required(
        text,
        "📋 Issue 01 — Membership",
        "論点1　入会手続",
        "membership kicker",
    )
    text = replace_required(
        text,
        '<p>任意団体への加入は、申込みと承諾を確認できることが基本です。「拒否しなければ加入」というオプトアウト方式・みなし加入だけで直ちに契約が無効になるとは限らず、会費納入などから黙示の合意が認定される場合もあります。後から追認・既成事実化されたと評価されないよう、加入意思、会費、個人情報利用を分けて記録することが重要です。</p>',
        '<p>学校への入学や在籍、PTAからの一方的な通知、保護者の沈黙だけでは、PTAへの加入は成立しません。PTAが会員関係を主張するには、本人による加入の申込みとPTAによる承諾を客観的に確認できる必要があります。個別の紛争で事後の行為が争点になることと、恒常的な加入制度を黙示の合意で運用することは別問題です。制度として採用できるのは、本人が積極的に申し込むオプトイン方式です。</p>',
        "membership hero thesis",
    )
    text = replace_required(text, "このページの構成", "目次", "membership toc label")
    text = replace_required(
        text,
        "「有効」と「無効」——入会同意の2つのルート",
        "オプトインで成立を確認し、オプトアウトでは成立を推定しない",
        "membership figure heading",
    )
    text = replace_required(
        text,
        "有効（オプトイン）と無効（オプトアウト）の2ルート",
        "成立を確認できるオプトインと、成立を推定できないオプトアウトの対比",
        "membership figure aria",
    )
    text = replace_optional(
        text,
        "契約は成立していない",
        "沈黙だけでは契約成立を確認できない",
        "membership contract label",
    )
    text = replace_optional(
        text,
        "消費者契約法上も無効の可能性",
        "消費者契約法上の不当条項・不当勧誘も問題となる",
        "membership consumer label",
    )
    text = replace_optional(
        text,
        "✗ 法的に無効",
        "✗ 加入制度として採用できない",
        "membership invalid label",
    )
    text = replace_required(
        text,
        "書面だけでなく、その後の会費納入や活動参加を含む具体的事情も契約成立の判断材料になり得ます。",
        "個別の紛争では事後の行為が主張されることがありますが、それは恒常的な加入制度を黙示の合意で代替できることを意味しません。",
        "membership post conduct explanation",
    )
    text = replace_required(
        text,
        "沈黙だけを承諾と扱うことには成立根拠の説明が必要です。一方、会費納入などの具体的事情から黙示の合意が認定される場合もあるため、申込みと承諾を記録します。",
        "沈黙や未提出は承諾の意思表示ではありません。会費納入等が個別紛争で争点になることはあっても、PTAが全保護者を一律に会員と扱う制度上の根拠にはなりません。申込みと承諾を、加入時点で客観的に記録する必要があります。",
        "membership silence explanation",
    )
    text = replace_required(
        text,
        "結論：オプトアウト方式は制度として物理的・法的に成立しない",
        "結論：オプトアウト方式はPTAの加入制度として採用できない",
        "membership optout conclusion",
    )
    text = replace_required(
        text,
        "適法なアプローチの起点（個人情報の取得）が不可能な以上、オプトアウト方式は実施プロセスの最初の段階から崩壊している。",
        "学校在籍者全員の情報を先に利用し、拒否しない人を会員と扱うオプトアウト方式は、加入意思と情報取得の双方で根拠を欠きます。PTAが加入者本人から申込みと必要情報を直接取得するオプトイン方式へ改める必要があります。",
        "membership process conclusion",
    )
    text = replace_required(
        text,
        "※ 契約成立には申込みと承諾の合致が必要です。書面がなくても具体的事情から黙示の合意が認定される場合があるため、加入意思と会費納入を記録します。",
        "※ 契約成立には申込みと承諾の合致が必要です。個別紛争で黙示の合意が主張されることはあっても、PTAの恒常的な加入制度をそれに依存させることはできません。加入時点で、本人の申込みとPTAの承諾を客観的に記録します。",
        "membership civil law note",
    )

    # Remove the duplicated hero table of contents visually while retaining the detailed sidebar TOC.
    style = """\n<style id=\"membership-editorial-fix\">\n.issue-hero-inner{grid-template-columns:minmax(0,1fr)!important;max-width:920px!important}\n.issue-hero-toc{display:none!important}\n.issue-hero-eyebrow,.section-eyebrow{text-transform:none!important;letter-spacing:.03em!important;border-radius:3px!important}\n</style>\n"""
    text = replace_required(text, "</head>", style + "</head>", "membership editorial CSS")

    if "直ちに契約が無効になるとは限らず" in text:
        raise RuntimeError("membership: old ambiguous hero statement remains")
    if "制度として採用できるのは、本人が積極的に申し込むオプトイン方式です" not in text:
        raise RuntimeError("membership: new central thesis missing")

    path.write_text(text, encoding="utf-8")
    print(f"membership.html: {before} -> {len(text)} bytes")


def patch_privacy() -> None:
    path = Path("privacy.html")
    text = path.read_text(encoding="utf-8")
    before = len(text)

    text = replace_required(text, "🔒 Issue 02 — Privacy", "論点2　個人情報", "privacy kicker")
    text = replace_required(
        text,
        '<p>公立学校が保有する名簿・住所・電話番号を、PTA運営のために本人同意等の根拠なく渡すことは、個人情報保護法第69条に抵触し得ます。PTAが必要な情報は、学校名簿の流用ではなく、会員本人から直接取得するのが基本です。</p>',
        '<p>公立学校が教育目的で保有する名簿・住所・電話番号等をPTA内部事務に使う場合は、まず学校自身による目的外利用なのか、学校からPTAへの提供なのかを分けます。いずれも個人情報保護法第61条・第69条の枠組みに照らし、所掌事務、利用目的、本人同意その他の具体的根拠を確認しなければなりません。PTAが必要な会員情報は、加入者本人から直接取得するのが基本です。</p>',
        "privacy hero thesis",
    )
    text = replace_required(
        text,
        "このページでは、学校保有情報を使うルートと、PTAが会員本人から直接取得するルートを分け、現場で起きやすい問題パターンを整理します。",
        "このページでは、学校自身が学校保有情報をPTA事務に利用する場合、学校からPTAへ提供する場合、PTAが加入者本人から直接取得する場合の三つを分け、現場で起きやすい問題を整理します。",
        "privacy route explanation",
    )
    text = replace_required(text, "🏫 学校（School）", "学校", "privacy school label")
    text = replace_required(text, "（Third Party）", "学校とは別の外部団体", "privacy PTA label")
    text = replace_required(
        text,
        "個人情報保護法 第69条違反",
        "第69条第2項等の具体的根拠がなければ認められない",
        "privacy flow legal label",
    )
    text = replace_required(text, "✅ 有効（適法）", "✅ PTAによる直接取得", "privacy direct collection label")
    text = replace_required(
        text,
        "PTAが配布した入会届に保護者が自ら記入し、PTA活動への情報利用に「明確に同意（オプトイン）」して提出した場合",
        "PTAが加入の任意性と利用目的を明示し、加入者本人が入会申込書等へ自ら記入してPTAへ提出した場合",
        "privacy direct collection explanation",
    )
    old_law_para = '<p>法改正による個人情報保護制度の一元化後、公立学校を含む地方公共団体側の個人情報取扱いは、個人情報保護法第5章の規律として整理されます。PTAは学校とは別の独立した私的団体であり、学校名簿の提供は学校内部の利用ではなく、外部団体への提供として確認する必要があります。</p>'
    new_law_para = '<p>法改正による個人情報保護制度の一元化後、公立学校を含む地方公共団体側の個人情報取扱いは、個人情報保護法第5章の規律として整理されます。第61条では、法令の定める所掌事務又は業務を遂行するために必要な場合に限って保有できるため、PTAの会員管理、会費徴収、役員選出等を学校の所掌事務・業務として特定できるかが前提になります。</p><p>そのうえで、第69条は利用目的外の利用・提供を原則として禁止しています。学校が自ら学校保有情報をPTA内部事務に使う場合と、学校からPTAへ情報を渡す場合を分け、第69条第2項各号のどの根拠によるのかを確認します。PTAは学校とは別の私的団体であり、学校在籍情報から会員関係が発生するわけではありません。</p>'
    text = replace_required(text, old_law_para, new_law_para, "privacy sections 61 and 69")

    if "個人情報保護法 第69条違反" in text:
        raise RuntimeError("privacy: categorical diagram label remains")
    if "学校自身による目的外利用なのか" not in text:
        raise RuntimeError("privacy: school self-use distinction missing")

    path.write_text(text, encoding="utf-8")
    print(f"privacy.html: {before} -> {len(text)} bytes")


def patch_parent() -> None:
    path = Path("guide-parent.html")
    text = path.read_text(encoding="utf-8")
    before = len(text)

    text = replace_optional(
        text,
        "PTA入会・会費・個人情報の問題を絵で直感的に整理。テンプレートPDF・FAQ付き。",
        "PTAの入会、会費、個人情報、学校関与について、確認すべき文書と手順を保護者向けに整理します。",
        "parent social description",
    )
    text = replace_optional(
        text,
        "PTA入会・会費・個人情報の問題を絵で直感的に整理。テンプレートPDF付き。",
        "PTAの入会、会費、個人情報、学校関与について、確認すべき文書と手順を保護者向けに整理します。",
        "parent meta description",
    )
    text = replace_required(text, "<div class=\"page-hero-kicker\">For Parents</div>", "<div class=\"page-hero-kicker\">保護者向け資料</div>", "parent kicker")
    text = replace_required(
        text,
        '<h1>PTAの「おかしい」に<br><em>法的根拠</em>があります。</h1><p>「入会した覚えがない」「断ると子どもが困るかも」「会費の根拠が分からない」——その気持ち、あなただけではありません。まずは“あるある”から、一緒に見ていきましょう。</p>',
        '<h1>入会・会費・個人情報を<br><em>文書で確認する</em></h1><p>PTAに入会した記録がない、会費の請求根拠が分からない、学校が保有する情報をPTAが使っている、非加入による子どもの扱いが不安という場合に、確認すべき事実と文書を順に整理します。</p>',
        "parent hero",
    )
    old_lead = '<section class="parent-lead-mag" id="parent-lead"><div class="wrap-narrow"><div class="lead-kicker">はじめに</div><h2>こんなこと、ありませんか。</h2><p>春、入学説明会で渡された分厚い封筒。気づけば「会員」になっていて、毎月、給食費と一緒に会費が引き落とされている。役員決めの日は、朝から気が重い。「断ったら、子どもが何か言われるかも」と思うと、何も言えないまま——。</p><p class="soft">それは、あなたが神経質だからでも、わがままだからでもありません。同じ場所で立ち止まり、「これって、おかしくない？」と感じてきた保護者が、全国にたくさんいます。そして、その違和感には、ちゃんと法的な裏づけがあります。</p><p class="lead-close">もし一つでも心当たりがあるなら、この先を読んでみてください。<br>あなたの「おかしい」には、ちゃんと理由があります。</p></div></section>'
    new_lead = '<section class="parent-lead-mag" id="parent-lead"><div class="wrap-narrow"><div class="lead-kicker">最初に確認すること</div><h2>学校への入学と、PTAへの加入は別の手続です</h2><p>学校への在籍は、児童生徒と公立学校との学校教育上の関係を生じさせます。しかし、学校とは別組織であるPTAとの会員関係まで自動的に発生させるものではありません。</p><p class="soft">入会申込書や電子申込記録がないまま会員と扱われている場合は、加入の申込み、PTAによる承諾、会費の請求根拠、個人情報の取得経路を分けて確認します。学校の案内、徴収金、連絡ツール、教職員の事務にPTA手続が混ざっていないかも重要です。</p><p class="lead-close">最初に確認するのは、感情や慣例ではなく、入会記録、会則、会費案内、口座振替の依頼書、個人情報の利用目的です。</p></div></section>'
    text = replace_required(text, old_lead, new_lead, "parent lead section")
    text = replace_required(text, "PTAは100%任意加入です", "学校への在籍だけでPTA会員にはなりません", "parent membership heading")
    text = replace_required(
        text,
        "社会教育法上の任意団体であり、加入・非加入はあなたの自由です。入会の意思確認がない運用は、まず確認が必要です。",
        "PTAは学校とは別組織です。本人の申込みとPTAの承諾を確認できなければ、学校への入学だけで会員関係は成立しません。",
        "parent membership explanation",
    )
    text = replace_required(text, "社会教育法 10条", "民法 521・522条", "parent law chip")
    text = replace_required(
        text,
        "PTAは任意加入であり、加入しないことを理由に子どもの扱いを分けることは許されません（憲法26条・14条）。「入らないとプレゼントを渡せないかも」という案内は、子どもの心情を通じて加入を迫るもので、消費者契約法上もPTAは「事業者」と整理され得て、不安をあおる勧誘は問題となり得ます。①任意性の明文確認、②非加入でも子どもに不利益を与えない確約、③当該一文の撤回を、書面で求めるのが有効です。",
        "保護者の加入・非加入を理由に、学校生活上の児童の扱いを変える運用は認められません。PTAが独自に購入する物品の取扱いであっても、学校内で児童を分け、子どもの心情を通じて加入を迫る案内は、任意加入を実質的に妨げる勧誘として問題になります。学校が配布、集金、児童の区分に関与している場合は教育委員会の確認対象です。①加入しなくても学校生活上の不利益を生じさせないこと、②学校関与の有無、③当該案内の撤回を文書で求めます。",
        "parent gift reply",
    )
    text = replace_required(
        text,
        "とりわけ入学前の提供は、学校からPTAへの「目的外提供」がなければ起こり得ません。",
        "入学前であっても取得経路は一つとは限らないため、まず学校、PTA、地域団体その他の取得経路を確認します。学校保有情報が使われた場合は、学校自身による目的外利用か、PTAへの提供かを分けて確認する必要があります。",
        "parent pre-enrollment data",
    )
    text = replace_required(
        text,
        "②利用停止・削除を請求する、③回答がなければ教育委員会・個人情報保護委員会へ相談する",
        "②学校保有情報については行政機関等の開示・訂正・利用停止制度を確認し、PTA保有情報についてはPTAに利用目的の説明や削除等を求める、③学校側の取扱いは教育委員会・個人情報保護委員会へ相談する",
        "parent remedies split",
    )
    text = replace_required(
        text,
        "学校徴収金にPTA会費を混入させる運用は、学校の公共性・中立性、公金経理の原則（地方財政法等）との関係で問題になり得ます。",
        "学校徴収金にPTA会費を混在させる運用は、加入契約、請求主体、口座情報の利用目的、学校徴収金の取扱基準、教職員が徴収事務を行う根拠との関係で確認が必要です。",
        "parent fee reply",
    )
    text = replace_required(
        text,
        "PTAが回答しない・改善がない場合は、学校を管轄する教育委員会に状況を伝えます。",
        "学校が名簿、徴収金、連絡ツール、教職員、施設を通じて関与している場合は、その事実と根拠を教育委員会に照会します。PTA内部の問題と学校・教育委員会の関与を分けて伝えます。",
        "parent board step",
    )
    text = replace_required(
        text,
        "学校またはPTA役員に会則の開示を求めてください。退会に関する条項を確認しておくことで、手続きがスムーズになります。",
        "PTA会長または役員に会則の提示を求め、入会・退会手続を確認します。学校が職務上取得・保有している会則がある場合は、学校または教育委員会に保有状況を確認します。",
        "parent rules request",
    )
    text = replace_required(text, "会則の開示は正当な権利です", "会員関係を主張する根拠として会則を確認", "parent rules tip")
    text = replace_required(
        text,
        "学校の事務室経由での提出も可能です。受領の確認を取っておくとより確実です。提出日や担当者名をメモしておきましょう。",
        "退会届はPTA会長またはPTAが指定する受付先へ提出します。学校による取次ぎは当然の校務ではないため、学校経由にする場合は、学校が取次ぎを受ける根拠と受領先を確認してください。提出日、提出方法、受領者を記録します。",
        "parent withdrawal submission",
    )
    text = replace_optional(
        text,
        "不当引き落としは返還請求が可能です（民法703条）",
        "返還の可否は契約成立、支払経緯、受益等の事実関係から検討します",
        "parent refund tip",
    )

    # Flatten the portal-like rows without removing any substantive text.
    style = """\n<style id=\"parent-editorial-fix\">\n.visual-grid,.steps-flow,.pdf-grid{display:block!important;max-width:900px!important;margin-left:auto!important;margin-right:auto!important}\n.visual-card{display:grid!important;grid-template-columns:190px minmax(0,1fr)!important;border:0!important;border-top:1px solid var(--line)!important;border-radius:0!important;box-shadow:none!important;margin:0!important}\n.visual-card:last-child{border-bottom:1px solid var(--line)!important}\n.visual-card:hover{transform:none!important;box-shadow:none!important}\n.vc-visual{height:auto!important;min-height:150px!important;border-radius:0!important}\n.step-block,.pdf-card{border:0!important;border-top:1px solid var(--line)!important;border-radius:0!important;box-shadow:none!important;margin:0!important;padding:22px 0!important}\n.step-block:last-child,.pdf-card:last-child{border-bottom:1px solid var(--line)!important}\n.page-hero-kicker,.lead-kicker,.section-kicker{text-transform:none!important;letter-spacing:.03em!important;border-radius:3px!important}\n@media(max-width:700px){.visual-card{grid-template-columns:1fr!important}.vc-visual{min-height:160px!important}}\n</style>\n"""
    text = replace_required(text, "</head>", style + "</head>", "parent editorial CSS")

    if "PTAは100%任意加入です" in text or "学校の事務室経由での提出も可能です" in text:
        raise RuntimeError("parent: old categorical wording remains")
    if "学校への在籍だけでPTA会員にはなりません" not in text:
        raise RuntimeError("parent: new membership explanation missing")

    path.write_text(text, encoding="utf-8")
    print(f"guide-parent.html: {before} -> {len(text)} bytes")


if __name__ == "__main__":
    patch_membership()
    patch_privacy()
    patch_parent()
    print("Core page patch completed successfully")
