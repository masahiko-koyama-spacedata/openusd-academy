# tools

教材の一貫性を保つための補助スクリプトです。教材の正本はHTMLで、これらはHTMLを生成・検査するために使います。

いずれも`pxr`（usd-core）を必要としません。標準ライブラリだけで動きます。

## reorder.py

学習順序の単一の正本です。`PLAN`に章とレッスンの並びを書き、実行すると次の2つを更新します。

- `curriculum.html` と `curriculum.md` をSTEP番号付きで再生成する
- 各レッスンの `<nav class="lesson-footer-nav">` を、同じ並びの前後リンクへ書き換える

レッスンを追加したら、`PLAN`の該当行のファイル名を`None`から実ファイル名へ変えて実行します。

```bash
python3 tools/reorder.py
```

## check_site.py

全HTMLページを検査します。相対リンクとimgの実在、タグの対応、`img`のalt、レッスン必須要素（site-header、app.js、前後ナビ、公式リファレンス、用語集、確認日）、見出し末尾の句点を確認します。

```bash
python3 tools/check_site.py
```

## gen_glossary.py

サイト全体の用語集の単一の正本です。`TERMS`に用語と定義を書き、`glossary.html`と`glossary.md`を並べ替えて生成します。

```bash
python3 tools/gen_glossary.py
```
