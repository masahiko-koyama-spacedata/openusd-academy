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

print("\n%d pages checked, %d with issues" % (len(list(pages())), problems))
sys.exit(0)
