const fs = require('fs');

const file = 'journal.html';
const marker = '<style id="journal-hero-head-fix">';
let html = fs.readFileSync(file, 'utf8');

if (html.includes(marker)) {
  console.log('Journal hero head fix already added.');
  process.exit(0);
}

const style = `
${marker}
  .journal-page .page-hero--photo{
    background:linear-gradient(135deg,#05172f 0%,#0f2747 58%,#16385f 100%) !important;
    border-top:1px solid rgba(212,175,55,.45) !important;
    border-bottom:1px solid rgba(5,17,31,.18) !important;
    padding:58px 0 54px !important;
    min-height:0 !important;
    overflow:hidden !important;
  }
  .journal-page .page-hero--photo::before{
    content:'' !important;
    position:absolute !important;
    inset:auto -12% -46% auto !important;
    width:420px !important;
    height:420px !important;
    background:radial-gradient(circle,rgba(212,175,55,.18),rgba(212,175,55,0) 70%) !important;
    pointer-events:none !important;
  }
  .journal-page .page-hero-bg-img{
    display:none !important;
  }
  .journal-page .page-hero-inner{
    width:min(calc(100% - 40px),1080px) !important;
    margin-inline:auto !important;
    position:relative !important;
    z-index:1 !important;
  }
  .journal-page .page-hero-kicker{
    display:inline-flex !important;
    align-items:center !important;
    padding:6px 13px !important;
    border-radius:999px !important;
    background:rgba(212,175,55,.14) !important;
    border:1px solid rgba(212,175,55,.42) !important;
    color:#fff2a8 !important;
    font-size:.72rem !important;
    font-weight:900 !important;
    letter-spacing:.12em !important;
    text-transform:uppercase !important;
    margin-bottom:18px !important;
  }
  .journal-page .page-hero h1{
    max-width:820px !important;
    margin:0 !important;
    color:#fff !important;
    text-shadow:none !important;
    font-size:clamp(1.85rem,3.8vw,3rem) !important;
    line-height:1.28 !important;
  }
  .journal-page .page-hero h1 em{
    color:#fff2a8 !important;
    font-style:normal !important;
  }
  .journal-page .page-hero p{
    max-width:820px !important;
    margin:18px 0 0 !important;
    color:rgba(255,255,255,.88) !important;
    text-shadow:none !important;
    font-weight:700 !important;
    line-height:1.95 !important;
  }
  .journal-page .breadcrumb-bar{
    background:#fff !important;
    border-bottom:1px solid rgba(5,17,31,.08) !important;
  }
  @media(max-width:760px){
    .journal-page .page-hero--photo{
      padding:44px 0 40px !important;
    }
  }
</style>
`;

html = html.replace('</head>', `${style}</head>`);
fs.writeFileSync(file, html, 'utf8');
console.log('Added journal hero head fix.');
