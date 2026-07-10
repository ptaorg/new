from pathlib import Path
import re

p = Path(__file__).resolve().parents[1] / 'fee-collection.html'
text = p.read_text(encoding='utf-8')

replacements = {
    '<body>': '<body class="fee-editorial">',
    'PTA会費の抱き合わせ徴収・無権代理・公私混在・地方財政法違反——会費徴収の法的問題を一次資料に基づき整理。': '学校徴収金とPTA会費を同じ通知・口座・引落しで扱う運用について、入会記録、請求主体、口座情報の利用目的、学校の事務権限、公私分離を整理。',
    '抱き合わせ徴収・無権代理・公私混在の三重問題を法令根拠で整理します。': '学校徴収金とPTA会費の混在を、会費債務、口座情報、学校の事務権限、公私分離から整理します。',
    '抱き合わせ徴収・無権代理・公私混在の三重問題を法令根拠で整理。返還請求の根拠も解説。': '学校徴収金とPTA会費の混在について、確認すべき文書と法的論点を整理します。',
    '<div class="issue-hero-eyebrow">💰 Issue 03 — Finance</div>': '<div class="issue-hero-eyebrow">会費徴収・学校徴収金</div>',
    '<p>給食費と同じ口座でPTA会費が引き落とされる「抱き合わせ徴収」。委任契約の不在・個別同意の欠如・公私混同の三重の法的問題を孕み、地方財政法上の割当寄付禁止にも抵触し得ます。文部科学省は学校徴収金でさえ「学校の本来業務ではない」と明示しています。</p>': '<p>PTA会費を学校徴収金と同じ通知、同じ口座、同じ引落し、同じ未納管理で扱う場合は、まずPTAへの加入と会費債務が成立しているか、学校保有の口座情報を何の根拠で使うのか、学校が私的団体の徴収事務を扱う権限と決裁があるか、会計が分離されているかを確認します。</p>',
    '<h2>抱き合わせ徴収の三重の法的問題</h2>': '<h2>学校によるPTA会費徴収で確認すべき三つの前提</h2>',
    '<h4>無権代理による徴収の無効</h4>': '<h4>会員関係と会費債務の確認</h4>',
    '<p>学校とPTAの間に正式な委任契約がない場合、学校によるPTA会費徴収は代理権の有無が問題になります。会員本人の入会・支払根拠を説明できなければ、不当利得返還の問題にもつながります。</p>': '<p>PTA会費を請求する前提は、本人による加入申込みとPTAの承諾、会則上の会費額を確認できることです。PTAから学校への徴収依頼だけでは、保護者の会費債務は生じません。</p>',
    '<span class="triple-law">民法 113条・703条</span>': '<span class="triple-law">民法 521条・522条</span>',
    '<h4>公私会計の混在と割当寄付</h4>': '<h4>学校徴収金との公私分離</h4>',
    '<p>学校徴収金とPTA会費を同じ通知・同じ引落しで扱うことは、公私会計の分離を不明確にします。任意加入団体の会費が事実上の学校支払いに見える場合、地方財政法上の割当的寄附の問題にも接続します。</p>': '<p>学校教育活動に関する費用と、PTAという別団体の会費では、請求主体、支払根拠、会計責任が異なります。同じ通知や口座で扱う場合でも、この区分を保護者と監査担当者が追跡できなければなりません。</p>',
    '<span class="triple-law">地方財政法 4条の5</span>': '<span class="triple-law">徴収主体・会計区分</span>',
    '<h4>口座情報の目的外利用</h4>': '<h4>学校保有の口座情報の利用根拠</h4>',
    '<p>学校が教育目的で取得した口座情報を、PTAという別団体の会費徴収に使用する運用は、個人情報保護法第69条の目的外利用・提供との関係で確認が必要です。</p>': '<p>学校が学校徴収金等のために取得した口座情報をPTA会費へ使う場合は、個人情報保護法第61条の所掌事務・業務と利用目的、第69条の目的外利用・提供の制限に沿って根拠を確認します。</p>',
    '<span class="triple-law">個人情報保護法 69条</span>': '<span class="triple-law">個人情報保護法 61条・69条</span>',
    '<h2>「二重委任構造」が生む責任の曖昧化</h2>': '<h2>学校徴収金とPTA会費を同じ仕組みで扱うと、責任の所在が曖昧になります</h2>',
    '<p>抱き合わせ徴収の実態では、以下のような「二重の委任構造」が形成されています。</p>': '<p>学校徴収金の徴収依頼と、PTA会費の徴収関与では、当事者、目的、根拠、資金の帰属が異なります。PTA会長から学校への依頼文書があっても、それだけで保護者の会費債務、学校の事務権限、学校保有情報の利用根拠まで整うわけではありません。</p>',
    '<p>この二重委任構造が内包する問題は三点です。第一に、会計区分（公金・準公金・私金）の混乱。第二に、PTA会費の使途に関する説明責任・監査責任の所在不明確化。第三に、退会希望者や未加入世帯が「支払いを拒否すると学校との関係が悪化する」という不安から、実質的に支払いを強制される状態が生まれることです。</p>': '<p>確認すべき点は三つです。第一に、PTAが誰を会員として会費を請求しているか。第二に、学校がどの決裁と権限に基づいて徴収・保管・未納管理をしているか。第三に、学校徴収金とPTA会費が、通知、口座、帳簿、未納者情報、監査で明確に分離されているかです。</p>',
    '<h2>公私会計の分離——学校徴収金とPTA会費は別物</h2>': '<h2>公私会計の分離——学校徴収金とPTA会費は請求主体が異なります</h2>',
    '<td class="ng">「学校の本来業務ではない」として切り離し方向</td>': '<td>文科省資料は学校徴収金を対象とするため、PTA会費を扱う根拠は別に確認</td>',
    '<p>文部科学省は、学校徴収金（給食費・教材費・修学旅行費等）でさえ「学校・教師の本来業務ではない」と位置づけ、公会計化・自治体管理への移行を強力に推進しています。この立場からすれば、私的団体であるPTAの会費を学校が扱い続けることは、さらに問題が大きいと言わざるを得ません。</p>': '<p>文部科学省の2019年ガイドラインは学校給食費の公会計化と地方公共団体による徴収・管理を扱い、2025年通知は学校給食費以外の学校徴収金についても、公会計化、地方公共団体による徴収、学校を経由しない直接支払等を検討するよう求めています。いずれもPTA会費の徴収を直接規律する資料ではありませんが、学校・教師の負担軽減と徴収主体の明確化を考える参考になります。</p>',
    '<p>さらに2025年4月の通知「学校徴収金の公会計化等の取組の一層の推進について」では、各自治体に対し学校徴収金の公会計化を一層促進するよう求めています。このような流れの中で、学校教育活動に直接必要な費用でさえ学校から切り離す方向で整備が進んでいるにもかかわらず、私的団体であるPTAの会費を学校が恒常的に扱い続けることは正当化が困難です。</p>': '<p>したがって、これらの資料から直ちに「学校によるPTA会費徴収は違法」と結論づけるのではなく、学校徴収金についてさえ徴収主体と業務負担を見直していることを踏まえ、PTA会費を学校が扱う固有の根拠、決裁、情報利用、会計区分を別に説明できるかを確認します。</p>',
    '<p>文部科学省通知の精神に立ち返れば、目指すべきは「PTAが自ら会費を集める完全分離（独自徴収）」です。</p>': '<p>最も構造が明確なのは、PTAが加入者本人から必要な情報を取得し、自ら会費を請求・徴収する完全分離です。学校が関与する例外的な運用を残す場合は、学校側とPTA側の根拠を別々に文書化する必要があります。</p>',
    '<div class="trans-item"><span class="trans-check">✓</span>個人情報保護法・民法・地財法の問題がすべて解消</div>': '<div class="trans-item"><span class="trans-check">✓</span>学校保有口座情報の流用、学校未納管理、公私混在の問題を避けやすい</div>',
    '<div class="trans-item"><span class="trans-check">△</span>入会届に「代理徴収への同意」欄を設け個別同意を取得</div>': '<div class="trans-item"><span class="trans-check">△</span>本人がPTAに対して学校関与の徴収方法を選択した記録と、学校側の情報利用根拠を分けて確認</div>',
    '<div class="trans-item"><span class="trans-check">△</span>PTA会長と校長の書面委任契約を締結</div>': '<div class="trans-item"><span class="trans-check">△</span>PTAからの依頼文書に加え、学校側の事務権限、決裁、責任範囲を文書化</div>',
}
for old, new in replacements.items():
    if old not in text:
        raise SystemExit(f'marker not found: {old[:110]}')
    text = text.replace(old, new, 1)

