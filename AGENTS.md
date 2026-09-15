# Working on Davide Fiorina's website

## Current direction

The September 2026 request supersedes the July redesign: a simple, scrollable
academic homepage, a lighter cyberpunk palette, and direct, personal writing.
The latest request widens the page and expands outreach explanations of the
research. The image library now uses `images/public/` for referenced website
assets and ignored `images/local/` for originals, unused images and larger
source versions, grouped by subject. See `images/README.md` and
`docs/MEDIA_LIBRARY.md`. This supersedes earlier image-folder instructions.
This file applies to Codex and other coding agents. Documents in `docs/archive/`
are historical evidence, not active instructions.
Read `README.md` for commands and `docs/ART_DIRECTION.md` for the current visual
and editorial decisions, including the latest photographic expansion. The user explicitly invoked
`Universal Website De-AIification and Human Art Direction Prompt.md`; apply it
to further refinements. `docs/WEBSITE_REVIEW.md` records the initial content audit.

## Repository and deployment

- Keep Jekyll and GitHub Pages compatibility in this authoritative checkout.
- Do not introduce a framework, CMS, backend, or required Node build step.
- Preserve `/`, `/research/`, `/publications/`, `/talks/`, `/teaching/`, `/cv/`,
  and `/resume`; old section URLs lead to the corresponding homepage anchors.
- Keep research anchors `cygno04`, `xray-polarimetry`, `new-rd`, `picosec`, and
  `cms-gem` working, including links into collapsed sections.
- Do not add analytics, trackers, cookies, or third-party forms.
- Do not change `files/CV.pdf` without an explicit request. Keep `files/cv.tex`
  local and excluded from Git and the published site.
- Inspect `git status --short` first. Preserve unrelated changes. Do not push
  or deploy unless requested; finish the local implementation and checks.
- Work through authorised tasks without artificial phase approval stops.

## Content and provenance

- Use clear first-person English and consistent British spelling. Prefer
  concrete activities and responsibilities over slogans or strings of jargon.
- Do not fabricate scientific results, publication metadata, roles, dates,
  authorship contributions, hobbies, anecdotes, or personal preferences.
- Ask Davide for missing personal information. Do not fill gaps with guesses.
- Davide explicitly authorised photo-based hobby selection and named trains
  and trail running. The current personal copy also reflects mountain walking
  visible in the supplied photographs. Do not infer race results, exact places,
  relationships, or a longer personal history from these images.
- Keep current work, previous work, concepts, and demonstrated results distinct.
- Use CYGNO, CYGNO04, CMS, PICOSEC, HypeX and EXPO consistently; use “X-ray”,
  “dark matter”, and “400 L” in prose. Define unfamiliar acronyms on first use.
- Preserve official paper and talk titles unless verified against their source.
- Maintain publication, talk and poster records in `_data/*.json`.
  Do not delete records to shorten the homepage; use native details.
- Avoid static citation counts, forced humour and invented personal statements.
- Retain source photographs and scientific figures even when unused.
  Keep them in `images/local/`, ignored by Git and excluded from Jekyll.
  Do not silently erase them or move them back into the published folders.
- Preserve the inherited `LICENSE`; do not infer rights for supplied photos.

## Design and implementation

- One continuous page in `_pages/home.html`, using `_layouts/default.html`.
- Palette: pale lilac and ice blue, dark violet text, teal/cyan and magenta accents.
  Keep body copy neutral and readable.
- Use real supplied photographs and local assets. Typography uses the locally
  hosted Go family; see `docs/FONTS.md` for provenance and licence.
- Prefer typography, spacing and documentary captions over repeated cards,
  numbered eyebrows, photo corner brackets and decorative technical UI.
- Keep scrolling native. Navigation tracks the section in view. All content
  must remain readable without JavaScript or with reduced motion enabled.
- Do not add parallax, scroll locking, autoplay, typewriter effects or particles.
  The two requested scientific animations use native controls, preload="none",
  poster frames, short captions and screen-reader descriptions. Preserve their baked-in credits and
  scientific scope. The local animation repositories are read-only sources here.
- Style in `assets/css/main.css`; behaviour in `assets/js/site.js`.
- Use native links and details/summary, semantic headings, descriptive alt
  text, visible focus, a skip link and at least 16 px body text.
- Lazy load below-the-fold images with dimensions and async decoding.
- `docs/PHOTO_SOURCES.json` maps original names to descriptive source names and
  hashes. `bin/prepare_photos.py` produces selected WebP sizes and `_data/photos.json`;
  it is optional maintenance tooling using Pillow, not a Jekyll build dependency.
  Preserve original photo bytes. The portrait's top crop and the trail photo's
  left-half crop are applied with CSS; other photographs retain full aspect ratios. Use modest display sizes and
  pairs where useful. Only referenced renditions belong in `images/public/`.
- The latest feedback asks for a closer portrait crop and a larger frame aligned
  with the intro row (420 px desktop, 150 px mobile). Use the shared research
  columns for day-to-day work and prototype rows; centre concept figures.
  The personal gallery selects the trail, train, Fitz Roy and penguin photos.
  CYGNO copy links to the website Davide designed/manages and the Instagram
  account he manages. CEνNS and EXPO figures illustrate concepts/proposals.
- CYGNO04 uses the copper vessel and `cygno04-cleanroom` photos together.
  PICOSEC uses the test-beam team; CMS GEM uses the GIF photographs.
- Use Jekyll `relative_url`/`absolute_url` filters for local links and assets.

## Verification and handoff

- Run `bash bin/build --safe` and `git diff --check`.
- Run `python3 bin/check_site.py` on generated output.
- For layout/navigation changes, inspect desktop and mobile in a browser.
  Check keyboard navigation, reduced motion, no JavaScript, deep links, history,
  overflow at 320/390 px and native expandable lists.
- Check a subpath build when changing URLs or redirects.
- Report verification evidence and unresolved author input separately.
