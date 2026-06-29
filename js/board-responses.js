/* board-responses.js — 地方別索引 + 分類別回答本文 + 概略地図（公開用マスキング版） */
(function () {
  'use strict';
  const DATA = window.PTA_BOARD_RESPONSE_INDEX || {};
  const REGIONS = [
    { id: 'hokkaido-tohoku', name: '北海道・東北', prefs: ['北海道','青森県','岩手県','宮城県','秋田県','山形県','福島県'] },
    { id: 'kanto', name: '関東', prefs: ['茨城県','栃木県','群馬県','埼玉県','千葉県','東京都','神奈川県'] },
    { id: 'chubu', name: '中部', prefs: ['新潟県','富山県','石川県','福井県','山梨県','長野県','岐阜県','静岡県','愛知県','三重県'] },
    { id: 'kinki', name: '近畿', prefs: ['滋賀県','京都府','大阪府','兵庫県','奈良県','和歌山県'] },
    { id: 'chugoku-shikoku', name: '中国・四国', prefs: ['鳥取県','島根県','岡山県','広島県','山口県','徳島県','香川県','愛媛県','高知県'] },
    { id: 'kyushu', name: '九州・沖縄', prefs: ['福岡県','佐賀県','長崎県','熊本県','大分県','宮崎県','鹿児島県','沖縄県'] }
  ];
  function esc(s) { return String(s ?? '').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&#039;'); }
  function ansId(no) { return 'ans-' + no; }
  function getRegionId(pref) { for (const r of REGIONS) if (r.prefs.includes(pref)) return r.id; return 'other'; }
  function injectPrivacyMarker() {
    if (document.getElementById('board-response-privacy-style')) return;
    const style = document.createElement('style');
    style.id = 'board-response-privacy-style';
    style.textContent = '.source-note{font-size:.78rem;color:var(--text-soft);margin-top:8px}.response-tags{display:flex;flex-wrap:wrap;gap:6px;margin:8px 0 10px}.response-tags span{font-size:.72rem;font-weight:800;color:#1e3a5f;background:#f4f7fb;border:1px solid #dbe4ee;border-radius:999px;padding:2px 8px}.mask-chip{display:inline-block;margin-left:.5em;color:#614500;background:#fff4c7;border:1px solid #ead88a;border-radius:999px;padding:1px 7px;font-size:.72rem;font-family:\'Noto Sans JP\',sans-serif;font-weight:900}.excluded-response-list{font-size:.88rem;line-height:1.8}.excluded-response-list li{margin-bottom:.45rem}.manual-map-pin-layer{display:none!important}';
    document.head.appendChild(style);
  }
  function renderIndex() {
    const el = document.getElementById('regionIndex'); if (!el) return;
    const tree = {};
    for (const m of DATA.municipalities || []) {
      const pref = m.prefecture || '不明'; const rid = getRegionId(pref);
      if (!tree[rid]) tree[rid] = {}; if (!tree[rid][pref]) tree[rid][pref] = []; tree[rid][pref].push(m);
    }
    let html = '';
    for (const region of REGIONS) {
      const prefs = tree[region.id]; if (!prefs || !Object.keys(prefs).length) continue;
      html += `<section class="region-block" data-region="${esc(region.id)}"><h3 class="region-heading">${esc(region.name)}</h3>`;
      for (const pref of Object.keys(prefs).sort()) {
        const list = prefs[pref].slice().sort((a,b)=>a.no-b.no);
        html += `<div class="prefecture-group"><h4 class="pref-heading">${esc(pref)}</h4><ul class="municipality-list">`;
        for (const m of list) html += `<li><a href="#${ansId(m.no)}" class="muni-link">${esc(m.municipality)}${m.detailCount>1?`<span class="muni-count">${m.detailCount}件</span>`:''}</a></li>`;
        html += '</ul></div>';
      }
      html += '</section>';
    }
    const other = tree.other;
    if (other) {
      html += '<section class="region-block" data-region="other"><h3 class="region-heading">その他・都道府県未分類</h3><ul class="municipality-list">';
      for (const [, list] of Object.entries(other)) for (const m of list.sort((a,b)=>a.no-b.no)) html += `<li><a href="#${ansId(m.no)}" class="muni-link">${esc(m.municipality)}</a></li>`;
      html += '</ul></section>';
    }
    el.innerHTML = html;
  }
  function renderBodies() {
    const el = document.getElementById('responseBodiesContent'); if (!el) return;
    const details = DATA.details || []; const typeMap = DATA.typeMap || {}; const TYPES = ['A','C'];
    let html = '';
    for (const type of TYPES) {
      const list = details.filter(d => d.type === type); if (!list.length) continue;
      const info = typeMap[type] || {};
      html += `<section class="type-section" id="type-${esc(type)}"><h3 class="type-heading"><span class="type-label-badge">${esc(type)}</span>${esc(info.title || type)}</h3>`;
      for (const d of list.sort((a,b)=>a.no-b.no)) {
        const tags = (DATA.municipalities || []).find(m => m.no === d.no)?.usefulTags || [];
        html += `<article id="${ansId(d.no)}" class="response-item"><h4 class="response-muni-name">${esc(d.municipality)}<span class="mask-chip">マスキング済</span></h4>`;
        html += `<p class="response-meta">分類：${esc(d.typeLabel || type)} ／ 回答日：${esc(d.date || '未確認')} ／ 本文取得：${esc(d.extractNote || '')}</p>`;
        if (tags.length) html += `<div class="response-tags">${tags.map(t=>`<span>${esc(t.label)}</span>`).join('')}</div>`;
        html += `<details><summary>回答本文を読む</summary><div class="response-body">${esc(d.body || '回答本文未掲載。原資料または関連ファイルで確認が必要です。')}</div>`;
        html += `<p class="source-note">原本ファイル：${esc(d.sourceFile || '未確認')} ／ 文字数：${esc(d.chars || '')}字 ／ メールアドレス・電話番号・所在地・個人宛名等は公開用に省略しています。</p></details>`;
        html += `<p class="back-to-index"><a href="#municipality-index">▲ 自治体索引へ戻る</a></p></article>`;
      }
      html += '</section>';
    }
    el.innerHTML = html;
  }
  function renderExcluded() {
    const el = document.getElementById('excludedResponses'); if (!el) return;
    const rows = DATA.excluded || [];
    el.innerHTML = `<ul class="excluded-response-list">${rows.map(x=>`<li><strong>No.${esc(x.no)} ${esc(x.name)}</strong> — ${esc(x.reason)}<br><span>原本：${esc(x.file || '未確認')}</span></li>`).join('')}</ul>`;
  }
  function initMap() {
    const el = document.getElementById('responseMap'); if (!el || typeof L === 'undefined') return;
    const map = L.map('responseMap', { scrollWheelZoom:false }).setView([36.2,138.2],5);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{ attribution:'&copy; OpenStreetMap contributors' }).addTo(map);
    const group = L.featureGroup();
    for (const m of DATA.municipalities || []) {
      if (!Array.isArray(m.coordinates)) continue;
      const marker = L.circleMarker(m.coordinates,{ radius:7,color:'#1e3a5f',fillColor:'#d4af37',fillOpacity:.88,weight:2 });
      marker.bindTooltip(`<strong>${esc(m.municipality)}</strong><br><small>概略位置・クリックで本文へ</small>`,{permanent:false,direction:'top',offset:[0,-8]});
      marker.on('click',()=>{ const target=document.getElementById(ansId(m.no)); if(!target) return; target.scrollIntoView({behavior:'smooth',block:'start'}); const det=target.querySelector('details'); if(det&&!det.open) det.open=true; });
      marker.addTo(map); group.addLayer(marker);
    }
    if (group.getLayers().length) map.fitBounds(group.getBounds().pad(0.12));
  }
  function initSearch() {
    const input = document.getElementById('muniSearch'); if (!input) return;
    input.addEventListener('input', function(){ const q=this.value.trim(); document.querySelectorAll('.muni-link').forEach(a=>{ const li=a.parentElement; if(li) li.style.display=(!q || a.textContent.includes(q))?'':'none'; }); document.querySelectorAll('.prefecture-group').forEach(pg=>{ const vis=[...pg.querySelectorAll('li')].some(li=>li.style.display!=='none'); pg.style.display=vis?'':'none'; }); document.querySelectorAll('.region-block').forEach(rb=>{ const vis=[...rb.querySelectorAll('li')].some(li=>li.style.display!=='none'); rb.style.display=vis?'':'none'; }); });
  }
  document.addEventListener('DOMContentLoaded', function(){ injectPrivacyMarker(); renderIndex(); renderBodies(); renderExcluded(); initMap(); initSearch(); });
})();
