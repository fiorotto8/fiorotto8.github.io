# Website Redesign Master Specification

## 1. Product goal

Create a personal academic website that quickly answers five questions:

1. Who is Davide Fiorina?
2. What detector and instrumentation problems does he work on?
3. What is he responsible for now?
4. What has he produced?
5. How can a collaborator, hiring committee, student, or organiser contact him or obtain his CV?

The website should communicate competence first and personality second. Personality must remain visible, but not compete with every scientific statement.

## 2. Primary audiences

### Scientific collaborators

Need:

- current projects;
- detector expertise;
- technical responsibilities;
- relevant papers and talks;
- contact information.

### Hiring and selection committees

Need:

- a clear research identity;
- leadership and coordination roles;
- evidence of independent technical responsibility;
- selected high-value outputs;
- CV access.

### Students and early-career researchers

Need:

- understandable descriptions of the research;
- teaching and supervision activities;
- a sense of the person behind the work.

### Conference and workshop organisers

Need:

- speaking topics;
- previous talks;
- concise biography;
- contact and CV.

## 3. Brand position

### One-line description

> Experimental particle and astroparticle physicist developing gaseous detectors and optical TPCs for rare-event searches, X-ray polarimetry, and precision timing.

### Personality

- technically direct;
- curious;
- hands-on;
- responsible;
- dry humour;
- not self-important;
- comfortable moving between hardware, simulation, operations, and coordination.

### Visual concept

**Dark technical editorial portfolio**

Reference qualities, not copied websites:

- scientific instrument documentation;
- clean research magazines on dark backgrounds;
- modern laboratory websites with deep charcoal surfaces;
- concise design portfolios;
- strong use of photography and whitespace.

The site uses a fixed dark theme based on deep blue-charcoal surfaces, not pure black. No theme toggle is implemented.

## 4. Information architecture

Keep the existing public structure:

- Home
- Research
- Publications
- Talks
- Teaching
- CV

Recommended navigation labels:

- `Research`
- `Publications`
- `Talks`
- `Teaching`
- `CV`

Use `Teaching` in the navigation and `Teaching & Outreach` as the page heading.

The homepage logo/name should link to `/`.

## 5. Homepage architecture

Order:

1. Masthead
2. Hero
3. Current status strip
4. Featured research
5. Previous detector work
6. Selected outputs
7. Teaching/outreach teaser
8. Contact/footer

### Hero

Left column:

- small category line;
- name;
- one-sentence research identity;
- current role;
- two or three action buttons;
- one optional human line.

Right column:

- one fixed portrait or strong laboratory image;
- simple caption if useful;
- no rotation.

Primary actions:

- `Explore research`
- `Download CV`
- optional secondary text link: `Contact`

### Current status strip

A compact band with three items:

- `Now — CYGNO04 integration and commissioning`
- `Also — optical TPCs for X-ray polarimetry`
- `Based at — GSSI / LNGS, L'Aquila`

This strip should remain factual.

### Featured research

Three cards:

1. CYGNO04
2. X-ray polarimetry
3. New detector concepts

Each card contains:

- image;
- title;
- one-sentence aim;
- one-sentence role;
- up to three tags;
- link to a research-page anchor.

### Previous detector work

Two compact horizontal entries:

- CMS GEM detectors
- PICOSEC Micromegas

The homepage should not reproduce the full project descriptions.

### Selected outputs

Maximum five items:

- three papers;
- two talks or one talk and one poster.

This section is a preview, not a duplicate of the publications page.

## 6. Research page architecture

Page introduction: 50–80 words.

### Current research

Order:

1. CYGNO04
2. Optical TPCs for X-ray polarimetry
3. New R&D: neutrinos, CEvNS, and space instrumentation

### Previous projects

Order:

1. PICOSEC timing
2. CMS GEM detectors

### Project block structure

Each project should use:

- project status label;
- title;
- one-sentence scientific objective;
- one strong image;
- `My role`;
- `Current focus` or `What I worked on`;
- maximum three bullets;
- selected links;
- up to three tags.

