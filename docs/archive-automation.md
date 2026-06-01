# 全国資料館 自動生成基盤

この仕組みは、学校別資料ページ、厚木市セクション、sitemap.xml を手作業ではなく JSON から生成するための基盤です。今回の段階ではローカルまたは Codex 上での手動実行を前提にし、GitHub Actions による自動生成は次段階の検討事項とします。

## 目的

- PDF・画像資料を学校ごとに配置する
- 学校別 JSON に評価・確認事項を書く
- JSON から学校別 HTML を生成する
- national-archive.html の学校一覧と評価バッジを JSON から更新する
- sitemap.xml に実在する学校別ページ URL を追加する
- 将来的に PDF 画像化、OGP 画像生成、AI 評価案生成、Google Sheets / GAS 連携へ拡張する

## ディレクトリ

- 学校別 JSON: `data/schools/{自治体slug}/{school-slug}.json`
- JSON schema: `data/schema/school-archive.schema.json`
- 学校別ページ: `archive/{自治体slug}/{school-slug}/index.html`
- 資料画像: `assets/archive/{自治体slug}/{school-slug}/`
- OGP 画像: `assets/ogp/{自治体slug}/{school-slug}.png`
- PDF 資料: `assets/documents/` 以下の該当カテゴリ

## 学校別 JSON の主な項目

- `municipality`: 自治体名
- `prefecture`: 都道府県名
- `schoolName`: 学校名
- `schoolType`: 小学校 / 中学校 等
- `slug`: URL に使う学校 slug
- `basePath`: `/archive/atsugi/echi-es/` のような公開パス
- `canonical`: `https://ptaorg.com/...` の正規 URL
- `ogImage`: OGP 画像の公開パス
- `status`: 評価ラベル
- `statusClass`: 評価色 CSS class
- `materials`: 確認資料、画像、PDF 掲載状況
- `confirmedFacts`: 資料上確認できる事実
- `unconfirmedPoints`: 資料上確認できない点
- `riskFlags`: 疑義フラグ
- `evaluation`: 当委員会の評価文
- `humanReviewRequired`: 人による確認が必要か

AI 評価案をそのまま確定評価として扱わないでください。将来的には `aiDraftEvaluation` と `evaluation` を分け、確定評価には必ず人の確認を経た内容だけを入れる運用にします。

## 評価ラベル対応

| 評価ラベル | CSS class |
| --- | --- |
| 重大リスク | `eval-critical` |
| 問題あり | `eval-problem` |
| 要確認 | `eval-warning` |
| 資料不足 | `eval-insufficient` |
| 適正化モデル | `eval-good` |
| 未評価 | `eval-pending` |
| 評価準備中 | `eval-pending` |

## 生成コマンド

```bash
npm run generate:all
```

個別に実行する場合:

```bash
npm run generate:schools
npm run generate:archive
npm run generate:sitemap
```

## スクリプト

- `scripts/generate-school-pages.js`
  - `data/schools/*/*.json` を読み込み、学校別 HTML を生成します。
  - GA4 タグ、canonical、OGP / X カード meta、評価色、PDF 保存ボタンを出力します。
  - 存在しない画像や PDF は出力しません。

- `scripts/generate-national-archive.js`
  - `national-archive.html` の `ATSUGI_ARCHIVE_START` / `ATSUGI_ARCHIVE_END` の範囲だけを更新します。
  - マーカーがない場合はエラー終了し、ページ全体を書き換えません。

- `scripts/generate-sitemap.js`
  - 公開 HTML と JSON 由来の学校別 URL から `sitemap.xml` を生成します。
  - 正規 URL は `https://ptaorg.com/` を使います。

## 手動確認が必要な項目

- 掲載する画像に個人情報、印影、口座情報、QR コード等が含まれていないか
- PDF リンクが実在し、公開してよい資料か
- 入会申込書の有無、学校徴収金との混在、個人情報提供、役員選出などの評価が資料に基づいているか
- OGP 画像が実在するか
- 生成後の `git diff` に意図しない大量削除がないか
- `archive/atsugi/*/index.html` の GA4 タグが重複していないか

## 将来拡張案

- Google Sheets をマスター台帳にし、GAS またはエクスポート JSON から `data/schools/` を更新する
- PDF から公開用 redacted 画像を生成するワークフローを追加する
- OGP カード画像を JSON から自動生成する
- OpenAI API で「AI 評価案」を作成し、人間レビュー後に `evaluation` へ反映する
- GitHub Actions で JSON 変更時に `npm run generate:all` を実行し、差分確認後に公開する
