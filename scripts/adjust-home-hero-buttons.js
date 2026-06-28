const fs = require('fs');
const path = require('path');

const INDEX_PATH = path.join(__dirname, '..', 'index.html');
const html = fs.readFileSync(INDEX_PATH, 'utf8');

const currentBlock = `<div aria-label="トップページの主要導線" class="home-photo-hero-actions">
<a class="primary" href="guide-parent.html">保護者として読む</a>
<a class="secondary" href="guide-board.html">学校・教育委員会向け</a>
<a class="secondary" href="national-archive.html">資料を見る</a>
</div>`;

const nextBlock = `<div aria-label="トップページの主要導線" class="home-photo-hero-actions">
<a class="primary" href="#audience-gateway">立場別に確認する</a>
<a class="secondary" href="documents.html">根拠資料を見る</a>
</div>`;

if (html.includes(nextBlock)) {
  console.log('hero buttons already adjusted; no changes made.');
  process.exit(0);
}

if (!html.includes(currentBlock)) {
  console.error('expected hero button block not found; index.html was not changed.');
  process.exit(1);
}

const next = html.replace(currentBlock, nextBlock);
fs.writeFileSync(INDEX_PATH, next, 'utf8');
console.log('adjusted homepage hero buttons.');
