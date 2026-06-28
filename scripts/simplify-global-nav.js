const fs = require('fs');
const path = require('path');

const ROOT = path.join(__dirname, '..');
const DRY_RUN = process.argv.includes('--dry-run');
const SKIP_DIRS = new Set(['.git', '.claude', 'assets', 'css', 'data', 'js', 'scripts', 'tools', 'node_modules', 'ホーム']);

const desktopNav = `<nav aria-label="主要ナビゲーション" class="desktop-nav">
<a class="nav-link" href="/index.html">トップ</a>
<div class="nav-item has-dropdown">
<a class="nav-link" href="#">はじめての方</a>
<div class="mega-menu">
<div class="mega-col">
<h4>立場別の入口</h4>
<ul>
<li><a href="/guide-parent.html">保護者の方へ</a></li>
<li><a href="/guide-pta.html">PTA役員の方へ</a></li>
<li><a href="/guide-board.html">教育委員会・学校へ</a></li>
</ul>
</div>
<div class="mega-col">
<h4>最初に見る資料</h4>
<ul>
<li><a href="/proper-management.html">PTA適正化とは</a></li>
<li><a href="/audit/index.html">運営チェック</a></li>
</ul>
</div>
</div>
</div>
<div class="nav-item has-dropdown">
<a class="nav-link" href="#">主要論点</a>
<div class="mega-menu">
<div class="mega-col">
<h4>手続・情報・会費</h4>
<ul>
<li><a href="/membership.html">入会手続</a></li>
<li><a href="/privacy.html">個人情報</a></li>
<li><a href="/fee-collection.html">会費徴収</a></li>
</ul>
</div>
<div class="mega-col">
<h4>学校との境界</h4>
<ul>
<li><a href="/personnel.html">教職員関与</a></li>
<li><a href="/facilities.html">施設利用</a></li>
<li><a href="/law-map.html">法制度マップ</a></li>
</ul>
</div>
</div>
</div>
<div class="nav-item has-dropdown">
<a class="nav-link" href="#">資料・回答</a>
<div class="mega-menu">
<div class="mega-col">
<h4>一次資料</h4>
<ul>
<li><a href="/board-responses.html">教育委員会の回答</a></li>
<li><a href="/national-archive.html">全国資料館</a></li>
<li><a href="/administrative-materials.html">行政通知・公式PDF</a></li>
</ul>
</div>
<div class="mega-col">
<h4>整理・文書</h4>
<ul>
<li><a href="/documents.html">資料入口・索引</a></li>
<li><a href="/journal.html">論考・調査報告</a></li>
<li><a href="/guideline.html">提出用ひな形</a></li>
</ul>
</div>
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

const navPattern = /<nav aria-label="主要ナビゲーション" class="desktop-nav">[\s\S]*?<\/nav>/;
const mobilePattern = /<div class="mobile-overlay" id="mobileOverlay">[\s\S]*?<div class="close-overlay" id="closeOverlay">CLOSE ×<\/div>\s*<\/div>/;

const changedFiles = [];
const skippedFiles = [];

function walk(dir) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (SKIP_DIRS.has(entry.name)) continue;
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      walk(full);
      continue;
    }
    if (!entry.isFile() || !entry.name.endsWith('.html')) continue;

    const text = fs.readFileSync(full, 'utf8');
    if (!text.includes('class="desktop-nav"') && !text.includes('id="mobileOverlay"')) continue;

    let next = text;
    const hasNav = navPattern.test(next);
    const hasMobile = mobilePattern.test(next);

    if (hasNav) next = next.replace(navPattern, desktopNav);
    if (hasMobile) next = next.replace(mobilePattern, mobileOverlay);

    if (next !== text) {
      changedFiles.push(path.relative(ROOT, full));
      if (!DRY_RUN) fs.writeFileSync(full, next, 'utf8');
    } else {
      skippedFiles.push(path.relative(ROOT, full));
    }
  }
}

walk(ROOT);

console.log(`${DRY_RUN ? 'Would update' : 'Updated'} ${changedFiles.length} HTML files.`);
for (const file of changedFiles) console.log(`- ${file}`);

if (skippedFiles.length) {
  console.log(`\nSkipped ${skippedFiles.length} files that looked like nav files but did not match safely:`);
  for (const file of skippedFiles) console.log(`- ${file}`);
}
