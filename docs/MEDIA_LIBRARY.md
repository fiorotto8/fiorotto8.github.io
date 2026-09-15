# Media library and compact research illustrations

> The subsequent [content and image refinement](CONTENT_REFINEMENT.md) records
> the smaller portrait, shorter CYGNO copy and expanded image selection.

15 September 2026. Implements the user's requested subject-based image library,
larger-source intake, portrait crop, CYGNO04 pairing, PICOSEC/GIF selections and
use of their own science animations.

## Folder organisation

See [the folder guide](../images/README.md). The entire old image tree was
inventoried before moving files. `IMAGE_LIBRARY.json` records all 135 moves,
pre-move paths and hashes. Every move preserved the file bytes. Empty former
folders were removed after their contents had moved.

- **`images/public/`** contains 36 referenced assets, grouped into identity,
  personal interests, research projects and teaching. These are the only media
  shipped with the website: 26 responsive photo files for 13 photos, two MP4s,
  two poster images, and six identity/manifest assets.
- **`images/local/`** contains 129 existing files: source photographs, unused
  images, higher-resolution versions, prior renditions and unused branding.
  It follows the same subjects, with `retired-renditions/` subfolders where useful.
  The earlier `not-to-use` selection is retained as `personal/not-for-use/`.
- `.gitignore` ignores `/images/local/`. Jekyll excludes `images/local` and
  the library README. No local path is indexed in Git. Previously tracked
  originals appear as removals at their former paths, while the files remain
  safely in the local library. Git history has not been rewritten.

The folder `image_larger_resolution` was distributed into research and teaching
subjects with descriptive filenames. Larger versions replace small exports as
the sources for the optical prototype and the two school photos. The original
4032×3024 PICOSEC group photo replaces the small annotated screenshot. Unselected
large schematics, apparatus and launch pictures remain local. Pixel dimensions
alone do not establish that a processed image contains more original detail.

`PHOTO_SOURCES.json` records the source/hash/subject/widths for the active
selection. `bin/prepare_photos.py` creates the public WebP variants and
`_data/photos.json`. Source files are required only when regenerating media;
normal builds use the checked-in public exports. Ignored originals need a
separate backup and are not included in Git.

## Design and image choices

The wider text layout and light palette are retained. The image treatment changes
from large individual photographs to smaller, related views with direct captions.

- **Portrait:** a square frame, bottom-weighted positioning and a small 1.08×
  CSS enlargement remove excess sky and bring the face closer. This is a
  reversible display crop; the original and exported WebPs remain uncropped.
- **CYGNO04:** the copper vessel and the requested `cygno04-cleanroom.jpeg`
  view appear together at approximately 260 px each on desktop. The caption
  identifies the clean room visible in the picture, rather than calling it a
  control room. Both full photo aspect ratios are retained.
- **PICOSEC:** the test-beam team photograph replaces the readout close-up,
  shown at a maximum width of 400 px.
- **CMS GEM:** two GIF photographs replace the magnet image: detector work
  and the irradiation setup, at approximately 220 px each.
- **Other sections:** the teaching photo is capped at 330 px, school group at
  400 px and optical prototype at 300 px. The personal gallery is narrower.
  Research image pairs stay together on mobile without horizontal overflow.

The Go typography, native scrolling and simple single-page structure remain.
No cards, scroll effects, filters or generated photographic content were added.

## Animations and scientific copy

Read the current local READMEs, scientific-scope notes, review status and licences
in both repositories, and checked the user-supplied GitHub pages. Selected:

