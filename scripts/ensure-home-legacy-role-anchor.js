const fs = require('fs');
const path = require('path');

const INDEX_PATH = path.join(__dirname, '..', 'index.html');
const html = fs.readFileSync(INDEX_PATH, 'utf8');

if (html.includes('id="audience-gateway"')) {
  console.log('legacy audience-gateway anchor already exists; no changes made.');
  process.exit(0);
}

const marker = '  <section class="home-roles-section" id="roles" aria-labelledby="roles-title">';
const alias = '  <span id="audience-gateway" class="home-anchor-alias" aria-hidden="true"></span>\n';

if (!html.includes(marker)) {
  console.error('roles section marker not found; index.html was not changed.');
  process.exit(1);
}

const next = html.replace(marker, alias + marker);
fs.writeFileSync(INDEX_PATH, next, 'utf8');
console.log('inserted the backward-compatible audience-gateway anchor before the roles section.');
