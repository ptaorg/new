const fs = require("fs");
const path = require("path");
const {
  ROOT,
  STATUS_ORDER,
  escapeHtml,
  listSchoolData,
  sortSchools,
  statusClassFor,
  writeFileIfChanged
} = require("./archive-utils");

const START = "<!-- ATSUGI_ARCHIVE_START -->";
const END = "<!-- ATSUGI_ARCHIVE_END -->";

function countByStatus(records) {
  const counts = Object.fromEntries(STATUS_ORDER.map((status) => [status, 0]));
  for (const record of records) {
    const key = record.status === "未評価" ? "評価準備中" : record.status;
    counts[key] = (counts[key] || 0) + 1;
  }
  return counts;
}

function renderCountCards(records) {
  const counts = countByStatus(records);
  return STATUS_ORDER.map((status) => {
    const cls = statusClassFor(status);
    return `          <div class="archive-count-card ${cls}">
            <span class="archive-count-label">${escapeHtml(status)}</span>
            <strong>${counts[status] || 0}校</strong>
          </div>`;
  }).join("\n");
}

function renderLegend() {
  const items = [
    ["重大リスク", "任意加入・入会手続・学校関与等に重大な疑義があるもの"],
    ["問題あり", "運用上の問題が確認されるもの"],
    ["要確認", "追加確認を要するもの"],
    ["資料不足", "判断に必要な資料が不足しているもの"],
    ["適正化モデル", "改善例として参照できるもの"],
    ["評価準備中", "資料確認・評価作業中のもの"]
  ];
  return items.map(([status, description]) => `          <span class="eval-badge ${statusClassFor(status)}">${escapeHtml(status)}</span>
          <span>${escapeHtml(description)}</span>`).join("\n");
}

function renderSchoolList(records, schoolType) {
  return records
    .filter((record) => record.schoolType === schoolType)
    .sort(sortSchools)
    .map((record) => {
      const pagePath = path.join(ROOT, record.basePath.replace(/^\/+/, ""), "index.html");
      const name = escapeHtml(record.schoolName);
      const nameHtml = fs.existsSync(pagePath)
        ? `<a href="${escapeHtml(record.basePath)}">${name}</a>`
        : `<span>${name}</span>`;
      const status = record.status === "未評価" ? "評価準備中" : record.status;
      return `              <li>${nameHtml} <span class="eval-badge ${statusClassFor(status, record.statusClass)}">${escapeHtml(status)}</span></li>`;
    })
    .join("\n");
}

function renderAtsugiSection(records) {
  const atsugiRecords = records.filter((record) => record.citySlug === "atsugi").sort(sortSchools);
  if (!atsugiRecords.length) throw new Error("No Atsugi school JSON files found");
  return `
    <!-- 厚木市 学校一覧 -->
    <section class="atsugi-schools-section" id="atsugi-schools">
      <div class="wrap">
        <div class="section-center atsugi-schools-head">
          <div class="section-kicker">Atsugi City</div>
          <h2 class="section-title">厚木市 PTA関連資料</h2>
          <p class="section-lead">厚木市について、今後、各学校ごとにPTA入会案内、PTA入会申込書、学校納入金・会費徴収資料等を整理して掲載します。現時点では、厚木市内の小学校・中学校一覧を先行掲載します。資料確認・評価が完了した学校から、順次、学校別ページまたは評価ページへリンクします。</p>
        </div>
        <div class="archive-evaluation-summary" aria-label="厚木市の評価別集計">
${renderCountCards(atsugiRecords)}
        </div>
        <div class="archive-legend" aria-label="評価バッジの説明">
${renderLegend()}
        </div>
        <div class="atsugi-school-groups" aria-label="厚木市内学校一覧">
          <div class="atsugi-school-group">
            <h3>厚木市小学校</h3>
            <ul class="atsugi-school-list">
${renderSchoolList(atsugiRecords, "小学校")}
            </ul>
          </div>
          <div class="atsugi-school-group">
            <h3>厚木市中学校</h3>
            <ul class="atsugi-school-list">
${renderSchoolList(atsugiRecords, "中学校")}
            </ul>
          </div>
        </div>
        <p class="atsugi-schools-note">補足：この一覧は、厚木市内の学校を母集団として整理するための基礎一覧です。今後、開示資料・入会案内・入会申込書・学校納入金資料等と突合し、資料あり／未確認／不存在回答／評価済みを分けて表示します。学校別ページへのリンクを設けています。資料確認・評価が進んだ学校から、評価ラベルを更新します。</p>
      </div>
    </section>
`;
}

function main() {
  const filePath = path.join(ROOT, "national-archive.html");
  const html = fs.readFileSync(filePath, "utf8");
  if (!html.includes(START) || !html.includes(END)) {
    throw new Error("ATSUGI archive markers are missing. Add ATSUGI_ARCHIVE_START and ATSUGI_ARCHIVE_END before running.");
  }
  const records = listSchoolData();
  const replacement = `${START}${renderAtsugiSection(records)}    ${END}`;
  const next = html.replace(new RegExp(`${START}[\\s\\S]*?${END}`), replacement);
  const changed = writeFileIfChanged(filePath, next);
  console.log(`Updated national-archive.html (${changed ? "changed" : "unchanged"}).`);
}

if (require.main === module) {
  main();
}
