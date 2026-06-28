# サイト保守メモ

このリポジトリでは、本文HTMLを正とし、JavaScriptは検索、ナビゲーション、補助表示に限定する方針で運用します。

## 生成ファイル

検索インデックスとサイトマップは、次のコマンドで生成します。

```bash
npm run generate:sitemap
npm run generate:search
```

まとめて生成する場合は次を使います。

```bash
npm run generate:all
```

## 生成ファイルの確認

生成結果がコミット済みファイルと一致しているかを確認します。

```bash
npm run check:generated
```

## `site.js` のキャッシュ更新

`js/site.js` を更新した場合、HTML側の読み込み指定も更新します。

```bash
npm run maintenance:bump-site-js -- 89
```

数字は `js/site.js` の版数に合わせて変更します。

## 注意

- 重要本文を JavaScript で差し替えない。
- トップページや主要解説ページの本文は HTML に置く。
- `data/site-search-index.js` は検索用の生成ファイルとして扱う。
- 大きなHTMLの置換は、本文変更とキャッシュ更新を分けて行う。
