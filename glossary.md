# OpenUSD Academy 用語集

このファイルはサイト全体の索引です。個々のレッスンにも、その回で使う用語集を必ず付けます。定義はレッスン執筆時に [NVIDIA Learn OpenUSD](https://docs.nvidia.com/learn-openusd/latest/index.html) の公式用語集と該当ページを確認します。

## A–Z

### Attribute（アトリビュート）

Primが持つ値のあるProperty。たとえば色、サイズ、位置などを表す。

### ASCII

文字として読めるデータ表現。USDAはASCII形式。

### Composition（コンポジション）

複数のシーン記述を規則に従って一つの結果へ組み立てる仕組み。

### Layer（レイヤー）

シーン記述の一部分を保持するデータの単位。複数のLayerを合成してStageを作れる。

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

### Relationship（リレーションシップ）

あるPrimやPropertyから、別のオブジェクトへのつながりを表すProperty。

### Stage（ステージ）

合成されたOpenUSDシーンにアクセスするための中心的なオブジェクト。

### USDA

人が読めるテキスト形式のOpenUSDファイル表現。構造や値を直接確認しやすい。

### USDC

圧縮されたバイナリのCrate形式。

### USD

ASCIIまたはバイナリを格納できるOpenUSDファイル拡張子。

### USDZ

複数アセットを一つにまとめる、配布向けの非圧縮ZIPパッケージ。

### Xform（エックスフォーム）

移動、回転、拡大縮小などの変換データを保持し、子Primに適用できるPrim型。

### def（デフ）

現在のLayerでPrimを具体的に定義するSpecifier。

### pseudo-root（疑似ルート）

Stage階層の出発点。Pathでは `/` で表す。

> **注意:** 上記はAcademyによる初学者向け要約です。技術的な厳密さが必要な場合は、各レッスンの公式リファレンスを参照してください。
