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

- USDAの基本構文
- Pythonと`pxr`モジュール
- MetadataとSchema
- Xformと階層
- Time Sample

## 3. コンポジション

- LayerとLayer Stack
- Sublayer
- ReferenceとPayload
- Variant Set
- Inherits、Specializes、強度順序

## 4. アセット設計

- Asset Structure
- Model KindとModel Hierarchy
- Asset Interface
- Workstreamと集約
- Reference/Payloadパターン

## 5. パイプライン開発

- データ交換
- GeometryとMaterialの抽出
- 変換と検証
- Scenegraph Instancing
- Point Instancing

> **Academy方針:** 各レッスンでは、公式の概念を改変せず、図解・USDA/Python対訳・日本語でのつまずき対策を加えます。
