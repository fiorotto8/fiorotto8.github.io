> Historical document. Superseded by the September 2026 request; see `/AGENTS.md` and `/docs/WEBSITE_REVIEW.md`.

# Complete Website Redesign Package
This combined document contains the core implementation documentation in one file.


---

# Source document: README_FIRST.md

# Davide Fiorina Website Redesign Package

## Purpose

This package is the authoritative implementation guide for redesigning:

- Live site: `https://fiorotto8.github.io/`
- Repository: `fiorotto8/fiorotto8.github.io`
- Platform: Jekyll on GitHub Pages
- Current theme lineage: AcademicPages / Minimal Mistakes

The strategy is intentionally separated from the implementation. The human decision is already made here; Claude Code should execute it rather than invent a new direction.

## Core decision

The new site should be a **modern technical portfolio with a controlled amount of humour**.

It must not become:

- a sterile institutional profile;
- a startup landing page full of slogans;
- a complete rewrite in React, Astro, Next.js, or another framework;
- an AI-generated collection of metaphors;
- a visually noisy page with gradients, animated particles, typewriter text, or excessive motion.

It should feel like:

- an experimental physicist built it;
- the research is serious and technically credible;
- the author has a recognisable personality;
- the page is easy to scan in under one minute;
- deeper details are available without dominating the first screen.

## Documents in this package

1. `CLAUDE.md`  
   Persistent repository instructions. Place this file in the repository root.

2. `CURRENT_SITE_AUDIT.md`  
   What is currently working, what is dated, and what must be preserved.

3. `MASTER_SPEC.md`  
   Product goals, design direction, information architecture, design tokens, and technical constraints.

4. `PAGE_COPY_DRAFTS.md`  
   Proposed wording and humour placement for each main page.

5. `IMPLEMENTATION_SEQUENCE.md`  
   The exact phased implementation order, files to touch, and expected commits.

6. `CLAUDE_CODE_PROMPTS.md`  
   Copy-paste prompts to run one phase at a time in Claude Code.

7. `QA_ACCEPTANCE_CHECKLIST.md`  
   Objective tests that must pass before deployment.

8. `POWERSHELL_SETUP.md`  
   Safe setup and execution instructions for Windows PowerShell.

## Required working method

Do not ask Claude Code to “redesign the whole website” in one prompt.

Use this sequence:

1. Put `CLAUDE.md` in the repository root.
2. Put the other documents under `docs/redesign/`.
3. Create a dedicated branch.
4. Run the prompts in `CLAUDE_CODE_PROMPTS.md` one at a time.
5. Review the browser result after every phase.
6. Commit each phase separately.
7. Merge only after the QA checklist passes.

## Important content principle

The goal is not to remove humour. The goal is to stop every paragraph, caption, and publication from competing to be the funniest line on the page.

Use humour as punctuation:

- factual sentence;
- factual sentence;
- occasional human line;
- back to the science.

The final result should contain fewer jokes, but the jokes that remain should feel more clearly like Davide rather than generic “clever AI” copy.


---

# Source document: CURRENT_SITE_AUDIT.md

# Current Site Audit

## Executive assessment

The current site has strong raw material:

- a clear scientific identity;
- substantial research experience;
- real detector photographs;
- a coherent set of main pages;
- working GitHub Pages deployment;
- hand-curated content that can be edited without a backend.

The main issue is not a lack of content. It is **too much equal-weight content and too much equal-weight personality**.

Almost every block contains a metaphor, joke, or personification. That makes the scientific information harder to scan and creates a synthetic tone even when the individual lines are amusing.

The visual layer also remains recognisably based on an older AcademicPages / Minimal Mistakes academic template:

- persistent author sidebar;
- narrow text column;
- grey default palette;
- inherited typography;
- archive-style page layouts;
- small captions;
- square image grids;
- limited hierarchy between primary and secondary work.

## Current technical structure

Primary files:

- `_pages/about.md` — homepage
- `_pages/portfolio.html` — research
- `_pages/publications.md`
- `_pages/talks.html`
- `_pages/teaching.html`
- `_pages/cv.md`
- `_data/navigation.yml`
- `_config.yml`
- `_includes/author-profile.html`
- `_sass/_variables.scss`
- `_sass/_page.scss`
- `_sass/_sidebar.scss`
- `_layouts/single.html`
- `_layouts/archive.html`

Current stack:

- Jekyll
- GitHub Pages
- Kramdown
- Liquid templates
- SCSS
- inherited Minimal Mistakes / AcademicPages components

This stack is adequate. Replacing it would add risk without solving the core content and design problems.

## Page-by-page findings

### Homepage

Current strengths:

- states the scientific field;
- states the current institution and CYGNO role;
- lists current activities;
- links to all major pages.

Current problems:

- the opening contains several jokes in rapid succession;
- the first paragraph lists many technologies before establishing a simple identity;
- the “Current Work” section mixes strategic priorities with playful asides;
- “Start Here” duplicates the top navigation;
- there is no strong visual hero or featured project hierarchy;
- the rotating sidebar photograph makes personal presentation inconsistent.

Decision:

- replace the current homepage structure;
- use a fixed profile image;
- lead with one clear research sentence and one role sentence;
- show three featured research cards;
- keep only one or two light human lines.

### Research page

Current strengths:

- five meaningful research areas;
- useful laboratory photographs;
- clear technical breadth;
- concrete role descriptions.

Current problems:

- every section has the same visual weight;
- every section repeats the same structure;
- nearly every caption is humorous;
- several paragraphs contain jokes after already humorous captions;
- current and previous work are not visually separated;
- the most important current work, CYGNO04, does not dominate enough;
- long bullet lists reduce scanability.

Decision:

