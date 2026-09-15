# Davide Fiorina

A single-page academic website built with Jekyll for GitHub Pages.
Pale lilac and ice blue with teal/magenta accents; documentary photographs,
outreach explanations and locally hosted Go fonts.

## Local development

Install Ruby and Bundler, then run:

```bash
bash bin/setup
bash bin/dev
```

Open <http://127.0.0.1:4000/>. No Node or JavaScript build is required.

## Build and check

```bash
bash bin/build --safe
python3 bin/check_site.py
git diff --check
```

`--safe` checks compatibility with the GitHub Pages plugin restrictions.
The Python checker uses only the standard library. `bin/check_browser.py` provides
optional Playwright checks and screenshots. Browser setup and content
review are described in [docs/ART_DIRECTION.md](docs/ART_DIRECTION.md).
The latest [photographic expansion](docs/PHOTOGRAPHIC_EXPANSION.md) covers the
wider layout, light palette, outreach copy and personal photographs.
The subsequent [media-library reorganisation](docs/MEDIA_LIBRARY.md) covers
the current folders, smaller photographs and requested animation players.
The latest [content refinement](docs/CONTENT_REFINEMENT.md) adds the CYGNO
communication links, compact concept figures and four-photo personal gallery.
[Row balance](docs/ROW_BALANCE.md) records the subsequent portrait correction,
column alignment and final photo selection.
The [initial review](docs/WEBSITE_REVIEW.md) records content questions.

## Editing

| File | Purpose |
| --- | --- |
| `_pages/home.html` | All homepage sections and biography |
| `_data/publications.json` | Selected papers; first four shown initially |
| `_data/talks.json`, `_data/posters.json` | Complete talk and poster records |
| `_data/photos.json`, `_includes/photo.html` | Selected responsive photographs |
| `_data/animations.json`, `_includes/animation.html` | Two native animation players, captions and screen-reader descriptions |
| `_data/navigation.yml` | Navigation labels and section IDs |
| `_config.yml` | Identity, contact details, URLs and build exclusions |
| `_layouts/default.html` | Header, page shell and footer |
| `assets/css/main.css` | Palette, typography and responsive layout |
| `assets/js/site.js` | Section tracking, deep links and legacy redirects |
| `files/CV.pdf` | Public CV; replace only when requested |
| `AGENTS.md` | Instructions for Codex and other coding agents |

All sections are on `/`. The old `/research/`, `/publications/`, `/talks/`,
`/teaching/`, `/cv/` and `/resume/` URLs lead to the corresponding section.
They include ordinary fallback links for visitors without JavaScript. Research
fragments are preserved, and links into collapsed sections open those sections.

Publication and talk titles retain their source wording. Original photographs
and scientific figures remain in `images/`; unused renditions are excluded from
the build. `files/cv.tex` remains local and is never published.

See the [image library guide](images/README.md). `images/public/` contains only
referenced assets, organised by identity, personal interests, research project
and teaching. `images/local/` contains originals, unused photographs, larger
source versions and retired exports. It is ignored by Git and excluded from
Jekyll. Keep a separate backup of these local files.

[docs/IMAGE_LIBRARY.json](docs/IMAGE_LIBRARY.json) records the moves and hashes;
[docs/PHOTO_SOURCES.json](docs/PHOTO_SOURCES.json) selects the source versions.
Run `python3 bin/prepare_photos.py` with Pillow to regenerate the selected WebP
sizes. This is optional maintenance; ordinary builds use the public exports.

July's design documents and previous page copy are in `docs/archive/`, excluded
from the site. They are historical records, superseded by `AGENTS.md`.

## Publishing

The existing GitHub Pages destination is <https://fiorotto8.github.io>. Review
content and the local preview before committing and pushing to `origin/master`.
Local development does not publish the site.

## Attribution

The repository began with [AcademicPages](https://github.com/academicpages/academicpages.github.io),
based on [Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/).
The inherited [LICENSE](LICENSE) is retained. It does not establish redistribution
rights for supplied photographs or collaboration figures.
