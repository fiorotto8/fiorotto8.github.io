# fiorotto8.github.io

Personal academic website built with Jekyll and the
[academicpages](https://github.com/academicpages/academicpages.github.io)
template.

## Local Setup

Install Ruby, Bundler, and Node.js if they are not already available:

```bash
sudo apt install ruby-dev ruby-bundler nodejs
```

Then install the site dependencies locally:

```bash
bash bin/setup
```

The setup script installs gems into `vendor/bundle`, so it does not need `sudo`.
It also clears empty proxy environment variables that can confuse RubyGems in
this WSL setup.

## Run Locally

```bash
bash bin/dev
```

Open http://127.0.0.1:4000/ in your browser. Jekyll watches the source files and
rebuilds automatically as you edit.

To run a one-off build:

```bash
bash bin/build
```

## What To Edit First

- `_config.yml`: site title, author details, social links, repository URL.
- `_pages/about.md`: homepage content.
- `_data/navigation.yml`: top navigation links.
- `_publications/`, `_talks/`, `_teaching/`, `_portfolio/`, `_posts/`: content collections.
- `files/`: PDFs and downloadable files.
- `images/profile.png`: sidebar profile image.
- `images/profile/`: rotating sidebar/profile photos.
- `images/research/<section>/`: square images used on the Research page.
- `images/teaching/`: images used on Teaching & Outreach.

## Refreshing The CV Pages

For a future refresh, place the latest CV files in:

- `files/CV.pdf` for the public downloadable CV.
- `files/cv.tex` for local content extraction.

Then ask Codex to rebuild the website pages from the CV. The TeX source is
ignored by git on purpose, so the public site publishes the PDF but not the raw
source.

## Publishing Later

This repository is already configured for the GitHub Pages user-site URL
`https://fiorotto8.github.io`. When the content is ready, commit the changes and
push `master` to `origin`.

## Template Notes

This site was forked from academicpages, which was forked from the
[Minimal Mistakes Jekyll Theme](https://mmistakes.github.io/minimal-mistakes/).
See `LICENSE` for license details.
