const fs = require('fs');
const path = require('path');

const root = path.resolve(__dirname, '..');
const out = path.join(root, '_site');
const ignored = new Set(['.git', '_site', 'node_modules']);
const textExtensions = new Set(['.html', '.css', '.js', '.xml', '.json', '.webmanifest']);

fs.rmSync(out, { recursive: true, force: true });

function copyTree(source, destination) {
  fs.mkdirSync(destination, { recursive: true });
  for (const entry of fs.readdirSync(source, { withFileTypes: true })) {
    if (ignored.has(entry.name)) continue;
    const from = path.join(source, entry.name);
    const to = path.join(destination, entry.name);
    if (entry.isDirectory()) {
      copyTree(from, to);
      continue;
    }
    if (!entry.isFile()) continue;
    fs.copyFileSync(from, to);
    if (!textExtensions.has(path.extname(entry.name).toLowerCase())) continue;
    let text = fs.readFileSync(to, 'utf8');
    text = text
      .replace(/((?:href|src|action|poster)=["'])\/(?!\/|new\/)/g, '$1/new/')
      .replace(/url\((["']?)\/(?!\/|new\/)/g, 'url($1/new/')
      .replace(/(["'])\/(?!\/|new\/)(?=[^"'\r\n]*["'])/g, '$1/new/');
    fs.writeFileSync(to, text);
  }
}

copyTree(root, out);
fs.writeFileSync(path.join(out, '.nojekyll'), '');
console.log('Built /new/ preview in _site.');
