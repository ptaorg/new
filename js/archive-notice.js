(function(){
  var cityOpsUrl='https://sites.google.com/view/ptatekiseika/%E5%85%A8%E5%9B%BDpta%E8%B3%87%E6%96%99%E9%A4%A8?authuser=0';
  var realDocsUrl='https://drive.google.com/drive/folders/1tbfpjRNJIhwQypk1vsAOaE7_qwW-lrm5?usp=sharing';

  function patchExistingGoogleSiteButton(){
    if(!location.pathname.endsWith('/national-archive.html'))return;
    var anchors=document.querySelectorAll('a[href^="https://sites.google.com/view/ptatekiseika"]');
    anchors.forEach(function(a){
      a.href=cityOpsUrl;
      a.target='_blank';
      a.rel='noopener noreferrer';
      if(a.textContent.indexOf('旧資料サイト')!==-1||a.textContent.indexOf('Googleサイト')!==-1){
        a.textContent='各都市PTA運用状況';
      }
    });
  }

  function addArchiveNotice(){
    if(!location.pathname.endsWith('/national-archive.html'))return;
    var target=document.getElementById('municipality-documents');
    patchExistingGoogleSiteButton();
    if(!target||document.querySelector('.archive-google-notice'))return;
    var st=document.createElement('style');
    st.textContent='.archive-google-notice{background:#fff;padding:34px 0;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}.archive-google-notice .box{max-width:1120px;margin:0 auto;padding:22px 24px;border-left:6px solid var(--gold);background:#fffdf3;border-radius:0 16px 16px 0;box-shadow:0 10px 26px rgba(5,17,31,.06)}.archive-google-notice h2{font-family:"Noto Serif JP",serif;color:var(--navy);font-size:1.28rem;line-height:1.5;margin:0 0 8px}.archive-google-notice p{color:var(--text);line-height:1.9;margin:0 0 16px}.archive-google-notice .archive-notice-actions{display:flex;flex-wrap:wrap;gap:12px}.archive-google-notice a{display:inline-flex;padding:10px 18px;border-radius:999px;background:var(--navy);color:#fff;text-decoration:none;font-weight:900}.archive-google-notice a:hover{background:#16395e;color:#fff}.archive-google-notice a.archive-drive-link{background:var(--gold);color:#10253f}.archive-google-notice a.archive-drive-link:hover{background:#c79f1d;color:#10253f}';
    document.head.appendChild(st);
    var sec=document.createElement('section');
    sec.className='archive-google-notice';
    sec.innerHTML='<div class="box"><h2>資料画像・PDFは現在移行中です</h2><p>このページでは自治体別の整理枠を整備中です。各都市のPTA運用状況と、学校・PTAから取得した文書実物は、下記の外部資料でも確認できます。</p><div class="archive-notice-actions"><a href="'+cityOpsUrl+'" target="_blank" rel="noopener noreferrer">各都市PTA運用状況</a><a class="archive-drive-link" href="'+realDocsUrl+'" target="_blank" rel="noopener noreferrer">全国PTA文書実物</a></div></div>';
    target.insertAdjacentElement('beforebegin',sec);
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',addArchiveNotice,{once:true});
  else addArchiveNotice();
})();
