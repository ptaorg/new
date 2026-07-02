# 配布ファイル

PDF本体、ZIP本体、スプレッドシート雛形などの大容量・バイナリファイルは、GitHub Pagesの通常ページとは分けて管理する。

## 推奨

- HTML本文は `starter-kit/` 配下で公開
- PDF/ZIPはGitHub Release添付、または別途配布ページで公開
- Apps Scriptは `starter-kit/implementation/` 配下で管理

## 注意

GitHub Pagesに大容量ファイルを大量に直置きすると、更新や確認が重くなる。公開ページには索引と説明を置き、実ファイルはRelease等に分けるのが安全である。
