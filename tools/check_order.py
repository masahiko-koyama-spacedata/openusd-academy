# -*- coding: utf-8 -*-
"""学習順序の検査。

初学者向け教材の前提として、あるSTEPは「まだ習っていないこと」に依存してはいけません。
このスクリプトは2種類の先取りを検出します。

1. 前方参照リンク  … STEP N のページから STEP M（M > N）へリンクしている
2. 用語の先取り    … STEP N の本文が、STEP M（M > N）の用語集で初出とされる語を使っている

どちらも「絶対に禁止」ではありません。次回予告として意図的に張る前方リンクはあり得ます。
そのため結果は一覧で出し、人が見て判断できる形にします。
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from reorder import PLAN, REPO  # noqa: E402

LESSONS = os.path.join(REPO, "lessons")


def step_of_file():
    steps, n = {}, 0
    for ch in PLAN:
        for fn, _label, _t, _d in ch["items"]:
            n += 1
            if fn:
                steps[fn] = n
    return steps


def strip_tags(html):
    html = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", html, flags=re.S)
    return re.sub(r"<[^>]+>", " ", html)


def glossary_terms(html):
    """そのページの用語集セクションに出てくる <dt> を返す。"""
    m = re.search(r'<p class="section-kicker">Glossary</p>.*?</section>', html, re.S)
    if not m:
        m = re.search(r'<h2>このレッスンの用語</h2>.*?</section>', html, re.S)
    if not m:
        return []
    terms = re.findall(r"<dt>(.*?)</dt>", m.group(0), re.S)
    out = []
    for t in terms:
        t = re.sub(r"<[^>]+>", "", t).strip()
        # 「Attribute（アトリビュート）」→ 検出には英字部分だけを使う
        head = re.split(r"[（(]", t)[0].strip()
        if len(head) >= 3 and re.match(r"^[A-Za-z][A-Za-z0-9_.:/ ]*$", head):
            out.append(head)
    return out


def main():
    steps = step_of_file()
    ordered = sorted(steps.items(), key=lambda kv: kv[1])

    pages = {}
    for fn, step in ordered:
        path = os.path.join(LESSONS, fn)
        if os.path.exists(path):
            pages[fn] = (step, open(path, encoding="utf-8").read())

    # 用語 -> 初出STEP
    first_seen = {}
    for fn, step in ordered:
        if fn not in pages:
            continue
        for term in glossary_terms(pages[fn][1]):
            if term not in first_seen or step < first_seen[term][0]:
                first_seen[term] = (step, fn)

    forward_links, early_terms = [], []
    for fn, (step, html) in pages.items():
        body = html
        # 前後ナビは順序どおり動くので検査から外す
        body = re.sub(r'<nav class="lesson-footer-nav">.*?</nav>', " ", body, flags=re.S)
        for href in re.findall(r'<a href="([0-9][^"]*\.html)"', body):
            target = steps.get(os.path.basename(href))
            if target and target > step:
                forward_links.append((step, fn, target, os.path.basename(href)))

        text = strip_tags(body)
        for term, (tstep, tfile) in first_seen.items():
            if tstep > step and re.search(r"(?<![A-Za-z])%s(?![A-Za-z])" % re.escape(term), text):
                early_terms.append((step, fn, term, tstep, tfile))

    print("=== 前方参照リンク（後のSTEPへのリンク）===")
    if not forward_links:
        print("  なし")
    for step, fn, target, href in sorted(forward_links):
        print("  STEP %02d %-34s -> STEP %02d %s" % (step, fn, target, href))

    print()
    print("=== 用語の先取り（後のSTEPで初出の語を使用）===")
    if not early_terms:
        print("  なし")
    for step, fn, term, tstep, tfile in sorted(early_terms):
        print("  STEP %02d %-30s 「%s」 初出=STEP %02d (%s)" % (step, fn, term, tstep, tfile))

    print()
    print("%d 前方リンク / %d 用語先取り" % (len(forward_links), len(early_terms)))


if __name__ == "__main__":
    main()
