# OpenUSD Academy 用語集

このファイルはサイト全体の索引です。個々のレッスンにも、その回で使う用語集を必ず付けます。定義はレッスン執筆時に [NVIDIA Learn OpenUSD](https://docs.nvidia.com/learn-openusd/latest/index.html) の公式用語集と該当ページを確認します。正本は `glossary.html` です。

## 用語一覧

### absolute path

pseudo-rootから対象までを表すPath。

### abstract Schema

型としては書けず、共通の性質をまとめるためのTyped Schema。ImageableやXformableなど。

### abstract（抽象）

Stageの既定の走査と描画から外れる状態。`IsAbstract()`が`True`を返す。

### active

PrimをStageの構成に含めるかどうかを決めるPrim Metadata。既定値は`true`。

### AddInherit

受け取る側にInheritsの対象Pathを追加するPython API。

### AddInternalReference

Internal ReferenceをPythonから追加するAPI。

### AddTarget

既存のTarget Listへ、Target Pathを一つ追加するPython API。

### AddVariantSet / AddVariant

選択肢の組と、その中の選択肢を作るPython API。

### Ancestral Arc

祖先のPrimに書かれ、子孫へ降りてきたComposition Arc。

### API Schema

Primの型を変えずに、機能や情報を足すSchema。

### apiSchemas

appliedなAPI Schemaの一覧を保持するPrim Metadata。

### append

一覧の末尾へ項目を足すキーワード。

### applied API Schema

`Apply()`して`apiSchemas`に記録が残るAPI Schema。

### Arc Strength（強度）

競合したときにどのArcの意見が勝つかの順序。まず種類、次にDirectかAncestralかで決まる。

### array

同じ型の値が並ぶ値の形です。型名の末尾に `[]` が付きます。

### assembly

公開できるまとまりを示すKind。列や区画のような集合に使う。

### asset

他のファイルを指すパスのValue Typeです。USDAでは `@ball.usda@` のようにアットマークで囲みます。

### Asset

独立して参照できるまとまりです。多くは1ファイルで、入口となるPrimを持ちます。

### Asset Boundary（アセットの境界）

ここから中は内部実装、という取り決めの線。

### Asset Interface

Assetが外へ公開する情報の集まりです。使う側との約束にあたります。

### Asset Modularity

どこで切ってAssetにするかという設計上の判断。

### Asset Parameterization

使う側が変えてよい部分を、作る側があらかじめ用意しておくこと。

### Attribute（アトリビュート）

Primが持つ値のあるProperty。色、サイズ、位置などを表します。

### axis（Cylinder・Cone）

その形自体が伸びる方向を決めるAttribute。既定値は`'Z'`。

### BBoxCache

Primを囲む箱を計算するためのPythonのオブジェクト。

### Broadcasted Refinement

共有を保ったまま、classなどを経由して全Instanceを一度に変えること。

### catmullClark

OpenUSDのMeshで既定となっている細分化の方式です。

### class

他のPrimが受け取るための意見をまとめて置く、abstractなPrimを作るSpecifierです。

### ClearReferences

そのPrimのReferenceの記述をすべて取り除くPython API。

### Composed Prim

合成の結果としてStage上に現れるPrim。

### Composition Arc

複数のシーン記述を組み合わせる演算子です。

### Composition Error

合成の過程で起きたエラー。Pythonの例外にはならないが、`stage.GetCompositionErrors()`や`usdchecker`で取り出せる。

### Composition（コンポジション）

複数のシーン記述を規則に従って一つの結果へ組み立てる仕組みです。

### ComputeFlattened

Indexed Primvarのindexを解いた後の値の並びを返すPython APIです。

### ComputeLocalToWorldTransform

そのPrimの、世界座標への変換行列を求めるPython API。

### ComputeMaskAtTime

どの配置が有効かを真偽の配列で返すPython API。

### ComputeVisibility

親からの継承まで含めて、最終的に描画されるかを求めるPython API。

### concrete Schema

型として実際に書けるTyped Schema。MeshやCubeなど。

### constant

Gprim全体へ値を一つだけ対応させるPrimvar Interpolationです。値の個数は形によらず常に1です。

### Contents

Payloadの先に置く、Assetの実際の中身。

### Converter

他のツールの形式からUSDを作る処理です。読む・対応づける・書くの3段に分けます。

### CreateClassPrim

`class`のPrimを作るPython API。

### custom

Schemaであらかじめ定義されていないカスタムPropertyを示す指定。

### Custom Property

Schemaが定義していない、利用者が独自に足したProperty。

### Custom Relationship

`custom rel`で書く、Schema外のRelationship。

### Dangling target

存在しないPathを指したままのRelationshipのtargetです。`usdchecker`では報告されません。

### De-instancing

`instanceable`を外し、そのPrimの中身を個別に持たせること。

### def

Primを定義するSpecifierです。Stage上にdefinedなPrimとして現れます。

### Default Predicate

`Traverse()`が既定で使う条件。定義済み・Active・<strong>Load済み</strong>・非abstract・非instance proxy。

### Default Prim（デフォルトプリム）

Layer Metadataで指定する、そのLayerの主な入口となるtop-level Primです。

### default（Spec）

そのLayerに書かれた、時間に依存しない値。

### defined（定義済み）

Compositionの結果、そのPrimが存在すると判定された状態。`IsDefined()`が`True`を返す。

### def（デフ）

現在のLayerでPrimを具体的に定義するSpecifierです。

### delete

一覧から項目を取り除くキーワード。

### Direct Arc

そのPrim自身に書かれたComposition Arc。

### displayColor

Gprimに最初から用意されている表示用の色のPrimvarです。既定のinterpolationは`constant`です。

### Encapsulation（カプセル化）

持ち込まれた側のComposition Arcが、そのファイルの中で完結していることです。

### Entry Point（入口）

Assetを外から使うときに最初に開かれるファイル、およびそのPrimです。

### explicit

キーワードを付けずに書き、一覧を丸ごと置き換える記述。

### Export Options

変換の条件を、外から指定できるようにしたものです。

### extentsHint

そのAssetのおおよその大きさを、入口に持たせるAttribute。

### External Arc

別のファイルを指すComposition Arc。

### Face

Meshを構成する面です。`faceVertexCounts`の要素数がFaceの枚数になります。

### Face Vertex

あるFaceが頂点を使った一回分です。同じPointが複数のFaceから使われると、その回数だけ増えます。

### faceVarying

Face Vertexごとに一つの値を対応させるPrimvar Interpolationです。Faceの境目で値を不連続にできます。

### faceVertexCounts

各Faceの頂点数を順に並べた配列です。要素数がFaceの枚数になります。

### faceVertexIndices

各Faceがどのpointを使うかを、`points`の位置番号で並べた配列です。

### fallback（既定値）

Schemaが定める、記述が無いときに返る値。

### FindLoadable

Load可能なPrimの一覧を返すPython API。

### FindPrimvarWithInheritance

自分に無ければ親をさかのぼってPrimvarを探すPython APIです。

### Flatten

合成した結果を1枚のLayerにまとめること。Pythonでは`stage.Flatten()`。

### Geometry Extraction

USDから形の情報を取り出し、他の形式へ渡せる形にすること。

### GetAuthoredPrimvars

そのPrimに実際に記述されたPrimvarだけを返すPython APIです。

### GetAuthoredPropertyNames

実際に記述されたPropertyの名前だけを返すPython API。

### GetChildren / GetAllChildren

直下の子を返すPython API。後者は条件を外す。

### GetDisplayName

Layerの表示用の短い名前を返すPython API。

### GetLayerStack

root layerとそのSublayerを、強い順に返すPython API。

### GetPrimPath

Property PathからPrim Pathの部分を取り出すPython API。

### GetPrototype / GetInstances

InstanceからPrototypeを、PrototypeからInstanceの一覧を得るPython API。

### GetRelationships

そのPrimが持つRelationshipをすべて返すPython API。

### GetVariantSets().GetNames()

そのPrimが持つVariant Setの名前を一覧するPython API。

### Gprim

MeshやSphereなど、実際に描画される形を持つPrimの総称です。Geometric Primitiveの略です。

### HasAPI

そのPrimに指定のAPI Schemaが付いているかを返すPython API。

### HasAuthoredReferences

そのPrimにReferenceが記述されているかを返すPython API。

### HasAuthoredValue

そのAttributeに値が実際に書かれているかを返すPython API。

### Hydra

Stageの内容を受け取り、実際に描く仕組みへ渡す層です。

### identifier（Layer）

そのLayerを一意に示す文字列。多くはファイルのPath。

### identity

そのAssetが何であるかを示す情報。名前・バージョン・種別など。

### ids

PointInstancerの各配置に振る番号。表示制御の対象を指すのに使う。

### Imageable

画像化される可能性のあるPrimに共通する性質をまとめたSchemaの基盤です。

### Inactive

`active = false`により、子孫ごと構成から外された状態。

### inactiveIds

指定したidの配置を無かったことにするPrim Metadata。

### Indexed Primvar

値配列と、その値を参照するindex配列を分けたPrimvarです。

### indices

値の配列の何番目を使うかを並べた `int[]` の配列です。Primvar名の後ろに `:indices` を付けて表します。

### info:id

そのShaderがどの種類かを示すAttribute。

### Inherits

別のPrimの意見を受け取るComposition Arc。`class`と組み合わせて使うことが多い。

### Instance

共有するPrototypeをシーン内で繰り返し利用するものです。

### Instance Proxy

Instanceの内側のPrimを読むための、書き込みできないPrimです。

### Instance Refinement

共有を保ったまま、Instanceごとに差を付けること。

### instanceable

そのPrimをInstanceにするかを決めるPrim Metadataです。

### Internal Arc

同じLayerの中の別のPrimを指すComposition Arc。

### Interpolation（補間）

Primvarの値をGprimのどの単位へ対応させるかを決めるMetadataです。

### invisibleIds

指定したidの配置を描画しないようにする配列。

### IsA

そのPrimが指定した型かどうかを判定するPython API。

### IsAncestral

そのArcがAncestralかどうかを返すPython API。

### IsCustom

そのPropertyがCustomかどうかを返すPython API。

### kilogramsPerUnit

そのLayerの質量の「1」が実世界の何キログラムかを示すLayer Metadata。

### Kind

PrimのModel Hierarchy上の役割を示すMetadataです。

### Kind.Tokens

PythonからKindを指定するための定数群。`component`や`assembly`など。

### Layer Metadata

ファイル先頭の丸括弧の中に書く、Layer全体に関わるMetadata。

### Layer Stack

root layerと再帰的なsublayerからなる順序付きのLayer集合です。

### Layer（レイヤー）

シーン記述の一部分を保持するデータの単位です。

### LinearUnits

Pythonで長さの単位を指定するための定数群。`UsdGeom.LinearUnits.centimeters`など。

### List Editing

一覧を持つ項目に対して、部分的な追加・削除・並べ替えを記述する仕組みです。

### ListOp

List Editingの内容を保持する`Sdf`側のデータ構造。

### LIVERPS

Local、Inherits、Variant Sets、rElocates、References、Payloads、Specializesを強い順に並べた略語です。SublayerのOpinionはLayer Stack内のLocalに含まれます。

### Load / Unload

Payloadの中身をStageへ読み込む、または外す操作。

### Load Set

現在Loadされているものの集合。`GetLoadSet()`で取得できる。

### LoadAll / LoadNone

Stageを開くときの初期Load状態を指定する定数。

### Load境界

Payloadを張った位置。ここから先を開くかどうかを選べる。

### Lofting

中身から計算した要約を、入口側へ書き写しておくことです。

### MassUnits

Pythonで質量の単位を指定するための定数群。`kilograms`、`grams`、`slugs`。

### Material

見た目のひとまとまりを表すPrimです。値そのものは持たず、Shaderへの接続を持ちます。

### Material Binding

GprimからMaterialへの結び付きです。`material:binding`というRelationshipで書かれます。

### MaterialBindingAPI

Bindingを読み書きするAPI Schema。

### matrix

行と列に並んだ数のまとまりです。`matrix4d`は座標変換に使います。

### Metadata（メタデータ）

Prim、Property、Layerに付ける時間変化しない補助情報です。

### metersPerUnit

そのLayerの長さの「1」が実世界の何メートルかを示すLayer Metadata。

### Module（モジュール）

関連するOpenUSD APIをまとめた単位です。例: Usd、Sdf、Gf。

### Namespace（名前空間）

Property名をコロンで区切って階層的にまとめる仕組みです。

### Nested Instancing

Instanceを含むPrimを、さらにInstanceにすること。

### non-applied API Schema

記録を残さず、読み書きの窓口としてだけ働くAPI Schema。

### OpenUSD

3Dシーンを記述、合成、シミュレーション、共同作業するためのフレームワーク。

### Opinion（意見）

あるLayerが、あるPropertyやMetadataに対して持つ値の主張。

### orientations / scales

PointInstancerで、向きと大きさを配置ごとに指定する配列。

### over

Primを定義せず、意見だけを重ねるSpecifierです。

### OverridePrim

`over`のPrim Specを作るPython API。

### parameter

使う側が調整してよい値。

### Path Translation

参照などにより、Layer内のPathが合成後のPathへ移し替えられること。

### Path（パス）

Stage内のPrimやPropertyを指す住所のような識別子です。例: `/World/Room`。

### Payload

読み込みを後回しにできるComposition Arc。

### Pcp

Compositionの計算を担当するモジュール。Arcの種類は`Pcp.ArcType…`で表される。

### Pcp.ArcTypePayload

Composition QueryでPayloadのArcを判別するための値。

### Pivot

回転と拡縮の中心として使う位置です。対になるinverse operationと組み合わせます。

### Point

Meshの頂点の位置です。`points`に並ぶ座標を指します。

### Point Instancing

配列で位置と種類を並べ、大量の配置を1つのPrimで表す仕組みです。

### PointInstancer

Point Instancingを担うPrim型。

### positions

各配置の位置を並べた`point3f[]`の配列。

### prepend

一覧の先頭へ項目を足すキーワード。

### Prim Composition

同じPathへ寄与する複数のPrim Specを、規則にしたがって一つのPrimへまとめることです。

### Prim Hierarchy Transformation

受け取った階層を、こちらの規則の階層へ組み替えること。

### Prim Metadata

Prim名の後ろの丸括弧の中に書く、そのPrimに関するMetadata。

### Prim name（Prim名）

階層内のPrimを識別し、Pathの一部分になる名前です。例: `World`。

### Prim Path

Stage内のPrimを識別するPathです。Prim名を `/` で区切ります。

### Prim Spec

一つのLayerの中に書かれた、あるPathに対するPrimの記述。

### Prim Stack

あるPrimへ寄与するPrim Specを、強い順に並べたリストです。

### PrimAllPrimsPredicate

何も除かない条件。`TraverseAll()`と同じ結果になる。

### PrimCompositionQuery

あるPrimに効いているComposition Arcを調べるPython API。

### PrimDefaultPredicate

`Traverse()`が既定で使う条件。

### PrimIsLoaded

Payloadが読み込まれているかを判定するフラグ。

### PrimIsModel / PrimIsGroup

KindがModelに属するか、そのうちGroupにあたるかを判定するフラグ。

### Primvar

名前が `primvars:` で始まり、Interpolation・index・継承を扱えるAttributeです。

### Primvar Inheritance

`constant`のPrimvarがScene Namespaceを下って子のImageable Primへ適用される仕組みです。

### PrimvarsAPI

Prim上のPrimvarを作成・取得するためのAPI Schemaです。

### Prim（プリム）

Stageを構成する基本要素。シーングラフ上のノードです。

### Property Path

Prim Pathの後ろに `.` とProperty名を続けたPathです。

### Property Stack

あるPropertyへ値を主張しているSpecを、強い順に並べたリストです。

### Property（プロパティ）

Primが持つ情報。AttributeとRelationshipの2種類があります。

### protoIndices

各配置がどのPrototypeを使うかを並べた`int[]`の配列。

### Prototype

複数のInstanceが共有するシーン構造です。

### Prototypeの階層

外側のPrototypeが内側のInstanceを持ち、内側のPrototypeが実際の形を持つ構造。

### pseudo-root（疑似ルート）

Stage階層の出発点です。Pathでは `/` で表します。

### purpose

そのPrimを何のために描くかを示すImageableのAttribute。描画対象かどうかに関わる。

### Reference/Payload Pattern

外からはReference、入口から中身へはPayloadでつなぐ、Asset構成の基本形です。

### References

別のLayerの内容を、あるPrimの下へ読み込むComposition Arc。

### Relationship（リレーションシップ）

0個以上のPrim PathまたはProperty Pathを対象として持てる、型のないPropertyです。

### Render Delegate

実際に絵を作る実装です。Storm、Metal、RenderManなど。

### Render Index

供給された内容をHydra側で保持し、描く側へ渡す部分。

### reorder

既にある項目の順番だけを変えるキーワード。

### role

値が位置・向き・法線・色・テクスチャ座標のどれを表すかという、Value Typeの意味の部分です。

### Rotate

軸の周りにPrimの向きを変える変換操作です。複数軸を使うときはRotation Orderも結果へ影響します。

### scalar

数が一つだけの値の形です。`double`や`int`などが該当します。

### Scale

Primの各軸方向の大きさへ倍率を掛ける変換操作です。変更しない倍率は1です。

### Scene

Assetを参照して配置し、そのシーンにしか無いものを加えたファイル。

### Scene Delegate

シーンの内容をHydraへ供給する仕組み。

### Scene Index

新しい世代で、Scene Delegateに代わって内容を供給する仕組み。

### Scene Namespace

Primの親子関係でできた名前の階層です。Pathで表されます。

### Scenegraph Instancing

合成結果が同じPrimの中身を、一つのPrototypeとして共有する仕組みです。

### SchemaRegistry

Schemaの種別や性質を問い合わせるためのPython API。

### Schema（スキーマ）

PrimやPropertyの構造、意味、取得・作成APIを定める設計図です。

### Scope

変換を持たず、Primを論理的に整理するconcrete IsA Schemaです。

### Sdf.AttributeSpec

一つのLayerに書かれた、合成前のAttributeの記述を表すオブジェクト。

### Sdf.CopySpec

Layer上の記述を、別のPathへそのまま写すPython API。

### Sdf.Layer

合成前のファイル一枚を表すオブジェクト。`defaultPrim`などを読める。

### Sdf.PrimSpec

一つのLayerに書かれた、合成前のPrimの記述を表すオブジェクト。

### Sdf.ValueTypeNames

PythonからAttributeのValue Typeを指定するための名前の一覧です。

### Seam（継ぎ目）

Faceの境目で値が不連続になる場所です。UVを展開したときの切れ目などを指します。

### Session Layer

Stageを開いたときに用意される、保存されない一時的なLayer。

### SetActive / ClearActive

`active`を書く、または記述を取り除くPython API。

### SetDefaultPrim

Layerの入口となるPrimを設定するPython API。

### SetTargets

Target Listを、渡した一覧の内容に置き換えるPython API。

### Shader

見た目の計算を担うPrimです。`inputs:`で始まる入力に実際の値を持ちます。

### single-apply / multiple-apply

1回だけ付けられるか、インスタンス名を変えて何度でも付けられるかの区別。

### Sparse Authoring（疎な記述）

同じ情報を必要な最小限の場所にだけ書く考え方です。

### Specifier

Prim Specの先頭に置き、そのPrimの扱い方を決める語です。`def`・`over`・`class`の3種類。

### SplitName

Namespaceで区切られたProperty名を要素に分解するPython API。

### st

UVを保持するPrimvarの、慣習的な名前。

### StageHasAuthoredKilogramsPerUnit

値が実際に記述されているかどうかを返すPython API。

### Stage（ステージ）

合成されたOpenUSDシーンにアクセスする中心的なオブジェクトです。

### Subdivision Surface（細分化サーフェス）

粗い多角形Meshを規則にしたがって細かく分割し、なめらかな形を作る仕組みです。

### subdivisionScheme

Meshを細分化するかどうかを決めるAttributeです。`none`は細分化せず、書いた多角形のまま扱います。

### subLayerPaths

Sublayerの一覧を保持するPython側のリスト。

### subLayers

あるLayerが重ねる他のLayerの一覧を示すLayer Metadata。

### Target

Relationshipが指すPrimまたはPropertyのPath。

### Target List

Relationshipが持つTarget Pathの一覧です。対象が一つのときも一覧として扱われます。

### texCoord2f

テクスチャ座標を表すValue Type。roleは`TextureCoordinate`。

### Time Code

単位を持たない時間上の位置です。

### Time Sample

特定のTime Codeに記述されたAttribute値です。

### token

決まった語を効率よく扱うための文字列型です。選択肢が決まっている場所で使われます。

### Topology（トポロジー）

PointとFaceのつながり方です。Primvarに必要な値の個数はこれで決まります。

### Translate

PrimをX・Y・Z方向へ移動する変換操作です。通常は`xformOp:translate`として記述します。

### Traversal Predicate

走査で降りるかどうかを決める条件。フラグを`&amp;`・`|`・`~`で組み合わせて作る。

### Traversal（走査）

Stage上のPrimを順に訪れること。

### Traverse / TraverseAll

Stage上のPrimを順に回るPython API。前者は既定で定義済みのPrimだけ、後者は定義されていないPrimも含む。

### TraverseInstanceProxies

Instance Proxyも走査に含める条件を作るPython API。

### Typed Schema

Primの型そのものになるSchema。`def Mesh`の`Mesh`にあたる。

### uniform

Faceごとに一つの値を対応させるPrimvar Interpolationです。Attributeの宣言に付く`uniform`（時間変化しない）とは別の意味です。

### Unresolved reference

参照先を解決できなかった状態。Primは残るが中身が空になる。

### upAxis

そのLayerで上とみなす軸を示すLayer Metadata。`'Y'`または`'Z'`。

### USD

UTF-8テキストまたはCrateバイナリを格納できるOpenUSDファイル拡張子です。

### Usd.ModelAPI

KindやAsset情報を読み書きするAPI Schema。

### Usd.PrimRange

任意のPrimを起点に、その配下を走査するPythonのオブジェクト。

### Usd.TimeCode.Default()

時間に依存しない値を指すTime Code。

### USDA

人が読めるUTF-8テキスト形式のOpenUSDファイル表現です。

### USDC

ランダムアクセスに対応するバイナリのCrate形式です。

### usdcat

USDファイルの内容を表示するコマンド。`--flatten`で合成後の姿を出せる。

### usdchecker

OpenUSD一般の規則を検査するコマンドです。終了コードで結果が分かります。

### UsdGeom.ModelAPI

`extentsHint`などのモデル情報を読み書きするAPI Schema。

### UsdGeomPrimvar

Primvarを読み書きするためのPythonのクラス。

### UsdPhysics

物理シミュレーション向けのSchemaとAPIをまとめたモジュール。

### UsdPreviewSurface

ツール間で共通して扱える、標準的なShaderの種類。

### usdrecord

Stageを画像として描き出すコマンドです。

### usdtree

Stageの階層を、Specifierと型名付きのツリーで表示するコマンドです。

### USDZ

複数アセットを一つにまとめる、配布向けの非圧縮ZIPパッケージです。

### UTF-8

Unicode文字を表す文字エンコーディングです。USDAは人が読めるUTF-8テキスト形式です。

### UV

Surface上の位置をテクスチャ画像の座標へ対応させる値です。`faceVarying`で持たせることが多い値です。

### Validation（検証）

アセットが規則を守っているかを、実行できる形で確かめることです。

### Value Type

Attributeが保持する値の型です。値の形と、その値が何を意味するか（role）の両方を決めます。

### Variant

Variant Setの中の一つの選択肢。

### Variant Edit Context

書き込み先を、選択中のVariantの内側へ切り替えるPythonのコンテキストです。

### Variant Selection

どの選択肢を使うかを示すPrim Metadata。

### Variant Set

名前の付いた選択肢の組を、一つのPrimにまとめる仕組み。

### varying

Pointごとに一つの値を対応させ、Surface上を線形に補間するPrimvar Interpolationです。

### vector

複数の数をひとまとまりにした値の形です。USDAでは丸括弧で囲みます。

### vertex

Pointごとに一つの値を対応させ、Surfaceの基底関数で補間するPrimvar Interpolationです。

### visibility

描画するかどうかを決めるImageableのAttribute。Inactiveとは別の仕組み。

### Vt.Vec3fArray / Vt.IntArray

Pythonのリストを、USDが扱える配列へ包む型。

### Workstream Layer

作業の種類ごとに分けたLayerです。同じPathへ、担当ぶんだけを書きます。

### XformCommonAPI

一般的な移動・回転・拡縮・pivotを共通構成で扱うnon-applied API Schemaです。

### XformOp

Xformに記述される移動、回転、拡大縮小など一つの変換操作です。

### xformOp:rotateX

X軸まわりにPrimを回転させるXformOp。上方向の補正に使う。

### xformOp:scale

Primの大きさへ倍率を掛けるXformOp。単位の補正にも使う。

### XformOpOrder

使用するxformOpとtransform stack上の順序を保持するtoken配列です。

### Xform（エックスフォーム）

移動、回転、拡大縮小などの変換データを保持し、子Primに適用できるPrim型です。

### Y-up / Z-up

上方向をどの軸に取るかという座標系の慣習。ツールによって異なる。

### yield

Pythonで、値を1つずつ返す関数を書くための仕組み。

### シーン固有のもの

地面・カメラ・照明など、そのシーンだけで使うPrim。

### プリセット

よく使う条件の組み合わせに名前を付けたもの。

### 内部実装

公開していない部分。Prim名や階層の形など、自由に変えてよいもの。

### 再利用の単位

差し替え・共有・Loadの制御が効く最小のまとまり。

### 単位の変換

入力の数値を、出力の`metersPerUnit`に合う値へ直すこと。

### 受け入れ検査

受け取った側で、渡されたものが約束どおりかを確かめること。

### 型名（typeName）

Specifierの後ろに書く、そのPrimのSchemaを示す名前。省略できる。

### 基底関数（basis function）

Surface上の位置から値を求めるための重み付けの規則です。

### 寄与する（contribute）

あるLayerの記述が、合成結果に関わっていること。

### 既定の選択

使う側が何も指定しなかったときに使われる選択肢。

### 既定値（default）

何も指定しなかったときに使われる条件。

### 最小のValidation

踏んだ失敗から1つずつ育てていく、小さな検査の集まり。

### 来歴（provenance）

そのデータがどう作られたかの記録。

### 枝刈り（pruning）

条件に合わないPrimに出会った時点で、その配下を訪れないこと。

### 深さ優先・行きがけ順

親を先に返し、子へ降りきってから兄弟へ移る訪問順。

### 相互運用

異なるアプリケーション間でデータを扱えること。

### 粒度（granularity）

まとまりの細かさ。細かすぎても粗すぎても扱いにくくなる。

### 総合演習

これまでに学んだ内容を組み合わせて、一つの成果物を作ること。

### 線形補間

2つの値の間を、距離に比例した割合でまっすぐつなぐ補間です。

### 調査の順番

Layer Stack → Prim Stack → Property Stack と、粗いほうから絞ること。

### 配れる形

入口・名乗り・検査を備え、他のシーンから参照して使える状態。

### 配置（layout）

どのAssetをどこへ置くか、というシーン側の情報。

### 階層の規則

形や色をどのPathの下に置くか、という取り決め。

### 非破壊

元データを直接上書きせず、変更を重ねて結果を作る考え方。

### 非破壊編集

元のファイルを書き換えずに、上のLayerで変更を表現する編集の仕方。
