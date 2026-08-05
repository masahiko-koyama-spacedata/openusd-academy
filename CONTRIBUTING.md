# OpenUSD Academyで複数PCを使う

このリポジトリは、PC間でフォルダを直接同期せず、GitHubを変更の受け渡し場所として使います。各PCにはリポジトリを個別にcloneし、`.git`を含むフォルダをiCloud Drive、Dropbox、OneDriveなどで同期しません。

## 基本ルール

- `main`では教材を直接編集しない
- 一つのLessonまたは一つの目的につき、一つの作業ブランチを作る
- ブランチ名は `codex/lesson-15-scope` のように目的が分かる名前にする
- 複数PCで同じLessonを同時に編集しない
- PCを移る前に変更をコミットし、利用者の承認を得てpushする
- `curriculum.html`、`curriculum.md`、`glossary.html`、`glossary.md`のような共有ファイルは、Lesson本体と同じブランチで更新する
- GitHubへのpush、公開、デプロイは必ず事前に利用者の承認を得る

## 作業を始める

未コミット変更がないことを確認してから、`main`を最新化します。

```bash
git status --short
git switch main
git pull --ff-only
git switch -c codex/lesson-15-scope
```

`git status --short`に変更が表示された場合は、先にコミットするか、不要な変更かを確認します。内容を確認せず破棄しません。

## 作業を保存する

変更を目的ごとに選んでコミットします。`git add .`ではなく、対象ファイルを明示します。

```bash
git status --short
git diff --check
git add lessons/15-scope.html curriculum.html curriculum.md
git diff --cached
git commit -m "Add Lesson 15 about Scope"
```

push前に、コミットへ意図しないファイルが入っていないことを確認します。

```bash
git status --short
git show --stat --oneline HEAD
```

## 別のPCへ引き継ぐ

利用者の承認後、現在のブランチをGitHubへpushします。

```bash
git push -u origin codex/lesson-15-scope
```

別のPCで同じブランチを引き継ぐ場合は、次のように取得します。

```bash
git fetch origin
git switch --track origin/codex/lesson-15-scope
```

すでにローカルブランチがある場合は、そのブランチへ切り替えてfast-forwardします。

```bash
git switch codex/lesson-15-scope
git pull --ff-only
```

同じブランチを両方のPCで同時に進めず、引き継ぐ側がpushを終えてから次のPCで作業を始めます。

## mainへ統合した後

GitHub上で作業ブランチを`main`へ統合したら、各PCの`main`を更新します。

```bash
git switch main
git pull --ff-only
```

不要になったローカルブランチは、統合済みであることを確認してから削除できます。

```bash
git branch -d codex/lesson-15-scope
```

## 衝突を避ける担当の分け方

Lesson番号単位で担当を分けます。たとえば、PC AでLesson 15を制作中なら、PC BではLesson 16を始めず、Lesson 15が`main`へ統合されてから次のLessonを開始するのが最も安全です。

並行作業が必要な場合は、Lesson本体が重ならない作業を選びます。ただしカリキュラムや用語集などの共有ファイルは衝突しやすいため、一方のブランチだけで更新します。

## pullできないとき

`git pull --ff-only`が失敗したら、その場でmergeや強制resetをせず、次を確認します。

```bash
git status --short --branch
git log --oneline --decorate --graph --all -12
```

未コミット変更、ローカルだけのコミット、別PCからの更新のどれがあるかを確認してから解決します。
