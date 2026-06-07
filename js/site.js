/* site.js v68 focused overlay */
(function(){
  try{ if('scrollRestoration' in history) history.scrollRestoration='manual'; }catch(e){}
  function keepTopUnlessHash(){
    if(location.hash) return;
    try{ window.scrollTo(0,0); }catch(e){}
    setTimeout(function(){ try{ if(!location.hash) window.scrollTo(0,0); }catch(e){} },80);
    setTimeout(function(){ try{ if(!location.hash) window.scrollTo(0,0); }catch(e){} },350);
    setTimeout(function(){ try{ if(!location.hash) window.scrollTo(0,0); }catch(e){} },900);
  }

  var TRIP_LOCATIONS=[
    {name:'札幌市',lat:43.0621,lng:141.3544},{name:'仙台市',lat:38.2682,lng:140.8694},{name:'いわき市',lat:37.0504,lng:140.8877},{name:'須賀川市',lat:37.2865,lng:140.3734},{name:'潮来市',lat:35.9344,lng:140.5453},{name:'久喜市',lat:36.0621,lng:139.6672},{name:'埼玉県',lat:35.8574,lng:139.6489},{name:'川口市',lat:35.8079,lng:139.7238},{name:'幸手市',lat:36.0747,lng:139.7247},{name:'越谷市',lat:35.8911,lng:139.7911},{name:'三鷹市',lat:35.6836,lng:139.5594},{name:'墨田区',lat:35.7129,lng:139.8015},{name:'江戸川区',lat:35.6783,lng:139.8711},{name:'足立区',lat:35.7750,lng:139.8044},{name:'厚木市',lat:35.4431,lng:139.3622},{name:'川崎市',lat:35.5302,lng:139.7029},{name:'海老名市',lat:35.4461,lng:139.3917},{name:'相模原市',lat:35.5714,lng:139.3736},{name:'神奈川県',lat:35.4478,lng:139.6425},{name:'茅ヶ崎市',lat:35.3323,lng:139.4061},{name:'長岡市',lat:37.4461,lng:138.8511},{name:'射水市',lat:36.7299,lng:137.0520},{name:'下諏訪町',lat:36.0728,lng:138.0877},{name:'各務原市',lat:35.4011,lng:136.8441},{name:'岐阜県',lat:35.3912,lng:136.7223},{name:'富士宮市',lat:35.2217,lng:138.6119},{name:'静岡市',lat:34.9756,lng:138.3828},{name:'一宮市',lat:35.3047,lng:136.7978},{name:'名古屋市',lat:35.1815,lng:136.9066},{name:'安城市',lat:34.9594,lng:137.0864},{name:'愛知県',lat:35.1802,lng:136.9066},{name:'愛西市',lat:35.1500,lng:136.7275},{name:'扶桑町',lat:35.3583,lng:136.9111},{name:'豊橋市',lat:34.7692,lng:137.3914},{name:'豊田市',lat:35.0825,lng:137.1561},{name:'長久手市',lat:35.1611,lng:137.0503},{name:'三重県',lat:34.7303,lng:136.5086},{name:'大津市',lat:35.0178,lng:135.8547},{name:'彦根市',lat:35.2744,lng:136.2597},{name:'甲賀市',lat:34.9656,lng:136.1692},{name:'野洲市',lat:35.1189,lng:136.0275},{name:'亀岡市',lat:35.0356,lng:135.5739},{name:'京都市',lat:35.0116,lng:135.7681},{name:'交野市',lat:34.7861,lng:135.6811},{name:'大阪市',lat:34.6937,lng:135.5023},{name:'枚方市',lat:34.8161,lng:135.6500},{name:'茨木市',lat:34.8164,lng:135.5683},{name:'高槻市',lat:34.8486,lng:135.6175},{name:'姫路市',lat:34.8150,lng:134.6853},{name:'岡山市',lat:34.6551,lng:133.9196},{name:'岡山県',lat:34.6618,lng:133.9350},{name:'広島市',lat:34.3853,lng:132.4553},{name:'徳島市',lat:34.0711,lng:134.5517},{name:'北九州市',lat:33.8833,lng:130.8833},{name:'宗像市',lat:33.8050,lng:130.5414},{name:'長崎市',lat:32.7503,lng:129.8777},{name:'熊本市',lat:32.8031,lng:130.7078},{name:'大分県',lat:33.2381,lng:131.6125},{name:'鹿児島市',lat:31.5967,lng:130.5572}
  ];

  function ready(fn){ if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',fn,{once:true}); else fn(); }
  function loadScript(id,src,cb){ var old=document.getElementById(id); if(old){ old.addEventListener('load',function(){cb&&cb();},{once:true}); if(old.dataset.loaded==='1')cb&&cb(); return; } var s=document.createElement('script'); s.id=id; s.src=src; s.onload=function(){s.dataset.loaded='1'; cb&&cb();}; document.head.appendChild(s); }
  function loadCss(id,href){ if(document.getElementById(id))return; var l=document.createElement('link'); l.id=id; l.rel='stylesheet'; l.href=href; document.head.appendChild(l); }
  function addStyle(id,css){ var st=document.getElementById(id); if(!st){ st=document.createElement('style'); st.id=id; document.head.appendChild(st); } st.textContent=css; }

  function baseInit(){
    ['addGlobalStyle','removeTopDonation','initPrimaryNavigation','initCompliancePageFixes','initParentCompliancePreview','initParentBoardResponsesPreview','initCommonFooter','initCompatibilityFixes','initMegaMenu','initMobileNav','initSearch','initFAQ','initChecklist','initPageClasses'].forEach(function(n){
      try{ if(typeof window[n]==='function')window[n](); }catch(e){ console.error('site init failed:',n,e); }
    });
  }

  function normalizeNavigation(){
    var supportUrl='/support.html';
    var d=document.querySelector('.desktop-nav');
    if(d){
      d.innerHTML='<a class="nav-link" href="/index.html">トップ</a><div class="nav-item has-dropdown"><a class="nav-link" href="#">立場別</a><div class="mega-menu"><div class="mega-col"><h4>立場別</h4><ul><li><a href="/guide-parent.html">保護者の方へ</a></li><li><a href="/guide-pta.html">PTA役員の方へ</a></li><li><a href="/guide-board.html">教育委員会・学校の方へ</a></li><li><a href="/guide-research.html">研究者・記者の方へ</a></li></ul></div></div></div><div class="nav-item has-dropdown"><a class="nav-link" href="#">資料・データ</a><div class="mega-menu"><div class="mega-col"><h4>一次資料</h4><ul><li><a href="/board-responses.html">教育委員会の回答</a></li><li><a href="/national-archive.html">全国資料館</a></li><li><a href="/administrative-materials.html">行政資料整理</a></li><li><a href="/compliance.html">PTA運営の現場実例</a></li></ul></div></div></div><div class="nav-item has-dropdown"><a class="nav-link" href="/journal.html">研究</a><div class="mega-menu"><div class="mega-col"><h4>論考・整理</h4><ul><li><a href="/guide-research.html">研究者・記者の方へ</a></li><li><a href="/journal.html">論考・調査報告</a></li><li><a href="/report.html">総合分析レポート</a></li><li><a href="/law-map.html">法制度マップ</a></li><li><a href="/cases.html">判例整理</a></li><li><a href="/timeline.html">PTA制度史</a></li></ul></div><div class="mega-col"><h4>論点別</h4><ul><li><a href="/membership.html">入会手続</a></li><li><a href="/privacy.html">個人情報</a></li><li><a href="/fee-collection.html">会費徴収</a></li><li><a href="/personnel.html">教職員関与</a></li><li><a href="/facilities.html">施設利用</a></li></ul></div></div></div><div class="nav-item has-dropdown"><a class="nav-link" href="#">ツール</a><div class="mega-menu"><div class="mega-col"><h4>点検用</h4><ul><li><a href="/audit/index.html">運営チェックアプリ</a></li><li><a href="/guideline.html">適正化ガイドライン</a></li></ul></div></div></div><a class="nav-link support-nav-link" href="'+supportUrl+'">応援</a>';
    }
    var m=document.getElementById('mobileOverlay');
    if(m){
      m.innerHTML='<a class="mobile-link" href="/index.html"><span>Top</span>トップ</a><a class="mobile-link" href="/guide-parent.html"><span>Parents</span>保護者の方へ</a><a class="mobile-link" href="/guide-pta.html"><span>PTA Board</span>PTA役員の方へ</a><a class="mobile-link" href="/guide-board.html"><span>School Board</span>教育委員会・学校へ</a><a class="mobile-link" href="/guide-research.html"><span>Research</span>研究者・記者の方へ</a><a class="mobile-link" href="/board-responses.html"><span>Data</span>教育委員会の回答</a><a class="mobile-link" href="/national-archive.html"><span>Archive</span>全国資料館</a><a class="mobile-link" href="/administrative-materials.html"><span>Materials</span>行政資料整理</a><a class="mobile-link" href="/compliance.html"><span>Examples</span>現場実例</a><a class="mobile-link" href="/journal.html"><span>Journal</span>論考・調査報告</a><a class="mobile-link" href="/audit/index.html"><span>Check</span>運営チェックアプリ</a><a class="mobile-link support-mobile-link" href="'+supportUrl+'"><span>Support</span>応援・寄付</a><div class="close-overlay" id="closeOverlay">CLOSE ×</div>';
    }
    try{ if(typeof window.initMegaMenu==='function')window.initMegaMenu(); }catch(e){}
  }

  function normalizeLegacyLinks(){
    document.querySelectorAll('a[href]').forEach(function(a){
      var h=a.getAttribute('href'); if(!h)return;
      if(h==='/donate/'||h==='donate/'||h==='https://ptaorg.com/donate/'||h==='https://ptaorg.github.io/donate/'||h==='https://ptaorg.github.io/donate')a.setAttribute('href','/support.html');
      if(h==='https://ptaorg.github.io/ed/'||h==='https://ptaorg.github.io/ed')a.setAttribute('href','https://ptaorg.com/ed');
    });
  }

  function rebuildHomeReadingSection(){
    var p=location.pathname; if(!(p==='/'||p.endsWith('/index.html')))return;
    var s=document.querySelector('.home-reading-section'); if(!s||s.dataset.rebuilt==='1')return; s.dataset.rebuilt='1';
    addStyle('home-custom-style-v68','.home-reading-section{background:#fff!important;padding:76px 0 82px!important}.home-lead-wrap{max-width:1080px!important}.home-lead-prose{max-width:900px;margin:22px 0 24px}.home-lead-prose p{font-size:1rem;line-height:2.05;color:var(--text);margin:0 0 16px}.home-activity-note{margin:26px 0 24px;padding:22px 24px;border-left:6px solid var(--gold);background:#fffdf4;border-radius:0 14px 14px 0;line-height:1.95}.home-evidence-map-block{margin:28px 0 36px;padding:22px;background:#f8fafc;border:1px solid var(--line);border-radius:18px}.evidence-map{height:420px;border:1px solid var(--line);border-radius:14px;background:#e5e7eb;overflow:hidden}.map-legend{display:flex;flex-wrap:wrap;gap:14px;margin-top:12px;color:var(--text-soft);font-size:.84rem}.map-legend span{display:inline-flex;align-items:center;gap:6px}.map-legend i{display:inline-block;width:10px;height:10px;border-radius:50%}.map-legend .blue i{background:#1d4ed8}.map-legend .red i{background:#b91c1c}.map-more-link{display:inline-flex;margin-top:14px;color:var(--navy);font-size:.86rem;font-weight:900;text-decoration:none;border-bottom:2px solid var(--gold)}.home-role-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px;margin-top:30px}.home-role-card{display:block;text-decoration:none;color:inherit;background:#fff;border:1px solid var(--line);border-radius:18px;padding:24px;box-shadow:var(--shadow-sm);transition:.18s}.home-role-card:hover{transform:translateY(-4px);box-shadow:var(--shadow-md);border-color:var(--gold)}.home-role-label{display:inline-flex;margin-bottom:13px;padding:4px 11px;border-radius:999px;background:rgba(212,175,55,.16);border:1px solid rgba(212,175,55,.34);color:#7a5c00;font-size:.72rem;font-weight:900}.home-role-card h3{font-family:"Noto Serif JP",serif;color:var(--navy);font-size:1.08rem;line-height:1.55;margin:0 0 10px}.home-role-card p{font-size:.9rem;line-height:1.85;color:var(--text-soft);margin:0 0 16px}.home-role-cta{font-size:.85rem;font-weight:900;color:var(--navy)}@media(max-width:860px){.home-role-grid{grid-template-columns:1fr}.evidence-map{height:340px}}');
    s.innerHTML='<div class="wrap home-lead-wrap"><div class="section-kicker">はじめに</div><h2 class="section-title" id="home-reading-title">PTAを「学校の一部」として扱わないために。</h2><div class="home-lead-prose"><p>PTAは、保護者と教職員が任意に参加する民間の任意団体です。学校教育を支える活動であっても、入会、会費、名簿、役員選出、連絡、会計処理は、学校の手続とは分けて考える必要があります。</p><p>問題は、PTAが存在することそのものではありません。入学や進級の手続、学校徴収金、学校の名簿、学校連絡ツール、教職員の勤務時間の中にPTAの事務が溶け込み、保護者が「任意加入であること」「断れること」「会費を支払う根拠」を確認できなくなることです。</p><p>このサイトでは、保護者、PTA役員、学校・教育委員会のそれぞれの立場から、どこを確認し、どのように公私の境界を整えるべきかを、一次資料と法令に基づいて整理しています。</p></div><div class="home-activity-note"><p>当委員会は、全国の教育委員会にPTA運営の法的見解を照会し、回答を収集・整理しています。</p><p>あわせて、公文書開示請求により、全国の学校・教育委員会から数千校分規模のPTA関連書類を取得しています。</p><p>得られた回答と資料をもとに教育委員会へ是正を求め、横浜市では市内全500校でPTA入退会自由を前提とする扱いを実現しました。</p></div><div class="home-evidence-map-block"><h3>照会回答・公文書開示請求マップ</h3><p>青は教育委員会から回答を得ている自治体、赤は公文書開示請求を行い、必要に応じて教育委員会へ直接出向いている自治体です。</p><div class="evidence-map" id="homeEvidenceMap"></div><div class="map-legend"><span class="blue"><i></i>教育委員会回答</span><span class="red"><i></i>公文書開示請求・訪問先</span></div><a class="map-more-link" href="/board-responses.html">回答本文を見る →</a></div><div class="home-role-grid"><a class="home-role-card" href="/guide-parent.html"><span class="home-role-label">保護者の方へ</span><h3>入会した覚えがない、会費を止めたい、断ると子どもが心配。</h3><p>入会意思、会費徴収、個人情報、役員選出のどこを確認すればよいかを整理します。</p><span class="home-role-cta">保護者向けガイドを読む →</span></a><a class="home-role-card" href="/guide-pta.html"><span class="home-role-label">PTA役員の方へ</span><h3>善意の活動を、強制や不透明な運営にしないために。</h3><p>入会申込、会費徴収、名簿管理、学校との役割分担を点検します。</p><span class="home-role-cta">役員向けガイドを読む →</span></a><a class="home-role-card" href="/guide-board.html"><span class="home-role-label">学校・教育委員会の方へ</span><h3>学校が協力できる範囲と、止めるべき範囲を分ける。</h3><p>名簿提供、学校徴収金、連絡ツール、教職員関与、施設利用を行政実務として整理します。</p><span class="home-role-cta">学校・教委向けガイドを読む →</span></a></div></div>';
  }

  function replaceHomeFieldcase(){
    var p=location.pathname; if(!(p==='/'||p.endsWith('/index.html')))return;
    var s=document.querySelector('.fieldcase-section'); if(!s||s.dataset.complianceRebuilt==='1')return; s.dataset.complianceRebuilt='1';
    addStyle('home-compliance-style-v68','.fieldcase-section{background:linear-gradient(135deg,#fefce8 0%,#fef9c3 100%)!important;padding:82px 0!important}.home-compliance-wrap{display:grid;grid-template-columns:minmax(0,.88fr) minmax(0,1.12fr);gap:34px;align-items:center}.home-compliance-copy{text-align:left}.home-compliance-copy p{font-size:.98rem;line-height:2;color:#274766;margin:0 0 15px}.home-compliance-button{display:inline-flex;margin-top:12px;padding:13px 24px;border-radius:999px;background:#b91c1c;color:#fff;text-decoration:none;font-weight:900}.home-compliance-live{display:block;background:#f8fafc;border:1px solid rgba(12,45,82,.16);border-radius:16px;overflow:hidden;text-decoration:none;color:inherit;box-shadow:0 12px 34px rgba(12,45,82,.14)}.mini-case{padding:24px;background:linear-gradient(180deg,#f8fafc,#fff)}.mini-case h3{font-family:"Noto Serif JP",serif;color:var(--navy);font-size:1.55rem;margin:0 0 8px}.mini-case .badge{display:inline-flex;margin-bottom:10px;padding:4px 10px;border-radius:999px;background:#eef2f7;color:var(--navy);font-size:.72rem;font-weight:900}.mini-case p{font-size:.78rem;line-height:1.75;color:#334155;margin:0 0 14px}.mini-case-grid{display:grid;grid-template-columns:.9fr 1.1fr;gap:16px}.mini-case-figs{display:grid;gap:10px}.mini-case-fig{background:#fff;border:1px solid #d9e2ef;border-radius:8px;overflow:hidden}.mini-case-fig img{display:block;width:100%;height:auto}.mini-case-caption{padding:7px 8px;font-size:.62rem;line-height:1.55;color:#475569}.mini-case-panel{display:grid;gap:12px}.mini-box{background:#fff;border:1px solid #d9e2ef;border-radius:14px;padding:14px}.mini-box h4{font-size:.9rem;color:var(--navy);margin:0 0 8px}.mini-box ul{margin:0;padding-left:16px;color:#334155;font-size:.76rem;line-height:1.8}.mini-strong{background:#fff5f5;border:1px solid #fca5a5;color:#991b1b;font-weight:900;font-size:.8rem;line-height:1.75;padding:12px}.mini-tags span{display:inline-flex;margin:3px;padding:4px 8px;border-radius:999px;background:#eff6ff;border:1px solid #bfdbfe;color:#1d4ed8;font-size:.68rem;font-weight:900}@media(max-width:860px){.home-compliance-wrap,.mini-case-grid{grid-template-columns:1fr}}');
    s.innerHTML='<div class="wrap home-compliance-wrap"><div class="home-compliance-copy"><div class="fieldcase-kicker">Field Examples — 現場実例</div><h2 class="fieldcase-title">PTA運営の現場実例</h2><p>このページは、全国の学校現場で見られるPTA運営上の典型的な問題を、実際の文書・通知・運用例をもとに整理するものです。</p><p>PTAは本来、保護者と教職員による任意加入の団体ですが、入学手続、学校徴収金、学校連絡、児童経由配布、役員選出、個人情報の利用などを通じて、学校とPTAの境界が曖昧になることがあります。</p><p>このページでは、特定の学校や個人を非難するのではなく、保護者・PTA役員・学校・教育委員会が確認すべき論点を整理します。</p><a class="home-compliance-button" href="/compliance.html">実例を見る →</a></div><a class="home-compliance-live" href="/compliance.html"><div class="mini-case"><span class="badge">Case 01</span><h3>みなし加入・全員加入扱い</h3><p>入会申込書や同意確認を経ないまま、保護者をPTA会員として扱う類型です。</p><div class="mini-case-grid"><div class="mini-case-figs"><div class="mini-case-fig"><img src="/assets/compliance/redacted/case-01-minashi-deemed-membership.png" alt="不提出をPTA入会扱いとする趣旨の実例資料"><div class="mini-case-caption">提出がない場合にPTA会員扱いとする趣旨の記載がある資料です。</div></div><div class="mini-case-fig"><img src="/assets/compliance/redacted/case-01-enrollment-equals-membership.png" alt="入学と同時にPTA加入とする趣旨の実例資料"><div class="mini-case-caption">入学とPTA加入を一体のものとして説明する構造が読み取れる資料です。</div></div></div><div class="mini-case-panel"><div class="mini-box"><h4>どこが問題か</h4><ul><li>入会申込書がない。</li><li>不提出を入会意思とみなしている。</li><li>学校徴収金の書類と同じ束に入っている。</li></ul></div><div class="mini-strong">入会申込や明確な承諾なしに会員として扱う運用は、PTA会員契約の成立を前提にできません。</div><div class="mini-box"><h4>関係する法令・制度</h4><p style="font-size:.76rem;line-height:1.75;margin:0 0 8px;color:#334155">契約は申込みと承諾によって成立します。</p><div class="mini-tags"><span>民法522条</span><span>憲法21条</span><span>消費者契約法4条</span></div></div></div></div></div></a></div>';
  }

  function fixGuidePtaTopLayout(){
    if(!location.pathname.endsWith('/guide-pta.html'))return;
    var main=document.querySelector('main'); if(main){ main.style.display='block'; main.style.width='100%'; main.style.maxWidth='none'; }
    var guide=document.getElementById('guidebook-text');
    var brief=document.querySelector('.editorial-brief.pta-editorial-brief');
    if(guide&&main&&main.firstElementChild!==guide)main.insertBefore(guide,main.firstElementChild);
    addStyle('guide-pta-layout-fix-v68','body:has(#guidebook-text) main{display:block!important;width:100%!important;max-width:none!important}#guidebook-text{display:block!important;position:static!important;float:none!important;clear:both!important;width:100%!important;max-width:none!important;margin:0!important;padding:56px 0 44px!important;background:transparent!important;border:0!important;border-radius:0!important;box-shadow:none!important}#guidebook-text>.wrap{display:block!important;float:none!important;position:static!important;width:min(calc(100% - 40px),860px)!important;max-width:860px!important;margin-left:auto!important;margin-right:auto!important;padding-left:0!important;padding-right:0!important;background:transparent!important;border:0!important;border-radius:0!important;box-shadow:none!important}.editorial-brief.pta-editorial-brief{display:block!important;position:static!important;float:none!important;clear:both!important;width:min(calc(100% - 40px),860px)!important;max-width:860px!important;margin:0 auto 54px!important;padding:0!important;background:transparent!important;border:0!important;border-radius:0!important;box-shadow:none!important;transform:none!important}.editorial-brief.pta-editorial-brief .editorial-brief-body{display:block!important;width:100%!important;background:transparent!important;border:0!important;border-radius:0!important;box-shadow:none!important;padding:0!important}.editorial-brief.pta-editorial-brief .editorial-brief-band{margin-left:0!important}.gb-chapter,.gb-chapter-accordion,.gb-chapter-summary{box-shadow:none!important}');
    if(guide){ guide.style.cssText += ';display:block!important;position:static!important;float:none!important;clear:both!important;width:100%!important;max-width:none!important;margin:0!important;padding:56px 0 44px!important;background:transparent!important;border:0!important;border-radius:0!important;box-shadow:none!important;'; var w=guide.querySelector(':scope > .wrap'); if(w){ w.style.cssText += ';display:block!important;position:static!important;float:none!important;width:min(calc(100% - 40px),860px)!important;max-width:860px!important;margin-left:auto!important;margin-right:auto!important;padding-left:0!important;padding-right:0!important;'; } }
    if(brief){ brief.style.cssText += ';display:block!important;position:static!important;float:none!important;clear:both!important;width:min(calc(100% - 40px),860px)!important;max-width:860px!important;margin:0 auto 54px!important;padding:0!important;background:transparent!important;border:0!important;border-radius:0!important;box-shadow:none!important;transform:none!important;'; var body=brief.querySelector('.editorial-brief-body'); if(body){ body.style.cssText += ';display:block!important;width:100%!important;background:transparent!important;border:0!important;border-radius:0!important;box-shadow:none!important;padding:0!important;'; } }
  }

  function improveParentBoardResponseIntro(){
    if(!location.pathname.endsWith('/guide-parent.html'))return;
    var note=document.querySelector('.parent-board-response-jump .pbr-note, .parent-board-response-jump .pbr-goodnote'); if(!note)return;
    note.className='pbr-goodnote';
    note.innerHTML='<p>ここで見てほしいのは、単に「回答がある」ということではありません。各地の教育委員会が、PTA加入・会費徴収・学校協力について、法令上の整理を示している点です。</p><p><strong>兵庫県西脇市の回答例。</strong>西脇市は、PTAは任意加入団体であり、入会には保護者の明確な申込みとPTAの承諾が必要で、意思確認をしない「みなし入会」では契約成立と判断できないと回答しています。</p><p><strong>利根町の回答例。</strong>利根町は、PTA加入について、学校から説明し、書面等による保護者の意思表示を確認し、PTAの承諾によって入会契約が成立すると整理しています。さらに、PTA運営に法令違反が懸念される場合には、学校施設の提供や学校による会費徴収への協力を停止することもあり得る、という趣旨の回答をしています。</p><blockquote>法令違反が懸念されるときは、学校による施設提供や会費徴収への協力を停止する措置を講ずることもあることを伝え、指導、助言を行っていきたいと考えております。</blockquote><p>これは、PTAが法令どおりに運営されない場合、学校や教育委員会の協力は当然に続くものではない、という重要な意味を持ちます。</p>';
    var top=note.closest('.pbr-top'); if(top&&top.parentNode&&note.parentNode!==top.parentNode)top.insertAdjacentElement('afterend',note);
  }

  function pdfLinks(){
    var cards=document.querySelectorAll('.parent-page .pdf-section .pdf-card');
    var ac='https://'+'acrobat'+'.'+'adobe'+'.'+'com/id/urn:aaid:sc:AP:';
    var pdfs=[ac+'ee52fff6-21cc-40c0-a631-bb9eafbca8c9',ac+'688231f9-f89a-45c4-a4c4-d29c85583a8b',ac+'36bed320-9ba2-4b4d-84fc-f90522a29e5b'];
    cards.forEach(function(card,i){var a=card.querySelector('a.pdf-btn'); if(a&&pdfs[i]){a.href=pdfs[i];a.target='_blank';a.rel='noopener';a.textContent='PDF';}});
  }

  function parentGuideConsultationBottom(){
    if(!location.pathname.endsWith('/guide-parent.html'))return;
    var soudan=document.getElementById('soudan'); var main=document.querySelector('main'); if(soudan&&main&&soudan.parentNode===main)main.appendChild(soudan);
  }

  function initHomeEvidenceMap(){
    var p=location.pathname; if(!(p==='/'||p.endsWith('/index.html')))return;
    var el=document.getElementById('homeEvidenceMap'); if(!el||el.dataset.initialized==='1')return; el.dataset.initialized='1';
    loadCss('leaflet-css-dynamic','https://unpkg.com/leaflet@1.9.4/dist/leaflet.css');
    function go(){
      if(!window.L)return;
      function icon(color){return L.icon({iconUrl:'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-'+color+'.png',shadowUrl:'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/images/marker-shadow.png',iconSize:[13,21],iconAnchor:[6.5,21],popupAnchor:[0,-20],shadowSize:[21,21]});}
      var map=L.map(el,{scrollWheelZoom:false}).setView([36.2,138.2],5);
      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{attribution:'&copy; OpenStreetMap contributors'}).addTo(map);
      var group=L.featureGroup(), blue=icon('blue'), red=icon('red'), data=window.PTA_BOARD_RESPONSE_INDEX||{}, munis=data.municipalities||[], blueNames={};
      munis.forEach(function(m){ if(!Array.isArray(m.coordinates))return; blueNames[m.municipality]=true; var mk=L.marker(m.coordinates,{icon:blue,title:m.municipality}).addTo(map).bindPopup('<strong>'+m.municipality+'</strong><br><small>教育委員会回答</small><br><a href="/board-responses.html#ans-'+m.no+'">回答本文へ</a>'); group.addLayer(mk); });
      TRIP_LOCATIONS.forEach(function(loc){ var lng=blueNames[loc.name]?loc.lng+0.035:loc.lng; var mk=L.marker([loc.lat,lng],{icon:red,title:loc.name,zIndexOffset:250}).addTo(map).bindPopup('<strong>'+loc.name+'</strong><br><small>公文書開示請求・訪問先</small>'); group.addLayer(mk); });
      if(group.getLayers().length)map.fitBounds(group.getBounds().pad(0.08));
      keepTopUnlessHash();
    }
    function ensureData(){ if(window.PTA_BOARD_RESPONSE_INDEX)go(); else loadScript('board-response-data-dynamic','/data/board-responses-index.js',go); }
    if(window.L)ensureData(); else loadScript('leaflet-js-dynamic','https://unpkg.com/leaflet@1.9.4/dist/leaflet.js',ensureData);
  }

  function loadArchiveNotice(){ if(location.pathname.endsWith('/national-archive.html'))loadScript('archive-notice-dynamic','/js/archive-notice.js?v=1'); }

  function local(){
    normalizeNavigation(); normalizeLegacyLinks(); rebuildHomeReadingSection(); replaceHomeFieldcase(); fixGuidePtaTopLayout(); pdfLinks(); improveParentBoardResponseIntro(); parentGuideConsultationBottom(); loadArchiveNotice(); initHomeEvidenceMap(); keepTopUnlessHash();
  }

  keepTopUnlessHash();
  var original=document.createElement('script');
  original.src='/js/site-v48-original.js?v=48';
  original.onload=function(){ ready(function(){ baseInit(); local(); setTimeout(fixGuidePtaTopLayout,250); setTimeout(keepTopUnlessHash,300); setTimeout(keepTopUnlessHash,1000); }); };
  original.onerror=function(){ ready(function(){ local(); setTimeout(fixGuidePtaTopLayout,250); setTimeout(keepTopUnlessHash,300); setTimeout(keepTopUnlessHash,1000); }); };
  document.head.appendChild(original);
})();
