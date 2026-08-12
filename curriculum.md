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

## [2. Propertyを読み書きする](chapters/02-properties.html)

Primが持つ情報の中身に入ります。値の型と、対象の指し方を押さえます。

- **STEP 06:** [AttributeとRelationship](lessons/04-attributes-relationships.html) — 値とつながりを読み分ける
- **STEP 07:** [AttributeのValue Type](lessons/22-value-types.html) — scalar、vector、matrix、arrayとrole
- **STEP 08:** [Prim PathとProperty Path](lessons/05-prim-property-paths.html) — Stage内の対象を正確に指す
- **STEP 09:** [Relationship Target](lessons/25-relationship-target.html) — 一つと複数の対象を同じ仕組みで書く
- **STEP 10:** [Custom Properties](lessons/26-custom-properties.html) — Schema外の情報を追加する

## [3. Pythonから触る](chapters/03-python.html)

ここで初めてコードを書きます。USDAで読めるようになった構造を、そのままAPIで作ります。

- **STEP 11:** [Pythonとpxrモジュール](lessons/08-python-pxr-modules.html) — Usd・Sdf・Gf・UsdGeomを使い分ける
- **STEP 12:** [MetadataとSchema](lessons/09-metadata-schemas.html) — 補助情報とデータの設計図を分ける
- **STEP 13:** [Schemaの種類](lessons/09b-schema-kinds.html) — Typed/APIの2系統と、concrete・abstract・applied・non-applied

## [4. 形を置いて動かす](chapters/04-transforms.html)

階層と変換です。ここまでで、自分でシーンを組み立てられるようになります。

- **STEP 14:** [Scope](lessons/15-scope.html) — 変換を持たず、Primを用途ごとに整理する
- **STEP 15:** [Xformと階層](lessons/10-xform-hierarchy.html) — 親の変換が子へ届く仕組みを知る
- **STEP 16:** [XformCommonAPI](lessons/16-xform-common-api.html) — 一般的な変換を交換しやすい構成で扱う
- **STEP 17:** [Translate](lessons/17a-translate.html) — 位置を三つの軸で記述する
- **STEP 18:** [Rotate](lessons/17b-rotate.html) — 回転角とRotation Orderを読む
- **STEP 19:** [Scale](lessons/17c-scale.html) — 各軸の倍率を記述する
- **STEP 20:** [Pivot](lessons/17d-pivot.html) — 回転と拡縮の中心を決める
- **STEP 21:** [XformOpOrder](lessons/18-xform-op-order.html) — 変換順序で結果が変わる理由

## [5. Meshの形と、その上へ値を配る](chapters/05-primvars.html)

まずMeshの形そのものを読み書きし、そこで数えた個数のままPrimvarへ進みます。

- **STEP 22:** [Meshのトポロジ](lessons/35-mesh-topology.html) — points・faceVertexCounts・faceVertexIndicesで形を作る
- **STEP 23:** [Meshの見え方を決めるAttribute](lessons/36-mesh-attributes.html) — subdivisionScheme・orientation・doubleSided・extent
- **STEP 24:** [Primvars](lessons/23-primvars.html) — Attributeとの違いと三つの機能
- **STEP 25:** [constant interpolation](lessons/24a-constant.html) — Prim全体へ一つの値
- **STEP 26:** [uniform interpolation](lessons/24b-uniform.html) — Faceごとに一つの値
- **STEP 27:** [vertex interpolation](lessons/24c-vertex.html) — Pointごとに一つの値
- **STEP 28:** [varying interpolation](lessons/24d-varying.html) — Pointごとの値を線形補間する
- **STEP 29:** [faceVarying interpolation](lessons/24e-face-varying.html) — Face Vertexごとに一つの値
- **STEP 30:** [Indexed Primvars](lessons/24f-indexed-primvars.html) — 値とindexを分けて再利用する
- **STEP 31:** [Primvar Inheritance](lessons/24g-primvar-inheritance.html) — constant Primvarを階層へ適用する

## [6. 見た目を記述する](chapters/06-shading.html)

形ができたので、次はその見え方です。MaterialとShaderの組み立て方と、形との結び付け方を扱います。

- **STEP 32:** [UsdShadeの基礎](lessons/46-usdshade-basics.html) — MaterialとShaderを接続で組み立てる
- **STEP 33:** [Material Binding](lessons/50-material-binding.html) — 形とMaterialを結び、子孫へ受け継がせる

## [7. 時間を記述する](chapters/07-time.html)

値が時間で変わる書き方です。Compositionへ進む前に済ませておきます。

- **STEP 34:** [Time CodeとTime Sample](lessons/11-time-codes-samples.html) — 時点と値で時間変化を記述する

