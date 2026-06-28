const fs = require('fs');

const file = 'css/style.css';
const marker = '/* === Action pack diagram large layout === */';
let css = fs.readFileSync(file, 'utf8');

if (css.includes(marker)) {
  console.log('Already added.');
  process.exit(0);
}

css += `

${marker}
.action-pack-layout{
  display:flex !important;
  flex-direction:column !important;
  gap:24px !important;
}

.action-pack-figure{
  order:-1 !important;
  width:100% !important;
  max-width:980px !important;
  margin:0 auto 8px !important;
  padding:18px !important;
  background:#fff !important;
  border:1px solid rgba(15,39,71,.12) !important;
  border-radius:16px !important;
  box-shadow:0 10px 24px rgba(5,17,31,.06) !important;
}

.action-pack-figure img{
  display:block !important;
  width:100% !important;
  max-width:900px !important;
  margin:0 auto !important;
  height:auto !important;
}

.action-pack-figure figcaption{
  margin-top:12px !important;
  text-align:center !important;
  font-size:.95rem !important;
  line-height:1.7 !important;
  color:#475569 !important;
}

.action-pack-grid{
  width:100% !important;
  display:grid !important;
  grid-template-columns:repeat(2,minmax(0,1fr)) !important;
  gap:16px !important;
}

@media (max-width:760px){
  .action-pack-grid{
    grid-template-columns:1fr !important;
  }

  .action-pack-figure{
    padding:14px !important;
  }
}
`;

fs.writeFileSync(file, css, 'utf8');
console.log('Added action-pack diagram layout CSS.');
