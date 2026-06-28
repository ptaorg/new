/* site.js v88 — static body preservation
   重要本文はHTML側を正とし、JavaScriptは補助機能だけを担当する。 */
(function(){
  var initialPath = location.pathname + location.search;
  var allowAutoTop = !location.hash;

  try {
    if ('scrollRestoration' in history) history.scrollRestoration = 'manual';
  } catch (e) {}

  function ready(fn) {
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', fn, { once: true });
    else fn();
  }

  function addStyle(id, css) {
    var style = document.getElementById(id);
    if (!style) {
      style = document.createElement('style');
      style.id = id;
      document.head.appendChild(style);
    }
    style.textContent = css;
  }

  function loadCss(id, href) {
    if (document.getElementById(id)) return;
    var link = document.createElement('link');
    link.id = id;
    link.rel = 'stylesheet';
    link.href = href;
    document.head.appendChild(link);
  }

  function loadScript(id, src, callback) {
    var old = document.getElementById(id);
    if (old) {
      if (old.dataset.loaded === '1') {
        if (callback) callback();
      } else if (callback) {
        old.addEventListener('load', callback, { once: true });
      }
      return;
    }
    var script = document.createElement('script');
    script.id = id;
    script.src = src;
    script.onload = function(){
      script.dataset.loaded = '1';
      if (callback) callback();
    };
    document.head.appendChild(script);
  }

  function forceTop() {
    if (!allowAutoTop) return;
    try { window.scrollTo({ top: 0, left: 0, behavior: 'auto' }); }
    catch (e) { try { window.scrollTo(0, 0); } catch (_) {} }
  }

  function forceTopBurst(ms) {
    var end = Date.now() + ms;
    forceTop();
    var timer = setInterval(function(){
      if (!allowAutoTop || Date.now() > end) {
        clearInterval(timer);
        return;
      }
      forceTop();
    }, 120);
  }

  ['wheel', 'touchstart', 'keydown', 'mousedown'].forEach(function(ev){
    window.addEventListener(ev, function(){ allowAutoTop = false; }, { once: true, passive: true });
  });

  function scrollToHashTarget() {
    if (!location.hash) return;
    var id = location.hash.slice(1);
    try { id = decodeURIComponent(id); } catch (e) {}
    if (!id) return;
    var el = document.getElementById(id);
    if (!el) return;
    var parentDetails = el.closest && el.closest('details');
    if (parentDetails) parentDetails.open = true;
    if (el.tagName && el.tagName.toLowerCase() === 'details') el.open = true;
    allowAutoTop = false;
    var header = document.querySelector('.site-header, .nav-container');
    var offset = (header ? header.getBoundingClientRect().height : 0) + 18;
    var y = el.getBoundingClientRect().top + (window.pageYOffset || document.documentElement.scrollTop || 0) - offset;
    try { window.scrollTo({ top: Math.max(0, y), left: 0, behavior: 'auto' }); }
    catch (e) { try { window.scrollTo(0, Math.max(0, y)); } catch (_) {} }
  }

  function scheduleHashScroll() {
    if (!location.hash) return;
    [0, 80, 260, 700, 1400].forEach(function(ms){
      setTimeout(scrollToHashTarget, ms);
    });
  }

  window.addEventListener('hashchange', function(){
    allowAutoTop = false;
    scheduleHashScroll();
  }, { passive: true });

  window.addEventListener('pageshow', function(){
    if (!location.hash && (location.pathname + location.search) === initialPath) forceTopBurst(1200);
  });

  var SITE_INDEX = [
    ['トップ', '/index.html', 'PTA適正化推進委員会の全体像'],
    ['資料入口・索引', '/documents.html', '公開資料への入口'],
    ['保護者の方へ', '/guide-parent.html', '入会した覚えがない・会費の根拠が分からない場合の確認手順'],
    ['PTA役員の方へ', '/guide-pta.html', '引き継いだ運営を適法に直す実務手順'],
    ['学校・教育委員会の方へ', '/guide-board.html', '確認すべき領域と初動チェック'],
    ['研究者・記者の方へ', '/guide-research.html', '調査・取材のための資料案内'],
    ['教委向け分離指針', '/edu-board-separation.html', '学校とPTAの線引き'],
    ['適正化とは', '/proper-management.html', 'PTA適正化の基本原則'],
    ['適正化ガイドライン', '/guideline.html', '実務ガイドラインと書式テンプレート'],
    ['入会手続とオプトアウト', '/membership.html', '入会申込書・同意・みなし加入'],
    ['個人情報提供の問題', '/privacy.html', '学校名簿のPTA提供と個人情報保護法'],
    ['会費徴収と学校徴収金', '/fee-collection.html', '抱合せ徴収・代行徴収・公会計化'],
    ['教職員関与と職務専念義務', '/personnel.html', '地方公務員法第35条と職専免'],
    ['施設利用と公私の境界', '/facilities.html', '学校教育法第137条と目的外使用許可'],
    ['法制度マップ', '/law-map.html', '関連法令を論点別に整理'],
    ['判例整理', '/cases.html', 'PTA関連裁判例の争点整理'],
    ['PTA制度史', '/timeline.html', '制度変遷の整理'],
    ['教育委員会の回答', '/board-responses.html', '自治体別・論点別の公式回答データベース'],
    ['全国資料館', '/national-archive.html', '自治体別・学校別の実物文書アーカイブ'],
    ['行政通知・公式PDF', '/administrative-materials.html', '行政通知・公式資料'],
    ['横浜市教育委員会通知 学教第1965号', '/journal/yokohama-notice-1965.html', '任意加入・個人情報・会費説明の中核資料'],
    ['提出文書キット', '/submission-kit.html', '学校・PTA・教育委員会への確認文'],
    ['主張と根拠の対応表', '/claim-evidence-ledger.html', '主張、根拠条文、公式資料、提出文例の対応'],
    ['PTAと消費者契約法', '/journal/consumer-contract.html', 'PTA加入・会費請求と消費者契約法'],
    ['PTAオプトアウト加入の無効性', '/journal/optout-invalidity.html', '退会届方式・みなし加入の整理'],
    ['PTA非会員情報・協力金', '/journal/nonmember-info.html', '非会員名簿、協力金、学校情報利用'],
    ['学校徴収金とPTA会費', '/journal/school-fee-separation.html', '学校徴収金と任意団体会費の分離'],
    ['第三者提供同意とPTA名簿', '/journal/third-party-consent.html', '学校書類内のPTA個人情報同意'],
    ['働き方改革とPTA会費代理徴収', '/journal/work-style-reform.html', '学校事務とPTA会費の分離'],
    ['PTA運営の現場実例', '/compliance.html', 'みなし加入・代行徴収・名簿提供の実例'],
    ['静岡市個人情報事案', '/shizuoka-incident.html', '個人情報漏えい事案の整理'],
    ['論考・調査報告', '/journal.html', '個別テーマの掘り下げ'],
    ['総合分析レポート', '/report.html', 'PTA問題の構造分析'],
    ['なぜ教育委員会の所掌なのか', '/education-board-responsibility.html', '学校関与を点検すべき理由'],
    ['運営チェックアプリ', '/audit/index.html', '自校・自PTAのセルフチェック'],
    ['お問い合わせ・情報提供', '/contact.html', '資料・情報提供窓口'],
    ['応援・寄付', '/support.html', '活動支援のお願い']
  ];

  function initSearch() {
    document.querySelectorAll('.header-search').forEach(function(box){
      var input = box.querySelector('.search-input');
      var dropdown = box.querySelector('.search-results-dropdown');
      if (!input || !dropdown || input.dataset.searchReady === '1') return;
      input.dataset.searchReady = '1';
      input.addEventListener('input', function(){
        var q = input.value.trim().toLowerCase();
        dropdown.innerHTML = '';
        if (!q) {
          dropdown.classList.remove('is-open');
          return;
        }
        var hits = SITE_INDEX.filter(function(row){
          return (row[0] + ' ' + row[1] + ' ' + row[2]).toLowerCase().indexOf(q) >= 0;
        }).slice(0, 8);
        if (!hits.length) {
          dropdown.innerHTML = '<div class="search-result-item srd-empty"><strong>該当なし</strong><span>別の語で検索してください。</span></div>';
        } else {
          hits.forEach(function(row){
            dropdown.insertAdjacentHTML('beforeend', '<a class="search-result-item srd-item" href="' + row[1] + '"><strong class="srd-item-title">' + row[0] + '</strong><span class="srd-item-desc">' + row[2] + '</span></a>');
          });
        }
        dropdown.classList.add('is-open');
      });
      document.addEventListener('click', function(e){
        if (!box.contains(e.target)) dropdown.classList.remove('is-open');
      });
    });
  }

  function mobileNavHtml() {
    return [
      '<button type="button" class="mobile-close-btn" id="closeOverlay" aria-label="メニューを閉じる">閉じる ×</button>',
      '<div class="mobile-menu-group">',
      '<div class="mobile-menu-label">主要入口</div>',
      '<a class="mobile-link" href="/index.html">トップ</a>',
      '<a class="mobile-link" href="/guide-parent.html">保護者の方へ</a>',
      '<a class="mobile-link" href="/guide-pta.html">PTA役員の方へ</a>',
      '<a class="mobile-link" href="/guide-board.html">教育委員会・学校へ</a>',
      '</div>',
      '<div class="mobile-menu-group">',
      '<div class="mobile-menu-label">資料・論考</div>',
      '<a class="mobile-link" href="/board-responses.html">教育委員会の回答</a>',
      '<a class="mobile-link" href="/national-archive.html">全国資料館</a>',
      '<a class="mobile-link" href="/administrative-materials.html">行政通知・公式PDF</a>',
      '<a class="mobile-link" href="/documents.html">資料入口・索引</a>',
      '<a class="mobile-link" href="/journal.html">論考・調査報告</a>',
      '</div>',
      '<div class="mobile-menu-group">',
      '<div class="mobile-menu-label">論点</div>',
      '<a class="mobile-link" href="/membership.html">入会手続</a>',
      '<a class="mobile-link" href="/privacy.html">個人情報</a>',
      '<a class="mobile-link" href="/fee-collection.html">会費徴収</a>',
      '<a class="mobile-link" href="/personnel.html">教職員関与</a>',
      '<a class="mobile-link" href="/facilities.html">施設利用</a>',
      '</div>',
      '<div class="mobile-menu-group mobile-menu-bottom">',
      '<a class="mobile-link" href="/audit/index.html">運営チェックアプリ</a>',
      '<a class="mobile-link" href="/contact.html">お問い合わせ・情報提供</a>',
      '<a class="mobile-link support-mobile-link" href="/support.html">応援・寄付</a>',
      '</div>'
    ].join('');
  }

  function stabilizeMobileNavigation() {
    var hamburger = document.getElementById('hamburger');
    var overlay = document.getElementById('mobileOverlay');
    if (!hamburger || !overlay || hamburger.dataset.stableMobileNav === 'v88') return;

    addStyle('mobile-nav-stable-v88',
      'html.mobile-nav-lock-root{overflow:hidden!important;overscroll-behavior:none!important}' +
      'body.mobile-nav-lock{position:fixed!important;left:0;right:0;width:100%;overflow:hidden!important;touch-action:none!important}' +
      '.mobile-overlay{position:fixed!important;inset:0!important;z-index:5000!important;display:none!important;flex-direction:column!important;justify-content:flex-start!important;align-items:center!important;gap:10px!important;padding:calc(18px + env(safe-area-inset-top)) 16px calc(24px + env(safe-area-inset-bottom))!important;background:rgba(5,17,31,.92)!important;backdrop-filter:blur(10px)!important;-webkit-backdrop-filter:blur(10px)!important;overflow-y:auto!important;overscroll-behavior:contain!important;-webkit-overflow-scrolling:touch!important}' +
      '.mobile-overlay.is-open{display:flex!important;opacity:1!important;visibility:visible!important;pointer-events:auto!important}' +
      '.mobile-menu-group{width:min(100%,430px);display:flex;flex-direction:column;gap:8px;margin:0 0 8px!important}' +
      '.mobile-menu-label{color:rgba(255,255,255,.55);font-size:.72rem;font-weight:900;letter-spacing:.1em;text-transform:uppercase;margin:5px 4px}' +
      '.mobile-link{width:100%!important;background:rgba(255,255,255,.97)!important;border-radius:14px!important;padding:14px 18px!important;text-decoration:none!important;color:var(--navy,#1e3a5f)!important;font-weight:800!important;box-shadow:0 6px 20px rgba(0,0,0,.14)!important}' +
      '.mobile-close-btn{width:min(100%,430px);min-height:44px;border:1px solid rgba(255,255,255,.35);border-radius:999px;background:rgba(255,255,255,.1);color:#fff;font-weight:900;cursor:pointer}'
    );

    var newHamburger = hamburger.cloneNode(true);
    var newOverlay = overlay.cloneNode(false);
    hamburger.parentNode.replaceChild(newHamburger, hamburger);
    overlay.parentNode.replaceChild(newOverlay, overlay);
    newOverlay.id = 'mobileOverlay';
    newOverlay.className = 'mobile-overlay';
    newOverlay.setAttribute('aria-hidden', 'true');
    newOverlay.innerHTML = mobileNavHtml();
    newHamburger.dataset.stableMobileNav = 'v88';
    newOverlay.dataset.stableMobileNav = 'v88';
    newHamburger.setAttribute('aria-controls', 'mobileOverlay');
    newHamburger.setAttribute('aria-expanded', 'false');
    newHamburger.setAttribute('aria-label', 'メニューを開く');

    var savedY = 0;
    function openMenu() {
      savedY = window.scrollY || window.pageYOffset || 0;
      allowAutoTop = false;
      newOverlay.classList.add('is-open');
      newHamburger.classList.add('is-active');
      newHamburger.setAttribute('aria-expanded', 'true');
      newHamburger.setAttribute('aria-label', 'メニューを閉じる');
      newOverlay.setAttribute('aria-hidden', 'false');
      document.body.style.top = '-' + savedY + 'px';
      document.documentElement.classList.add('mobile-nav-lock-root');
      document.body.classList.add('mobile-nav-lock');
      setTimeout(function(){
        var close = newOverlay.querySelector('#closeOverlay');
        if (close && close.focus) close.focus({ preventScroll: true });
      }, 0);
    }
    function closeMenu() {
      var locked = document.body.classList.contains('mobile-nav-lock');
      newOverlay.classList.remove('is-open');
      newHamburger.classList.remove('is-active');
      newHamburger.setAttribute('aria-expanded', 'false');
      newHamburger.setAttribute('aria-label', 'メニューを開く');
      newOverlay.setAttribute('aria-hidden', 'true');
      document.body.classList.remove('mobile-nav-lock');
      document.documentElement.classList.remove('mobile-nav-lock-root');
      document.body.style.top = '';
      if (locked) {
        try { window.scrollTo(0, savedY); } catch (e) {}
      }
    }
    newHamburger.addEventListener('click', function(e){
      e.preventDefault();
      e.stopPropagation();
      if (newOverlay.classList.contains('is-open')) closeMenu();
      else openMenu();
    });
    newOverlay.addEventListener('click', function(e){
      if (e.target === newOverlay || e.target.id === 'closeOverlay' || (e.target.closest && e.target.closest('a.mobile-link'))) closeMenu();
    });
    document.addEventListener('keydown', function(e){
      if (e.key === 'Escape' && newOverlay.classList.contains('is-open')) closeMenu();
    });
    window.addEventListener('resize', function(){
      if (window.innerWidth > 860 && newOverlay.classList.contains('is-open')) closeMenu();
    }, { passive: true });
  }

  function normalizeNavigation() {
    var desktop = document.querySelector('.desktop-nav');
    if (!desktop || desktop.dataset.normalized === 'v88') return;
    desktop.dataset.normalized = 'v88';
    desktop.innerHTML = '<a class="nav-link" href="/index.html">トップ</a>' +
      '<div class="nav-item has-dropdown"><a class="nav-link" href="/guide-parent.html">立場別</a><div class="mega-menu"><div class="mega-col"><h4>立場別</h4><ul><li><a href="/guide-parent.html">保護者の方へ</a></li><li><a href="/guide-pta.html">PTA役員の方へ</a></li><li><a href="/guide-board.html">教育委員会・学校の方へ</a></li><li><a href="/guide-research.html">研究者・記者の方へ</a></li></ul></div></div></div>' +
      '<div class="nav-item has-dropdown"><a class="nav-link" href="/documents.html">資料・データ</a><div class="mega-menu"><div class="mega-col"><h4>一次資料</h4><ul><li><a href="/board-responses.html">教育委員会の回答</a></li><li><a href="/national-archive.html">全国資料館</a></li><li><a href="/administrative-materials.html">行政通知・公式PDF</a></li><li><a href="/compliance.html">PTA運営の現場実例</a></li></ul></div><div class="mega-col"><h4>配布資料・索引</h4><ul><li><a href="/documents.html">資料入口・索引</a></li><li><a href="/guide-board.html#board-jp-guideline">教委向け分離資料</a></li><li><a href="/PTA運営適正化ガイドブック_第4版_改訂本文.html">適正化ガイドブック 第4版</a></li></ul></div></div></div>' +
      '<div class="nav-item has-dropdown"><a class="nav-link" href="/journal.html">研究</a><div class="mega-menu"><div class="mega-col"><h4>論考・整理</h4><ul><li><a href="/journal.html">論考・調査報告</a></li><li><a href="/report.html">総合分析レポート</a></li><li><a href="/law-map.html">法制度マップ</a></li><li><a href="/cases.html">判例整理</a></li><li><a href="/timeline.html">PTA制度史</a></li></ul></div><div class="mega-col"><h4>論点別</h4><ul><li><a href="/membership.html">入会手続</a></li><li><a href="/privacy.html">個人情報</a></li><li><a href="/fee-collection.html">会費徴収</a></li><li><a href="/personnel.html">教職員関与</a></li><li><a href="/facilities.html">施設利用</a></li></ul></div></div></div>' +
      '<div class="nav-item has-dropdown"><a class="nav-link" href="/audit/index.html">ツール</a><div class="mega-menu"><div class="mega-col"><h4>点検用</h4><ul><li><a href="/audit/index.html">運営チェックアプリ</a></li><li><a href="/guideline.html">適正化ガイドライン</a></li><li><a href="/edu-board-separation.html">教委向け分離指針</a></li></ul></div></div></div>' +
      '<a class="nav-link support-nav-link" href="/support.html">応援</a>';
  }

  function normalizeLinks() {
    document.querySelectorAll('a[href]').forEach(function(a){
      var href = a.getAttribute('href');
      if (!href) return;
      if (href === '/donate/' || href === 'donate/' || href === 'https://ptaorg.com/donate/') a.setAttribute('href', '/support.html');
      if (href === '/jp/' || href === 'jp/' || href === 'https://ptaorg.com/jp/') a.setAttribute('href', '/guide-board.html#board-jp-guideline');
      if (href === 'https://ptaorg.github.io/ed/' || href === 'https://ptaorg.github.io/ed') a.setAttribute('href', 'https://ptaorg.com/ed');
    });
  }

  function fixGuidePta() {
    if (!location.pathname.endsWith('/guide-pta.html')) return;
    var main = document.querySelector('main');
    if (main) {
      main.style.display = 'block';
      main.style.width = '100%';
      main.style.maxWidth = 'none';
    }
    var guide = document.getElementById('guidebook-text');
    if (guide && main && main.firstElementChild !== guide) main.insertBefore(guide, main.firstElementChild);
    addStyle('guide-pta-layout-v88',
      'body:has(#guidebook-text) main{display:block!important;width:100%!important;max-width:none!important}' +
      '#guidebook-text{display:block!important;position:static!important;float:none!important;clear:both!important;width:100%!important;max-width:none!important;margin:0!important;padding:56px 0 44px!important;background:transparent!important;border:0!important;border-radius:0!important;box-shadow:none!important}' +
      '#guidebook-text>.wrap{display:block!important;float:none!important;position:static!important;width:min(calc(100% - 40px),860px)!important;max-width:860px!important;margin-left:auto!important;margin-right:auto!important;padding-left:0!important;padding-right:0!important;background:transparent!important;border:0!important;border-radius:0!important;box-shadow:none!important}' +
      '.gb-chapter,.gb-chapter-accordion,.gb-chapter-summary{box-shadow:none!important}'
    );
  }

  function pdfLinks() {
    var cards = document.querySelectorAll('.parent-page .pdf-section .pdf-card');
    var pdfs = ['/assets/pdf/pta-membership-inquiry.pdf', '/assets/pdf/pta-withdrawal-notice.pdf', '/assets/pdf/personal-data-deletion-request.pdf'];
    cards.forEach(function(card, i){
      var link = card.querySelector('a.pdf-btn');
      if (link && pdfs[i]) {
        link.href = pdfs[i];
        link.removeAttribute('target');
        link.removeAttribute('rel');
        link.textContent = 'PDFを開く';
      }
    });
  }

  var TRIP_LOCATIONS = [
    {name:'札幌市',lat:43.0621,lng:141.3544},{name:'仙台市',lat:38.2682,lng:140.8694},{name:'いわき市',lat:37.0504,lng:140.8877},{name:'須賀川市',lat:37.2865,lng:140.3734},{name:'潮来市',lat:35.9344,lng:140.5453},{name:'久喜市',lat:36.0621,lng:139.6672},{name:'埼玉県',lat:35.8574,lng:139.6489},{name:'川口市',lat:35.8079,lng:139.7238},{name:'幸手市',lat:36.0747,lng:139.7247},{name:'越谷市',lat:35.8911,lng:139.7911},{name:'三鷹市',lat:35.6836,lng:139.5594},{name:'墨田区',lat:35.7129,lng:139.8015},{name:'江戸川区',lat:35.6783,lng:139.8711},{name:'足立区',lat:35.7750,lng:139.8044},{name:'厚木市',lat:35.4431,lng:139.3622},{name:'川崎市',lat:35.5302,lng:139.7029},{name:'海老名市',lat:35.4461,lng:139.3917},{name:'相模原市',lat:35.5714,lng:139.3736},{name:'神奈川県',lat:35.4478,lng:139.6425},{name:'茅ヶ崎市',lat:35.3323,lng:139.4061},{name:'静岡市',lat:34.9756,lng:138.3828},{name:'名古屋市',lat:35.1815,lng:136.9066},{name:'大津市',lat:35.0178,lng:135.8547},{name:'京都市',lat:35.0116,lng:135.7681},{name:'大阪市',lat:34.6937,lng:135.5023},{name:'岡山市',lat:34.6551,lng:133.9196},{name:'広島市',lat:34.3853,lng:132.4553},{name:'徳島市',lat:34.0711,lng:134.5517},{name:'北九州市',lat:33.8833,lng:130.8833},{name:'長崎市',lat:32.7503,lng:129.8777},{name:'熊本市',lat:32.8031,lng:130.7078},{name:'鹿児島市',lat:31.5967,lng:130.5572}
  ];

  function initHomeMap() {
    var p = location.pathname;
    if (!(p === '/' || p.endsWith('/index.html'))) return;
    var el = document.getElementById('homeEvidenceMap');
    if (!el || el.dataset.initialized === '1') return;
    el.dataset.initialized = '1';
    loadCss('leaflet-css-dynamic', 'https://unpkg.com/leaflet@1.9.4/dist/leaflet.css');
    function draw() {
      if (!window.L) return;
      function icon(color) {
        return L.icon({
          iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-' + color + '.png',
          shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/images/marker-shadow.png',
          iconSize: [13, 21], iconAnchor: [6.5, 21], popupAnchor: [0, -20], shadowSize: [21, 21]
        });
      }
      var map = L.map(el, { scrollWheelZoom: false }).setView([36.2, 138.2], 5);
      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', { attribution: '&copy; OpenStreetMap contributors' }).addTo(map);
      var group = L.featureGroup();
      var blue = icon('blue');
      var red = icon('red');
      var data = window.PTA_BOARD_RESPONSE_INDEX || {};
      var munis = data.municipalities || [];
      var blueNames = {};
      munis.forEach(function(m){
        if (!Array.isArray(m.coordinates)) return;
        blueNames[m.municipality] = true;
        var marker = L.marker(m.coordinates, { icon: blue, title: m.municipality }).addTo(map)
          .bindPopup('<strong>' + m.municipality + '</strong><br><small>教育委員会回答</small><br><a href="/board-responses.html#ans-' + m.no + '">回答本文へ</a>');
        group.addLayer(marker);
      });
      TRIP_LOCATIONS.forEach(function(loc){
        var lng = blueNames[loc.name] ? loc.lng + 0.035 : loc.lng;
        var marker = L.marker([loc.lat, lng], { icon: red, title: loc.name, zIndexOffset: 250 }).addTo(map)
          .bindPopup('<strong>' + loc.name + '</strong><br><small>資料取得・訪問先</small>');
        group.addLayer(marker);
      });
      if (group.getLayers().length) map.fitBounds(group.getBounds().pad(0.08));
    }
    function loadDataThenMap() {
      if (window.PTA_BOARD_RESPONSE_INDEX) draw();
      else loadScript('board-response-data-dynamic', '/data/board-responses-index.js', draw);
    }
    if (window.L) loadDataThenMap();
    else loadScript('leaflet-js-dynamic', 'https://unpkg.com/leaflet@1.9.4/dist/leaflet.js', loadDataThenMap);
  }

  function loadArchiveNotice() {
    if (location.pathname.endsWith('/national-archive.html')) loadScript('archive-notice-dynamic', '/js/archive-notice.js?v=1');
  }

  function initFAQ() {
    document.querySelectorAll('.faq-item .faq-q').forEach(function(q){
      if (q.dataset.faqReady === '1') return;
      q.dataset.faqReady = '1';
      q.addEventListener('click', function(){
        var item = q.closest('.faq-item');
        if (item) item.classList.toggle('is-open');
      });
    });
  }

  function boot() {
    normalizeNavigation();
    stabilizeMobileNavigation();
    normalizeLinks();
    initSearch();
    initFAQ();
    fixGuidePta();
    pdfLinks();
    loadArchiveNotice();
    initHomeMap();
    if (location.hash) scheduleHashScroll();
    else forceTopBurst(1000);
  }

  window.initSearch = initSearch;
  window.initMobileNav = stabilizeMobileNavigation;
  window.initPrimaryNavigation = function(){ normalizeNavigation(); stabilizeMobileNavigation(); };

  ready(function(){
    boot();
    setTimeout(stabilizeMobileNavigation, 80);
    setTimeout(function(){
      if (location.hash) scheduleHashScroll();
    }, 300);
  });
})();
