from pathlib import Path

p = Path(__file__).resolve().parents[1] / 'personnel.html'
text = p.read_text(encoding='utf-8')

replacements = {
    '勤務時間中の従事であれば、地方公務員法35条の職務専念義務との関係で確認が必要です。「ちょっとした手伝い」であっても、恒常的・組織的に行われれば問題状況になります。担任本人が認識しないうちに、学校として説明しにくい運用に置かれている可能性があります。': '勤務時間中に恒常的・組織的に行われている場合は、その作業が校務として特定されているか、職務命令または職専免等の根拠があるかを確認します。作業量の大小だけでなく、誰の事務を、どの身分と時間で行っているかが重要です。',
    '服務免除の制度は存在しますが、条例・規則の根拠と個別の手続きが必要です。「校長の口頭承認」だけでは不十分で、PTAへの日常的な関与を包括的に免除することはできません。また服務免除が認められたとしても、公費（給与）でPTAを支援することは、行政の中立性・社会教育法上の問題として残ります。': '職務専念義務免除は、各自治体の条例・規則に基づいて行われます。PTA関係で適用する場合は、対象者、用務、日時、申請・承認記録、承認権者を確認します。校長の口頭了解だけで足りるか、包括的な取扱いが可能かは自治体の規定によります。職専免の有無とは別に、学校施設・情報・会計等の便宜供与の根拠も確認します。',
    '来賓として出席すること自体は渉外業務の範囲と考えられます。ただし「議決権を持つ役員として出席する」「予算・人事を実質的に決める」等の関与は、PTAの自律性を損ない社会教育法上の問題が生じます。「校長が事実上PTAを運営している」状態は避けてください。': '総会への出席は、学校代表としての説明・連絡調整なのか、PTA役員としての議決参加なのかを分けます。役員として議決権を行使し、予算・人事・会員管理を担う場合は、兼職等の手続、勤務時間の取扱い、学校の公的権限とPTAの自主的意思決定の分離を確認します。',
    '勤務時間中の補助は職務専念義務違反の疑いがあります。PTAが独自に会計を担える体制（会計担当役員＋クラウド会計ツール等）を整備し、事務職員への依頼を段階的に終了することが適正化の手順です。移行期間が必要な場合は、校長に計画を共有しながら進めてください。': 'まず、会費集計が校務として特定されているか、職務命令、職専免、学校会計規程等の根拠があるかを確認します。根拠が明確でない場合は、PTAが自ら会計と徴収を担う体制を整え、学校事務職員への依存を段階的に終了する計画を共有します。',
}

for old, new in replacements.items():
    if old not in text:
        raise SystemExit(f'marker not found: {old[:120]}')
    text = text.replace(old, new, 1)

style = '''
<style id="personnel-faq-editorial-20260710">
body.personnel-editorial .faq-list{
  gap:0!important;
  border-top:1px solid #cfd8e2!important;
}
body.personnel-editorial .faq-item{
  border-left:0!important;
  border-right:0!important;
  border-top:0!important;
  border-bottom:1px solid #cfd8e2!important;
  border-radius:0!important;
  box-shadow:none!important;
}
body.personnel-editorial .faq-q{
  padding:20px 0!important;
}
body.personnel-editorial .faq-a{
  padding-left:0!important;
  padding-right:0!important;
}
</style>
'''
if 'personnel-faq-editorial-20260710' not in text:
    text = text.replace('</head>', style + '</head>', 1)

p.write_text(text, encoding='utf-8')