- separate `Current research` and `Previous projects`;
- make CYGNO04 the lead feature;
- use one image per project in the main flow, with optional secondary images;
- show `Goal`, `My role`, and `Focus`;
- keep no more than two humorous lines on the entire page.

### Publications page

Current strengths:

- selected list rather than an unmanageable complete bibliography;
- direct DOI/arXiv links;
- bibliometric information;
- external Scopus and ORCID links.

Current problems:

- each publication has a second joke line;
- the joke lines add length without clarifying contribution;
- all 16 entries are presented as one long numbered list;
- the page does not distinguish first-author or especially relevant work;
- bibliometric numbers visually compete with the selected science.

Decision:

- retain the selected list;
- remove the joke below each paper;
- optionally group by research theme or use compact tags;
- show title, year, venue/link, and a factual one-line contribution only when useful;
- keep one playful introductory line at most.

### Talks page

Current strengths:

- comprehensive list;
- year and event metadata;
- invited/plenary/parallel distinctions.

Current problems:

- the top does not surface the most significant recent talks;
- the list is visually dense;
- entries are not consistently sorted by year;
- there are no direct slide or event links where available;
- the introduction contains more personality than the structure can support.

Decision:

- add a small `Featured talks` area;
- sort the complete list reverse chronologically;
- use a compact metadata layout;
- keep “The suitcase survived. Mostly.” if desired, and remove other competing jokes.

### Teaching & Outreach

Current strengths:

- strong evidence of supervision, teaching, outreach, and service;
- good photographs;
- this is the page where personality is most appropriate.

Current problems:

- jokes appear in the intro, both captions, supervision, and outreach;
- the four sections are text blocks rather than a modern grid;
- there is no quick overview of scale or audience.

Decision:

- retain one humorous caption and one human sentence;
- turn the four areas into cards;
- use concise factual descriptions;
- keep the tone more relaxed than the research and publications pages.

### CV page

Current strengths:

- simple access to the PDF;
- complete information remains available.

Current problems to inspect during implementation:

- embedded PDF behaviour on mobile;
- clarity of download/open actions;
- excessive empty space or inherited sidebar width.

Decision:

- use a clean introduction;
- provide prominent `Download CV` and `Open PDF` actions;
- keep the embedded document only if it remains usable on mobile.

## Cross-site findings

### Random profile image

The author-profile include currently chooses a random image from the profile directory on page load.

Problems:

- visual identity changes unpredictably;
- unsuitable or inconsistent photos may appear;
- page layout can shift;
- it feels less intentional than a fixed portrait.

Decision:

- select one fixed image;
- remove randomisation code;
- keep a simple fallback.

### Image performance

The repository contains several multi-megabyte images. This affects:

- mobile load time;
- Largest Contentful Paint;
- bandwidth;
- responsiveness on slower networks.

Decision:

- optimise only after the layout is stable;
- preserve originals during conversion;
- use appropriately sized WebP files;
- lazy-load below-the-fold images.

### Theme complexity

The repository contains unused blog and collection infrastructure.

Decision:

- do not perform a broad theme cleanup during the visual redesign;
- unused infrastructure can remain if harmless;
- remove only code that directly interferes with the new pages;
- avoid combining redesign and repository archaeology in one branch.

## What must be preserved

- all public URLs;
- all publication links;
- the downloadable CV;
- ORCID, Scopus, GitHub, and email links;
- research images that are still meaningful;
- scientific role accuracy;
- current GitHub Pages deployment;
- the ability to edit pages directly in Markdown/HTML;
- a recognisable personal voice.

## What should disappear

- random profile-photo rotation;
- a joke under every publication;
- a humorous caption under every image;
- repeated “detectors have personalities” language;
- duplicated homepage navigation;
- inherited sidebar on primary pages;
- visually identical treatment of current and historical projects;
- unnecessary technical slogans.

## Risk assessment

### Low risk

- text reduction;
- fixed portrait;
- new layout using the existing default shell;
- additive SCSS partial;
- new page-specific classes;
- navigation label simplification.

### Medium risk

- image renaming;
- image format conversion;
- changing the main layout used by all pages;
- extensive inherited SCSS overrides;
- changing Liquid includes.

### High risk and not recommended

- framework migration;
- deleting inherited theme infrastructure wholesale;
- converting all content to collections in the same redesign;
- adding a JavaScript-heavy filter/search system;
- rewriting publication metadata automatically without validation.


---

# Source document: MASTER_SPEC.md

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

**Technical editorial portfolio**

Reference qualities, not copied websites:

