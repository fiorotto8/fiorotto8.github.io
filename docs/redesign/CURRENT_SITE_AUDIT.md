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
