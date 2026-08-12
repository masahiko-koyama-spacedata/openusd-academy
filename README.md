# OpenUSD Academy

日本でいちばんわかりやすいOpenUSD学習教材を目指す、静的なマルチページWebサイトです。

## ローカルで見る

`index.html` をブラウザで開いてください。ビルドや依存パッケージのインストールは不要です。簡易サーバーを使う場合は、プロジェクト直下で `python3 -m http.server 8000` を実行し、`http://localhost:8000/` を開きます。

### VS CodeでUSDをすぐ確認する

VS Codeで`.usd`または`.usda`ファイルを開き、`⌘⇧B`を押します。現在のファイルを`usdchecker`で検証し、成功した場合だけ`usdrecord`で描画してプレビューを開きます。ファイルに`ShotCam`があればそれを使い、無ければ自動のカメラになります。

その他のタスクは、コマンドパレットの「Tasks: Run Task」から選べます。

| タスク | 内容 |
| --- | --- |
| USD: Validate Current File | `usdchecker`だけを実行する |
| USD: Show Scenegraph (usdtree) | 階層をSpecifierと型名つきで表示する |
| USD: Show Composed Result (usdcat --flatten) | 合成後の中身を1枚のUSDAとして表示する |
| Academy: Check Site | 全ページのリンクと必須要素を検査する |
| Academy: Rebuild Curriculum | 学習順序・章ページ・前後ナビ・STEP番号を再生成する |

`usdview`はこのMacに入っていないため使いません。描画はすべて`usdrecord`で行います。

### 教材の画像を作り直す

レッスンの描画結果は、macOS標準のApple USD Tools（`/usr/bin/usdrecord`）で`examples/`のUSDAから生成しています。各画像のキャプションに、使用したファイル名・バージョン・撮影環境を記載しています。

```bash
usdchecker examples/lesson-24b/uniform.usda
usdrecord --camera ShotCam --imageWidth 800 -c high \
  examples/lesson-24b/uniform.usda assets/images/lesson-24b/uniform.png
```

## 編集方針

- HTMLを教材のcanonical source（正本）とする
- レッスン執筆前に [NVIDIA Learn OpenUSD](https://docs.nvidia.com/learn-openusd/latest/index.html) を確認する
- 公式情報とAcademy独自の補足を明示的に分ける
- JavaScriptが無効でも本文とナビゲーションを読めるようにする
- レッスンの必須構成は `AGENTS.md` に従う
- 学習順序は `tools/reorder.py` の `PLAN` を正本とし、カリキュラムと前後ナビを生成する
- 用語集は `tools/gen_glossary.py` の `TERMS` を正本とし、HTMLとMarkdownを生成する
- 変更後は `python3 tools/check_site.py` でリンクと必須要素を検査する
- 学習順序の先取りは `python3 tools/check_order.py` で確認する

複数のPCで編集するときは、[複数PCでのGit運用](CONTRIBUTING.md)に従ってブランチを分け、GitHub経由で変更を引き継ぎます。

## 構成

```text
.
├── index.html          サイトの入口。STEP単位の学習コース
├── curriculum.html     全STEPの一覧（tools/reorder.py が生成）
├── glossary.html       サイト全体の用語集（tools/gen_glossary.py が生成）
├── curriculum.md       curriculum.html と同じ内容のMarkdown
├── glossary.md         glossary.html と同じ内容のMarkdown
├── lessons/            レッスン本体のHTML（正本）
├── examples/           各レッスンのUSDAサンプル
├── assets/
│   ├── css/style.css
│   ├── js/app.js
│   └── images/         usdrecordで生成した描画結果
└── tools/              並び順・用語集の生成と、リンク検査
```

## 現在の状態

全15章・91STEPをすべて収録しています。各レッスンのHTMLを正本とし、共通スタイルとテーマ切り替えだけを `assets/` から読み込みます。章ごとに、全体像をまとめた大単元ページを `chapters/` に置いています。

**読者に見せる番号はSTEPだけです。** ファイル名の数字（`24a-constant.html` など）は教材を追加してきた順に付いた識別子で、学習順とは一致しません。ページ本文・見出し・前後リンクのSTEP番号は `tools/reorder.py` が一括で振り直すので、手で書きません。
