# -*- coding: utf-8 -*-
"""Single source for the learning order and the chapter overview pages.

Lesson file names (and therefore lesson numbers) stay fixed so that the cross-links
between pages keep working. What changes is the order a learner walks through them:
the curriculum lists STEPs, every lesson's prev/next nav follows the same order, and
each chapter gets a generated overview page under chapters/.
"""
import os
import re

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def node(title, sub, kind=""):
    cls = " " + kind if kind else ""
    return '<div class="map-node%s"><b>%s</b><span>%s</span></div>' % (cls, title, sub)


def row(*parts):
    return '<div class="map-row">%s</div>' % "".join(parts)


ARROW = '<div class="map-note" aria-hidden="true">→</div>'
DOWN = '<div class="map-note" aria-hidden="true">↓</div>'


def band(text):
    return '<div class="map-band">%s</div>' % text


PLAN = [
    dict(
        title="1. まずUSDAを読む", slug="01-read-usda",
        lead="最初の目標は「書く」ではなく「読める」です。短いテキストを一行ずつ読み解きます。",
        takeaway="USDAはテキスト。読めれば中で何が起きているか分かる",
        map=row(node("Stage", "シーン全体", "is-base"), ARROW,
                node("Prim", "階層のノード"), ARROW,
                node("Property", "Primが持つ情報"), ARROW,
                node("Path", "対象を指す住所", "is-goal"))
            + band("この4語だけで、USDAの構造はひととおり説明できます"),
        outcomes=["短いUSDAを開いて、どこがStageの設定で、どこがPrimの定義かを見分けられる",
                  "波括弧・引用符・インデントが何を表しているかを説明できる",
                  "USDA・USDC・USD・USDZの違いを用途で選べる"],
        items=[
            ("01-reading-usda.html", "Lesson 01", "はじめてのUSDAを読む", "Stage、Prim、Xform、名前、Pathを短いUSDAから一行ずつ読む"),
            ("02-what-is-openusd.html", "Lesson 02", "OpenUSDとは何か", "シーン記述・合成・共同作業の土台を知る"),
            ("03-stage-prim-property.html", "Lesson 03", "Stage・Prim・Property", "全体、構成要素、情報を分ける"),
            ("07-usda-syntax.html", "Lesson 07", "USDAの基本構文", "型・名前・波括弧・Propertyを読む"),
            ("06-usd-file-formats.html", "Lesson 06", "USDA・USDC・USD・USDZ", "中身と用途でファイル形式を選ぶ"),
        ]),
    dict(
        title="2. Propertyを読み書きする", slug="02-properties",
        lead="Primが持つ情報の中身に入ります。値の型と、対象の指し方を押さえます。",
        takeaway="Propertyは値を持つAttributeと、対象を指すRelationshipの2種類",
        map=row(node("Property", "Primが持つ情報", "is-base"))
            + DOWN
            + row(node("Attribute", "値を持つ。型が一つ決まる"), node("Relationship", "0個以上のPathを対象に持つ"))
            + DOWN
            + row(node("Value Type", "形（scalar/vector/array）と意味（role）"),
                  node("Target List", "一つでも複数でも同じ一覧"))
            + band("Schemaに無い情報を足したいときは custom を付けます"),
        outcomes=["AttributeとRelationshipを、書き方から見分けられる",
                  "3つの数が並ぶ型からpoint3f・color3f・normal3fを選び分けられる",
                  "Prim PathとProperty Pathをドットとスラッシュで書き分けられる"],
        items=[
            ("04-attributes-relationships.html", "Lesson 04", "AttributeとRelationship", "値とつながりを読み分ける"),
            ("22-value-types.html", "Lesson 22", "AttributeのValue Type", "scalar、vector、matrix、arrayとrole"),
            ("05-prim-property-paths.html", "Lesson 05", "Prim PathとProperty Path", "Stage内の対象を正確に指す"),
            ("25-relationship-target.html", "Lesson 25", "Relationship Target", "一つと複数の対象を同じ仕組みで書く"),
            ("26-custom-properties.html", "Lesson 26", "Custom Properties", "Schema外の情報を追加する"),
        ]),
    dict(
        title="3. Pythonから触る", slug="03-python",
        lead="ここで初めてコードを書きます。USDAで読めるようになった構造を、そのままAPIで作ります。",
        takeaway="USDAで読めるものは、そのままAPIで書ける",
        map=row(node("Usd", "Stage・Prim・Property"), node("Sdf", "Path・型・Layer"),
                node("Gf", "ベクトルと行列"), node("UsdGeom", "形とXform"))
            + DOWN
            + row(node("USDAの一行 ↔ APIの一行", "対応が付けば、どちらからでも書ける", "is-goal")),
        outcomes=["どのモジュールに何があるかを見当付けられる",
                  "USDAの一行に対応するPython APIを選べる",
                  "MetadataとSchemaの役割の違いを説明できる"],
        items=[
            ("08-python-pxr-modules.html", "Lesson 08", "Pythonとpxrモジュール", "Usd・Sdf・Gf・UsdGeomを使い分ける"),
            ("09-metadata-schemas.html", "Lesson 09", "MetadataとSchema", "補助情報とデータの設計図を分ける"),
        ("09b-schema-kinds.html", "Lesson 09B", "Schemaの種類", "Typed/APIの2系統と、concrete・abstract・applied・non-applied"),
        ]),
    dict(
        title="4. 形を置いて動かす", slug="04-transforms",
        lead="階層と変換です。ここまでで、自分でシーンを組み立てられるようになります。",
        takeaway="親の変換は子へ積み重なり、書いた順番で結果が変わる",
        map=row(node("Scope", "変換を持たない整理用"), node("Xform", "変換を持ち、子へ伝える", "is-base"))
            + DOWN
            + row(node("translate", "位置"), node("rotate", "向き"),
                  node("scale", "大きさ"), node("pivot", "回転と拡縮の中心"))
            + DOWN
            + row(node("xformOpOrder", "並べた順に適用される。順番で結果が変わる", "is-goal"))
            + band("XformCommonAPIを使うと、この4つを決まった構成でまとめて扱えます"),
        outcomes=["整理だけしたい場所にScope、動かしたい場所にXformを選べる",
                  "translate・rotate・scale・pivotをUSDAとPythonの両方で書ける",
                  "xformOpOrderを読んで、変換が適用される順番を追える"],
        items=[
            ("15-scope.html", "Lesson 15", "Scope", "変換を持たず、Primを用途ごとに整理する"),
            ("10-xform-hierarchy.html", "Lesson 10", "Xformと階層", "親の変換が子へ届く仕組みを知る"),
            ("16-xform-common-api.html", "Lesson 16", "XformCommonAPI", "一般的な変換を交換しやすい構成で扱う"),
            ("17a-translate.html", "Lesson 17A", "Translate", "位置を三つの軸で記述する"),
            ("17b-rotate.html", "Lesson 17B", "Rotate", "回転角とRotation Orderを読む"),
            ("17c-scale.html", "Lesson 17C", "Scale", "各軸の倍率を記述する"),
            ("17d-pivot.html", "Lesson 17D", "Pivot", "回転と拡縮の中心を決める"),
            ("18-xform-op-order.html", "Lesson 18", "XformOpOrder", "変換順序で結果が変わる理由"),
        ]),
    dict(
        title="5. Meshの形と、その上へ値を配る", slug="05-primvars",
        lead="まずMeshの形そのものを読み書きし、そこで数えた個数のままPrimvarへ進みます。",
        takeaway="形の3つの数（Point・Face・Face Vertex）が、そのままPrimvarの個数になる",
        map=row(node("points", "点の一覧", "is-base"), node("faceVertexIndices", "使う点の番号"),
                node("faceVertexCounts", "何角形かの並び"))
            + DOWN
            + row(node("Point数", "= pointsの要素数"), node("Face数", "= countsの要素数"),
                  node("Face Vertex数", "= countsの合計"))
            + DOWN
            + row(node("constant", "1個 — Prim全体"), node("uniform", "Face数"),
                  node("vertex / varying", "Point数"), node("faceVarying", "Face Vertex数", "is-goal"))
            + DOWN
            + row(node("indices", "値を使い回して短くする"), node("継承", "constantだけが子へ降りる"))
            + band("同じ板（Face 2枚・Point 6個・Face Vertex 8個）で、全部を実際に描画して見比べます"),
        outcomes=["Meshの形を3つの配列から読み取り、Point・Face・Face Vertexを数えられる",
                  "subdivisionSchemeやorientationの書き忘れが何を招くか説明できる",
                  "interpolationごとに、値をいくつ書けばよいか数えられる",
                  "Faceの境目で色を切り替えたいときにfaceVaryingを選べる",
                  "同じ値の繰り返しをindicesで短くできる"],
        items=[
            ("35-mesh-topology.html", "Lesson 35", "Meshのトポロジ", "points・faceVertexCounts・faceVertexIndicesで形を作る"),
            ("36-mesh-attributes.html", "Lesson 36", "Meshの見え方を決めるAttribute", "subdivisionScheme・orientation・doubleSided・extent"),
            ("23-primvars.html", "Lesson 23", "Primvars", "Attributeとの違いと三つの機能"),
            ("24a-constant.html", "Lesson 24A", "constant interpolation", "Prim全体へ一つの値"),
            ("24b-uniform.html", "Lesson 24B", "uniform interpolation", "Faceごとに一つの値"),
            ("24c-vertex.html", "Lesson 24C", "vertex interpolation", "Pointごとに一つの値"),
            ("24d-varying.html", "Lesson 24D", "varying interpolation", "Pointごとの値を線形補間する"),
            ("24e-face-varying.html", "Lesson 24E", "faceVarying interpolation", "Face Vertexごとに一つの値"),
            ("24f-indexed-primvars.html", "Lesson 24F", "Indexed Primvars", "値とindexを分けて再利用する"),
            ("24g-primvar-inheritance.html", "Lesson 24G", "Primvar Inheritance", "constant Primvarを階層へ適用する"),
        ]),
    dict(
        title="6. 見た目を記述する", slug="06-shading",
        lead="形ができたので、次はその見え方です。MaterialとShaderの組み立て方、形との結び付け方、そして光を扱います。",
        takeaway="Materialは外向きの窓口、Shaderが中身。形からはRelationshipで結ぶ",
        map=row(node("Gprim", "形の側", "is-base"), ARROW,
                node("material:binding", "Relationshipで指す"), ARROW,
                node("Material", "窓口。outputs:surface"), ARROW,
                node("Shader", "中身。info:idと接続", "is-goal"))
            + DOWN
            + row(node("UsdPreviewSurface", "どこでも同じに解釈される標準Shader"),
                  node("primvars:st", "第5章で書いたUVがここで効く"))
            + DOWN
            + row(node("Light型", "DistantLight・SphereLightなど。光の形"),
                  node("LightAPI", "intensity・colorなど、型に共通の設定", "is-goal"))
            + band("bindingは子孫へ受け継がれます。祖先に一度書けば、下の形すべてに届きます"),
        outcomes=["MaterialとShaderの役割の違いを説明できる",
                  "outputs:surface.connectで両者をつなげる",
                  "UsdPreviewSurfaceの主な入力を選んで質感を作れる",
                  "material:bindingの継承と強さの規則を読み解ける",
                  "Light型とLightAPIを見分け、光の明るさと向きを記述できる"],
        items=[
            ("46-usdshade-basics.html", "Lesson 46", "UsdShadeの基礎", "MaterialとShaderを接続で組み立てる"),
            ("50-material-binding.html", "Lesson 50", "Material Binding", "形とMaterialを結び、子孫へ受け継がせる"),
            ("37-lights.html", "Lesson 37", "Lights", "UsdLuxのLight型とLightAPIで光を記述する"),
        ]),
    dict(
        title="7. 時間を記述する", slug="07-time",
        lead="値が時間で変わる書き方です。Compositionへ進む前に済ませておきます。",
        takeaway="defaultは時間に依存しない値、Time Sampleは時点ごとの値",
        map=row(node("default", "時間に依存しない一つの値", "is-base"), ARROW,
                node("timeSamples", "時点と値の組を並べる", "is-goal"))
            + band("両方あるときは Time Sample が優先されます"),
        outcomes=["timeSamplesの書き方を読める",
                  "defaultとTime Sampleのどちらが使われるか判断できる",
                  "Time Codeが単位を持たない数だと説明できる"],
        items=[
            ("11-time-codes-samples.html", "Lesson 11", "Time CodeとTime Sample", "時点と値で時間変化を記述する"),
        ]),
    dict(
        title="8. Prim Specの3つの書き方", slug="08-specifiers",
        lead="Compositionの前に、def・over・classの違いをここで確実にします。これがないと合成の説明が読めません。",
        takeaway="描画されない理由は3つあり、それぞれ別の仕組み",
        map=row(node("def", "定義する。Stageに現れる", "is-goal"),
                node("over", "意見だけ重ねる。defが無ければ現れない"),
                node("class", "abstract。自分は現れず、他へ配る"))
            + DOWN
            + row(node("IsDefined()", "def があるか"), node("IsAbstract()", "class か"),
                  node("IsActive()", "外されていないか"))
            + band("「見えない」と思ったとき、どれが原因かをこの3つで切り分けます"),
        outcomes=["def・over・classを目的で選べる",
                  "上書きが効かないときにPathの不一致を疑える",
                  "classとInheritsを組み合わせて共通の設定を配れる"],
        items=[
            ("27a-def.html", "Lesson 27A", "def", "Primを定義する"),
            ("27b-over.html", "Lesson 27B", "over", "既存PrimへOpinionだけを重ねる"),
            ("27c-class.html", "Lesson 27C", "class", "Inherits用の抽象Prim Specを作る"),
        ]),
    dict(
        title="9. コンポジション", slug="09-composition",
        lead="OpenUSDでいちばん難しい部分です。ここまでの土台があって初めて読み進められます。",
        takeaway="複数のLayerの意見を、決まった強さの順で一つに畳む",
        map=row(node("L", "Local"), node("I", "Inherits"), node("V", "Variant Sets"),
                node("E", "rElocates"), node("R", "References"),
                node("P", "Payloads"), node("S", "Specializes"))
            + DOWN
            + row(node("強い ← LIVERPS → 弱い", "左ほど強い。先に書いたものが勝つ", "is-base"))
            + DOWN
            + row(node("Value Resolution", "合成後のPropertyから最終値を一つ選ぶ", "is-goal")),
        outcomes=["LIVERPSの並びが強さの順だと説明できる",
                  "Sublayerで下のファイルを書き換えずに上書きできる",
                  "思った値にならないとき、どのArcが勝っているか見当を付けられる"],
        items=[
            ("12-composition.html", "Lesson 12", "コンポジションとLIVERPS", "強度順序、SublayerとLocalの関係、Opinionの上書き"),
            ("12-sublayers.html", "Lesson 12A", "SublayerとLayer Stack", "同じnamespaceを積み、Local内の強弱を追う"),
            ("12-local.html", "Lesson 12B", "L · Local Opinion", "利用側の直接Opinionで上書きする"),
            ("12-inherits.html", "Lesson 12C", "I · Inherits", "クラスの変更をbroadcastする"),
            ("12-variants.html", "Lesson 12D", "V · Variant Sets", "名前付き選択肢を合成する"),
            ("12-relocates.html", "Lesson 12E", "E · rElocates", "namespace上のPathを移し替える"),
            ("12-references.html", "Lesson 12F", "R · References", "階層の接ぎ木とPath変換を追う"),
            ("12-payloads.html", "Lesson 12G", "P · Payloads", "Load可能な内容を合成する"),
            ("12-specializes.html", "Lesson 12H", "S · Specializes", "最も弱いfallbackを共有する"),
            ("21-value-resolution.html", "Lesson 21", "Value Resolution", "Composition後のPropertyから最終値を選ぶ"),
        ]),
    dict(
        title="10. ファイル先頭の宣言と入口", slug="10-stage-metadata",
        lead="第1章から毎回出てきた「ファイル先頭の丸括弧」を、ここで回収します。単位を直すにはscale、上方向を直すにはrotate、入口を語るにはReferenceが要るので、この位置に置いています。",
        takeaway="先頭の丸括弧は宣言であって、自動変換はしない",
        map=row(node("defaultPrim", "外から入る入口"), node("metersPerUnit", "長さの「1」"),
                node("upAxis", "どの軸が上か"), node("kilogramsPerUnit", "質量の「1」"))
            + DOWN
            + row(node("読む側が解釈する", "書いてあることが前提。欠けると usdchecker がエラーにする", "is-goal"))
            + band("どれも「そう決めた」と書くだけ。実際に合わせるのは読み込む側の仕事です"),
        outcomes=["ファイル先頭の丸括弧がLayer Metadataの場所だと分かる",
                  "単位や上方向が食い違うアセットを、scaleやrotateで補正できる",
                  "usdcheckerがこの3つの欠落を報告する理由を説明できる"],
        items=[
            ("09a-default-prim.html", "Lesson 09A", "Default Prim", "Layerを外から利用するときの入口を決める"),
            ("20a-meters-per-unit.html", "Lesson 20A", "metersPerUnit", "長さの「1」が何メートルかを宣言する"),
            ("20b-up-axis.html", "Lesson 20B", "upAxis", "どの軸が上かを宣言する"),
            ("20c-kilograms-per-unit.html", "Lesson 20C", "kilogramsPerUnit", "質量の「1」が何キログラムかを宣言する"),
        ]),
    dict(
        title="11. Compositionを組み立てる", slug="11-composition-practice",
        lead="合成の仕組みが分かったところで、実際の組み立て方と、原因を追う道具へ進みます。",
        takeaway="合成の結果を疑う前に、寄与している記述の一覧を見る",
        map=row(node("組み立てる", "Arcの張り方・一覧の編集・境界の守り方", "is-base"), ARROW,
                node("調べる", "Prim StackとProperty Stackで出どころを追う", "is-goal"))
            + DOWN
            + row(node("prepend", "先頭へ足す"), node("append", "末尾へ足す"),
                  node("delete", "取り除く"), node("reorder", "並べ替える"))
            + band("キーワードを付けずに書くと一覧を丸ごと置き換えます。共同作業では避けます"),
        outcomes=["一覧を壊さずに項目を足したり消したりできる",
                  "Internal ArcとExternal Arcを書き分けられる",
                  "値の出どころをProperty Stackの1行目で特定できる"],
        items=[
            ("28-prim-composition.html", "Lesson 28", "Prim Composition", "複数のPrim Specが一つになる"),
            ("29-internal-external-arc.html", "Lesson 29", "Internal ArcとExternal Arc", "同じLayer内と別ファイル"),
            ("30-list-editing.html", "Lesson 30", "List Editing", "prepend・append・delete・reorder"),
            ("31-encapsulation.html", "Lesson 31", "Encapsulation", "Assetの境界を守る"),
            ("32-variant-edit-context.html", "Lesson 32", "Variant Edit Context", "選択肢の中へ書く"),
            ("33-direct-ancestral-arc.html", "Lesson 33", "Direct ArcとAncestral Arc", "同じArc内の強度を追う"),
            ("34a-prim-stack.html", "Lesson 34A", "Prim Stack", "Primへ寄与するPrim Specを調べる"),
            ("34b-property-stack.html", "Lesson 34B", "Property Stack", "Propertyへ寄与するSpecを調べる"),
        ]),
    dict(
        title="12. モデル階層とアセット設計", slug="12-model-hierarchy",
        lead="Kindでシーンに役割を与え、再利用できるアセットの形にまとめます。",
        takeaway="Prim型は「何であるか」、Kindは「どういう役割か」",
        map=row(node("assembly", "公開できるまとまり", "is-base"), ARROW,
                node("group", "Modelをまとめる階層"), ARROW,
                node("component", "再利用の最小単位", "is-goal"), ARROW,
                node("subcomponent", "component内部の目印"))
            + band("上から下へ切れ目なく続くことがModel Hierarchyの条件です"),
        outcomes=["Schema型とKindを混同せずに説明できる",
                  "componentを境界として、参照される単位を設計できる",
                  "Model Hierarchyが途切れる書き方を避けられる"],
        items=[
            ("19a-kind.html", "Lesson 19A", "Kind", "Schema型とModel Hierarchy上の役割を分ける"),
            ("19b-component.html", "Lesson 19B", "component", "再利用可能なleaf modelを作る"),
            ("19c-group.html", "Lesson 19C", "group", "Modelを正しい祖先階層へまとめる"),
            ("19d-assembly.html", "Lesson 19D", "assembly", "公開可能なaggregate Assetを作る"),
            ("19e-subcomponent.html", "Lesson 19E", "subcomponent", "component内部の重要なPrimを示す"),
            ("13-asset-structure.html", "Lesson 13", "再利用できるアセット設計", "Asset Structure、Model Kind、Asset Interface、Reference/Payload Pattern"),
        ]),
    dict(
        title="13. Stageを調べて制御する", slug="13-stage-control",
        lead="大きなシーンを扱うための、読み込みと走査の制御です。",
        takeaway="見えない理由を切り分け、必要な部分だけを読む",
        map=row(node("active = false", "構成から外す。ファイルに書く"),
                node("Unload", "Payloadを開かない。実行時に決める"))
            + DOWN
            + row(node("Traverse()", "既定の条件で回る"), node("TraverseAll()", "条件を外して全部見る"),
                  node("Predicate", "枝ごと切り落とす条件", "is-goal"))
            + band("Predicateはフィルタではなく枝刈りです。ここを取り違えると結果が空になります"),
        outcomes=["削除・非表示・Inactiveを目的で選び分けられる",
                  "Payloadを開かずにシーンの骨格だけを読める",
                  "Traversal Predicateが枝刈りだと理解して使える"],
        items=[
            ("41-active-inactive.html", "Lesson 41", "ActiveとInactive", "Compositionから除外する"),
            ("42-load-unload.html", "Lesson 42", "LoadとUnload", "Payloadを制御する"),
            ("43-stage-traversal.html", "Lesson 43", "Stage Traversal", "Primを順番に調べる"),
            ("44-traversal-predicate.html", "Lesson 44", "Traversal Predicate", "調べるPrimを絞る"),
            ("45-hydra.html", "Lesson 45", "Hydra", "Scene Indexとレンダリングの入口"),
        ]),
    dict(
        title="14. パイプラインとData Exchange", slug="14-pipeline",
        lead="他のツールとの間でデータを受け渡す実務です。ここからは設計の話が増えます。",
        takeaway="外から見える面と、中の作り方を分ける",
        map=row(node("Entry Point", "参照される入口", "is-base"), ARROW,
                node("Interface", "外から使う情報だけ見せる"), ARROW,
                node("Contents", "重い中身はPayloadの奥へ"))
            + DOWN
            + row(node("入力", "他ツールの形式"), ARROW, node("変換", "Geometry・Material"),
                  ARROW, node("検証", "usdcheckerと自前の規則", "is-goal"))
            + DOWN
            + row(node("Material", "窓口。outputs:surface"), ARROW, node("Shader", "中身。info:idと接続"),
                  ARROW, node("material:binding", "形と結び、子孫へ受け継がれる"))
            + band("入口を固定しておくと、中身を作り直しても下流が壊れません"),
        outcomes=["Assetの入口と中身を分けて設計できる",
                  "作業ごとにLayerを分けて衝突を避けられる",
                  "変換結果を自動で検証する仕組みを書ける"],
        items=[
            ("14-data-pipelines.html", "Lesson 14", "データを運ぶパイプライン", "データ交換、抽出、変換、検証、Instancing"),
            ("47-asset-entry-point.html", "Lesson 47", "Asset Entry Point", "参照される入口を作る"),
            ("48-asset-interface.html", "Lesson 48", "Asset Interface", "公開する情報を選ぶ"),
            ("49-workstream-layers.html", "Lesson 49", "Workstream Layers", "作業をLayerで分ける"),
            ("51-asset-parameterization.html", "Lesson 51", "Asset Parameterization", "下流から変更できる値"),
            ("52-reference-payload-pattern.html", "Lesson 52", "Reference/Payload Pattern", "InterfaceとContentsを分ける"),
            ("53-lofting.html", "Lesson 53", "Lofting", "Payloadを開かず重要情報を見せる"),
            ("54-converter-structure.html", "Lesson 54", "Converterの構造", "入力・変換・出力を分ける"),
            ("55-geometry-extraction.html", "Lesson 55", "Geometry Extraction", "点・法線・UVを対応させる"),
            ("56-material-extraction.html", "Lesson 56", "Material Extraction", "MaterialとBindingを対応させる"),
            ("57-asset-validation.html", "Lesson 57", "Asset Validation", "規則をコードにする"),
            ("58-prim-hierarchy-transformation.html", "Lesson 58", "Prim Hierarchy Transformation", "階層を目的形へ変える"),
            ("59-export-options.html", "Lesson 59", "Export Options", "変換条件を利用者へ公開する"),
        ]),
    dict(
        title="15. Instancingと大規模シーン", slug="15-instancing",
        lead="同じものを大量に置くための仕組みです。数が増えたときに効いてきます。",
        takeaway="同じ中身は一つだけ持ち、置き方だけを増やす",
        map=row(node("そのまま並べる", "数だけPrimが増える", "is-base"), ARROW,
                node("Scenegraph Instancing", "Prototypeを共有する"), ARROW,
                node("Point Instancing", "位置の配列だけで置く", "is-goal"))
            + band("個別に差を付けたいか、とにかく軽くしたいかで選び分けます"),
        outcomes=["Instanceの中身が共有されることを説明できる",
                  "Scenegraph InstancingとPoint Instancingを用途で選べる",
                  "Instanceごとに差を付けたいときの手段が分かる"],
        items=[
            ("60-asset-modularity.html", "Lesson 60", "Asset Modularity", "再利用単位を決める"),
            ("61-scenegraph-instancing.html", "Lesson 61", "Scenegraph Instancing", "CompositionからPrototypeを作る"),
            ("62-nested-instancing.html", "Lesson 62", "Nested Instancing", "Instanceを階層化する"),
            ("63-instance-refinement.html", "Lesson 63", "Instance Refinement", "Instanceごとの差を付ける"),
            ("38-hierarchical-refinement.html", "Lesson 38", "Hierarchical RefinementとAd Hoc Arc", "Prototypeを増やす書き方と増やさない書き方"),
            ("39-broadcasted-refinement.html", "Lesson 39", "Broadcasted Refinement", "下流の1か所で対象の全Instanceを変える"),
            ("64-point-instancing.html", "Lesson 64", "Point Instancing", "大量の単純要素を配置する"),
            ("40-point-instance-refinement.html", "Lesson 40", "Point Instanceに差を付ける", "Primvar・Prototype追加・Promotion"),
            ("65-instancing-choice.html", "Lesson 65", "ScenegraphとPointの選択", "用途と制約を比較する"),
        ]),
    dict(
        title="16. 調査・検証・総復習", slug="16-debugging",
        lead="最後に、壊れたシーンを自分で直せるところまで進みます。",
        takeaway="推測せずに、道具で出どころを突き止める",
        map=row(node("症状", "見えない・色が違う・開けない", "is-base"), ARROW,
                node("道具", "usdview / usdtree / usdcat / Stack / Validation"), ARROW,
                node("原因", "どのファイルのどの行か", "is-goal"))
            + DOWN
            + row(node("総合演習", "小さなAssetを作り、Sceneへ組み上げる"))
            + band("ここまでのレッスンで出てきた道具を、症状から逆引きできる形に整理します"),
        outcomes=["usdviewの各区画が何を見せているか説明できる",
                  "症状から使うべき道具を選べる",
                  "壊れたReferenceやPathを自力で直せる",
                  "小さなAssetとSceneを最初から組み立てられる"],
        items=[
            ("73-usdview.html", "Lesson 73", "usdviewで目で確かめる", "階層・描画・Property・合成を一つの画面で見る"),
            ("66-inspect-stage.html", "Lesson 66", "usdrecordとusdtreeでStageを読む", "構造と描画を確かめる"),
            ("67-inspect-layer-stack.html", "Lesson 67", "Layer Stackを調べる", "どのLayerの意見が効いているか"),
            ("68-fix-broken-references.html", "Lesson 68", "壊れたReferenceとPathを直す", "よくある破損の直し方"),
            ("69-minimal-validation.html", "Lesson 69", "Pythonで最小Validationを書く", "規則を自動で確かめる"),
            ("70-build-an-asset.html", "Lesson 70", "小さなAssetを最初から組み立てる", "総合演習1"),
            ("71-build-a-scene.html", "Lesson 71", "複数Assetから小さなSceneを作る", "総合演習2"),
            ("72-review.html", "Lesson 72", "OpenUSD教材の総復習", "全体を振り返る"),
        ]),
]

