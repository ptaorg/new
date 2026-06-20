(function(){
  function esc(v){return String(v||'').replace(/[&<>'"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;',"'":'&#39;','"':'&quot;'}[c];});}

  function renderDriveMaterials(data){
    var target=document.getElementById('municipality-documents');
    if(!target||document.getElementById('archive-drive-materials'))return;
    var st=document.createElement('style');
    st.textContent='.archive-drive-materials{background:#fff;padding:42px 0 52px;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}.archive-drive-materials .wrap{max-width:1120px;margin:0 auto;padding:0 24px}.archive-drive-lead{max-width:880px;line-height:1.9;color:var(--text);margin:0 0 18px}.archive-drive-actions{display:flex;flex-wrap:wrap;gap:10px;margin:14px 0 18px}.archive-drive-actions a{display:inline-flex;padding:9px 15px;border-radius:999px;background:var(--navy);color:#fff;text-decoration:none;font-weight:900;font-size:.86rem}.archive-drive-actions a.sub{background:#fff;color:var(--navy);border:1px solid var(--navy)}.archive-drive-table-wrap{overflow-x:auto;border:1px solid var(--line);border-radius:14px;background:#fff;box-shadow:0 10px 24px rgba(5,17,31,.05)}.archive-drive-table{width:100%;border-collapse:collapse;min-width:760px}.archive-drive-table th,.archive-drive-table td{padding:12px 13px;border-bottom:1px solid #e5edf5;text-align:left;vertical-align:top;line-height:1.65;font-size:.9rem}.archive-drive-table th{background:#f8fafc;color:var(--navy);font-weight:900}.archive-drive-table tr:last-child td{border-bottom:none}.archive-drive-tag{display:inline-block;border:1px solid #cbd5e1;border-radius:999px;padding:2px 8px;margin:2px;background:#f8fafc;color:#334155;font-size:.74rem;font-weight:800}.archive-drive-table a{color:var(--navy);font-weight:900;text-decoration-thickness:2px;text-underline-offset:3px}.archive-drive-representative{margin-top:26px}.archive-drive-representative h3{font-family:"Noto Serif JP",serif;color:var(--navy);font-size:1.12rem;margin:0 0 10px}@media(max-width:700px){.archive-drive-materials{padding:34px 0}.archive-drive-materials .wrap{padding:0 18px}}';
    document.head.appendChild(st);
    var sec=document.createElement('section');
    sec.className='archive-drive-materials';
    sec.id='archive-drive-materials';
    var folderRows=(data.municipalFolders||[]).map(function(x){return '<tr><td><strong>'+esc(x.name)+'</strong><br>'+esc(x.prefecture||'')+'</td><td>'+esc(x.observed||'')+'</td><td>'+((x.primaryIssues||[]).map(function(t){return '<span class="archive-drive-tag">'+esc(t)+'</span>';}).join(''))+'</td><td><a href="'+x.folderUrl+'" target="_blank" rel="noopener">Drive</a></td></tr>';}).join('');
    var materialRows=(data.selectedMaterials||[]).map(function(x){return '<tr><td>'+esc(x.municipality)+'</td><td><strong>'+esc(x.school)+'</strong><br>'+esc(x.title)+'<br>'+esc(x.type)+'</td><td>'+esc(x.summary)+'<br>'+((x.issues||[]).map(function(t){return '<span class="archive-drive-tag">'+esc(t)+'</span>';}).join(''))+'</td><td><a href="'+x.sourceUrl+'" target="_blank" rel="noopener">原本</a></td></tr>';}).join('');
    sec.innerHTML='<div class="wrap"><div class="section-kicker">Drive Materials</div><h2 class="section-title">Drive資料目録</h2><p class="archive-drive-lead">各地で入手したPTA案内、入会関係書類、会費徴収資料、学校配布文書を、自治体別・学校別に整理しています。原本を確認しながら、代表資料のメモから必要な箇所へ進めます。</p><div class="archive-drive-actions"><a href="'+esc(data.rootFolder&&data.rootFolder.url)+'" target="_blank" rel="noopener">Drive親フォルダを開く</a><a class="sub" href="/assets/data/national-materials.json">目録JSON</a></div><div class="archive-drive-table-wrap"><table class="archive-drive-table"><thead><tr><th>自治体・区分</th><th>確認状況</th><th>主な論点</th><th>原本</th></tr></thead><tbody>'+folderRows+'</tbody></table></div><div class="archive-drive-representative"><h3>代表資料</h3><div class="archive-drive-table-wrap"><table class="archive-drive-table"><thead><tr><th>自治体</th><th>資料</th><th>メモ</th><th>原本</th></tr></thead><tbody>'+materialRows+'</tbody></table></div></div></div>';
    target.insertAdjacentElement('beforebegin',sec);
  }

  function addArchiveDriveMaterials(){
    if(!location.pathname.endsWith('/national-archive.html'))return;
    fetch('/assets/data/national-materials.json',{cache:'no-store'}).then(function(r){return r.json();}).then(renderDriveMaterials).catch(function(){
      renderDriveMaterials({rootFolder:{url:'https://drive.google.com/drive/folders/1tbfpjRNJIhwQypk1vsAOaE7_qwW-lrm5'},municipalFolders:[],selectedMaterials:[]});
    });
  }

  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',addArchiveDriveMaterials,{once:true});
  else addArchiveDriveMaterials();
})();
