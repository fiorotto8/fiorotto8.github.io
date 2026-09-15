# Image and animation library

Only `public/` is published. It contains the image sizes and two animation
previews actually referenced by the website, organised by subject:

```text
images/
  public/
    identity/                 favicon, icons, social card, manifest
    personal/
      portraits/              homepage portrait
      trails/                 trail running
      mountains/              Fitz Roy portrait
      trains/                 railway museum
      travel-and-life/        penguin enclosure visit
    research/
      cygno/                  copper vessel, clean-room TPC, assembly, animation
      polarimetry/            prototype, laboratory work, schematic, animation
      neutrinos/              CEνNS detector concept
      expo/                   instrument and spacecraft concepts
      picosec/                test-beam team
      cms-gem/                GIF detector work and setup
    teaching/                 detector schools and public talk
  local/                      ignored by Git and excluded from Jekyll
    identity/                 unused branding and editable social-card source
    personal/                 originals and unused personal photographs
    research/                 originals, larger versions and unused research images
    teaching/                 originals and larger school photographs
```

`local/` follows the same subjects. `retired-renditions/` within those subjects
holds previous web exports. `personal/not-for-use/` preserves the pre-existing
selection restriction. Nothing in the local library is deleted by the build.

## Updating the published selection

1. Put the original in the appropriate subject under `local/`.
2. Record its path/hash, subject (`area`) and desired widths in
   `docs/PHOTO_SOURCES.json`. A nonempty `widths` list selects a photograph.
3. Run `python3 bin/prepare_photos.py` with Pillow installed. It generates
   responsive WebP files and `_data/photos.json`; no upscaling is allowed.
4. Use `_includes/photo.html` from the page. Move any retired exports to the
   corresponding local subject folder.
5. Build and run `python3 bin/check_site.py`. The check rejects missing assets,
   published local files and files in `public/` that the site does not reference.

Keep originals backed up separately: ignored files are not stored in Git.
Jekyll builds only need the published exports, not Pillow or local originals.

The portrait has a reversible CSS crop; its original and WebP files remain
uncropped. The trail-running hillside image shows only its left half through CSS.
Other photographs and technical figures keep their full aspect ratios. Animation
previews are copied without changes, including their credits, from Davide's
two source repositories. They use native controls, `preload="none"` and screen-reader
descriptions. No autoplay or external video embed is used.

## Provenance

- `docs/IMAGE_LIBRARY.json`: original moves, subsequent intakes and pre-move hashes.
- `docs/PHOTO_SOURCES.json`: selected source versions and generation settings.
- `docs/ANIMATION_SOURCES.json`: exact source paths, commits, hashes and posters.
- `docs/MEDIA_LIBRARY.md`: decisions and verification for this reorganisation.

The larger-resolution intake folder was distributed across the subject folders.
An increased pixel count in a supplied processed image is not a claim of newly
recovered photographic detail.
