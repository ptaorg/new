window.PTA_SITE_SEARCH_INDEX = [
  ["PTA適正化推進委員会", "/index.html", "一次資料・法令・行政回答にもとづき、PTAの任意加入、公私分離、個人情報、会費徴収を整理する資料サイトです。"],
  ["保護者の方へ", "/guide-parent.html", "入会した覚えがない・会費の根拠が分からない場合の確認手順"],
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
  function ready(fn){
    if(document.readyState === 'loading') document.addEventListener('DOMContentLoaded', fn, {once:true});
    else fn();
  }
  function addOfficerTemplateCard(){
    var path = location.pathname.replace(/\/+$/, '');
    if(!/\/guide-pta\.html$/.test(path) && path !== '/guide-pta') return;
    if(document.getElementById('pta-member-template')) return;

    var style = document.createElement('style');
    style.id = 'pta-template-connect-style';
    style.textContent = `
      .pta-template-connect{background:linear-gradient(180deg,#fffaf0 0%,#f7f3e8 100%);padding:52px 0;border-bottom:1px solid rgba(15,39,71,.08)}
      .pta-template-card{width:min(calc(100% - 40px),1080px);margin-inline:auto;background:#fff;border:1px solid rgba(15,39,71,.14);border-left:8px solid #2f6f73;border-radius:22px;box-shadow:0 16px 42px rgba(5,17,31,.10);padding:30px 32px 28px}
      .pta-template-badge{display:inline-flex;align-items:center;padding:6px 13px;border-radius:999px;background:rgba(47,111,115,.10);color:#2f6f73;font-size:.74rem;font-weight:900;letter-spacing:.08em;text-transform:uppercase;margin-bottom:14px}
      .pta-template-card h2{margin:0 0 12px;color:#0f2747;font-family:'Noto Serif JP',serif;font-size:clamp(1.34rem,2.3vw,1.9rem);line-height:1.42}
      .pta-template-lead{max-width:900px;margin:0 0 18px;color:#334155;font-size:.98rem;line-height:1.92;font-weight:600}
      .pta-template-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px;margin:18px 0 22px}
      .pta-template-point{background:#f8fafc;border:1px solid #dbe4ee;border-top:4px solid #2f6f73;border-radius:14px;padding:16px 17px}
      .pta-template-point:nth-child(2){border-top-color:#d4af37}.pta-template-point:nth-child(3){border-top-color:#8c3b2f}
      .pta-template-point strong{display:block;color:#0f2747;font-weight:900;margin-bottom:6px}.pta-template-point p{margin:0;color:#475569;font-size:.9rem;line-height:1.75}
      .pta-template-actions{display:flex;flex-wrap:wrap;gap:12px;align-items:center;margin-top:8px}.pta-template-note{margin:16px 0 0;color:#64748b;font-size:.88rem;line-height:1.75}
      @media(max-width:820px){.pta-template-grid{grid-template-columns:1fr}.pta-template-card{padding:24px 20px;border-left-width:6px}}
    `;
    document.head.appendChild(style);

    var section = document.createElement('section');
    section.className = 'pta-template-connect';
    section.id = 'pta-member-template';
    section.setAttribute('aria-labelledby','pta-member-template-title');
    section.innerHTML = '<div class="pta-template-card"><div class="pta-template-badge">役員向け配布セット</div><h2 id="pta-member-template-title">PTA加入・会員管理テンプレートを使って、学校名簿に頼らない運営へ切り替える</h2><p class="pta-template-lead">加入申込、会員確定、入金確認、取下げ・無効処理を分けて記録するためのテンプレートです。Googleフォームとスプレッドシートを使い、PTAが自ら必要最小限の情報を取得・管理する設計にしています。学校名簿の流用、学校徴収金との抱き合わせ、みなし加入を前提にしません。</p><div class="pta-template-grid"><div class="pta-template-point"><strong>入会申込を記録する</strong><p>加入意思、重要事項への同意、連絡先をフォームで受け付け、申込のない保護者を会員扱いしない運用へ整理します。</p></div><div class="pta-template-point"><strong>会員確定と入金確認を分ける</strong><p>申込受付、会員確定、会費入金、取消・無効を別ステータスで管理し、後から説明できる台帳にします。</p></div><div class="pta-template-point"><strong>個人情報を最小限にする</strong><p>PTAが本人から取得する情報だけで運用し、学校名簿や学校連絡網への依存を減らすための構成です。</p></div></div><div class="pta-template-actions"><a class="btn-gold" href="/downloads/pta-membership-management-template.html">ZIPをダウンロード</a><a class="btn-outline" href="#first-check">役員向け6点確認へ</a><a class="btn-outline" href="/privacy.html">個人情報の論点を見る</a></div><p class="pta-template-note">配布セットには、空の会員管理テンプレート、Apps Script、利用者向け手順、個人情報取扱いの考え方、重要事項説明文テンプレートを含めています。実際の配布前には、各PTAの会則・会費額・利用目的に合わせて文面を確認してください。</p></div>';

    var main = document.querySelector('main');
    if(main) main.insertBefore(section, main.firstChild);
    var actions = document.querySelector('.hero-actions');
    if(actions && !actions.querySelector('a[href="#pta-member-template"]')){
      var a = document.createElement('a');
      a.className = 'btn-gold';
      a.href = '#pta-member-template';
      a.textContent = '会員管理テンプレート';
      actions.insertBefore(a, actions.firstChild);
    }
  }
  ready(addOfficerTemplateCard);
})();
