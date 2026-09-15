# Human art direction — second pass, 15 September 2026

> The subsequent request for a **lighter palette, wider page and new photographs**
> is implemented in [PHOTOGRAPHIC_EXPANSION.md](PHOTOGRAPHIC_EXPANSION.md).
> That request supersedes the dark-palette decision documented in this pass.
> The current [media-library guide](MEDIA_LIBRARY.md) adds the subsequent folder
> organisation, compact photo pairs, portrait crop and requested animations.

## Brief and preservation contract

Apply [the supplied prompt](../Universal%20Website%20De-AIification%20and%20Human%20Art%20Direction%20Prompt.md) to the existing single-page implementation.
The earlier request for a dark cyberpunk palette remains explicit. Refine its
hierarchy; do not replace it with a light journal or invent a new brand.

Keep Jekyll, all public routes/fragments, structured publication/talk data,
CV, source photographs, responsive navigation, native details, print handling,
scroll tracking, reduced motion, metadata and local development workflow.
The large set of existing changes belongs to the first pass and is not a clean
Git baseline. This pass is compared with a separate local snapshot.

## Original visual problems

- The 124 px, tightly tracked two-line name dominates a short laptop screen.
  The actual research role appears much lower in the same hierarchy.
- Nearly every section starts with an uppercase, numbered monospace label,
  then repeats its category in a much larger heading.
- Cyan/magenta photo corners, a coloured name stop, status dot and repeated
  arrows compete with an already distinctive clean-room portrait.
- Every major section inherits 104 px padding. Research, bibliography and
  contact consequently have the same pace despite different reading tasks.
- Tiny monospace captions, years and talk types signify technology but make
  the scholarly record harder to read. Paper titles and talks look alike.
- The CV has a card border although alignment and a heading already group it.
- Mobile stacks the entire desktop introduction before its portrait.

## Original editorial problems

- “04 / Teaching & outreach” immediately repeats “Teaching & outreach”.
- The hero and biography both summarise the same hardware/simulation/data arc.
- “The common thread has been…” repeats concrete work already explained.
- Generic “Scroll to explore” and “Get in touch” add prompts without useful context.
- Project names can carry headings without a repeated section category or
  terminal punctuation. Existing scientific qualifications and formal titles
  need no stylistic embellishment.

## Design thesis

This is an experimental physicist's working record: laboratory photographs,
precise project responsibilities and a bibliography that colleagues can scan.
It speaks to collaborators, hiring committees, students and seminar organisers.
The useful impression is proximity to real detector work and care with evidence.

The visual direction is **a detector research record with documentary captions**.
The signature device is the close relationship between an unaltered laboratory
photograph and its plain-language caption. A photo may be large when it shows
apparatus; the portrait is smaller because it introduces the person.
The neon palette supplies the requested atmosphere, with cyan primarily for
navigation and magenta as secondary emphasis. It is a preference supplied by
Davide, not a colour system inferred from detector physics.

Typographic hierarchy should work at reading size: clear scientific symbols,
distinguishable numerals and compact bibliographic metadata. Test Go, the current
system sans, and a TeX Gyre Heros/Pagella combination on actual page content
before choosing. A serif is not required merely to signal academic work.

Preserve the unposed portrait, instrument photographs, direct first-person
research descriptions, structured output lists and simple native navigation.
Remove generic technical ornaments, repetitive section labels and excess CTA
emphasis. Do not add HUD diagrams, fake plots, research metrics or personal stories.

## Planned three passes

1. **System:** compare typography in browser, establish reading widths and
   a restrained palette hierarchy, and improve metadata legibility.
2. **Art direction:** rebalance the introduction, give apparatus photographs
   space, distinguish bibliography from talks, and adjust section density.
3. **Subtraction and copy:** remove repeated labels, border containers,
   decorative arrows and redundant summaries; read the whole page again.

## Evidence

Before screenshots and font comparisons: `.site-review/art-direction/before/`
and `.site-review/art-direction/specimens/`. These are local and excluded from
publication. Final decisions and validation are recorded below after inspection.

## Typography decision

Compared browser specimens using the actual name, role, a long publication
title, captions and 400 L / 10–60 keV / N² / Greek symbols. Selected **Go** as
one family: its differentiated letterforms and numerals remain clear in compact
research records, while regular, bold and true italic provide enough hierarchy.
The Heros/Pagella trial gave publication-like contrast but made the introduction
feel more formal than the candid laboratory material. The system sans control
retained the previous anonymous display treatment.

Go Regular/Bold/Italic are served locally as WOFF2, with the upstream licence.
No font service or production build dependency is added. Metadata no longer
uses monospace as an ornamental shorthand for technology.

## Layout and rhythm

The first browser pass brought the introduction onto a short laptop viewport
with the role, photograph and CV links visible together. On mobile, the portrait
sits next to the research identity before the biography rather than being pushed
below every piece of introductory text. The apparatus photograph is larger than
the portrait because its construction details carry information.

Research has room for images and explanation. Publications use a narrower
bibliographic measure and fewer dividing rules; talks retain year/event/type
columns. Teaching and appointments use their own reading structures. Contact is
a compact closing address. Section spacing is no longer one repeated value.

## Components

Retained the understandable sticky navigation, active underline and reading
progress. Converted the homepage research button to an ordinary reading link.
Removed photo corner brackets, the coloured name stop, status dot, numbered
section labels and repeated external arrows. The CV is grouped by alignment and
one separating rule, rather than a surrounding panel. Details/summary remains
native and keyboard accessible. Venue italics distinguish papers from talks.

## Colour and material

