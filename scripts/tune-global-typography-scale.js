const fs = require('fs');

const file = 'css/style.css';
const marker = '/* === Global typography scale tuning === */';
let css = fs.readFileSync(file, 'utf8');

if (css.includes(marker)) {
  console.log('Global typography scale tuning already added.');
  process.exit(0);
}

css += `

${marker}
:root{
  --type-hero-title:clamp(1.48rem,2.55vw,2.22rem);
  --type-page-title:clamp(1.42rem,2.45vw,2.18rem);
  --type-section-title:clamp(1.35rem,2.25vw,2.05rem);
  --type-card-title:clamp(1.02rem,1.35vw,1.18rem);
  --type-lead:.96rem;
}

/* Page and section headings: reduce visual pressure while preserving hierarchy */
.page-hero h1,
.page-hero--photo h1{
  font-size:var(--type-page-title) !important;
  line-height:1.36 !important;
  letter-spacing:-.012em !important;
}
.page-hero p,
.page-hero--photo p{
  font-size:var(--type-lead) !important;
  line-height:1.9 !important;
}
.section-title{
  font-size:var(--type-section-title) !important;
  line-height:1.34 !important;
  letter-spacing:-.01em !important;
}
.section-lead{
  font-size:.95rem !important;
  line-height:1.85 !important;
}

/* Homepage text hero */
.home-text-hero h1,
.home-photo-hero-title{
  font-size:var(--type-hero-title) !important;
  line-height:1.36 !important;
  letter-spacing:-.012em !important;
}
.home-text-hero p,
.home-photo-hero-lead{
  font-size:.98rem !important;
  line-height:1.88 !important;
}

/* Common large headings in article/list pages */
.journal-page .page-hero h1,
.parent-page .page-hero h1,
.board-page .page-hero h1,
.pta-page .page-hero h1,
.simple-hero h1{
  font-size:var(--type-page-title) !important;
  line-height:1.36 !important;
}
.journal-intro h2,
.panel h2,
.article-title,
.guide-section h2,
.content-section h2,
.feature-section h2{
  font-size:clamp(1.18rem,1.75vw,1.55rem) !important;
  line-height:1.45 !important;
}

/* Card titles */
.audience-gateway-card h3,
.action-pack-card h3,
.article-card h3,
.ac-title,
.case-subject,
.card h3{
  font-size:var(--type-card-title) !important;
  line-height:1.5 !important;
}

/* Header/nav should stay compact */
.logo{
  font-size:clamp(.88rem,1.35vw,1.05rem) !important;
}
.nav-link{
  font-size:.86rem !important;
}
.btn-gold,
.btn-navy,
.btn-outline,
.btn-soft{
  font-size:.86rem !important;
}

@media(max-width:760px){
  :root{
    --type-hero-title:clamp(1.34rem,6vw,1.78rem);
    --type-page-title:clamp(1.32rem,5.6vw,1.72rem);
    --type-section-title:clamp(1.22rem,5vw,1.58rem);
    --type-card-title:1.02rem;
    --type-lead:.92rem;
  }
  .page-hero,
  .page-hero--photo{
    padding-top:40px !important;
    padding-bottom:38px !important;
  }
  .section-kicker,
  .page-hero-kicker{
    font-size:.68rem !important;
  }
}
`;

fs.writeFileSync(file, css, 'utf8');
console.log('Added global typography scale tuning.');
