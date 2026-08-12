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
MODS = ["Ar", "Gf", "Plug", "Sdf", "Sdr", "Tf", "Trace", "Usd", "UsdGeom",
        "UsdLux", "UsdShade", "UsdUtils", "Vt", "Work"]
py_bad = 0
for rel in sorted(os.path.join("lessons", f) for f in os.listdir(os.path.join(REPO, "lessons"))
                  if f.endswith(".html")):
    text = open(os.path.join(REPO, rel), encoding="utf-8").read()
    for m in re.finditer(r'<div class="code-card python-card">.*?<span>([^<]*)</span>.*?<pre><code>(.*?)</code></pre>',
                         text, re.S):
        code = _html.unescape(re.sub(r"<[^>]+>", "", m.group(2)))
        imp = re.search(r"from pxr import ([^\n]+)", code)
        if not imp:
            continue      # 続きのスニペットは import を書かない
        imported = {x.strip() for x in imp.group(1).split(",")}
        used = {n for n in MODS if re.search(r"\b%s\." % re.escape(n), code)}
        missing = sorted(used - imported)
        if missing:
            py_bad += 1
            print("\n%s" % rel)
            print("   - import漏れ [%s] %s" % (m.group(1), ", ".join(missing)))

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

print("\n%d pages checked, %d with issues" % (len(list(pages())), problems))
print("%d lessons nav-checked, %d with issues" % (len(order), nav_problems))
print("%d USDA blocks parsed, %d with syntax errors" % (usda_checked, usda_bad))
print("%d python blocks with missing imports" % py_bad)
print("%d lessons missing a required section" % sec_bad)

sys.exit(0)
