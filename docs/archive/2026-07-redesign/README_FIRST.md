> Historical document. Superseded by the September 2026 request; see `/AGENTS.md` and `/docs/WEBSITE_REVIEW.md`.

# Davide Fiorina Website Redesign Package

## Purpose

This package is the authoritative implementation guide for redesigning:

- Live site: `https://fiorotto8.github.io/`
- Repository: `fiorotto8/fiorotto8.github.io`
- Platform: Jekyll on GitHub Pages
- Current theme lineage: AcademicPages / Minimal Mistakes

The strategy is intentionally separated from the implementation. The human decision is already made here; Claude Code should execute it rather than invent a new direction.

## Core decision

The new site should be a **modern dark technical portfolio with a controlled amount of humour**.

"Dark" means deep blue-charcoal editorial styling — scientific, restrained, and high-contrast. It does not mean neon, terminal, or cyberpunk aesthetics.

It must not become:

- a sterile institutional profile;
- a startup landing page full of slogans;
- a hacker terminal or neon-on-black "cyberpunk" aesthetic;
- a complete rewrite in React, Astro, Next.js, or another framework;
- an AI-generated collection of metaphors;
- a visually noisy page with gradients, animated particles, typewriter text, or excessive motion.

It should feel like:

- an experimental physicist built it;
- the research is serious and technically credible;
- the author has a recognisable personality;
- the page is easy to scan in under one minute;
- deeper details are available without dominating the first screen.

## Documents in this package

1. `CLAUDE.md`  
   Persistent repository instructions. Place this file in the repository root.

2. `CURRENT_SITE_AUDIT.md`  
   What is currently working, what is dated, and what must be preserved.

3. `MASTER_SPEC.md`  
   Product goals, design direction, information architecture, design tokens, and technical constraints.

4. `PAGE_COPY_DRAFTS.md`  
   Proposed wording and humour placement for each main page.

5. `IMPLEMENTATION_SEQUENCE.md`  
   The exact phased implementation order, files to touch, and expected commits.

6. `CLAUDE_CODE_PROMPTS.md`  
   Copy-paste prompts to run one phase at a time in Claude Code.

7. `QA_ACCEPTANCE_CHECKLIST.md`  
   Objective tests that must pass before deployment.

8. `POWERSHELL_SETUP.md`  
   Safe setup and execution instructions for Windows PowerShell.

## Required working method

Do not ask Claude Code to “redesign the whole website” in one prompt.

Use this sequence:

1. Put `CLAUDE.md` in the repository root.
2. Put the other documents under `docs/redesign/`.
3. Create a dedicated branch.
4. Run the prompts in `CLAUDE_CODE_PROMPTS.md` one at a time.
5. Review the browser result after every phase.
6. Commit each phase separately.
7. Merge only after the QA checklist passes.

## Important content principle

The goal is not to remove humour. The goal is to stop every paragraph, caption, and publication from competing to be the funniest line on the page.

Use humour as punctuation:

- factual sentence;
- factual sentence;
- occasional human line;
- back to the science.

The final result should contain fewer jokes, but the jokes that remain should feel more clearly like Davide rather than generic “clever AI” copy.
