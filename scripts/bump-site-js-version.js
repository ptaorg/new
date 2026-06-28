const fs = require("fs");
const path = require("path");
const { ROOT, writeFileIfChanged } = require("./archive-utils");

const TARGET_VERSION = process.argv[2] || "89";
const SKIP_DIRS = new Set([".git", ".claude", "assets", "css", "data", "js", "scripts", "tools", "node_modules", "ホーム"]);
const SCRIPT_RE = /(<script\b[^>]*\bsrc=["'])([^"']*js\/site\.js)(?:\?v=\d+)?(["'][^>]*><\/script>)/gi;

function walkHtml(dir, files = []) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      if (SKIP_DIRS.has(entry.name)) continue;
      walkHtml(full, files);
    } else if (entry.isFile() && entry.name.endsWith(".html")) {
      files.push(full);
    }
  }
  return files;
}

function bumpFile(filePath) {
  const before = fs.readFileSync(filePath, "utf8");
  const after = before.replace(SCRIPT_RE, (_match, prefix, src, suffix) => `${prefix}${src}?v=${TARGET_VERSION}${suffix}`);
  if (after === before) return false;
  return writeFileIfChanged(filePath, after);
}

function main() {
  let matched = 0;
  let changed = 0;
  for (const filePath of walkHtml(ROOT)) {
    const before = fs.readFileSync(filePath, "utf8");
    if (!SCRIPT_RE.test(before)) {
      SCRIPT_RE.lastIndex = 0;
      continue;
    }
    SCRIPT_RE.lastIndex = 0;
    matched += 1;
    if (bumpFile(filePath)) changed += 1;
  }
  console.log(`Bumped js/site.js cache version to v=${TARGET_VERSION}: ${changed}/${matched} files changed.`);
}

if (require.main === module) {
  main();
}