## [8. Prim Specの3つの書き方](chapters/08-specifiers.html)

Compositionの前に、def・over・classの違いをここで確実にします。これがないと合成の説明が読めません。

- **STEP 35:** [def](lessons/27a-def.html) — Primを定義する
- **STEP 36:** [over](lessons/27b-over.html) — 既存PrimへOpinionだけを重ねる
- **STEP 37:** [class](lessons/27c-class.html) — Inherits用の抽象Prim Specを作る

## [9. コンポジション](chapters/09-composition.html)

OpenUSDでいちばん難しい部分です。ここまでの土台があって初めて読み進められます。

- **STEP 38:** [コンポジションとLIVERPS](lessons/12-composition.html) — 強度順序、SublayerとLocalの関係、Opinionの上書き
- **STEP 39:** [SublayerとLayer Stack](lessons/12-sublayers.html) — 同じnamespaceを積み、Local内の強弱を追う
- **STEP 40:** [L · Local Opinion](lessons/12-local.html) — 利用側の直接Opinionで上書きする
- **STEP 41:** [I · Inherits](lessons/12-inherits.html) — クラスの変更をbroadcastする
- **STEP 42:** [V · Variant Sets](lessons/12-variants.html) — 名前付き選択肢を合成する
- **STEP 43:** [E · rElocates](lessons/12-relocates.html) — namespace上のPathを移し替える
- **STEP 44:** [R · References](lessons/12-references.html) — 階層の接ぎ木とPath変換を追う
- **STEP 45:** [P · Payloads](lessons/12-payloads.html) — Load可能な内容を合成する
- **STEP 46:** [S · Specializes](lessons/12-specializes.html) — 最も弱いfallbackを共有する
- **STEP 47:** [Value Resolution](lessons/21-value-resolution.html) — Composition後のPropertyから最終値を選ぶ

## [10. ファイル先頭の宣言と入口](chapters/10-stage-metadata.html)

第1章から毎回出てきた「ファイル先頭の丸括弧」を、ここで回収します。単位を直すにはscale、上方向を直すにはrotate、入口を語るにはReferenceが要るので、この位置に置いています。

- **STEP 48:** [Default Prim](lessons/09a-default-prim.html) — Layerを外から利用するときの入口を決める
- **STEP 49:** [metersPerUnit](lessons/20a-meters-per-unit.html) — 長さの「1」が何メートルかを宣言する
- **STEP 50:** [upAxis](lessons/20b-up-axis.html) — どの軸が上かを宣言する
- **STEP 51:** [kilogramsPerUnit](lessons/20c-kilograms-per-unit.html) — 質量の「1」が何キログラムかを宣言する

## [11. Compositionを組み立てる](chapters/11-composition-practice.html)

合成の仕組みが分かったところで、実際の組み立て方と、原因を追う道具へ進みます。

- **STEP 52:** [Prim Composition](lessons/28-prim-composition.html) — 複数のPrim Specが一つになる
- **STEP 53:** [Internal ArcとExternal Arc](lessons/29-internal-external-arc.html) — 同じLayer内と別ファイル
- **STEP 54:** [List Editing](lessons/30-list-editing.html) — prepend・append・delete・reorder
- **STEP 55:** [Encapsulation](lessons/31-encapsulation.html) — Assetの境界を守る
- **STEP 56:** [Variant Edit Context](lessons/32-variant-edit-context.html) — 選択肢の中へ書く
- **STEP 57:** [Direct ArcとAncestral Arc](lessons/33-direct-ancestral-arc.html) — 同じArc内の強度を追う
- **STEP 58:** [Prim Stack](lessons/34a-prim-stack.html) — Primへ寄与するPrim Specを調べる
- **STEP 59:** [Property Stack](lessons/34b-property-stack.html) — Propertyへ寄与するSpecを調べる

## [12. モデル階層とアセット設計](chapters/12-model-hierarchy.html)

Kindでシーンに役割を与え、再利用できるアセットの形にまとめます。

- **STEP 60:** [Kind](lessons/19a-kind.html) — Schema型とModel Hierarchy上の役割を分ける
- **STEP 61:** [component](lessons/19b-component.html) — 再利用可能なleaf modelを作る
- **STEP 62:** [group](lessons/19c-group.html) — Modelを正しい祖先階層へまとめる
- **STEP 63:** [assembly](lessons/19d-assembly.html) — 公開可能なaggregate Assetを作る
- **STEP 64:** [subcomponent](lessons/19e-subcomponent.html) — component内部の重要なPrimを示す
- **STEP 65:** [再利用できるアセット設計](lessons/13-asset-structure.html) — Asset Structure、Model Kind、Asset Interface、Reference/Payload Pattern

