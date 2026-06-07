(function(){
  function addArchiveNotice(){
    if(!location.pathname.endsWith('/national-archive.html'))return;
    var target=document.getElementById('municipality-documents');
    if(!target||document.querySelector('.archive-google-notice'))return;
    var st=document.createElement('style');
    st.textContent='.archive-google-notice{background:#fff;padding:34px 0;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}.archive-google-notice .box{max-width:1120px;margin:0 auto;padding:22px 24px;border-left:6px solid var(--gold);background:#fffdf3;border-radius:0 16px 16px 0;box-shadow:0 10px 26px rgba(5,17,31,.06)}.archive-google-notice h2{font-family:"Noto Serif JP",serif;color:var(--navy);font-size:1.28rem;line-height:1.5;margin:0 0 8px}.archive-google-notice p{color:var(--text);line-height:1.9;margin:0 0 16px}.archive-google-notice a{display:inline-flex;padding:10px 18px;border-radius:999px;background:var(--navy);color:#fff;text-decoration:none;font-weight:900}.archive-google-notice a:hover{background:#16395e;color:#fff}';
    document.head.appendChild(st);
    var sec=document.createElement('section');
    sec.className='archive-google-notice';
    var u='https://'+'sites.google.com'+'/view/ptatekiseika/';
    sec.innerHTML='<div class="box"><h2>&#36039;&#26009;&#30011;&#20687;&#12539;PDF&#12399;&#29694;&#22312;&#31227;&#34892;&#20013;&#12391;&#12377;</h2><p>&#12371;&#12398;&#12506;&#12540;&#12472;&#12391;&#12399;&#33258;&#27835;&#20307;&#21029;&#12398;&#25972;&#29702;&#26528;&#12434;&#25972;&#20633;&#20013;&#12391;&#12377;&#12290;&#36039;&#26009;&#12398;&#12480;&#12454;&#12531;&#12525;&#12540;&#12489;&#12420;&#21407;&#26412;&#30906;&#35469;&#12399;&#12289;&#24403;&#20998;&#12398;&#38291;&#12289;&#26087;Google&#12469;&#12452;&#12488;&#20596;&#12391;&#30906;&#35469;&#12375;&#12390;&#12367;&#12384;&#12373;&#12356;&#12290;</p><a href="'+u+'" target="_blank" rel="noopener">Google&#12469;&#12452;&#12488;&#12391;&#36039;&#26009;&#12434;&#30906;&#35469;&#12377;&#12427; &#8594;</a></div>';
    target.insertAdjacentElement('beforebegin',sec);
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',addArchiveNotice,{once:true});
  else addArchiveNotice();
})();