- scientific instrument documentation;
- clean research magazines;
- modern laboratory websites;
- concise design portfolios;
- strong use of photography and whitespace.

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
$refresh-bg: #f6f8fa;
$refresh-surface: #ffffff;
$refresh-text: #17212b;
$refresh-muted: #5f6b76;
$refresh-border: #dce3e8;
$refresh-accent: #007b87;
$refresh-accent-dark: #005e68;
$refresh-warm: #d85b42;
$refresh-dark: #10212b;
$refresh-dark-text: #f4f7f8;
```

Rules:

- teal is the principal interactive accent;
- warm coral is used rarely for labels or small visual emphasis;
- do not use both accent colours in every component;
- body background is light;
- dark colour may be used for a compact footer or status area;
- links must remain clearly identifiable.

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

- accent background;
- white text;
- medium radius;
- strong focus ring.

Secondary button:

- transparent or white;
- border;
- dark text.

Do not use pill-shaped buttons for every control.

### Cards

Project cards should:

- have a white background;
- use a 1 px border;
- use 14–18 px radius;
- avoid heavy shadows;
- align content consistently;
- keep images at a stable aspect ratio;
- lift subtly on hover only when motion is permitted.

### Images

- Hero portrait: approximately 4:5.
- Project card images: approximately 16:10 or 3:2.
- Avoid forced square crops for all scientific images.
- Use `object-fit: cover` for photographs.
- Use `object-fit: contain` on white or neutral backgrounds for diagrams.
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


---

# Source document: PAGE_COPY_DRAFTS.md

# Page Copy Drafts

## Editorial note

These drafts define the intended meaning, order, and tone. Claude Code may adjust punctuation or HTML wrapping, but it must not replace the copy with generic marketing language.

Scientific claims and roles must be checked against the existing site and CV before publication.

The recommended language is British English, except inside official publication and talk titles.

---

# Homepage

## Front matter

Recommended:

```yaml
---
layout: portfolio-page
permalink: /
title: "Davide Fiorina"
excerpt: "Experimental particle and astroparticle physicist developing gaseous detectors and optical TPCs for rare-event searches, X-ray polarimetry, and precision timing."
author_profile: false
---
```

## Hero kicker

> Experimental particle & astroparticle physics

## Hero title

> Davide Fiorina

## Hero lead

> I design, build, and operate gaseous detectors for rare-event searches, X-ray polarimetry, and precision timing.

## Current role

> Postdoctoral researcher at GSSI and Technical Coordinator of CYGNO04 at LNGS.

Before publishing, confirm whether `Site Manager` should also appear in this sentence. Do not add every formal role to the hero.

## Optional human line — keep only this one in the hero

> In practice, this means moving between detector physics, clean-room work, simulation, commissioning, and the occasional cable with strong opinions.

This is one of the homepage’s two permitted playful lines.

## Hero actions

- Explore research
- Download CV
- Contact

## Status strip

### Now

> CYGNO04 detector integration and commissioning

### Also

> Optical TPCs for hard X-ray polarimetry

### Based at

> GSSI and Laboratori Nazionali del Gran Sasso

## Featured research heading

> Current research

Intro:

> My work spans the full detector lifecycle, from concept and simulation to construction, commissioning, operation, and data analysis.

### Card 1 — CYGNO04

Title:

> CYGNO04

Text:

> A 400 L radiopure optical time projection chamber for directional dark-matter searches at LNGS.

Role:

> I coordinate detector integration, installation, commissioning, and the technical interfaces between subsystems.

Tags:

- Optical TPC
- Directional dark matter
- Detector integration

### Card 2 — X-ray polarimetry

Title:

> Optical TPCs for X-ray polarimetry

Text:

> Triple-GEM optical TPCs for reconstructing low-energy photoelectron tracks and measuring polarisation in the 10–60 keV range.

Role:

> I work on detector development, calibration, simulation, and track reconstruction.

Tags:

- Triple-GEM
- Polarimetry
- Track reconstruction

### Card 3 — New detector concepts

Title:

> Neutrinos, CEvNS, and space instrumentation

Text:

> Detector and simulation studies for directional solar neutrinos, coherent neutrino scattering, and future space-based instruments.

Role:

> I develop detector concepts and response simulations, with an emphasis on directional information and low-energy signals.

Tags:

- Neutrinos
- CEvNS
- Space environment

## Previous detector work heading

> Earlier detector programmes

Intro:

> Before CYGNO, I worked on precision timing and on the development, commissioning, and operation of large-area GEM detectors for CMS.

### PICOSEC

> I coordinated PICOSEC Micromegas R&D for future muon-collider detector concepts, including prototypes, test beams, photocathodes, gases, and background-rejection studies.

### CMS GEM

> I worked on CMS triple-GEM detectors from R&D and quality control to commissioning, gas-system responsibility, and Run 3 operations.

## Selected outputs heading

> Selected work

Intro:

> A few recent papers and talks. The complete record is available on the dedicated pages and in my CV.

Do not add jokes to individual entries.

## Teaching teaser

Heading:

> Teaching, supervision, and outreach

Text:

> I supervise students, teach detector laboratories, contribute to international detector schools, and give public seminars on particle and astroparticle physics.

Optional second homepage playful line:

> The objective is to make the physics clear before the apparatus decides to provide its own demonstration.

Use this only if the hero already contains no other additional joke.

## Contact block

Heading:

> Get in touch

Text:

> For research collaborations, detector R&D, seminars, or student projects, contact me by email or through the profiles linked below.

---

# Research Page

## Front matter

```yaml
---
layout: portfolio-page
title: "Research"
permalink: /research/
excerpt: "Research on gaseous detectors, optical TPCs, directional dark matter, X-ray polarimetry, precision timing, and low-energy neutrino detection."
author_profile: false
---
```

## Introduction

> My research is centred on gaseous-detector instrumentation, especially Micro-Pattern Gaseous Detectors and optical time projection chambers. I work across detector design, simulation, construction, commissioning, operation, and data analysis, with a focus on extracting directional or timing information from low-energy and rare signals.

No joke in the introduction.

## Section heading

> Current research

### CYGNO04

Status label:

> Current · Technical coordination and commissioning

Scientific objective:

> CYGNO04 is a 400 L radiopure optical TPC designed to demonstrate directional dark-matter detection at LNGS.

My role:

> I coordinate the technical development of the detector, including subsystem interfaces, assembly, installation planning, commissioning, operations, and collaboration-wide action tracking.

Focus bullets:

- detector integration and commissioning;
- optical and electronic readout;
- gas, high voltage, services, shielding, and background control.

Suggested factual captions:

- `Decommissioning of the LIME prototype at LNGS.`
- `CYGNO04 detector integration in the clean room.`

One optional playful caption may replace the second caption:

> Clean-room work: where one loose fibre can become the main character.

Do not add another joke in the CYGNO04 text if this caption is used.

### Optical TPCs for X-ray polarimetry

Status label:

> Current · Detector development and reconstruction

Scientific objective:

> This programme adapts large-area optical triple-GEM TPCs to reconstruct photoelectron tracks and measure X-ray polarisation in the 10–60 keV energy range.

My role:

> I develop and test the detector, study light and charge response, simulate its performance, and work on track reconstruction and modulation measurements.

Focus bullets:

- low-energy photoelectron imaging;
- detector calibration and data–simulation comparison;
- wide-field hard X-ray polarimeter concepts.

Captions:

- `Laboratory test of the optical TPC for X-ray polarimetry.`
- `Reconstruction of the photoelectron emission direction from the optical track.`

No jokes required here.

### New R&D: neutrinos, CEvNS, and space instrumentation

Status label:

> Developing concepts

Scientific objective:

> I investigate detector concepts in which low-energy tracking, timing, or directional information can improve sensitivity to neutrino and astroparticle signals.

My role:

> I contribute detector modelling, response simulation, sensitivity studies, and space-environment background simulations.

Focus bullets:

- directional solar-neutrino studies;
- high-pressure TPC concepts for CEvNS;
- EXPO instrument and orbital-background simulations.

Captions should be factual.

## Section heading

> Previous projects

### PICOSEC timing

Status label:

> Previous · R&D coordination

Scientific objective:

> PICOSEC Micromegas combines Cherenkov light and gaseous amplification to provide precise timing for minimum-ionising particles.

My role:

> I coordinated detector R&D for muon-collider applications, connecting prototype development, materials, gases, test beams, and beam-induced-background simulations.

Focus bullets:

- larger and more robust prototypes;
- photocathode and radiator studies;
- timing-based background rejection.

Optional playful line — this can be the second and final humorous line on the research page:

> Picoseconds are small; the test-beam preparation is not.

Do not add a humorous image caption if this sentence is used.

### CMS GEM detectors

Status label:

> Previous · Development, commissioning, and operations

Scientific objective:

> Large-area triple-GEM detectors extend the CMS muon system into high-rate forward regions.

My role:

> I worked from detector R&D and qualification through commissioning and Run 3 operation, including gas-system responsibility and detector performance studies.

Focus bullets:

- ageing, discharge, rate, and magnetic-field studies;
- quality control and test beams;
- gas monitoring, commissioning, shifts, and operational tools.

No joke in this section.

---

# Publications Page

## Front matter

```yaml
---
layout: portfolio-page
title: "Publications"
permalink: /publications/
excerpt: "Selected publications on optical TPCs, gaseous detectors, X-ray polarimetry, PICOSEC timing, and CMS GEM detectors."
author_profile: false
---
```

## Introduction

Recommended:

> A selected set of publications tracing my work across optical TPCs, gaseous-detector development, X-ray polarimetry, precision timing, and CMS GEM detectors.

Optional playful alternative:

> This is the selected list; the complete version is closer to a small gravitational object and is available through Scopus, ORCID, and my CV.

Use one version only. If using the playful alternative, do not add any other joke on the page.

## Metrics heading

> Publication record

Use the existing verified numbers and update date. Format as compact cards:

- Publications
- Citations
- h-index

Below:

> Source: Scopus. Last updated: [existing verified date].

## External links

- Scopus profile
- ORCID profile
- Download CV

## Selected publication entries

For each item, retain:

- official title;
- year;
- direct DOI or arXiv link;
- optional journal;
- optional factual contribution line.

Remove the current humorous second line from every paper.

Example factual contribution lines:

### Optical TPC polarimetry paper

> Demonstration of low-energy electron-track imaging and polarimetric response with a large-area optical TPC.

### CYGNO light-response paper

> Detector-response model connecting energy deposition, GEM amplification, optical emission, and camera response.

### CMS discharge paper

> Study of discharge and short-circuit behaviour observed during Run 3 operation of CMS GE1/1 detectors.

Factual contribution lines are optional. Do not invent authorship position or claim personal ownership of a collaboration result.

---

# Talks Page

## Front matter

```yaml
---
layout: portfolio-page
title: "Talks and presentations"
permalink: /talks/
excerpt: "Selected invited, plenary, and conference presentations on CYGNO, X-ray polarimetry, PICOSEC, and CMS GEM detectors."
author_profile: false
---
```

## Introduction

> Invited, plenary, and conference presentations on gaseous detectors, directional dark matter, X-ray polarimetry, precision timing, and detector operations. The suitcase survived. Mostly.

This is the only joke on the page.

## Featured talks

Select up to four based on scientific relevance and recency. Recommended candidates from the current content:

- The CYGNO experiment — 9th CYGNUS Workshop, Kobe, 2026
- CYGNO directional dark matter — TAUPP or EPS-HEP, 2025
- X-POT: X-ray Polarimetry with Optical Time Projection Chamber — ASAPP, 2025
- PICOSEC Micromegas detector for precise muon timing — FAST, 2023

Do not claim a talk is invited or plenary unless the existing source states it.

## Complete list

- sort reverse chronologically;
- within the same year, place international invited/plenary talks before parallel talks, then collaboration meetings;
- retain event, location, and type;
- use compact metadata styling;
- add links only when verified.

---

# Teaching & Outreach Page

## Front matter

```yaml
---
layout: portfolio-page
title: "Teaching & Outreach"
permalink: /teaching/
excerpt: "Teaching, student supervision, detector schools, public outreach, and scientific service."
author_profile: false
---
```

## Introduction

> I supervise students, teach experimental detector laboratories, contribute to international schools, and present particle and astroparticle physics to specialist and public audiences.

No joke in the intro.

## Gallery captions

Factual caption:

> Hands-on gaseous-detector teaching at an international detector school.

Optional playful caption:

> First explain the avalanche, then hope the setup also listened.

Second factual caption:

> Public seminar on particle and astroparticle detectors.

Only one playful caption in the gallery.

## Student supervision

> Co-supervisor of GSSI PhD students and supervisor or co-supervisor of Bachelor, Master, CERN Summer Student, and short-term internship projects.

Supporting line:

> My supervision focuses on connecting the physics question to a reproducible analysis or a detector that can actually be operated.

This is direct, not a joke.

## Laboratory teaching

> Lecturer for the GSSI PhD course Laboratory of Low-Energy Radiation Measurement and tutor for hands-on detector schools at LNGS and CERN, including DRD1 and RD51 activities.

## Outreach

> INFN LNGS guide, former CMS guide, public-seminar speaker, European Researchers' Night contributor, and coordinator of CYGNO outreach and social-media activities.

Optional second playful line on the page:

> Translating detector dialect into normal human language remains an active research programme.

Use only if the gallery already has no playful caption, or count both and do not add more.

## Scientific service

> Organiser and laboratory manager for detector schools and collaboration meetings, including CYGNO, DRD1, RD51, the Gran Sasso Hands-on PhD Summer School, and the Frontiers in X-ray Polarimetry Academy. Referee for JINST and EPJ Techniques and Instrumentation.

Verify journal wording against the CV before publication.

---

# CV Page

## Front matter

```yaml
---
layout: portfolio-page
title: "Curriculum Vitae"
permalink: /cv/
excerpt: "Curriculum vitae of Davide Fiorina, experimental particle and astroparticle physicist."
author_profile: false
---
```

## Introduction

> A complete record of my research experience, detector responsibilities, publications, talks, teaching, and scientific service.

## Actions

Primary:

> Download CV

Secondary:

> Open PDF in a new tab

Mobile fallback:

> The embedded viewer may be limited on mobile devices. Use the download or open link for the full document.

No jokes on this page.

---

# Fixed Profile / Short Bio

Recommended short bio for metadata or compact components:

> Experimental particle and astroparticle physicist working on gaseous detectors, optical TPCs, directional dark matter, X-ray polarimetry, and precision timing.

Recommended medium bio:

> Davide Fiorina is an experimental particle and astroparticle physicist at GSSI. His research focuses on gaseous detectors and optical time projection chambers for directional dark-matter searches, X-ray polarimetry, precision timing, and low-energy neutrino detection. He is Technical Coordinator of CYGNO04 at LNGS.

Before publication, confirm the exact current role title and whether `Site Manager` should be included.

---

# Words and constructions to avoid

Do not use these repeatedly:

- cutting-edge
- groundbreaking
- innovative research
- pushing boundaries
- unlocking insights
- at the forefront
- passionate about
- bridge between
- intersection between
- where X meets Y
- shy signals
- detector personality
- theatrical confidence
- feral ideas
- noble aim
- delicate art
- suspicious amount of coffee

A single naturally chosen informal phrase is acceptable. Repetition is not.


---

# Source document: IMPLEMENTATION_SEQUENCE.md

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


---

# Source document: CLAUDE_CODE_PROMPTS.md

# Claude Code Prompts

## How to use these prompts

Run one prompt at a time.

After Claude Code finishes a phase:

1. read its summary;
2. inspect `git diff`;
3. run the local site;
4. review the relevant page in a browser;
5. correct issues before continuing;
6. commit only the reviewed phase.

Do not paste all prompts at once.

---

## Prompt 0 — Baseline and plan validation

```text
Read CLAUDE.md and these files:

