> Historical document. Superseded by the September 2026 request; see `/AGENTS.md` and `/docs/WEBSITE_REVIEW.md`.

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
