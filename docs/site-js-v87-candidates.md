# site.js v87 候補ページ

GitHub 検索で `site.js?v=87` が残っている候補として出たページの作業メモです。

検索結果は古いインデックスを拾う可能性があるため、正本は次のローカル確認コマンドです。

```bash
npm run report:site-js-version
```

## 候補一覧

- `law-map.html`
- `cases.html`
- `index.html`
- `documents.html`
- `board-responses.html`
- `guideline.html`
- `facilities.html`
- `proper-management.html`
- `edu-board-separation.html`
- `report.html`
- `guide-research.html`
- `membership.html`
- `journal/consumer-contract.html`
- `reality.html`
- `timeline.html`
- `privacy.html`
- `administrative-materials.html`
- `guide-pta.html`
- `fee-collection.html`
- `journal.html`
- `education-board-responsibility.html`
- `guide-parent.html`
- `personnel.html`
- `claim-evidence-ledger.html`
- `audit/index.html`
- `shizuoka-incident.html`
- `compliance.html`

## 推奨作業手順

```bash
npm run report:site-js-version
npm run maintenance:bump-site-js:dry-run
npm run maintenance:bump-site-js:check
npm run check:all
```

## 注意

- 上記は検索結果ベースの候補であり、すでに更新済みのページが混じる可能性があります。
- 大型 HTML は GitHub コネクタ上で全文取得が切れることがあるため、手作業全文置換を避けます。
- 版数更新と本文修正は別コミットにします。
