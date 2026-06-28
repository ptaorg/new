const fs = require('fs');

const file = 'css/style.css';
const marker = '/* === Parent guide case card colors === */';
let css = fs.readFileSync(file, 'utf8');

if (css.includes(marker)) {
  console.log('Parent case card colors already added.');
  process.exit(0);
}

css += `

${marker}
.parent-page .case-section{
  background:linear-gradient(180deg,#fff 0%,#f7f3e8 100%) !important;
}
.parent-page .case-list{
  gap:22px !important;
}
.parent-page .case-card{
  position:relative !important;
  overflow:hidden !important;
  border:1px solid rgba(15,39,71,.14) !important;
  border-left:7px solid var(--pta-teal,#2f6f73) !important;
  background:linear-gradient(90deg,rgba(47,111,115,.055),#fff 28%) !important;
  box-shadow:0 12px 30px rgba(5,17,31,.08) !important;
}
.parent-page .case-card::before{
  content:'' !important;
  position:absolute !important;
  left:0 !important;
  top:0 !important;
  right:0 !important;
  height:5px !important;
  background:var(--pta-teal,#2f6f73) !important;
}
.parent-page .case-card .case-tag{
  background:var(--pta-teal,#2f6f73) !important;
  color:#fff !important;
}
.parent-page .case-card .case-subject{
  color:#0f2747 !important;
}
.parent-page .case-card .case-toggle{
  color:var(--pta-teal,#2f6f73) !important;
}
.parent-page .case-card:nth-child(1){
  border-left-color:var(--pta-redbrown,#8c3b2f) !important;
  background:linear-gradient(90deg,rgba(140,59,47,.065),#fff 28%) !important;
}
.parent-page .case-card:nth-child(1)::before,
.parent-page .case-card:nth-child(1) .case-tag{background:var(--pta-redbrown,#8c3b2f) !important;}
.parent-page .case-card:nth-child(1) .case-toggle{color:var(--pta-redbrown,#8c3b2f) !important;}
.parent-page .case-card:nth-child(2){
  border-left-color:var(--gold,#d4af37) !important;
  background:linear-gradient(90deg,rgba(212,175,55,.12),#fff 28%) !important;
}
.parent-page .case-card:nth-child(2)::before,
.parent-page .case-card:nth-child(2) .case-tag{background:#b68a1f !important;}
.parent-page .case-card:nth-child(2) .case-toggle{color:#9a7418 !important;}
.parent-page .case-card:nth-child(3){
  border-left-color:var(--pta-teal,#2f6f73) !important;
  background:linear-gradient(90deg,rgba(47,111,115,.08),#fff 28%) !important;
}
.parent-page .case-card:nth-child(4){
  border-left-color:var(--navy,#0f2747) !important;
  background:linear-gradient(90deg,rgba(15,39,71,.07),#fff 28%) !important;
}
.parent-page .case-card:nth-child(4)::before,
.parent-page .case-card:nth-child(4) .case-tag{background:var(--navy,#0f2747) !important;}
.parent-page .case-card:nth-child(4) .case-toggle{color:var(--navy,#0f2747) !important;}
.parent-page .case-card:hover{
  transform:translateY(-3px) !important;
  box-shadow:0 18px 42px rgba(5,17,31,.12) !important;
}
.parent-page .case-meta{
  padding-top:2px !important;
}
.parent-page .case-from{
  color:#64748b !important;
  font-weight:800 !important;
}
.parent-page .case-summary{
  color:#475569 !important;
}
.parent-page .case-answer .case-quote{
  background:#fffaf0 !important;
}
@media (max-width:760px){
  .parent-page .case-card{
    border-left-width:5px !important;
  }
}
`;

fs.writeFileSync(file, css, 'utf8');
console.log('Added parent guide case card colors.');
