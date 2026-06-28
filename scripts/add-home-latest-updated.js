const fs = require('fs');
const path = require('path');

const INDEX_PATH = path.join(__dirname, '..', 'index.html');
const html = fs.readFileSync(INDEX_PATH, 'utf8');

const updatedLine = '<p class="home-latest-updated" style="margin:10px 0 0;color:#64748b;font-size:.92rem;font-weight:700">最終更新：2026年6月28日</p>';

if (html.includes('class="home-latest-updated"')) {
  const next = html.replace(/<p class="home-latest-updated"[\s\S]*?<\/p>/, updatedLine);
  fs.writeFileSync(INDEX_PATH, next, 'utf8');
  console.log('updated existing latest update date.');
  process.exit(0);
}

const anchor = '<h2 class="section-title">最新更新・掲載情報</h2>';

if (!html.includes(anchor)) {
  console.error('latest update heading not found; index.html was not changed.');
  process.exit(1);
}

const next = html.replace(anchor, `${anchor}\n${updatedLine}`);
fs.writeFileSync(INDEX_PATH, next, 'utf8');
console.log('inserted latest update date into index.html.');
