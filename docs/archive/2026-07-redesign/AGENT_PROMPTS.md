> Historical document. Superseded by the September 2026 request; see `/AGENTS.md` and `/docs/WEBSITE_REVIEW.md`.

# Claude Code Prompts

## How to use these prompts

Run one prompt at a time.

After Claude Code finishes a phase:

1. read its summary;
2. inspect `git diff`;
3. run the local site;
4. review the relevant page in a browser;
5. correct issues before continuing;
6. commit only the reviewed phase.

Do not paste all prompts at once.

---

## Prompt 0 — Baseline and plan validation

```text
Read CLAUDE.md and these files:

- docs/redesign/CURRENT_SITE_AUDIT.md
- docs/redesign/MASTER_SPEC.md
- docs/redesign/IMPLEMENTATION_SEQUENCE.md
- docs/redesign/QA_ACCEPTANCE_CHECKLIST.md

Do not edit the website yet.

Tasks:
1. Run git status --short and report the current branch.
2. Inspect the current Jekyll structure and confirm the key files named in the audit exist.
3. Run the existing production build using the repository's documented build command.
4. Identify any baseline build errors, warnings, broken references, or missing dependencies.
5. Produce a concise implementation map listing the exact files you expect to create or edit in Phases 1–8.
6. Flag any conflict between the documentation and the actual repository.

Do not redesign, rewrite, commit, or push. Stop after the report.
```

---

## Prompt 1 — Layout and SCSS foundation

```text
Implement Phase 1 from docs/redesign/IMPLEMENTATION_SEQUENCE.md.

Read:
- CLAUDE.md
- docs/redesign/MASTER_SPEC.md, especially sections 11–13
- docs/redesign/QA_ACCEPTANCE_CHECKLIST.md

Scope:
- create _layouts/portfolio-page.html
- create _sass/_site-refresh.scss
- modify assets/css/main.scss only as required to import the new partial

Requirements:
- retain Jekyll and the existing default layout;
- do not modify page content yet;
- do not modify unrelated inherited theme files;
- omit the sidebar in the new layout;
- use semantic main content;
- implement the design tokens, basic wrapper, typography, buttons, cards, tags, focus states, breakpoints, and reduced-motion rules;
- namespace the new component classes to minimise regressions;
- do not add JavaScript;
- do not add external font dependencies.

Before editing, show the files you will touch.
After editing:
1. run git diff --check;
2. run the production Jekyll build;
3. report changed files, build result, and manual checks required.

Do not commit, push, or begin Phase 2. Stop.
```

---

## Prompt 2 — Homepage

```text
Implement Phase 2 from docs/redesign/IMPLEMENTATION_SEQUENCE.md.

Read:
- CLAUDE.md
- docs/redesign/MASTER_SPEC.md sections 5, 11, and 12
- docs/redesign/PAGE_COPY_DRAFTS.md, Homepage section
- docs/redesign/QA_ACCEPTANCE_CHECKLIST.md

Primary scope:
- modify _pages/about.md
- modify _sass/_site-refresh.scss only when homepage-specific styles are needed
- create at most one small reusable include if it clearly reduces duplication
- use existing images only

Requirements:
- use layout: portfolio-page;
- preserve permalink /;
- build the hero, status strip, current research cards, earlier detector programmes, selected work, teaching teaser, and contact block;
- use one fixed profile or laboratory portrait;
- do not use the random profile system;
- do not duplicate the navigation in a Start Here list;
- keep the scientific text faithful to PAGE_COPY_DRAFTS.md;
- maximum two playful lines on the entire homepage;
- add descriptive alt text;
- do not invent links, metrics, roles, or outputs;
- link research cards to valid anchors that will exist after Phase 3;
- make the page usable at 390 px width.

Before editing, inspect the available profile images and state which one you selected and why, using only visible file properties and existing image review. Do not select files from a not-to-use directory.

After editing:
1. run git diff --check;
2. run the production build;
3. count the playful lines and report them;
4. report files changed and manual viewport checks needed.

Do not commit, push, or begin Phase 3. Stop.
```

---

## Prompt 3 — Research page

