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

print("\n%d pages checked, %d with issues" % (len(list(pages())), problems))
print("%d lessons nav-checked, %d with issues" % (len(order), nav_problems))
sys.exit(0)
