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

## check_order.py

学習順序の検査です。「まだ習っていないことに依存していないか」を2つの観点で検出します。

- 前方参照リンク: STEP N のページから STEP M（M > N）へのリンク
- 用語の先取り: STEP N の本文が、STEP M（M > N）の用語集で初出とされる語を使用

どちらも一律に禁止ではありません（次の回への案内は妥当）。一覧で出すので、人が見て判断します。

```bash
python3 tools/check_order.py
```

### check_site.py が見るもの（2026-08-12 追加分）

- 相対リンク・タグの対応・img の alt・レッスン必須要素・見出しの句点
- 前後ナビの行き先とラベルが学習順序と一致しているか
- **掲載中のUSDAを `usdcat` で実際に解析する**（断片・端末出力は除外）
- **Python例の import 漏れ**（ページ内でそこまでに import されたものを積み上げて判定。コメント内の出現は使用扱いにしない）
- **xformOp の型が Python API の既定精度と一致するか**（`AddScaleOp()` は float、`AddTranslateOp()` は double）
- 必須セクション（mapping / Diagram / USDAカード / Pythonカード / よくある間違い）
- 記法（インデント・波括弧・引用符・Path・Asset Path）の説明が初出のレッスンにあるか

**問題が1件でもあれば終了コード 1 を返す。** 以前は常に 0 を返していたため、
エラーを表示していてもシェルやCIからは成功として扱われていた。