## [13. Stageを調べて制御する](chapters/13-stage-control.html)

大きなシーンを扱うための、読み込みと走査の制御です。

- **STEP 66:** [ActiveとInactive](lessons/41-active-inactive.html) — Compositionから除外する
- **STEP 67:** [LoadとUnload](lessons/42-load-unload.html) — Payloadを制御する
- **STEP 68:** [Stage Traversal](lessons/43-stage-traversal.html) — Primを順番に調べる
- **STEP 69:** [Traversal Predicate](lessons/44-traversal-predicate.html) — 調べるPrimを絞る
- **STEP 70:** [Hydra](lessons/45-hydra.html) — Scene Indexとレンダリングの入口

## [14. パイプラインとData Exchange](chapters/14-pipeline.html)

他のツールとの間でデータを受け渡す実務です。ここからは設計の話が増えます。

- **STEP 71:** [データを運ぶパイプライン](lessons/14-data-pipelines.html) — データ交換、抽出、変換、検証、Instancing
- **STEP 72:** [Asset Entry Point](lessons/47-asset-entry-point.html) — 参照される入口を作る
- **STEP 73:** [Asset Interface](lessons/48-asset-interface.html) — 公開する情報を選ぶ
- **STEP 74:** [Workstream Layers](lessons/49-workstream-layers.html) — 作業をLayerで分ける
- **STEP 75:** [Asset Parameterization](lessons/51-asset-parameterization.html) — 下流から変更できる値
- **STEP 76:** [Reference/Payload Pattern](lessons/52-reference-payload-pattern.html) — InterfaceとContentsを分ける
- **STEP 77:** [Lofting](lessons/53-lofting.html) — Payloadを開かず重要情報を見せる
- **STEP 78:** [Converterの構造](lessons/54-converter-structure.html) — 入力・変換・出力を分ける
- **STEP 79:** [Geometry Extraction](lessons/55-geometry-extraction.html) — 点・法線・UVを対応させる
- **STEP 80:** [Material Extraction](lessons/56-material-extraction.html) — MaterialとBindingを対応させる
- **STEP 81:** [Asset Validation](lessons/57-asset-validation.html) — 規則をコードにする
- **STEP 82:** [Prim Hierarchy Transformation](lessons/58-prim-hierarchy-transformation.html) — 階層を目的形へ変える
- **STEP 83:** [Export Options](lessons/59-export-options.html) — 変換条件を利用者へ公開する

## [15. Instancingと大規模シーン](chapters/15-instancing.html)

同じものを大量に置くための仕組みです。数が増えたときに効いてきます。

- **STEP 84:** [Asset Modularity](lessons/60-asset-modularity.html) — 再利用単位を決める
- **STEP 85:** [Scenegraph Instancing](lessons/61-scenegraph-instancing.html) — CompositionからPrototypeを作る
- **STEP 86:** [Nested Instancing](lessons/62-nested-instancing.html) — Instanceを階層化する
- **STEP 87:** [Instance Refinement](lessons/63-instance-refinement.html) — Instanceごとの差を付ける
- **STEP 88:** [Point Instancing](lessons/64-point-instancing.html) — 大量の単純要素を配置する
- **STEP 89:** [ScenegraphとPointの選択](lessons/65-instancing-choice.html) — 用途と制約を比較する

## [16. 調査・検証・総復習](chapters/16-debugging.html)

最後に、壊れたシーンを自分で直せるところまで進みます。

- **STEP 90:** [usdrecordとusdtreeでStageを読む](lessons/66-inspect-stage.html) — 構造と描画を確かめる
- **STEP 91:** [Layer Stackを調べる](lessons/67-inspect-layer-stack.html) — どのLayerの意見が効いているか
- **STEP 92:** [壊れたReferenceとPathを直す](lessons/68-fix-broken-references.html) — よくある破損の直し方
- **STEP 93:** [Pythonで最小Validationを書く](lessons/69-minimal-validation.html) — 規則を自動で確かめる
- **STEP 94:** [小さなAssetを最初から組み立てる](lessons/70-build-an-asset.html) — 総合演習1
- **STEP 95:** [複数Assetから小さなSceneを作る](lessons/71-build-a-scene.html) — 総合演習2
- **STEP 96:** [OpenUSD教材の総復習](lessons/72-review.html) — 全体を振り返る

> **Academy方針:** 各レッスンは現在と同程度の長さと難易度に保ち、一回に一つの中心概念を扱います。公式の概念を改変せず、図解・USDA/Python対訳・日本語でのつまずき対策を加えます。