HEAD = ('<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">'
        '<meta name="color-scheme" content="light dark">')
THEME = ('<button class="theme-toggle" type="button" data-theme-toggle aria-label="表示テーマを切り替える" '
         'aria-pressed="false"><span aria-hidden="true">◐</span><span class="theme-label">テーマ</span></button>')


def exists(fn):
    return os.path.exists(os.path.join(REPO, "lessons", fn))


def written_sequence():
    seq = []
    for ch in PLAN:
        for fn, label, title, _d in ch["items"]:
            if fn and exists(fn):
                seq.append((fn, label, title, ch))
    return seq


def rewrite_navs():
    seq = written_sequence()
    changed = 0
    for i, (fn, _label, _title, chapter) in enumerate(seq):
        path = os.path.join(REPO, "lessons", fn)
        text = open(path, encoding="utf-8").read()
        _r, steps_by_file, _t = step_numbers()
        parts = []
        if i > 0:
            parts.append('<a href="%s">← STEP %02d</a>' % (seq[i - 1][0], steps_by_file[seq[i - 1][0]]))
        else:
            parts.append('<a href="../curriculum.html">← カリキュラム</a>')
        parts.append('<a class="nav-chapter" href="../chapters/%s.html">%s</a>'
                     % (chapter["slug"], chapter["title"]))
        if i < len(seq) - 1:
            parts.append('<a href="%s">STEP %02d →</a>' % (seq[i + 1][0], steps_by_file[seq[i + 1][0]]))
        else:
            parts.append('<a href="../curriculum.html">全カリキュラムへ →</a>')
        nav = '<nav class="lesson-footer-nav">%s</nav>' % "".join(parts)
        # 古いテンプレートは <nav class="lesson-footer-nav" aria-label="..."> と
        # 属性が付いている。属性を許さない正規表現だと20ページが書き換え対象から
        # 漏れ、前後リンクが古い順序のまま公開されていた。
        new = re.sub(r'<nav class="lesson-footer-nav"[^>]*>.*?</nav>', nav, text, flags=re.S)
        if new != text:
            open(path, "w", encoding="utf-8").write(new)
            changed += 1
    return len(seq), changed


