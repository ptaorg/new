from pathlib import Path

path = Path('administrative-materials.html')
text = path.read_text(encoding='utf-8')

if text.count('<body>') != 1:
    raise SystemExit('body marker not found')
text = text.replace('<body>', '<body class="admin-materials-editorial">', 1)

if text.count('<p class="admin-materials-kicker">Administrative Materials</p>') != 1:
    raise SystemExit('kicker marker not found')
text = text.replace('<p class="admin-materials-kicker">Administrative Materials</p>', '<p class="admin-materials-kicker">行政通知・公式資料</p>', 1)

old_row = '<tr><td>A</td><td><a href="https://www.mext.go.jp/content/20250616-mxt_zaimu-100002245_2.pdf" rel="noopener" target="_blank">学校徴収金の公会計化等の取組の一層の推進について</a><small>文部科学省資料PDF</small></td><td>学校徴収金の公会計化、学校・教師の負担軽減、学校以外が担うべき業務。</td><td>公式PDF。PTA会費を学校徴収金から分ける比較資料として優先。</td></tr>'
new_row = '<tr><td>A</td><td><a href="https://www.mext.go.jp/content/20250616-mxt_zaimu-100002245_2.pdf" rel="noopener" target="_blank">学校徴収金の公会計化等の取組の一層の推進について</a><small>文部科学省資料PDF</small></td><td>学校給食費以外の学校徴収金について、公会計化して地方公共団体が徴収・管理する方法に加え、保護者が業者等へ直接支払い、学校を経由しない方法を示す。学校・教師の徴収管理負担を学校の外へ移す政策資料。</td><td>公式PDF。PTA会費を直接規律する通知ではないが、学校教育に必要な費用ですら学校外へ移す政策方向との比較資料として優先。</td></tr>'
if text.count(old_row) != 1:
    raise SystemExit(f'mext row count: {text.count(old_row)}')
text = text.replace(old_row, new_row, 1)

old_fee = '<tr><td>A</td><td><a href="https://www.mext.go.jp/content/20250616-mxt_zaimu-100002245_2.pdf" rel="noopener" target="_blank">学校徴収金の公会計化等の取組の一層の推進について</a><small>文部科学省資料PDF</small></td><td>学校徴収金とPTA会費を混同しないための前提資料。</td><td>公式PDF。会費徴収分離申入書の根拠資料として優先。</td></tr>'
new_fee = '<tr><td>A</td><td><a href="https://www.mext.go.jp/content/20250616-mxt_zaimu-100002245_2.pdf" rel="noopener" target="_blank">学校徴収金の公会計化等の取組の一層の推進について</a><small>文部科学省資料PDF</small></td><td>学校給食費以外の学校徴収金について、公会計化と、学校を経由しない直接支払を示した資料。学校徴収金とPTA会費を混同しないための政策的前提として使う。</td><td>公式PDF。PTA会費への直接適用ではなく、会費徴収分離申入書の比較・説明資料として位置づける。</td></tr>'
if text.count(old_fee) != 1:
    raise SystemExit(f'fee row count: {text.count(old_fee)}')
text = text.replace(old_fee, new_fee, 1)

style = '''
<style id="admin-materials-editorial-20260710">
.admin-materials-editorial .admin-materials-kicker{
  text-transform:none!important;
  letter-spacing:.04em!important;
}
.admin-materials-editorial .yokohama-brief{
  display:block!important;
}
.admin-materials-editorial .yokohama-brief-card{
  margin:0!important;
  padding:22px 0!important;
  background:transparent!important;
  border:0!important;
  border-top:1px solid #dbe3ee!important;
  border-radius:0!important;
  box-shadow:none!important;
}
.admin-materials-editorial .yokohama-brief-card:last-child{
  border-bottom:1px solid #dbe3ee!important;
}
.admin-materials-editorial .materials-pdf-links{
  display:block!important;
}
.admin-materials-editorial .materials-pdf-links a{
  display:inline!important;
  margin-right:1em!important;
  padding:0!important;
  background:transparent!important;
  border:0!important;
  border-radius:0!important;
  color:#0f4c81!important;
  text-decoration:underline!important;
}
.admin-materials-editorial main a:hover{
  transform:none!important;
  box-shadow:none!important;
}
</style>
'''
if 'admin-materials-editorial-20260710' in text:
    raise SystemExit('editorial style already present')
text = text.replace('</head>', style + '</head>', 1)

path.write_text(text, encoding='utf-8')
