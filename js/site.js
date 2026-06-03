/* PTA適正化推進委員会 — site.js v4 */
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
  const lead=document.querySelector('#board-first-reading .section-lead');
  if(!lead)return;
  lead.insertAdjacentHTML('afterend',[
    '<section id="pta-contract-entry" aria-labelledby="pta-contract-entry-title" style="margin:28px 0 8px;padding:30px 32px;background:linear-gradient(145deg,#fff,#f8fafc);border:1px solid #dbe4ee;border-left:7px solid var(--gold);border-radius:0 18px 18px 0;box-shadow:0 12px 28px rgba(15,39,66,.06)">',
    '<div class="section-kicker" style="margin-bottom:10px">入会意思確認の基本</div>',
    '<h2 id="pta-contract-entry-title" style="font-family:\'Noto Serif JP\',serif;color:var(--navy);font-size:clamp(1.35rem,3vw,1.85rem);line-height:1.55;margin:0 0 18px">PTAの入会は、学校手続ではなく契約行為である</h2>',
    '<div class="chapter-content plain-prose-block" style="padding:0;margin:0">',
    '<p>教育委員会・学校管理職が最初に確認すべき点は、PTAへの加入を「入学に伴って当然に発生する地位」と扱っていないかどうかです。PTAは学校とは別の任意団体であり、保護者が会員になるためには、PTA側が会則、会費、活動内容、個人情報の利用目的、退会方法などを示し、保護者本人がそれを理解したうえで加入する意思を表示する必要があります。入学、在籍、児童の所属、学級名簿への記載は、それ自体ではPTA入会の意思表示にはなりません。</p>',
    '<p>民法上、契約は、契約の内容を示してその締結を申し入れる意思表示に対して、相手方が承諾をしたときに成立するという構造を取ります。PTA入会でいえば、PTA又はPTAの委任を受けた者が「この団体に、この会則・会費・取扱条件で加入してください」と申込みの対象を具体的に示し、保護者が「加入します」と承諾することが必要です。したがって、入会申込書、オンライン申込記録、同意取得記録など、申込みと承諾を後から確認できる資料がない運用は、会員資格、会費請求、議決権、役員選出、個人情報利用の根拠を不安定にします。</p>',
    '<p>消費者契約法上も、PTAが任意団体であることは契約法の外に置かれる理由にはなりません。同法は、消費者と事業者との間に情報量・交渉力の格差があることを前提に、消費者契約の申込み又は承諾の意思表示を保護する枠組みを置いています。保護者個人が、学校内で、入学説明会や学級配布物を通じて、学校手続と一体に見える形で加入を求められる場合、保護者は「加入しないと子どもに不利益があるのではないか」と受け止めやすく、自由意思による承諾が曖昧になります。</p>',
    '<p>そのため、学校がPTA入会案内を配布する場合でも、本文上は「学校への提出書類」ではなく「PTAへの任意加入の申込み」であることを明記しなければなりません。未提出を加入承諾とみなす方式、退会届を出さなければ会員と扱う方式、非加入の意思表示を求めるオプトアウト方式、学校徴収金の口座振替にPTA会費を混在させる方式は、契約成立の確認を曖昧にし、消費者契約法上の誤認・困惑の問題を生じさせます。</p>',
    '<p>結論として、教育委員会が点検すべき実務は明確です。各学校について、PTA入会案内が任意加入であることを正面から説明しているか、保護者本人の明示的な加入申込みを取得しているか、PTA会費の徴収対象者が申込記録と一致しているか、学校が未加入家庭を把握・抽出する運用になっていないかを確認する必要があります。入会記録がない場合は、「全員が会員だった」と扱うのではなく、入会の根拠を確認できない状態として、徴収・名簿利用・役員選出の前提を見直すべきです。</p>',
    '<div style="margin-top:22px;padding:18px 20px;background:#fff8df;border:1px solid rgba(212,175,55,.42);border-radius:14px;color:#4b3a12;line-height:1.85;font-size:.94rem"><strong style="display:block;color:var(--navy);margin-bottom:6px">学校管理職向けの確認事項</strong>入会申込記録のない保護者からPTA会費を徴収していないか。学校の配布・回収・口座振替・連絡ツールが、保護者に「PTA加入は学校手続の一部」と誤認させる形になっていないか。まずここを点検してください。</div>',
    '</div>',
    '</section>'
  ].join(''));
}
document.addEventListener('DOMContentLoaded',()=>{initSearch();initHamburger();initMegaMenu();initFAQ();initChecklist();initBoardContractSection();});