const fs = require('fs');
const path = require('path');

const ROOT = path.join(__dirname, '..');
const STYLESHEET = '<link rel="stylesheet" href="/css/audience-guides.css?v=20260701">';

const boardContent = `<nav aria-label="パンくず" class="breadcrumb-bar"><div class="breadcrumb-inner"><a href="/index.html">トップ</a><span>›</span><span>立場別</span><span>›</span><span class="current">教育委員会・学校へ</span></div></nav>
<section class="audience-hero-v2">
  <div class="audience-hero-v2__inner">
    <div class="audience-hero-v2__kicker">For School Boards / Administrators</div>
    <h1>学校が関与した事実を確認し、共通方針へ</h1>
    <p>PTA内部を指揮するためのページではありません。入会、配布、回収、徴収、名簿、連絡、教職員の勤務、施設利用に学校が関与している範囲を確認し、学校ごとの差を教育委員会の方針で整えるための入口です。</p>
    <div class="audience-meta"><span>対象：教育委員会・学校管理職</span><span>読む時間：約8分</span><span>得られるもの：確認資料・調査票・通知モデル</span></div>
    <div class="audience-hero-v2__actions">
      <a class="primary" href="#school-involvement-action-plan">最初に集める資料</a>
      <a class="secondary" href="#board-jp-guideline">配布用資料</a>
      <a class="secondary" href="/audit/index.html?mode=board">運営チェック</a>
    </div>
  </div>
</section>
<main class="audience-v2">
  <span class="legacy-anchor" id="s1"></span><span class="legacy-anchor" id="s2"></span><span class="legacy-anchor" id="s3"></span><span class="legacy-anchor" id="s4"></span><span class="legacy-anchor" id="s5"></span><span class="legacy-anchor" id="s6"></span><span class="legacy-anchor" id="s7"></span><span class="legacy-anchor" id="s8"></span><span class="legacy-anchor" id="s9"></span><span class="legacy-anchor" id="s10"></span><span class="legacy-anchor" id="s11"></span><span class="legacy-anchor" id="s12"></span><span class="legacy-anchor" id="s13"></span>
  <section id="board-executive-brief">
    <div class="audience-v2__wrap">
      <div class="audience-conclusion">
        <div class="audience-v2__label">まず結論</div>
        <h2>確認対象はPTAの活動内容ではなく、学校が動いた部分です</h2>
        <p><strong>「任意団体だから教育委員会は関与しない」という整理だけでは、学校管理上の確認は終わりません。</strong>学校がPTA文書を配布・回収した、学校保有情報を使った、学校徴収金と一緒に会費を扱った、教職員が勤務時間中に事務を担った、学校施設を利用させた場合は、その事実と根拠を確認します。</p>
        <div class="audience-evidence">
          <div class="audience-evidence__fact"><strong>確認できた事実</strong><p>学校が行った配布、徴収、情報利用、事務、施設許可を資料で特定します。</p></div>
          <div class="audience-evidence__view"><strong>管理上の整理</strong><p>PTA内部の判断と、学校・設置者が説明すべき行為を分けます。</p></div>
          <div class="audience-evidence__action"><strong>次の行動</strong><p>全校で同じ資料を確認し、停止・移行・継続条件を共通化します。</p></div>
        </div>
      </div>
    </div>
  </section>

  <section id="school-involvement-action-plan">
    <div class="audience-v2__wrap">
      <div class="audience-v2__label">最初の30日</div>
      <h2>各学校から提出を求める5種類の資料</h2>
      <p class="audience-v2__lead">法令解釈を先に争うのではなく、現在の運用を同じ資料で確認します。不存在の場合も「問題なし」とせず、誰がどの情報を基に会員・請求対象・役員候補を決めているかを確認します。</p>
      <div class="audience-grid">
        <article class="audience-card"><div class="audience-card__no">1</div><h3>入会意思を確認できる記録</h3><p>紙・電子の申込記録、承諾日、会則・会費・退会方法を示した資料。</p></article>
        <article class="audience-card"><div class="audience-card__no">2</div><h3>会員名簿と情報取得経路</h3><p>名簿項目、取得元、利用目的、学校からの提供・内部利用・同意の記録。</p></article>
        <article class="audience-card"><div class="audience-card__no">3</div><h3>会費の案内・徴収資料</h3><p>請求主体、対象者、口座、学校徴収金との区分、委任・返金・未納管理。</p></article>
        <article class="audience-card"><div class="audience-card__no">4</div><h3>教職員関与の記録</h3><p>配布回収、会計、名簿、役員選出、連絡ツール操作と、校務・職専免等の整理。</p></article>
        <article class="audience-card"><div class="audience-card__no">5</div><h3>施設・設備の使用記録</h3><p>使用許可、目的、条件、鍵・印刷・保管・学校アカウント利用の管理記録。</p></article>
        <a class="audience-card" href="/evidence-checklist.html"><div class="audience-card__tag">作業用</div><h3>資料検証チェックリスト</h3><p>受け取った資料を、事実・未確認点・次の照会事項へ分けます。</p><span class="audience-card__link">チェック項目を開く</span></a>
      </div>
    </div>
  </section>

  <section>
    <div class="audience-v2__wrap">
      <div class="audience-v2__label">2ステップ</div>
      <h2>現状確認から分離方針へ</h2>
      <div class="audience-process">
        <a href="/board-pta-chain.html"><span>STEP 1　現状確認</span><strong>学校関与の根拠がどこで不安定になるか</strong><p>入会確認の欠落が、名簿・徴収・連絡・職員・施設へ波及する順番を確認します。</p></a>
        <a href="/edu-board-separation.html"><span>STEP 2　実務対応</span><strong>学校とPTAの分離指針</strong><p>教育委員会通知モデル、全校調査、移行案、校長・PTAへの説明文を使います。</p></a>
      </div>
    </div>
  </section>

  <section id="board-jp-guideline">
    <span class="legacy-anchor" id="s14"></span>
    <div class="audience-v2__wrap">
      <div class="audience-v2__label">そのまま配布・編集</div>
      <h2>教育委員会・学校管理職向け資料</h2>
      <p class="audience-v2__lead">説明だけで終わらせず、全校調査と通知に使えるファイルへ進みます。</p>
      <div class="audience-downloads">
        <a class="audience-download" href="/jp/public/pdf/pta-school-separation-guideline.pdf">学校・PTA分離ガイドライン PDF<span>学校が行わない事務、協力できる範囲、移行の基本線。</span></a>
        <a class="audience-download" href="/jp/public/pdf/pta-school-separation-notice-template.pdf">学校長宛通知モデル PDF<span>教育委員会として全校共通方針を通知するための文案。</span></a>
        <a class="audience-download" href="/jp/public/pdf/pta-school-separation-school-survey-form.pdf">学校別実態調査票 PDF<span>配布、名簿、会費、教職員、施設の現状を各校から集めます。</span></a>
        <a class="audience-download" href="/jp/public/xlsx/pta-school-separation-school-survey.xlsx">学校別実態調査票 Excel<span>回答集約・比較・進捗管理に使える編集用ファイル。</span></a>
      </div>
    </div>
  </section>

  <section id="municipal-voices">
    <div class="audience-v2__wrap">
      <div class="audience-v2__label">判断材料</div>
      <h2>行政回答と改善の手がかり</h2>
      <p class="audience-v2__lead">問題事例だけでなく、入会意思確認、PTAによる直接徴収、学校とPTAの分離に踏み込んだ回答を確認し、自自治体の通知・調査項目へ置き換えます。</p>
      <div class="audience-grid">
        <a class="audience-card" href="/board-responses.html"><div class="audience-card__tag">公式回答</div><h3>教育委員会の回答</h3><p>自治体名、担当部署、回答年月、論点別に原文を確認します。</p><span class="audience-card__link">回答データベース</span></a>
        <a class="audience-card" href="/administrative-materials.html"><div class="audience-card__tag">行政資料</div><h3>通知・公式PDF</h3><p>文部科学省、個人情報保護委員会、自治体通知を資料種別で確認します。</p><span class="audience-card__link">行政資料を開く</span></a>
        <a class="audience-card" href="/national-archive.html"><div class="audience-card__tag">現場資料</div><h3>全国資料館</h3><p>学校別の入会案内、会費資料、同意書等を実物で照合します。</p><span class="audience-card__link">実物文書を開く</span></a>
      </div>
    </div>
  </section>

  <section id="key-materials">
    <div class="audience-v2__wrap">
      <div class="audience-v2__label">詳説は分けて読む</div>
      <h2>必要な論点だけ深掘りする</h2>
      <div class="audience-grid audience-grid--2">
        <a class="audience-card" href="/education-board-responsibility.html"><h3>なぜ教育委員会の確認対象か</h3><p>PTA内部と学校関与を分け、所掌の範囲を整理します。</p></a>
        <a class="audience-card" href="/edu-board-separation.html"><h3>分離指針・通知・全校調査</h3><p>校長任せにしない共通方針と移行手順を確認します。</p></a>
        <a class="audience-card" href="/law-map.html"><h3>法制度マップ</h3><p>入会、情報、会費、服務、施設を条文と確認資料へ接続します。</p></a>
        <a class="audience-card" href="/PTA運営適正化ガイドブック_第4版_改訂本文.html"><h3>適正化ガイドブック全文</h3><p>総合的な解説が必要な場合にHTML版全文を参照します。</p></a>
      </div>
    </div>
  </section>

  <section>
    <div class="audience-v2__wrap">
      <div class="audience-v2__label">よくある確認</div>
      <h2>判断を止めないためのQ&A</h2>
      <div class="audience-faq">
        <details><summary>PTAは任意団体なので、教育委員会は何も確認できないのでは？</summary><p>PTA内部の活動を指揮することと、学校が行った配布、情報利用、徴収、服務、施設許可を確認することは別です。後者は学校管理上の事実として確認します。</p></details>
        <details><summary>任意加入であることを周知していれば十分ですか？</summary><p>周知文だけでなく、誰が会員かを確認できる記録、会費請求対象、学校保有情報の利用、非会員児童への取扱いまで確認します。</p></details>
        <details><summary>学校とPTAの覚書があれば代行を続けられますか？</summary><p>覚書の存在だけで結論を出さず、個々の行為について権限、本人説明、服務、会計、施設管理の根拠と記録を確認します。</p></details>
        <details><summary>すぐ全面停止すると学校現場が混乱しませんか？</summary><p>個人情報の新規提供や会員根拠のない請求など優先度の高い項目から止め、連絡・徴収・名簿を段階的にPTAへ移す計画を示します。</p></details>
      </div>
    </div>
  </section>

  <section class="audience-cta">
    <div class="audience-v2__wrap">
      <h2>まず一校ではなく、全校を同じ項目で確認してください</h2>
      <p>学校ごとの慣行ではなく、教育委員会として確認資料・判断基準・移行期限を揃えることが、校長とPTA役員の双方を守ります。</p>
      <div class="audience-cta__links"><a href="#board-jp-guideline">配布資料を使う</a><a href="/contact.html">資料提供・問い合わせ</a></div>
    </div>
  </section>
</main>`;