- docs/redesign/CURRENT_SITE_AUDIT.md
- docs/redesign/MASTER_SPEC.md
- docs/redesign/IMPLEMENTATION_SEQUENCE.md
- docs/redesign/QA_ACCEPTANCE_CHECKLIST.md

Do not edit the website yet.

Tasks:
1. Run git status --short and report the current branch.
2. Inspect the current Jekyll structure and confirm the key files named in the audit exist.
3. Run the existing production build using the repository's documented build command.
4. Identify any baseline build errors, warnings, broken references, or missing dependencies.
5. Produce a concise implementation map listing the exact files you expect to create or edit in Phases 1–8.
6. Flag any conflict between the documentation and the actual repository.

Do not redesign, rewrite, commit, or push. Stop after the report.
```

---

## Prompt 1 — Layout and SCSS foundation

```text
Implement Phase 1 from docs/redesign/IMPLEMENTATION_SEQUENCE.md.

Read:
- CLAUDE.md
- docs/redesign/MASTER_SPEC.md, especially sections 11–13
- docs/redesign/QA_ACCEPTANCE_CHECKLIST.md

Scope:
- create _layouts/portfolio-page.html
- create _sass/_site-refresh.scss
- modify assets/css/main.scss only as required to import the new partial

Requirements:
- retain Jekyll and the existing default layout;
- do not modify page content yet;
- do not modify unrelated inherited theme files;
- omit the sidebar in the new layout;
- use semantic main content;
- implement the design tokens, basic wrapper, typography, buttons, cards, tags, focus states, breakpoints, and reduced-motion rules;
- namespace the new component classes to minimise regressions;
- do not add JavaScript;
- do not add external font dependencies.

