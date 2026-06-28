# トップページ最終更新日 反映手順

## 目的

トップページの「最新更新・掲載情報」に、最終更新日を表示する。

表示文言：

```text
最終更新：2026年6月28日
```

## 実行コマンド

Codespaces のターミナルで次を実行する。

```bash
git pull --rebase origin main
node scripts/add-home-latest-updated.js
npm run generate:search
npm run generate:sitemap
git status
git add index.html data/site-search-index.js sitemap.xml
git commit -m "Add homepage latest updated date"
git push
```

## 確認方法

```bash
grep -n "home-latest-updated" index.html
```

または公開ページで次を確認する。

```text
https://ptaorg.com/?check=latest
```

## 注意

- 大型の `index.html` を手作業で全文置換しない。
- 既に `home-latest-updated` がある場合、スクリプトは既存行を更新する。
- 検索インデックスとサイトマップは、本文変更後に再生成する。