# Replace the legally overbroad unauthorized-agency section with a document-based analysis.
pattern = re.compile(r'\s*<!-- ===== 3\. 無権代理 ===== -->.*?\s*<!-- ===== 4\. 公私会計 ===== -->', re.S)
replacement = r'''

      <!-- ===== 3. 徴収関与の根拠 ===== -->
      <section id="no-agency" class="issue-section">
        <h2>PTAから学校への依頼だけでは、会費徴収の前提は整いません</h2>
        <p>会費徴収の前提は、本人とPTAとの間に会員関係と会費債務が成立していることです。PTA会長が学校へ徴収を依頼しても、その文書だけで未加入者を会員にしたり、保護者に会費債務を負わせたりすることはできません。</p>
        <div class="law-quote-block">
          <div class="lq-label">確認の順序</div>
          <p>加入申込みと承諾、会則上の会費額、徴収対象者を先に確認し、その後に学校が徴収へ関与する根拠、学校保有情報の利用目的、決裁、会計区分を確認します。</p>
        </div>
        <h3 id="civil113">民法113条を一律の中心根拠にはしない</h3>
        <p>民法113条は、代理権のない者が他人の代理人として契約をした場合の効果帰属を定める規定です。既に成立した会費債務の収納補助や口座振替事務が、常に同条の「契約」に当たるとは限りません。学校の関与を評価するときは、誰が誰の名で何を行ったのか、契約締結、請求、収納、保管、送金、未納管理を分けて、具体的な文書から判断します。</p>
        <h3 id="requirements">学校が徴収に関与する場合の確認事項</h3>
        <div class="req-steps">
          <div class="req-step"><div class="req-step-num">1</div><div class="req-step-body"><strong>加入と会費債務</strong><p>本人の加入申込み、PTAの承諾、会則上の会費額、徴収対象となる会員を確認します。</p><span class="req-law">民法521条・522条</span></div></div>
          <div class="req-step"><div class="req-step-num">2</div><div class="req-step-body"><strong>学校保有情報の利用根拠</strong><p>学校が学校徴収金等のために取得した口座情報を使う場合は、所掌事務・業務、利用目的、目的外利用・提供の根拠を確認します。</p><span class="req-law">個人情報保護法61条・69条</span></div></div>
          <div class="req-step"><div class="req-step-num">3</div><div class="req-step-body"><strong>学校側の事務権限と決裁</strong><p>PTAからの依頼書だけでなく、学校または教育委員会がその事務を扱う根拠、決裁、責任者、対象業務を確認します。</p><span class="req-law">文書管理・服務・会計規程</span></div></div>
          <div class="req-step"><div class="req-step-num">4</div><div class="req-step-body"><strong>会計と未納管理の分離</strong><p>通知、引落しデータ、帳簿、通帳、未納者情報、監査を学校徴収金から区別し、PTA資金の帰属と保管責任を追跡できるようにします。</p><span class="req-law">会計区分・保管責任</span></div></div>
        </div>
      </section>

      <!-- ===== 4. 公私会計 ===== -->'''
