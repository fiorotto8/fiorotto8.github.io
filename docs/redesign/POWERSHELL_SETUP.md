# PowerShell Setup and Safe Execution

## 1. Unpack the documentation

Assume the downloaded ZIP is in your Downloads folder.

```powershell
$zip = "$env:USERPROFILE\Downloads\fiorina_website_redesign_package.zip"
$docsTemp = "$env:USERPROFILE\Downloads\fiorina_website_redesign_package"

Expand-Archive -Path $zip -DestinationPath $docsTemp -Force
```

## 2. Set the repository path

Replace the example path with the actual local clone.

```powershell
$repo = "C:\Users\david\path\to\fiorotto8.github.io"
Set-Location $repo
```

Confirm:

```powershell
git status --short
git branch --show-current
git remote -v
```

Do not continue until unrelated uncommitted work is committed, stashed, or intentionally preserved.

## 3. Update the base branch safely

```powershell
git switch master
git pull --ff-only
```

If `git pull --ff-only` fails, stop and inspect the branch history. Do not force-reset unless you have intentionally backed up local work.

## 4. Create the redesign branch

```powershell
git switch -c redesign/technical-portfolio-2026
```

Optional local backup tag:

```powershell
git tag backup/pre-website-redesign-2026
```

Optional remote backup tag:

```powershell
git push origin backup/pre-website-redesign-2026
```

## 5. Copy the documentation into the repository

```powershell
New-Item -ItemType Directory -Path ".\docs\redesign" -Force | Out-Null

Copy-Item `
  "$docsTemp\CLAUDE.md" `
  ".\CLAUDE.md" `
  -Force

Get-ChildItem "$docsTemp\*.md" |
  Where-Object { $_.Name -ne "CLAUDE.md" } |
  Copy-Item -Destination ".\docs\redesign" -Force
```

Confirm:

```powershell
Get-ChildItem .\CLAUDE.md
Get-ChildItem .\docs\redesign
```

## 6. Commit documentation separately

```powershell
git add CLAUDE.md docs/redesign
git diff --cached --check
git commit -m "docs: add website redesign specification"
```

## 7. Run the baseline build

The repository overview documents helper scripts intended for WSL.

From PowerShell with WSL available:

```powershell
wsl bash -lc "cd '$(wslpath -a "$repo")' && bash bin/build"
```

If the quoting above is problematic, open WSL directly and run:

```bash
cd /mnt/c/Users/david/path/to/fiorotto8.github.io
bash bin/build
```

Alternative direct Jekyll command from the configured environment:

```bash
bundle exec jekyll build --config _config.yml,_config.dev.yml
```

Use the command that already works for the repository. Do not change dependencies merely to avoid using the existing environment.

## 8. Start Claude Code

From the repository root:

```powershell
claude
```

The current local Claude Code configuration routes model requests to the local endpoint. The redesign workflow does not depend on a specific hosted model, but the prompts are intentionally strict because the implementation model may be less reliable at design judgement.

## 9. First prompt

Open:

```powershell
Get-Content .\docs\redesign\CLAUDE_CODE_PROMPTS.md
```

Copy only `Prompt 0 — Baseline and plan validation` into Claude Code.

Do not start with the homepage prompt.

## 10. Review after every phase

Useful commands:

```powershell
git status --short
git diff --stat
git diff
git diff --check
```

Run the local development server through WSL:

```bash
bash bin/dev
```

Then open:

```text
http://localhost:4000
```

Review at least:

- homepage;
- relevant edited page;
- navigation;
- mobile responsive mode.

## 11. Commit a reviewed phase

Example:

```powershell
git add _layouts/portfolio-page.html _sass/_site-refresh.scss assets/css/main.scss
git diff --cached --check
git commit -m "redesign: add portfolio page shell"
```

Do not use `git add .` without first reviewing `git status --short`.

## 12. Undo an uncommitted phase

To discard changes to a specific file:

```powershell
git restore path\to\file
```

To discard all uncommitted tracked changes:

```powershell
git restore .
```

Use with care. This does not remove untracked files.

To remove an untracked file deliberately:

```powershell
Remove-Item path\to\untracked-file
```

Do not use broad clean commands such as `git clean -fd` unless you have inspected every untracked path.

## 13. Compare with master

```powershell
git diff master...HEAD --stat
git log --oneline --decorate master..HEAD
```

## 14. Push only after review

```powershell
git push -u origin redesign/technical-portfolio-2026
```

Open a draft pull request. Do not merge until the mandatory QA items pass.

## 15. Recommended interaction pattern with the local model

Use one narrowly scoped task.

Good:

> Implement Phase 3 only. Modify the research page and the redesign SCSS. Stop after the build report.

Bad:

> Make the whole website modern, funny, responsive, fast, and deploy it.

When a result is wrong:

1. identify the exact component;
2. state the acceptance criterion it violates;
3. ask for a minimal correction;
4. prohibit unrelated edits.

Example:

```text
The mobile project cards violate I01 because the page scrolls horizontally at 390 px.
Inspect only the card grid and image sizing in _sass/_site-refresh.scss.
Make the minimum correction, run the build, and stop.
```
