from pathlib import Path


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: expected 1 occurrence, found {count}")
    return text.replace(old, new)


# submission-kit.html
submission_path = Path("submission-kit.html")
submission = submission_path.read_text(encoding="utf-8")

submission = replace_once(
    submission,
    "3　学校が保有する児童・保護者情報をPTAへ提供している場合の提供項目、同意取得方法、提供記録の有無\n4　教職員が勤務時間中に行っているPTA関連事務の内容及び校務分掌上の位置づけ\n5　学校ホームページ、配信アプリ、学校施設、学校備品をPTA内部事務に使用している場合の取扱い",
    "3　学校が保有する児童・保護者情報を、PTA会員管理、会費徴収、役員選出等のために学校自身が利用している場合の利用目的、所掌事務・業務、根拠及び利用記録\n4　学校が保有する児童・保護者情報をPTAへ提供している場合の提供項目、提供先、根拠、同意取得方法及び提供記録\n5　教職員が勤務時間中に行っているPTA関連事務の内容、校務としての位置づけ、職務命令、職専免又は兼職兼業等の根拠\n6　学校ホームページ、配信アプリ、学校施設、学校備品をPTA内部事務に使用している場合の取扱い",
    "submission inquiry",
)

submission = replace_once(
    submission,
    "PTA会費は、学校徴収金とは異なり、任意団体であるPTAの会費です。入会意思、会費額、請求主体、支払方法、退会・非加入時の取扱いを明確にするため、次の点について分離又は資料確認をお願いします。\n\n1　学校徴収金通知",
    "PTA会費は、学校徴収金とは異なり、任意団体であるPTAの会費です。入会意思、会費額、請求主体、支払方法、退会・非加入時の取扱いを明確にするため、次の点について分離又は資料確認をお願いします。\n\n文部科学省の2025年通知は、学校給食費以外の学校徴収金について、公会計化して地方公共団体が徴収・管理する方法だけでなく、保護者が業者等へ直接支払い、学校を経由しない方法も示しています。この通知はPTA会費を直接規律するものではありませんが、学校教育に必要な費用ですら学校外へ移す政策方向を示す重要な資料です。\n\n1　学校徴収金通知",
    "submission 2025 notice",
)

submission = replace_once(
    submission,
    "1　PTAへ提供又は共有している情報項目\n2　学校側の利用目的及びPTA側の利用目的\n3　本人又は保護者の同意取得方法、同意しない場合の除外・マスキング方法\n4　提供記録、管理責任者、保管期間、廃棄方法\n5　学校配信アプリ、学校メール、学校HPをPTA内部事務に使う場合の基準",
    "1　学校がPTA会員管理、会費徴収、役員選出等のために学校保有情報を自ら利用している場合の情報項目、利用目的、所掌事務・業務及び利用記録\n2　PTAへ提供又は共有している情報項目、提供先及び提供方法\n3　個人情報保護法第61条・第69条に基づく利用又は提供の根拠\n4　本人又は保護者の同意取得方法、同意しない場合の除外・マスキング方法\n5　利用・提供記録、管理責任者、保管期間、廃棄方法\n6　学校配信アプリ、学校メール、学校HPをPTA内部事務に使う場合の基準",
    "submission privacy checklist",
)

submission = replace_once(
    submission,
    "<tr><td>個人情報</td><td>名簿提供記録、同意書、利用目的通知、学校アプリ配信文。</td><td>学校保有情報とPTA会員管理・地区班・当番表の接続を確認する。</td></tr>",
    "<tr><td>個人情報</td><td>学校側の利用記録、名簿提供記録、同意書、利用目的通知、学校アプリ配信文。</td><td>学校自身による目的外利用と、学校からPTAへの提供を分け、学校保有情報とPTA会員管理・地区班・当番表の接続を確認する。</td></tr>",
    "submission evidence table",
)

submission_path.write_text(submission, encoding="utf-8")


# report.html
report_path = Path("report.html")
report = report_path.read_text(encoding="utf-8")

report = replace_once(
    report,
    '<div class="page-banner-kicker">Research Report · 総合分析レポート</div>',
    '<div class="page-banner-kicker">総合分析レポート</div>',
    "report kicker",
)

report = replace_once(
    report,
    '<span class="ax5-name">入会手続・オプトアウト</span><span class="ax5-law">民法522条／消費者契約法／憲法21条</span><span class="ax5-desc">入会申込書の有無が、任意加入、退会、会費負担の説明根拠を左右します。</span>',
    '<span class="ax5-name">入会手続・オプトイン</span><span class="ax5-law">民法521・522条／憲法21条</span><span class="ax5-desc">学校への入学や保護者の沈黙ではなく、本人の加入申込みとPTAの承諾を客観的な記録で確認します。</span>',
    "report membership axis",
)

report = replace_once(
    report,
    '<span class="ax5-name">個人情報提供</span><span class="ax5-law">個人情報保護法69条</span><span class="ax5-desc">学校が持つ保護者情報をPTA目的で使うには、目的、項目、同意、提供記録の確認が必要です。</span>',
    '<span class="ax5-name">学校保有情報の利用・提供</span><span class="ax5-law">個人情報保護法61・62・69条</span><span class="ax5-desc">学校自身によるPTA目的での利用と、学校からPTAへの提供を分け、所掌事務・業務、利用目的、例外根拠、対象項目、記録を確認します。</span>',
    "report privacy axis",
)

report = replace_once(
    report,
    '<span class="ax5-name">会費徴収・学校徴収金混在</span><span class="ax5-law">民法113条／地方財政法4条の5</span><span class="ax5-desc">PTA会費を学校徴収金と一体で扱うと、契約、代理、寄附、会計区分の説明が崩れやすくなります。</span>',
    '<span class="ax5-name">会費徴収・学校徴収金混在</span><span class="ax5-law">民法521・522条／個人情報保護法61・69条／2025年通知</span><span class="ax5-desc">加入契約と会費債務を確認したうえで、学校保有口座情報の利用、学校の事務権限・決裁、会計区分を検証します。2025年通知が学校徴収金の公会計化と学校を経由しない直接支払を示した文脈も重要です。</span>',
    "report fee axis",
)

report = replace_once(
    report,
    '<span class="ax5-name">教職員関与・職務専念義務</span><span class="ax5-law">地方公務員法35条</span><span class="ax5-desc">勤務時間内に私団体の会計、名簿、役員選出、徴収事務を担わせる運用は整理が必要です。</span>',
    '<span class="ax5-name">教職員関与・職務専念義務</span><span class="ax5-law">地方公務員法35条／職専免・兼職兼業</span><span class="ax5-desc">作業内容、校務としての位置づけ、職務命令、職専免又は兼職兼業の根拠を分けて確認します。</span>',
    "report personnel axis",
)

report = replace_once(
    report,
    '<span class="ax5-name">施設利用・公私境界</span><span class="ax5-law">学校教育法137条／施設使用許可</span><span class="ax5-desc">学校施設を使う場合も、任意団体としての適正な運営と学校教育への支障の有無を分けて確認します。</span>',
    '<span class="ax5-name">施設利用・公私境界</span><span class="ax5-law">学校教育法137条／自治体の財産管理規則</span><span class="ax5-desc">PTAに当然の使用権があるのではなく、許可権者、使用目的、場所・時間、費用又は減免、責任、取消し・停止条件を確認します。</span>',
    "report facilities axis",
)

report_path.write_text(report, encoding="utf-8")
