# -*- coding: utf-8 -*-
"""Single source for the learning order.

Lesson file names (and therefore lesson numbers) stay fixed so that the 55 pages of
cross-links keep working. What changes is the order a learner walks through them:
the curriculum lists STEPs, and every lesson's prev/next nav follows the same order.
"""
import os
import re

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# (chapter title, chapter lead, [(file or None, lesson label, title, one-line description)])
PLAN = [
    ("1. まずUSDAを読む",
     "最初の目標は「書く」ではなく「読める」です。短いテキストを一行ずつ読み解きます。", [
        ("01-reading-usda.html", "Lesson 01", "はじめてのUSDAを読む", "Stage、Prim、Xform、名前、Pathを短いUSDAから一行ずつ読む"),
        ("02-what-is-openusd.html", "Lesson 02", "OpenUSDとは何か", "シーン記述・合成・共同作業の土台を知る"),
        ("03-stage-prim-property.html", "Lesson 03", "Stage・Prim・Property", "全体、構成要素、情報を分ける"),
        ("07-usda-syntax.html", "Lesson 07", "USDAの基本構文", "型・名前・波括弧・Propertyを読む"),
        ("06-usd-file-formats.html", "Lesson 06", "USDA・USDC・USD・USDZ", "中身と用途でファイル形式を選ぶ"),
     ]),
    ("2. ファイル先頭の約束事",
     "すべての例に出てくるファイル先頭のMetadataを、ここで先に理解しておきます。", [
        ("09a-default-prim.html", "Lesson 09A", "Default Prim", "Layerを外から利用するときの入口を決める"),
        ("20a-meters-per-unit.html", "Lesson 20A", "metersPerUnit", "長さの「1」が何メートルかを宣言する"),
        ("20b-up-axis.html", "Lesson 20B", "upAxis", "どの軸が上かを宣言する"),
        ("20c-kilograms-per-unit.html", "Lesson 20C", "kilogramsPerUnit", "質量の「1」が何キログラムかを宣言する"),
     ]),
    ("3. Propertyを読み書きする",
     "Primが持つ情報の中身に入ります。値の型と、対象の指し方を押さえます。", [
        ("04-attributes-relationships.html", "Lesson 04", "AttributeとRelationship", "値とつながりを読み分ける"),
        ("22-value-types.html", "Lesson 22", "AttributeのValue Type", "scalar、vector、matrix、arrayとrole"),
        ("05-prim-property-paths.html", "Lesson 05", "Prim PathとProperty Path", "Stage内の対象を正確に指す"),
        ("25-relationship-target.html", "Lesson 25", "Relationship Target", "一つと複数の対象を同じ仕組みで書く"),
        ("26-custom-properties.html", "Lesson 26", "Custom Properties", "Schema外の情報を追加する"),
     ]),
    ("4. Pythonから触る",
     "ここで初めてコードを書きます。USDAで読めるようになった構造を、そのままAPIで作ります。", [
        ("08-python-pxr-modules.html", "Lesson 08", "Pythonとpxrモジュール", "Usd・Sdf・Gf・UsdGeomを使い分ける"),
        ("09-metadata-schemas.html", "Lesson 09", "MetadataとSchema", "補助情報とデータの設計図を分ける"),
     ]),
    ("5. 形を置いて動かす",
     "階層と変換です。ここまでで、自分でシーンを組み立てられるようになります。", [
        ("15-scope.html", "Lesson 15", "Scope", "変換を持たず、Primを用途ごとに整理する"),
        ("10-xform-hierarchy.html", "Lesson 10", "Xformと階層", "親の変換が子へ届く仕組みを知る"),
        ("16-xform-common-api.html", "Lesson 16", "XformCommonAPI", "一般的な変換を交換しやすい構成で扱う"),
        ("17a-translate.html", "Lesson 17A", "Translate", "位置を三つの軸で記述する"),
        ("17b-rotate.html", "Lesson 17B", "Rotate", "回転角とRotation Orderを読む"),
        ("17c-scale.html", "Lesson 17C", "Scale", "各軸の倍率を記述する"),
        ("17d-pivot.html", "Lesson 17D", "Pivot", "回転と拡縮の中心を決める"),
        ("18-xform-op-order.html", "Lesson 18", "XformOpOrder", "変換順序で結果が変わる理由"),
     ]),
    ("6. 形の上へ値を配る",
     "Primvarの回です。値の個数の数え方が中心で、5つのInterpolationを一つずつ確かめます。", [
        ("23-primvars.html", "Lesson 23", "Primvars", "Attributeとの違いと三つの機能"),
        ("24a-constant.html", "Lesson 24A", "constant interpolation", "Prim全体へ一つの値"),
        ("24b-uniform.html", "Lesson 24B", "uniform interpolation", "Faceごとに一つの値"),
        ("24c-vertex.html", "Lesson 24C", "vertex interpolation", "Pointごとに一つの値"),
        ("24d-varying.html", "Lesson 24D", "varying interpolation", "Pointごとの値を線形補間する"),
        ("24e-face-varying.html", "Lesson 24E", "faceVarying interpolation", "Face Vertexごとに一つの値"),
        ("24f-indexed-primvars.html", "Lesson 24F", "Indexed Primvars", "値とindexを分けて再利用する"),
        ("24g-primvar-inheritance.html", "Lesson 24G", "Primvar Inheritance", "constant Primvarを階層へ適用する"),
     ]),
    ("7. 時間を記述する",
     "値が時間で変わる書き方です。Compositionへ進む前に済ませておきます。", [
        ("11-time-codes-samples.html", "Lesson 11", "Time CodeとTime Sample", "時点と値で時間変化を記述する"),
     ]),
    ("8. Prim Specの3つの書き方",
     "Compositionの前に、def・over・classの違いをここで確実にします。これがないと合成の説明が読めません。", [
        ("27a-def.html", "Lesson 27A", "def", "Primを定義する"),
        ("27b-over.html", "Lesson 27B", "over", "既存PrimへOpinionだけを重ねる"),
        ("27c-class.html", "Lesson 27C", "class", "Inherits用の抽象Prim Specを作る"),
     ]),
    ("9. コンポジション",
     "OpenUSDでいちばん難しい部分です。ここまでの土台があって初めて読み進められます。", [
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
    ("10. Compositionを組み立てる",
     "合成の仕組みが分かったところで、実際の組み立て方と調べ方へ進みます。", [
        (None, "Lesson 28", "Prim Composition", "複数のPrim Specが一つになる"),
        ("29-internal-external-arc.html", "Lesson 29", "Internal ArcとExternal Arc", "同じLayer内と別ファイル"),
        ("30-list-editing.html", "Lesson 30", "List Editing", "prepend・append・delete・reorder"),
        (None, "Lesson 31", "Encapsulation", "Assetの境界を守る"),
        (None, "Lesson 32", "Variant Edit Context", "選択肢の中へ書く"),
        (None, "Lesson 33", "Direct ArcとAncestral Arc", "同じArc内の強度を追う"),
        ("34a-prim-stack.html", "Lesson 34A", "Prim Stack", "Primへ寄与するPrim Specを調べる"),
        ("34b-property-stack.html", "Lesson 34B", "Property Stack", "Propertyへ寄与するSpecを調べる"),
     ]),
    ("11. モデル階層とアセット設計",
     "Kindでシーンに役割を与え、再利用できるアセットの形にまとめます。", [
        ("19a-kind.html", "Lesson 19A", "Kind", "Schema型とModel Hierarchy上の役割を分ける"),
        ("19b-component.html", "Lesson 19B", "component", "再利用可能なleaf modelを作る"),
        ("19c-group.html", "Lesson 19C", "group", "Modelを正しい祖先階層へまとめる"),
        ("19d-assembly.html", "Lesson 19D", "assembly", "公開可能なaggregate Assetを作る"),
        ("19e-subcomponent.html", "Lesson 19E", "subcomponent", "component内部の重要なPrimを示す"),
        ("13-asset-structure.html", "Lesson 13", "再利用できるアセット設計", "Asset Structure、Model Kind、Asset Interface、Reference/Payload Pattern"),
     ]),
    ("12. Stageを調べて制御する",
     "大きなシーンを扱うための、読み込みと走査の制御です。", [
        ("41-active-inactive.html", "Lesson 41", "ActiveとInactive", "Compositionから除外する"),
        ("42-load-unload.html", "Lesson 42", "LoadとUnload", "Payloadを制御する"),
        ("43-stage-traversal.html", "Lesson 43", "Stage Traversal", "Primを順番に調べる"),
        ("44-traversal-predicate.html", "Lesson 44", "Traversal Predicate", "調べるPrimを絞る"),
        (None, "Lesson 45", "Hydra", "Scene Indexとレンダリングの入口"),
     ]),
    ("13. パイプラインとData Exchange",
     "他のツールとの間でデータを受け渡す実務です。", [
        ("14-data-pipelines.html", "Lesson 14", "データを運ぶパイプライン", "データ交換、抽出、変換、検証、Instancing"),
        (None, "Lesson 47", "Asset Entry Point", "参照される入口を作る"),
        (None, "Lesson 48", "Asset Interface", "公開する情報を選ぶ"),
        (None, "Lesson 49", "Workstream Layers", "作業をLayerで分ける"),
        (None, "Lesson 51", "Asset Parameterization", "下流から変更できる値"),
        (None, "Lesson 52", "Reference/Payload Pattern", "InterfaceとContentsを分ける"),
        (None, "Lesson 53", "Lofting", "Payloadを開かず重要情報を見せる"),
        (None, "Lesson 54", "Converterの構造", "入力・変換・出力を分ける"),
        (None, "Lesson 55", "Geometry Extraction", "点・法線・UVを対応させる"),
        (None, "Lesson 56", "Material Extraction", "MaterialとBindingを対応させる"),
        (None, "Lesson 57", "Asset Validation", "規則をコードにする"),
        (None, "Lesson 58", "Prim Hierarchy Transformation", "階層を目的形へ変える"),
        (None, "Lesson 59", "Export Options", "変換条件を利用者へ公開する"),
     ]),
    ("14. Instancingと大規模シーン",
     "同じものを大量に置くための仕組みです。", [
        (None, "Lesson 60", "Asset Modularity", "再利用単位を決める"),
        (None, "Lesson 61", "Scenegraph Instancing", "CompositionからPrototypeを作る"),
        (None, "Lesson 62", "Nested Instancing", "Instanceを階層化する"),
        (None, "Lesson 63", "Instance Refinement", "Instanceごとの差を付ける"),
        (None, "Lesson 64", "Point Instancing", "大量の単純要素を配置する"),
        (None, "Lesson 65", "ScenegraphとPointの選択", "用途と制約を比較する"),
     ]),
    ("15. 調査・検証・総復習",
     "最後に、壊れたシーンを直せるところまで進みます。", [
        (None, "Lesson 66", "usdviewとusdrecordでStageを読む", "構造と描画を確かめる"),
        (None, "Lesson 67", "Layer Stackを調べる", "どのLayerの意見が効いているか"),
        (None, "Lesson 68", "壊れたReferenceとPathを直す", "よくある破損の直し方"),
        (None, "Lesson 69", "Pythonで最小Validationを書く", "規則を自動で確かめる"),
        (None, "Lesson 70", "小さなAssetを最初から組み立てる", "総合演習1"),
        (None, "Lesson 71", "複数Assetから小さなSceneを作る", "総合演習2"),
        (None, "Lesson 72", "OpenUSD教材の総復習", "全体を振り返る"),
     ]),
]


def written_sequence():
    seq = []
    for _, _, items in PLAN:
        for fn, label, title, _desc in items:
            if fn:
                seq.append((fn, label, title))
    return seq


def rewrite_navs():
    seq = written_sequence()
    changed = 0
    for i, (fn, label, title) in enumerate(seq):
        path = os.path.join(REPO, "lessons", fn)
        text = open(path, encoding="utf-8").read()
        parts = []
        if i > 0:
            pfn, plabel, _ = seq[i - 1]
            parts.append('<a href="%s">← %s</a>' % (pfn, plabel))
        else:
            parts.append('<a href="../curriculum.html">← カリキュラム</a>')
        if i < len(seq) - 1:
            nfn, nlabel, _ = seq[i + 1]
            parts.append('<a href="%s">%s →</a>' % (nfn, nlabel))
        else:
            parts.append('<a href="../curriculum.html">全カリキュラムへ →</a>')
        nav = '<nav class="lesson-footer-nav">%s</nav>' % "".join(parts)
        new = re.sub(r'<nav class="lesson-footer-nav">.*?</nav>', nav, text, flags=re.S)
        if new != text:
            open(path, "w", encoding="utf-8").write(new)
            changed += 1
    return len(seq), changed


def render_curriculum():
    step = 0
    html_sections, md_sections = [], []
    for ch_title, ch_lead, items in PLAN:
        lis, md_lines = [], []
        for fn, label, title, desc in items:
            step += 1
            if fn:
                lis.append('<li><a href="lessons/%s"><strong>STEP %02d · %s: %s</strong>'
                           '<span>%s</span></a></li>' % (fn, step, label, title, desc))
                md_lines.append("- **STEP %02d · %s:** [%s](lessons/%s) — %s"
                                % (step, label, title, fn, desc))
            else:
                lis.append('<li><span class="planned"><strong>STEP %02d · %s: %s（予定）</strong>'
                           '<span>%s</span></span></li>' % (step, label, title, desc))
                md_lines.append("- **STEP %02d · %s（予定）:** %s — %s" % (step, label, title, desc))
        html_sections.append('<section><h2>%s</h2><p class="chapter-lead">%s</p>'
                             '<ol class="lesson-index">%s</ol></section>'
                             % (ch_title, ch_lead, "".join(lis)))
        md_sections.append("## %s\n\n%s\n\n%s" % (ch_title, ch_lead, "\n".join(md_lines)))

    intro = ("このカリキュラムは、[OpenUSD公式ドキュメント](https://openusd.org/release/index.html) を技術上の一次情報とし、"
             "[NVIDIA Learn OpenUSD](https://docs.nvidia.com/learn-openusd/latest/index.html) を主要な学習資料として照合したうえで、"
             "日本語の初学者が段階的に進めるようAcademy独自に整理した計画です（確認日: 2026-08-06）。")
    note = ("**STEP番号が学習の順番です。** Lesson番号はファイルの識別子で、教材を追加してきた順に付いています。"
            "初学者がつまずきにくい順序を優先した結果、Lesson番号とSTEP番号は一致しません。"
            "各レッスンの前後リンクもSTEPの順に並んでいるので、上から順にたどれば迷いません。")

    html = '''<!doctype html>
<html lang="ja">
<head>
  <meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="color-scheme" content="light dark">
  <title>カリキュラム — OpenUSD Academy</title>
  <link rel="stylesheet" href="assets/css/style.css"><script src="assets/js/app.js" defer></script>
</head>
<body>
  <header class="site-header"><a class="brand" href="index.html"><span class="brand-mark" aria-hidden="true">O</span><span>OpenUSD Academy</span></a><nav aria-label="メインナビゲーション"><a href="index.html">ホーム</a><a href="glossary.html">用語集</a></nav><button class="theme-toggle" type="button" data-theme-toggle aria-label="表示テーマを切り替える" aria-pressed="false"><span aria-hidden="true">◐</span><span class="theme-label">テーマ</span></button></header>
  <main class="document">
    <p class="eyebrow">CURRICULUM</p><h1>OpenUSD Academy カリキュラム</h1>
    <p class="lead">%s</p>
    <aside class="academy-note"><p class="source-label">読み方</p><p>%s</p></aside>
%s
    <p><a class="back-link" href="index.html">← ホームへ戻る</a></p>
  </main>
  <footer><p>OpenUSD Academy</p><a href="https://docs.nvidia.com/learn-openusd/latest/index.html">NVIDIA Learn OpenUSD ↗</a></footer>
</body></html>
''' % (intro, note.replace("**", ""), "\n    ".join(html_sections))

    md = "# OpenUSD Academy カリキュラム\n\n%s\n\n> %s\n\n%s\n\n> **Academy方針:** 各レッスンは現在と同程度の長さと難易度に保ち、一回に一つの中心概念を扱います。公式の概念を改変せず、図解・USDA/Python対訳・日本語でのつまずき対策を加えます。\n" % (
        intro, note, "\n\n".join(md_sections))

    open(os.path.join(REPO, "curriculum.html"), "w", encoding="utf-8").write(html)
    open(os.path.join(REPO, "curriculum.md"), "w", encoding="utf-8").write(md)
    return step


if __name__ == "__main__":
    total, changed = rewrite_navs()
    steps = render_curriculum()
    print("%d written lessons in order, %d navs rewritten, %d steps listed" % (total, changed, steps))