text, count = pattern.subn(replacement, text, count=1)
if count != 1:
    raise SystemExit(f'unauthorized-agency section replacement count={count}')

# Replace the broad Local Finance Act application with a scoped explanation.
pattern = re.compile(r'<section id="financial-law" class="issue-section">.*?</section>\s*\n\s*<!-- ===== 7\. 移行方法 ===== -->', re.S)
replacement = r'''<section id="financial-law" class="issue-section">
        <h2>地方財政法4条の5は、PTA会費に当然適用される条文ではありません</h2>
        <div class="law-quote-block">
          <div class="lq-label">地方財政法4条の5の対象</div>
          <p>地方公共団体またはその機関が、住民に寄附金を割り当てて強制的に徴収することを禁止する規定です。</p>
        </div>
        <p>PTA会費は私的団体の会費であるため、学校が徴収へ関与したという事情だけで、直ちに同条の割当寄附に当たるとはいえません。通常の会費徴収で中心となるのは、入会契約、会費債務、学校保有情報の利用、学校の事務権限、公私会計の分離です。</p>
        <p>一方、学校または教育委員会が保護者へ一定額を割り当て、学校経費の肩代わりを目的として事実上強制している場合は、徴収主体、資金の帰属、使途、行政の関与を確認した上で、同条との関係を別途検討します。</p>
      </section>

      <!-- ===== 7. 移行方法 ===== -->'''
