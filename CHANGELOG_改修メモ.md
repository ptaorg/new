# 改修メモ

最終更新: 2026-06-06

## 反映済み

### documents.html

旧 `documents.html?id=...` 形式のURLを単純リダイレクトで潰さず、資料IDごとに関連ページを案内する互換ページへ修正した。

主な対応ID:

- `yokohama-notice`
- `yokohama-bessi`
- `ppc-personal-info`
- `mext-accounting-notice`
- `mext-koukaikkei-2025`
- `mext-pta-survey-2025`
- `mext-toshin2019`
- `atsugi-pta-notice`
- `guidebook-board`
- `guidebook-pta`
- `pta-voluntary-kamino`

### css/refine.css

既存 `style.css` を直接壊さず、後読みCSSとして以下を追加した。

- 見出し・キッカーの文字の重さを調整
- 本文の行間・余白を調整
- カード類の影を軽くする
- 空の `section` / `entry-section` を非表示
- 本文資料サイトとして読みやすい見た目へ寄せる

### contact.html

- canonical の重複を整理
- OGPを整理
- Xカード画像を明示
- `css/refine.css` を読み込み

### board-responses.html

- canonical の重複を整理
- OGPを整理
- Xカード画像を明示
- `css/refine.css` を読み込み

### js/site.js

巨大HTMLを一括上書きせず、共通補修として以下を追加した。

- `css/refine.css` の自動読み込み
- 空の `entry-section` の非表示
- 重複 canonical の表示時除去
- 旧アンカーリンクの置換
- 旧アンカー互換IDの付与
- ガイドブック表紙タイトルの `h1` 化
- 「癒着」等の強すぎる語句の表示上補正
- 「公務には変わりません」「構造的にできません」の表示上緩和

## 未直接反映

以下のHTMLは、ローカル作業用ファイルでは修正確認済みだが、GitHubコネクタが部分パッチではなく全文差し替え方式のため、本文欠落リスクを避けてまだ直接上書きしていない。

- `timeline.html`
- `shizuoka-incident.html`
- `guideline.html`
- `compliance.html`
- `index.html`
- `guide-board.html`
- `guide-parent.html`
- `guide-pta.html`
- `membership.html`
- `fee-collection.html`
- `report.html`
- `PTA運営適正化ガイドブック_第4版_改訂本文.html`

## 残課題

### 静的HTML本体への twitter:image 追加

`timeline.html`、`shizuoka-incident.html`、`guideline.html`、`compliance.html` は、ローカル作業用ファイルでは `twitter:image` と `twitter:image:alt` の追加を確認済み。

ただし、SNSクローラー向けメタタグはJavaScript補修では不十分な場合があるため、最終的にはHTML本体へ直接反映するのが望ましい。

### ブラウザ表示確認

ブラウザ表示確認は未実施。作業環境側でブラウザ実行が管理者制限により止まるため、できたとは記録しない。

### 画像ファイル

`assets/og-image-popc-en.png` は、リモート側に既にPNGとして存在しているため上書きしていない。ZIP内画像は拡張子と実体形式に不整合があったため、上書き対象から除外した。
