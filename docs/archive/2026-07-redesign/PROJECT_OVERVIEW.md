> Historical document. Superseded by the September 2026 request; see `/AGENTS.md` and `/docs/WEBSITE_REVIEW.md`.

# Project Overview — fiorotto8.github.io

> Personal academic website for **Davide Fiorina**, postdoctoral researcher at GSSI/LNGS.

---

## 1. What This Is

A **personal academic website** hosted on GitHub Pages at `https://fiorotto8.github.io`. It showcases research, publications, talks, teaching, and CV — all driven by Markdown/HTML content, no backend needed.

**Technology stack:**
- **Jekyll** (static site generator) — powered by the `github-pages` Ruby gem
- **academicpages** theme (fork of **Minimal Mistakes** Jekyll Theme by Michael Rose)
- **SCSS** for styling (Susy grid + Breakpoint mixins)
- **Font Awesome 5** + **Academicons** for icons
- **Kramdown** for Markdown processing, **Rouge** for syntax highlighting
- Deployed automatically by **GitHub Pages** on every push to `master`

---

## 2. Directory Structure

```
fiorotto8.github.io/
├── _config.yml              # Main site configuration (author, URLs, plugins, collections)
├── _config.dev.yml          # Local dev overrides (localhost URL, no analytics)
├── Gemfile                  # Ruby dependencies (github-pages, jekyll plugins)
├── .gitignore               # Excludes _site/, vendor/, cv.tex, caches
├── README.md                # Quick-start guide for local setup
├── LICENSE                  # MIT license (from Minimal Mistakes)
│
├── bin/                     # Local development scripts (WSL-friendly)
│   ├── setup                # bundle config + install into vendor/bundle
│   ├── dev                  # jekyll serve --livereload on port 4000
│   └── build                # One-off jekyll build
│
├── _pages/                  # Site pages (nav items + internal templates)
│   ├── about.md             # Homepage (permalink: /) — bio + current work
│   ├── cv.md                # CV page with embedded PDF
│   ├── publications.md      # Selected publications list (hand-curated)
│   ├── talks.html           # Talks and posters list
│   ├── teaching.html        # Teaching, supervision, outreach, scientific service
│   ├── portfolio.html       # Research page (permalink: /research/) — galleries + descriptions
│   ├── 404.md               # Not found page
│   ├── sitemap.md           # Sitemap
│   └── (archive pages)      # Tag/category/year archives — excluded from build
│
├── _data/
│   └── navigation.yml       # Top navigation bar links
│
├── _layouts/                # Jekyll layout templates
│   ├── default.html, single.html, archive.html, splash.html, talk.html
│   └── compress.html        # HTML compression wrapper
│
├── _includes/               # Reusable partials
│   ├── author-profile.html  # ⭐ CUSTOMIZED — random profile photo + GSSI logo
│   ├── sidebar.html, masthead.html, footers, head, scripts, SEO
│   └── (analytics, comments, social share providers)
│
├── _sass/                   # SCSS partials
│   ├── _page.scss           # ⭐ CUSTOMIZED — research-gallery + teaching-gallery CSS
│   ├── _sidebar.scss        # ⭐ CUSTOMIZED — employer logo styling
│   ├── _variables.scss      # Colors, fonts, breakpoints (mostly template defaults)
│   └── vendor/              # Breakpoint, Susy, Font Awesome, Magnific Popup
│
├── assets/
│   ├── css/main.scss        # Entry point — imports all _sass partials
│   ├── css/collapse.css     # Accordion/collapsible content styling
│   ├── js/                  # jQuery plugins (navigation, videos, lightbox, smooth scroll)
│   └── fonts/               # Font Awesome + Academicons font files
│
├── images/
│   ├── profile.png          # Fallback avatar (exists but overridden by random rotation)
│   ├── gssi-logo.png        # Employer logo in sidebar
│   ├── profile/             # Profile photo pool for random rotation ⭐
│   │   ├── P8100200.JPG, PXL_*.jpg, profile_*.jpeg, WhatsApp Image*.jpeg, a.jpeg
│   │   └── not-to-use/      # Photos flagged as not suitable
│   ├── research/            # Research page images organized by sub-project ⭐
│   │   ├── cygno/           # CYGNO04 dark matter detector photos
│   │   ├── xray-polarimetry/# X-ray polarimetry test + sketch images
│   │   ├── picosec/         # PICOSEC Micromegas test-beam + timing results
│   │   ├── cms-gem/         # CMS GEM detector tests (GIF++, magnet)
│   │   └── R&D/             # Super-K, EXPO satellite, CEvNS concept images
│   └── teaching/            # Teaching & outreach photos
│       ├── DRD1-school.png
│       └── public-talk.png
│
├── files/
│   ├── CV.pdf               # Downloadable CV (embedded on /cv/)
│   └── cv.tex               # Raw TeX source — git-ignored, local-only
│
├── _posts/                  # Blog posts collection — EMPTY (no blog content)
├── _publications/           # Publications collection — EMPTY (hand-curated in publications.md instead)
├── _talks/                  # Talks collection — EMPTY (hand-written in talks.html instead)
├── _teaching/               # Teaching collection — EMPTY (hand-written in teaching.html instead)
└── _portfolio/              # Portfolio collection — EMPTY (research in portfolio.html instead)

(_site/ is the generated output, git-ignored.)
```

