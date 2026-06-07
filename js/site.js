/* site.js v54 safe loader */
(function(){
  function baseInit(){
    var names=['addGlobalStyle','removeTopDonation','initPrimaryNavigation','initCompliancePageFixes','initParentCompliancePreview','initParentBoardResponsesPreview','initCommonFooter','initCompatibilityFixes','initMegaMenu','initMobileNav','initSearch','initFAQ','initChecklist','initPageClasses'];
    names.forEach(function(n){try{if(typeof window[n]==='function')window[n]();}catch(e){console.error('site init failed:',n,e);}});
  }
  function pdfLinks(){
    var cards=document.querySelectorAll('.parent-page .pdf-section .pdf-card');
    var ac='https://'+'acrobat'+'.'+'adobe'+'.'+'com/id/urn:aaid:sc:AP:';
    var pdfs=[ac+'ee52fff6-21cc-40c0-a631-bb9eafbca8c9',ac+'688231f9-f89a-45c4-a4c4-d29c85583a8b',ac+'36bed320-9ba2-4b4d-84fc-f90522a29e5b'];
    cards.forEach(function(card,i){var a=card.querySelector('a.pdf-btn');if(a&&pdfs[i]){a.href=pdfs[i];a.target='_blank';a.rel='noopener';a.textContent='PDF';}});
  }
  function topCards(){
    if(!(location.pathname==='/'||location.pathname.endsWith('/index.html')))return;
    var title=document.getElementById('home-reading-title');
    if(!title||document.querySelector('.home-role-entry-injected'))return;
    var st=document.createElement('style');
    st.textContent='.home-role-entry-injected{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px;margin:26px 0 34px}.home-role-entry-card{display:block;text-decoration:none;color:inherit;background:#fff;border:1px solid #d8e0ea;border-radius:16px;padding:22px;box-shadow:0 10px 28px rgba(5,17,31,.08);transition:.18s}.home-role-entry-card:hover{border-color:var(--gold);box-shadow:0 16px 38px rgba(5,17,31,.13);transform:translateY(-3px)}.home-role-entry-kicker{display:inline-flex;margin-bottom:10px;padding:3px 9px;border-radius:999px;background:rgba(212,175,55,.15);border:1px solid rgba(212,175,55,.35);color:#7a5c00;font-size:.68rem;font-weight:900}.home-role-entry-card h3{font-family:"Noto Serif JP",serif;color:var(--navy);font-size:1.04rem;line-height:1.45;margin:0 0 8px}.home-role-entry-card p{color:var(--text-soft);font-size:.86rem;line-height:1.82;margin:0 0 14px}.home-role-entry-cta{color:var(--navy);font-size:.82rem;font-weight:900}@media(max-width:820px){.home-role-entry-injected{grid-template-columns:1fr}}';
    document.head.appendChild(st);
    var block=document.createElement('div');
    block.className='home-role-entry-injected';
    block.innerHTML='<a class="home-role-entry-card" href="/guide-parent.html"><span class="home-role-entry-kicker">Parents</span><h3>&#20445;&#35703;&#32773;&#12398;&#26041;&#12408;</h3><p>&#20837;&#20250;&#12539;&#36864;&#20250;&#12539;&#20250;&#36027;&#12539;&#20491;&#20154;&#24773;&#22577;&#12395;&#12388;&#12356;&#12390;&#12289;&#12414;&#12378;&#20309;&#12434;&#30906;&#35469;&#12377;&#12427;&#12363;&#12434;&#25972;&#29702;&#12375;&#12414;&#12377;&#12290;</p><span class="home-role-entry-cta">&#20445;&#35703;&#32773;&#21521;&#12369;&#12460;&#12452;&#12489;&#12408; &#8594;</span></a><a class="home-role-entry-card" href="/guide-pta.html"><span class="home-role-entry-kicker">PTA</span><h3>PTA&#24441;&#21729;&#12398;&#26041;&#12408;</h3><p>&#20837;&#20250;&#35352;&#37682;&#12289;&#20250;&#36027;&#24500;&#21454;&#12289;&#20491;&#20154;&#24773;&#22577;&#12289;&#23398;&#26657;&#12392;&#12398;&#20998;&#38626;&#12434;&#23455;&#21209;&#12392;&#12375;&#12390;&#28857;&#26908;&#12375;&#12414;&#12377;&#12290;</p><span class="home-role-entry-cta">&#24441;&#21729;&#21521;&#12369;&#12460;&#12452;&#12489;&#12408; &#8594;</span></a><a class="home-role-entry-card" href="/guide-board.html"><span class="home-role-entry-kicker">Board</span><h3>&#25945;&#32946;&#22996;&#21729;&#20250;&#12539;&#23398;&#26657;&#12398;&#26041;&#12408;</h3><p>&#21517;&#31807;&#12289;&#24500;&#21454;&#12289;&#37197;&#24067;&#12289;&#26045;&#35373;&#12289;&#25945;&#32887;&#21729;&#38306;&#19982;&#12398;&#31684;&#22258;&#12434;&#30906;&#35469;&#12375;&#12414;&#12377;&#12290;</p><span class="home-role-entry-cta">&#23398;&#26657;&#12539;&#25945;&#22996;&#21521;&#12369;&#12460;&#12452;&#12489;&#12408; &#8594;</span></a>';
    title.insertAdjacentElement('afterend',block);
  }
  function loadArchiveNotice(){
    if(!location.pathname.endsWith('/national-archive.html'))return;
    var x=document.createElement('script');x.src='/js/archive-notice.js?v=1';document.head.appendChild(x);
  }
  function local(){pdfLinks();topCards();loadArchiveNotice();}
  var s=document.createElement('script');
  s.src='/js/site-v48-original.js?v=48';
  s.onload=function(){if(document.readyState==='loading'){document.addEventListener('DOMContentLoaded',function(){baseInit();local();},{once:true});}else{baseInit();local();}};
  s.onerror=function(){local();};
  document.head.appendChild(s);
})();
