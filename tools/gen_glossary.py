# -*- coding: utf-8 -*-
"""Single source for the site-wide glossary; emits glossary.html and glossary.md."""
import os
import re

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# (term, definition) -- definitions end with です/ます in the HTML edition.
TERMS = [
    ("array", "同じ型の値が並ぶ値の形です。型名の末尾に <code>[]</code> が付きます。"),
    ("asset", "他のファイルを指すパスのValue Typeです。USDAでは <code>@ball.usda@</code> のようにアットマークで囲みます。"),
    ("Asset", "独立して参照できるまとまりです。多くは1ファイルで、入口となるPrimを持ちます。"),
    ("Asset Interface", "Assetが外へ公開する情報の集まりです。使う側との約束にあたります。"),
    ("Converter", "他のツールの形式からUSDを作る処理です。読む・対応づける・書くの3段に分けます。"),
    ("Dangling target", "存在しないPathを指したままのRelationshipのtargetです。<code>usdchecker</code>では報告されません。"),
    ("Encapsulation（カプセル化）", "持ち込まれた側のComposition Arcが、そのファイルの中で完結していることです。"),
    ("Entry Point（入口）", "Assetを外から使うときに最初に開かれるファイル、およびそのPrimです。"),
    ("Export Options", "変換の条件を、外から指定できるようにしたものです。"),
    ("Hydra", "Stageの内容を受け取り、実際に描く仕組みへ渡す層です。"),
    ("Instance Proxy", "Instanceの内側のPrimを読むための、書き込みできないPrimです。"),
    ("List Editing", "一覧を持つ項目に対して、部分的な追加・削除・並べ替えを記述する仕組みです。"),
    ("Lofting", "中身から計算した要約を、入口側へ書き写しておくことです。"),
    ("Material", "見た目のひとまとまりを表すPrimです。値そのものは持たず、Shaderへの接続を持ちます。"),
    ("Material Binding", "GprimからMaterialへの結び付きです。<code>material:binding</code>というRelationshipで書かれます。"),
    ("Point Instancing", "配列で位置と種類を並べ、大量の配置を1つのPrimで表す仕組みです。"),
    ("Prim Composition", "同じPathへ寄与する複数のPrim Specを、規則にしたがって一つのPrimへまとめることです。"),
    ("Prim Stack", "あるPrimへ寄与するPrim Specを、強い順に並べたリストです。"),
    ("Property Stack", "あるPropertyへ値を主張しているSpecを、強い順に並べたリストです。"),
    ("Reference/Payload Pattern", "外からはReference、入口から中身へはPayloadでつなぐ、Asset構成の基本形です。"),
    ("Render Delegate", "実際に絵を作る実装です。Storm、Metal、RenderManなど。"),
    ("Scenegraph Instancing", "合成結果が同じPrimの中身を、一つのPrototypeとして共有する仕組みです。"),
    ("Shader", "見た目の計算を担うPrimです。<code>inputs:</code>で始まる入力に実際の値を持ちます。"),
    ("Specifier", "Prim Specの先頭に置き、そのPrimの扱い方を決める語です。<code>def</code>・<code>over</code>・<code>class</code>の3種類。"),
    ("Validation（検証）", "アセットが規則を守っているかを、実行できる形で確かめることです。"),
    ("Variant Edit Context", "書き込み先を、選択中のVariantの内側へ切り替えるPythonのコンテキストです。"),
    ("Workstream Layer", "作業の種類ごとに分けたLayerです。同じPathへ、担当ぶんだけを書きます。"),
    ("class", "他のPrimが受け取るための意見をまとめて置く、abstractなPrimを作るSpecifierです。"),
    ("def", "Primを定義するSpecifierです。Stage上にdefinedなPrimとして現れます。"),
    ("instanceable", "そのPrimをInstanceにするかを決めるPrim Metadataです。"),
    ("over", "Primを定義せず、意見だけを重ねるSpecifierです。"),
    ("usdchecker", "OpenUSD一般の規則を検査するコマンドです。終了コードで結果が分かります。"),
    ("usdrecord", "Stageを画像として描き出すコマンドです。"),
    ("usdtree", "Stageの階層を、Specifierと型名付きのツリーで表示するコマンドです。"),
    ("Attribute（アトリビュート）", "Primが持つ値のあるProperty。色、サイズ、位置などを表します。"),
    ("catmullClark", "OpenUSDのMeshで既定となっている細分化の方式です。"),
    ("ComputeFlattened", "Indexed Primvarのindexを解いた後の値の並びを返すPython APIです。"),
    ("Composition（コンポジション）", "複数のシーン記述を規則に従って一つの結果へ組み立てる仕組みです。"),
    ("Composition Arc", "複数のシーン記述を組み合わせる演算子です。"),
    ("constant", "Gprim全体へ値を一つだけ対応させるPrimvar Interpolationです。値の個数は形によらず常に1です。"),
    ("def（デフ）", "現在のLayerでPrimを具体的に定義するSpecifierです。"),
    ("Default Prim（デフォルトプリム）", "Layer Metadataで指定する、そのLayerの主な入口となるtop-level Primです。"),
    ("displayColor", "Gprimに最初から用意されている表示用の色のPrimvarです。既定のinterpolationは<code>constant</code>です。"),
    ("Face", "Meshを構成する面です。<code>faceVertexCounts</code>の要素数がFaceの枚数になります。"),
    ("Face Vertex", "あるFaceが頂点を使った一回分です。同じPointが複数のFaceから使われると、その回数だけ増えます。"),
    ("faceVarying", "Face Vertexごとに一つの値を対応させるPrimvar Interpolationです。Faceの境目で値を不連続にできます。"),
    ("faceVertexCounts", "各Faceの頂点数を順に並べた配列です。要素数がFaceの枚数になります。"),
    ("faceVertexIndices", "各Faceがどのpointを使うかを、<code>points</code>の位置番号で並べた配列です。"),
    ("FindPrimvarWithInheritance", "自分に無ければ親をさかのぼってPrimvarを探すPython APIです。"),
    ("GetAuthoredPrimvars", "そのPrimに実際に記述されたPrimvarだけを返すPython APIです。"),
    ("Gprim", "MeshやSphereなど、実際に描画される形を持つPrimの総称です。Geometric Primitiveの略です。"),
    ("Imageable", "画像化される可能性のあるPrimに共通する性質をまとめたSchemaの基盤です。"),
    ("Indexed Primvar", "値配列と、その値を参照するindex配列を分けたPrimvarです。"),
    ("indices", "値の配列の何番目を使うかを並べた <code>int[]</code> の配列です。Primvar名の後ろに <code>:indices</code> を付けて表します。"),
    ("Instance", "共有するPrototypeをシーン内で繰り返し利用するものです。"),
    ("Interpolation（補間）", "Primvarの値をGprimのどの単位へ対応させるかを決めるMetadataです。"),
    ("Kind", "PrimのModel Hierarchy上の役割を示すMetadataです。"),
    ("Layer（レイヤー）", "シーン記述の一部分を保持するデータの単位です。"),
    ("Layer Stack", "root layerと再帰的なsublayerからなる順序付きのLayer集合です。"),
    ("LIVERPS", "Local、Inherits、Variant Sets、rElocates、References、Payloads、Specializesを強い順に並べた略語です。SublayerのOpinionはLayer Stack内のLocalに含まれます。"),
    ("matrix", "行と列に並んだ数のまとまりです。<code>matrix4d</code>は座標変換に使います。"),
    ("Metadata（メタデータ）", "Prim、Property、Layerに付ける時間変化しない補助情報です。"),
    ("Module（モジュール）", "関連するOpenUSD APIをまとめた単位です。例: Usd、Sdf、Gf。"),
    ("Namespace（名前空間）", "Property名をコロンで区切って階層的にまとめる仕組みです。"),
    ("Path（パス）", "Stage内のPrimやPropertyを指す住所のような識別子です。例: <code>/World/Room</code>。"),
    ("Pivot", "回転と拡縮の中心として使う位置です。対になるinverse operationと組み合わせます。"),
    ("Point", "Meshの頂点の位置です。<code>points</code>に並ぶ座標を指します。"),
    ("Prim（プリム）", "Stageを構成する基本要素。シーングラフ上のノードです。"),
    ("Prim name（Prim名）", "階層内のPrimを識別し、Pathの一部分になる名前です。例: <code>World</code>。"),
    ("Prim Path", "Stage内のPrimを識別するPathです。Prim名を <code>/</code> で区切ります。"),
    ("Primvar", "名前が <code>primvars:</code> で始まり、Interpolation・index・継承を扱えるAttributeです。"),
    ("Primvar Inheritance", "<code>constant</code>のPrimvarがScene Namespaceを下って子のImageable Primへ適用される仕組みです。"),
    ("PrimvarsAPI", "Prim上のPrimvarを作成・取得するためのAPI Schemaです。"),
    ("Property（プロパティ）", "Primが持つ情報。AttributeとRelationshipの2種類があります。"),
    ("Property Path", "Prim Pathの後ろに <code>.</code> とProperty名を続けたPathです。"),
    ("Prototype", "複数のInstanceが共有するシーン構造です。"),
    ("pseudo-root（疑似ルート）", "Stage階層の出発点です。Pathでは <code>/</code> で表します。"),
    ("Relationship（リレーションシップ）", "0個以上のPrim PathまたはProperty Pathを対象として持てる、型のないPropertyです。"),
    ("role", "値が位置・向き・法線・色・テクスチャ座標のどれを表すかという、Value Typeの意味の部分です。"),
    ("Rotate", "軸の周りにPrimの向きを変える変換操作です。複数軸を使うときはRotation Orderも結果へ影響します。"),
    ("scalar", "数が一つだけの値の形です。<code>double</code>や<code>int</code>などが該当します。"),
    ("Scale", "Primの各軸方向の大きさへ倍率を掛ける変換操作です。変更しない倍率は1です。"),
    ("Scene Namespace", "Primの親子関係でできた名前の階層です。Pathで表されます。"),
    ("Schema（スキーマ）", "PrimやPropertyの構造、意味、取得・作成APIを定める設計図です。"),
    ("Scope", "変換を持たず、Primを論理的に整理するconcrete IsA Schemaです。"),
    ("Sdf.ValueTypeNames", "PythonからAttributeのValue Typeを指定するための名前の一覧です。"),
    ("Seam（継ぎ目）", "Faceの境目で値が不連続になる場所です。UVを展開したときの切れ目などを指します。"),
    ("Sparse Authoring（疎な記述）", "同じ情報を必要な最小限の場所にだけ書く考え方です。"),
    ("Stage（ステージ）", "合成されたOpenUSDシーンにアクセスする中心的なオブジェクトです。"),
    ("Subdivision Surface（細分化サーフェス）", "粗い多角形Meshを規則にしたがって細かく分割し、なめらかな形を作る仕組みです。"),
    ("subdivisionScheme", "Meshを細分化するかどうかを決めるAttributeです。<code>none</code>は細分化せず、書いた多角形のまま扱います。"),
    ("Target List", "Relationshipが持つTarget Pathの一覧です。対象が一つのときも一覧として扱われます。"),
    ("Time Code", "単位を持たない時間上の位置です。"),
    ("Time Sample", "特定のTime Codeに記述されたAttribute値です。"),
    ("token", "決まった語を効率よく扱うための文字列型です。選択肢が決まっている場所で使われます。"),
    ("Topology（トポロジー）", "PointとFaceのつながり方です。Primvarに必要な値の個数はこれで決まります。"),
    ("Translate", "PrimをX・Y・Z方向へ移動する変換操作です。通常は<code>xformOp:translate</code>として記述します。"),
    ("uniform", "Faceごとに一つの値を対応させるPrimvar Interpolationです。Attributeの宣言に付く<code>uniform</code>（時間変化しない）とは別の意味です。"),
    ("USD", "UTF-8テキストまたはCrateバイナリを格納できるOpenUSDファイル拡張子です。"),
    ("USDA", "人が読めるUTF-8テキスト形式のOpenUSDファイル表現です。"),
    ("USDC", "ランダムアクセスに対応するバイナリのCrate形式です。"),
    ("USDZ", "複数アセットを一つにまとめる、配布向けの非圧縮ZIPパッケージです。"),
    ("UTF-8", "Unicode文字を表す文字エンコーディングです。USDAは人が読めるUTF-8テキスト形式です。"),
    ("UV", "Surface上の位置をテクスチャ画像の座標へ対応させる値です。<code>faceVarying</code>で持たせることが多い値です。"),
    ("Value Type", "Attributeが保持する値の型です。値の形と、その値が何を意味するか（role）の両方を決めます。"),
    ("varying", "Pointごとに一つの値を対応させ、Surface上を線形に補間するPrimvar Interpolationです。"),
    ("vector", "複数の数をひとまとまりにした値の形です。USDAでは丸括弧で囲みます。"),
    ("vertex", "Pointごとに一つの値を対応させ、Surfaceの基底関数で補間するPrimvar Interpolationです。"),
    ("Xform（エックスフォーム）", "移動、回転、拡大縮小などの変換データを保持し、子Primに適用できるPrim型です。"),
    ("XformCommonAPI", "一般的な移動・回転・拡縮・pivotを共通構成で扱うnon-applied API Schemaです。"),
    ("XformOp", "Xformに記述される移動、回転、拡大縮小など一つの変換操作です。"),
    ("XformOpOrder", "使用するxformOpとtransform stack上の順序を保持するtoken配列です。"),
    ("基底関数（basis function）", "Surface上の位置から値を求めるための重み付けの規則です。"),
    ("線形補間", "2つの値の間を、距離に比例した割合でまっすぐつなぐ補間です。"),
]