Before editing, show the files you will touch.
After editing:
1. run git diff --check;
2. run the production Jekyll build;
3. report changed files, build result, and manual checks required.

Do not commit, push, or begin Phase 2. Stop.
```

---

## Prompt 2 — Homepage

```text
Implement Phase 2 from docs/redesign/IMPLEMENTATION_SEQUENCE.md.

Read:
- CLAUDE.md
- docs/redesign/MASTER_SPEC.md sections 5, 11, and 12
- docs/redesign/PAGE_COPY_DRAFTS.md, Homepage section
- docs/redesign/QA_ACCEPTANCE_CHECKLIST.md

Primary scope:
- modify _pages/about.md
- modify _sass/_site-refresh.scss only when homepage-specific styles are needed
- create at most one small reusable include if it clearly reduces duplication
- use existing images only

Requirements:
- use layout: portfolio-page;
- preserve permalink /;
- build the hero, status strip, current research cards, earlier detector programmes, selected work, teaching teaser, and contact block;
- use one fixed profile or laboratory portrait;
- do not use the random profile system;
- do not duplicate the navigation in a Start Here list;
- keep the scientific text faithful to PAGE_COPY_DRAFTS.md;
- maximum two playful lines on the entire homepage;
- add descriptive alt text;
- do not invent links, metrics, roles, or outputs;
- link research cards to valid anchors that will exist after Phase 3;
- make the page usable at 390 px width.

