# site.js キャッシュ更新手順

`js/site.js` を更新した後は、HTML 側の読み込み指定も同じ版数に揃えます。

## 1. 変更予定を確認する

```bash
npm run maintenance:bump-site-js:dry-run
```

このコマンドは、変更予定の HTML ファイルを一覧表示します。実ファイルは変更しません。

## 2. 読み込み版数を更新し、検査する

```bash
npm run maintenance:bump-site-js:check
```

このコマンドは、HTML 側の `site.js` 読み込み指定を `v=89` に更新し、その直後に版数検査を実行します。

個別に実行する場合は、次の順で行います。

```bash
npm run maintenance:bump-site-js -- 89
npm run check:site-js-version
```

`89` は現在の `js/site.js` 版数です。次に `site.js` を更新した場合は、その版数に合わせて変更します。

## 3. 総合チェックを行う

```bash
npm run check:all
```

`check:all` は、サイト構造、生成ファイル、`site.js` 版数をまとめて確認します。

## 注意

- 大きい HTML を手作業で全文置換しない。
- まず dry-run で対象ファイルを確認する。
- 版数更新と本文修正は別コミットに分ける。
- `site.js` で本文を差し替えず、本文は HTML を正本にする。
