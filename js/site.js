/* site.js v56 safe loader */
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

  function pdfLinks(){
    var cards=document.querySelectorAll('.parent-page .pdf-section .pdf-card');
    var ac='https://'+'acrobat'+'.'+'adobe'+'.'+'com/id/urn:aaid:sc:AP:';
    var pdfs=[ac+'ee52fff6-21cc-40c0-a631-bb9eafbca8c9',ac+'688231f9-f89a-45c4-a4c4-d29c85583a8b',ac+'36bed320-9ba2-4b4d-84fc-f90522a29e5b'];
    cards.forEach(function(card,i){var a=card.querySelector('a.pdf-btn');if(a&&pdfs[i]){a.href=pdfs[i];a.target='_blank';a.rel='noopener';a.textContent='PDF';}});
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
    pdfLinks();
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