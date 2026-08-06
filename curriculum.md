# OpenUSD Academy カリキュラム

このカリキュラムは、[OpenUSD公式ドキュメント](https://openusd.org/release/index.html) を技術上の一次情報とし、[NVIDIA Learn OpenUSD](https://docs.nvidia.com/learn-openusd/latest/index.html) を主要な学習資料として照合したうえで、日本語の初学者が段階的に進めるようAcademy独自に整理した計画です（確認日: 2026-08-05）。各レッスンの内容は執筆時に該当する公式ページを再確認します。Lesson 15〜72は予定で、個別HTMLはまだ公開していません。

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
- **Lesson 09A:** [Default Prim](lessons/09a-default-prim.html) — Layerを外から利用するときの入口を決める
- **Lesson 10:** [Xformと階層](lessons/10-xform-hierarchy.html) — 親の変換が子へ届く仕組みを知る
- **Lesson 11:** [Time CodeとTime Sample](lessons/11-time-codes-samples.html) — 時点と値で時間変化を記述する

## 3. コンポジション

- **Lesson 12:** [コンポジションとLIVERPS](lessons/12-composition.html) — 強度順序、SublayerとLocalの関係、V・R・Sの使い分け、Opinionの上書き
- **Lesson 12A:** [SublayerとLayer Stack](lessons/12-sublayers.html) — 同じnamespaceを積み、Local内の強弱を追う
- **Lesson 12B:** [L · Local Opinion](lessons/12-local.html) — 利用側の直接Opinionで上書きする
- **Lesson 12C:** [I · Inherits](lessons/12-inherits.html) — クラスの変更をbroadcastする
- **Lesson 12D:** [V · Variant Sets](lessons/12-variants.html) — 名前付き選択肢を合成する
- **Lesson 12E:** [E · rElocates](lessons/12-relocates.html) — namespace上のPathを移し替える
- **Lesson 12F:** [R · References](lessons/12-references.html) — 階層の接ぎ木とPath変換を追う
- **Lesson 12G:** [P · Payloads](lessons/12-payloads.html) — Load可能な内容を合成する
- **Lesson 12H:** [S · Specializes](lessons/12-specializes.html) — 最も弱いfallbackを共有する

## 4. アセット設計

- **Lesson 13:** [再利用できるアセット設計](lessons/13-asset-structure.html) — Asset Structure、Model Kind、Asset Interface、Workstream、Reference/Payload Pattern

## 5. パイプライン開発

- **Lesson 14:** [データを運ぶパイプライン](lessons/14-data-pipelines.html) — データ交換、GeometryとMaterialの抽出、変換、検証、Scenegraph Instancing、Point Instancing

## 6. Scene Descriptionの部品

- **Lesson 15:** [Scope](lessons/15-scope.html) — 変換を持たず、Primを用途ごとに整理する
- **Lesson 16:** [XformCommonAPI](lessons/16-xform-common-api.html) — 一般的な変換を交換しやすい構成で扱う
- **Lesson 17A:** [Translate](lessons/17a-translate.html) — 位置を三つの軸で記述する
- **Lesson 17B:** [Rotate](lessons/17b-rotate.html) — 回転角とRotation Orderを読む
- **Lesson 17C:** [Scale](lessons/17c-scale.html) — 各軸の倍率を記述する
- **Lesson 17D:** [Pivot](lessons/17d-pivot.html) — 回転と拡縮の中心を決める
- **Lesson 18:** [XformOpOrder](lessons/18-xform-op-order.html) — 変換順序で結果が変わる理由
- **Lesson 19A:** [Kind](lessons/19a-kind.html) — Schema型とModel Hierarchy上の役割を分ける
- **Lesson 19B:** [component](lessons/19b-component.html) — 再利用可能なleaf modelを作る
- **Lesson 19C（予定）:** group — Modelを正しい祖先階層へまとめる
- **Lesson 19D（予定）:** assembly — 公開可能なaggregate Assetを作る
- **Lesson 19E（予定）:** subcomponent — component内部の重要なPrimを示す
- **Lesson 20A（予定）:** metersPerUnit — 長さの尺度をStageへ記録する
- **Lesson 20B（予定）:** upAxis — 上方向をYまたはZで指定する
- **Lesson 20C（予定）:** kilogramsPerUnit — Physicsの質量尺度を記録する

### 後続の優先順

- Value Resolution、Default Value、Time Sample
- Primvars、constant・uniform・vertex・faceVarying interpolation
- UsdLux、DistantLight、SphereLight、area light、DomeLight、intensity、color

## 7. Propertyを深く理解する

- **Lesson 21（予定）:** Attributeの型 — scalar、vector、array
- **Lesson 22（予定）:** Default ValueとTime Sample — 静的な値と時間変化
- **Lesson 23（予定）:** Relationship Target — 一つと複数の対象
- **Lesson 24（予定）:** Custom Properties — Schema外の情報を追加する
- **Lesson 25（予定）:** Primvars — Geometryへ補間可能なデータを渡す
- **Lesson 26（予定）:** Value Resolution — 最終値が決まるまでを追う

## 8. Compositionの基本操作

- **Lesson 27（予定）:** def・over・class — 三つのSpecifier
- **Lesson 28（予定）:** Default Prim — Assetの入口を決める
- **Lesson 29（予定）:** Prim Composition — 複数のPrim Specが一つになる
- **Lesson 30（予定）:** Sublayer — Layer Stackを作る
- **Lesson 31（予定）:** Reference — Assetを再利用する
- **Lesson 32（予定）:** Payload — 必要なときだけロードする
- **Lesson 33（予定）:** Internal ArcとExternal Arc — 同じLayer内と別ファイル

## 9. Compositionを使い分ける

- **Lesson 34（予定）:** Encapsulation — Assetの境界を守る
- **Lesson 35（予定）:** Variant Set — 選択肢を作る
- **Lesson 36（予定）:** Variant Edit Context — 選択肢の中へ書く
- **Lesson 37（予定）:** Inherits — 複数PrimでOpinionを共有する
- **Lesson 38（予定）:** Specializes — 弱いFallbackを作る
- **Lesson 39（予定）:** LIVERPS — 強度順序を一段ずつ追う
- **Lesson 40（予定）:** Prim StackとProperty Stack — 結果の出所を調べる

## 10. Stageを調べて制御する

- **Lesson 41（予定）:** ActiveとInactive — Compositionから除外する
- **Lesson 42（予定）:** LoadとUnload — Payloadを制御する
- **Lesson 43（予定）:** Stage Traversal — Primを順番に調べる
- **Lesson 44（予定）:** Traversal Predicate — 調べるPrimを絞る
- **Lesson 45（予定）:** Model Kinds — 高水準の階層を検索する
- **Lesson 46（予定）:** Hydra — Scene Delegateとレンダリングの入口

## 11. Asset Structureを実践する

- **Lesson 47（予定）:** Asset Entry Point — 参照される入口を作る
- **Lesson 48（予定）:** Asset Interface — 公開する情報を選ぶ
- **Lesson 49（予定）:** Component・Group・Assembly — Kind階層を作る
- **Lesson 50（予定）:** Workstream Layers — 作業をLayerで分ける
- **Lesson 51（予定）:** Asset Parameterization — 下流から変更できる値
- **Lesson 52（予定）:** Reference/Payload Pattern — InterfaceとContentsを分ける
- **Lesson 53（予定）:** Lofting — Payloadを開かず重要情報を見せる

## 12. Data Exchangeを作る

- **Lesson 54（予定）:** Converterの構造 — 入力・変換・出力を分ける
- **Lesson 55（予定）:** Geometry Extraction — 点・法線・UVを対応させる
- **Lesson 56（予定）:** Material Extraction — MaterialとBindingを対応させる
- **Lesson 57（予定）:** Asset Validation — 規則をコードにする
- **Lesson 58（予定）:** Prim Hierarchy Transformation — 階層を目的形へ変える
- **Lesson 59（予定）:** Export Options — 変換条件を利用者へ公開する

## 13. Instancingと大規模シーン

- **Lesson 60（予定）:** Asset Modularity — 再利用単位を決める
- **Lesson 61（予定）:** Scenegraph Instancing — CompositionからPrototypeを作る
- **Lesson 62（予定）:** Nested Instancing — Instanceを階層化する
- **Lesson 63（予定）:** Instance Refinement — Instanceごとの差を付ける
- **Lesson 64（予定）:** Point Instancing — 大量の単純要素を配置する
- **Lesson 65（予定）:** ScenegraphとPointの選択 — 用途と制約を比較する

## 14. 調査・検証・実践

- **Lesson 66（予定）:** usdviewでStageを読む
- **Lesson 67（予定）:** Layer Stackを調べる
- **Lesson 68（予定）:** 壊れたReferenceとPathを直す
- **Lesson 69（予定）:** Pythonで最小Validationを書く
- **Lesson 70（予定）:** 小さなAssetを最初から組み立てる
- **Lesson 71（予定）:** 複数Assetから小さなSceneを作る
- **Lesson 72（予定）:** OpenUSD教材の総復習

> **Academy方針:** 各レッスンは現在と同程度の長さと難易度に保ち、一回に一つの中心概念を扱います。公式の概念を改変せず、図解・USDA/Python対訳・日本語でのつまずき対策を加えます。
