# OpenUSD Academy カリキュラム

このカリキュラムは、[NVIDIA Learn OpenUSD](https://docs.nvidia.com/learn-openusd/latest/index.html) の学習領域を一次情報として確認し、日本語の初学者が段階的に進めるようAcademy独自に整理した計画です（確認日: 2026-08-04）。各レッスンの内容は執筆時に該当する公式ページを再確認します。

## 1. OpenUSDの土台

- **Lesson 01:** [はじめてのUSDAを読む](lessons/01-reading-usda.html) — Stage、Prim、Xform、名前、Pathを短いUSDAから一行ずつ読む
- **Lesson 02:** [OpenUSDとは何か](lessons/02-what-is-openusd.html) — シーン記述・合成・共同作業の土台を知る
- **Lesson 03:** [Stage・Prim・Property](lessons/03-stage-prim-property.html) — 全体、構成要素、情報を分ける
- **Lesson 04:** [AttributeとRelationship](lessons/04-attributes-relationships.html) — 値とつながりを読み分ける
- **Lesson 05:** [Prim PathとProperty Path](lessons/05-prim-property-paths.html) — Stage内の対象を正確に指す
- **Lesson 06:** [USDA・USDC・USD・USDZ](lessons/06-usd-file-formats.html) — 中身と用途でファイル形式を選ぶ

## 2. シーンを記述する

- **Lesson 07:** [USDAの基本構文](lessons/07-usda-syntax.html) — 型・名前・波括弧・Propertyを読む
- **Lesson 08:** [Pythonとpxrモジュール](lessons/08-python-pxr-modules.html) — Usd・Sdf・Gf・UsdGeomを使い分ける
- **Lesson 09:** [MetadataとSchema](lessons/09-metadata-schemas.html) — 補助情報とデータの設計図を分ける
- **Lesson 10:** [Xformと階層](lessons/10-xform-hierarchy.html) — 親の変換が子へ届く仕組みを知る
- **Lesson 11:** [Time CodeとTime Sample](lessons/11-time-codes-samples.html) — 時点と値で時間変化を記述する

## 3. コンポジション

- **Lesson 12:** [コンポジションを一本につなぐ](lessons/12-composition.html) — Layer、Sublayer、Reference、Payload、Variant、Inherits、Specializes、LIVERPS

## 4. アセット設計

- **Lesson 13:** [再利用できるアセット設計](lessons/13-asset-structure.html) — Asset Structure、Model Kind、Asset Interface、Workstream、Reference/Payload Pattern

## 5. パイプライン開発

- **Lesson 14:** [データを運ぶパイプライン](lessons/14-data-pipelines.html) — データ交換、GeometryとMaterialの抽出、変換、検証、Scenegraph Instancing、Point Instancing

> **Academy方針:** 各レッスンでは、公式の概念を改変せず、図解・USDA/Python対訳・日本語でのつまずき対策を加えます。
