# Website review and redesign — 15 September 2026

> This records the first pass. See [ART_DIRECTION.md](ART_DIRECTION.md) for the
> subsequent refinement using the user-supplied de-AIification prompt.

## Outcome

A local, single-page version is implemented. It keeps Jekyll and the existing
GitHub Pages repository. No commit, push or publication was performed.

The page contains an introduction, research, publications, talks and posters,
teaching and outreach, an about section with a short CV, and contact details.
The navigation and accent colour follow the section in view. Scrolling remains
native; longer lists use accessible HTML details/summary controls.

## What the review found

| Area | Weak spot in the previous site | Change / remaining work |
| --- | --- | --- |
| Structure | The homepage repeats research descriptions, roles, output lists and contact prompts from five separate pages. | One continuous page; longer academic lists expand in place. Previous URLs still lead to the appropriate sections. |
| Writing | Repeated descriptions of the full detector lifecycle make different projects sound alike. Some lines are generic personal statements or compulsory jokes from the previous design brief. | Short first-person descriptions of the objective and the actual work. Direct headings, no prescribed humour quota. |
| Research | Large cards give developing proposals similar prominence to active detector programmes. The 10–60 keV wording can read as demonstrated coverage of the whole range. | Feature CYGNO04 and optical TPC polarimetry. Label concepts and previous projects explicitly; describe the energy range as an aim. |
| Academic record | Publications and talks are embedded directly in long page templates; featured talks are repeated in the full list. | Preserve all 16 papers, 24 talks and 12 posters in separate JSON data files. Each entry appears once. |
| Bibliometrics | Publication/citation/h-index counters are a snapshot dated 25 May 2026. | Remove counters and link to Scopus and ORCID. No invented update. |
| Personal profile | Career and detector work dominate. There is little about the person beyond an abstract statement about enjoying hands-on work. | Add a short career narrative and the TV-dubbing physics advisory work documented in the supplied CV. Hobbies and anecdotes await author input. |
| Talk links | 23 of 24 talk records have no programme or slide link. | Preserve the entries as plain text. Add links when supplied or independently verified. |
| Design | Repeated cards, buttons, tags, logo strips and an embedded CV make a small academic site feel bigger than its content requires. | Typography, photographs and simple dividing lines; direct CV links. Deep violet background, cyan/magenta accents and occasional pale yellow. |
| Maintenance | Hundreds of inherited theme files, sample pages, fake comments, obsolete plugins and conflicting design documents remain. | Replace the theme runtime with one layout, one stylesheet and one script. Remove verified template leftovers; archive previous authored material. |

## Source and factual boundaries

- The source pages and the supplied `files/CV.pdf` / local `files/cv.tex` are the
  principal evidence for research roles, appointments, teaching and outreach.
- The PDF was checked by SHA-256 before and after the work and is unchanged.
  The TeX source remains ignored and excluded from the build.
- All original publication and talk metadata was compared with the migrated
  data. The only typographic normalisation is HTML superscript N² represented
  as Unicode in talk/event text. Paper titles, years, venues and links are retained.
