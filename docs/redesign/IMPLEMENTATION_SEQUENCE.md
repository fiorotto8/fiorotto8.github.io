# Implementation Sequence

## Overview

Implement the redesign in eight controlled phases.

Do not combine phases unless the previous phase has been manually reviewed.

Suggested branch:

```text
redesign/technical-portfolio-2026
```

Suggested commit pattern:

```text
redesign: add portfolio page shell
redesign: rebuild homepage
redesign: restructure research page
redesign: refresh publications and talks
redesign: refresh teaching and CV
redesign: fix profile and navigation
perf: optimise website images
qa: address responsive and accessibility issues
```

---

## Phase 0 — Repository preparation

### Goal

Create a safe working branch and install the documentation.

### Actions

1. Confirm working tree status.
2. Update `master` with fast-forward only.
3. Create the redesign branch.
4. Copy:
   - `CLAUDE.md` to repository root;
   - all other package documents to `docs/redesign/`.
5. Build the current site before any changes.
6. Record the baseline build result.

### No design files changed in this phase

### Acceptance criteria

- branch exists;
- documentation is present;
- baseline build succeeds or existing errors are documented;
- no source changes yet.

---

## Phase 1 — New page shell and design foundation

### Goal

Create an isolated full-width layout and additive design system without rewriting page content.

### Create

- `_layouts/portfolio-page.html`
- `_sass/_site-refresh.scss`

### Modify

- `assets/css/main.scss`

### Recommended layout

The new layout should:

- inherit from `default`;
- preserve the existing masthead and footer;
- omit the sidebar;
- render one main content container;
- include semantic `main`;
- support page-specific content classes.

Conceptual structure:

```html
---
layout: default
---

<div class="site-shell">
  <main class="site-content" id="main-content">
    {{ content }}
  </main>
</div>
```

Check whether the inherited masthead already provides a skip link before adding another.

### SCSS foundation

Implement:

- colour variables;
- typography;
- width constraints;
- section spacing;
- buttons;
- cards;
- tags;
- focus states;
- reduced-motion rules;
- desktop/tablet/mobile breakpoints.

Do not yet restyle every inherited component.

### Acceptance criteria

- Jekyll build passes;
- a temporary test page can use the new layout;
- no existing live page has changed visually unless intentionally switched;
- SCSS compiles;
- no global horizontal overflow.

---

## Phase 2 — Homepage rebuild

### Goal

Replace the text-heavy homepage with a modern visual hierarchy.

### Modify

- `_pages/about.md`

### Optional create

- `_includes/featured-project-card.html`

Only create an include if it meaningfully reduces repetition without making Liquid more fragile. Static HTML in the page is acceptable.

### Content source

Use `PAGE_COPY_DRAFTS.md`, Homepage section.

### Required sections

- hero;
- status strip;
- current research cards;
- earlier detector programmes;
- selected work;
- teaching teaser;
- contact block.

### Required image decision

Select one fixed profile image from `images/profile/`.

Criteria:

- recognisable head-and-shoulders or laboratory portrait;
- good lighting;
- no distracting crop;
- suitable for a professional research website;
- consistent on mobile.

Do not keep random rotation.

The actual randomisation code is removed in Phase 6 unless required earlier to prevent it from appearing.

### Text reduction target

The homepage prose should be approximately 35–50% shorter than the current total word count.

### Humour limit

Maximum two playful lines.

### Acceptance criteria

- hero communicates role and research within the first viewport;
- fixed image;
- no duplicated “Start Here” list;
- buttons work;
- cards link to research anchors;
- no more than two playful lines;
- mobile layout works at 390 px.

---

## Phase 3 — Research page restructure

### Goal

Create hierarchy between principal current work, emerging R&D, and previous projects.

### Modify

- `_pages/portfolio.html`

### Use

- the new layout;
- the exact anchors in the master specification;
- existing images unless a replacement is clearly superior.

### Required structure

- page introduction;
- Current research:
  - CYGNO04 featured;
  - X-ray polarimetry;
  - new R&D;
- Previous projects:
  - PICOSEC;
  - CMS GEM.

### Required presentation

Each project contains:

- status label;
- title;
- objective;
- image;
- role;
- up to three bullets;
- tags or links.

### Humour limit

Maximum two playful lines or captions across the entire page.

### Acceptance criteria

- CYGNO04 is visually dominant;
- current and previous work are clearly separated;
- all five research areas remain represented;
- no scientific content is invented;
- no more than three bullets per project;
- all images have descriptive alt text;
- research anchors work.

---

