const fs = require('fs');
const path = require('path');

const STYLE_PATH = path.join(__dirname, '..', 'css', 'style.css');
let css = fs.readFileSync(STYLE_PATH, 'utf8');

const marker = '/* === Force text-only page heroes === */';
const block = `${marker}
.page-hero--photo{
  background:linear-gradient(135deg,#05172f 0%,#0f2747 58%,#16385f 100%)!important;
  color:#fff!important;
  min-height:0!important;
  padding:58px 0 54px!important;
  border-top:3px solid var(--gold)!important;
  border-bottom:1px solid rgba(5,17,31,.18)!important;
}
.page-hero--photo .page-hero-bg-img{display:none!important;}
.page-hero--photo::before{
  content:''!important;
  position:absolute!important;
  inset:0!important;
  background-image:radial-gradient(circle,rgba(255,255,255,.055) 1px,transparent 1px)!important;
  background-size:46px 46px!important;
}
.page-hero--photo::after{
  content:''!important;
  position:absolute!important;
  inset:0!important;
  background:radial-gradient(ellipse 78% 58% at 84% 24%,rgba(212,175,55,.16),transparent 62%)!important;
}
.page-hero--photo .page-hero-inner{position:relative!important;z-index:1!important;}
.page-hero--photo .page-hero-kicker{
  background:rgba(212,175,55,.14)!important;
  border:1px solid rgba(212,175,55,.42)!important;
  color:#fff2a8!important;
}
.page-hero--photo h1{color:#fff!important;letter-spacing:-.02em!important;}
.page-hero--photo h1 em{color:#fff2a8!important;}
.page-hero--photo p{color:rgba(255,255,255,.86)!important;font-weight:600!important;}
.page-hero--photo .btn-outline,
.page-hero--photo .btn-outline-white{
  color:#fff!important;
  border-color:rgba(255,255,255,.55)!important;
  background:rgba(255,255,255,.1)!important;
}
`;

if (css.includes(marker)) {
  console.log('photo page hero override already exists; no changes made.');
  process.exit(0);
}

css = `${css.trim()}\n\n${block}\n`;
fs.writeFileSync(STYLE_PATH, css, 'utf8');
console.log('added text-only override for photo page heroes.');
