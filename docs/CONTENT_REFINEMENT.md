# Content and image refinement — 15 September 2026

> Superseded for portrait size, row alignment and photo selection by
> [ROW_BALANCE.md](ROW_BALANCE.md), following the author’s correction.

This pass follows the latest author feedback and supersedes the portrait size,
visible animation descriptions and personal-gallery arrangement in
[MEDIA_LIBRARY.md](MEDIA_LIBRARY.md).

## Direction and changes

The existing light palette, Go typography and documentary photographs already
fit the academic homepage. The remaining problems were an oversized portrait,
a long CYGNO04 explanation, unnecessary animation disclosure controls and a
wide trail photograph occupying the space of two images. Keep the visual system;
use shorter copy and a more informative selection of small photographs.

- Portrait: 280 px on desktop (previously 340), 210 px on tablets and 120 px on
  phones. Removed the extra 1.08 scale; retained the mild top crop through CSS.
- CYGNO04: three short paragraphs covering the research, technical coordination
  and communication work. The author explicitly supplied the website-design
  and management credit and Instagram-management credit. Both are linked.
- Animations: removed both “Read the animation description” controls. Visible
  summaries, credits and native playback remain. Complete descriptions remain
  available to screen readers through `aria-describedby`.
- Polarimetry: paired the prototype with an existing photograph of laboratory
  work, exported from the 984×737 source without cropping or upscaling.
- CEνNS and EXPO: small, uncropped supplied drawings. Captions and surrounding
  text identify these as detector concepts and a mission proposal. No instrument
  specifications or implementation status were inferred from the drawings.
- Personal gallery: the hillside photograph displays exactly its left half
  through CSS. A stone-steps running photograph fills the additional position.
  Four columns become two on narrower screens. Source photographs are unchanged.

## Organisation and provenance

The three new PNGs are now in ignored `images/local/research/neutrinos/` and
`images/local/research/expo/`, with descriptive names. The existing laboratory
photograph was renamed `polarimetry-laboratory-work.png`. The source manifests
record the moves and hashes; responsive exports live under `images/public/`.
There are 46 referenced public assets and 132 local source/unused files. All
132 local files were checked against their recorded SHA-256 hashes and Git
ignore rules. The originals remain local and need a separate backup.

The CYGNO homepage was fetched successfully. Instagram throttled the browser
fetch; its exact author-supplied URL is retained as an ordinary link. The author's
statement is the source for the website and account management credits.

## Verification

Screenshots and check results are in `.site-review/refinement/`. Desktop and
mobile visual review covers the portrait, CYGNO, polarimetry, new concept figures
and four-photo personal gallery. Axe reports no WCAG A/AA violations at 1440 px
and 390 px. Colour contrast and silent-video captions remain manual-review items;
readable colours, short visible captions and screen-reader descriptions remain.
This does not constitute a complete accessibility audit.

The first navigation run was interrupted by the development server's live
reload. Navigation was rerun against a fixed production build and passed.

Passed: safe Jekyll builds at the root and `/preview` subpath; static checks
on both outputs; `git diff --check`; browser checks at 320, 390, 768, 844, 1024,
1366, 1440 and 1920 px. Browser coverage includes image decoding, overflow,
section tracking, anchor clearance, keyboard navigation, disclosures, legacy
URLs, history, reduced motion and use without JavaScript. The production output
is 5167 KiB, including the two unchanged animation files.

No font, palette, production JavaScript, CV or publication/talk record changes.
No deployment or push. Chromium/WSL checks do not cover physical devices,
Safari or Firefox.
