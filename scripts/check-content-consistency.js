const fs = require('fs');
const path = require('path');

const root = path.join(__dirname, '..');
const forbidden = [
  { text: 'https://ptaorg.github.io/donate/', label: '旧寄付URL' },
  { text: '運営チェックアプリ', label: '旧運営チェック名称' },
  { text: 'PTAオプトアウト加入の無効性', label: '旧オプトアウト記事名' },
];

const ignoredDirs = new Set(['.git', 'node_modules']);
const checkedExtensions = new Set(['.html', '.js', '.mjs']);
const findings = [];

function walk(dir) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (ignoredDirs.has(entry.name)) continue;
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      walk(full);
      continue;
    }
    if (!entry.isFile() || !checkedExtensions.has(path.extname(entry.name))) continue;
    const text = fs.readFileSync(full, 'utf8');
    for (const rule of forbidden) {
      if (text.includes(rule.text)) {
        findings.push(`${path.relative(root, full)}: ${rule.label} (${rule.text})`);
      }
    }
  }
}

walk(root);

if (findings.length) {
  console.error('Content consistency check failed:');
  for (const finding of findings) console.error(`- ${finding}`);
  process.exit(1);
}

console.log('Content consistency check passed.');