```text
Implement Phase 3 from docs/redesign/IMPLEMENTATION_SEQUENCE.md.

Read:
- CLAUDE.md
- docs/redesign/MASTER_SPEC.md section 6
- docs/redesign/PAGE_COPY_DRAFTS.md, Research Page section
- docs/redesign/QA_ACCEPTANCE_CHECKLIST.md

Scope:
- modify _pages/portfolio.html
- modify _sass/_site-refresh.scss only for research-page components
- update image references only when necessary

Required structure:
- concise introduction;
- Current research:
  1. CYGNO04 as the visually dominant feature;
  2. optical TPCs for X-ray polarimetry;
  3. neutrinos, CEvNS, and space instrumentation;
- Previous projects:
  1. PICOSEC;
  2. CMS GEM.

Each project must contain:
- status label;
- title;
- scientific objective;
- image;
- My role;
- no more than three focus bullets;
- tags or verified links.

Required anchors:
- #cygno04
- #xray-polarimetry
- #new-rd
- #picosec
- #cms-gem

Humour:
- maximum two playful lines or captions across the whole page;
- report exactly which lines count toward this total.

Accuracy:
- preserve all five research areas;
- do not invent results, funding, responsibilities, or links;
- keep official experiment names.

After editing:
1. run git diff --check;
2. run the production build;
3. verify the five anchors in generated HTML or source;
4. report changed files, humour count, and manual checks.

Do not commit, push, or begin Phase 4. Stop.
```

---

## Prompt 4 — Publications and talks

```text
Implement Phase 4 from docs/redesign/IMPLEMENTATION_SEQUENCE.md.

Read:
- CLAUDE.md
- docs/redesign/MASTER_SPEC.md sections 7 and 8
- docs/redesign/PAGE_COPY_DRAFTS.md, Publications Page and Talks Page sections
- docs/redesign/QA_ACCEPTANCE_CHECKLIST.md

Scope:
- modify _pages/publications.md
- modify _pages/talks.html
- modify _sass/_site-refresh.scss only as needed

Publications requirements:
- preserve every existing selected publication and its link;
- preserve official titles exactly;
- create a compact metrics panel with the existing verified numbers and update date;
- retain Scopus, ORCID, and CV links;
- remove the humorous annotation below every paper;
- use at most one playful sentence on the page;
- do not invent journal names, authorship roles, or contribution claims.

Talks requirements:
- preserve all current talks and posters;
- sort talks reverse chronologically;
- create a Featured talks section with at most four items selected from the existing list;
- retain invited/plenary/parallel type only when already stated;
- retain posters as a separate section;
- add links only if already present or verified in the repository;
- use at most one playful sentence on the page.

Validation:
- before editing, record the number of selected publications, talks, and posters;
- after editing, report the same counts and explain any difference;
- compare all publication URLs before and after.

After editing:
1. run git diff --check;
2. run the production build;
3. report count preservation, humour count, and manual checks.

Do not commit, push, or begin Phase 5. Stop.
```

---

## Prompt 5 — Teaching and CV

```text
Implement Phase 5 from docs/redesign/IMPLEMENTATION_SEQUENCE.md.

Read:
- CLAUDE.md
- docs/redesign/MASTER_SPEC.md sections 9 and 10
- docs/redesign/PAGE_COPY_DRAFTS.md, Teaching & Outreach Page and CV Page sections
- docs/redesign/QA_ACCEPTANCE_CHECKLIST.md

Scope:
- modify _pages/teaching.html
- modify _pages/cv.md
- modify _sass/_site-refresh.scss only as needed

Teaching requirements:
- retain the two current images;
- create four clear cards: Student supervision, Laboratory teaching, Outreach, Scientific service;
- preserve the factual scope of all four areas;
- maximum two playful lines on the page;
- descriptive alt text;
- no unsupported numeric claims.

CV requirements:
- preserve the PDF file and its path;
- add a primary Download CV action;
- add a secondary Open PDF in new tab action;
- retain the embed only if it remains usable;
- provide a mobile fallback message;
- no jokes;
- do not modify files/CV.pdf.

After editing:
1. run git diff --check;
2. run the production build;
3. verify both CV links resolve to the existing PDF path;
4. report changed files, humour count, and manual checks.

Do not commit, push, or begin Phase 6. Stop.
```

---

## Prompt 6 — Navigation, metadata, and profile cleanup

