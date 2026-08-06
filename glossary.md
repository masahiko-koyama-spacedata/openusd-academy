# OpenUSD Academy 用語集

このファイルはサイト全体の索引です。個々のレッスンにも、その回で使う用語集を必ず付けます。定義はレッスン執筆時に [NVIDIA Learn OpenUSD](https://docs.nvidia.com/learn-openusd/latest/index.html) の公式用語集と該当ページを確認します。

## A–Z

### Attribute（アトリビュート）

Primが持つ値のあるProperty。たとえば色、サイズ、位置などを表す。

### UTF-8

Unicode文字を表す文字エンコーディング。USDAは人が読めるUTF-8テキスト形式。

### Composition（コンポジション）

複数のシーン記述を規則に従って一つの結果へ組み立てる仕組み。

### Composition Arc

複数のシーン記述を組み合わせる演算子。

### Instance

共有するPrototypeをシーン内で繰り返し利用するもの。

### Kind

PrimのModel Hierarchy上の役割を示すMetadata。

### Layer（レイヤー）

シーン記述の一部分を保持するデータの単位。複数のLayerを合成してStageを作れる。

### Layer Stack

root layerと再帰的なsublayerからなる順序付きのLayer集合。

### LIVERPS

Local、Inherits、Variant Sets、rElocates、References、Payloads、Specializesを強い順に並べた略語。SublayerのOpinionはLayer Stack内のLocalに含まれる。

### Metadata（メタデータ）

Prim、Property、Layerに付ける時間変化しない補助情報。

### Default Prim（デフォルトプリム）

Layer Metadataで指定する、そのLayerの主な入口となるtop-level Prim。外部ReferenceやPayloadで対象Prim Pathを省略するときに使われる。

### Module（モジュール）

関連するOpenUSD APIをまとめた単位。例: Usd、Sdf、Gf。

### Scope

変換を持たず、Primを論理的に整理するconcrete IsA Schema。

### XformCommonAPI

一般的な単一の移動・回転・拡縮・pivotを、交換しやすい共通構成で扱うnon-applied API Schema。

### Translate

PrimをX・Y・Z方向へ移動する変換操作。通常は<code>xformOp:translate</code>として記述する。

### Rotate

軸の周りにPrimの向きを変える変換操作。複数軸を使うときはRotation Orderも結果へ影響する。

### Scale

Primの各軸方向の大きさへ倍率を掛ける変換操作。変更しない倍率は1。

### Pivot

回転と拡縮の中心として使う位置。対になるinverse operationと組み合わせる。

### Path（パス）

Stage内のPrimやPropertyを指す住所のような識別子。例: `/World/Room`。

### Prim name（Prim名）

階層内のPrimを識別し、Pathの一部分になる名前。例: `World`。

### Prim Path

Stage内のPrimを識別するPath。Prim名を `/` で区切る。

### Prim（プリム）

Stageを構成する基本要素。シーングラフ上のノードとして、オブジェクトやまとまりを表す。

### Property（プロパティ）

Primが持つ情報。AttributeとRelationshipの2種類がある。

### Property Path

Prim Pathの後ろに `.` とProperty名を続けたPath。

### Prototype

複数のInstanceが共有するシーン構造。

### Relationship（リレーションシップ）

0個以上のPrim PathまたはProperty Pathを対象として持てる、型のないProperty。

### Stage（ステージ）

合成されたOpenUSDシーンにアクセスするための中心的なオブジェクト。

### Schema（スキーマ）

PrimやPropertyの構造、意味、取得・作成APIを定める設計図。

### Time Code

単位を持たない時間上の位置。

### Time Sample

特定のTime Codeに記述されたAttribute値。

### USDA

人が読めるUTF-8テキスト形式のOpenUSDファイル表現。構造や値を直接確認しやすい。

### USDC

ランダムアクセスに対応するバイナリのCrate形式。

### USD

UTF-8テキストまたはCrateバイナリを格納できるOpenUSDファイル拡張子。

### USDZ

複数アセットを一つにまとめる、配布向けの非圧縮ZIPパッケージ。

### Xform（エックスフォーム）

移動、回転、拡大縮小などの変換データを保持し、子Primに適用できるPrim型。

### XformOp

Xformに記述される移動、回転、拡大縮小など一つの変換操作。

### XformOpOrder

使用するxformOpとtransform stack上の順序を保持するtoken配列。

### def（デフ）

現在のLayerでPrimを具体的に定義するSpecifier。

### pseudo-root（疑似ルート）

Stage階層の出発点。Pathでは `/` で表す。

> **注意:** 上記はAcademyによる初学者向け要約です。技術的な厳密さが必要な場合は、各レッスンの公式リファレンスを参照してください。
