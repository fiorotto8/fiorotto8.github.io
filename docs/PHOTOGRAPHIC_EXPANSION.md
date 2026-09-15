# Lighter palette, wider page and a photographic account of work and life

> This records the preceding pass. [MEDIA_LIBRARY.md](MEDIA_LIBRARY.md) records
> the subsequent folder reorganisation, revised image selection and animations.

15 September 2026. Applies the user's next request within the existing
[art-direction prompt](../Universal%20Website%20De-AIification%20and%20Human%20Art%20Direction%20Prompt.md).

## Audit and design thesis

The previous pass made the academic record easier to scan, but its 1120 px
canvas and dark background kept the photographs small. The research descriptions
mostly named technologies and responsibilities. They did not give a reader
outside physics enough explanation of the questions behind the work. Personal
interests were absent because no material had yet been supplied.

The new brief supplies 18 personal images and 14 work images and explicitly
authorises selection, descriptive renaming and photo-based hobby inference.
The page should now read as an illustrated explanation from a working physicist:
the scientific question, the physical instrument, Davide's contribution, and
some life outside the laboratory. Keep the existing single-page architecture,
Go typography and native controls.

Before editing the layout, inspected every supplied image in labelled contact
sheets, opened selected scientific and personal images individually, reviewed
the CV and current copy, ran Jekyll and captured fresh desktop/mobile screenshots.

## Palette, typography and layout

- Light lilac `#f4f0fb`, lavender `#eae7f6` and ice blue `#e7f4f5` backgrounds.
  Dark violet `#241c38` text, muted violet `#5c536e`, teal `#006a73` and
  magenta `#a12676` retain the user's cyberpunk preference in a lighter form.
- Main width increases from 1120 to 1360 px; body type from 17 to 18 px on
  desktop. Paragraph lengths remain bounded. The bibliography widens to 1180 px.
- The Go family already compared in the previous pass remains appropriate for
  the longer science copy and metadata. No additional font or runtime dependency.
- A larger outdoor portrait introduces the person. The previous clean-room
  portrait now accompanies the explanation of day-to-day detector work.
- The copper-vessel assembly photograph anchors CYGNO. The schematic and small
  prototype serve different explanatory roles and retain their full aspect ratios.
- The personal gallery gives the landscape trail photograph more width than
  the two portrait photographs. It becomes two columns on tablet, one on mobile.
- The lighter palette also updates browser chrome, the manifest, favicon,
  application icons and social card. Native section tracking is retained.

## Photographs and provenance

All 32 files were renamed by visible subject, with original bytes preserved.
`PHOTO_SOURCES.json` records original and final paths, SHA-256 hashes, selected
sizes and output keys. No image content was generated, retouched or removed.
The empty user-supplied `images/new_images` file is preserved and excluded.

Selected eleven new images:

| Placement | Selected subject |
| --- | --- |
| Introduction | Outdoor portrait at dusk |
| CYGNO | Copper vessel during assembly |
| X-ray polarimetry | Photoelectron-tracking schematic and optical TPC prototype |
| Earlier research | PICOSEC prototype/readout and magnetic-field test apparatus |
| Teaching | Detector-school bench and Gran Sasso school group |
| Outside the lab | Hillside trail running, steam locomotive museum, mountain-lake walk |

The schematic depicts charge readout; its caption explicitly distinguishes the
optical prototype's camera readout. It is not presented as an engineering drawing
of CYGNO or its optical prototype. The rocket-launch image is unused because no
specific connection to Davide's mission work was supplied. Small source images
stay at modest display sizes; no upscaling is performed during asset generation.

Only selected responsive WebP versions are published. Source folders remain
available in the repository and are excluded from the Jekyll output. Images keep
dimensions, useful alt text and native lazy loading below the introduction.
`bin/prepare_photos.py` generates the assets with Pillow and `_data/photos.json`;
ordinary Jekyll builds serve them directly.

## Editorial pass and scientific sources

The research now explains gas ionisation, optical tracking, why recoil direction
matters, how photoelectron directions encode polarisation, and why calibration
and simulations are part of a measurement. Separate paragraphs describe Davide's
coordination, integration and analysis responsibilities. PICOSEC and CMS are
still earlier work; neutrino concepts and EXPO remain developing/proposed work.
The 10–60 keV range remains an aim, without adding a new sensitivity claim.

Responsibility statements come from the supplied CV and existing source pages.
General explanations were checked against primary sources:

