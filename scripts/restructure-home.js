const fs = require('fs');
const path = require('path');

const file = path.join(__dirname, '..', 'index.html');
let html = fs.readFileSync(file, 'utf8');

function sectionRangeAt(start) {
  if (start < 0 || !html.startsWith('<section', start)) throw new Error('Section start not found');
  const token = /<section\b|<\/section>/g;
  token.lastIndex = start;
  let depth = 0;
  let match;
  while ((match = token.exec(html))) {
    if (match[0] === '<section') depth += 1;
    else depth -= 1;
    if (depth === 0) return [start, token.lastIndex];
  }
  throw new Error('Unclosed section');
}

function findSection(marker) {
  const markerAt = html.indexOf(marker);
  if (markerAt < 0) return null;
  const start = html.lastIndexOf('<section', markerAt);
  return sectionRangeAt(start);
}

const today = `<section class="home-next-section" aria-labelledby="home-next-title">
<div class="wrap" style="max-width:1080px">
<div class="home-next-section__head">
<div class="section-kicker">今日できること</div>
<h2 id="home-next-title">説明を読むだけで終わらせず、一つ記録を残す</h2>
<p>すべてを理解してから動く必要はありません。今の立場に近い作業を一つ選ぶと、確認すべき資料と次の文書へ進めます。</p>
</div>
<div class="home-next-grid">
<a class="home-next-card" href="/audit/index.html"><span>CHECK</span><strong>現在の運営を点検する</strong><p>入会、名簿、会費、教職員、施設の状態を設問に沿って確認します。</p></a>
<a class="home-next-card" href="/evidence-checklist.html"><span>RECORD</span><strong>手元の資料を整理する</strong><p>確認できた事実、未確認点、次に照会する文書を分けて記録します。</p></a>
<a class="home-next-card" href="/documents.html"><span>ACTION</span><strong>確認文・申入書を使う</strong><p>学校、PTA、教育委員会へ出す文例と配布資料を目的別に探します。</p></a>
</div>
</div>
</section>`;

if (!html.includes('class="home-next-section"')) {
  const firstReading = findSection('aria-labelledby="home-reading-title"');
  if (!firstReading) throw new Error('Primary home reading section not found');
  html = html.slice(0, firstReading[1]) + '\n' + today + html.slice(firstReading[1]);
}

const walkthrough = findSection('このサイトの歩き方');
if (walkthrough) html = html.slice(0, walkthrough[0]) + html.slice(walkthrough[1]);

let fieldcase = findSection('class="fieldcase-section"');
let proper = findSection('class="proper-section"');
if (!fieldcase) throw new Error('Fieldcase section not found');
if (!proper) throw new Error('Proper management section not found');
if (fieldcase[0] < proper[0]) {
  const fieldcaseHtml = html.slice(fieldcase[0], fieldcase[1]);
  html = html.slice(0, fieldcase[0]) + html.slice(fieldcase[1]);
  proper = findSection('class="proper-section"');
  html = html.slice(0, proper[1]) + '\n' + fieldcaseHtml + html.slice(proper[1]);
}

if (!html.includes('/css/home-clarity.css')) {
  html = html.replace('</head>', '<link rel="stylesheet" href="/css/home-clarity.css?v=20260701">\n</head>');
}

html = html.replace(/最終更新：\d{4}年\d{1,2}月\d{1,2}日/, '掲載情報更新：2026年7月1日');
fs.writeFileSync(file, html, 'utf8');
console.log('Restructured index.html');
