const fs = require('fs');
const path = require('path');

const INDEX_PATH = path.join(__dirname, '..', 'index.html');
let html = fs.readFileSync(INDEX_PATH, 'utf8');

const replacements = [
  ['font-size:clamp(2rem, 4.2vw, 3.5rem);', 'font-size:clamp(1.65rem, 3.2vw, 2.65rem);'],
  ['line-height:1.22;', 'line-height:1.3;'],
  ['letter-spacing:-.035em;', 'letter-spacing:-.02em;'],
  ['.home-photo-hero-title{font-size:clamp(1.72rem, 8vw, 2.45rem);}', '.home-photo-hero-title{font-size:clamp(1.38rem, 6.2vw, 1.95rem);}'],
];

let changed = false;
for (const [from, to] of replacements) {
  if (html.includes(to)) {
    continue;
  }
  if (!html.includes(from)) {
    console.error(`expected CSS fragment not found: ${from}`);
    process.exit(1);
  }
  html = html.replace(from, to);
  changed = true;
}

if (!changed) {
  console.log('hero title size already tuned; no changes made.');
  process.exit(0);
}

fs.writeFileSync(INDEX_PATH, html, 'utf8');
console.log('tuned homepage hero title size.');