Before editing, inspect the available profile images and state which one you selected and why, using only visible file properties and existing image review. Do not select files from a not-to-use directory.

After editing:
1. run git diff --check;
2. run the production build;
3. count the playful lines and report them;
4. report files changed and manual viewport checks needed.

Do not commit, push, or begin Phase 3. Stop.
```

---

## Prompt 3 — Research page

```text
Implement Phase 3 from docs/redesign/IMPLEMENTATION_SEQUENCE.md.

Read:
- CLAUDE.md
- docs/redesign/MASTER_SPEC.md section 6
- docs/redesign/PAGE_COPY_DRAFTS.md, Research Page section
- docs/redesign/QA_ACCEPTANCE_CHECKLIST.md

Scope:
- modify _pages/portfolio.html
- modify _sass/_site-refresh.scss only for research-page components
- update image references only when necessary

Required structure:
- concise introduction;
- Current research:
  1. CYGNO04 as the visually dominant feature;
  2. optical TPCs for X-ray polarimetry;
  3. neutrinos, CEvNS, and space instrumentation;
- Previous projects:
  1. PICOSEC;
  2. CMS GEM.

Each project must contain:
- status label;
- title;
- scientific objective;
- image;
- My role;
- no more than three focus bullets;
- tags or verified links.

Required anchors:
- #cygno04
- #xray-polarimetry
- #new-rd
- #picosec
- #cms-gem

Humour:
- maximum two playful lines or captions across the whole page;
- report exactly which lines count toward this total.

Accuracy:
- preserve all five research areas;
- do not invent results, funding, responsibilities, or links;
- keep official experiment names.

After editing:
1. run git diff --check;
2. run the production build;
3. verify the five anchors in generated HTML or source;
4. report changed files, humour count, and manual checks.

Do not commit, push, or begin Phase 4. Stop.
```

---

## Prompt 4 — Publications and talks

```text
Implement Phase 4 from docs/redesign/IMPLEMENTATION_SEQUENCE.md.

Read:
- CLAUDE.md
- docs/redesign/MASTER_SPEC.md sections 7 and 8
- docs/redesign/PAGE_COPY_DRAFTS.md, Publications Page and Talks Page sections
- docs/redesign/QA_ACCEPTANCE_CHECKLIST.md

Scope:
- modify _pages/publications.md
- modify _pages/talks.html
- modify _sass/_site-refresh.scss only as needed

Publications requirements:
- preserve every existing selected publication and its link;
- preserve official titles exactly;
- create a compact metrics panel with the existing verified numbers and update date;
- retain Scopus, ORCID, and CV links;
- remove the humorous annotation below every paper;
- use at most one playful sentence on the page;
- do not invent journal names, authorship roles, or contribution claims.

Talks requirements:
- preserve all current talks and posters;
- sort talks reverse chronologically;
- create a Featured talks section with at most four items selected from the existing list;
- retain invited/plenary/parallel type only when already stated;
- retain posters as a separate section;
- add links only if already present or verified in the repository;
- use at most one playful sentence on the page.

Validation:
- before editing, record the number of selected publications, talks, and posters;
- after editing, report the same counts and explain any difference;
- compare all publication URLs before and after.

After editing:
1. run git diff --check;
2. run the production build;
3. report count preservation, humour count, and manual checks.

Do not commit, push, or begin Phase 5. Stop.
```

---

## Prompt 5 — Teaching and CV

```text
Implement Phase 5 from docs/redesign/IMPLEMENTATION_SEQUENCE.md.

Read:
- CLAUDE.md
- docs/redesign/MASTER_SPEC.md sections 9 and 10
- docs/redesign/PAGE_COPY_DRAFTS.md, Teaching & Outreach Page and CV Page sections
- docs/redesign/QA_ACCEPTANCE_CHECKLIST.md

Scope:
- modify _pages/teaching.html
- modify _pages/cv.md
- modify _sass/_site-refresh.scss only as needed

Teaching requirements:
- retain the two current images;
- create four clear cards: Student supervision, Laboratory teaching, Outreach, Scientific service;
- preserve the factual scope of all four areas;
- maximum two playful lines on the page;
- descriptive alt text;
- no unsupported numeric claims.

CV requirements:
- preserve the PDF file and its path;
- add a primary Download CV action;
- add a secondary Open PDF in new tab action;
- retain the embed only if it remains usable;
- provide a mobile fallback message;
- no jokes;
- do not modify files/CV.pdf.

After editing:
1. run git diff --check;
2. run the production build;
3. verify both CV links resolve to the existing PDF path;
4. report changed files, humour count, and manual checks.

Do not commit, push, or begin Phase 6. Stop.
```

---

## Prompt 6 — Navigation, metadata, and profile cleanup

```text
Implement Phase 6 from docs/redesign/IMPLEMENTATION_SEQUENCE.md.

Read:
- CLAUDE.md
- docs/redesign/MASTER_SPEC.md sections 4 and 14
- docs/redesign/PAGE_COPY_DRAFTS.md, Fixed Profile / Short Bio section
- docs/redesign/QA_ACCEPTANCE_CHECKLIST.md

Scope:
- _data/navigation.yml
- _config.yml
- _includes/author-profile.html
- _sass/_masthead.scss or _sass/_sidebar.scss only if necessary
- _sass/_site-refresh.scss only if necessary

