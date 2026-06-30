const fs = require('fs');
const path = require('path');

const ROOT = path.join(__dirname, '..');
const SKIP = new Set(['.git', 'node_modules', 'assets', 'downloads']);

function walk(dir) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (SKIP.has(entry.name)) continue;
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) walk(full);
    else if (entry.isFile() && entry.name.endsWith('.html')) {
      const before = fs.readFileSync(full, 'utf8');
      const after = before
        .replace(/href=(['"])\/?research\.html([#?][^'"]*)?\1/g, 'href=$1/research-index.html$2$1')
        .replace(/href=(['"])\/?reality\.html([#?][^'"]*)?\1/g, 'href=$1/compliance.html$2$1');
      if (after !== before) fs.writeFileSync(full, after, 'utf8');
    }
  }
}

function redirectPage(title, description, target) {
  return `<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,follow">
<meta http-equiv="refresh" content="0;url=${target}">
<link rel="canonical" href="https://ptaorg.com${target}">
<title>${title}｜PTA適正化推進委員会</title>
<meta name="description" content="${description}">
<style>body{margin:0;background:#f4f7fa;color:#172033;font-family:-apple-system,BlinkMacSystemFont,'Noto Sans JP',sans-serif}.redirect{width:min(calc(100% - 36px),720px);margin:12vh auto;padding:30px;background:#fff;border:1px solid #d9e3ed;border-left:7px solid #176c72;border-radius:0 16px 16px 0;box-shadow:0 12px 30px rgba(15,39,66,.08)}h1{font-size:clamp(1.35rem,4vw,2rem);line-height:1.5;color:#102c4a}p{line-height:1.9}a{color:#075f8c;font-weight:800}</style>
</head>
<body><main class="redirect"><h1>${title}</h1><p>${description}</p><p><a href="${target}">統合先のページを開く</a></p></main></body>
</html>
`;
}

walk(ROOT);

const researchIndex = path.join(ROOT, 'research-index.html');
let research = fs.readFileSync(researchIndex, 'utf8');
research = research
  .replace('<h2>このハブの使い方</h2>', '<h2>資料を検証するときの4原則</h2>')
  .replace('このハブは、リンク集ではありません。PTA問題を資料から検証するために、どの順番で資料を読み、どのページで論点を整理し、どの段階で学校・PTA・教育委員会への照会に落とすかを決める入口です。', '資料の量より、論点・作成主体・根拠・次の照会を分けることが重要です。以下の4原則で読み方を揃えてから、必要な一次資料へ進みます。');
fs.writeFileSync(researchIndex, research, 'utf8');

fs.writeFileSync(path.join(ROOT, 'research.html'), redirectPage(
  '研究・資料ハブは統合されました',
  '法制度、行政回答、実物資料、検証方法の入口を「研究・資料ハブ」に一本化しました。',
  '/research-index.html'
), 'utf8');

fs.writeFileSync(path.join(ROOT, 'reality.html'), redirectPage(
  '現場実例ページは統合されました',
  'みなし加入、会費徴収、個人情報、教職員関与などの構造説明と実物資料を「PTA運営の現場実例」に一本化しました。',
  '/compliance.html'
), 'utf8');

console.log('Consolidated research.html and reality.html');