## Phase 4 — Publications and talks

### Goal

Reduce repetitive copy and make long lists easier to scan.

### Modify

- `_pages/publications.md`
- `_pages/talks.html`

### Publications actions

- switch to new layout;
- create metrics panel;
- retain verified numbers and date;
- retain Scopus, ORCID, and CV links;
- remove humorous annotation below every publication;
- preserve all current publication links;
- use compact, accessible entries.

### Talks actions

- switch to new layout;
- add featured talks;
- sort complete list reverse chronologically;
- preserve type labels;
- keep posters separate;
- add links only when verified.

### Humour limit

- Publications: one playful sentence maximum.
- Talks: one playful sentence maximum.

### Acceptance criteria

- no publication link lost;
- no official title modified;
- publications page is visibly shorter;
- talks are sorted;
- talk types remain accurate;
- mobile lists remain readable.

---

## Phase 5 — Teaching and CV

### Goal

Make teaching more visual and the CV page more usable.

### Modify

- `_pages/teaching.html`
- `_pages/cv.md`

### Teaching actions

- switch to new layout;
- retain the two images;
- create four activity cards;
- reduce paragraph length;
- retain supervision, teaching, outreach, and service information;
- use no more than two playful lines.

### CV actions

- switch to new layout;
- add clear download/open controls;
- preserve the embedded PDF if it is usable;
- add mobile fallback;
- do not modify `files/CV.pdf`.

### Acceptance criteria

- teaching page has four clear areas;
- captions are readable;
- CV download works;
- PDF opens in a new tab;
- mobile users are not forced to use an unusable embed.

---

## Phase 6 — Navigation, metadata, and profile cleanup

### Goal

Apply the new identity consistently and remove obsolete presentation behaviour.

### Modify

- `_data/navigation.yml`
- `_config.yml`
- `_includes/author-profile.html`
- possibly `_sass/_masthead.scss`
- possibly `_sass/_sidebar.scss`

### Navigation actions

- keep five primary links;
- use `Teaching` as the compact navigation label;
- verify active states;
- ensure mobile menu is usable.

### Metadata actions

- update site description if needed;
- update short author bio;
- add page-specific excerpts through page front matter;
- do not add unverified social profiles;
- do not expose new personal data.

### Profile actions

- remove random image JavaScript;
- use one fixed profile image;
- keep author-profile include simple for legacy pages;
- no primary redesigned page should show the old sidebar.

### Acceptance criteria

- no random profile image;
- all nav links work;
- navigation fits at common desktop widths;
- mobile menu works;
- metadata remains accurate.

---

## Phase 7 — Image optimisation

### Goal

Improve load performance without breaking scientific figures.

### Scope

Start with images actually used on the redesigned main pages.

### Actions

1. Inventory file dimensions and sizes.
2. Identify:
   - hero portrait;
   - homepage project images;
   - research images;
   - teaching images.
3. Preserve originals during processing.
4. Convert photographic images to WebP where safe.
5. Resize to realistic display dimensions.
6. Update references.
7. Add:
   - `loading="lazy"` below the fold;
   - `decoding="async"`;
   - explicit width/height or aspect ratio where practical.
8. Do not recompress plots or diagrams until visual labels have been checked.

### Filename cleanup

Where safe, use `git mv` to fix obvious filename errors, including polarimetry image names. Update all references in the same commit.

### Target sizes

- profile/hero: under 300 KB;
- ordinary photographs: under 250 KB;
- plots/diagrams: retain sufficient resolution for labels;
- never degrade a scientific figure merely to hit an arbitrary target.

### Acceptance criteria

- no broken images;
- visually acceptable quality;
- meaningful reduction in transferred image size;
- no lazy loading of the above-the-fold hero;
- no layout shift from missing dimensions.

---

## Phase 8 — QA and deployment preparation

### Goal

Resolve defects and prepare a reviewable pull request.

### Run

- production Jekyll build;
- `git diff --check`;
- internal-link review;
- responsive browser review;
- keyboard navigation;
- focus visibility;
- alt-text review;
- humour-budget review;
- content accuracy review;
- image-size review.

### Recommended manual viewport checks

- 1440 × 900
- 1024 × 768
- 768 × 1024
- 390 × 844

### Deployment

Do not push directly to `master` during implementation.

Preferred:

1. push redesign branch;
2. open draft pull request;
3. review deployed preview if available;
4. merge after acceptance.

### Acceptance criteria

Every mandatory item in `QA_ACCEPTANCE_CHECKLIST.md` passes or is explicitly documented as an accepted exception.
