const fs = require('fs');
const path = require('path');

const STYLE_PATH = path.join(__dirname, '..', 'css', 'style.css');
let css = fs.readFileSync(STYLE_PATH, 'utf8');

const marker = '/* === Homepage color accents === */';
const block = `${marker}
:root{
  --pta-cream:#f7f3e8;
  --pta-teal:#2f6f73;
  --pta-redbrown:#8c3b2f;
  --pta-softgray:#eef1f4;
}
.home-audience-gateway{
  background:var(--pta-cream)!important;
  border-top:1px solid rgba(140,59,47,.16)!important;
  border-bottom:1px solid rgba(140,59,47,.16)!important;
}
.home-audience-gateway .audience-gateway-card{
  position:relative!important;
  overflow:hidden!important;
  border:1px solid rgba(15,39,71,.14)!important;
  box-shadow:0 12px 28px rgba(5,17,31,.08)!important;
}
.home-audience-gateway .audience-gateway-card::before{
  content:''!important;
  position:absolute!important;
  left:0!important;
  top:0!important;
  right:0!important;
  height:6px!important;
  background:var(--pta-teal)!important;
}
.home-audience-gateway .audience-gateway-card:nth-child(2)::before{background:var(--navy)!important;}
.home-audience-gateway .audience-gateway-card:nth-child(3)::before{background:var(--gold)!important;}
.home-audience-gateway .audience-gateway-card:nth-child(1) div:first-child{color:var(--pta-teal)!important;}
.home-audience-gateway .audience-gateway-card:nth-child(2) div:first-child{color:var(--navy)!important;}
.home-audience-gateway .audience-gateway-card:nth-child(3) div:first-child{color:#9a7418!important;}
.home-reading-section{
  background:#fffaf0!important;
  border-top:1px solid rgba(140,59,47,.18)!important;
  border-bottom:1px solid rgba(140,59,47,.18)!important;
}
.home-reading-section .section-kicker{
  background:rgba(140,59,47,.09)!important;
  color:var(--pta-redbrown)!important;
}
.home-reading-section .section-title{
  padding-left:18px!important;
  border-left:6px solid var(--pta-redbrown)!important;
}
.home-reading-section .editorial-bluebar{
  background:linear-gradient(90deg,var(--pta-teal),#0f7892)!important;
  color:#fff!important;
}
.home-reading-section .editorial-matrix{
  background:#fff!important;
  border:1px solid rgba(140,59,47,.16)!important;
  border-radius:14px!important;
  box-shadow:0 12px 28px rgba(5,17,31,.06)!important;
  overflow:hidden!important;
}
.home-reading-section .editorial-matrix-term{
  background:#eef5f3!important;
  color:var(--pta-teal)!important;
}
.home-reading-section .editorial-matrix-row:nth-child(2) .editorial-matrix-term{
  background:#f7f3e8!important;
  color:#9a7418!important;
}
.home-reading-section .editorial-matrix-row:nth-child(3) .editorial-matrix-term{
  background:#f8eeee!important;
  color:var(--pta-redbrown)!important;
}
.action-pack-section{
  background:linear-gradient(180deg,#f7f3e8 0%,#eef1f4 100%)!important;
  border-top:1px solid rgba(15,39,71,.12)!important;
}
.action-pack-section .section-kicker{
  background:rgba(47,111,115,.1)!important;
  color:var(--pta-teal)!important;
}
.action-pack-card{
  border-color:rgba(47,111,115,.2)!important;
  box-shadow:0 10px 24px rgba(5,17,31,.06)!important;
}
.action-pack-card:nth-child(1){border-left:5px solid var(--pta-redbrown)!important;}
.action-pack-card:nth-child(2){border-left:5px solid var(--pta-teal)!important;}
.action-pack-card:nth-child(3){border-left:5px solid var(--gold)!important;}
.action-pack-card:nth-child(4){border-left:5px solid var(--navy)!important;}
`;

if (css.includes(marker)) {
  console.log('homepage color accents already exist; no changes made.');
  process.exit(0);
}

css = `${css.trim()}\n\n${block}\n`;
fs.writeFileSync(STYLE_PATH, css, 'utf8');
console.log('added homepage color accents.');