The deep violet background and cyan/magenta accents follow Davide's explicit
palette request. Cyan marks navigation and key links; magenta is reserved for
secondary emphasis and focus. Body copy is near-white, captions a readable muted
colour. Removed the third pale-yellow accent and ornamental use of neon colour.
Photographs retain their real laboratory lighting and colour.

## Imagery

Preserved the same five documentary photographs and their captions, full aspect
ratios and alt-text meaning. No generated images, filters or invented diagrams.
The CYGNO04 apparatus receives more area; the introduction uses a smaller portrait.
The polarimetry setup is an inset next to its technical description. Captions
are attached closely and use a true italic face at reading size.

## Copy and subtraction

Removed the repeated hardware/simulation/data summary from the biography,
redundant category labels, decorative terminal punctuation, “Scroll to explore”,
and the generic closing heading. Kept formal paper/talk titles, specialised
terms and the 10–60 keV qualification. The existing TV-dubbing sentence remains
sourced to the supplied CV; no personal history, hobbies or scientific claims
were added.

After inspecting pass 1, removed four more labels whose information was already
present in project names, the previous-work summary or the first sentence.
The three passes were system, photographic/layout hierarchy, then subtraction
and a separate full-page copy read. This is a refinement of the existing page,
not a second architecture migration.

## Preserved functionality

Jekyll, routes and anchors, JSON record schemas, CV, native expansion controls,
fragment/history behaviour, SEO semantics, printing and reduced motion retain
their operating model. SHA-256 comparisons confirm that the CV, publication
data and poster data are unchanged from the start of this pass. The two
intentional exceptions for talk data and navigation are described below.
The user-supplied prompt is preserved in the repository and excluded from the site.

During the full-page copy read, fixed one migrated event-label spacing error:
`N²is better than N` → `N² is better than N`, matching the original
`docs/archive/2026-07-content/talks.html.txt`. This is the only record-data edit
in this pass; the talk title, event meaning, year and URL are unchanged.

### Functional correction exposed by the shorter layout

At 1920×1080, both About and Contact fit near the bottom of the screen. The
existing script always selected Contact when scrolling reached the end, even
after clicking About. A bounded correction retains the clicked section while
it remains visible at the bottom; wheel, touch, pointer or scrolling keys resume
normal tracking. This was required to preserve navigation behaviour in the
more compact layout. Added a regression check, including a repeated About click.
The navigation script therefore intentionally differs from the initial snapshot;
its redirect, history, native-scrolling and reduced-motion model is preserved.

## Validation

Executed successfully:

```sh
bash bin/build --safe --destination /tmp/fiorina-art-final
python3 bin/check_site.py /tmp/fiorina-art-final
/tmp/fiorina-site-qa/bin/python bin/check_browser.py --output .site-review/art-direction/checks
bash bin/build --safe --baseurl /preview --destination /tmp/fiorina-art-subpath
python3 bin/check_site.py /tmp/fiorina-art-subpath --baseurl /preview
node --check assets/js/site.js
git diff --check
```

The production output contains eight pages and is 857 KiB, including the CV,
photographs and fonts. The static check covers internal links, anchors, heading
structure, metadata, the 16 publication / 24 talk / 12 poster records, and
exclusion of local/private/development files. The three local fonts total
89,408 bytes; no font-service request or new production runtime is required.

Browser checks cover all navigation links, legacy routes and fragments,
collapsed-section targets, back/forward history, keyboard focus, reduced
motion, image decoding and no-JavaScript fallbacks. The final-section selection
regression is covered at 1920×1080.

The `/preview/` subdirectory build also passes. A browser check against that
output verifies all three font files, the CV download, section navigation and
the legacy PICOSEC link into collapsed previous research.

An additional Chromium pass with axe-core 4.10.3 reported zero detected
accessibility violations on the desktop and mobile page with expandable
content open. Contrast items requiring manual review were checked against the
actual solid backgrounds: muted text is at least 9.60:1, primary text 16.22:1,
cyan 13.08:1 and magenta 8.09:1. Automated checks are not a complete
accessibility certification.

## Visual QA

Inspected the homepage introduction, research photographs/captions,
publications, talks, teaching, About/CV, contact, expanded records and 404 page.
Compared the initial and final laptop views directly: the research identity,
portrait and CV link now fit above the beginning of Research at 1366×768.
The mobile introduction gives the portrait a place beside the research identity;
long titles, the email address and dates wrap without horizontal overflow.

Browser regression viewports: 1920×1080, 1440×900, 1366×768, 1024×900,
768×1024, 390×844, 320×844 and 844×390 landscape. Additional checks used
910×512 and 683×384. Actual browser zoom was also set and verified through
Chromium's zoom API at 150% and 200% on a 1366×768 window; navigation and
reflow passed at both levels. This was not solely a resized-viewport simulation.

Evidence is local under `.site-review/art-direction/`: `before/`, `specimens/`,
`pass-1/`, `after/` and `checks/`. The final screenshots include every main
section at desktop and mobile sizes. The updated 1200×630 social card was
rendered from its SVG and visually inspected: it follows the same typography
and palette, without the earlier circuit ornament or enclosing panel.

## Remaining limitations

- Browser validation used Chromium in Linux/WSL. Safari, Firefox, physical
  phones and a screen-reader session were not tested.
- This pass preserves sourced academic statements and publication metadata;
  it does not establish whether every role or external record is current.
  The outstanding author questions in `WEBSITE_REVIEW.md` still apply.
- A fuller personal paragraph requires Davide's own interests or anecdotes.
  The existing TV-dubbing work is retained; no personal details were invented.
- Changes and evidence are local. Nothing has been committed, pushed or deployed.
