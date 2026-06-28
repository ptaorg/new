#!/usr/bin/env node
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const SITE_JS_PATTERN = /site\.js(?:\?v=([^"']+))?/g;
const SKIP_DIRS = new Set([
  '.git',
  '.claude',
  'assets',
  'css',
  'data',
  'js',
  'node_modules',
  'scripts',
  'tools',
  'ホーム',
]);

const rows = [];

function walk(dir) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      if (SKIP_DIRS.has(entry.name)) continue;
      walk(full);
      continue;
    }

    if (!entry.isFile() || !entry.name.endsWith('.html')) continue;

    const rel = path.relative(ROOT, full).replace(/\\/g, '/');
    const text = fs.readFileSync(full, 'utf8');
    if (!text.includes('site.js')) return;

    SITE_JS_PATTERN.lastIndex = 0;
    const versions = [];
    let match;
    while ((match = SITE_JS_PATTERN.exec(text))) {
      versions.push(match[1] || '(no version)');
    }

    rows.push({ file: rel, versions: [...new Set(versions)] });
  }
}

walk(ROOT);
rows.sort((a, b) => a.file.localeCompare(b.file));

const counts = new Map();
for (const row of rows) {
  for (const version of row.versions) counts.set(version, (counts.get(version) || 0) + 1);
}

console.log('site.js version summary');
for (const [version, count] of [...counts.entries()].sort()) {
  console.log(`- ${version}: ${count}`);
}

console.log('\nFiles');
for (const row of rows) {
  console.log(`- ${row.file}: ${row.versions.join(', ')}`);
}
