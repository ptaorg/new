from pathlib import Path
import re

p = Path('js/site.js')
s = p.read_text(encoding='utf-8')

s = s.replace('/* site.js v91 — static body preservation', '/* site.js v90 — static body preservation', 1)

# Remove the starter-kit entries that were injected ahead of the real site index.
for line in [
    "    ['PTA適正運営スターターキット v1.0', '/starter-kit/', '任意加入、個人情報、会計分離、学校との公私分離を実務資料一式で確認'],\n",
    "    ['スターターキット ダウンロード', '/starter-kit/downloads.html', 'PDF印刷版、総合ZIP、Google実装版の配布ページ'],\n",
    "      merged.unshift(['PTA適正運営スターターキット v1.0', '/starter-kit/', '任意加入、個人情報、会計分離、学校との公私分離を実務資料一式で確認']);\n",
    "      merged.unshift(['スターターキット ダウンロード', '/starter-kit/downloads.html', 'PDF印刷版、総合ZIP、Google実装版の配布ページ']);\n",
]:
    if line not in s:
        raise SystemExit(f'missing starter-kit line: {line[:45]}')
    s = s.replace(line, '', 1)

replacements = {
    "    ['入会手続とオプトアウト', '/membership.html', '入会申込書・同意・みなし加入'],": "    ['PTA入会の成立と申込記録', '/membership.html', '申込み・承諾・申込記録・みなし加入の確認'],",
    "    ['個人情報提供の問題', '/privacy.html', '学校名簿のPTA提供と個人情報保護法'],": "    ['学校保有情報のPTA目的利用・提供', '/privacy.html', '学校自身の利用、PTAへの提供、PTAによる直接取得'],",
    "    ['運営チェックアプリ', '/audit/index.html', '自校・自PTAのセルフチェック'],": "    ['運営チェック', '/audit/index.html', '資料と運用の確認優先度を整理するチェック表'],",
    "    ['PTA運営の現場実例', '/compliance.html', 'みなし加入・代行徴収・名簿提供の実例'],": "    ['学校とPTAの運用実例を点検する', '/reality.html', '入会案内、会費徴収、学校保有情報、教職員関与の再現資料'],",
}
for old, new in replacements.items():
    if old not in s:
        raise SystemExit(f'missing index entry: {old}')
    s = s.replace(old, new, 1)

# Remove the unverified incident shortcut from the fallback index.
incident = "    ['静岡市個人情報事案', '/shizuoka-incident.html', '個人情報漏えい事案の整理'],\n"
if incident in s:
    s = s.replace(incident, '', 1)

# Remove the automatic top-page promotional bridge completely.
pattern = r'\n  function insertStarterKitBridge\(\) \{.*?\n  \}\n\n  function stabilizeMobileNavigation'
s, count = re.subn(pattern, '\n\n  function stabilizeMobileNavigation', s, count=1, flags=re.S)
if count != 1:
    raise SystemExit(f'starter-kit bridge function: expected 1, found {count}')

if '    insertStarterKitBridge();\n' not in s:
    raise SystemExit('starter-kit bridge invocation missing')
s = s.replace('    insertStarterKitBridge();\n', '', 1)

# Replace card-like mobile links with a simple vertical navigation list.
old_css = "      '.mobile-menu-group{width:min(100%,430px);display:flex;flex-direction:column;gap:8px;margin:0 0 8px!important}' +\n      '.mobile-menu-label{color:rgba(255,255,255,.55);font-size:.72rem;font-weight:900;letter-spacing:.1em;text-transform:uppercase;margin:5px 4px}' +\n      '.mobile-link{width:100%!important;background:rgba(255,255,255,.97)!important;border-radius:14px!important;padding:14px 18px!important;text-decoration:none!important;color:var(--navy,#1e3a5f)!important;font-weight:800!important;box-shadow:0 6px 20px rgba(0,0,0,.14)!important}' +\n      '.mobile-close-btn{width:min(100%,430px);min-height:44px;border:1px solid rgba(255,255,255,.35);border-radius:999px;background:rgba(255,255,255,.1);color:#fff;font-weight:900;cursor:pointer}'"
new_css = "      '.mobile-menu-group{width:min(100%,430px);display:flex;flex-direction:column;gap:0;margin:0 0 16px!important;border-top:1px solid rgba(255,255,255,.2)}' +\n      '.mobile-menu-label{color:rgba(255,255,255,.58);font-size:.72rem;font-weight:900;letter-spacing:.08em;text-transform:none;margin:14px 0 6px}' +\n      '.mobile-link{width:100%!important;background:transparent!important;border:0!important;border-bottom:1px solid rgba(255,255,255,.18)!important;border-radius:0!important;padding:13px 2px!important;text-decoration:none!important;color:#fff!important;font-weight:800!important;box-shadow:none!important}' +\n      '.mobile-close-btn{width:min(100%,430px);min-height:44px;border:1px solid rgba(255,255,255,.35);border-radius:0;background:transparent;color:#fff;font-weight:900;cursor:pointer}'"
if old_css not in s:
    raise SystemExit('mobile card css block missing')
s = s.replace(old_css, new_css, 1)

# Normalize every known historic support URL.
old = "      if (href === '/donate/' || href === 'donate/' || href === 'https://ptaorg.com/donate/') a.setAttribute('href', '/support.html');"
new = "      if (href === '/donate/' || href === 'donate/' || href === 'https://ptaorg.com/donate/' || href === 'https://ptaorg.github.io/donate/' || href === 'https://ptaorg.github.io/donate') a.setAttribute('href', '/support.html');"
if old not in s:
    raise SystemExit('support normalization line missing')
s = s.replace(old, new, 1)

p.write_text(s, encoding='utf-8')