Requirements:
- keep the existing public URLs;
- use navigation labels Research, Publications, Talks, Teaching, CV;
- ensure the site name links to /;
- remove random profile-image JavaScript;
- use one fixed image;
- keep the legacy author profile functional but simple;
- no primary redesigned page should display the old sidebar;
- update site description and short author bio only with wording from PAGE_COPY_DRAFTS.md;
- do not add unverified social profiles;
- do not expose additional personal information;
- do not broadly delete unused theme infrastructure.

After editing:
1. search the repository for js-random-profile-avatar and random-profile-avatar;
2. confirm no active random profile code remains;
3. run git diff --check;
4. run the production build;
5. report changed files and manual navigation checks.

Do not commit, push, or begin Phase 7. Stop.
```

---

## Prompt 7 — Image optimisation

```text
Implement Phase 7 from docs/redesign/IMPLEMENTATION_SEQUENCE.md.

Read:
- CLAUDE.md
- docs/redesign/MASTER_SPEC.md sections 11 and 15
- docs/redesign/QA_ACCEPTANCE_CHECKLIST.md

Do not process all repository images blindly.

Tasks:
1. Inventory only images used by the redesigned homepage, research page, and teaching page.
2. Report current dimensions and file sizes.
3. Propose an exact conversion table before changing files:
   - source path;
   - destination path;
   - target dimensions;
   - target format;
   - reason.
4. Preserve source images until converted versions are verified.
5. Convert photographic images to WebP where useful.
6. Do not damage labels in plots or diagrams.
7. Use git mv for any filename cleanup.
8. Update all references.
9. Add loading=lazy and decoding=async below the fold.
10. Do not lazy-load the hero image.
11. Add explicit dimensions or stable aspect ratios where practical.

After editing:
- verify every referenced image exists;
- report before/after total byte size for the processed set;
- run git diff --check;
- run the production build;
- list images that require visual inspection.

Do not commit, push, or begin Phase 8. Stop.
```

---

## Prompt 8 — Final QA

```text
Perform Phase 8 from docs/redesign/IMPLEMENTATION_SEQUENCE.md.

Read:
- CLAUDE.md
- docs/redesign/QA_ACCEPTANCE_CHECKLIST.md

Do not add new features.

Tasks:
1. Run the production Jekyll build.
2. Run git diff --check.
3. Review generated pages for:
   - missing images;
   - broken internal links;
   - invalid heading order;
   - duplicate IDs;
   - empty links;
   - missing alt text;
   - old sidebar leakage;
   - random profile code;
   - humour-budget violations.
4. Inspect CSS for horizontal overflow risks at 390 px.
5. Check the five primary navigation links and CV PDF path.
6. Compare publication, talk, and poster counts against the pre-redesign source.
7. Review all changed scientific wording for unsupported claims.
8. Produce a checklist report using the IDs in QA_ACCEPTANCE_CHECKLIST.md.
9. Fix only objective defects found during QA.
10. Re-run tests after fixes.

Do not commit, push, merge, or open a pull request. Stop with:
- pass/fail table;
- remaining manual browser checks;
- exact files changed during QA.
```

---

## Prompt 9 — Prepare reviewed commit

Use only after manually reviewing the phase:

```text
Review the current git diff for the completed phase.

Tasks:
1. Confirm the diff is limited to the intended phase.
2. Summarise the user-visible changes.
3. Run git diff --check and the production Jekyll build once more.
4. If both pass, create one commit with a concise conventional message beginning with redesign:, perf:, or qa: as appropriate.
5. Show the commit hash and git status --short.

Do not push.
```

---

## Prompt 10 — Prepare draft pull request

Use only after all phases and manual QA:

```text
Read CLAUDE.md and docs/redesign/QA_ACCEPTANCE_CHECKLIST.md.

Confirm:
- working tree is clean;
- all redesign commits are on the redesign branch;
- production build passes;
- mandatory QA items pass.

Then:
1. summarise commits relative to master;
2. push the redesign branch to origin;
3. prepare a draft pull request to master titled:
   "Redesign academic website as a technical research portfolio"
4. Include:
   - design summary;
   - page changes;
   - content and humour strategy;
   - performance changes;
   - testing performed;
   - remaining manual checks.

