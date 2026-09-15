# Desktop row balance and final photo selection

15 September 2026. This author correction supersedes the smaller-portrait
choice and gallery selection in [CONTENT_REFINEMENT.md](CONTENT_REFINEMENT.md).

## Visual direction

The request is about how content occupies the existing columns. Keep the light
palette, Go typography, native navigation and readable body copy. Align related
research rows on the same grid, centre smaller figures within those columns,
and use supplied photographs to explain the work. Do not pad the page with
unverified accomplishments or crop technical diagrams to fill space.

## Changes

- The portrait is larger and more closely cropped: 420 px on desktop, 280 px
  on tablets and 150 px on phones, with a reversible 1.18 CSS zoom. Its desktop
  frame is approximately the height of the introduction. The original is intact.
- CYGNO has two additional paragraphs about recoil directions, backgrounds and
  the demonstrator, adapted from the earlier verified explanation. Technical
  coordination and the author-supplied website/Instagram credits remain.
- Day-to-day work and prototype rows use the same full-width research grid.
  The clean-room photograph is centred; both prototype images are larger.
- A supplied photoelectron schematic sits below the polarimetry animation.
  It is labelled as a conceptual gas polarimeter, not as an engineering drawing
  of the optical prototype. Its desktop caption sits beside it to balance the
  text column; on phones the caption sits beneath it.
- CEνNS and EXPO figures are centred within their respective subcolumns.
- The existing public-talk photograph joins the school-group photograph in
  the outreach row. Its caption does not invent an event, location or date.
- The personal gallery is centred across the page: trail running, a steam
  locomotive, the Fitz Roy portrait and the penguin photograph. The author
  identified Fitz Roy and the penguins. The stone-steps photo/caption and the
  previous mountain-lake image are retired locally. No personal history is added.

## Assets and preservation

`docs/PHOTO_SOURCES.json` selects the new responsive exports and records source
hashes. `docs/IMAGE_LIBRARY.json` also records the four retired exports, which
were moved to ignored `images/local/` folders. Originals and technical diagrams
are unaltered; only the portrait and trail photograph have CSS crops.

The public talk is exported at 320/554 px without upscaling. The Fitz Roy and
penguin photographs use 360/720 px exports. The schematic uses 300/597 px
lossless WebP exports from the supplied original. No new build dependency.

A SHA-256 comparison confirms that the CV, paper/talk/poster datasets and
production JavaScript are unchanged. Videos and their credits are unchanged.
No commit, push or deployment. The library contains 50 referenced public
assets and 136 preserved local files; every local manifest hash and ignore
rule was verified.

## Review evidence

Before/after captures, measured row dimensions and accessibility results are
in `.site-review/row-balance/`. Desktop review covers the introduction, CYGNO,
day-to-day work, polarimetry, prototype, concepts, outreach and personal gallery.
The same rows are inspected on mobile. Automated accessibility checks do not
replace a complete manual audit; silent-video captions and image-dependent
contrast still require judgement. Chromium/WSL does not cover Safari, Firefox
or physical devices.

Safe Jekyll builds and static checks passed at the root and `/preview` subpath
(5425 KiB and 5427 KiB respectively). Axe reported no WCAG A/AA violations
at 1440 and 390 px. The diagram, captions, photo selection and crops were
visually reviewed at both sizes. `git diff --check` passed.

The final browser run passed at 320, 390, 768, 844, 1024, 1366, 1440 and
1920 px: no overflow, image decoding, section tracking, anchor clearance,
keyboard navigation and native disclosures. Legacy routes/deep links,
back/forward history, reduced motion and use without JavaScript also passed.
