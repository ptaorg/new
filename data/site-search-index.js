window.PTA_SITE_SEARCH_INDEX = [
  ["PTA適正化推進委員会", "/index.html", "一次資料・法令・行政回答にもとづき、PTAの任意加入、公私分離、個人情報、会費徴収を整理する資料サイトです。"],
  ["保護者の方へ", "/guide-parent.html", "入会した覚えがない・会費の根拠が分からない場合の確認手順"],
  ["入会申込書がないと何が崩れるのか", "/pta-application-chain.html", "入会申込書がない場合の会員資格・会費徴収・学校名簿・教職員関与・施設利用の連鎖構造と確認文例"],
  ["PTA確認シート・文例", "/pta-application-chain-action-kit.html", "学校・PTA・教育委員会へ確認する8項目とメール文例。印刷してPDF保存できます。"],
  ["PTA役員の方へ", "/guide-pta.html", "学校名簿に頼らない入会・会員管理、会費、個人情報、学校分離の実務手順"],
  ["教育委員会・学校へ", "/guide-board.html", "学校関与を点検するための確認事項"],
  ["PTA適正化とは", "/proper-management.html", "PTA適正化の基本原則"],
  ["入会手続", "/membership.html", "入会申込書・同意・みなし加入"],
  ["個人情報", "/privacy.html", "学校名簿のPTA提供と個人情報保護"],
  ["会費徴収", "/fee-collection.html", "抱合せ徴収・代行徴収・公会計化"],
  ["教職員関与", "/personnel.html", "地方公務員法第35条と職専免"],
  ["施設利用", "/facilities.html", "学校教育法第137条と目的外使用許可"],
  ["教育委員会の回答", "/board-responses.html", "自治体別・論点別の公式回答データベース"],
  ["全国資料館", "/national-archive.html", "自治体別・学校別の実物文書アーカイブ"],
  ["行政通知・公式PDF", "/administrative-materials.html", "行政通知・公式資料"],
  ["資料入口・索引", "/documents.html", "公開資料への入口"],
  ["提出用ひな形", "/guideline.html", "実務ガイドラインと書式テンプレート"],
  ["論考・調査報告", "/journal.html", "個別テーマの掘り下げ"],
  ["運営チェックアプリ", "/audit/index.html", "自校・自PTAのセルフチェック"],
  ["PTA運営の現場実例", "/compliance.html", "みなし加入・代行徴収・名簿提供の実例"],
  ["お問い合わせ・情報提供", "/contact.html", "資料・情報提供窓口"],
  ["応援・寄付", "/support.html", "活動支援のお願い"],
  ["PTA加入・会員管理テンプレート", "/downloads/pta-membership-management-template.html", "PTA役員向けの加入申込・会員管理テンプレート配布セット"]
];

(function(){
  function ready(fn){ if(document.readyState === 'loading') document.addEventListener('DOMContentLoaded', fn, {once:true}); else fn(); }
  function nav(){
    var path='/pta-application-chain.html', label='入会申込書がないと何が崩れるのか';
    var nav=document.querySelector('.desktop-nav');
    if(nav && !nav.querySelector('a[href="'+path+'"]')){
      var ul=nav.querySelector('.nav-item.has-dropdown .mega-col ul');
      if(ul){ var li=document.createElement('li'); li.innerHTML='<a href="'+path+'">'+label+'</a>'; ul.appendChild(li); }
    }
    var overlay=document.getElementById('mobileOverlay');
    if(overlay && !overlay.querySelector('a[href="'+path+'"]')){
      var a=document.createElement('a'); a.className='mobile-link'; a.href=path; a.textContent=label; overlay.appendChild(a);
    }
  }
  function parentCta(){
    var p=location.pathname.replace(/\/+$/,'');
    if(!/\/guide-parent\.html$/.test(p) && p!=='/guide-parent') return;
    if(document.getElementById('pac-parent-top-link')) return;
    var lead=document.getElementById('parent-lead'); if(!lead || !lead.parentNode) return;
    var st=document.createElement('style'); st.textContent='#pac-parent-top-link{background:#fff7ed;padding:28px 0;border-top:1px solid #eee;border-bottom:1px solid #eee}#pac-parent-top-link .box{width:min(calc(100% - 40px),900px);margin:auto;background:#fff;border-left:7px solid #b91c1c;border-radius:0 16px 16px 0;padding:22px 24px;box-shadow:0 10px 28px rgba(5,17,31,.08)}#pac-parent-top-link h2{margin:0 0 8px;color:#0f2747;font-family:"Noto Serif JP",serif;font-size:clamp(1.25rem,2.3vw,1.7rem);line-height:1.45}#pac-parent-top-link p{margin:0 0 14px;color:#334155;line-height:1.85}#pac-parent-top-link a{display:inline-flex;margin:4px 8px 4px 0;padding:9px 15px;border-radius:999px;font-weight:900;text-decoration:none}#pac-parent-top-link .main{background:#d4af37;color:#0f2747}#pac-parent-top-link .sub{background:#f8fafc;color:#0f2747;border:1px solid #dbe4ee}'; document.head.appendChild(st);
    var sec=document.createElement('section'); sec.id='pac-parent-top-link';
    sec.innerHTML='<div class="box"><h2>入会申込書がないまま会員扱いされていませんか</h2><p>入会申込書がない場合、会員資格、会費徴収、学校名簿、教職員関与、学校施設利用まで根拠が連鎖的に不安定になります。確認用の文例も用意しています。</p><a class="main" href="/pta-application-chain.html">図解と確認文例を見る</a><a class="sub" href="/pta-application-chain-action-kit.html">確認シートをPDF保存</a></div>';
    lead.parentNode.insertBefore(sec, lead.nextSibling);
  }
  ready(function(){nav(); parentCta(); setTimeout(nav,300); setTimeout(nav,1000);});
})();