def step_numbers():
    """Return {chapter index: (first step, last step)} and {file: step}."""
    ranges, steps, n = {}, {}, 0
    for ci, ch in enumerate(PLAN):
        first = n + 1
        for fn, _l, _t, _d in ch["items"]:
            n += 1
            if fn:
                steps[fn] = n
        ranges[ci] = (first, n)
    return ranges, steps, n


def write_chapter_pages():
    ranges, _steps, _total = step_numbers()
    os.makedirs(os.path.join(REPO, "chapters"), exist_ok=True)
    step = 0
    for ci, ch in enumerate(PLAN):
        lis = []
        for fn, label, title, desc in ch["items"]:
            step += 1
            if fn and exists(fn):
                lis.append('<li><a href="../lessons/%s"><strong>STEP %02d: %s</strong>'
                           '<span>%s</span></a></li>' % (fn, step, title, desc))
            else:
                lis.append('<li><span class="planned"><strong>STEP %02d: %s（予定）</strong>'
                           '<span>%s</span></span></li>' % (step, title, desc))
        outcomes = "".join("<li>%s</li>" % o for o in ch["outcomes"])
        first, last = ranges[ci]
        number = ch["title"].split(".")[0]
        heading = ch["title"].split(". ", 1)[1]

        prev_ch = PLAN[ci - 1] if ci > 0 else None
        next_ch = PLAN[ci + 1] if ci < len(PLAN) - 1 else None
        nav = []
        nav.append('<a href="%s.html">← %s</a>' % (prev_ch["slug"], prev_ch["title"])
                   if prev_ch else '<a href="../curriculum.html">← カリキュラム</a>')
        nav.append('<a href="%s.html">%s →</a>' % (next_ch["slug"], next_ch["title"])
                   if next_ch else '<a href="../curriculum.html">全カリキュラムへ →</a>')

        prereq = ""
        if prev_ch:
            prereq = ('<section class="lesson-section"><p class="section-kicker">前提</p>'
                      '<h2>この章の前に読んでおくところ</h2>'
                      '<a class="chapter-card" href="%s.html"><p class="eyebrow">前の章</p>'
                      '<strong>%s</strong><span>%s</span></a></section>'
                      % (prev_ch["slug"], prev_ch["title"], prev_ch["lead"]))

        html = '''<!doctype html><html lang="ja"><head>%s<title>%s — OpenUSD Academy</title><link rel="stylesheet" href="../assets/css/style.css"><script src="../assets/js/app.js" defer></script></head><body>
<header class="site-header"><a class="brand" href="../index.html"><span class="brand-mark" aria-hidden="true">O</span><span>OpenUSD Academy</span></a><nav aria-label="メインナビゲーション"><a href="../index.html">ホーム</a><a href="../curriculum.html">カリキュラム</a><a href="../glossary.html">用語集</a></nav>%s</header>
<main class="lesson"><header class="lesson-hero"><p class="eyebrow">CHAPTER %s · STEP %02d–%02d</p><h1>%s</h1><p class="lesson-lead">%s</p></header>
<section class="lesson-section takeaway"><p class="section-kicker">この章のねらい</p><h2>%s</h2></section>
<section class="lesson-section"><p class="section-kicker">全体像</p><h2>この章で扱うものの関係</h2><figure class="chapter-map">%s<figcaption>OpenUSD Academyによる第%s章の全体図</figcaption></figure></section>
<section class="lesson-section"><p class="section-kicker">この章を終えたら</p><h2>できるようになること</h2><ol class="outcome-list">%s</ol></section>
<section class="lesson-section"><p class="section-kicker">この章のSTEP</p><h2>上から順に進めます</h2><ol class="lesson-index">%s</ol></section>
%s
<nav class="lesson-footer-nav">%s</nav></main><footer><p>OpenUSD Academy · 第%s章</p><a href="../curriculum.html">カリキュラム</a></footer></body></html>
''' % (HEAD, ch["title"], THEME, number, first, last, heading, ch["lead"], ch["takeaway"],
       ch["map"], number, outcomes, "".join(lis), prereq, "".join(nav), number)
        open(os.path.join(REPO, "chapters", ch["slug"] + ".html"), "w", encoding="utf-8").write(html)
    return len(PLAN)


