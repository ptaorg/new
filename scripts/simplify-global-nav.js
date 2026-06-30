const fs = require('fs');
const path = require('path');

const ROOT = path.join(__dirname, '..');
const DRY_RUN = process.argv.includes('--dry-run');
const SKIP_DIRS = new Set(['.git', '.claude', 'assets', 'css', 'data', 'js', 'scripts', 'tools', 'node_modules', 'ホーム']);

const desktopNav = `<nav aria-label="主要ナビゲーション" class="desktop-nav">
<a class="nav-link" href="/index.html">トップ</a>
<div class="nav-item has-dropdown">
<a class="nav-link" href="/index.html#audience-gateway">立場別</a>
<div class="mega-menu">
<div class="mega-col">
<h4>あなたの立場から</h4>
<ul>
<li><a href="/guide-parent.html">保護者の方へ</a></li>
<li><a href="/guide-pta.html">PTA役員の方へ</a></li>
<li><a href="/guide-board.html">教育委員会・学校へ</a></li>
<li><a href="/guide-research.html">研究者・記者の方へ</a></li>
</ul>
</div>
<div class="mega-col">
<h4>改善後の姿</h4>
<ul>
<li><a href="/proper-management.html">適正なPTA運営モデル</a></li>
<li><a href="/audit/index.html">現在の運営を点検</a></li>
</ul>
</div>
</div>
</div>
<div class="nav-item has-dropdown">
<a class="nav-link" href="/membership.html">問題別</a>
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
<a class="nav-link" href="/research-index.html">根拠資料</a>
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
<h4>調査・整理</h4>
<ul>
<li><a href="/cases.html">判例整理</a></li>
<li><a href="/journal.html">論考・調査報告</a></li>
<li><a href="/report.html">総合分析レポート</a></li>
</ul>
</div>
</div>
</div>
<div class="nav-item has-dropdown">
<a class="nav-link" href="/documents.html">チェック・文例</a>
<div class="mega-menu">
<div class="mega-col">
<h4>点検・改善</h4>
<ul>
<li><a href="/audit/index.html">運営チェック</a></li>
<li><a href="/guideline.html">適正化ガイドライン</a></li>
<li><a href="/submission-kit.html">提出文書キット</a></li>
</ul>
</div>
<div class="mega-col">
<h4>資料を使う</h4>
<ul>
<li><a href="/documents.html">資料入口・文例索引</a></li>
<li><a href="/contact.html">問い合わせ・情報提供</a></li>
</ul>
</div>
</div>
</div>
<a class="btn-gold" href="/support.html">応援</a>
</nav>`;

const mobileOverlay = `<div class="mobile-overlay" id="mobileOverlay">
<div class="mobile-menu-group"><div class="mobile-menu-label">主要入口</div>
<a class="mobile-link" href="/index.html">トップ</a>
<a class="mobile-link" href="/guide-parent.html">保護者の方へ</a>
<a class="mobile-link" href="/guide-pta.html">PTA役員の方へ</a>
<a class="mobile-link" href="/guide-board.html">教育委員会・学校へ</a>
<a class="mobile-link" href="/guide-research.html">研究者・記者の方へ</a></div>
<div class="mobile-menu-group"><div class="mobile-menu-label">問題別</div>
<a class="mobile-link" href="/membership.html">入会手続</a>
<a class="mobile-link" href="/privacy.html">個人情報</a>
<a class="mobile-link" href="/fee-collection.html">会費徴収</a>
<a class="mobile-link" href="/personnel.html">教職員関与</a>
<a class="mobile-link" href="/facilities.html">施設利用</a></div>
<div class="mobile-menu-group"><div class="mobile-menu-label">根拠資料</div>
<a class="mobile-link" href="/research-index.html">根拠資料の入口</a>
<a class="mobile-link" href="/board-responses.html">教育委員会の回答</a>
<a class="mobile-link" href="/national-archive.html">全国資料館</a>
<a class="mobile-link" href="/administrative-materials.html">行政通知・公式PDF</a></div>
<div class="mobile-menu-group mobile-menu-bottom"><div class="mobile-menu-label">チェック・文例</div>
<a class="mobile-link" href="/audit/index.html">運営チェック</a>
<a class="mobile-link" href="/documents.html">資料入口・文例索引</a>
<a class="mobile-link" href="/contact.html">問い合わせ・情報提供</a>
<a class="mobile-link support-mobile-link" href="/support.html">応援・寄付</a></div>
<button type="button" class="mobile-close-btn" id="closeOverlay" aria-label="メニューを閉じる">閉じる ×</button>
</div>`;

const navPattern = /<nav aria-label="主要ナビゲーション" class="desktop-nav">[\s\S]*?<\/nav>/;
const mobilePattern = /<div class="mobile-overlay" id="mobileOverlay">[\s\S]*?(?:<div class="close-overlay" id="closeOverlay">CLOSE ×<\/div>|<button[^>]*id="closeOverlay"[^>]*>[\s\S]*?<\/button>)\s*<\/div>/;
const emptyMobilePattern = /<div class="mobile-overlay" id="mobileOverlay"(?:\s+aria-hidden="true")?>\s*<\/div>/;

const changedFiles = [];
const unchangedFiles = [];

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
    if (!text.includes('/js/site.js') && !text.includes('js/site.js')) continue;
    if (!text.includes('class="desktop-nav"') && !text.includes('id="mobileOverlay"')) continue;

    let next = text;
    const hasNav = navPattern.test(next);
    const hasMobile = mobilePattern.test(next) || emptyMobilePattern.test(next);

    if (hasNav) next = next.replace(navPattern, desktopNav);
    if (mobilePattern.test(next)) next = next.replace(mobilePattern, mobileOverlay);
    else if (emptyMobilePattern.test(next)) next = next.replace(emptyMobilePattern, mobileOverlay);

    if (next !== text) {
      changedFiles.push(path.relative(ROOT, full));
      if (!DRY_RUN) fs.writeFileSync(full, next, 'utf8');
    } else {
      unchangedFiles.push(path.relative(ROOT, full));
    }
  }
}

walk(ROOT);

console.log(`${DRY_RUN ? 'Would update' : 'Updated'} ${changedFiles.length} HTML files.`);
for (const file of changedFiles) console.log(`- ${file}`);

if (unchangedFiles.length) {
  console.log(`\nAlready current: ${unchangedFiles.length} HTML files.`);
}
