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

## 構成

```text
.
├── index.html
├── curriculum.html
├── glossary.html
├── curriculum.md
├── glossary.md
├── lessons/
│   └── 01-reading-usda.html
└── assets/
    ├── css/style.css
    └── js/app.js
```

## 現在の状態

Lesson 01「はじめてのUSDAを読む」を公開中です。`lessons/01-reading-usda.html` はHTMLを正本とし、共通スタイルとテーマ切り替えだけを `assets/` から読み込みます。公開・ホスティング・GitHub接続は行っていません。
