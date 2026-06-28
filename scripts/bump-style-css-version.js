const fs = require('fs');
const path = require('path');

const ROOT = path.join(__dirname, '..');
const TARGET_VERSION = process.argv[2] || '20260628-hero';
const DRY_RUN = process.argv.includes('--dry-run');
const SKIP_DIRS = new Set(['.git', '.claude', 'assets', 'data', 'js', 'scripts', 'tools', 'node_modules', 'ホーム']);
const STYLE_PATTERN = /css\/style\.css(?:\?v=[^"']*)?/g;

const changedFiles = [];

function walk(dir) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (SKIP_DIRS.has(entry.name)) continue;
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      walk(full);
      continue;
    }
    if (!entry.isFile() || !entry.name.endsWith('.html')) continue;

    const text = fs.readFileSync(full, 'utf8');
    if (!text.includes('css/style.css')) continue;

    const next = text.replace(STYLE_PATTERN, `css/style.css?v=${TARGET_VERSION}`);
    if (next !== text) {
      changedFiles.push(path.relative(ROOT, full));
      if (!DRY_RUN) fs.writeFileSync(full, next, 'utf8');
    }
  }
}

walk(ROOT);

if (changedFiles.length === 0) {
  console.log('No style.css references needed updating.');
  process.exit(0);
}

console.log(`${DRY_RUN ? 'Would update' : 'Updated'} ${changedFiles.length} HTML files to css/style.css?v=${TARGET_VERSION}:`);
for (const file of changedFiles) console.log(`- ${file}`);
