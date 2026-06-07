/* site.js v60 safe loader */
(function(){
  function baseInit(){
    var names=['addGlobalStyle','removeTopDonation','initPrimaryNavigation','initCompliancePageFixes','initParentCompliancePreview','initParentBoardResponsesPreview','initCommonFooter','initCompatibilityFixes','initMegaMenu','initMobileNav','initSearch','initFAQ','initChecklist','initPageClasses'];
    names.forEach(function(n){
      try{ if(typeof window[n]==='function') window[n](); }
      catch(e){ console.error('site init failed:', n, e); }
    });
  }

  function normalizeNavigation(){
    var supportUrl='/support.html';
    var desktop=document.querySelector('.desktop-nav');
    if(desktop){
      desktop.innerHTML =
        '<a class="nav-link" href="/index.html">トップ</a>'+
        '<div class="nav-item has-dropdown"><a class="nav-link" href="#">立場別</a><div class="mega-menu"><div class="mega-col"><h4>立場別</h4><ul>'+
        '<li><a href="/guide-parent.html">保護者の方へ</a></li>'+
        '<li><a href="/guide-pta.html">PTA役員の方へ</a></li>'+
        '<li><a href="/guide-board.html">教育委員会・学校の方へ</a></li>'+
        '<li><a href="/guide-research.html">研究者・記者の方へ</a></li>'+
        '</ul></div></div></div>'+
        '<div class="nav-item has-dropdown"><a class="nav-link" href="#">資料・データ</a><div class="mega-menu"><div class="mega-col"><h4>一次資料</h4><ul>'+
        '<li><a href="/board-responses.html">教育委員会の回答</a></li>'+
        '<li><a href="/national-archive.html">全国資料館</a></li>'+
        '<li><a href="/administrative-materials.html">行政資料整理</a></li>'+
        '<li><a href="/compliance.html">PTA運営の現場実例</a></li>'+
        '</ul></div></div></div>'+
        '<div class="nav-item has-dropdown"><a class="nav-link" href="/journal.html">研究</a><div class="mega-menu"><div class="mega-col"><h4>論考・整理</h4><ul>'+
        '<li><a href="/guide-research.html">研究者・記者の方へ</a></li>'+
        '<li><a href="/journal.html">論考・調査報告</a></li>'+
        '<li><a href="/report.html">総合分析レポート</a></li>'+
        '<li><a href="/law-map.html">法制度マップ</a></li>'+
        '<li><a href="/cases.html">判例整理</a></li>'+
        '<li><a href="/timeline.html">PTA制度史</a></li>'+
        '</ul></div><div class="mega-col"><h4>論点別</h4><ul>'+
        '<li><a href="/membership.html">入会手続</a></li>'+
        '<li><a href="/privacy.html">個人情報</a></li>'+
        '<li><a href="/fee-collection.html">会費徴収</a></li>'+
        '<li><a href="/personnel.html">教職員関与</a></li>'+
        '<li><a href="/facilities.html">施設利用</a></li>'+
        '</ul></div></div></div>'+
        '<div class="nav-item has-dropdown"><a class="nav-link" href="#">ツール</a><div class="mega-menu"><div class="mega-col"><h4>点検用</h4><ul>'+
        '<li><a href="/audit/index.html">運営チェックアプリ</a></li>'+
        '<li><a href="/guideline.html">適正化ガイドライン</a></li>'+
        '</ul></div></div></div>'+
        '<a class="nav-link support-nav-link" href="'+supportUrl+'">応援</a>';
    }

    var mobile=document.getElementById('mobileOverlay');
    if(mobile){
      mobile.innerHTML =
        '<a class="mobile-link" href="/index.html"><span>Top</span>トップ</a>'+
        '<a class="mobile-link" href="/guide-parent.html"><span>Parents</span>保護者の方へ</a>'+
        '<a class="mobile-link" href="/guide-pta.html"><span>PTA Board</span>PTA役員の方へ</a>'+
        '<a class="mobile-link" href="/guide-board.html"><span>School Board</span>教育委員会・学校へ</a>'+
        '<a class="mobile-link" href="/guide-research.html"><span>Research</span>研究者・記者の方へ</a>'+
        '<a class="mobile-link" href="/board-responses.html"><span>Data</span>教育委員会の回答</a>'+
        '<a class="mobile-link" href="/national-archive.html"><span>Archive</span>全国資料館</a>'+
        '<a class="mobile-link" href="/administrative-materials.html"><span>Materials</span>行政資料整理</a>'+
        '<a class="mobile-link" href="/compliance.html"><span>Examples</span>現場実例</a>'+
        '<a class="mobile-link" href="/journal.html"><span>Journal</span>論考・調査報告</a>'+
        '<a class="mobile-link" href="/audit/index.html"><span>Check</span>運営チェックアプリ</a>'+
        '<a class="mobile-link support-mobile-link" href="'+supportUrl+'"><span>Support</span>応援・寄付</a>'+
        '<div class="close-overlay" id="closeOverlay">CLOSE ×</div>';
    }

    try{ if(typeof window.initMegaMenu==='function') window.initMegaMenu(); }
    catch(e){ console.error('site nav bind failed:', e); }
  }

  function normalizeLegacyLinks(){
    document.querySelectorAll('a[href]').forEach(function(a){
      var h=a.getAttribute('href');
      if(!h) return;
      if(h==='/donate/' || h==='donate/' || h==='https://ptaorg.com/donate/' || h==='https://ptaorg.github.io/donate/' || h==='https://ptaorg.github.io/donate') a.setAttribute('href','/support.html');
      if(h==='https://ptaorg.github.io/ed/' || h==='https://ptaorg.github.io/ed') a.setAttribute('href','https://ptaorg.com/ed');
    });
  }

  function rebuildHomeReadingSection(){
    var path=location.pathname;
    if(!(path==='/' || path.endsWith('/index.html')))return;
    var section=document.querySelector('.home-reading-section');
    if(!section || section.dataset.rebuilt==='1')return;
    section.dataset.rebuilt='1';
    section.innerHTML='<div class="wrap home-lead-wrap"><div class="section-kicker">はじめに</div><h2 class="section-title" id="home-reading-title">PTAを「学校の一部」として扱わないために。</h2><div class="home-lead-prose"><p>PTAは、保護者と教職員が任意に参加する民間の任意団体です。学校教育を支える活動であっても、入会、会費、名簿、役員選出、連絡、会計処理は、学校の手続とは分けて考える必要があります。</p><p>問題は、PTAが存在することそのものではありません。入学や進級の手続、学校徴収金、学校の名簿、学校連絡ツール、教職員の勤務時間の中にPTAの事務が溶け込み、保護者が「任意加入であること」「断れること」「会費を支払う根拠」を確認できなくなることです。</p><p>このサイトでは、保護者、PTA役員、学校・教育委員会のそれぞれの立場から、どこを確認し、どのように公私の境界を整えるべきかを、一次資料と法令に基づいて整理しています。</p></div><div class="home-role-grid" aria-label="立場別入口"><a class="home-role-card" href="/guide-parent.html"><span class="home-role-label">保護者の方へ</span><h3>入会した覚えがない、会費を止めたい、断ると子どもが心配。</h3><p>まずは、入会意思、会費徴収、個人情報、役員選出のどこを確認すればよいかを整理します。</p><span class="home-role-cta">保護者向けガイドを読む →</span></a><a class="home-role-card" href="/guide-pta.html"><span class="home-role-label">PTA役員の方へ</span><h3>善意の活動を、強制や不透明な運営にしないために。</h3><p>入会申込、会費徴収、名簿管理、学校との役割分担を、役員を責めずに点検します。</p><span class="home-role-cta">役員向けガイドを読む →</span></a><a class="home-role-card" href="/guide-board.html"><span class="home-role-label">学校・教育委員会の方へ</span><h3>学校が協力できる範囲と、止めるべき範囲を分ける。</h3><p>名簿提供、学校徴収金、連絡ツール、教職員関与、施設利用を行政実務として整理します。</p><span class="home-role-cta">学校・教委向けガイドを読む →</span></a></div></div>';
    if(!document.getElementById('home-rebuilt-style')){
      var st=document.createElement('style');
      st.id='home-rebuilt-style';
      st.textContent='.home-reading-section{background:#fff!important;padding:76px 0 82px!important}.home-lead-wrap{max-width:1080px!important}.home-lead-prose{max-width:900px;margin:22px 0 34px}.home-lead-prose p{font-size:1rem;line-height:2.05;color:var(--text);margin:0 0 16px}.home-role-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px;margin-top:30px}.home-role-card{display:block;text-decoration:none;color:inherit;background:#fff;border:1px solid var(--line);border-radius:18px;padding:24px 24px 22px;box-shadow:var(--shadow-sm);transition:transform .18s,box-shadow .18s,border-color .18s}.home-role-card:hover{transform:translateY(-4px);box-shadow:var(--shadow-md);border-color:var(--gold)}.home-role-label{display:inline-flex;margin-bottom:13px;padding:4px 11px;border-radius:999px;background:rgba(212,175,55,.16);border:1px solid rgba(212,175,55,.34);color:#7a5c00;font-size:.72rem;font-weight:900;letter-spacing:.04em}.home-role-card h3{font-family:"Noto Serif JP",serif;color:var(--navy);font-size:1.08rem;line-height:1.55;margin:0 0 10px}.home-role-card p{font-size:.9rem;line-height:1.85;color:var(--text-soft);margin:0 0 16px}.home-role-cta{font-size:.85rem;font-weight:900;color:var(--navy)}@media(max-width:860px){.home-role-grid{grid-template-columns:1fr}.home-lead-prose p{font-size:.96rem}}';
      document.head.appendChild(st);
    }
  }

  function pdfLinks(){
    var cards=document.querySelectorAll('.parent-page .pdf-section .pdf-card');
    var ac='https://'+'acrobat'+'.'+'adobe'+'.'+'com/id/urn:aaid:sc:AP:';
    var pdfs=[ac+'ee52fff6-21cc-40c0-a631-bb9eafbca8c9',ac+'688231f9-f89a-45c4-a4c4-d29c85583a8b',ac+'36bed320-9ba2-4b4d-84fc-f90522a29e5b'];
    cards.forEach(function(card,i){var a=card.querySelector('a.pdf-btn');if(a&&pdfs[i]){a.href=pdfs[i];a.target='_blank';a.rel='noopener';a.textContent='PDF';}});
  }

  function improveParentBoardResponseIntro(){
    if(!location.pathname.endsWith('/guide-parent.html'))return;
    var note=document.querySelector('.parent-board-response-jump .pbr-note, .parent-board-response-jump .pbr-goodnote');
    if(!note)return;
    note.className='pbr-goodnote';
    note.dataset.rewritten='1';
    note.innerHTML='<p>ここで見てほしいのは、単に「回答がある」ということではありません。各地の教育委員会が、PTA加入・会費徴収・学校協力について、法令上の整理を示している点です。</p><p><strong>兵庫県西脇市の回答例。</strong>西脇市は、PTAは任意加入団体であり、入会には保護者の明確な申込みとPTAの承諾が必要で、意思確認をしない「みなし入会」では契約成立と判断できないと回答しています。つまり、入学しただけで自動的にPTA会員になる、断らなければ加入したものと扱う、という運用は、この考え方とは合いません。</p><p><strong>利根町の回答例。</strong>利根町は、PTA加入について、学校から説明し、書面等による保護者の意思表示を確認し、PTAの承諾によって入会契約が成立すると整理しています。さらに、PTA運営に法令違反が懸念される場合には、学校施設の提供や学校による会費徴収への協力を停止することもあり得る、という趣旨の回答をしています。</p><blockquote>法令違反が懸念されるときは、学校による施設提供や会費徴収への協力を停止する措置を講ずることもあることを伝え、指導、助言を行っていきたいと考えております。</blockquote><p>これは、PTAが法令どおりに運営されない場合、学校や教育委員会の協力は当然に続くものではない、という重要な意味を持ちます。</p>';
    var top=note.closest('.pbr-top');
    if(top && top.parentNode && note.parentNode!==top.parentNode){
      top.insertAdjacentElement('afterend', note);
    }
    if(!document.getElementById('pbr-goodnote-style')){
      var st=document.createElement('style');
      st.id='pbr-goodnote-style';
      st.textContent='.pbr-goodnote{display:block;width:100%;max-width:none;box-sizing:border-box;margin:4px 0 28px;padding:0;border:0;background:transparent;color:var(--text);font-size:.98rem;line-height:1.95}.pbr-goodnote p{max-width:none;margin:0 0 12px;color:var(--text)}.pbr-goodnote p:last-child{margin-bottom:0;font-weight:700;color:var(--navy)}.pbr-goodnote blockquote{margin:14px 0 16px;padding:14px 18px;border-left:5px solid var(--gold);background:#fffaf0;color:var(--navy);font-family:"Noto Serif JP",serif;font-weight:700;line-height:1.9}';
      document.head.appendChild(st);
    }
  }

  function parentGuideConsultationBottom(){
    if(!location.pathname.endsWith('/guide-parent.html'))return;
    var soudan=document.getElementById('soudan');
    var main=document.querySelector('main');
    if(soudan&&main&&soudan.parentNode===main){main.appendChild(soudan);}
  }

  function loadArchiveNotice(){
    if(!location.pathname.endsWith('/national-archive.html'))return;
    var x=document.createElement('script');x.src='/js/archive-notice.js?v=1';document.head.appendChild(x);
  }

  function local(){
    normalizeNavigation();
    normalizeLegacyLinks();
    rebuildHomeReadingSection();
    pdfLinks();
    improveParentBoardResponseIntro();
    parentGuideConsultationBottom();
    loadArchiveNotice();
  }

  var s=document.createElement('script');
  s.src='/js/site-v48-original.js?v=48';
  s.onload=function(){
    if(document.readyState==='loading'){
      document.addEventListener('DOMContentLoaded',function(){baseInit();local();},{once:true});
    }else{
      baseInit();local();
    }
  };
  s.onerror=function(){local();};
  document.head.appendChild(s);
})();