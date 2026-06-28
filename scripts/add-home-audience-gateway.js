const fs = require('fs');
const path = require('path');

const INDEX_PATH = path.join(__dirname, '..', 'index.html');
const html = fs.readFileSync(INDEX_PATH, 'utf8');

if (html.includes('id="audience-gateway"')) {
  console.log('audience gateway already exists; no changes made.');
  process.exit(0);
}

const anchor = '</section>\n<section aria-labelledby="home-reading-title" class="home-reading-section"';

const block = `</section>
<section aria-labelledby="audience-gateway-title" class="home-audience-gateway" id="audience-gateway" style="background:#f8fafc;padding:44px 0;border-bottom:1px solid rgba(5,17,31,.08)">
<div class="wrap" style="max-width:1080px">
<div class="section-center" style="margin-bottom:28px">
<div class="section-kicker">Start Here</div>
<h2 class="section-title" id="audience-gateway-title">まず、ご自身の立場から確認してください。</h2>
<p class="section-lead" style="max-width:820px">PTA問題は、立場によって最初に確認すべき文書が異なります。保護者、PTA役員、教育委員会・学校の入口を分けて、入会意思、会費、個人情報、学校関与を順に確認できるようにしています。</p>
</div>
<div class="audience-gateway-grid" style="display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px">
<a class="audience-gateway-card" href="guide-parent.html" style="display:block;background:#fff;border:1px solid #dbe4ee;border-radius:18px;padding:24px 24px 22px;text-decoration:none;color:inherit;box-shadow:0 10px 26px rgba(5,17,31,.06)">
<div style="font-size:.76rem;font-weight:900;letter-spacing:.08em;color:#1e3a5f;text-transform:uppercase;margin-bottom:10px">For Parents</div>
<h3 style="font-size:1.18rem;color:#0f2747;margin:0 0 10px;font-weight:900">保護者の方へ</h3>
<p style="font-size:.94rem;line-height:1.85;color:#475569;margin:0 0 18px">入会した覚えがない、会費の根拠が分からない、非加入・退会後の扱いが不安な場合に、最初に確認する資料です。</p>
<span style="font-size:.88rem;font-weight:900;color:#0f2747">保護者向け入口へ →</span>
</a>
<a class="audience-gateway-card" href="guide-pta.html" style="display:block;background:#fff;border:1px solid #dbe4ee;border-radius:18px;padding:24px 24px 22px;text-decoration:none;color:inherit;box-shadow:0 10px 26px rgba(5,17,31,.06)">
<div style="font-size:.76rem;font-weight:900;letter-spacing:.08em;color:#1e3a5f;text-transform:uppercase;margin-bottom:10px">For PTA Officers</div>
<h3 style="font-size:1.18rem;color:#0f2747;margin:0 0 10px;font-weight:900">PTA役員の方へ</h3>
<p style="font-size:.94rem;line-height:1.85;color:#475569;margin:0 0 18px">前年度から引き継いだ運営を、入会申込書、会費徴収、個人情報、学校との役割分担から点検します。</p>
<span style="font-size:.88rem;font-weight:900;color:#0f2747">役員向け入口へ →</span>
</a>
<a class="audience-gateway-card" href="guide-board.html" style="display:block;background:#fff;border:1px solid #dbe4ee;border-radius:18px;padding:24px 24px 22px;text-decoration:none;color:inherit;box-shadow:0 10px 26px rgba(5,17,31,.06)">
<div style="font-size:.76rem;font-weight:900;letter-spacing:.08em;color:#1e3a5f;text-transform:uppercase;margin-bottom:10px">For Schools / Boards</div>
<h3 style="font-size:1.18rem;color:#0f2747;margin:0 0 10px;font-weight:900">教育委員会・学校へ</h3>
<p style="font-size:.94rem;line-height:1.85;color:#475569;margin:0 0 18px">PTAは任意団体ですが、学校の情報、徴収金、教職員、施設利用に関する関与は点検対象です。</p>
<span style="font-size:.88rem;font-weight:900;color:#0f2747">学校・教委向け入口へ →</span>
</a>
</div>
</div>
<style>@media(max-width:760px){.audience-gateway-grid{grid-template-columns:1fr!important}.home-audience-gateway{padding:34px 0!important}.audience-gateway-card{padding:22px 20px!important}}</style>
</section>
<section aria-labelledby="home-reading-title" class="home-reading-section"`;

if (!html.includes(anchor)) {
  console.error('anchor not found; index.html was not changed.');
  process.exit(1);
}

const next = html.replace(anchor, block);
fs.writeFileSync(INDEX_PATH, next, 'utf8');
console.log('inserted audience gateway into index.html.');
