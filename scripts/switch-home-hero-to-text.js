const fs = require('fs');
const path = require('path');

const INDEX_PATH = path.join(__dirname, '..', 'index.html');
const html = fs.readFileSync(INDEX_PATH, 'utf8');

if (html.includes('class="home-text-hero"')) {
  console.log('text hero already exists; no changes made.');
  process.exit(0);
}

const heroStart = '<section aria-labelledby="top-hero-title" class="home-photo-hero">';
const gatewayStart = '<section aria-labelledby="audience-gateway-title" class="home-audience-gateway"';
const readingStart = '<section aria-labelledby="home-reading-title" class="home-reading-section"';

const startIndex = html.indexOf(heroStart);
if (startIndex === -1) {
  console.error('photo hero start not found; index.html was not changed.');
  process.exit(1);
}

let nextSectionIndex = html.indexOf(gatewayStart, startIndex);
if (nextSectionIndex === -1) {
  nextSectionIndex = html.indexOf(readingStart, startIndex);
}
if (nextSectionIndex === -1) {
  console.error('next section after hero not found; index.html was not changed.');
  process.exit(1);
}

const textHero = `<section aria-labelledby="top-hero-title" class="home-text-hero" style="background:linear-gradient(135deg,#05172f 0%,#0f2747 58%,#16385f 100%);color:#fff;border-top:1px solid rgba(212,175,55,.5);border-bottom:1px solid rgba(5,17,31,.18)">
<div class="wrap" style="max-width:1080px;padding:58px 24px 54px">
<div style="display:inline-flex;align-items:center;padding:6px 13px;border-radius:999px;background:rgba(212,175,55,.14);border:1px solid rgba(212,175,55,.42);color:#fff2a8;font-size:.72rem;font-weight:900;letter-spacing:.12em;text-transform:uppercase;margin-bottom:18px">Research · Evidence · Legal Compliance</div>
<h1 id="top-hero-title" style="max-width:820px;margin:0;font-family:'Noto Serif JP',serif;font-size:clamp(1.72rem,3.4vw,2.75rem);font-weight:900;line-height:1.34;letter-spacing:-.02em;color:#fff">PTAを、任意加入の原則と<br/><span style="color:#fff2a8">法令に基づく運営</span>へ。</h1>
<p style="max-width:820px;margin:18px 0 0;font-size:clamp(.98rem,1.45vw,1.12rem);line-height:1.95;color:rgba(255,255,255,.86);font-weight:600">学校手続に溶け込んだPTA運営を、入会意思、個人情報、会費徴収、教職員関与、学校施設利用から点検します。慣習ではなく、文書と根拠で確認するための資料ポータルです。</p>
<div aria-label="トップページの主要導線" class="home-photo-hero-actions" style="display:flex;flex-wrap:wrap;gap:12px;margin-top:26px">
<a class="primary" href="#audience-gateway" style="display:inline-flex;align-items:center;justify-content:center;min-height:42px;padding:10px 20px;border-radius:999px;text-decoration:none;font-size:.9rem;font-weight:900;line-height:1;background:var(--gold,#d4af37);color:var(--navy,#05172f);box-shadow:0 8px 24px rgba(5,17,31,.22)">立場別に確認する</a>
<a class="secondary" href="documents.html" style="display:inline-flex;align-items:center;justify-content:center;min-height:42px;padding:10px 20px;border-radius:999px;text-decoration:none;font-size:.9rem;font-weight:900;line-height:1;color:#fff;border:1px solid rgba(255,255,255,.55);background:rgba(255,255,255,.1);box-shadow:0 8px 24px rgba(5,17,31,.22)">根拠資料を見る</a>
</div>
</div>
</section>
`;

const next = html.slice(0, startIndex) + textHero + html.slice(nextSectionIndex);
fs.writeFileSync(INDEX_PATH, next, 'utf8');
console.log('switched homepage hero to text-only hero.');
