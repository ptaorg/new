const fs = require('fs');
const path = require('path');

const ROOT = path.join(__dirname, '..');
const DRY_RUN = process.argv.includes('--dry-run');

const TARGET_FILES = [
  'case-reading.html',
  'claim-evidence-ledger.html',
  'evidence-checklist.html',
  'journal/consumer-contract.html',
  'journal/nonmember-info.html',
  'journal/optout-invalidity.html',
  'journal/school-fee-separation.html',
  'journal/third-party-consent.html',
  'journal/work-style-reform.html',
  'journal/yokohama-notice-1965.html',
  'key-materials.html',
  'law-map.html',
  'research-index.html',
  'research.html',
  'submission-kit.html',
  'timeline-issues.html',
];

const desktopNav = `<nav aria-label="主要ナビゲーション" class="desktop-nav">
<a class="nav-link" href="/index.html">トップ</a>
<div class="nav-item has-dropdown">
<a class="nav-link" href="#">はじめての方</a>
<div class="mega-menu">
<div class="mega-col"><h4>立場別の入口</h4><ul><li><a href="/guide-parent.html">保護者の方へ</a></li><li><a href="/guide-pta.html">PTA役員の方へ</a></li><li><a href="/guide-board.html">教育委員会・学校へ</a></li></ul></div>
<div class="mega-col"><h4>最初に見る資料</h4><ul><li><a href="/proper-management.html">PTA適正化とは</a></li><li><a href="/audit/index.html">運営チェック</a></li></ul></div>
</div>
</div>
<div class="nav-item has-dropdown">
<a class="nav-link" href="#">主要論点</a>
<div class="mega-menu">
<div class="mega-col"><h4>手続・情報・会費</h4><ul><li><a href="/membership.html">入会手続</a></li><li><a href="/privacy.html">個人情報</a></li><li><a href="/fee-collection.html">会費徴収</a></li></ul></div>
<div class="mega-col"><h4>学校との境界</h4><ul><li><a href="/personnel.html">教職員関与</a></li><li><a href="/facilities.html">施設利用</a></li><li><a href="/law-map.html">法制度マップ</a></li></ul></div>
</div>
</div>
<div class="nav-item has-dropdown">
<a class="nav-link" href="#">資料・回答</a>
<div class="mega-menu">
<div class="mega-col"><h4>一次資料</h4><ul><li><a href="/board-responses.html">教育委員会の回答</a></li><li><a href="/national-archive.html">全国資料館</a></li><li><a href="/administrative-materials.html">行政通知・公式PDF</a></li></ul></div>
<div class="mega-col"><h4>整理・文書</h4><ul><li><a href="/documents.html">資料入口・索引</a></li><li><a href="/journal.html">論考・調査報告</a></li><li><a href="/guideline.html">提出用ひな形</a></li></ul></div>
</div>
</div>
<a class="nav-link contact-nav-link" href="/contact.html">お問い合わせ</a>
<a class="btn-gold" href="/support.html">応援</a>
</nav>`;

const mobileOverlay = `<div class="mobile-overlay" id="mobileOverlay">
<a class="mobile-link" href="/index.html"><span>Home</span>トップページ</a>
<a class="mobile-link" href="/guide-parent.html"><span>Start</span>保護者の方へ</a>
<a class="mobile-link" href="/guide-pta.html"><span>Start</span>PTA役員の方へ</a>
<a class="mobile-link" href="/guide-board.html"><span>Start</span>教育委員会・学校へ</a>
<a class="mobile-link" href="/membership.html"><span>Issue</span>入会・会費・個人情報</a>
<a class="mobile-link" href="/board-responses.html"><span>Data</span>教育委員会の回答</a>
<a class="mobile-link" href="/documents.html"><span>Docs</span>資料入口・索引</a>
<a class="mobile-link" href="/contact.html"><span>Contact</span>お問い合わせ</a>
<a class="mobile-link support-mobile-link" href="/support.html"><span>Support</span>応援・寄付</a>
<div class="close-overlay" id="closeOverlay">CLOSE ×</div>
</div>`;

const navPattern = /<nav\b(?=[^>]*class=["'][^"']*\bdesktop-nav\b[^"']*["'])[^>]*>[\s\S]*?<\/nav>/;
const headerMobileMainPattern = /(<\/header>)\s*<div\b(?=[^>]*id=["']mobileOverlay["'])[^>]*>[\s\S]*?<\/div>\s*(<main\b)/;

const changedFiles = [];
const skippedFiles = [];

for (const rel of TARGET_FILES) {
  const full = path.join(ROOT, rel);
  if (!fs.existsSync(full)) {
    skippedFiles.push(`${rel} (not found)`);
    continue;
  }

  const text = fs.readFileSync(full, 'utf8');
  let next = text;

  const hasNav = navPattern.test(next);
  const hasMobileBridge = headerMobileMainPattern.test(next);

  if (hasNav) next = next.replace(navPattern, desktopNav);
  if (hasMobileBridge) next = next.replace(headerMobileMainPattern, `$1${mobileOverlay}$2`);

  if (next !== text) {
    changedFiles.push(rel);
    if (!DRY_RUN) fs.writeFileSync(full, next, 'utf8');
  } else {
    skippedFiles.push(rel);
  }
}

console.log(`${DRY_RUN ? 'Would update' : 'Updated'} ${changedFiles.length} legacy HTML files.`);
for (const file of changedFiles) console.log(`- ${file}`);

if (skippedFiles.length) {
  console.log(`\nSkipped ${skippedFiles.length} legacy files:`);
  for (const file of skippedFiles) console.log(`- ${file}`);
}