text, count = pattern.subn(replacement, text, count=1)
if count != 1:
    raise SystemExit(f'financial-law section replacement count={count}')

# Remove an unofficial negotiation quotation from the central argument.
pattern = re.compile(r'<div class="mext-quote">\s*<div class="mext-source">📋 文部科学省 交渉記録（自治労、2013年）</div>.*?</div>', re.S)
replacement = '<p>勤務時間中のPTA会計事務については、この交渉記録だけで結論づけず、校務としての位置付け、職務命令、職務専念義務免除、兼職・兼業、具体的な従事時間を確認します。</p>'
text, count = pattern.subn(replacement, text, count=1)
if count != 1:
    raise SystemExit(f'MEXT negotiation replacement count={count}')

style = r'''
<style id="fee-editorial-accuracy-20260710">
body.fee-editorial .issue-hero-toc,
body.fee-editorial .issue-sidebar,
body.fee-editorial #slide-flow,
body.fee-editorial #overview > .fee-fig,
body.fee-editorial #structure > .fee-fig,
body.fee-editorial #structure .double-commission,
body.fee-editorial #public-private > .fee-fig{
  display:none!important;
}
body.fee-editorial .issue-hero-inner{
  width:min(calc(100% - 40px),920px)!important;
  grid-template-columns:1fr!important;
}
body.fee-editorial .issue-hero-eyebrow,
body.fee-editorial .section-eyebrow{
  text-transform:none!important;
  letter-spacing:.03em!important;
  border-radius:3px!important;
}
body.fee-editorial .issue-content{
  width:min(calc(100% - 40px),920px)!important;
  display:block!important;
  padding:68px 0 92px!important;
}
body.fee-editorial .issue-section,
body.fee-editorial .editorial-panel,
body.fee-editorial .editorial-brief{
  margin:0!important;
  padding:42px 0 48px!important;
  background:#fff!important;
  border:0!important;
  border-top:1px solid #cfd8e2!important;
  border-radius:0!important;
  box-shadow:none!important;
}
body.fee-editorial .editorial-brief-grid,
body.fee-editorial .triple-problem,
body.fee-editorial .transition-options{
  display:block!important;
}
body.fee-editorial .editorial-brief-point,
body.fee-editorial .triple-card,
body.fee-editorial .trans-card,
body.fee-editorial .req-step{
  margin:0!important;
  padding:20px 0!important;
  background:#fff!important;
  border:0!important;
  border-top:1px solid #dbe4ee!important;
  border-radius:0!important;
  box-shadow:none!important;
  transform:none!important;
}
body.fee-editorial .editorial-brief-point:last-child,
body.fee-editorial .triple-card:last-child,
body.fee-editorial .trans-card:last-child,
body.fee-editorial .req-step:last-child{
  border-bottom:1px solid #dbe4ee!important;
}
body.fee-editorial .triple-card::before{
  display:none!important;
}
body.fee-editorial .triple-law,
body.fee-editorial .req-law,
body.fee-editorial .trans-label{
  border-radius:0!important;
  background:transparent!important;
  padding:0!important;
}
body.fee-editorial .related-link-grid{
  display:block!important;
  border-top:1px solid #dbe4ee!important;
}
body.fee-editorial .related-link-card{
  display:grid!important;
  grid-template-columns:220px minmax(0,1fr)!important;
  gap:18px!important;
  margin:0!important;
  padding:18px 0!important;
  border:0!important;
  border-bottom:1px solid #dbe4ee!important;
  border-radius:0!important;
  box-shadow:none!important;
  transform:none!important;
}
body.fee-editorial .related-link-card .rlc-label{
  display:none!important;
}
body.fee-editorial main a:hover{
  transform:none!important;
  box-shadow:none!important;
}
@media(max-width:700px){
  body.fee-editorial .issue-hero-inner,
  body.fee-editorial .issue-content{
    width:min(calc(100% - 30px),920px)!important;
  }
  body.fee-editorial .related-link-card{
    grid-template-columns:1fr!important;
    gap:5px!important;
  }
}
</style>
'''
if 'fee-editorial-accuracy-20260710' not in text:
    text = text.replace('</head>', style + '</head>', 1)

p.write_text(text, encoding='utf-8')
