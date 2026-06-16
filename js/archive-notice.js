(function(){
  var cityOpsUrl='/documents.html';
  var realDocsUrl='/national-archive.html';

  function addArchiveNotice(){
    if(!location.pathname.endsWith('/national-archive.html'))return;
    var target=document.getElementById('municipality-documents');
    if(!target||document.querySelector('.archive-google-notice'))return;
    var st=document.createElement('style');
    st.textContent='.archive-google-notice{background:#fff;padding:34px 0;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}.archive-google-notice .box{max-width:1120px;margin:0 auto;padding:22px 24px;border-left:6px solid var(--gold);background:#fffdf3;border-radius:0 16px 16px 0;box-shadow:0 10px 26px rgba(5,17,31,.06)}.archive-google-notice h2{font-family:"Noto Serif JP",serif;color:var(--navy);font-size:1.28rem;line-height:1.5;margin:0 0 8px}.archive-google-notice p{color:var(--text);line-height:1.9;margin:0 0 16px}.archive-google-notice .archive-notice-actions{display:flex;flex-wrap:wrap;gap:12px}.archive-google-notice a{display:inline-flex;padding:10px 18px;border-radius:999px;background:var(--navy);color:#fff;text-decoration:none;font-weight:900}.archive-google-notice a:hover{background:#16395e;color:#fff}.archive-google-notice a.archive-drive-link{background:var(--gold);color:#10253f}.archive-google-notice a.archive-drive-link:hover{background:#c79f1d;color:#10253f}';
    document.head.appendChild(st);
    var sec=document.createElement('section');
    sec.className='archive-google-notice';
    sec.innerHTML='<div class="box"><h2>資料画像・PDFは現在移行中です</h2><p>このページでは自治体別の整理枠を整備中です。学校・PTAから取得した文書実物と行政資料は、サイト内の資料入口からも確認できます。</p><div class="archive-notice-actions"><a href="'+cityOpsUrl+'">資料入口・索引</a><a class="archive-drive-link" href="'+realDocsUrl+'">全国PTA資料館</a></div></div>';
    target.insertAdjacentElement('beforebegin',sec);
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',addArchiveNotice,{once:true});
  else addArchiveNotice();
})();