---

## 3. How It Works

### Build Pipeline

```
Source files (*.md, *.html, _config.yml)
        │
        ▼
  Jekyll processes with:
    • Kramdown (Markdown → HTML)
    • Liquid templating (_layouts, _includes)
    • SCSS compilation (_sass → CSS)
    • Collections expansion (_posts, _publications, etc.)
        │
        ▼
  _site/ (flat static HTML + assets)
        │
        ▼
  GitHub Pages serves at https://fiorotto8.github.io
```

### Local Development (WSL)

The `bin/` scripts are designed for a **WSL environment** on Windows:

| Command | What it does |
|---------|-------------|
| `bash bin/setup` | Installs Ruby gems into `vendor/bundle`, clears proxy vars |
| `bash bin/dev` | Starts Jekyll server with live-reload on `localhost:4000` |
| `bash bin/build` | One-off production build |

All three scripts unset `HTTP_PROXY`/`HTTPS_PROXY`/`NO_PROXY` to avoid RubyGems issues in WSL. They also load `_config.dev.yml` which overrides the URL to localhost and disables analytics.

### Deployment

1. Commit changes to `master` branch
2. Push to GitHub (`fiorotto8/fiorotto8.github.io`)
3. GitHub Pages detects the push and rebuilds automatically
4. Site is live at `https://fiorotto8.github.io` within ~1-2 minutes

No CI/CD pipeline needed — GitHub Pages builds user sites natively.

### Key Custom Features

#### Random Profile Photo Rotation
The sidebar avatar picks a random photo from `images/profile/` on each page load. This is implemented in `_includes/author-profile.html` with inline JavaScript that scans all files in that directory at build time and randomly selects one at runtime.

#### Research Gallery Layout
Custom CSS classes `.research-gallery`, `.teaching-gallery`, and `.research-activity` define grid-based image galleries with hover effects, figcaption captions, and responsive breakpoints. The `--three` variant creates a 3-column layout. `.figure-contain` switches from `cover` to `contain` object-fit for diagrams.

#### Employer Logo in Sidebar
The GSSI logo (`images/gssi-logo.png`) appears next to the employer name in the author profile sidebar, linking to a Google Maps location.

---

## 4. Content Strategy

### What's Used vs What's Not

