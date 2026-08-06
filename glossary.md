# OpenUSD Academy 用語集

このファイルはサイト全体の索引です。個々のレッスンにも、その回で使う用語集を必ず付けます。定義はレッスン執筆時に [NVIDIA Learn OpenUSD](https://docs.nvidia.com/learn-openusd/latest/index.html) の公式用語集と該当ページを確認します。正本は `glossary.html` です。

## 用語一覧

### array

同じ型の値が並ぶ値の形です。型名の末尾に `[]` が付きます。

### asset

他のファイルを指すパスのValue Typeです。USDAでは `@ball.usda@` のようにアットマークで囲みます。

### Attribute（アトリビュート）

Primが持つ値のあるProperty。色、サイズ、位置などを表します。

### catmullClark

OpenUSDのMeshで既定となっている細分化の方式です。

### Composition Arc

複数のシーン記述を組み合わせる演算子です。

### Composition（コンポジション）

複数のシーン記述を規則に従って一つの結果へ組み立てる仕組みです。

### ComputeFlattened

Indexed Primvarのindexを解いた後の値の並びを返すPython APIです。

### constant

Gprim全体へ値を一つだけ対応させるPrimvar Interpolationです。値の個数は形によらず常に1です。

### Default Prim（デフォルトプリム）

Layer Metadataで指定する、そのLayerの主な入口となるtop-level Primです。

### def（デフ）

現在のLayerでPrimを具体的に定義するSpecifierです。

### displayColor

Gprimに最初から用意されている表示用の色のPrimvarです。既定のinterpolationは`constant`です。

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

### FindPrimvarWithInheritance

自分に無ければ親をさかのぼってPrimvarを探すPython APIです。

### GetAuthoredPrimvars

そのPrimに実際に記述されたPrimvarだけを返すPython APIです。

### Gprim

MeshやSphereなど、実際に描画される形を持つPrimの総称です。Geometric Primitiveの略です。

### Imageable

画像化される可能性のあるPrimに共通する性質をまとめたSchemaの基盤です。

### Indexed Primvar

値配列と、その値を参照するindex配列を分けたPrimvarです。

### indices

値の配列の何番目を使うかを並べた `int[]` の配列です。Primvar名の後ろに `:indices` を付けて表します。

### Instance

共有するPrototypeをシーン内で繰り返し利用するものです。

### Interpolation（補間）

Primvarの値をGprimのどの単位へ対応させるかを決めるMetadataです。

### Kind

PrimのModel Hierarchy上の役割を示すMetadataです。

### Layer Stack

root layerと再帰的なsublayerからなる順序付きのLayer集合です。

### Layer（レイヤー）

シーン記述の一部分を保持するデータの単位です。

### LIVERPS

Local、Inherits、Variant Sets、rElocates、References、Payloads、Specializesを強い順に並べた略語です。SublayerのOpinionはLayer Stack内のLocalに含まれます。

### matrix

行と列に並んだ数のまとまりです。`matrix4d`は座標変換に使います。

### Metadata（メタデータ）

Prim、Property、Layerに付ける時間変化しない補助情報です。

### Module（モジュール）

関連するOpenUSD APIをまとめた単位です。例: Usd、Sdf、Gf。

### Namespace（名前空間）

Property名をコロンで区切って階層的にまとめる仕組みです。

### Path（パス）

Stage内のPrimやPropertyを指す住所のような識別子です。例: `/World/Room`。

### Pivot

回転と拡縮の中心として使う位置です。対になるinverse operationと組み合わせます。

### Point

Meshの頂点の位置です。`points`に並ぶ座標を指します。

### Prim name（Prim名）

階層内のPrimを識別し、Pathの一部分になる名前です。例: `World`。

### Prim Path

Stage内のPrimを識別するPathです。Prim名を `/` で区切ります。

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

### Property（プロパティ）

Primが持つ情報。AttributeとRelationshipの2種類があります。

### Prototype

複数のInstanceが共有するシーン構造です。

### pseudo-root（疑似ルート）

Stage階層の出発点です。Pathでは `/` で表します。

### Relationship（リレーションシップ）

0個以上のPrim PathまたはProperty Pathを対象として持てる、型のないPropertyです。

### role

値が位置・向き・法線・色・テクスチャ座標のどれを表すかという、Value Typeの意味の部分です。

### Rotate

軸の周りにPrimの向きを変える変換操作です。複数軸を使うときはRotation Orderも結果へ影響します。

### scalar

数が一つだけの値の形です。`double`や`int`などが該当します。

### Scale

Primの各軸方向の大きさへ倍率を掛ける変換操作です。変更しない倍率は1です。

### Scene Namespace

Primの親子関係でできた名前の階層です。Pathで表されます。

### Schema（スキーマ）

PrimやPropertyの構造、意味、取得・作成APIを定める設計図です。

### Scope

変換を持たず、Primを論理的に整理するconcrete IsA Schemaです。

### Sdf.ValueTypeNames

PythonからAttributeのValue Typeを指定するための名前の一覧です。

### Seam（継ぎ目）

Faceの境目で値が不連続になる場所です。UVを展開したときの切れ目などを指します。

### Sparse Authoring（疎な記述）

同じ情報を必要な最小限の場所にだけ書く考え方です。

### Stage（ステージ）

合成されたOpenUSDシーンにアクセスする中心的なオブジェクトです。

### Subdivision Surface（細分化サーフェス）

粗い多角形Meshを規則にしたがって細かく分割し、なめらかな形を作る仕組みです。

### subdivisionScheme

Meshを細分化するかどうかを決めるAttributeです。`none`は細分化せず、書いた多角形のまま扱います。

### Target List

Relationshipが持つTarget Pathの一覧です。対象が一つのときも一覧として扱われます。

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

### uniform

Faceごとに一つの値を対応させるPrimvar Interpolationです。Attributeの宣言に付く`uniform`（時間変化しない）とは別の意味です。

### USD

UTF-8テキストまたはCrateバイナリを格納できるOpenUSDファイル拡張子です。

### USDA

人が読めるUTF-8テキスト形式のOpenUSDファイル表現です。

### USDC

ランダムアクセスに対応するバイナリのCrate形式です。

### USDZ

複数アセットを一つにまとめる、配布向けの非圧縮ZIPパッケージです。

### UTF-8

Unicode文字を表す文字エンコーディングです。USDAは人が読めるUTF-8テキスト形式です。

### UV

Surface上の位置をテクスチャ画像の座標へ対応させる値です。`faceVarying`で持たせることが多い値です。

### Value Type

Attributeが保持する値の型です。値の形と、その値が何を意味するか（role）の両方を決めます。

### varying

Pointごとに一つの値を対応させ、Surface上を線形に補間するPrimvar Interpolationです。

### vector

複数の数をひとまとまりにした値の形です。USDAでは丸括弧で囲みます。

### vertex

Pointごとに一つの値を対応させ、Surfaceの基底関数で補間するPrimvar Interpolationです。

### XformCommonAPI

一般的な移動・回転・拡縮・pivotを共通構成で扱うnon-applied API Schemaです。

### XformOp

Xformに記述される移動、回転、拡大縮小など一つの変換操作です。

### XformOpOrder

使用するxformOpとtransform stack上の順序を保持するtoken配列です。

### Xform（エックスフォーム）

移動、回転、拡大縮小などの変換データを保持し、子Primに適用できるPrim型です。

### 基底関数（basis function）

Surface上の位置から値を求めるための重み付けの規則です。

### 線形補間

2つの値の間を、距離に比例した割合でまっすぐつなぐ補間です。
