/* PTA適正化推進委員会 — site.js v50 wrapper */
document.write('<script src="/js/site-v48-original.js?v=48"><\/script>');
document.addEventListener('DOMContentLoaded',function(){
  var cards=document.querySelectorAll('.parent-page .pdf-section .pdf-card');
  var pdfs=['/assets/pdf/pta-membership-inquiry.pdf','/assets/pdf/pta-withdrawal-notice.pdf','/assets/pdf/personal-data-deletion-request.pdf'];
  cards.forEach(function(card,i){var a=card.querySelector('a.pdf-btn');if(a&&pdfs[i]){a.href=pdfs[i];a.removeAttribute('target');a.removeAttribute('rel');a.textContent='PDFを開く';}});
  if(location.pathname==='/'||location.pathname.endsWith('/index.html')){
    var title=document.getElementById('home-reading-title');
    if(title&&!document.querySelector('.home-role-entry-injected')){
      var st=document.createElement('style');
      st.textContent='.home-role-entry-injected{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px;margin:26px 0 34px}.home-role-entry-card{display:block;text-decoration:none;color:inherit;background:#fff;border:1px solid #d8e0ea;border-radius:16px;padding:22px;box-shadow:0 10px 28px rgba(5,17,31,.08)}.home-role-entry-card:hover{border-color:var(--gold);box-shadow:0 16px 38px rgba(5,17,31,.13);transform:translateY(-3px)}.home-role-entry-kicker{display:inline-flex;margin-bottom:10px;padding:3px 9px;border-radius:999px;background:rgba(212,175,55,.15);border:1px solid rgba(212,175,55,.35);color:#7a5c00;font-size:.68rem;font-weight:900}.home-role-entry-card h3{font-family:"Noto Serif JP",serif;color:var(--navy);font-size:1.04rem;line-height:1.45;margin:0 0 8px}.home-role-entry-card p{color:var(--text-soft);font-size:.86rem;line-height:1.82;margin:0 0 14px}.home-role-entry-cta{color:var(--navy);font-size:.82rem;font-weight:900}@media(max-width:820px){.home-role-entry-injected{grid-template-columns:1fr}}';
      document.head.appendChild(st);
      var block=document.createElement('div');
      block.className='home-role-entry-injected';
      block.setAttribute('aria-label','立場別入り口');
      block.innerHTML='<a class="home-role-entry-card" href="/guide-parent.html"><span class="home-role-entry-kicker">保護者</span><h3>保護者の方へ</h3><p>入会・退会・会費・個人情報について、まず何を確認するかを整理します。</p><span class="home-role-entry-cta">保護者向けガイドへ →</span></a><a class="home-role-entry-card" href="/guide-pta.html"><span class="home-role-entry-kicker">PTA役員</span><h3>PTA役員の方へ</h3><p>入会記録、会費徴収、個人情報、学校との分離を実務として点検します。</p><span class="home-role-entry-cta">役員向けガイドへ →</span></a><a class="home-role-entry-card" href="/guide-board.html"><span class="home-role-entry-kicker">学校・教育委員会</span><h3>教育委員会・学校の方へ</h3><p>名簿、徴収、配布、施設、教職員関与の範囲を確認します。</p><span class="home-role-entry-cta">学校・教委向けガイドへ →</span></a>';
      title.insertAdjacentElement('afterend',block);
    }
  }
});
