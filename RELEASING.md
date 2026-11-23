---
type: Guide
---

# MOP: Release a version of Markdown 101

Method of procedure for publishing a new version, such as `v0.5`, from an Android phone with Termux. A release is a GitHub Release with the slides and cheat sheets attached as HTML, PDF, and PowerPoint.

| | |
|:---|:---|
| **Who** | Repo owner (`thephm`) |
| **Time** | 5 minutes, plus about 2 minutes for the build |
| **Risk** | Low. A release adds files and doesn't change the course |
| **Undo** | See [Rollback](#rollback) |

## How it works

Pushing a tag that starts with `v` runs the [Course workflow](.github/workflows/course.yml). It stamps the version into every footer, builds both decks and both cheat sheets, and publishes them as a release named after the tag.

Version numbers have two parts, `vMAJOR.MINOR`:

- **MINOR** (`v0.4` to `v0.5`): new or changed slides, fixes
- **MAJOR** (`v0.9` to `v1.0`): the course is restructured, or it's ready for real sessions

Never reuse a version number, even after deleting a release.

## One-time setup

Do this once per phone.

### 1. Install the tools

Install [Termux](https://termux.dev/) from F-Droid, then:

```bash
pkg install git gh
```

```bash
termux-setup-storage
```

Tap **Allow** so Termux can see your phone's storage at `~/storage/shared`.

### 2. Make a GitHub token

On github.com, go to **Settings › Developer settings › Fine-grained tokens › Generate new token**, or open <https://github.com/settings/personal-access-tokens/new>.

| Setting | Value |
|:---|:---|
| Expiration | Your choice. You'll redo this section when it expires |
| Repository access | Only select repositories: `thephm/markdown` |
| Contents | Read and write |
| Workflows | Read and write |

Copy the token. GitHub shows it only once.

### 3. Sign in

```bash
gh auth login --with-token
```

There's no prompt. Paste the token, press **Enter**, then **Ctrl+D**. In Termux, Ctrl is on the extra-keys row above the keyboard, or hold **Volume Down** and tap **D**.

```bash
gh auth setup-git
```

```bash
gh auth status
```

Expect `Logged in to github.com account thephm`.

### 4. Clone the repo

```bash
cd ~/storage/shared/github
```

```bash
git clone https://github.com/thephm/markdown.git
```

```bash
git config --global --add safe.directory /storage/emulated/0/github/markdown
```

## Procedure

### 1. Pre-checks

On github.com, open **Actions › Course** and check that the latest run on `main` is green. Don't release a commit whose build failed.

Check the existing versions so you pick the next number:

```bash
cd ~/storage/shared/github/markdown
```

```bash
git pull
```

```bash
git tag
```

### 2. Tag and push

Replace `v0.5` with the next version.

```bash
git tag v0.5
```

```bash
git push origin v0.5
```

Expect `* [new tag] v0.5 -> v0.5`.

### 3. Verify

1. Open <https://github.com/thephm/markdown/actions/workflows/course.yml>. A run for `v0.5` appears within a minute. Wait for it to turn green.
2. Open <https://github.com/thephm/markdown/releases/latest>. It should be `v0.5`, with these assets:

| File | What |
|:---|:---|
| `markdown-101.html`, `.pdf`, `.pptx` | Core deck |
| `markdown-101-microsoft.html`, `.pdf`, `.pptx` | Microsoft edition deck |
| `markdown-cheatsheet.pdf` | Core cheat sheet |
| `markdown-cheatsheet-microsoft.pdf` | Microsoft cheat sheet |
| `markdown-101.md`, `markdown-101-microsoft.md` | The built decks as Markdown |

3. Open one PDF. The footer should say `Markdown 101 · v0.5`.

## Rollback

If a release is wrong, the cleanest fix is a new version with the fix, such as `v0.6`. To remove a bad release anyway:

1. On the release page, tap **Delete** (trash icon).
2. Delete the tag:

```bash
git push origin --delete v0.5
```

```bash
git tag -d v0.5
```

Don't reuse `v0.5` afterwards.

## Troubleshooting

| Symptom | Cause | Fix |
|:---|:---|:---|
| `gh auth login` hangs after the questions | Termux can't open a browser | Ctrl+C, then sign in with a token (setup step 3) |
| `gh auth login --with-token` seems stuck | It's waiting for the token, with no prompt | Paste the token, Enter, then Ctrl+D |
| `fatal: detected dubious ownership` | Android storage doesn't track file owners | `git config --global --add safe.directory /storage/emulated/0/github/markdown` |
| `git push` asks for a username and password | git isn't using the `gh` sign-in | `gh auth setup-git`, then push again |
| `Permission to thephm/markdown.git denied` (403) | The token can't write to the repo | Edit the token at <https://github.com/settings/personal-access-tokens>: add the repo, set Contents and Workflows to Read and write |
| Push fails with 401 or 403 after working before | The token expired | Make a new token (setup step 2), then redo setup step 3 |
| `tag 'v0.5' already exists` | You tagged before, or picked a used number | Run `git tag` and pick the next free number |
| The release has no files | The build failed | Open the run under **Actions › Course** and read the failed step |

Tags can't be pushed from Claude Code cloud sessions: the session's connection to GitHub refuses them. Use this procedure, or create the release in a browser at <https://github.com/thephm/markdown/releases/new>.