def render_curriculum():
    step = 0
    html_sections, md_sections = [], []
    for ch in PLAN:
        lis, md_lines = [], []
        for fn, label, title, desc in ch["items"]:
            step += 1
            if fn and exists(fn):
                lis.append('<li><a href="lessons/%s"><strong>STEP %02d: %s</strong>'
                           '<span>%s</span></a></li>' % (fn, step, title, desc))
                md_lines.append("- **STEP %02d:** [%s](lessons/%s) — %s"
                                % (step, title, fn, desc))
            else:
                lis.append('<li><span class="planned"><strong>STEP %02d: %s（予定）</strong>'
                           '<span>%s</span></span></li>' % (step, title, desc))
                md_lines.append("- **STEP %02d（予定）:** %s — %s" % (step, title, desc))
        html_sections.append(
            '<section><h2><a href="chapters/%s.html">%s</a></h2><p class="chapter-lead">%s</p>'
            '<ol class="lesson-index">%s</ol></section>'
            % (ch["slug"], ch["title"], ch["lead"], "".join(lis)))
        md_sections.append("## [%s](chapters/%s.html)\n\n%s\n\n%s"
                           % (ch["title"], ch["slug"], ch["lead"], "\n".join(md_lines)))

    intro_md = ("このカリキュラムは、[OpenUSD公式ドキュメント](https://openusd.org/release/index.html) を技術上の一次情報とし、"
                "[NVIDIA Learn OpenUSD](https://docs.nvidia.com/learn-openusd/latest/index.html) を主要な学習資料として照合したうえで、"
                "日本語の初学者が段階的に進めるようAcademy独自に整理した計画です（確認日: 2026-08-06）。")
    # HTML側ではMarkdownのリンク記法をアンカーへ変換する
    intro = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', intro_md)
    note = ("**STEP番号のとおりに上から進めてください。** 各ページの前後リンクも同じ並びなので、"
            "順にたどるだけで迷いません。章の見出しをたどると、その章の全体像をまとめたページへ移動します。"
            "初学者がつまずきにくい順序を優先しているため、公式資料の章立てとは並びが異なります。")

    html = '''<!doctype html>
<html lang="ja">
<head>
  %s
  <title>カリキュラム — OpenUSD Academy</title>
  <link rel="stylesheet" href="assets/css/style.css"><script src="assets/js/app.js" defer></script>
</head>
<body>
  <header class="site-header"><a class="brand" href="index.html"><span class="brand-mark" aria-hidden="true">O</span><span>OpenUSD Academy</span></a><nav aria-label="メインナビゲーション"><a href="index.html">ホーム</a><a href="glossary.html">用語集</a></nav>%s</header>
  <main class="document">
    <p class="eyebrow">CURRICULUM</p><h1>OpenUSD Academy カリキュラム</h1>
    <p class="lead">%s</p>
    <aside class="academy-note"><p class="source-label">読み方</p><p>%s</p></aside>
%s
    <p><a class="back-link" href="index.html">← ホームへ戻る</a></p>
  </main>
  <footer><p>OpenUSD Academy</p><a href="https://docs.nvidia.com/learn-openusd/latest/index.html">NVIDIA Learn OpenUSD ↗</a></footer>
</body></html>
''' % (HEAD, THEME, intro, note.replace("**", ""), "\n    ".join(html_sections))

    md = ("# OpenUSD Academy カリキュラム\n\n%s\n\n> %s\n\n%s\n\n"
          "> **Academy方針:** 各レッスンは現在と同程度の長さと難易度に保ち、一回に一つの中心概念を扱います。"
          "公式の概念を改変せず、図解・USDA/Python対訳・日本語でのつまずき対策を加えます。\n"
          % (intro_md, note, "\n\n".join(md_sections)))

    open(os.path.join(REPO, "curriculum.html"), "w", encoding="utf-8").write(html)
    open(os.path.join(REPO, "curriculum.md"), "w", encoding="utf-8").write(md)
    return step