CYGNO04 may use a larger featured layout.

Suggested anchors:

- `#cygno04`
- `#xray-polarimetry`
- `#new-rd`
- `#picosec`
- `#cms-gem`

## 7. Publications page architecture

1. Page heading and short introduction
2. Compact metrics panel
3. External profile links
4. Selected publications
5. Link to complete CV

### Metrics panel

Show:

- publication count;
- citations;
- h-index;
- source and update date.

Do not embellish these numbers with jokes.

### Publication entry

Required:

- year;
- title;
- journal or preprint status if available;
- DOI/arXiv link;
- optional factual contribution line.

Do not include a playful line under every entry.

Optional tags:

- CYGNO
- X-ray polarimetry
- PICOSEC
- CMS GEM
- detector R&D

Do not add client-side filtering in the first release.

## 8. Talks page architecture

1. Heading
2. One short introduction
3. Featured talks, maximum four
4. Complete reverse-chronological list
5. Posters subsection

Each list item should distinguish:

- title;
- event;
- location;
- year;
- type: invited, plenary, parallel, poster;
- link if available.

No invented slide links.

## 9. Teaching page architecture

1. Heading and concise introduction
2. Two-image gallery
3. Four cards:
   - Student supervision
   - Laboratory teaching
   - Outreach
   - Scientific service
4. Contact or invitation line

This page may carry slightly more personality than the research pages.

## 10. CV page architecture

1. Heading
2. One-sentence description
3. Primary `Download CV` button
4. Secondary `Open PDF` link
5. Embedded PDF on desktop if reliable
6. Mobile fallback message and direct link

No sidebar.

## 11. Design system

### Colour tokens

Use these as the starting palette:

```scss
body.portfolio-theme {
  --refresh-bg: #0b1117;
  --refresh-surface: #121b24;
  --refresh-surface-raised: #18232e;
  --refresh-surface-soft: #0f1820;

  --refresh-text: #edf3f6;
  --refresh-muted: #a6b2bd;
  --refresh-subtle: #7f8d98;

  --refresh-border: #293743;
  --refresh-border-strong: #3a4b59;

  --refresh-accent: #55c2c3;
  --refresh-accent-hover: #79d4d3;
  --refresh-accent-dark: #248f96;

  --refresh-warm: #ef8065;
  --refresh-dark: #071015;
  --refresh-dark-text: #f7fafb;
}
```

Rules:

- teal (`#55c2c3`) is the principal interactive accent;
- warm coral (`#ef8065`) is used rarely for labels or small visual emphasis;
- do not use both accent colours in every component;
- page background is deep blue-charcoal (`#0b1117`), never pure black;
- cards and content surfaces use layered dark surfaces (`--refresh-surface`, `--refresh-surface-raised`);
- status strips, footer, or focused areas may use `--refresh-dark`;
- links must remain clearly identifiable using underline or border treatment, not colour alone.

### Typography

Avoid adding a required external font dependency in the first release.

Recommended stack:

```scss
$refresh-sans:
  Inter,
  ui-sans-serif,
  -apple-system,
  BlinkMacSystemFont,
  "Segoe UI",
  Roboto,
  Helvetica,
  Arial,
  sans-serif;

$refresh-mono:
  "SFMono-Regular",
  Consolas,
  "Liberation Mono",
  monospace;
```

Use:

- sans-serif for all primary text;
- monospace only for small technical labels or project status;
- no serif captions in the redesign.

Suggested scale:

```scss
--text-xs: clamp(0.75rem, 0.72rem + 0.1vw, 0.82rem);
--text-sm: clamp(0.88rem, 0.84rem + 0.15vw, 0.98rem);
--text-base: clamp(1rem, 0.96rem + 0.2vw, 1.12rem);
--text-lg: clamp(1.2rem, 1.1rem + 0.4vw, 1.45rem);
--text-xl: clamp(1.65rem, 1.4rem + 1vw, 2.25rem);
--text-hero: clamp(2.6rem, 2rem + 3vw, 5rem);
```

