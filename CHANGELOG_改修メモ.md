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

### timeline.html / shizuoka-incident.html / guideline.html / compliance.html

SNSクローラー向けに、静的HTML本体へXカード画像まわりのメタタグと `css/refine.css?v=refine1` の読み込みを直接反映した。

- `twitter:image:alt` を追加
- `css/refine.css?v=refine1` を読み込み
- canonical 周辺の整形
- 本文、章立て、リンク、画像、ナビゲーションは変更していない

### index.html

トップページに残っていた空の `entry-section` をHTML本体から削除した。

- 削除は空セクション2行のみ
- 本文、リンク、画像、ナビゲーションは変更していない

### PTA運営適正化ガイドブック_第4版_改訂本文.html

ガイドブック本文HTMLについて、表示時補正に頼らずHTML本体へ直接反映した。

- 表紙タイトルを `h1 class="cover-title"` に修正
- 表紙サブタイトルを行政向け説明資料として通りやすい表現へ調整
- 「癒着」表現を「公私混同」等へ調整
- 本文の論理、章立て、リンク、CSS、JSは変更していない

## 確認済み

- `main` は最新コミットに一致している
- open PR は残っていない
- `index.html` の空 `entry-section` は `main` 上で削除済み
- ガイドブック本文HTMLは `main` 上で `h1` 化・表現調整済み
- `guide-board.html` には、確認時点で「癒着」「公務には変わりません」「構造的にできません」は残っていない

## 残課題

### ブラウザ表示確認

ブラウザ表示確認は未実施。作業環境側でブラウザ実行が管理者制限により止まるため、できたとは記録しない。

最低限、以下の公開URLを目視確認する必要がある。

- `https://ptaorg.github.io/`
- `https://ptaorg.github.io/PTA運営適正化ガイドブック_第4版_改訂本文.html`
- `https://ptaorg.github.io/timeline.html`
- `https://ptaorg.github.io/compliance.html`

### 作業ブランチ整理

今回の作業で作成した `fix/...` ブランチは、main反映後の確認が終わってから削除する。

### 画像ファイル

`assets/og-image-popc-en.png` は、リモート側に既にPNGとして存在しているため上書きしていない。ZIP内画像は拡張子と実体形式に不整合があったため、上書き対象から除外した。
