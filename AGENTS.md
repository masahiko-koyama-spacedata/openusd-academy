# OpenUSD Academy — Contributor Rules

## Mission

日本でいちばんわかりやすいOpenUSD学習教材を作る。

## Source policy

1. レッスンを書く、または技術内容を変更する前に、必ず [NVIDIA Learn OpenUSD](https://docs.nvidia.com/learn-openusd/latest/index.html) の該当ページを確認する。
2. NVIDIA Learn OpenUSDを一次情報とし、レッスン末尾に確認した公式ページへのリンクと確認日を記載する。
3. 公式資料に基づく内容には「公式」、日本語化・比喩・補足・独自図解には「Academy補足」と明記する。
4. 公式資料を長く転載せず、自分の言葉で説明する。引用する場合は必要最小限にする。

## Canonical format

- 教材の正本はHTML。Markdownやノートブックは補助資料としてのみ扱う。
- レッスンは `lessons/NN-slug.html` に置き、相対リンクで単体表示できるようにする。
- 本文はJavaScriptなしでも完全に読めること。JavaScriptはテーマや小さな操作補助に限定する。

## Required lesson structure

すべてのレッスンに、次の順序を基本として含める。

1. 「今日これだけ」— 一文で到達点を示す
2. 概念図 — HTML/CSS、画像、またはアクセシブルな図。代替テキストを付ける
3. USDA例 — 完全でコピー可能な最小例
4. Python例 — USDA例と同じ結果を作る最小例
5. USDA → Python対応表 — 行や概念の対応を明示する
6. 初学者向け解説 — 前提知識を仮定しない
7. 記法の解説 — 構文、インデント、波括弧、引用符、パスを具体的に説明する
8. よくある間違い — 症状、原因、直し方を示す
9. 用語集 — そのレッスンで初出の語を末尾にまとめる
10. 公式リファレンス — URL、ページ名、確認日を記載する

## Design and quality

- Appleのプロダクトページを思わせる、余白・階層・可読性を重視したデザインにする（Appleの商標・素材は模倣しない）。
- ライト／ダーク両モードをサポートする。
- アニメーションは控えめにし、`prefers-reduced-motion` を尊重する。
- セマンティックHTML、キーボード操作、十分なコントラスト、レスポンシブ表示を維持する。
- コードは実行または妥当性を確認し、説明と出力が一致するようにする。

## Git and publishing

- 変更は目的ごとに小さくコミットする。
- GitHubへの接続、remote追加、push、公開、デプロイは必ず事前に利用者の承認を得る。
