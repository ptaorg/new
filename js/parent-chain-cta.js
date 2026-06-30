(function(){
  function ready(fn){
    if(document.readyState === 'loading') document.addEventListener('DOMContentLoaded', fn, {once:true});
    else fn();
  }
  ready(function(){
    var path = location.pathname.replace(/\/+$/, '');
    if(!/\/guide-parent\.html$/.test(path) && path !== '/guide-parent') return;
    if(document.getElementById('pac-parent-top-link')) return;
    var lead = document.getElementById('parent-lead');
    if(!lead || !lead.parentNode) return;
    var style = document.createElement('style');
    style.id = 'pac-parent-top-link-style';
    style.textContent = '#pac-parent-top-link{background:#fff7ed;border-top:1px solid rgba(15,39,71,.06);border-bottom:1px solid rgba(15,39,71,.08);padding:34px 0}#pac-parent-top-link .pacx-wrap{width:min(calc(100% - 40px),900px);margin:0 auto;background:#fff;border:1px solid rgba(15,39,71,.14);border-left:7px solid #b91c1c;border-radius:0 18px 18px 0;box-shadow:0 10px 28px rgba(5,17,31,.09);padding:24px 26px}#pac-parent-top-link .pacx-badge{display:inline-flex;padding:4px 11px;border-radius:999px;background:rgba(185,28,28,.09);color:#b91c1c;font-size:.72rem;font-weight:900;letter-spacing:.08em;margin-bottom:10px}#pac-parent-top-link h2{font-family:"Noto Serif JP",serif;color:#0f2747;font-size:clamp(1.25rem,2.3vw,1.75rem);line-height:1.45;margin:0 0 10px}#pac-parent-top-link p{color:#334155;font-size:.96rem;line-height:1.9;margin:0 0 16px}#pac-parent-top-link .pacx-actions{display:flex;flex-wrap:wrap;gap:10px}#pac-parent-top-link .pacx-actions a{display:inline-flex;align-items:center;justify-content:center;text-decoration:none;border-radius:999px;font-weight:900;font-size:.88rem;padding:9px 15px}#pac-parent-top-link .pacx-main{background:#d4af37;color:#0f2747}#pac-parent-top-link .pacx-sub{background:#f8fafc;color:#0f2747;border:1px solid #dbe4ee}@media(max-width:760px){#pac-parent-top-link{padding:26px 0}#pac-parent-top-link .pacx-wrap{width:min(calc(100% - 28px),900px);padding:22px 18px}}';
    document.head.appendChild(style);
    var section = document.createElement('section');
    section.id = 'pac-parent-top-link';
    section.innerHTML = '<div class="pacx-wrap"><div class="pacx-badge">保護者向け確認ページ</div><h2>入会申込書がないまま会員扱いされていませんか</h2><p>入会申込書がない場合、会員資格、会費徴収、学校名簿の利用、教職員関与、学校施設利用まで根拠が連鎖的に不安定になります。学校・PTA・教育委員会へ確認するための文例も用意しました。</p><div class="pacx-actions"><a class="pacx-main" href="/pta-application-chain.html">入会申込書がないと何が崩れるのかを見る</a><a class="pacx-sub" href="/pta-application-chain-action-kit.html">確認シートをPDF保存する</a></div></div>';
    lead.parentNode.insertBefore(section, lead.nextSibling);
  });
})();