| Jekyll Collection | Used? | Notes |
|-------------------|-------|-------|
| `_pages/` | **Yes** | All main pages live here |
| `_posts/` | **No** | Empty — no blog functionality |
| `_publications/` | **No** | Empty — publications are hand-written in `publications.md` |
| `_talks/` | **No** | Empty — talks are hand-written in `talks.html` |
| `_teaching/` | **No** | Empty — teaching content is hand-written in `teaching.html` |
| `_portfolio/` | **No** | Empty — replaced by `portfolio.html` (Research page) |

The site deliberately avoids Jekyll's collection-based content management and instead uses **hand-crafted Markdown pages**. This gives full control over presentation but means every publication, talk, or teaching entry is written manually.

### Excluded from Build
Many template files are in `_config.yml`'s `exclude` list: archive pages, demo portfolio items, the markdown generator script, and development tooling. They exist for reference but never appear on the live site.

---

## 5. Configuration Highlights

From [_config.yml](_config.yml):

| Setting | Value | Purpose |
|---------|-------|---------|
| `url` | `https://fiorotto8.github.io` | Public site URL |
| `baseurl` | `""` | No subpath prefix |
| `timezone` | `Europe/Rome` | Correct date handling |
| `future: true` | Yes | Allows dated future posts (e.g., upcoming talks) |
| `comments` | Disabled | No comment system active |
| `analytics` | Disabled | No tracking configured |
| `talkmap_link` | false | No interactive talk map |

Author links that **are configured**: email, GitHub, Scopus, ORCID.
Social links that are **empty**: Twitter, LinkedIn, Facebook, etc.

---

## 6. Git History Context