```text
Implement Phase 6 from docs/redesign/IMPLEMENTATION_SEQUENCE.md.

Read:
- CLAUDE.md
- docs/redesign/MASTER_SPEC.md sections 4 and 14
- docs/redesign/PAGE_COPY_DRAFTS.md, Fixed Profile / Short Bio section
- docs/redesign/QA_ACCEPTANCE_CHECKLIST.md

Scope:
- _data/navigation.yml
- _config.yml
- _includes/author-profile.html
- _sass/_masthead.scss or _sass/_sidebar.scss only if necessary
- _sass/_site-refresh.scss only if necessary

Requirements:
- keep the existing public URLs;
- use navigation labels Research, Publications, Talks, Teaching, CV;
- ensure the site name links to /;
- remove random profile-image JavaScript;
- use one fixed image;
- keep the legacy author profile functional but simple;
- no primary redesigned page should display the old sidebar;
- update site description and short author bio only with wording from PAGE_COPY_DRAFTS.md;
- do not add unverified social profiles;
- do not expose additional personal information;
- do not broadly delete unused theme infrastructure.

After editing:
1. search the repository for js-random-profile-avatar and random-profile-avatar;
2. confirm no active random profile code remains;
3. run git diff --check;
4. run the production build;
5. report changed files and manual navigation checks.

Do not commit, push, or begin Phase 7. Stop.
```

---

## Prompt 7 — Image optimisation

```text
Implement Phase 7 from docs/redesign/IMPLEMENTATION_SEQUENCE.md.

Read:
- CLAUDE.md
- docs/redesign/MASTER_SPEC.md sections 11 and 15
- docs/redesign/QA_ACCEPTANCE_CHECKLIST.md

Do not process all repository images blindly.

Tasks:
1. Inventory only images used by the redesigned homepage, research page, and teaching page.
2. Report current dimensions and file sizes.
3. Propose an exact conversion table before changing files:
   - source path;
   - destination path;
   - target dimensions;
   - target format;
   - reason.
4. Preserve source images until converted versions are verified.
5. Convert photographic images to WebP where useful.
6. Do not damage labels in plots or diagrams.
7. Use git mv for any filename cleanup.
8. Update all references.
9. Add loading=lazy and decoding=async below the fold.
10. Do not lazy-load the hero image.
11. Add explicit dimensions or stable aspect ratios where practical.

After editing:
- verify every referenced image exists;
- report before/after total byte size for the processed set;
- run git diff --check;
- run the production build;
- list images that require visual inspection.

Do not commit, push, or begin Phase 8. Stop.
```

---

## Prompt 8 — Final QA

```text
Perform Phase 8 from docs/redesign/IMPLEMENTATION_SEQUENCE.md.

Read:
- CLAUDE.md
- docs/redesign/QA_ACCEPTANCE_CHECKLIST.md

Do not add new features.

Tasks:
1. Run the production Jekyll build.
2. Run git diff --check.
3. Review generated pages for:
   - missing images;
   - broken internal links;
   - invalid heading order;
   - duplicate IDs;
   - empty links;
   - missing alt text;
   - old sidebar leakage;
   - random profile code;
   - humour-budget violations.
4. Inspect CSS for horizontal overflow risks at 390 px.
5. Check the five primary navigation links and CV PDF path.
6. Compare publication, talk, and poster counts against the pre-redesign source.
7. Review all changed scientific wording for unsupported claims.
8. Produce a checklist report using the IDs in QA_ACCEPTANCE_CHECKLIST.md.
9. Fix only objective defects found during QA.
10. Re-run tests after fixes.

Do not commit, push, merge, or open a pull request. Stop with:
- pass/fail table;
- remaining manual browser checks;
- exact files changed during QA.
```

---

## Prompt 9 — Prepare reviewed commit

Use only after manually reviewing the phase:

```text
Review the current git diff for the completed phase.

Tasks:
1. Confirm the diff is limited to the intended phase.
2. Summarise the user-visible changes.
3. Run git diff --check and the production Jekyll build once more.
4. If both pass, create one commit with a concise conventional message beginning with redesign:, perf:, or qa: as appropriate.
5. Show the commit hash and git status --short.

Do not push.
```

---

## Prompt 10 — Prepare draft pull request

Use only after all phases and manual QA:

```text
Read CLAUDE.md and docs/redesign/QA_ACCEPTANCE_CHECKLIST.md.

Confirm:
- working tree is clean;
- all redesign commits are on the redesign branch;
- production build passes;
- mandatory QA items pass.

Then:
1. summarise commits relative to master;
2. push the redesign branch to origin;
3. prepare a draft pull request to master titled:
   "Redesign academic website as a technical research portfolio"
4. Include:
   - design summary;
   - page changes;
   - content and humour strategy;
   - performance changes;
   - testing performed;
   - remaining manual checks.

Do not merge.
```
