const fs = require('fs');
const path = require('path');

const STYLE_PATH = path.join(__dirname, '..', 'css', 'style.css');
let css = fs.readFileSync(STYLE_PATH, 'utf8');

const replacements = [
  [
    '.page-hero{background:linear-gradient(135deg,#dbeafe 0%,#e0f2fe 50%,#ede9fe 100%);color:var(--navy);padding:72px 0 64px;position:relative;overflow:hidden;border-top:4px solid var(--gold);border-bottom:1px solid #c7d9f5}',
    '.page-hero{background:linear-gradient(135deg,#05172f 0%,#0f2747 58%,#16385f 100%);color:#fff;padding:58px 0 54px;position:relative;overflow:hidden;border-top:3px solid var(--gold);border-bottom:1px solid rgba(5,17,31,.18)}'
  ],
  [
    '.page-hero::before{content:\'\';position:absolute;inset:0;background-image:radial-gradient(circle,rgba(29,78,216,.07) 1px,transparent 1px);background-size:44px 44px}',
    '.page-hero::before{content:\'\';position:absolute;inset:0;background-image:radial-gradient(circle,rgba(255,255,255,.055) 1px,transparent 1px);background-size:46px 46px}'
  ],
  [
    '.page-hero::after{content:\'\';position:absolute;inset:0;background:radial-gradient(ellipse 80% 60% at 80% 30%,rgba(212,175,55,.12),transparent 60%)}',
    '.page-hero::after{content:\'\';position:absolute;inset:0;background:radial-gradient(ellipse 78% 58% at 84% 24%,rgba(212,175,55,.16),transparent 62%)}'
  ],
  [
    '.page-hero-kicker{display:inline-flex;align-items:center;gap:8px;padding:6px 14px;border-radius:999px;background:rgba(29,78,216,.1);border:1px solid rgba(29,78,216,.25);color:#1d4ed8;font-size:.74rem;font-weight:900;letter-spacing:.1em;text-transform:uppercase;margin-bottom:16px}',
    '.page-hero-kicker{display:inline-flex;align-items:center;gap:8px;padding:6px 14px;border-radius:999px;background:rgba(212,175,55,.14);border:1px solid rgba(212,175,55,.42);color:#fff2a8;font-size:.74rem;font-weight:900;letter-spacing:.1em;text-transform:uppercase;margin-bottom:16px}'
  ],
  [
    '.page-hero h1{font-family:\'Noto Serif JP\',serif;font-size:clamp(1.7rem,3.2vw,2.8rem);font-weight:900;line-height:1.28;margin-bottom:16px;color:var(--navy)}',
    '.page-hero h1{font-family:\'Noto Serif JP\',serif;font-size:clamp(1.6rem,3vw,2.55rem);font-weight:900;line-height:1.34;margin-bottom:16px;color:#fff;letter-spacing:-.02em}'
  ],
  [
    '.page-hero h1 em{font-style:normal;color:#1d4ed8}',
    '.page-hero h1 em{font-style:normal;color:#fff2a8}'
  ],
  [
    '.page-hero p{color:var(--text-soft);font-size:1rem;line-height:1.85;max-width:680px}',
    '.page-hero p{color:rgba(255,255,255,.86);font-size:1rem;line-height:1.9;max-width:760px;font-weight:600}'
  ],
];

let changed = false;
for (const [from, to] of replacements) {
  if (css.includes(to)) {
    continue;
  }
  if (!css.includes(from)) {
    console.error(`expected CSS fragment not found: ${from}`);
    process.exit(1);
  }
  css = css.replace(from, to);
  changed = true;
}

if (!changed) {
  console.log('global page heroes already tuned; no changes made.');
  process.exit(0);
}

fs.writeFileSync(STYLE_PATH, css, 'utf8');
console.log('tuned global page hero style.');
