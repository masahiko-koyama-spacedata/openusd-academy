# OpenUSD Academy カリキュラム

このカリキュラムは、[OpenUSD公式ドキュメント](https://openusd.org/release/index.html) を技術上の一次情報とし、[NVIDIA Learn OpenUSD](https://docs.nvidia.com/learn-openusd/latest/index.html) を主要な学習資料として照合したうえで、日本語の初学者が段階的に進めるようAcademy独自に整理した計画です（確認日: 2026-08-06）。

> **STEP番号が学習の順番です。** Lesson番号はファイルの識別子で、教材を追加してきた順に付いています。初学者がつまずきにくい順序を優先した結果、Lesson番号とSTEP番号は一致しません。各レッスンの前後リンクもSTEPの順に並んでいるので、上から順にたどれば迷いません。

## 1. まずUSDAを読む

最初の目標は「書く」ではなく「読める」です。短いテキストを一行ずつ読み解きます。

- **STEP 01 · Lesson 01:** [はじめてのUSDAを読む](lessons/01-reading-usda.html) — Stage、Prim、Xform、名前、Pathを短いUSDAから一行ずつ読む
- **STEP 02 · Lesson 02:** [OpenUSDとは何か](lessons/02-what-is-openusd.html) — シーン記述・合成・共同作業の土台を知る
- **STEP 03 · Lesson 03:** [Stage・Prim・Property](lessons/03-stage-prim-property.html) — 全体、構成要素、情報を分ける
- **STEP 04 · Lesson 07:** [USDAの基本構文](lessons/07-usda-syntax.html) — 型・名前・波括弧・Propertyを読む
- **STEP 05 · Lesson 06:** [USDA・USDC・USD・USDZ](lessons/06-usd-file-formats.html) — 中身と用途でファイル形式を選ぶ

## 2. ファイル先頭の約束事

すべての例に出てくるファイル先頭のMetadataを、ここで先に理解しておきます。

- **STEP 06 · Lesson 09A:** [Default Prim](lessons/09a-default-prim.html) — Layerを外から利用するときの入口を決める
- **STEP 07 · Lesson 20A:** [metersPerUnit](lessons/20a-meters-per-unit.html) — 長さの「1」が何メートルかを宣言する
- **STEP 08 · Lesson 20B:** [upAxis](lessons/20b-up-axis.html) — どの軸が上かを宣言する
- **STEP 09 · Lesson 20C:** [kilogramsPerUnit](lessons/20c-kilograms-per-unit.html) — 質量の「1」が何キログラムかを宣言する

## 3. Propertyを読み書きする

Primが持つ情報の中身に入ります。値の型と、対象の指し方を押さえます。

- **STEP 10 · Lesson 04:** [AttributeとRelationship](lessons/04-attributes-relationships.html) — 値とつながりを読み分ける
- **STEP 11 · Lesson 22:** [AttributeのValue Type](lessons/22-value-types.html) — scalar、vector、matrix、arrayとrole
- **STEP 12 · Lesson 05:** [Prim PathとProperty Path](lessons/05-prim-property-paths.html) — Stage内の対象を正確に指す
- **STEP 13 · Lesson 25:** [Relationship Target](lessons/25-relationship-target.html) — 一つと複数の対象を同じ仕組みで書く
- **STEP 14 · Lesson 26:** [Custom Properties](lessons/26-custom-properties.html) — Schema外の情報を追加する

## 4. Pythonから触る

ここで初めてコードを書きます。USDAで読めるようになった構造を、そのままAPIで作ります。

- **STEP 15 · Lesson 08:** [Pythonとpxrモジュール](lessons/08-python-pxr-modules.html) — Usd・Sdf・Gf・UsdGeomを使い分ける
- **STEP 16 · Lesson 09:** [MetadataとSchema](lessons/09-metadata-schemas.html) — 補助情報とデータの設計図を分ける

## 5. 形を置いて動かす

階層と変換です。ここまでで、自分でシーンを組み立てられるようになります。

- **STEP 17 · Lesson 15:** [Scope](lessons/15-scope.html) — 変換を持たず、Primを用途ごとに整理する
- **STEP 18 · Lesson 10:** [Xformと階層](lessons/10-xform-hierarchy.html) — 親の変換が子へ届く仕組みを知る
- **STEP 19 · Lesson 16:** [XformCommonAPI](lessons/16-xform-common-api.html) — 一般的な変換を交換しやすい構成で扱う
- **STEP 20 · Lesson 17A:** [Translate](lessons/17a-translate.html) — 位置を三つの軸で記述する
- **STEP 21 · Lesson 17B:** [Rotate](lessons/17b-rotate.html) — 回転角とRotation Orderを読む
- **STEP 22 · Lesson 17C:** [Scale](lessons/17c-scale.html) — 各軸の倍率を記述する
- **STEP 23 · Lesson 17D:** [Pivot](lessons/17d-pivot.html) — 回転と拡縮の中心を決める
- **STEP 24 · Lesson 18:** [XformOpOrder](lessons/18-xform-op-order.html) — 変換順序で結果が変わる理由

## 6. 形の上へ値を配る

Primvarの回です。値の個数の数え方が中心で、5つのInterpolationを一つずつ確かめます。

- **STEP 25 · Lesson 23:** [Primvars](lessons/23-primvars.html) — Attributeとの違いと三つの機能
- **STEP 26 · Lesson 24A:** [constant interpolation](lessons/24a-constant.html) — Prim全体へ一つの値
- **STEP 27 · Lesson 24B:** [uniform interpolation](lessons/24b-uniform.html) — Faceごとに一つの値
- **STEP 28 · Lesson 24C:** [vertex interpolation](lessons/24c-vertex.html) — Pointごとに一つの値
- **STEP 29 · Lesson 24D:** [varying interpolation](lessons/24d-varying.html) — Pointごとの値を線形補間する
- **STEP 30 · Lesson 24E:** [faceVarying interpolation](lessons/24e-face-varying.html) — Face Vertexごとに一つの値
- **STEP 31 · Lesson 24F:** [Indexed Primvars](lessons/24f-indexed-primvars.html) — 値とindexを分けて再利用する
- **STEP 32 · Lesson 24G:** [Primvar Inheritance](lessons/24g-primvar-inheritance.html) — constant Primvarを階層へ適用する

## 7. 時間を記述する

値が時間で変わる書き方です。Compositionへ進む前に済ませておきます。

- **STEP 33 · Lesson 11:** [Time CodeとTime Sample](lessons/11-time-codes-samples.html) — 時点と値で時間変化を記述する

## 8. Prim Specの3つの書き方

Compositionの前に、def・over・classの違いをここで確実にします。これがないと合成の説明が読めません。

- **STEP 34 · Lesson 27A:** [def](lessons/27a-def.html) — Primを定義する
- **STEP 35 · Lesson 27B:** [over](lessons/27b-over.html) — 既存PrimへOpinionだけを重ねる
- **STEP 36 · Lesson 27C:** [class](lessons/27c-class.html) — Inherits用の抽象Prim Specを作る

## 9. コンポジション

OpenUSDでいちばん難しい部分です。ここまでの土台があって初めて読み進められます。

- **STEP 37 · Lesson 12:** [コンポジションとLIVERPS](lessons/12-composition.html) — 強度順序、SublayerとLocalの関係、Opinionの上書き
- **STEP 38 · Lesson 12A:** [SublayerとLayer Stack](lessons/12-sublayers.html) — 同じnamespaceを積み、Local内の強弱を追う
- **STEP 39 · Lesson 12B:** [L · Local Opinion](lessons/12-local.html) — 利用側の直接Opinionで上書きする
- **STEP 40 · Lesson 12C:** [I · Inherits](lessons/12-inherits.html) — クラスの変更をbroadcastする
- **STEP 41 · Lesson 12D:** [V · Variant Sets](lessons/12-variants.html) — 名前付き選択肢を合成する
- **STEP 42 · Lesson 12E:** [E · rElocates](lessons/12-relocates.html) — namespace上のPathを移し替える
- **STEP 43 · Lesson 12F:** [R · References](lessons/12-references.html) — 階層の接ぎ木とPath変換を追う
- **STEP 44 · Lesson 12G:** [P · Payloads](lessons/12-payloads.html) — Load可能な内容を合成する
- **STEP 45 · Lesson 12H:** [S · Specializes](lessons/12-specializes.html) — 最も弱いfallbackを共有する
- **STEP 46 · Lesson 21:** [Value Resolution](lessons/21-value-resolution.html) — Composition後のPropertyから最終値を選ぶ

## 10. Compositionを組み立てる

合成の仕組みが分かったところで、実際の組み立て方と調べ方へ進みます。

- **STEP 47 · Lesson 28（予定）:** Prim Composition — 複数のPrim Specが一つになる
- **STEP 48 · Lesson 29:** [Internal ArcとExternal Arc](lessons/29-internal-external-arc.html) — 同じLayer内と別ファイル
- **STEP 49 · Lesson 30:** [List Editing](lessons/30-list-editing.html) — prepend・append・delete・reorder
- **STEP 50 · Lesson 31（予定）:** Encapsulation — Assetの境界を守る
- **STEP 51 · Lesson 32（予定）:** Variant Edit Context — 選択肢の中へ書く
- **STEP 52 · Lesson 33（予定）:** Direct ArcとAncestral Arc — 同じArc内の強度を追う
- **STEP 53 · Lesson 34A:** [Prim Stack](lessons/34a-prim-stack.html) — Primへ寄与するPrim Specを調べる
- **STEP 54 · Lesson 34B:** [Property Stack](lessons/34b-property-stack.html) — Propertyへ寄与するSpecを調べる

## 11. モデル階層とアセット設計

Kindでシーンに役割を与え、再利用できるアセットの形にまとめます。

- **STEP 55 · Lesson 19A:** [Kind](lessons/19a-kind.html) — Schema型とModel Hierarchy上の役割を分ける
- **STEP 56 · Lesson 19B:** [component](lessons/19b-component.html) — 再利用可能なleaf modelを作る
- **STEP 57 · Lesson 19C:** [group](lessons/19c-group.html) — Modelを正しい祖先階層へまとめる
- **STEP 58 · Lesson 19D:** [assembly](lessons/19d-assembly.html) — 公開可能なaggregate Assetを作る
- **STEP 59 · Lesson 19E:** [subcomponent](lessons/19e-subcomponent.html) — component内部の重要なPrimを示す
- **STEP 60 · Lesson 13:** [再利用できるアセット設計](lessons/13-asset-structure.html) — Asset Structure、Model Kind、Asset Interface、Reference/Payload Pattern

## 12. Stageを調べて制御する

大きなシーンを扱うための、読み込みと走査の制御です。

- **STEP 61 · Lesson 41:** [ActiveとInactive](lessons/41-active-inactive.html) — Compositionから除外する
- **STEP 62 · Lesson 42:** [LoadとUnload](lessons/42-load-unload.html) — Payloadを制御する
- **STEP 63 · Lesson 43:** [Stage Traversal](lessons/43-stage-traversal.html) — Primを順番に調べる
- **STEP 64 · Lesson 44:** [Traversal Predicate](lessons/44-traversal-predicate.html) — 調べるPrimを絞る
- **STEP 65 · Lesson 45（予定）:** Hydra — Scene Indexとレンダリングの入口

## 13. パイプラインとData Exchange

他のツールとの間でデータを受け渡す実務です。

- **STEP 66 · Lesson 14:** [データを運ぶパイプライン](lessons/14-data-pipelines.html) — データ交換、抽出、変換、検証、Instancing
- **STEP 67 · Lesson 47（予定）:** Asset Entry Point — 参照される入口を作る
- **STEP 68 · Lesson 48（予定）:** Asset Interface — 公開する情報を選ぶ
- **STEP 69 · Lesson 49（予定）:** Workstream Layers — 作業をLayerで分ける
- **STEP 70 · Lesson 51（予定）:** Asset Parameterization — 下流から変更できる値
- **STEP 71 · Lesson 52（予定）:** Reference/Payload Pattern — InterfaceとContentsを分ける
- **STEP 72 · Lesson 53（予定）:** Lofting — Payloadを開かず重要情報を見せる
- **STEP 73 · Lesson 54（予定）:** Converterの構造 — 入力・変換・出力を分ける
- **STEP 74 · Lesson 55（予定）:** Geometry Extraction — 点・法線・UVを対応させる
- **STEP 75 · Lesson 56（予定）:** Material Extraction — MaterialとBindingを対応させる
- **STEP 76 · Lesson 57（予定）:** Asset Validation — 規則をコードにする
- **STEP 77 · Lesson 58（予定）:** Prim Hierarchy Transformation — 階層を目的形へ変える
- **STEP 78 · Lesson 59（予定）:** Export Options — 変換条件を利用者へ公開する

## 14. Instancingと大規模シーン

同じものを大量に置くための仕組みです。

- **STEP 79 · Lesson 60（予定）:** Asset Modularity — 再利用単位を決める
- **STEP 80 · Lesson 61（予定）:** Scenegraph Instancing — CompositionからPrototypeを作る
- **STEP 81 · Lesson 62（予定）:** Nested Instancing — Instanceを階層化する
- **STEP 82 · Lesson 63（予定）:** Instance Refinement — Instanceごとの差を付ける
- **STEP 83 · Lesson 64（予定）:** Point Instancing — 大量の単純要素を配置する
- **STEP 84 · Lesson 65（予定）:** ScenegraphとPointの選択 — 用途と制約を比較する

## 15. 調査・検証・総復習

最後に、壊れたシーンを直せるところまで進みます。

- **STEP 85 · Lesson 66（予定）:** usdviewとusdrecordでStageを読む — 構造と描画を確かめる
- **STEP 86 · Lesson 67（予定）:** Layer Stackを調べる — どのLayerの意見が効いているか
- **STEP 87 · Lesson 68（予定）:** 壊れたReferenceとPathを直す — よくある破損の直し方
- **STEP 88 · Lesson 69（予定）:** Pythonで最小Validationを書く — 規則を自動で確かめる
- **STEP 89 · Lesson 70（予定）:** 小さなAssetを最初から組み立てる — 総合演習1
- **STEP 90 · Lesson 71（予定）:** 複数Assetから小さなSceneを作る — 総合演習2
- **STEP 91 · Lesson 72（予定）:** OpenUSD教材の総復習 — 全体を振り返る

> **Academy方針:** 各レッスンは現在と同程度の長さと難易度に保ち、一回に一つの中心概念を扱います。公式の概念を改変せず、図解・USDA/Python対訳・日本語でのつまずき対策を加えます。