- [DirectionalDM_animations — Galactic wind](https://github.com/fiorotto8/DirectionalDM_animations/blob/cda6569b3ec0ba5c2fe4ffed491dacbc06ba9a26/media/videos/01_galactic_wind/480p30/GalacticWind.mp4):
  39.63 seconds, explaining the halo, Solar motion and the apparent incoming wind.
- [XPol_art — tracks to modulation](https://github.com/fiorotto8/XPol_art/blob/f398cebea5c2dc50b9047fb1800c8f2aee6220b3/animations/landscape/480p30/tracks_to_modulation_animation.mp4):
  12 seconds, showing how simulated track directions build a modulation pattern.

Both files are the existing 854×480, 30 fps, silent H.264 previews copied without
alteration. SHA-256 comparisons confirm identical bytes. The existing credit
“By Davide Fiorina via Local Qwen3.8” is preserved. No master render or alteration
of the source repositories was needed. Posters were extracted at 25 s and 8 s
respectively, retaining the complete frame. Exact paths, commits, licences and
hashes are in `ANIMATION_SOURCES.json`.

The players are capped at 480 px, have native controls and fullscreen, and use
`preload="none"` without autoplay. The page makes no MP4 request before playback.
Each video has an accessible label, a caption, a text description and links to
its source and CC BY 4.0 licence. The animation descriptions explain the silent
visual narrative for readers who do not play the video.

The dark-matter paragraph now connects the proposed directional measurement to
the Solar System's motion through a halo. Polarimetry copy explains why many
tracks and a calibrated detector response are required. The polarimetry video
replaces the former charge-readout schematic; the real optical prototype remains
beside the measurement explanation. Simulated distributions are identified as
illustrations, and the text does not claim their numerical results as measured
TPC performance. Scene 05, which the source marks pending collaboration
validation, is not used. No new collaboration-approval claim is made.

## Functionality and checks

The CV, publication/talk/poster datasets and navigation script are unchanged by
SHA-256 comparison. All previous page URLs, deep links and disclosure behaviour
are retained. Metadata, manifest icons and image references now use the public
paths. No new production dependency or JavaScript is introduced.

The static checker now validates video posters and social-image metadata as
asset references, validates manifest icons, rejects published local files, and
fails if any file in `images/public/` is unused.

Passed:

```sh
python3 bin/prepare_photos.py
bash bin/build --safe --destination /tmp/fiorina-media-site
python3 bin/check_site.py /tmp/fiorina-media-site
/tmp/fiorina-site-qa/bin/python bin/check_browser.py --url http://127.0.0.1:4002/ --output .site-review/media-library/checks
bash bin/build --safe --baseurl /preview --destination /tmp/fiorina-media-subpath
python3 bin/check_site.py /tmp/fiorina-media-subpath --baseurl /preview
git diff --check
```

The production site is 4279 KiB including both videos (about 1.94 MiB together)
and every responsive image variant. This is a stored-file total; the videos do
not download until requested. All selected photos retain dimensions and lazy
loading; the portrait is prioritised.

Chromium navigation, overflow, image decoding, keyboard, disclosure, history,
legacy-route, reduced-motion and no-JavaScript checks passed at 1920×1080,
1440×900, 1366×768, 1024×900, 768×1024, 390×844, 320×844 and 844×390.
FFmpeg decoded both complete videos without errors. Playback and seeking were
checked in the Jekyll preview, which supports HTTP byte ranges. The temporary
Python static server returns whole files for range requests, so it is suitable
for layout checks but not for testing video seeking.

Final desktop and mobile screenshots were visually reviewed for the portrait
crop, photo pairs, animation players and surrounding text. Axe reported no
WCAG A/AA violations at 1440×900 and 390×844. Its manual-review items were
colour contrast and video captions: the existing readable palette is retained,
and both silent animations have expandable text descriptions. This is not a
claim of a complete accessibility audit.

Both players passed playback, seeking and end-of-video checks in the Jekyll
preview. Neither MP4 was requested before interaction. Screenshots and machine
results are retained locally in `.site-review/media-library/after/` and
`.site-review/media-library/checks/`.

## Limits

The photo intake and crop do not add information about dates, exact locations,
relationships or results. Research-role wording remains sourced to the supplied
CV. Chromium/WSL verification does not cover Safari, Firefox or physical devices.
The unused and original image files are local-only and must be backed up outside
Git. This work has not committed, pushed or deployed anything.
