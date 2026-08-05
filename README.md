# OpenUSD Academy

日本でいちばんわかりやすいOpenUSD学習教材を目指す、静的なマルチページWebサイトです。

## ローカルで見る

`index.html` をブラウザで開いてください。ビルドや依存パッケージのインストールは不要です。簡易サーバーを使う場合は、プロジェクト直下で `python3 -m http.server 8000` を実行し、`http://localhost:8000/` を開きます。

## 編集方針

- HTMLを教材のcanonical source（正本）とする
- レッスン執筆前に [NVIDIA Learn OpenUSD](https://docs.nvidia.com/learn-openusd/latest/index.html) を確認する
- 公式情報とAcademy独自の補足を明示的に分ける
- JavaScriptが無効でも本文とナビゲーションを読めるようにする
- レッスンの必須構成は `AGENTS.md` に従う

複数のPCで編集するときは、[複数PCでのGit運用](CONTRIBUTING.md)に従ってブランチを分け、GitHub経由で変更を引き継ぎます。

## 構成

```text
.
├── index.html
├── curriculum.html
├── glossary.html
├── curriculum.md
├── glossary.md
├── lessons/
│   ├── 01-reading-usda.html
│   ├── 02-what-is-openusd.html
│   ├── 03-stage-prim-property.html
│   ├── 04-attributes-relationships.html
│   ├── 05-prim-property-paths.html
│   └── 06-usd-file-formats.html
└── assets/
    ├── css/style.css
    └── js/app.js
```

## 現在の状態

Section 1〜5のLesson 01〜14を収録しています。NVIDIA Learn OpenUSDの主要領域を細かく学ぶSection 6〜14、Lesson 15〜72を今後追加する計画です。各レッスンのHTMLを正本とし、共通スタイルとテーマ切り替えだけを `assets/` から読み込みます。
