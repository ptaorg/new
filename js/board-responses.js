/* board-responses.js — 公開用マスキング版：索引・本文・地図 */
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
  const REGION_BY_ID = Object.fromEntries(REGIONS.map(r => [r.id, r]));
  let miniMap = null;
  let miniMapLayer = null;

  function esc(s) {
    return String(s ?? '')
      .replace(/&/g,'&amp;').replace(/</g,'&lt;')
      .replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&#039;');
  }
  function ansId(no) { return 'ans-' + no; }
  function getRegionId(pref) {
    for (const r of REGIONS) if (r.prefs.includes(pref)) return r.id;
    return 'other';
  }
  function getRegionMunicipalities(regionId) {
    return (DATA.municipalities || []).filter(m => getRegionId(m.prefecture || '') === regionId);
  }
  function createPinIcon() {
    return L.divIcon({
      className: 'response-pin-wrap',
      html: '<span class="response-pin-marker"></span>',
      iconSize: [18, 26],
      iconAnchor: [9, 24],
      popupAnchor: [0, -18],
      tooltipAnchor: [0, -16]
    });
  }

  function injectMapStyles() {
    if (document.getElementById('board-response-pin-style')) return;
    const style = document.createElement('style');
    style.id = 'board-response-pin-style';
    style.textContent = `
      .source-note{font-size:.78rem;color:var(--text-soft);margin-top:8px}
      .response-tags{display:flex;flex-wrap:wrap;gap:6px;margin:8px 0 10px}
      .response-tags span{font-size:.72rem;font-weight:800;color:#1e3a5f;background:#f4f7fb;border:1px solid #dbe4ee;border-radius:999px;padding:2px 8px}
      .mask-chip{display:inline-block;margin-left:.5em;color:#614500;background:#fff4c7;border:1px solid #ead88a;border-radius:999px;padding:1px 7px;font-size:.72rem;font-family:'Noto Sans JP',sans-serif;font-weight:900}
      .excluded-response-list{font-size:.88rem;line-height:1.8}
      .excluded-response-list li{margin-bottom:.6rem}
      .response-pin-wrap{background:transparent!important;border:none!important}
      .response-pin-marker{display:block;width:14px;height:14px;border-radius:50% 50% 50% 0;background:#d93025;border:2px solid #fff;box-shadow:0 1px 5px rgba(0,0,0,.28);transform:rotate(-45deg)}
      .response-pin-marker::after{content:'';position:absolute;width:4px;height:4px;border-radius:50%;background:#fff;left:3px;top:3px}
      .manual-map-pin-layer{display:none!important}
    `;
    document.head.appendChild(style);
  }

  function renderIndex() {
    const el = document.getElementById('regionIndex');
    if (!el) return;

    const tree = {};
    for (const m of DATA.municipalities || []) {
      const pref = m.prefecture || '不明';
      const rid = getRegionId(pref);
      if (!tree[rid]) tree[rid] = {};
      if (!tree[rid][pref]) tree[rid][pref] = [];
      tree[rid][pref].push(m);
    }

    let html = '';
    for (const region of REGIONS) {
      const prefs = tree[region.id];
      if (!prefs || !Object.keys(prefs).length) continue;
      html += `<section class="region-block" data-region="${esc(region.id)}">`;
      html += `<h3 class="region-heading" data-region-id="${esc(region.id)}">${esc(region.name)}</h3>`;
      for (const pref of Object.keys(prefs).sort()) {
        const list = prefs[pref].slice().sort((a,b)=>a.no-b.no);
        html += `<div class="prefecture-group"><h4 class="pref-heading">${esc(pref)}</h4><ul class="municipality-list">`;
        for (const m of list) {
          const badge = m.detailCount > 1 ? `<span class="muni-count">${m.detailCount}件</span>` : '';
          html += `<li><a href="#${ansId(m.no)}" class="muni-link" data-region-id="${esc(region.id)}">${esc(m.municipality)}${badge}</a></li>`;
        }
        html += `</ul></div>`;
      }
      html += `</section>`;
    }
    el.innerHTML = html;

    el.querySelectorAll('.region-heading').forEach(function (heading) {
      heading.addEventListener('click', function () {
        setActiveRegion(this.getAttribute('data-region-id'));
      });
    });
    el.querySelectorAll('.muni-link').forEach(function (link) {
      link.addEventListener('mouseenter', function () {
        setActiveRegion(this.getAttribute('data-region-id'));
      });
      link.addEventListener('focus', function () {
        setActiveRegion(this.getAttribute('data-region-id'));
      });
    });
  }

  function renderBodies() {
    const el = document.getElementById('responseBodiesContent');
    if (!el) return;

    const details = DATA.details || [];
    const typeMap = DATA.typeMap || {};
    const munis = DATA.municipalities || [];
    const muniByName = {};
    for (const m of munis) muniByName[m.municipality] = m;

    const byType = {};
    for (const d of details) {
      if (!byType[d.type]) byType[d.type] = [];
      byType[d.type].push(d);
    }

    const types = Object.keys(typeMap).sort();
    let html = '';
    const anchored = new Set();

    for (const type of types) {
      const items = (byType[type] || []).slice().sort((a,b) => {
        const na = muniByName[a.municipality]?.no || 9999;
        const nb = muniByName[b.municipality]?.no || 9999;
        return na - nb;
      });
      if (!items.length) continue;

      const info = typeMap[type] || {};
      html += `<section class="type-section" id="type-${esc(type)}">`;
      html += `<h3 class="type-heading"><span class="type-label-badge">${esc(type)}</span>${esc(info.title || type)}</h3>`;

      for (const d of items) {
        const muni = muniByName[d.municipality] || {};
        const no = muni.no;
        const idAttr = no && !anchored.has(no) ? ` id="${ansId(no)}"` : '';
        if (no) anchored.add(no);
        const tags = (muni.usefulTags || []).map(t => `<span>${esc(t.label)}</span>`).join('');
        const flags = (muni.qualityFlags || []).map(f => f.key === 'masked' ? `<span class="mask-chip">${esc(f.label)}</span>` : '').join('');
        html += `<article class="response-item"${idAttr}>`;
        html += `<h4 class="response-muni-name">${esc(d.municipality)}${flags}</h4>`;
        html += `<p class="response-meta">分類：${esc(d.typeLabel || type)} ／ 回答日：${esc(d.date || '未確認')}</p>`;
        if (tags) html += `<div class="response-tags">${tags}</div>`;
        html += `<details><summary>回答本文を読む</summary><div class="response-body">${esc(d.body || '回答本文未掲載。')}</div></details>`;
        if (d.sourceFile) html += `<p class="source-note">元資料：${esc(d.sourceFile)}</p>`;
        html += `<p class="back-to-index"><a href="#municipality-index">▲ 自治体索引へ戻る</a></p>`;
        html += `</article>`;
      }
      html += `</section>`;
    }
    el.innerHTML = html;
  }

  function renderExcluded() {
    const el = document.getElementById('excludedResponses');
    if (!el) return;
    const excluded = DATA.excluded || [];
    if (!excluded.length) {
      el.innerHTML = '<p>掲載対象から外した資料はありません。</p>';
      return;
    }
    const items = excluded.map(item => {
      const reason = item.reason ? ` — ${esc(item.reason)}` : '';
      const source = item.sourceFile ? ` <small>（${esc(item.sourceFile)}）</small>` : '';
      return `<li><strong>${esc(item.municipality || '名称未確認')}</strong>${reason}${source}</li>`;
    }).join('');
    el.innerHTML = `<ul class="excluded-response-list">${items}</ul>`;
  }

  function initMainMap() {
    const el = document.getElementById('responseMap');
    if (!el || typeof L === 'undefined') return;
    const map = L.map('responseMap', { scrollWheelZoom: false }).setView([36.2, 138.2], 5);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; OpenStreetMap contributors'
    }).addTo(map);

    const group = L.featureGroup();
    const pinIcon = createPinIcon();
    for (const m of DATA.municipalities || []) {
      if (!Array.isArray(m.coordinates)) continue;
      const marker = L.marker(m.coordinates, { icon: pinIcon, keyboard: false });
      marker.bindTooltip(`<strong>${esc(m.municipality)}</strong><br><small>クリックで回答本文へ</small>`, {
        permanent: false, direction: 'top', offset: [0, -16]
      });
      marker.on('click', function () {
        const target = document.getElementById(ansId(m.no));
        if (!target) return;
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        const det = target.querySelector('details');
        if (det && !det.open) det.open = true;
      });
      marker.addTo(map);
      group.addLayer(marker);
    }
    if (group.getLayers().length) map.fitBounds(group.getBounds().pad(0.12));
  }

  function buildRegionSelector() {
    const el = document.getElementById('regionSelector');
    if (!el) return;
    el.innerHTML = REGIONS.map(r => `<button type="button" class="region-chip" data-region-id="${esc(r.id)}">${esc(r.name)}</button>`).join('');
    el.querySelectorAll('.region-chip').forEach(function (btn) {
      btn.addEventListener('click', function () {
        setActiveRegion(this.getAttribute('data-region-id'));
      });
    });
  }

  function initMiniMap() {
    const el = document.getElementById('regionMiniMap');
    if (!el || typeof L === 'undefined') return;
    miniMap = L.map('regionMiniMap', { scrollWheelZoom: false, zoomControl: true }).setView([36.2, 138.2], 5);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; OpenStreetMap contributors'
    }).addTo(miniMap);
    miniMapLayer = L.featureGroup().addTo(miniMap);
    setActiveRegion(REGIONS[0].id);
  }

  function setActiveRegion(regionId) {
    if (!regionId || !miniMap || !miniMapLayer) return;
    document.querySelectorAll('.region-chip').forEach(function (btn) {
      btn.classList.toggle('is-active', btn.getAttribute('data-region-id') === regionId);
    });
    document.querySelectorAll('.region-heading').forEach(function (heading) {
      heading.style.color = heading.getAttribute('data-region-id') === regionId ? 'var(--orange)' : 'var(--navy)';
    });

    miniMapLayer.clearLayers();
    const pinIcon = createPinIcon();
    const munis = getRegionMunicipalities(regionId);
    const caption = document.getElementById('regionMiniMapCaption');
    const region = REGION_BY_ID[regionId];

    for (const m of munis) {
      if (!Array.isArray(m.coordinates)) continue;
      const marker = L.marker(m.coordinates, { icon: pinIcon, keyboard: false });
      marker.bindTooltip(esc(m.municipality), { direction: 'top', offset: [0, -16] });
      marker.on('click', function () {
        const target = document.getElementById(ansId(m.no));
        if (!target) return;
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        const det = target.querySelector('details');
        if (det && !det.open) det.open = true;
      });
      marker.addTo(miniMapLayer);
    }

    if (miniMapLayer.getLayers().length) {
      miniMap.fitBounds(miniMapLayer.getBounds().pad(0.18));
    } else {
      miniMap.setView([36.2, 138.2], 4);
    }
    if (caption) {
      caption.textContent = region
        ? `${region.name}に含まれる掲載自治体 ${munis.length} 件を表示しています。ピンをクリックすると本文へ移動します。`
        : '地方を選択してください。';
    }
    setTimeout(() => miniMap.invalidateSize(), 0);
  }

  function initSearch() {
    const input = document.getElementById('muniSearch');
    if (!input) return;
    input.addEventListener('input', function () {
      const q = this.value.trim();
      document.querySelectorAll('.muni-link').forEach(function (a) {
        const li = a.parentElement;
        if (li) li.style.display = (!q || a.textContent.includes(q)) ? '' : 'none';
      });
      document.querySelectorAll('.prefecture-group').forEach(function (pg) {
        const visible = [...pg.querySelectorAll('li')].some(li => li.style.display !== 'none');
        pg.style.display = visible ? '' : 'none';
      });
      document.querySelectorAll('.region-block').forEach(function (rb) {
        const visible = [...rb.querySelectorAll('li')].some(li => li.style.display !== 'none');
        rb.style.display = visible ? '' : 'none';
      });
    });
  }

  document.addEventListener('DOMContentLoaded', function () {
    injectMapStyles();
    renderIndex();
    renderBodies();
    renderExcluded();
    buildRegionSelector();
    initMainMap();
    initMiniMap();
    initSearch();
  });
})();