def normalize_labels():
    """Replace every "Lesson NN" label with the current "STEP NN".

    The learner only ever sees STEP numbers. Lesson numbers stay as file names.
    Linked references derive their STEP from the href, so this stays correct when
    the order changes; plain-text mentions use the label map.
    """
    _ranges, steps_by_file, _total = step_numbers()
    label_step, n = {}, 0
    for ch in PLAN:
        for fn, label, _t, _d in ch["items"]:
            n += 1
            label_step[label] = n
    # longest labels first so "Lesson 12A" is not eaten by "Lesson 12"
    labels = sorted(label_step, key=len, reverse=True)

    changed = 0
    for sub in ("lessons", "chapters"):
        folder = os.path.join(REPO, sub)
        if not os.path.isdir(folder):
            continue
        for name in sorted(os.listdir(folder)):
            if not name.endswith(".html"):
                continue
            path = os.path.join(folder, name)
            text = original = open(path, encoding="utf-8").read()

            # フッターナビは rewrite_navs() が丸ごと書き直す。ここで触ると
            # "← STEP 14" の矢印を残したまま前置してしまい、
            # "STEP 72 ← STEP 66" のような表示になる。除外して往復を断つ。
            nav_m = re.search(r'<nav class="lesson-footer-nav"[^>]*>.*?</nav>', text, flags=re.S)
            nav_src = nav_m.group(0) if nav_m else None
            if nav_src:
                text = text.replace(nav_src, "\x00NAV\x00")

            # 1. links to other lessons -> STEP derived from the href
            def relabel(m):
                href, inner = m.group(1), m.group(2)
                target = steps_by_file.get(os.path.basename(href))
                if target is None:
                    return m.group(0)
                rest = re.sub(r"^(?:Lesson\s+[0-9]+[A-Z]?|STEP\s+[0-9]+)\s*", "", inner)
                label = "STEP %02d" % target
                return '<a href="%s">%s</a>' % (href, (label + " " + rest).strip() if rest else label)

            # リンク文字列にタグ（<code> など）が入る場合もあるので [^<]* では拾えない。
            text = re.sub(r'<a href="((?:\.\./lessons/)?[0-9][^"]*\.html)">(.*?)</a>',
                          relabel, text, flags=re.S)

            # 2. this page's own labels
            #    LESSON と STEP の両方を拾う。そうしないと一度変換した後に
            #    番号がずれても二度と直らない（実際にこれで41ページがずれた）。
            own = steps_by_file.get(name)
            if own:
                text = re.sub(r'(<p class="eyebrow">)(?:LESSON|STEP)\s+[0-9]+[A-Z]?',
                              lambda m: "%sSTEP %02d" % (m.group(1), own), text)
                # 先頭の旧ラベルは「コロン付き」とは限らない。"STEP 17 Scope" のように
                # コロン無しの形を剥がし損ねると、前に付け足して
                # "STEP 14: STEP 17 Scope" という二重表記になる（実際に13ページで起きた）。
                text = re.sub(r'<title>(?:(?:Lesson|STEP)\s+[0-9]+[A-Z]?:?\s*)+',
                              '<title>', text, count=1, flags=re.I)
                text = re.sub(r'<title>', '<title>STEP %02d: ' % own, text, count=1)
                text = re.sub(r'(<footer><p>OpenUSD Academy · )[^<]*',
                              lambda m: "%sSTEP %02d" % (m.group(1), own), text)

            # 3. remaining plain-text mentions (including not-yet-written lessons)
            for label in labels:
                if label in text:
                    text = text.replace(label, "STEP %02d" % label_step[label])

            if nav_src:
                text = text.replace("\x00NAV\x00", nav_src)
            if text != original:
                open(path, "w", encoding="utf-8").write(text)
                changed += 1
    return changed


