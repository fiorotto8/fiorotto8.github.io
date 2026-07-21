# CLAUDE.md — Repository Instructions for the Website Redesign

## Authority

This file is authoritative for all redesign work in this repository.

Before editing, read:

- `docs/redesign/MASTER_SPEC.md`
- the relevant phase in `docs/redesign/IMPLEMENTATION_SEQUENCE.md`
- the relevant page text in `docs/redesign/PAGE_COPY_DRAFTS.md`
- `docs/redesign/QA_ACCEPTANCE_CHECKLIST.md`

Do not reinterpret the visual direction unless the user explicitly asks for a change.

## Repository and deployment constraints

- Keep Jekyll.
- Keep GitHub Pages compatibility.
- Keep the existing repository and deployment process.
- Preserve existing public permalinks:
  - `/`
  - `/research/`
  - `/publications/`
  - `/talks/`
  - `/teaching/`
  - `/cv/`
- Do not migrate to React, Astro, Next.js, Hugo, or another framework.
- Do not introduce Node as a required production build step.
- Do not add a CMS or backend.
- Do not add analytics, cookies, trackers, or third-party forms.
- Do not modify the CV PDF unless explicitly instructed.
- Do not fabricate scientific results, publication metadata, roles, links, dates, or metrics.
- Do not delete source content merely because it is not shown on the homepage.
- Do not modify unrelated files.

## Safety and version-control rules

At the start of every phase:

1. Run `git status --short`.
2. Inspect the files named in the phase.
3. If unrelated local changes exist, do not overwrite them.
4. State which files will be modified.

At the end of every phase:

1. Run `git diff --check`.
2. Run the Jekyll production build.
3. Report:
   - files changed;
   - build result;
   - known limitations;
   - exact manual checks still needed.
4. Stop. Do not continue to the next phase automatically.

Use small commits. A phase should normally produce one commit.

## Technical implementation strategy

Prefer a low-risk additive redesign over editing the entire inherited theme.

Recommended architecture:

- Create a new layout: `_layouts/portfolio-page.html`.
- The layout should use the existing `default` layout, masthead, head, scripts, and footer.
- It should not render the inherited author sidebar.
- It should expose a full-width modern content wrapper.
- Create a new SCSS partial: `_sass/_site-refresh.scss`.
- Import `_site-refresh.scss` last from `assets/css/main.scss`.
- Use new, clearly namespaced classes such as:
  - `.site-shell`
  - `.site-content`
  - `.home-hero`
  - `.hero-kicker`
  - `.hero-actions`
  - `.status-strip`
  - `.section-heading`
  - `.project-grid`
  - `.project-card`
  - `.project-meta`
  - `.project-tags`
  - `.publication-list`
  - `.talk-list`
  - `.teaching-grid`
- Avoid broad selectors that unintentionally change old template pages.
- Reuse existing Liquid variables such as `base_path`.
- Keep the existing masthead and footer structure unless a phase explicitly says otherwise.
- Remove the random profile-photo behaviour. Use one fixed image.
- Keep the old sidebar include functional if it is used by an unconverted legacy page, but no primary page should require it after the redesign.

## Content rules

### Voice

Use clear first-person English.

Prefer:

- “I coordinate detector integration and commissioning.”
- “I develop optical TPCs for X-ray polarimetry.”
- “My work covers detector design, simulation, construction, and operation.”

Avoid:

- inflated claims;
- startup language;
- repeated rhetorical contrasts;
- repeated “this is where X meets Y” constructions;
- making detectors “shy,” “dramatic,” “opinionated,” “feral,” or “uncooperative” in every section;
- phrases such as “pushing the boundaries,” “at the forefront,” “cutting-edge,” or “unlocking new insights” unless factually necessary.

### Humour budget

Humour is required, but controlled.

Hard limits:

- Homepage: maximum 2 playful lines.
- Research page: maximum 2 playful captions or lines across the whole page.
- Publications page: maximum 1 playful introductory sentence; no joke under every paper.
- Talks page: maximum 1 playful sentence.
- Teaching page: maximum 2 playful lines because this page can be more personal.
- CV page: no jokes in the main instructions or download controls.
- Never place two jokes in adjacent content blocks.
- Never attach a joke to a safety role, formal responsibility, scientific result, or bibliometric number.
- A joke must be short enough that removing it does not change the meaning.

### Scientific precision

- Capitalise experiment names consistently: CYGNO, CYGNO04, CMS, PICOSEC, HypeX, EXPO.
- Use “dark matter” in running text unless it begins a title.
- Use “X-ray,” not “X-Ray.”
- Use “litre” or “L” consistently; prefer `400 L`.
- Use en dashes for ranges where practical: `10–60 keV`.
- Keep British or American spelling internally consistent. The recommended choice for this site is British English:
  - modelling
  - polarisation
  - programme
  - centre
- Do not silently alter official paper titles.

## Design rules

The visual concept is **dark technical editorial portfolio**.

The site uses a fixed dark theme based on deep blue-charcoal surfaces, not pure black. Pages using `layout: portfolio-page` are styled dark via the `body.portfolio-theme` class. Legacy pages still using inherited layouts remain visually unchanged until migrated.

Required qualities:

- clean;
- spacious;
- modern;
- scientific;
- slightly playful;
- readable on mobile;
- no visual gimmicks;
- fixed dark theme (no toggle).

Dark theme rules:

- use deep blue-charcoal backgrounds (`#0b1117`), never pure `#000000`;
- use layered dark surfaces with restrained borders for cards and elevated elements;
- maintain WCAG AA contrast at all times;
- use teal (`#55c2c3`) as the principal interactive accent;
- use warm coral (`#ef8065`) only for rare emphasis;
- avoid neon-on-black “hacker” styling;
- avoid glowing borders or box-shadow halos;
- avoid large gradients;
- avoid glassmorphism;
- avoid excessive shadows;
- do not add a light/dark theme toggle;
- the theme is fixed dark for all redesigned pages.

Avoid:

- neon-on-black “hacker” styling;
- glassmorphism;
- large gradient blobs;
- animated stars or particles;
- typewriter effects;
- carousels;
- auto-playing media;
- parallax;
- excessive rounded pills;
- heavy shadows;
- decorative charts with no data meaning.

## Accessibility rules

- Every meaningful image must have descriptive `alt` text.
- Decorative images must use empty `alt=""`.
- Maintain visible keyboard focus.
- Use semantic headings in order.
- Do not use colour as the only indicator.
- Link text must be descriptive.
- Use `aria-label` only where visible text is insufficient.
- Respect `prefers-reduced-motion`.
- All hover interactions must also work with keyboard focus.
- Body text must remain at least 16 px.
- Target WCAG AA contrast.

## Performance rules

- Add `loading="lazy"` and `decoding="async"` to below-the-fold images.
- Do not lazy-load the primary hero image if it is visible immediately.
- Avoid loading full-resolution phone images when a smaller file is sufficient.
- Prefer WebP for photographs if the conversion is performed safely.
- Preserve original source images until the converted versions are verified.
- Do not add a heavy JavaScript framework.
- New JavaScript should be avoided unless a feature cannot be implemented accessibly with HTML and CSS.

## Completion criteria

A phase is complete only when:

- Jekyll builds without errors;
- no Liquid syntax is broken;
- the changed page has valid heading order;
- there is no obvious horizontal overflow at 390 px width;
- humour limits are respected;
- the requested files only were changed, except for a clearly justified dependency;
- the phase-specific acceptance criteria pass.
