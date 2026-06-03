/* PTA適正化推進委員会 — site.js v7 */
const SITE_INDEX=[
  {title:'トップページ',url:'index.html',desc:'サイト全体の入口。今何が起きているか、立場別ガイド、監査システム。みなし加入 強制加入 横領 個人情報'},
  {title:'静岡市・9200人分個人情報無断提供事案',url:'shizuoka-incident.html',desc:'2026年4月発覚。静岡市立20校で保護者の同意なく個人情報をPTAに提供。教育長「法律と学校文化にずれ」。構造的分析。'},
  {title:'保護者の方へ',url:'guide-parent.html',desc:'入会・会費・個人情報。絵で直感的に理解できるガイド。みなし加入 退会 返還請求 テンプレートPDF'},
  {title:'PTA役員の方へ',url:'guide-pta.html',desc:'就任直後の確認・適正化ロードマップ・PDF雛形。役員 リスク 会計 入会届'},
  {title:'教育委員会・学校の方へ',url:'guide-board.html',desc:'職務専念義務・渉外業務・覚書問題。校長 教頭 教職員 地公法35条'},
  {title:'教委向け分離指針',url:'edu-board-separation.html',desc:'学校とPTAの線引きを校長任せにしない。教育委員会通知 校長会資料 PTA直接徴収 会員管理 分離通知'},
  {title:'研究者・記者の方へ',url:'guide-research.html',desc:'全国公文書・教委回答・一次資料へのアクセスガイド。取材 問い合わせ'},
  {title:'資料・文書一覧',url:'documents.html',desc:'資料入口。行政通知 教育委員会回答 全国資料館 論点別資料 入会申込書 個人情報 会費徴収'},
  {title:'教育委員会の回答',url:'board-responses.html',desc:'76自治体・111件の分類済み回答。任意加入 個人情報 会費徴収 教職員関与 横浜市通知'},
  {title:'全国資料館',url:'national-archive.html',desc:'開示請求で収集した全国のPTA関連公文書。入会届 会費 名簿 覚書'},
  {title:'PTA運営の現場実例',url:'compliance.html',desc:'みなし加入 抱き合わせ徴収 個人情報提供 学校連絡ツール 教職員関与 施設利用 非会員対応 児童への不利益'},
  {title:'論考・調査報告',url:'journal.html',desc:'法律論考・調査報告・行政動向の分析。スライド 会費徴収パラドックス'},
  {title:'監査システム',url:'audit/index.html',desc:'5軸・3立場でPTA運営のリスクを自動診断。保護者 役員 学校管理職'},
  {title:'入会手続・オプトアウト',url:'membership.html',desc:'みなし加入・オプトアウト方式の法的無効性。民法522条 不当利得 沈黙は承諾ではない'},
  {title:'個人情報提供',url:'privacy.html',desc:'学校からPTAへの名簿提供の違法性。個人情報保護法69条 第三者提供 オプトイン'},
  {title:'会費徴収',url:'fee-collection.html',desc:'学校徴収金との混在・無権代理・不当利得。抱き合わせ徴収 給食費 口座引落'},
  {title:'教職員関与・職務専念義務',url:'personnel.html',desc:'地公法35条・PTA事務への恒常的従事の問題。担任 集金 配布 渉外業務'},
  {title:'施設利用',url:'facilities.html',desc:'学校教育法137条・公私境界の整理。PTA室 コピー機 光熱費 鍵'},
  {title:'法制度マップ',url:'law-map.html',desc:'憲法・民法・個人情報保護法・地公法・地方財政法の論点別整理。条文 e-Gov'},
  {title:'判例整理',url:'cases.html',desc:'PTA関連の裁判例・学説の整理。熊本地裁 大阪地裁 黙示の承諾'},
  {title:'行政資料整理',url:'administrative-materials.html',desc:'文科省通知・教委回答・行政実例の整理。1964年行政実例 横浜市通知'},
  {title:'総合分析レポート',url:'report.html',desc:'全国調査に基づく構造分析・提言。法的枠組み 歴史 適正化の方向性'},
];
function initSearch(){
  document.querySelectorAll('.search-input').forEach(input=>{
    const dd=input.closest('.header-search')?.querySelector('.search-results-dropdown');
    if(!dd)return;
    input.addEventListener('input',()=>{
      const q=input.value.trim().toLowerCase();
      if(q.length<2){dd.classList.remove('is-open');return;}
      const hits=SITE_INDEX.filter(p=>p.title.toLowerCase().includes(q)||p.desc.toLowerCase().includes(q)).slice(0,6);
      dd.innerHTML=hits.length?hits.map(p=>`<a href="${p.url}" class="srd-item"><div class="srd-item-title">${p.title}</div><div class="srd-item-desc">${p.desc}</div></a>`).join(''):`<div class="srd-empty">「${input.value}」に一致するページが見つかりません</div>`;
      dd.classList.add('is-open');
    });
    document.addEventListener('click',e=>{if(!input.closest('.header-search').contains(e.target))dd.classList.remove('is-open');});
    input.addEventListener('keydown',e=>{if(e.key==='Escape')dd.classList.remove('is-open');});
  });
}
function initHamburger(){
  const btn=document.getElementById('hamburger'),ol=document.getElementById('mobileOverlay'),cl=document.getElementById('closeOverlay');
  if(!btn||!ol)return;
  btn.addEventListener('click',()=>{ol.classList.add('is-open');btn.setAttribute('aria-expanded','true');});
  cl?.addEventListener('click',()=>{ol.classList.remove('is-open');btn.setAttribute('aria-expanded','false');});
}
function initMegaMenu(){
  document.querySelectorAll('.nav-item.has-dropdown>.nav-link').forEach(link=>{
    link.addEventListener('click',e=>{
      const item=link.closest('.nav-item');
      if(window.innerWidth>860){e.preventDefault();item.classList.toggle('is-open');document.querySelectorAll('.nav-item.is-open').forEach(i=>{if(i!==item)i.classList.remove('is-open');});}
    });
  });
  document.addEventListener('click',e=>{if(!e.target.closest('.nav-item'))document.querySelectorAll('.nav-item.is-open').forEach(i=>i.classList.remove('is-open'));});
}
function initFAQ(){
  document.querySelectorAll('.faq-item').forEach(item=>{
    const q=item.querySelector('.faq-q');
    if(!q)return;
    q.addEventListener('click',()=>{const o=item.classList.toggle('is-open');const t=item.querySelector('.faq-toggle');if(t)t.textContent=o?'▲':'▼';});
  });
}
function initChecklist(){
  document.querySelectorAll('.check-box').forEach(box=>{
    box.addEventListener('click',()=>{box.classList.toggle('checked');box.textContent=box.classList.contains('checked')?'✓':'';});
  });
}
function initBoardContractSection(){
  const isGuideBoard=location.pathname.endsWith('/guide-board.html')||location.pathname.endsWith('guide-board.html');
  if(!isGuideBoard||document.getElementById('pta-contract-entry'))return;
  const article137=document.getElementById('article137-school-use');
  if(!article137)return;
  article137.insertAdjacentHTML('beforebegin',[
    '<section class="board-guide-section article137-focus" id="pta-contract-entry" aria-labelledby="pta-contract-entry-title">',
    '<div class="wrap">',
    '<div class="section-kicker">入会意思確認の基本</div>',
    '<h2 class="section-title" id="pta-contract-entry-title" style="font-size:clamp(.95rem,2.4vw,1.42rem);line-height:1.45;white-space:nowrap;text-decoration:underline;text-decoration-thickness:2px;text-underline-offset:8px">PTAの入会は、学校手続ではなく契約行為である</h2>',
    '<p class="section-lead">PTAが学校とは別の任意団体である以上、保護者が会員になるには、PTA側からの加入条件の提示と、保護者本人による明示的な承諾が必要です。学校への入学、児童の在籍、学級名簿への記載は、それ自体ではPTA入会の意思表示にはなりません。</p>',
    '<div class="article137-lead">',
    '<p>教育委員会・学校管理職が最初に確認すべき点は、PTAへの加入を「入学に伴って当然に発生する地位」と扱っていないかどうかです。PTAは学校とは別の任意団体であり、保護者が会員になるためには、PTA側が会則、会費、活動内容、個人情報の利用目的、退会方法などを示し、保護者本人がそれを理解したうえで加入する意思を表示する必要があります。</p>',
    '<p>民法上、契約は、契約の内容を示してその締結を申し入れる意思表示に対して、相手方が承諾をしたときに成立するという構造を取ります。PTA入会でいえば、PTA又はPTAの委任を受けた者が「この団体に、この会則・会費・取扱条件で加入してください」と申込みの対象を具体的に示し、保護者が「加入します」と承諾することが必要です。</p>',
    '<p>したがって、入会申込書、オンライン申込記録、同意取得記録など、申込みと承諾を後から確認できる資料がない運用は、会員資格、会費請求、議決権、役員選出、個人情報利用の根拠を不安定にします。「毎年そうしている」「全員加入として扱ってきた」という慣行は、契約成立の証拠にはなりません。</p>',
    '<div style="margin:18px 0 26px;padding:18px 20px;background:#fff;border:1px solid #dbe4ee;border-left:5px solid #1e3a5f;border-radius:0 14px 14px 0;color:#1f2937;line-height:1.85;font-size:.9rem"><strong style="display:block;color:#0b2a4a;margin-bottom:8px">民法第522条（契約の成立と方式）</strong><p style="margin:0 0 .7em">１　契約は、契約の内容を示してその締結を申し入れる意思表示（以下「申込み」という。）に対して相手方が承諾をしたときに成立する。</p><p style="margin:0">２　契約の成立には、法令に特別の定めがある場合を除き、書面の作成その他の方式を具備することを要しない。</p></div>',
    '<p>消費者契約法上も、PTAが任意団体であることは契約法の外に置かれる理由にはなりません。同法は、消費者と事業者との間に情報量・交渉力の格差があることを前提に、消費者契約の申込み又は承諾の意思表示を保護する枠組みを置いています。保護者個人が、学校内で、入学説明会や学級配布物を通じて、学校手続と一体に見える形で加入を求められる場合、保護者は「加入しないと子どもに不利益があるのではないか」と受け止めやすく、自由意思による承諾が曖昧になります。</p>',
    '<div style="margin:18px 0 26px;padding:18px 20px;background:#fff;border:1px solid #dbe4ee;border-left:5px solid #b45309;border-radius:0 14px 14px 0;color:#1f2937;line-height:1.85;font-size:.88rem"><strong style="display:block;color:#92400e;margin-bottom:8px">消費者契約法第4条・第10条（関連条文）</strong><p style="margin:0 0 .75em"><b>第4条第1項</b>　消費者は、事業者が消費者契約の締結について勧誘をするに際し、当該消費者に対して次の各号に掲げる行為をしたことにより当該各号に定める誤認をし、それによって当該消費者契約の申込み又はその承諾の意思表示をしたときは、これを取り消すことができる。</p><p style="margin:0 0 .75em">一　重要事項について事実と異なることを告げること。　当該告げられた内容が事実であるとの誤認</p><p style="margin:0 0 .75em"><b>第4条第2項</b>　消費者は、事業者が消費者契約の締結について勧誘をするに際し、当該消費者に対してある重要事項又は当該重要事項に関連する事項について当該消費者の利益となる旨を告げ、かつ、当該重要事項について当該消費者の不利益となる事実（当該告知により当該事実が存在しないと消費者が通常考えるべきものに限る。）を故意又は重大な過失によって告げなかったことにより、当該事実が存在しないとの誤認をし、それによって当該消費者契約の申込み又はその承諾の意思表示をしたときは、これを取り消すことができる。</p><p style="margin:0"><b>第10条</b>　消費者の不作為をもって当該消費者が新たな消費者契約の申込み又はその承諾の意思表示をしたものとみなす条項その他の法令中の公の秩序に関しない規定の適用による場合に比して消費者の権利を制限し又は消費者の義務を加重する消費者契約の条項であって、民法第一条第二項に規定する基本原則に反して消費者の利益を一方的に害するものは、無効とする。</p></div>',
    '<p>そのため、学校がPTA入会案内を配布すること自体を避けるべきです。PTAへの入会案内、加入申込み、会費の説明、個人情報の取得は、学校手続とは切り離し、PTAが自らの責任で、保護者に対して直接行う必要があります。学校が配布・回収の経路に入ると、保護者はそれを学校への提出書類又は学校手続の一部と受け止めやすく、任意加入の前提である自由な承諾が損なわれます。未提出を加入承諾とみなす方式、退会届を出さなければ会員と扱う方式、非加入の意思表示を求めるオプトアウト方式、学校徴収金の口座振替にPTA会費を混在させる方式は、契約成立の確認を曖昧にし、消費者契約法上の誤認・困惑の問題を生じさせます。</p>',
    '</div>',
    '<table class="article137-table">',
    '<thead><tr><th>点検対象</th><th>確認すべきこと</th></tr></thead>',
    '<tbody>',
    '<tr><td>入会案内</td><td>学校がPTA入会案内を配布していないか。PTAが、任意加入であること、会則・会費・活動内容・退会方法を保護者へ直接示しているか。</td></tr>',
    '<tr><td>申込みと承諾</td><td>保護者本人の明示的な加入申込みを取得し、後から確認できる記録として保管しているか。</td></tr>',
    '<tr><td>会費徴収</td><td>PTA会費の徴収対象者が、入会申込記録のある会員と一致しているか。</td></tr>',
    '<tr><td>学校関与</td><td>学校の配布・回収・口座振替・連絡ツールが、PTA加入を学校手続の一部と誤認させる形になっていないか。</td></tr>',
    '</tbody>',
    '</table>',
    '<div class="article137-conclusion">',
    '<h3>入会記録がない場合は、「全員が会員だった」と扱わない</h3>',
    '<p>入会記録がない場合は、入会の根拠を確認できない状態として扱う必要があります。そのまま会費徴収、名簿利用、議決権付与、役員選出を続けると、PTA内部の問題にとどまらず、学校が関与した徴収・配布・個人情報取扱いの適法性まで問われます。</p>',
    '<p class="article137-note">学校管理職は、PTAの内部運営を支配するのではなく、学校が関与している範囲について、契約成立の確認を曖昧にしていないかを点検する必要があります。</p>',
    '</div>',
    '</div>',
    '</section>'
  ].join(''));
}
document.addEventListener('DOMContentLoaded',()=>{initSearch();initHamburger();initMegaMenu();initFAQ();initChecklist();initBoardContractSection();});