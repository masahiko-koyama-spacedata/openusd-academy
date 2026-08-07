# OpenUSD Academy カリキュラム

このカリキュラムは、[OpenUSD公式ドキュメント](https://openusd.org/release/index.html) を技術上の一次情報とし、[NVIDIA Learn OpenUSD](https://docs.nvidia.com/learn-openusd/latest/index.html) を主要な学習資料として照合したうえで、日本語の初学者が段階的に進めるようAcademy独自に整理した計画です（確認日: 2026-08-06）。

> **STEP番号のとおりに上から進めてください。** 各ページの前後リンクも同じ並びなので、順にたどるだけで迷いません。章の見出しをたどると、その章の全体像をまとめたページへ移動します。初学者がつまずきにくい順序を優先しているため、公式資料の章立てとは並びが異なります。

## [1. まずUSDAを読む](chapters/01-read-usda.html)

最初の目標は「書く」ではなく「読める」です。短いテキストを一行ずつ読み解きます。

- **STEP 01:** [はじめてのUSDAを読む](lessons/01-reading-usda.html) — Stage、Prim、Xform、名前、Pathを短いUSDAから一行ずつ読む
- **STEP 02:** [OpenUSDとは何か](lessons/02-what-is-openusd.html) — シーン記述・合成・共同作業の土台を知る
- **STEP 03:** [Stage・Prim・Property](lessons/03-stage-prim-property.html) — 全体、構成要素、情報を分ける
- **STEP 04:** [USDAの基本構文](lessons/07-usda-syntax.html) — 型・名前・波括弧・Propertyを読む
- **STEP 05:** [USDA・USDC・USD・USDZ](lessons/06-usd-file-formats.html) — 中身と用途でファイル形式を選ぶ

## [2. ファイル先頭の約束事](chapters/02-stage-metadata.html)

すべての例に出てくるファイル先頭のMetadataを、ここで先に理解しておきます。

- **STEP 06:** [Default Prim](lessons/09a-default-prim.html) — Layerを外から利用するときの入口を決める
- **STEP 07:** [metersPerUnit](lessons/20a-meters-per-unit.html) — 長さの「1」が何メートルかを宣言する
- **STEP 08:** [upAxis](lessons/20b-up-axis.html) — どの軸が上かを宣言する
- **STEP 09:** [kilogramsPerUnit](lessons/20c-kilograms-per-unit.html) — 質量の「1」が何キログラムかを宣言する

## [3. Propertyを読み書きする](chapters/03-properties.html)

Primが持つ情報の中身に入ります。値の型と、対象の指し方を押さえます。

- **STEP 10:** [AttributeとRelationship](lessons/04-attributes-relationships.html) — 値とつながりを読み分ける
- **STEP 11:** [AttributeのValue Type](lessons/22-value-types.html) — scalar、vector、matrix、arrayとrole
- **STEP 12:** [Prim PathとProperty Path](lessons/05-prim-property-paths.html) — Stage内の対象を正確に指す
- **STEP 13:** [Relationship Target](lessons/25-relationship-target.html) — 一つと複数の対象を同じ仕組みで書く
- **STEP 14:** [Custom Properties](lessons/26-custom-properties.html) — Schema外の情報を追加する

## [4. Pythonから触る](chapters/04-python.html)

ここで初めてコードを書きます。USDAで読めるようになった構造を、そのままAPIで作ります。

- **STEP 15:** [Pythonとpxrモジュール](lessons/08-python-pxr-modules.html) — Usd・Sdf・Gf・UsdGeomを使い分ける
- **STEP 16:** [MetadataとSchema](lessons/09-metadata-schemas.html) — 補助情報とデータの設計図を分ける

## [5. 形を置いて動かす](chapters/05-transforms.html)

階層と変換です。ここまでで、自分でシーンを組み立てられるようになります。

- **STEP 17:** [Scope](lessons/15-scope.html) — 変換を持たず、Primを用途ごとに整理する
- **STEP 18:** [Xformと階層](lessons/10-xform-hierarchy.html) — 親の変換が子へ届く仕組みを知る
- **STEP 19:** [XformCommonAPI](lessons/16-xform-common-api.html) — 一般的な変換を交換しやすい構成で扱う
- **STEP 20:** [Translate](lessons/17a-translate.html) — 位置を三つの軸で記述する
- **STEP 21:** [Rotate](lessons/17b-rotate.html) — 回転角とRotation Orderを読む
- **STEP 22:** [Scale](lessons/17c-scale.html) — 各軸の倍率を記述する
- **STEP 23:** [Pivot](lessons/17d-pivot.html) — 回転と拡縮の中心を決める
- **STEP 24:** [XformOpOrder](lessons/18-xform-op-order.html) — 変換順序で結果が変わる理由

## [6. 形の上へ値を配る](chapters/06-primvars.html)

Primvarの回です。値の個数の数え方が中心で、5つのInterpolationを一つずつ確かめます。

- **STEP 25:** [Primvars](lessons/23-primvars.html) — Attributeとの違いと三つの機能
- **STEP 26:** [constant interpolation](lessons/24a-constant.html) — Prim全体へ一つの値
- **STEP 27:** [uniform interpolation](lessons/24b-uniform.html) — Faceごとに一つの値
- **STEP 28:** [vertex interpolation](lessons/24c-vertex.html) — Pointごとに一つの値
- **STEP 29:** [varying interpolation](lessons/24d-varying.html) — Pointごとの値を線形補間する
- **STEP 30:** [faceVarying interpolation](lessons/24e-face-varying.html) — Face Vertexごとに一つの値
- **STEP 31:** [Indexed Primvars](lessons/24f-indexed-primvars.html) — 値とindexを分けて再利用する
- **STEP 32:** [Primvar Inheritance](lessons/24g-primvar-inheritance.html) — constant Primvarを階層へ適用する

## [7. 時間を記述する](chapters/07-time.html)

値が時間で変わる書き方です。Compositionへ進む前に済ませておきます。

- **STEP 33:** [Time CodeとTime Sample](lessons/11-time-codes-samples.html) — 時点と値で時間変化を記述する

## [8. Prim Specの3つの書き方](chapters/08-specifiers.html)

Compositionの前に、def・over・classの違いをここで確実にします。これがないと合成の説明が読めません。

- **STEP 34:** [def](lessons/27a-def.html) — Primを定義する
- **STEP 35:** [over](lessons/27b-over.html) — 既存PrimへOpinionだけを重ねる
- **STEP 36:** [class](lessons/27c-class.html) — Inherits用の抽象Prim Specを作る

## [9. コンポジション](chapters/09-composition.html)

OpenUSDでいちばん難しい部分です。ここまでの土台があって初めて読み進められます。

- **STEP 37:** [コンポジションとLIVERPS](lessons/12-composition.html) — 強度順序、SublayerとLocalの関係、Opinionの上書き
- **STEP 38:** [SublayerとLayer Stack](lessons/12-sublayers.html) — 同じnamespaceを積み、Local内の強弱を追う
- **STEP 39:** [L · Local Opinion](lessons/12-local.html) — 利用側の直接Opinionで上書きする
- **STEP 40:** [I · Inherits](lessons/12-inherits.html) — クラスの変更をbroadcastする
- **STEP 41:** [V · Variant Sets](lessons/12-variants.html) — 名前付き選択肢を合成する
- **STEP 42:** [E · rElocates](lessons/12-relocates.html) — namespace上のPathを移し替える
- **STEP 43:** [R · References](lessons/12-references.html) — 階層の接ぎ木とPath変換を追う
- **STEP 44:** [P · Payloads](lessons/12-payloads.html) — Load可能な内容を合成する
- **STEP 45:** [S · Specializes](lessons/12-specializes.html) — 最も弱いfallbackを共有する
- **STEP 46:** [Value Resolution](lessons/21-value-resolution.html) — Composition後のPropertyから最終値を選ぶ

## [10. Compositionを組み立てる](chapters/10-composition-practice.html)

合成の仕組みが分かったところで、実際の組み立て方と、原因を追う道具へ進みます。

- **STEP 47（予定）:** Prim Composition — 複数のPrim Specが一つになる
- **STEP 48:** [Internal ArcとExternal Arc](lessons/29-internal-external-arc.html) — 同じLayer内と別ファイル
- **STEP 49:** [List Editing](lessons/30-list-editing.html) — prepend・append・delete・reorder
- **STEP 50（予定）:** Encapsulation — Assetの境界を守る
- **STEP 51（予定）:** Variant Edit Context — 選択肢の中へ書く
- **STEP 52（予定）:** Direct ArcとAncestral Arc — 同じArc内の強度を追う
- **STEP 53:** [Prim Stack](lessons/34a-prim-stack.html) — Primへ寄与するPrim Specを調べる
- **STEP 54:** [Property Stack](lessons/34b-property-stack.html) — Propertyへ寄与するSpecを調べる

## [11. モデル階層とアセット設計](chapters/11-model-hierarchy.html)

Kindでシーンに役割を与え、再利用できるアセットの形にまとめます。

- **STEP 55:** [Kind](lessons/19a-kind.html) — Schema型とModel Hierarchy上の役割を分ける
- **STEP 56:** [component](lessons/19b-component.html) — 再利用可能なleaf modelを作る
- **STEP 57:** [group](lessons/19c-group.html) — Modelを正しい祖先階層へまとめる
- **STEP 58:** [assembly](lessons/19d-assembly.html) — 公開可能なaggregate Assetを作る
- **STEP 59:** [subcomponent](lessons/19e-subcomponent.html) — component内部の重要なPrimを示す
- **STEP 60:** [再利用できるアセット設計](lessons/13-asset-structure.html) — Asset Structure、Model Kind、Asset Interface、Reference/Payload Pattern

## [12. Stageを調べて制御する](chapters/12-stage-control.html)

大きなシーンを扱うための、読み込みと走査の制御です。

- **STEP 61:** [ActiveとInactive](lessons/41-active-inactive.html) — Compositionから除外する
- **STEP 62:** [LoadとUnload](lessons/42-load-unload.html) — Payloadを制御する
- **STEP 63:** [Stage Traversal](lessons/43-stage-traversal.html) — Primを順番に調べる
- **STEP 64:** [Traversal Predicate](lessons/44-traversal-predicate.html) — 調べるPrimを絞る
- **STEP 65（予定）:** Hydra — Scene Indexとレンダリングの入口

## [13. パイプラインとData Exchange](chapters/13-pipeline.html)

他のツールとの間でデータを受け渡す実務です。ここからは設計の話が増えます。

- **STEP 66:** [データを運ぶパイプライン](lessons/14-data-pipelines.html) — データ交換、抽出、変換、検証、Instancing
- **STEP 67（予定）:** Asset Entry Point — 参照される入口を作る
- **STEP 68（予定）:** Asset Interface — 公開する情報を選ぶ
- **STEP 69（予定）:** Workstream Layers — 作業をLayerで分ける
- **STEP 70（予定）:** Asset Parameterization — 下流から変更できる値
- **STEP 71（予定）:** Reference/Payload Pattern — InterfaceとContentsを分ける
- **STEP 72（予定）:** Lofting — Payloadを開かず重要情報を見せる
- **STEP 73（予定）:** Converterの構造 — 入力・変換・出力を分ける
- **STEP 74（予定）:** Geometry Extraction — 点・法線・UVを対応させる
- **STEP 75（予定）:** Material Extraction — MaterialとBindingを対応させる
- **STEP 76（予定）:** Asset Validation — 規則をコードにする
- **STEP 77（予定）:** Prim Hierarchy Transformation — 階層を目的形へ変える
- **STEP 78（予定）:** Export Options — 変換条件を利用者へ公開する

## [14. Instancingと大規模シーン](chapters/14-instancing.html)

同じものを大量に置くための仕組みです。数が増えたときに効いてきます。

- **STEP 79（予定）:** Asset Modularity — 再利用単位を決める
- **STEP 80（予定）:** Scenegraph Instancing — CompositionからPrototypeを作る
- **STEP 81（予定）:** Nested Instancing — Instanceを階層化する
- **STEP 82（予定）:** Instance Refinement — Instanceごとの差を付ける
- **STEP 83（予定）:** Point Instancing — 大量の単純要素を配置する
- **STEP 84（予定）:** ScenegraphとPointの選択 — 用途と制約を比較する

## [15. 調査・検証・総復習](chapters/15-debugging.html)

最後に、壊れたシーンを自分で直せるところまで進みます。

- **STEP 85（予定）:** usdrecordとusdtreeでStageを読む — 構造と描画を確かめる
- **STEP 86（予定）:** Layer Stackを調べる — どのLayerの意見が効いているか
- **STEP 87（予定）:** 壊れたReferenceとPathを直す — よくある破損の直し方
- **STEP 88（予定）:** Pythonで最小Validationを書く — 規則を自動で確かめる
- **STEP 89（予定）:** 小さなAssetを最初から組み立てる — 総合演習1
- **STEP 90（予定）:** 複数Assetから小さなSceneを作る — 総合演習2
- **STEP 91（予定）:** OpenUSD教材の総復習 — 全体を振り返る

> **Academy方針:** 各レッスンは現在と同程度の長さと難易度に保ち、一回に一つの中心概念を扱います。公式の概念を改変せず、図解・USDA/Python対訳・日本語でのつまずき対策を加えます。
