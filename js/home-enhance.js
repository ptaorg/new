/*
  ptaorg.github.io home enhancement
  上部写真スライドショーは一切変更しない。
  既存の .hero-content-wrap の直後に、画像付き入口群を追加する。
*/
(function () {
  function link(href, cls, imgCls, kicker, title, desc) {
    return `
      <a class="eh-card" href="${href}">
        <div class="eh-img ${imgCls}" role="img" aria-label="${title}のイメージ画像"></div>
        <div class="eh-body">
          <span class="eh-kicker">${kicker}</span>
          <h3>${title}</h3>
          <p>${desc}</p>
          <span class="eh-go">開く →</span>
        </div>
      </a>`;
  }

  function buildEnhanceSection() {
    return `
<section class="pta-home-enhance" aria-label="PTA適正化推進委員会 主要入口">
  <div class="eh-wrap">
    <div class="eh-alert">
      <div><strong>重要</strong>このサイトは、PTAを学校の空気ではなく、実物資料・教育委員会回答・制度から確認するための研究ポータルです。</div>
      <a href="materials-catalog.html">資料を見る</a>
    </div>

    <div class="eh-section-head">
      <div>
        <h2>まず、自分の立場から読む。</h2>
        <p>保護者、PTA役員、学校・教育委員会で、見るべき資料と論点は変わります。入口を分け、必要なページへすぐ進めるようにしました。</p>
      </div>
      <span class="eh-mini">入口を整理</span>
    </div>

    <div class="eh-grid three">
      ${link("guide-parent.html", "eh-card", "parent", "Parent", "保護者の方へ", "入会、会費、個人情報、役員・当番を、手元のプリントと照らして確認します。")}
      ${link("guide-pta.html", "eh-card", "pta", "PTA", "PTA役員の方へ", "任意団体として必要な会員管理、入会記録、会費、個人情報の扱いを整理します。")}
      ${link("guide-board.html", "eh-card", "board", "School / Board", "学校・教育委員会へ", "PTAを直接統制せず、学校側の関与を所掌範囲として点検します。")}
    </div>

    <div class="eh-feature">
      <div>
        <h2>実物資料庫を中心に、サイト内で完結させる。</h2>
        <p>Google Driveは原本保管に使っても、読者に見せる主導線はこのサイト内に置きます。各地から取り寄せたPTA資料を画像化し、画像と解説を並べて確認できる資料庫へ育てます。</p>
        <div class="eh-note">資料は、確認済み・本文未確認・資料名からの仮分類など、検証状態を分けて扱います。</div>
      </div>
      <div>
        <div class="eh-feature-imgs">
          <div class="eh-img materials" role="img" aria-label="資料束の画像"></div>
          <div class="eh-img catalog" role="img" aria-label="資料整理の画像"></div>
          <div class="eh-img responses" role="img" aria-label="公文書資料の画像"></div>
          <div class="eh-img search" role="img" aria-label="チェックリストの画像"></div>
        </div>
        <div class="eh-links">
          <a href="materials-catalog.html">実物資料カタログ</a>
          <a href="responses.html">教育委員会回答DB</a>
          <a href="edu.html">教育委員会向け指針</a>
        </div>
      </div>
    </div>

    <div class="eh-section-head">
      <div>
        <h2>確認する主要論点。</h2>
        <p>入会意思確認、会費徴収、個人情報、教職員関与など、PTA運営の問題を論点別に確認します。</p>
      </div>
      <span class="eh-mini">画像付き入口</span>
    </div>

    <div class="eh-grid four">
      ${link("membership.html", "eh-card", "membership", "Membership", "入会意思確認", "入会申込、承諾、退会、未加入の扱いを確認します。")}
      ${link("fee-collection.html", "eh-card", "fee", "Fee", "会費徴収", "学校徴収金との混在、口座、委任、返金処理を確認します。")}
      ${link("privacy.html", "eh-card", "privacy", "Privacy", "個人情報", "学校保有情報の提供、PTAによる直接取得、同意文書を確認します。")}
      ${link("pta-duty-concentration.html", "eh-card", "staff", "Duty", "教職員関与", "勤務時間内PTA事務、校務分掌、職専免の有無を確認します。")}
    </div>

    <div class="eh-section-head" style="margin-top:38px">
      <div>
        <h2>資料・回答・検索。</h2>
        <p>実物資料、教育委員会回答、サイト内検索から、根拠に戻れる導線を置きます。</p>
      </div>
    </div>

    <div class="eh-grid three">
      ${link("materials-catalog.html", "eh-card", "catalog", "Archive", "実物PTA資料カタログ", "自治体名、学校名、資料名、論点候補から資料を探します。")}
      ${link("responses.html", "eh-card", "responses", "Database", "教育委員会回答DB", "全国の教育委員会回答を自治体別・質問類型別に確認します。")}
      ${link("search.html", "eh-card", "search", "Search", "サイト内検索", "資料名、自治体名、論点名から必要なページを探します。")}
    </div>
  </div>
</section>`;
  }

  document.addEventListener("DOMContentLoaded", function () {
    if (document.querySelector(".pta-home-enhance")) return;

    var target = document.querySelector(".hero-content-wrap");
    var section = document.createElement("div");
    section.innerHTML = buildEnhanceSection();

    if (target && target.parentNode) {
      target.insertAdjacentElement("afterend", section.firstElementChild);
    } else {
      var main = document.querySelector("main") || document.body;
      main.insertAdjacentElement("afterbegin", section.firstElementChild);
    }
  });
})();