The repository is a fork of [academicpages](https://github.com/academicpages/academicpages.github.io), which itself forks [Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/). The upstream history (200+ commits) represents the community template evolution.

**User-specific changes** (6 commits on top of the fork):
1. `8e37504` — First commit: initial personalization
2. `7d61c6e` — Test iteration
3. `7415354` — "Finally added my stuff": full content population (all pages, images, CV)
4. `9fbbde0` — "betetr": refinements
5. `fe980db` — "even_nicer": final polish

These commits removed all placeholder template content (demo posts, sample publications, example talks) and replaced everything with real content across ~73 files.

---

## 7. Known Issues & Improvement Opportunities

### Image Management (High Impact)

- **Uncompressed uploads:** Many images are full-resolution phone photos (1–5 MB each). `images/research/cygno/LIME-decommissioning.jpg` is 5.2 MB, `images/research/picosec/picosec-testbeam.png` is 4.3 MB, and several profile JPGs exceed 2 MB. These load slowly for visitors, especially on mobile.
  - **Fix:** Compress all images before uploading. Use tools like `mozjpeg`, `oxipng`, or Squoosh. Target: <200 KB for research photos, <100 KB for profile images. Consider WebP format with fallbacks.

- **Profile photo cleanup:** The `images/profile/` directory contains 16 files including WhatsApp exports, misspelled names (`WhaatsApp`, `Imagaae`, `a.jpeg`), and a `not-to-use/` subdirectory. The random rotation script includes ALL files in the root level, even unsuitable ones like `a.jpeg`.
  - **Fix:** Delete unused photos. Rename remaining files with clear, descriptive names. Move or delete the `not-to-use/` directory entirely (it's still indexed by git).

- **Typos in filenames:** `poalrimetry-test.jpg` → `polarimetry`, `polarimetry-schetck.png` → `sketch`.
  - **Fix:** Rename files and update references in `portfolio.html`.

### SEO & Accessibility (Medium Impact)

- **No meta descriptions per page:** The site uses a single `description` from `_config.yml`. Each page could have its own `excerpt` or `description` for better search results.
- **No Open Graph / Twitter Card images:** `og_image` in `_config.yml` is empty. Social shares show no preview image.
- **Social profiles incomplete:** LinkedIn and Twitter handles are blank in `_config.yml`. Adding them improves discoverability.
- **404 page uses Google FixURL script** which loads an external JavaScript — deprecated and slow. Consider a simpler custom 404 with search suggestions.

### Structure & Maintenance (Medium Impact)

- **No blog, but blog infrastructure exists:** `_posts/` is empty, yet the config sets up pagination, related posts, read time, comments, and sharing for posts. This adds unnecessary complexity to the build.
  - **Fix:** Remove blog-related defaults from `_config.yml` and exclude unused archive pages.

- **Hand-written publications & talks:** Currently maintained as plain lists in Markdown. Works fine for now but becomes tedious as the count grows (already 16 selected publications, 24 talks, 12 posters).
  - **Future option:** Adopt a `_publications/` collection with YAML frontmatter for sorting, filtering, or auto-generating from BibTeX (the template already has a `markdown_generator` script for this).

- **CV pages are static:** The CV is embedded as a PDF. The README mentions a future plan to regenerate CV pages from `cv.tex`, but this pipeline doesn't exist yet.
  - **Future option:** Use the `markdown_generator` approach or a simple Python script to extract sections from TeX and generate Markdown.

### Performance (Low-Medium Impact)

- **No image lazy loading:** All images load eagerly. Adding `loading="lazy"` to below-the-fold images improves initial page load.
- **No CDN for assets:** GitHub Pages serves files from a single region. For an academic CV site this is fine, but could be improved with Cloudflare or similar.
- **Font Awesome loaded entirely:** The full FA5 library is included. Only a subset of icons are used (envelope, map-marker, github, database, orcid, link). Could reduce by loading only needed icons.

### Security & Privacy (Low Impact)

- **Email exposed in plaintext** in `_config.yml` and rendered as `mailto:` — susceptible to scraping. Consider obfuscation or a contact form.
- **No HTTPS enforcement** in config — GitHub Pages redirects automatically, but no `Strict-Transport-Security` header is set.

### Nice-to-Have Enhancements

- Add a **search function** (e.g., Simple-Jekyll-Search) for publications and talks.
- Add an **RSS feed** with actual content (currently configured via `jekyll-feed` plugin but has no posts to feed).
- Configure **analytics** (Privacy-friendly options: Plausible, Umami, or fathom.dev — lightweight and GDPR-compliant).
- Add **structured data** (JSON-LD) for Person/Publication schemas — helps Google display rich results.
- Consider a **dark mode toggle** — the SCSS variables make this achievable.

---

## 8. Quick Reference: Editing Guide

| To change... | Edit this file |
|--------------|----------------|
| Site title, author info, social links | `_config.yml` |
| Top navigation bar | `_data/navigation.yml` |
| Homepage bio & current work | `_pages/about.md` |
| Research sections with images | `_pages/portfolio.html` + `images/research/` |
| Selected publications | `_pages/publications.md` |
| Talks and posters | `_pages/talks.html` |
| Teaching & outreach | `_pages/teaching.html` |
| CV PDF | Replace `files/CV.pdf` |
| Sidebar profile photos | Add/remove files in `images/profile/` |
| Colors, fonts, breakpoints | `_sass/_variables.scss` |
| Gallery layout styles | `_sass/_page.scss` (bottom section) |

---

## 9. Dependencies

```
Ruby gems:
  github-pages        → Jekyll + GitHub-compatible plugins
  jekyll-feed         → Atom/RSS feed generation
  jekyll-sitemap      → sitemap.xml generation
  jekyll-gist         → GitHub gist embedding
  jekyll-redirect-from → URL redirects in frontmatter
  jemoji              → Emoji rendering (whitelist only)
  hawkins             → Linter for Jekyll sites

JavaScript:
  jQuery 1.12.4       → DOM manipulation
  magnific-popup      → Image lightbox gallery
  smooth-scroll       → Anchor link scrolling
  greedy-navigation   → Responsive navbar collapse
  stickyfill          → Sticky sidebar fallback
```

---

*Generated on 2026-07-21. Based on commit `fe980db` (branch: master).*