const officerContent = `<nav aria-label="パンくず" class="breadcrumb-bar"><div class="breadcrumb-inner"><a href="/index.html">トップ</a><span>›</span><span>立場別</span><span>›</span><span class="current">PTA役員の方へ</span></div></nav>
<section class="audience-hero-v2">
  <div class="audience-hero-v2__inner">
    <div class="audience-hero-v2__kicker">For PTA Officers</div>
    <h1>引き継ぐ前に、説明できる運営か確認する</h1>
    <p>前年度踏襲より先に、誰が会員か、誰に会費を請求するか、会員情報をどこから取得したか、学校に何を依頼しているかを確認します。問題を見つけるためではなく、役員個人が根拠の曖昧な運用を背負わないための実務ガイドです。</p>
    <div class="audience-meta"><span>対象：PTA役員・会計・会長</span><span>読む時間：約7分</span><span>得られるもの：6点チェック・移行手順・テンプレート</span></div>
    <div class="audience-hero-v2__actions">
      <a class="primary" href="#first-check">6点を確認</a>
      <a class="secondary" href="#roadmap">是正手順</a>
      <a class="secondary" href="#officer-tools">運用ツール</a>
    </div>
  </div>
</section>
<main class="audience-v2">
  <section id="first-check">
    <div class="audience-v2__wrap">
      <div class="audience-conclusion">
        <div class="audience-v2__label">就任時に最初に確認</div>
        <h2>活動内容より先に、運営の根拠を6点確認します</h2>
        <div class="audience-checks">
          <div class="audience-check"><div class="audience-check__no">1</div><div><h3>加入</h3><p>入会意思を確認できる紙・電子の記録があり、未提出者を会員扱いしていない。</p></div></div>
          <div class="audience-check"><div class="audience-check__no">2</div><div><h3>会費</h3><p>会員に対してPTAが請求し、学校徴収金・学校口座・学校の未納管理と分けている。</p></div></div>
          <div class="audience-check"><div class="audience-check__no">3</div><div><h3>個人情報</h3><p>PTAが本人から必要最小限の情報を取得し、学校名簿を会員名簿として流用していない。</p></div></div>
          <div class="audience-check"><div class="audience-check__no">4</div><div><h3>教職員への依頼</h3><p>会計、集金、名簿、役員選出、督促を教職員の通常業務に載せていない。</p></div></div>
          <div class="audience-check"><div class="audience-check__no">5</div><div><h3>学校施設・連絡手段</h3><p>施設、印刷機、学校アプリ、児童経由配布の許可・条件・文責を確認している。</p></div></div>
          <div class="audience-check"><div class="audience-check__no">6</div><div><h3>会則・総会・会計</h3><p>会員、議決、予算決算、監査、退会、個人情報の扱いを会員へ説明できる。</p></div></div>
        </div>
      </div>
    </div>
  </section>

  <section id="roadmap">
    <div class="audience-v2__wrap">
      <div class="audience-v2__label">問題が見つかったら</div>
      <h2>止める・確かめる・分ける・引き継ぐ</h2>
      <div class="audience-grid audience-grid--2">
        <article class="audience-card"><div class="audience-card__no">1</div><h3>新しい処理を止める</h3><p>会員根拠の確認前に、新規請求、名簿転記、役員候補抽出を進めません。</p></article>
        <article class="audience-card"><div class="audience-card__no">2</div><h3>現在の会員を確認する</h3><p>申込記録、会則、会費記録を照合し、不明な人を推測で会員にしません。</p></article>
        <article class="audience-card"><div class="audience-card__no">3</div><h3>学校経由を分ける</h3><p>申込、連絡、徴収、問い合わせをPTA自身の窓口へ段階的に移します。</p></article>
        <article class="audience-card"><div class="audience-card__no">4</div><h3>決定と経過を残す</h3><p>理事会・総会の決定、移行期限、担当、旧データの廃棄を次年度へ引き継ぎます。</p></article>
      </div>
    </div>
  </section>

  <section id="officer-tools">
    <div class="audience-v2__wrap">
      <div class="audience-v2__label">すぐ使える運用基盤</div>
      <h2>会員管理を学校名簿から切り離す</h2>
      <p class="audience-v2__lead">入会案内、申込、会員確定、名簿、取下げ記録を一つの流れで整えます。</p>
      <div class="audience-downloads">
        <a class="audience-download" href="/downloads/pta-membership-management-template-complete.zip">テンプレート一式 ZIP<span>運用資料と会員管理用ファイルをまとめて取得します。</span></a>
        <a class="audience-download" href="/pta-membership-template.html">加入・会員管理テンプレート<span>保護者へ示す説明と管理者向けの基本線を確認します。</span></a>
        <a class="audience-download" href="/pta-addon.html">Google Sheetsアドオン<span>受付、会員確定、取下げ、名簿反映を状態別に管理します。</span></a>
        <a class="audience-download" href="/audit/index.html?mode=officer">役員向け運営チェック<span>自校の運用を設問に沿って確認し、見直す項目を絞ります。</span></a>
      </div>
    </div>
  </section>

  <section id="officer-video">
    <div class="audience-v2__wrap audience-video">
      <div><div class="audience-v2__label">26秒の導入動画</div><h2>入会手続と会員管理を見直す</h2><p>会員資格、会費、個人情報、学校との役割分担が一つの入口からつながっていることを短く確認できます。詳細を読む前の共有用にも使えます。</p></div>
      <video controls playsinline preload="metadata" aria-label="PTA役員向け説明動画"><source src="/assets/videos/pta-officers.mp4" type="video/mp4">お使いのブラウザは動画再生に対応していません。</video>
    </div>
  </section>

  <section id="visual-guide">
    <div class="audience-v2__wrap">
      <div class="audience-v2__label">全体構造</div>
      <h2>入会確認から何が連鎖するか</h2>
      <div class="audience-process">
        <a href="/pta-officer-chain.html"><span>図解</span><strong>PTA運営の何が不安定になるのか</strong><p>会員名簿、会費、役員選出、学校名簿、教職員関与の順に確認します。</p></a>
        <a href="/proper-management.html"><span>改善後</span><strong>適正な運営モデル</strong><p>任意加入、直接取得、直接徴収、学校との分離を運営手順に戻します。</p></a>
      </div>
    </div>
  </section>

  <section>
    <div class="audience-v2__wrap">
      <div class="audience-v2__label">必要なところだけ詳しく</div>
      <h2>6つの論点別ページ</h2>
      <div class="audience-grid">
        <a class="audience-card" href="/membership.html"><h3>入会手続</h3><p>申込、承諾、会員確定、退会を整理します。</p></a>
        <a class="audience-card" href="/fee-collection.html"><h3>会費徴収</h3><p>請求主体と学校徴収金との分離を確認します。</p></a>
        <a class="audience-card" href="/privacy.html"><h3>個人情報</h3><p>本人からの直接取得と学校保有情報を分けます。</p></a>
        <a class="audience-card" href="/personnel.html"><h3>教職員関与</h3><p>校務、連絡調整、PTA内部事務を区別します。</p></a>
        <a class="audience-card" href="/facilities.html"><h3>施設利用</h3><p>学校施設・設備の許可と利用条件を確認します。</p></a>
        <a class="audience-card" href="/guideline.html"><h3>会則・総会・会計</h3><p>運営ルールと提出用ひな形を確認します。</p></a>
      </div>
    </div>
  </section>

  <section id="guidebook-text">
    <div class="audience-v2__wrap">
      <div class="audience-v2__label">総合解説</div>
      <h2>ガイドブック全文は別ページで読む</h2>
      <p class="audience-v2__lead">入口ページでは実務判断に必要な項目だけを示しています。法令、会計、学校との関係、会則例をまとめて確認する場合は、HTML版またはPDF版をご利用ください。</p>
      <div class="audience-downloads" id="pdf-officer">
        <a class="audience-download" href="/PTA運営適正化ガイドブック_第4版_改訂本文.html">ガイドブック HTML版<span>章ごとに検索・引用しやすい全文ページです。</span></a>
        <a class="audience-download" href="/PTA運営適正化ガイドブック_第4版_改訂版.pdf">ガイドブック PDF版<span>保存・印刷・配布に適した版です。</span></a>
      </div>
    </div>
  </section>

  <section>
    <div class="audience-v2__wrap">
      <div class="audience-v2__label">よくある確認</div>
      <h2>役員からよく出る質問</h2>
      <div class="audience-faq">
        <details><summary>過去の入会記録が見つからない場合、全員に入り直してもらうのですか？</summary><p>まず現状の会員根拠と会則を確認し、推測で会員扱いしない状態にします。次年度から明確な申込方式へ切り替え、現年度の扱いは総会等で説明と決定を残します。</p></details>
        <details><summary>学校経由をやめると回収率が下がりませんか？</summary><p>回収率より、PTA自身が誰から何を受け取ったか説明できることを優先します。Webフォーム、専用メール、郵送、会員向け連絡手段を組み合わせます。</p></details>
        <details><summary>非会員の子どもに活動の利益を渡してよいですか？</summary><p>子どもへの取扱いと保護者の会員資格を分けます。非会員家庭を学校が識別し、児童生徒に不利益が生じる運用は避けます。</p></details>
        <details><summary>一年度で全部変えるのが難しい場合は？</summary><p>新規の情報提供と根拠のない請求を優先的に止め、名簿、徴収、連絡、施設の順に期限と担当を決めて移行します。</p></details>
      </div>
    </div>
  </section>

  <section class="audience-cta">
    <div class="audience-v2__wrap">
      <h2>前年度踏襲ではなく、次年度へ説明できる記録を残す</h2>
      <p>会員、会費、名簿、学校への依頼を一度に完璧にする必要はありません。新しい処理を止め、事実を確認し、移行期限を決めるところから始めます。</p>
      <div class="audience-cta__links"><a href="#first-check">6点を再確認</a><a href="/contact.html">資料提供・相談</a></div>
    </div>
  </section>
</main>`;

