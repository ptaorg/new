const { spawnSync } = require("child_process");

function run(command, args) {
  const result = spawnSync(command, args, { stdio: "inherit", shell: process.platform === "win32" });
  if (result.status !== 0) process.exit(result.status || 1);
}

function main() {
  run("node", ["scripts/generate-sitemap.js"]);
  run("node", ["scripts/generate-search-index.js"]);
  const diff = spawnSync("git", ["diff", "--", "sitemap.xml", "data/site-search-index.js"], {
    encoding: "utf8",
    shell: process.platform === "win32"
  });
  if (diff.status !== 0) process.exit(diff.status || 1);
  if (diff.stdout.trim()) {
    console.error("Generated files are out of date. Run npm run generate:sitemap && npm run generate:search, then commit the result.");
    console.error(diff.stdout);
    process.exit(1);
  }
  console.log("Generated files are up to date.");
}

if (require.main === module) {
  main();
}