- [CYGNO04 experiment description](https://web.infn.it/cygnus/the-experiment/):
  400 L demonstrator and ionisation, amplification and optical tracking principle.
- [INFN Roma CYGNO research description](https://www.roma1.infn.it/en/ricerca/csn2/cygno.html):
  the use of recoil directions to distinguish a possible signal from backgrounds.
  Its older scale-up specification was not used for the current detector volume.
- [Fiorina et al., optical TPC polarimetry preprint](https://arxiv.org/abs/2510.26239):
  the scientific scope and photoelectron-tracking approach. Publication metadata
  and the existing cautious energy-range wording are retained.

Hobby copy is inferred within Davide's explicit authorisation from the supplied
photographs and his examples of trains and trail running. Mountain walking is
also directly represented. No exact locations, race names, results, frequency,
relationships or personal history have been inferred. The gallery excludes
unneeded group/celebration photos rather than inventing stories for them.

The subtraction pass removes redundant portrait captions and generic biography
or teaching sentences. It adds no claims about achievements, detector records,
photograph ownership or scientific approval.

## Preserved functionality

Jekyll/GitHub Pages, all previous URLs and research fragments, publication/talk/
poster data, CV PDF, no-JavaScript navigation, native disclosures, reduced motion,
print expansion and scroll tracking retain their operating model. No production
JavaScript changes are needed. Browser checks now load photographs within closed
research details, and the final-section test scrolls to the end rather than
assuming the former short About section still fits within 200 px of Contact.

## Validation and visual QA

Passed:

```sh
python3 bin/prepare_photos.py
bash bin/build --safe --destination /tmp/fiorina-photo-site
python3 bin/check_site.py /tmp/fiorina-photo-site
/tmp/fiorina-site-qa/bin/python bin/check_browser.py --url http://127.0.0.1:4001/ --output .site-review/photographic-expansion/checks
bash bin/build --safe --baseurl /preview --destination /tmp/fiorina-photo-subpath
python3 bin/check_site.py /tmp/fiorina-photo-subpath --baseurl /preview
node --check assets/js/site.js
git diff --check
```

The production output contains eight pages and is **2197 KiB**, including all
responsive image variants, the CV and fonts. Selected new photo variants total
1615 KiB; the browser chooses one size per photograph. These are stored file
sizes, not a claim about measured load time. The source-photo folders and
local/private/development material are absent from both production and preview.

SHA-256 checks confirm the CV PDF, all three scholarly record datasets and the
navigation script are unchanged. All 32 renamed source images retain their
original hashes. Every selected WebP decodes at its declared dimensions.

Chromium navigation and image checks passed at 1920×1080, 1440×900, 1366×768,
1024×900, 768×1024, 390×844, 320×844 and 844×390. Checks cover overflow,
image decoding including closed research disclosures, section tracking, target
clearance below the header, keyboard focus, details, old routes and fragments,
browser history, reduced motion and no-JavaScript fallback. Print expansion and
restoration of disclosure state also passed.

Actual browser zoom was set and read back with Chromium's zoom API: 150% and
200%, yielding CSS viewports of 911×512 and 683×384 from a 1366×768 window.
Navigation and reflow passed. This was not merely a resized-viewport simulation.

axe-core 4.10.3 found zero WCAG A/AA or 2.1 AA rule violations in the expanded
desktop and mobile pages. Colour cases requiring manual review were checked
against the three actual solid backgrounds. Minimum contrast ratios are 13.29:1
for body text, 5.92:1 for muted text, 5.22:1 for teal and 5.65:1 for magenta.

Visually inspected matched before/after laptop introductions, desktop and mobile
research, teaching, bibliography, earlier projects, biography/personal gallery,
contact and 404 layouts. The schematic retains its labels; photographs are not
cropped or distorted. The light social card and application icons were rendered
from their editable SVG sources, and the social card was inspected.

Evidence: `.site-review/photographic-expansion/` contains labelled inventories,
source snapshots, `before/`, `pass-1/`, `after/`, `checks/` and `contrast.json`.
The live development preview at `http://127.0.0.1:4000/` was restarted with the
updated exclusions, and its assets were compared with the reviewed production
build. No content was committed, pushed or published.

## Remaining limitations

Personal copy uses only the supplied visual evidence and stated interests; a
specific anecdote would still need Davide's words. Current role wording remains
grounded in the supplied CV. This pass is not a new verification of every
historical paper, talk or appointment. Changes remain local and unpublished.
Browser checks used Chromium on Linux/WSL; Safari, Firefox, physical devices and
a screen-reader session were not tested. Automated accessibility results do not
constitute full WCAG certification. Small supplied images retain their original
resolution limits.