function rebuild(fileName, content) {
  const file = path.join(ROOT, fileName);
  const html = fs.readFileSync(file, 'utf8');
  const start = html.indexOf('<nav aria-label="パンくず"');
  const mainEndStart = html.indexOf('</main>', start);
  if (start < 0 || mainEndStart < 0) throw new Error(`Could not locate audience content in ${fileName}`);
  const end = mainEndStart + '</main>'.length;
  let next = html.slice(0, start) + content + html.slice(end);
  // These two entry pages previously accumulated page-specific CSS and scripts
  // that hid, reordered, or injected body sections at runtime. The rebuilt
  // pages use one scoped stylesheet and static HTML, so remove those obsolete
  // layers instead of leaving them to compete with the new document order.
  next = next.replace(/<style(?:\s[^>]*)?>[\s\S]*?<\/style>\s*/gi, '');
  next = next.replace(/<script([^>]*)>([\s\S]*?)<\/script>\s*/gi, (match, attrs, body) => {
    if (/guide-board-direct-fixed|board-fact-accordion-v31|cl20-item|checklist-grid-20/.test(body)) return '';
    return match;
  });
  if (!next.includes('/css/audience-guides.css')) next = next.replace('</head>', `${STYLESHEET}\n</head>`);
  fs.writeFileSync(file, next, 'utf8');
  console.log(`Rebuilt ${fileName}`);
}

rebuild('guide-board.html', boardContent);
rebuild('guide-pta.html', officerContent);