- The existing polarimetry preprint link and title were checked against
  [arXiv](https://arxiv.org/abs/2510.26239). It remains labelled as a preprint.
- [GSSI's physics postdoc directory](https://www.gssi.it/people/post-doc/post-doc-physics)
  lists Davide Fiorina. This supports the institutional context, but is not a
  substitute for Davide confirming his exact current role and project phase.
- No new performance claim, bibliometric value, role, funding amount or hobby
  was inferred. Earlier CMS/PICOSEC work and developing concepts remain distinct.
- The TV-dubbing sentence comes from the CV's Scientific Outreach and Public
  Engagement entry about Pumais Due. Davide should decide how much prominence
  this activity should have and whether a specific example can be shared.
- The website review does not constitute a new verification of every historical
  paper or conference programme. Existing source metadata is retained.

## Input that would improve the next content pass

1. **Current role and priorities:** Is “GSSI postdoctoral researcher and CYGNO
   Technical Coordinator, working on CYGNO04 integration and commissioning” still
   accurate? Which project or result should a visitor remember first?
2. **Personal material:** A few rough notes about interests, hobbies, places,
   motivations or an anecdote. Include TV-dubbing work if it is something you
   want to feature. No polished biography is needed.
3. **Academic emphasis:** Which papers best represent your own contribution?
   A concrete, author-approved contribution sentence would be more useful than
   citation counters. Send public slide/programme links for talks worth featuring.

Davide subsequently supplied personal and work photographs and explicitly
authorised hobby selection, naming trains and trail running. The personal input
has now been incorporated; see `PHOTOGRAPHIC_EXPANSION.md`. Current role and
academic-emphasis questions remain open. No placeholder biography is shown.

## Repository changes

- `CLAUDE.md` → `AGENTS.md`, rewritten for the new request and shared agent use.
- `_pages/about.md` → `_pages/home.html`; the misleading research filename
  `_pages/portfolio.html` → `_pages/research.html` (now a legacy entry route).
- The July documents and `PROJECT_OVERVIEW.md` moved to `docs/archive/2026-07-redesign/`.
  The old Claude prompt document is named `AGENT_PROMPTS.md` in that archive.
  Previous authored page content is retained under `docs/archive/2026-07-content/`.
- Removed the old theme layouts/includes, Sass vendor tree, jQuery and plugins,
  icon fonts, unused collapse code, sample pages/comments/authors, template demo
  images, dummy TSV/notebook generators, talk-map code, and old npm build file.
- Removed the empty blog-feed integration; retained the sitemap plugin and the
  local live-reload dependency. No installed dependency versions were upgraded.
- Kept all supplied research photographs, personal photographs and scientific
  figures in the repository. Sixty-three source/unused image files are excluded
  from publication. The selected photographs keep their original colours.
- Updated the editable favicon and social-card SVG colours; rendered PNG icons
  and the social preview from those vector sources. Preserved the inherited licence.
- No third-party runtime font, script, tracker or image service is needed.

## Verification

Passed on the local implementation:

- `bash bin/build --safe`: GitHub Pages-compatible production build.
- `python3 bin/check_site.py`: all local links, image URLs, fragments, heading
  structure, structured data, record counts and output exclusions.
- A `/preview` subpath build and the same static checks with `--baseurl /preview`.
- Chromium at 1440, 1024, 768, 390 and 320 px: no horizontal overflow, decoded
  photographs, working navigation, readable section targets below the sticky
  header, keyboard skip link and expandable lists.
- Legacy routes, research links into collapsed content, browser back/forward,
  reduced motion and navigation with JavaScript disabled.
- Normal smooth scrolling and print expansion/restoration of details.
- axe-core 4.10.3, WCAG A/AA and 2.1 AA rules, desktop and mobile with all lists
  expanded: zero detected violations. Colour-contrast cases marked for manual
  review were supplemented by inspection and palette contrast calculations.
- Screenshots visually inspected: desktop/mobile introduction, research,
  publications, teaching, about/CV, contact, and the generated social image.
- Unchanged CV hash; unchanged migrated record metadata apart from N² typography.
- `git diff --check` and JavaScript syntax validation.

The production output is approximately 775 KiB including the CV PDF and images.
CSS is approximately 14 KiB and JavaScript 4 KiB, before transfer compression.
These are file sizes, not a measured load-time claim.

Browser testing used local Chromium. Safari/Firefox and physical devices have
not been checked. Automated accessibility checks do not establish full WCAG
conformance. Author review of personal voice and current facts remains open.

## Reproducing the checks

```bash
bash bin/build --safe
python3 bin/check_site.py
git diff --check
```

In a separate terminal, run `bash bin/dev` to serve the site. For the optional
browser suite, install Playwright in an isolated environment:

```bash
python3 -m venv /tmp/fiorina-browser-qa
/tmp/fiorina-browser-qa/bin/pip install playwright
/tmp/fiorina-browser-qa/bin/playwright install chromium
/tmp/fiorina-browser-qa/bin/python bin/check_browser.py
```

Screenshots and the browser report go to the ignored `.site-review/` directory.
They are local review artifacts, excluded from deployment.