def sort_key(term):
    head = term[0]
    ascii_lead = re.match(r"[A-Za-z]", head)
    # Japanese-headed terms go last, after the A-Z run.
    return (0 if ascii_lead else 1, term.lower())


ordered = sorted(TERMS, key=lambda t: sort_key(t[0]))
assert len({t for t, _ in ordered}) == len(ordered), "duplicate term"

rows = "\n".join("      <dt>%s</dt><dd>%s</dd>" % (t, d) for t, d in ordered)

HTML = '''<!doctype html>
<html lang="ja">
<head>
  <meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="color-scheme" content="light dark">
  <title>用語集 — OpenUSD Academy</title>
  <link rel="stylesheet" href="assets/css/style.css"><script src="assets/js/app.js" defer></script>
</head>
<body>
  <header class="site-header"><a class="brand" href="index.html"><span class="brand-mark" aria-hidden="true">O</span><span>OpenUSD Academy</span></a><nav aria-label="メインナビゲーション"><a href="index.html">ホーム</a><a href="curriculum.html">カリキュラム</a></nav><button class="theme-toggle" type="button" data-theme-toggle aria-label="表示テーマを切り替える" aria-pressed="false"><span aria-hidden="true">◐</span><span class="theme-label">テーマ</span></button></header>
  <main class="document">
    <p class="eyebrow">GLOSSARY</p><h1>OpenUSD用語集</h1>
    <p class="lead">以下はAcademyによる初学者向け要約です。各レッスンでは公式資料を参照し、より厳密な意味と出典を示します。アルファベット順に並べ、日本語で始まる語を最後にまとめています。</p>
    <section><h2>用語一覧</h2><dl>
%s
    </dl></section>
    <p><a class="back-link" href="index.html">← ホームへ戻る</a></p>
  </main>
  <footer><p>OpenUSD Academy</p><a href="https://docs.nvidia.com/learn-openusd/latest/index.html">NVIDIA Learn OpenUSD ↗</a></footer>
</body></html>
''' % rows

md_rows = "\n\n".join("### %s\n\n%s" % (t, re.sub(r"</?code>", "`", d)) for t, d in ordered)
MD = '''# OpenUSD Academy 用語集

このファイルはサイト全体の索引です。個々のレッスンにも、その回で使う用語集を必ず付けます。定義はレッスン執筆時に [NVIDIA Learn OpenUSD](https://docs.nvidia.com/learn-openusd/latest/index.html) の公式用語集と該当ページを確認します。正本は `glossary.html` です。

## 用語一覧

%s
''' % md_rows

open(os.path.join(REPO, "glossary.html"), "w", encoding="utf-8").write(HTML)
open(os.path.join(REPO, "glossary.md"), "w", encoding="utf-8").write(MD)
print("%d terms written" % len(ordered))
