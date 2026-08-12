"""Check every HTML page in the repo: relative links resolve, tags balance, required sections exist."""
import html.parser
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VOID = {"meta", "link", "br", "img", "input", "hr", "source", "area", "base", "col", "embed",
        "param", "track", "wbr"}


class Balance(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.errors = []

    def handle_starttag(self, tag, attrs):
        if tag not in VOID:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if not self.stack:
            self.errors.append("</%s> with nothing open" % tag)
        elif self.stack[-1] != tag:
            self.errors.append("</%s> while <%s> open" % (tag, self.stack[-1]))
            if tag in self.stack:
                while self.stack and self.stack.pop() != tag:
                    pass
        else:
            self.stack.pop()


def pages():
    for name in sorted(os.listdir(REPO)):
        if name.endswith(".html"):
            yield os.path.join(REPO, name)
    for sub in ("chapters", "lessons"):
        folder = os.path.join(REPO, sub)
        if not os.path.isdir(folder):
            continue
        for name in sorted(os.listdir(folder)):
            if name.endswith(".html"):
                yield os.path.join(folder, name)


problems = 0
for path in pages():
    rel = os.path.relpath(path, REPO)
    text = open(path, encoding="utf-8").read()
    issues = []

    b = Balance()
    b.feed(text)
    issues += b.errors
    if b.stack:
        issues.append("unclosed: %s" % b.stack)

    base = os.path.dirname(path)
    for attr in ("href", "src"):
        for target in re.findall(r'%s="([^"]+)"' % attr, text):
            if target.startswith(("http", "#", "mailto:", "data:")):
                continue
            if not os.path.exists(os.path.join(base, target.split("#")[0])):
                issues.append("missing %s=%s" % (attr, target))

    for img in re.findall(r"<img [^>]*>", text):
        if 'alt="' not in img:
            issues.append("img without alt: %s" % img[:60])

    if rel.startswith("lessons/"):
        for needed, label in ((r'class="site-header"', "site-header"),
                              (r"assets/js/app.js", "app.js"),
                              (r'class="lesson-footer-nav"', "footer-nav"),
                              (r'class="lesson-section references"', "references"),
                              (r"lesson-glossary|<dl", "glossary"),
                              (r"確認日", "確認日")):
            if not re.search(needed, text):
                issues.append("missing %s" % label)
        for h in re.findall(r"<h[123][^>]*>(.*?)</h[123]>", text, re.S):
            plain = re.sub(r"<[^>]+>", "", h).strip()
            if plain.endswith("。"):
                issues.append("heading ends with 。: %s" % plain[:40])

    if issues:
        problems += 1
        print("\n%s" % rel)
        for i in issues:
            print("   - %s" % i)

# --- 前後ナビが学習順序と一致しているか ---
# <nav class="lesson-footer-nav" aria-label="..."> と属性が付いた古い
# テンプレートが reorder.py の書き換えから漏れ、20ページが古い順序のまま
# 公開されていた。存在チェックだけでは気付けなかったので、中身も見る。
import importlib.util

spec = importlib.util.spec_from_file_location(
    "reorder", os.path.join(REPO, "tools", "reorder.py"))
reorder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(reorder)
order = [it[0] for ch in reorder.PLAN for it in ch["items"] if it[0]]
step_of = {fn: i + 1 for i, fn in enumerate(order)}

nav_problems = 0
for index, fn in enumerate(order, 1):
    text = open(os.path.join(REPO, "lessons", fn), encoding="utf-8").read()
    nav = re.search(r'<nav class="lesson-footer-nav"[^>]*>(.*?)</nav>', text, re.S)
    found = []
    if not nav:
        found.append("footer nav が無い")
    else:
        targets = []
        for href, label in re.findall(r'<a[^>]*href="([^"]+)"[^>]*>(.*?)</a>',
                                      nav.group(1), re.S):
            if "chapters/" in href:
                continue
            targets.append(os.path.basename(href))
            plain = re.sub(r"<[^>]+>", "", label)
            if len(re.findall(r"STEP\s+\d+", plain)) > 1:
                found.append("footer nav のラベルが二重: %s" % plain)
            want = step_of.get(os.path.basename(href))
            got = re.search(r"STEP\s+(\d+)", plain)
            if want and got and int(got.group(1)) != want:
                found.append("footer nav の番号が不一致: %s は STEP %d" % (plain, want))
        for offset, name in ((-1, "prev"), (1, "next")):
            j = index - 1 + offset
            if 0 <= j < len(order) and order[j] not in targets:
                found.append("footer nav の%sが順序と不一致: %s が無い" % (name, order[j]))
    if found:
        nav_problems += 1
        print("\n%s (STEP %02d)" % (fn, index))
        for f in found:
            print("   - %s" % f)

# --- 表示しているUSDAが本当に構文として通るか ---
# lessons に貼ったUSDAは読者がそのまま写して使う。3ページで
# `def Sphere "Seat" { double radius = 0.5 }` という、Propertyを含む
# 一行のPrim bodyを書いてしまい公開していた。usdcat で実際に読ませる。
import html as _html
import subprocess
import tempfile

# 断片（Prim定義を含まない一部だけの引用）は1ファイルとして成立しないので対象外
SKIP_CARD = re.compile(r"ターミナル|出力|usdtree|usdcat|usdchecker|usdrecord|\.json|\.py|結果|断片")
usda_checked = usda_bad = 0
for rel, path in [(r, os.path.join(REPO, r)) for r in
                  sorted(os.path.join("lessons", f) for f in os.listdir(os.path.join(REPO, "lessons"))
                         if f.endswith(".html"))]:
    text = open(path, encoding="utf-8").read()
    for m in re.finditer(r'<div class="code-card usda-card">.*?<span>([^<]*)</span>.*?<pre><code>(.*?)</code></pre>',
                         text, re.S):
        title, raw = m.group(1), m.group(2)
        if SKIP_CARD.search(title):
            continue
        code = _html.unescape(re.sub(r"<[^>]+>", "", raw))
        if re.search(r"^\s*\$", code, re.M) or "..." in code or "…" in code:
            continue          # シェル出力・省略記号を含む抜粋は対象外
        if not re.search(r"^\s*(def|over|class)\s", code, re.M):
            continue          # Prim定義が無いものは1ファイルとして成立しない
        usda_checked += 1
        src = code if code.lstrip().startswith("#usda") else \
            '#usda 1.0\n(\n    metersPerUnit = 1\n    upAxis = "Y"\n)\n\n' + code
        with tempfile.NamedTemporaryFile("w", suffix=".usda", delete=False, encoding="utf-8") as fh:
            fh.write(src)
            tmp = fh.name
        r = subprocess.run(["/usr/bin/usdcat", tmp], capture_output=True, text=True)
        os.unlink(tmp)
        if r.returncode != 0:
            usda_bad += 1
            msg = re.sub(r'Failed to open "[^"]*" - \S*?:', "", (r.stderr or r.stdout)).strip()
            print("\n%s" % rel)
            print("   - USDA構文エラー [%s] %s" % (title, msg.splitlines()[0][:110]))

# --- Python例のimport漏れ ---
# import を書いていないカードを一律に飛ばすと、ページ内のどのカードでも
# import されていないモジュールを見逃す（実際に adhoc.py で起きた）。
# ページ単位で「そこまでに import されたもの」を積み上げて判定する。
MODS = ["Ar", "Gf", "Plug", "Sdf", "Sdr", "Tf", "Trace", "Usd", "UsdGeom",
        "UsdLux", "UsdShade", "UsdUtils", "Vt", "Work"]
py_bad = 0
for rel in sorted(os.path.join("lessons", f) for f in os.listdir(os.path.join(REPO, "lessons"))
                  if f.endswith(".html")):
    text = open(os.path.join(REPO, rel), encoding="utf-8").read()
    # カード見出しが別の .py なら別ファイル。そこで import を引き継ぐと、
    # 前のファイルの import で通ってしまう。同じファイル名の続きだけ引き継ぐ。
    by_file = {}          # ファイル名 -> import 済みモジュール
    current = None
    for m in re.finditer(r'<div class="code-card python-card">.*?<span>([^<]*)</span>.*?<pre><code>(.*?)</code></pre>',
                         text, re.S):
        title = m.group(1)
        name = re.search(r"[\w.-]+\.py", title)
        if name:
            current = name.group(0)
        elif current is None:
            current = title            # ファイル名が無い最初のカード
        seen = by_file.setdefault(current, set())
        code = _html.unescape(re.sub(r"<[^>]+>", "", m.group(2)))
        for imp in re.findall(r"from pxr import ([^\n]+)", code):
            seen |= {x.strip() for x in imp.split(",")}
        # 出力例をコメントで併記しているので、コメントは使用扱いにしない
        live = re.sub(r"#[^\n]*", "", code)
        used = {n for n in MODS if re.search(r"\b%s\." % re.escape(n), live)}
        missing = sorted(used - seen)
        if missing:
            py_bad += 1
            print("\n%s" % rel)
            print("   - import漏れ [%s] %s（%s のどのカードにも無い）"
                  % (title, ", ".join(missing), current))

# --- xformOp の型が Python API の既定精度と一致しているか ---
# AddScaleOp() の既定は PrecisionFloat なので float3、AddTranslateOp() は
# PrecisionDouble なので double3 になる。USDA 側を double3 xformOp:scale と
# 書くと、対訳の Python が別の型を作ることになる。
XFORM_PRECISION = {"xformOp:scale": "float3",
                   "xformOp:translate": "double3",
                   "xformOp:rotateXYZ": "float3",
                   "xformOp:rotateXYZ:": "float3"}
xf_bad = 0
for rel in sorted([os.path.join("lessons", f) for f in os.listdir(os.path.join(REPO, "lessons"))
                   if f.endswith(".html")]
                  + [os.path.join(dp, f).replace(REPO + os.sep, "")
                     for dp, _dn, fn in os.walk(os.path.join(REPO, "examples"))
                     for f in fn if f.endswith(".usda")]):
    text = open(os.path.join(REPO, rel), encoding="utf-8").read()
    # 明示的に PrecisionDouble / PrecisionFloat を使うと書いてあるページは、
    # その精度を意図しているので対象外。double3 xformOp:scale 自体は
    # OpenUSD として正しい記述で、誤りなのは「対訳のPythonと型が食い違う」ときだけ。
    if re.search(r"Precision(?:Double|Float)|MakeMatrixXform", text):
        continue
    # xformOp:translate:pivot などサフィックス付きは別扱いなので除外する
    for typ, name in re.findall(
            r"\b(double3|float3) (xformOp:(?:scale|translate|rotateXYZ))(?![:\w])", text):
        want = XFORM_PRECISION.get(name)
        if want and typ != want:
            xf_bad += 1
            print("\n%s" % rel)
            print("   - xformOpの型がAPIの既定と違う: %s %s（%s が既定。\n     意図して別精度にするなら Precision* を明示する）" % (typ, name, want))

# --- 教材ルールの必須セクション ---

REQUIRED = (("USDA→Python mapping", r"USDA\s*→\s*(Python|コマンド)\s*mapping"),
            ("Diagram", r'class="chapter-map"|class="concept-flow"|class="hierarchy-figure"|class="tree-stage"'),
            ("USDAカード", r"code-card usda-card"),
            ("Pythonカード", r"code-card python-card"),
            ("よくある間違い", r"よくある間違い"))
sec_bad = 0
for rel in sorted(os.path.join("lessons", f) for f in os.listdir(os.path.join(REPO, "lessons"))
                  if f.endswith(".html")):
    text = open(os.path.join(REPO, rel), encoding="utf-8").read()
    missing = [name for name, rx in REQUIRED if not re.search(rx, text)]
    if missing:
        sec_bad += 1
        print("\n%s" % rel)
        for name in missing:
            print("   - 必須セクションが無い: %s" % name)

# --- 記法（記号）の説明が初出のレッスンにあるか ---
# AGENTS.md のルール7。以前は「全レッスンで説明する」と読める書き方だったが、
# 100レッスンで毎回繰り返すと本題が埋もれるため「初出時に説明する」へ改めた。
# 改めた以上、初出のレッスンにあることは機械で確かめる。
SYMBOLS = ((u"インデント", ["01-reading-usda.html", "07-usda-syntax.html"]),
           (u"波括弧", ["01-reading-usda.html", "07-usda-syntax.html"]),
           (u"引用符", ["01-reading-usda.html", "07-usda-syntax.html"]),
           (u"Path", ["01-reading-usda.html", "05-prim-property-paths.html"]),
           (u"アットマーク|Asset Path", ["12-references.html"]))
sym_bad = 0
for label, files in SYMBOLS:
    for fn in files:
        path = os.path.join(REPO, "lessons", fn)
        if not os.path.exists(path):
            continue
        if not re.search(label, open(path, encoding="utf-8").read()):
            sym_bad += 1
            print("\nlessons/%s" % fn)
            print("   - 記法の説明が無い: %s（初出のレッスンなので必要）" % label)

print("\n%d pages checked, %d with issues" % (len(list(pages())), problems))
print("%d lessons nav-checked, %d with issues" % (len(order), nav_problems))
print("%d USDA blocks parsed, %d with syntax errors" % (usda_checked, usda_bad))
print("%d python blocks with missing imports" % py_bad)
print("%d lessons missing a required section" % sec_bad)
print("%d symbol explanations missing at first use" % sym_bad)

# 検査が問題を見つけたら 0 以外で終わる。ここが常に 0 だったため、
# エラーを表示していてもシェルやCIからは成功として扱われていた。
failures = problems + nav_problems + usda_bad + py_bad + xf_bad + sec_bad + sym_bad
if failures:
    print("\nFAILED: %d issue(s)" % failures)
    sys.exit(1)
print("\nAll checks passed")
sys.exit(0)