Do not merge.
```


---

# Source document: QA_ACCEPTANCE_CHECKLIST.md

# QA and Acceptance Checklist

Use the IDs in this document in the final QA report.

`MUST` items block deployment. `SHOULD` items require either a pass or a documented reason for acceptance.

---

## A. Build and repository integrity

| ID | Level | Requirement |
|---|---|---|
| A01 | MUST | Production Jekyll build completes without error. |
| A02 | MUST | `git diff --check` returns no whitespace errors. |
| A03 | MUST | No public permalink has changed. |
| A04 | MUST | No unrelated repository files were modified. |
| A05 | MUST | The CV PDF remains present at its intended path. |
| A06 | MUST | No credentials, tokens, local paths, or private configuration were added. |
| A07 | SHOULD | Each implementation phase is represented by a small reviewable commit. |

## B. Navigation and structure

| ID | Level | Requirement |
|---|---|---|
| B01 | MUST | Home, Research, Publications, Talks, Teaching, and CV pages load. |
| B02 | MUST | Main navigation contains Research, Publications, Talks, Teaching, and CV. |
| B03 | MUST | Site name/logo links to `/`. |
| B04 | MUST | Mobile navigation can be opened and used by keyboard. |
| B05 | MUST | No redesigned primary page displays the old author sidebar. |
| B06 | MUST | Research anchors `cygno04`, `xray-polarimetry`, `new-rd`, `picosec`, and `cms-gem` exist and are unique. |
| B07 | SHOULD | Current-page navigation state is visually clear. |

## C. Homepage

| ID | Level | Requirement |
|---|---|---|
| C01 | MUST | Name, research identity, and current role are visible in the first desktop viewport. |
| C02 | MUST | The hero uses one fixed image. |
| C03 | MUST | No random image selection code affects the hero or sidebar. |
| C04 | MUST | Homepage contains no duplicated Start Here navigation list. |
| C05 | MUST | Homepage contains at most two playful lines. |
| C06 | MUST | Primary calls to action work. |
| C07 | MUST | Featured research cards link to valid destinations or anchors. |
| C08 | SHOULD | Homepage prose is at least 35% shorter than the previous version. |

## D. Research page

| ID | Level | Requirement |
|---|---|---|
| D01 | MUST | CYGNO04 is the most visually prominent project. |
| D02 | MUST | Current research and previous projects are clearly separated. |
| D03 | MUST | All five project areas remain present. |
| D04 | MUST | Each project states a scientific objective and Davide's role. |
| D05 | MUST | Each project has no more than three main bullets. |
| D06 | MUST | Research page contains at most two playful lines or captions. |
| D07 | MUST | No unverified scientific result, funding claim, role, or project status was introduced. |

## E. Publications

| ID | Level | Requirement |
|---|---|---|
| E01 | MUST | All existing selected publication entries remain. |
| E02 | MUST | All existing publication URLs remain or are replaced only by verified equivalents. |
| E03 | MUST | Official publication titles are unchanged. |
| E04 | MUST | The joke/annotation below every paper has been removed. |
| E05 | MUST | Page contains at most one playful introductory sentence. |
| E06 | MUST | Bibliometric values include their source and update date. |
| E07 | MUST | Scopus, ORCID, and CV links work. |

## F. Talks and posters

| ID | Level | Requirement |
|---|---|---|
| F01 | MUST | All existing talks remain. |
| F02 | MUST | All existing posters remain. |
| F03 | MUST | Talks are sorted reverse chronologically. |
| F04 | MUST | Invited, plenary, and parallel labels match the existing source. |
| F05 | MUST | No slide or event link was invented. |
| F06 | MUST | Page contains at most one playful sentence. |
| F07 | SHOULD | Up to four featured talks appear above the full list. |

## G. Teaching and CV

| ID | Level | Requirement |
|---|---|---|
| G01 | MUST | Student supervision, laboratory teaching, outreach, and scientific service remain represented. |
| G02 | MUST | Teaching page contains at most two playful lines. |
| G03 | MUST | Both teaching images load and have descriptive alt text. |
| G04 | MUST | CV download link resolves to the existing PDF. |
| G05 | MUST | CV open-in-new-tab link works. |
| G06 | MUST | CV page contains no jokes in its instructions or controls. |
| G07 | SHOULD | Embedded PDF has a usable mobile fallback. |

## H. Accessibility

| ID | Level | Requirement |
|---|---|---|
| H01 | MUST | Every page has one H1. |
| H02 | MUST | Heading levels do not skip for visual styling. |
| H03 | MUST | Every meaningful image has useful alt text. |
| H04 | MUST | Keyboard focus is visible. |
| H05 | MUST | All interactive controls are keyboard reachable. |
| H06 | MUST | Text and controls meet reasonable WCAG AA contrast. |
| H07 | MUST | Link purpose is clear from visible text or accessible name. |
| H08 | MUST | Reduced-motion preferences are respected. |
| H09 | SHOULD | Page landmarks use semantic header, nav, main, and footer elements. |

## I. Responsive layout

| ID | Level | Requirement |
|---|---|---|
| I01 | MUST | No horizontal scrolling at 390 px viewport width. |
| I02 | MUST | Hero content stacks logically on mobile. |
| I03 | MUST | Buttons remain readable and tappable on mobile. |
| I04 | MUST | Cards reduce to one column where required. |
| I05 | MUST | Navigation does not overlap the page title or hero. |
| I06 | MUST | Scientific plots remain legible or openable at full size. |
| I07 | SHOULD | Layout is visually balanced at 768 px and 1024 px widths. |

## J. Performance and images

| ID | Level | Requirement |
|---|---|---|
| J01 | MUST | Hero image is not randomly selected. |
| J02 | MUST | Hero image is not lazy-loaded when above the fold. |
| J03 | MUST | Below-the-fold images use lazy loading where appropriate. |
| J04 | MUST | No processed image reference is broken. |
| J05 | MUST | Plot labels remain readable after optimisation. |
| J06 | SHOULD | Hero image is under approximately 300 KB. |
| J07 | SHOULD | Ordinary displayed photographs are under approximately 250 KB. |
| J08 | SHOULD | Images have stable dimensions or aspect ratios to reduce layout shift. |
| J09 | SHOULD | Total transferred image size on the homepage is substantially lower than before. |

## K. Tone and authorship

| ID | Level | Requirement |
|---|---|---|
| K01 | MUST | Scientific claims are direct and factual. |
| K02 | MUST | No page uses repeated personification of detectors. |
| K03 | MUST | Humour budgets are respected page by page. |
| K04 | MUST | No two humorous lines appear in adjacent content blocks. |
| K05 | MUST | Publication entries do not contain jokes. |
| K06 | MUST | Formal roles and metrics are not paired with jokes. |
| K07 | SHOULD | At least one human, recognisably personal line remains on the homepage. |
| K08 | SHOULD | Teaching/outreach sounds less formal than publications without becoming flippant. |

## L. Manual content review

The human reviewer must confirm:

- exact current job title;
- whether `Site Manager` appears publicly;
- selected fixed portrait;
- current bibliometric numbers and date;
- preferred featured talks;
- whether all listed projects are still current;
- journal-referee wording;
- contact links;
- final humour lines.

These items cannot be safely inferred by a coding model.


---

# Source document: POWERSHELL_SETUP.md

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
