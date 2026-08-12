# OpenUSD Academy — Contributor Rules

## Mission

日本でいちばんわかりやすいOpenUSD学習教材を作る。

最終的にはNVIDIA Learn OpenUSDの主要学習領域を初学者向けに収めた教科書規模を目指す。量を増やすときも一つのレッスンへ概念を詰め込まず、現在のレッスンと同程度の長さ・説明密度・難易度を保つ。

## Source policy

1. レッスンを書く、または技術内容を変更する前に、必ず [NVIDIA Learn OpenUSD](https://docs.nvidia.com/learn-openusd/latest/index.html) の該当ページを確認し、技術的な記述をOpenUSD公式仕様・APIリファレンスと照合する。
2. OpenUSD公式仕様・APIリファレンスを技術上の一次情報、NVIDIA Learn OpenUSDを主要な学習資料として扱い、レッスン末尾に確認した公式ページへのリンクと確認日を記載する。
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
7. 記法の解説 — 構文・インデント・波括弧・引用符・Path・Asset Path（`@ @`）を、**その記号が初めて出るレッスンで**具体的に説明する。全レッスンで毎回繰り返す必要はない（100レッスンで繰り返すと本題が埋もれるため、2026-08-12にこの方針へ変更した）。初出は次のとおりで、`tools/check_site.py` が検査する。
   - インデント・波括弧・引用符・Path … 第1章（STEP 01–05）
   - Asset Path（`@ @`）… References の回
   新しい記号を導入するレッスンでは、Beginner notes か本文でその場で説明する。
8. よくある間違い — 症状、原因、直し方を示す
9. 用語集 — そのレッスンで初出の語を末尾にまとめる
10. 公式リファレンス — URL、ページ名、確認日を記載する

## Design and quality

- Appleのプロダクトページを思わせる、余白・階層・可読性を重視したデザインにする（Appleの商標・素材は模倣しない）。
- デフォルトは常にライトモードとし、背景 `#FFFFFF`、本文 `#1D1D1F`、補助文字 `#6E6E73`、アクセント `#0071E3` を基本にする。OS設定による自動ダーク化はしない。
- ライト／ダーク両モードをサポートし、ダークモードは手動切り替えにする。
- 全ページを中央寄せの単一カラムで構成し、本文幅はおよそ820–900pxに収める。
- 読者の視線が上から下へ自然に進む順序を優先し、コア教材を左右に分割しない。
- USDA → 直下の説明 → 段階的な図 → Python → 対応関係、のように近い情報を連続して配置する。
- 一画面につき主題を一つに絞り、コードは小さな段階で提示する。離れた領域の見比べを初学者に要求しない。
- カードを多用しない。通常の説明は白地と余白、細い区切り線で構成する。
- 枠線や色付き背景は「今日これだけ」、OpenUSD Academy Note、警告、コード、クイズに限定する。
- アニメーションは短いフェードまたは小さな縦方向の表示だけにし、`prefers-reduced-motion` を尊重する。
- セマンティックHTML、キーボード操作、十分なコントラスト、レスポンシブ表示を維持する。
- コードは実行または妥当性を確認し、説明と出力が一致するようにする。
- 実習では「VS CodeでUSDAを書く → `usdchecker`で検証する → `usdview`でStage・Scenegraph・Viewportを確認する」を基本フローにする。
- 目で確認できる概念には、実際のサンプルUSDを開いた`usdview`画面を付ける。装飾画像ではなく、コードとScenegraphの対応が分かる画像を優先する。
- スクリーンショットには、使用したサンプルファイル、OpenUSDのバージョン、撮影環境を記録する。
- 見出しの末尾に句点「。」を付けない。
- USDAコードは暖色、Pythonコードは青系の文字色で区別し、色だけに依存せずラベルも付ける。

## Git and publishing

- 変更は目的ごとに小さくコミットする。
- GitHubへの接続、remote追加、push、公開、デプロイは必ず事前に利用者の承認を得る。

## ローカルのビルド環境（2026-08-12）

`usdview` は `pip install usd-core` に含まれないため、OpenUSD v26.08 をソースからビルドして用意した。

- ソース: `~/Developer/OpenUSD`（tag `v26.08`）
- インストール先: `~/Developer/usd-install`（`bin/usdview`、`bin/usdrecord` ほか）
- ビルド用venv: `~/Developer/usd-build-env`（cmake / PySide6 / PyOpenGL / Jinja2 / numpy）
- 実行時: `PYTHONPATH=~/Developer/usd-install/lib/python3.9/site-packages`
- 完全版Xcodeが無くCommand Line Toolsだけの環境なので、`build_scripts/apple_utils.py` の
  `GetXcodeVersion()` に CLT 版を返すフォールバックを入れている（元は `apple_utils.py.orig`）

**画像の出どころを撮影方法ごとに分ける。**

- Apple USD Tools 0.25.2 の `/usr/bin/usdrecord` … 初期のレッスンの画像
- ソースからビルドした v26.08 の `usdrecord --disableCameraLight` … STEP 34 以降のライトを扱う画像
- `usdview` のウィンドウキャプチャ … STEP 93

`usdrecord` は既定でカメラ位置にライトを足す。自分の書いた Light だけを見たいときは
`--disableCameraLight` を付ける。付けないと intensity を 0 にしても絵が変わらない。

レッスンのコード検証には `~/Developer/usd-practice/.venv`（usd-core 0.26.8）を使う。