def render_home_path():
    """Rewrite the learning-path list on index.html from PLAN.

    手書きにしていたせいで、章を足すたびにホームだけ古い順序のまま取り残された
    （STEP 46までしか出ておらず、開始リンクも3つずれていた）。ここから生成する。
    """
    ranges, _steps, total = step_numbers()
    items = []
    for ci, ch in enumerate(PLAN):
        first, last = ranges[ci]
        entry = next((fn for fn, _l, _t, _d in ch["items"] if fn and exists(fn)), None)
        if entry is None:
            continue
        num = ch["title"].split(".", 1)[0]
        name = ch["title"].split(".", 1)[1].strip()
        items.append(
            '<li><span class="path-number">STEP<br>%02d–%02d</span>'
            '<div><p class="status">第%s章 · %d STEP%s</p>'
            '<h3><a href="chapters/%s.html">%s</a></h3><p>%s</p></div>'
            '<a class="path-arrow" href="lessons/%s" aria-label="STEP %02dから始める">→</a></li>'
            % (first, last, num, last - first + 1, "S" if last > first else "",
                 ch["slug"], name, ch["lead"], entry, first))

    path = os.path.join(REPO, "index.html")
    text = original = open(path, encoding="utf-8").read()
    block = ('<!-- PATH:START generated by tools/reorder.py -->\n'
             '      <ol class="path-list">\n        %s\n      </ol>\n'
             '      <!-- PATH:END -->' % "\n        ".join(items))
    text = re.sub(r"<!-- PATH:START.*?<!-- PATH:END -->", block, text, flags=re.S)
    text = re.sub(r"(<h2 id=\"path-title\">)[^<]*", r"\g<1>全%d STEP・全%d章" % (total, len(PLAN)), text)
    if text != original:
        open(path, "w", encoding="utf-8").write(text)
    return len(items)


if __name__ == "__main__":
    relabelled = normalize_labels()
    total, changed = rewrite_navs()
    chapters = write_chapter_pages()
    steps = render_curriculum()
    home = render_home_path()
    print("%d lessons in order, %d navs, %d relabelled, %d chapter pages, %d steps, home %d chapters"
          % (total, changed, relabelled, chapters, steps, home))