### Spacing

Use an 8 px base rhythm.

Suggested tokens:

```scss
--space-1: 0.5rem;
--space-2: 1rem;
--space-3: 1.5rem;
--space-4: 2rem;
--space-5: 3rem;
--space-6: 4.5rem;
--space-7: 6rem;
```

### Widths

```scss
--site-max: 1180px;
--reading-max: 760px;
--wide-reading-max: 920px;
```

### Radius and shadows

```scss
--radius-sm: 8px;
--radius-md: 14px;
--radius-lg: 22px;
--shadow-soft: 0 14px 40px rgba(16, 33, 43, 0.08);
```

Use borders more often than shadows.

### Buttons

Primary button:

- teal accent background;
- dark readable text (sufficiently contrasting);
- medium radius;
- strong focus ring.

Secondary button:

- dark transparent or surface background;
- visible border;
- light text;
- clear hover state.

Do not use pill-shaped buttons for every control.

### Cards

Project cards should:

- use the dark raised surface (`--refresh-surface-raised`) background;
- use a 1 px border (`--refresh-border`);
- use 14–18 px radius;
- avoid heavy shadows and neon glow;
- align content consistently;
- keep images at a stable aspect ratio;
- lift subtly on hover only when motion is permitted.

### Images

- Hero portrait: approximately 4:5.
- Project card images: approximately 16:10 or 3:2.
- Avoid forced square crops for all scientific images.
- Use `object-fit: cover` for photographs.
- Use `object-fit: contain` on dark neutral backgrounds for diagrams.
- Do not apply `filter: invert()` to any image.
- Captions should normally be factual.
- One or two playful captions may remain site-wide per page according to the humour budget.

## 12. Responsive behaviour

### Desktop: 1100 px and above

- two-column hero;
- three-column project grid;
- comfortable whitespace;
- sticky or stable masthead;
- no sidebar.

### Tablet: 700–1099 px

- two-column project grid;
- hero may remain two columns if image and text fit;
- navigation must not overlap;
- reduced section spacing.

### Mobile: below 700 px

- single-column hero;
- image below text;
- single-column cards;
- buttons wrap or stack;
- no horizontal scrolling;
- body padding at least 18 px;
- no content hidden solely because of viewport width.

## 13. Motion

Allowed:

- subtle hover movement of 2–4 px;
- opacity transition;
- underline transition;
- image scale up to 1.02.

Required:

```scss
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    scroll-behavior: auto !important;
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

Not allowed:

- scroll-triggered entrance animations for every section;
- parallax;
- auto-rotating content;
- animated background effects.

## 14. SEO and metadata

For each main page:

- provide a specific `excerpt`;
- use one H1;
- maintain meaningful page titles;
- preserve canonical URLs generated by Jekyll;
- add or configure a default Open Graph image only after a suitable image is selected;
- keep Person structured data from the theme where it remains correct.

Do not expose additional personal information beyond what is already intentionally public.

## 15. Performance targets

Practical goals, not absolute guarantees:

- hero image under 300 KB;
- ordinary project photographs under 250 KB where visually acceptable;
- diagrams under 400 KB;
- no below-the-fold eager image loading;
- no new JavaScript bundle;
- no layout shift caused by random images;
- explicit image aspect ratio or dimensions where practical.

## 16. Non-goals for version 1

Do not include:

- blog;
- search;
- publication filters;
- dark-mode toggle;
- multilingual content;
- automatic BibTeX import;
- automatic CV generation;
- analytics;
- contact form;
- project timeline animations.

These can be separate future projects.

## 17. Definition of success

The redesign succeeds when:

- a visitor can identify the research focus in five seconds;
- CYGNO04 is clearly the principal current project;
- the homepage is at least 35% shorter in text volume;
- the research page is easier to scan;
- humour is visible but no longer repetitive;
- the site looks intentional on desktop and mobile;
- GitHub Pages deployment remains simple;
- the author recognises his own voice.
