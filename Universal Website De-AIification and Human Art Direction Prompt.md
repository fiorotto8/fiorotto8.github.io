# UNIVERSAL WEBSITE DE-AIIFICATION & HUMAN ART DIRECTION PROMPT

You are working on an EXISTING WEBSITE.

Your task is to perform a comprehensive HUMAN ART DIRECTION AND EDITORIAL REFINEMENT PASS.

The website may already be technically complete.

Do not assume it needs to be rebuilt.

Your objective is to remove the visual, structural, typographic, interaction, and writing patterns that make websites look obviously AI-generated, template-generated, automatically designed, or assembled from generic modern-web conventions.

The final website should feel:

- intentionally designed;
- deliberately written;
- specific to its subject;
- internally coherent;
- editorially considered;
- visually distinctive without being theatrical;
- appropriate to the organization, project, product, institution, person, publication, or subject it represents;
- difficult to mistake for a generic AI-generated website.

Do not merely make the website "better."

Do not merely make it "modern."

Do not merely make it "clean."

Do not simply replace one fashionable design language with another.

Discover what THIS website should look and sound like.

Then refine the existing website toward that identity.

The core principle is:

> Preserve the machine. Replace the generic visual and editorial language surrounding it.

---

# 1. DO NOT START CODING IMMEDIATELY

Before making changes, investigate the project.

Do not open the first CSS file and start changing colors.

Do not immediately install fonts.

Do not immediately change border-radius.

Do not decide that the site needs dark mode, gradients, cards, animation, serif typography, brutalism, minimalism, or any other aesthetic before understanding the project.

First perform design archaeology.

Determine:

- what the website actually is;
- who it is for;
- what its content is trying to communicate;
- which parts are authoritative;
- how its architecture works;
- which behaviors are intentional;
- which components are data-driven;
- which pages matter most;
- what visual identity is already latent in its content;
- what currently makes it look generic or machine-produced.

Do not implement until you can answer those questions.

---

# 2. READ THE REPOSITORY AS A CONTRACT

Inspect all relevant project documentation before changing presentation.

Look for files such as:

README
CONTRIBUTING
AGENTS
CLAUDE
CODEX
architecture documentation
content-editing documentation
design documentation
package configuration
framework configuration
theme configuration
routing configuration
CMS configuration
data schemas
content schemas
test documentation
deployment documentation

Determine which files are:

AUTHORITATIVE SOURCES

and which files are:

GENERATED OUTPUTS.

Never edit generated files manually when an authoritative source and generation workflow exist.

Understand:

- content sources;
- routes;
- templates;
- CMS behavior;
- components;
- backend dependencies;
- data synchronization;
- asset processing;
- API usage;
- forms;
- user authentication if present;
- search;
- navigation;
- deployment;
- build scripts;
- testing;
- localization;
- analytics;
- accessibility behavior.

Treat documented architecture as a constraint.

A visual redesign does not justify quietly changing the application's operating model.

---

# 3. PRESERVATION CONTRACT

Unless the task explicitly requires otherwise, preserve existing:

- URLs;
- routes;
- navigation destinations;
- data models;
- schemas;
- database behavior;
- API contracts;
- application state;
- forms;
- authentication;
- CMS workflows;
- update workflows;
- generated-content workflows;
- backend behavior;
- JavaScript behavior;
- server behavior;
- analytics;
- search;
- accessibility semantics;
- SEO semantics;
- heading structure where semantically correct;
- image meaning;
- alt-text purpose;
- figure captions;
- structured metadata;
- user permissions;
- responsive functionality;
- reduced-motion support;
- localization;
- integrations;
- deployment assumptions;
- testing infrastructure.

Do not rebuild functional systems merely because a new layout would be easier to implement.

Do not duplicate authoritative data.

Do not turn data-driven content into manually maintained HTML.

Do not hard-code content that currently comes from a structured source.

Do not introduce a page builder merely for styling.

Do not introduce a frontend framework solely to change appearance.

Do not replace working components simply because you prefer another implementation pattern.

Presentation changes should remain presentation changes whenever reasonably possible.

---

# 4. DETERMINE WHETHER THIS IS A VISUAL REFINEMENT OR A PRODUCT REDESIGN

Assume this is a visual/editorial refinement unless the user explicitly requests changes to information architecture or product behavior.

The existing website may already have:

- correct content;
- correct section order;
- correct functionality;
- correct page hierarchy;
- correct workflows.

Do not confuse:

"this looks generic"

with:

"this structure is wrong."

Generic appearance is often caused by:

- typography;
- spacing;
- excessive card use;
- repetitive composition;
- generic copy;
- uniform radii;
- predictable hero structures;
- poor image art direction;
- generic CTAs;
- generic iconography;
- weak editorial hierarchy.

Fix those first.

---

# 5. RENDER THE CURRENT WEBSITE

Do not judge design from source code alone.

Run the project using its intended local-development workflow.

Use a real browser.

Inspect representative pages at minimum in:

desktop
short laptop
tablet
mobile

Capture BEFORE screenshots.

If the application supports multiple key states, inspect those too.

For example:

homepage
major landing page
content-heavy page
listing/archive page
detail page
form
navigation open state
footer
empty state
error state
modal/dialog if important
authenticated state if appropriate and locally available

You need rendered evidence.

Source code can tell you what the CSS intends.

Screenshots tell you what the user sees.

---

# 6. CREATE A VISUAL AI-TELL AUDIT

Before editing, identify recurring patterns that make the current website feel generated rather than art-directed.

Do not write vague findings like:

"The website feels too AI."

Write observations that name the actual pattern.

For example:

"The same rounded panel, padding, border and shadow treatment is used for services, testimonials, statistics and navigation, causing unrelated information to feel generated from one component recipe."

Audit specifically for the following.

## GENERIC TYPOGRAPHY

Look for:

Inter everywhere
Roboto everywhere
Open Sans everywhere
Arial-like neutral sans everywhere
generic system font stacks
geometric sans fonts used without reason
monospace used just to communicate "technology"
oversized headings compensating for weak typography
identical heading treatment on every section
lack of meaningful typographic contrast
generic heavy-bold headline plus small gray body-copy formula

## GENERIC HEROES

Look for:

huge centered headline
small eyebrow above it
gradient-highlighted keyword
one paragraph underneath
two pill buttons
three statistic cards
floating abstract image
purple or blue glow
blurred orb
generic dashboard mockup
meaningless trust badges
decorative arrows
floating feature pills

## COMPONENT MONOCULTURE

Look for:

everything inside cards
every card having the same radius
every section using the same maximum width
three equal columns repeated endlessly
icon + heading + text cards
uniform padding everywhere
every block having a background panel
every section containing an eyebrow label
every CTA looking identical
every piece of metadata being a badge

## GENERIC COLOR LANGUAGE

Look for:

purple-to-blue gradients
cyan glow
neon blue on black
overused dark mode
arbitrary pastel gradients
washed-out gray text
glassmorphism
transparent panels with blur
accent colors distributed everywhere without hierarchy

## GENERIC SPACING

Look for:

the same section padding everywhere
mathematically equal whitespace
identical gaps between every content relationship
huge empty areas without compositional purpose
repetitive alternating sections
sections that feel generated by a loop

## GENERIC IMAGERY

Look for:

stock photography
abstract AI illustrations
meaningless gradients
floating 3D objects
generic blob graphics
decorative screenshots without context
all images receiving identical rounded frames
images used only because a template expects an image

## GENERIC INTERACTION

Look for:

everything animating on scroll
every element fading upward
constant hover transforms
floating elements
parallax without purpose
animated gradient backgrounds
cursor effects
button arrows sliding everywhere
unnecessary carousel behavior

## GENERIC WRITING

Look for:

"Unlock..."
"Elevate..."
"Discover..."
"Transform..."
"Reimagine..."
"Empower..."
"Supercharge..."
"Revolutionize..."
"Seamless..."
"Effortless..."
"Next-generation..."
"Cutting-edge..."
"Game-changing..."
"Designed to..."
"Built to..."
"Built for..."
"Whether you're..."
"In today's fast-paced..."
"At [company], we believe..."
"We're passionate about..."
"Your journey starts here."
"Take your X to the next level."
"Experience the future of..."
"Where innovation meets..."
"Powerful. Simple. Intuitive."
"Smarter. Faster. Better."

Also identify:

excessive em dashes;
repeated three-part slogans;
overuse of rhetorical questions;
fake conversational enthusiasm;
constant second-person sales language;
generic benefits without evidence;
repetitive "not just X, but Y" constructions;
sentence fragments used mechanically;
excessive adjectives;
generic claims such as "world-class";
SEO phrases repeated unnaturally;
copy that could belong to almost any company after changing the nouns.

---

# 7. DISTINGUISH GENERIC FROM SIMPLY CONVENTIONAL

Do not remove standard patterns merely because AI often uses them.

Some conventions are useful.

For example:

buttons should still look clickable;
navigation should remain understandable;
forms should remain familiar;
body text should remain readable;
links should remain identifiable;
mobile menus should remain usable.

The goal is not novelty at any cost.

The goal is specificity and judgment.

A conventional solution used intentionally is better than a novel solution that hurts usability.

---

# 8. EXTRACT THE WEBSITE'S REAL IDENTITY

Do not invent the design identity from current web trends.

Derive it from the project's actual material.

Study:

- subject matter;
- language;
- users;
- history;
- location;
- industry;
- physical products;
- scientific material;
- architecture;
- photographs;
- diagrams;
- illustrations;
- existing brand assets;
- logos;
- documents;
- typography already used offline;
- packaging;
- print materials;
- institutional context;
- cultural references;
- product interfaces;
- existing visual assets.

Ask:

What does this organization actually produce?

What does it care about?

What distinguishes it from competitors or peers?

What physical or conceptual materials belong naturally to its world?

What visual characteristics are already present in the content?

The design language should emerge from those answers.

---

# 9. WRITE AN INTERNAL DESIGN THESIS

Before implementation, write a short internal design thesis.

It should answer:

1. What is this website fundamentally about?

2. Who is it speaking to?

3. What should a visitor feel?

4. What currently makes it look generic?

5. Which existing visual elements are worth preserving?

6. What kind of typography belongs to this subject?

7. What kind of imagery belongs to this subject?

8. What visual tension or contrast defines the project?

9. What one visual device could make the site recognizable?

10. What fashionable design approaches would be inappropriate?

Do not begin serious styling until the thesis is coherent.

---

# 10. CHOOSE A SPECIFIC DESIGN DIRECTION

Do not aim for:

"modern, sleek and professional."

Those words are not a design direction.

Choose language specific enough to reject alternatives.

Examples:

archival editorial + industrial engineering

Swiss publication design + warm natural materials

museum catalogue + understated luxury craftsmanship

academic journal + experimental instrumentation

independent magazine + documentary photography

civic institution + contemporary information design

heritage manufacturing + precision technical drawing

coastal hospitality + vernacular Mediterranean typography

The exact direction should come from the project.

Do not choose these examples mechanically.

---

# 11. TYPOGRAPHY SHOULD CARRY IDENTITY

Typography is usually the fastest way to make an AI-generated website feel authored.

Do not simply keep the default font because changing it seems risky.

Do not simply install the fashionable font currently popular on design websites.

Avoid defaulting automatically to:

Inter
Roboto
Arial
Open Sans
system-ui
generic geometric sans families

This does not mean those fonts are forbidden.

It means they require a reason.

Select typography according to:

subject
audience
reading density
content length
brand character
available weights
italics
numerals
symbols
languages
technical requirements

Consider whether the site benefits from:

one family;
two complementary families;
occasionally a third specialized face.

Do not automatically create a three-font system.

---

# 12. TEST FONTS ON REAL CONTENT

Do not select typography from a specimen website alone.

Create multiple plausible font combinations.

Render them using real website material such as:

main headline;
long paragraph;
navigation;
metadata;
numbers;
technical terms;
captions;
button;
article title;
table;
product name.

Compare actual browser screenshots.

Select the type system that works best across the real content.

Evaluate:

character;
readability;
line length;
letter shapes;
numerals;
italics;
 punctuation;
technical symbols;
special characters;
language support.

---

# 13. BUILD HIERARCHY WITH MORE THAN SIZE

Do not rely on enormous headings.

Hierarchy can come from:

font family
font weight
font width
italic
line height
letter spacing
case
indentation
alignment
position
contrast
whitespace
rules
measure

Use those tools.

A 70px heading is not automatically more designed than a 42px heading.

Frequently it is merely louder.

---

# 14. BODY TEXT MUST BE EDITORIALLY COMFORTABLE

Long-form reading should normally use an intentional measure.

Aim for approximately 55–75 characters per line where appropriate.

Do not stretch explanatory prose across huge desktop containers.

Do not center paragraphs except in very short intentional compositions.

Give paragraphs enough line height.

Use muted text carefully.

Secondary text must remain readable.

Do not reduce contrast purely to look sophisticated.

---

# 15. CREATE A SMALL VISUAL TOKEN SYSTEM

Before styling every page independently, establish deliberate foundations.

Define useful recurring tokens for:

typography;
text color;
background;
surface;
rules;
accent;
spacing;
container widths;
reading measure;
wide measure;
radius;
motion.

Keep the system compact.

Do not create 70 design tokens simply because large design systems do.

Each token should correspond to a recurring decision.

---

# 16. COLOR MUST COME FROM THE PROJECT

Do not reach automatically for:

blue;
purple;
cyan;
neon;
gradients;
black backgrounds.

Study the site's subject and imagery.

Derive a constrained palette.

Prefer:

a dominant background atmosphere;
strong readable text;
one primary accent;
possibly one restrained secondary accent;
functional colors for success/warning/error only where needed.

Do not distribute every brand color equally.

Hierarchy is more important than variety.

---

# 17. USE GRADIENTS ONLY WHEN THE IDENTITY ACTUALLY SUPPORTS THEM

Gradients are not prohibited.

Generic gradients are.

Do not use a gradient merely because the hero feels empty.

Do not highlight random headline words with a gradient.

Do not put blue-purple glowing backgrounds behind every technology-related website.

If the real visual identity has a reason for a gradient, use it deliberately.

Otherwise prefer:

solid fields;
photography;
texture;
rules;
whitespace;
typography.

---

# 18. ELIMINATE CARD DEPENDENCY

Cards should represent semantic grouping.

They should not be the default answer to layout.

Before creating or retaining a card, ask:

Would spacing and alignment communicate the same relationship more elegantly?

Would a rule work?

Would a list work?

Would typography work?

Would a table work?

Would a simple grid work?

Would the content actually be clearer without a container?

Use cards only when the boundary itself communicates meaning.

---

# 19. DIFFERENT INFORMATION TYPES SHOULD LOOK DIFFERENT

Do not force:

people
products
features
quotes
statistics
articles
pricing
technical information
events
publications
navigation

into the same component.

Their information structures are different.

Design them accordingly.

A quote may need typographic emphasis.

A specification may need a table.

A publication may need bibliography treatment.

A person may need a portrait and institutional context.

A feature may not need a container at all.

---

# 20. REDUCE BORDER-RADIUS HOMOGENEITY

AI-generated sites frequently use large rounded rectangles for everything.

Avoid universal 16–24px radii.

Establish different edge logic if appropriate.

For example:

buttons may use a low radius;
images may have small or zero radius;
editorial figures may be square;
cards may use modest radius;
tables may use none;
navigation may use none.

Do not create a website where everything looks inflatable.

---

# 21. USE SHADOWS SPARINGLY

Do not separate every surface using elevation.

Excessive shadows make websites resemble component libraries.

Prefer:

whitespace;
rules;
background changes;
typographic hierarchy;
alignment.

Use a shadow when an element actually behaves as an elevated layer.

Examples include:

popover;
menu;
dialog;
floating control.

A static content section usually does not need to float.

---

# 22. BREAK REPETITIVE SECTION FORMULAS

Look for sequences such as:

eyebrow
heading
paragraph
cards

followed by:

eyebrow
heading
paragraph
cards

followed by:

eyebrow
heading
paragraph
cards.

Break the repetition.

Give important sections distinct compositions.

Use recurring grid logic so the site remains coherent.

Consistency does not mean identical composition.

---

# 23. CREATE EDITORIAL RHYTHM

Think in chapters rather than stacked components.

A page can move through:

quiet introduction
dense explanation
large image
small annotation
open whitespace
structured data
narrow text
wide visual
closing statement

The exact sequence depends on the content.

Spacing should communicate relationships.

Internal component spacing should be smaller than major section spacing.

Major chapter transitions should be obvious without requiring giant colored panels.

---

# 24. HUMAN DESIGN USES CONTROLLED EXCEPTIONS

Perfect algorithmic regularity often looks generated.

Allow carefully chosen exceptions.

For example:

one major image may exceed the reading column;
one section may align to an outer grid line;
one quote may sit in the margin;
one title may have a narrower measure;
one important object may intentionally interrupt the rhythm.

Every exception needs a reason.

Do not add randomness.

"Human-designed" does not mean inconsistent.

It means intentionally composed.

---

# 25. DO NOT OVERUSE ASYMMETRY EITHER

Asymmetry has itself become a generated-design cliché.

Do not offset every block.

Do not overlap everything.

Do not rotate elements randomly.

Do not create arbitrary broken grids.

Use asymmetry when it expresses priority or creates a meaningful visual relationship.

Otherwise use strong alignment.

---

# 26. TREAT IMAGES AS CONTENT, NOT DECORATION

Determine the semantic category of each image.

Possible categories include:

documentary photograph;
product photograph;
technical figure;
screenshot;
diagram;
chart;
portrait;
historical image;
illustration;
logo;
artwork.

Do not treat them all identically.

A technical diagram should not be cropped like a lifestyle photograph.

A portrait does not need the same frame as a screenshot.

A screenshot may need contextual scale.

A chart is evidence, not decoration.

---

# 27. AVOID GENERIC IMAGE FRAMING

Do not automatically put every image into:

rounded rectangle
+ border
+ shadow.

Consider:

edge-to-edge imagery;
editorial inset;
full bleed;
square archival frame;
borderless presentation;
hairline rule;
figure-caption relationship;
asymmetric crop;
natural aspect ratio.

The image itself should determine the treatment.

---

# 28. DO NOT FABRICATE VISUAL CONTENT

Never invent:

customer logos;
client logos;
awards;
statistics;
testimonials;
product screenshots;
scientific results;
maps;
charts;
financial numbers;
press quotations;
review scores;
certifications;
partner organizations.

Do not create fake evidence to make the design fuller.

If something is missing, design intelligently around its absence.

---

# 29. HEADER DESIGN

Preserve understandable navigation.

Do not automatically create a floating pill-shaped navbar.

Do not automatically make the header transparent.

Do not automatically add a CTA button in the top-right corner.

Determine what the site actually requires.

Refine:

spacing;
typography;
brand relationship;
active states;
hover;
focus;
responsive behavior.

A calm header is often more credible than an over-designed one.

---

# 30. FOOTER DESIGN

Do not treat the footer as an afterthought.

It should provide intentional closure.

Preserve useful information and destinations.

Organize by actual information hierarchy.

Avoid dumping everything into four identical columns simply because templates do.

A footer can be:

dense;
quiet;
editorial;
institutional;
utilitarian.

Choose what fits the project.

---

# 31. BUTTONS NEED HIERARCHY

Not every link needs a button.

Not every button needs to be a pill.

Create meaningful levels.

PRIMARY ACTION

Use only when an action genuinely deserves high emphasis.

SECONDARY ACTION

Lower visual weight.

EDITORIAL LINK

Suitable for reading/navigation contexts.

INLINE LINK

Within prose.

Avoid:

two large CTA buttons under every heading;
arrow icons after every button;
excessive hover movement;
oversized padding;
universal pills.

---

# 32. ICONS SHOULD COMMUNICATE, NOT DECORATE

Do not place an icon above every card title.

Do not put every icon inside a rounded colored square.

Use icons where they improve recognition.

Do not use icons merely to fill empty space.

Text may be better.

A rule may be better.

Nothing may be better.

---

# 33. BADGES AND PILLS ARE NOT DECORATION

Use badge-like UI for real categories, statuses, tags, filters, or compact metadata.

Do not turn random words into pills merely to create visual interest.

Examples of unnecessary pills include:

"Fast"
"Modern"
"Secure"
"Powerful"
"Trusted"

unless those labels actually represent structured information.

---

# 34. MOTION SHOULD HAVE A JOB

Motion should provide:

feedback;
orientation;
causal relationship;
progress;
spatial continuity.

Do not animate because the page feels too static.

Avoid automatically adding:

scroll reveal to every section;
parallax;
cursor followers;
animated blobs;
continuous gradient animation;
floating objects;
background particle systems;
bounce;
large hover translations.

Prefer subtle CSS transitions.

Respect reduced-motion preferences.

Never hide essential information behind animation.

---

# 35. MICROINTERACTIONS SHOULD BE RESTRAINED

Hover states should confirm interactivity.

They do not need to perform.

Good examples:

underline changes;
small contrast changes;
subtle border changes;
slight image response;
modest directional movement when relevant.

Avoid turning every interaction into a mini-animation.

---

# 36. REWRITE GENERIC AI COPY

This task includes editorial refinement.

Inspect all prominent website copy.

Rewrite language that sounds:

generated;
generic;
inflated;
promotional without evidence;
repetitive;
overly polished;
vague;
mechanically enthusiastic.

However:

NEVER ALTER FACTUAL MEANING.

NEVER INVENT CLAIMS.

NEVER INVENT NUMBERS.

NEVER INVENT RESULTS.

NEVER INVENT TESTIMONIALS.

NEVER INVENT CLIENTS.

NEVER INVENT CAPABILITIES.

NEVER INVENT HISTORY.

NEVER INVENT CERTIFICATIONS.

NEVER INVENT SCIENTIFIC CONCLUSIONS.

NEVER INVENT PERFORMANCE BENEFITS.

If evidence is missing, write modestly.

---

# 37. PRESERVE DOMAIN TERMINOLOGY

Do not dumb down specialized language merely to make it sound conversational.

The intended audience may understand domain terminology.

Preserve:

scientific terminology;
legal terminology;
technical terminology;
industry terminology;
product terminology;
institutional names;
official program names;
established terminology.

Improve surrounding prose without replacing precise terms with vague marketing language.

---

# 38. WRITE LIKE A HUMAN EDITOR, NOT A COPYWRITING MODEL

Human writing usually has:

specific nouns;
concrete verbs;
uneven sentence length;
selective emphasis;
occasional understatement;
meaningful transitions;
domain vocabulary;
context.

AI-style copy often has:

repetitive sentence length;
parallel construction everywhere;
constant enthusiasm;
generic adjectives;
abstract nouns;
overexplaining;
unnecessary summaries;
forced rhetorical questions;
repeated "you" framing;
excessive signposting.

Prefer the former.

---

# 39. REMOVE EMPTY MARKETING LANGUAGE

Delete or rewrite claims such as:

innovative
industry-leading
world-class
best-in-class
next-generation
cutting-edge
revolutionary
seamless
powerful
transformative
game-changing
premium

unless the surrounding content specifically substantiates them.

Replace abstraction with facts.

Instead of:

"Our innovative platform delivers seamless collaboration."

Prefer something concrete such as:

"Teams can review, comment on and approve the same document without exporting it between systems."

Only write that if the product actually does it.

---

# 40. STOP USING GENERIC OPENING SENTENCES

Avoid introductions like:

"In today's rapidly evolving landscape..."

"Now more than ever..."

"At [company], we believe..."

"Welcome to..."

"We are passionate about..."

"Whether you're a..."

"Imagine a world where..."

"The future of X is here."

Start with the actual subject.

---

# 41. AVOID COPYWRITING FORMULAS

Do not repeatedly use:

"It's not just X. It's Y."

"From X to Y."

"X, reimagined."

"Where X meets Y."

"Built for X. Designed for Y."

"Simple. Powerful. Secure."

"Faster. Smarter. Better."

"Less X. More Y."

"Everything you need to X."

These constructions can occasionally work.

They become obvious AI tells when repeated.

---

# 42. CONTROL EM DASHES

Do not remove every em dash.

Do stop using them in every paragraph.

AI writing frequently overuses the construction:

statement — explanatory aside — conclusion.

Prefer punctuation that fits the sentence naturally.

Use:

periods;
commas;
parentheses;
colons;
semicolons;

where appropriate.

Sentence rhythm should vary.

---

# 43. AVOID TRIPLET ADDICTION

AI writing frequently groups everything into threes.

For example:

"fast, secure, and scalable"

"design, build, and grow"

"simple, intuitive, and powerful"

Do not mechanically generate triplets.

Use the number of items the meaning actually requires.

---

# 44. AVOID FAKE CONTRAST

Do not repeatedly write:

"not just X, but Y"

"more than X"

"doesn't just X"

unless a real contrast exists.

These constructions frequently make ordinary statements sound artificially dramatic.

State the important thing directly.

---

# 45. REDUCE RHETORICAL QUESTIONS

Do not fill pages with:

"Ready to transform your workflow?"

"Want to learn more?"

"What if X could be easier?"

"Why settle for less?"

Use questions only when a real question improves communication.

Most website sections should simply tell the reader what matters.

---

# 46. DO NOT TALK TO THE USER CONSTANTLY

Second-person language can be useful.

Do not make every sentence about "you."

For institutional, scientific, cultural, technical, editorial, governmental, or research websites, excessive second-person copy often sounds commercial and artificial.

Choose voice according to the organization.

---

# 47. VARY SENTENCE LENGTH NATURALLY

Do not artificially make every sentence short.

Do not make every paragraph:

Short statement.

Another short statement.

Dramatic fragment.

This pattern is also an AI/copywriting cliché.

Use sentence length appropriate to the subject.

Technical and editorial websites can support longer sentences when clarity remains good.

---

# 48. REMOVE REDUNDANCY

AI-generated web copy often states the same point in:

eyebrow
heading
paragraph
button label
next heading.

Inspect adjacent copy for semantic duplication.

For example:

Eyebrow:
OUR SERVICES

Heading:
Services built for your business

Body:
Explore the services we offer to help your business succeed.

This communicates almost nothing.

Compress it.

Let each layer perform a different job.

---

# 49. HEADLINES SHOULD SAY SOMETHING

Avoid headings such as:

"Designed for success"
"Built for what's next"
"Powering possibilities"
"Innovation that matters"
"Solutions that scale"

unless they genuinely convey project-specific meaning.

Strong headings often include:

a concrete idea;
a real claim;
a useful distinction;
a memorable phrase grounded in the subject.

Do not make every heading clever.

Clarity can itself be distinctive.

---

# 50. EYEBROW LABELS MUST EARN THEIR PLACE

AI-generated websites overuse tiny uppercase labels above every heading.

Examples:

OUR MISSION
OUR FEATURES
WHY US
WHAT WE DO
OUR PROCESS
OUR WORK

Use them only when they improve navigation or hierarchy.

Do not automatically add them to every section.

If the heading already makes the category obvious, remove the eyebrow.

---

# 51. CTA TEXT SHOULD BE SPECIFIC

Avoid generic CTA labels when a specific action exists.

Weak:

Learn More
Get Started
Explore
Discover
See More

Sometimes these are appropriate.

But prefer specific labels when possible:

Read the methodology
View current projects
See pricing
Browse publications
Download the report
Compare plans
Contact the laboratory
View the collection

Do not make labels overly clever.

---

# 52. DO NOT OVERWRITE GOOD COPY

Not every existing sentence needs revision.

If existing copy is:

specific;
accurate;
human;
well-paced;
domain-appropriate;

leave it alone.

This is editing, not compulsory rewriting.

A good editor knows when not to change something.

---

# 53. HIGH-STAKES AND AUTHORITATIVE CONTENT

Exercise additional restraint when handling:

scientific findings;
medical information;
legal statements;
financial information;
government information;
safety instructions;
research conclusions;
official policy;
technical specifications.

Do not improve prose by changing substance.

Do not turn qualified claims into confident claims.

Do not remove uncertainty.

Do not replace exact terminology with promotional language.

Where a statement is authoritative, preserve meaning precisely.

---

# 54. DO NOT CREATE FAKE SOCIAL PROOF

Never add:

"Trusted by 10,000+ teams"
"Used by leading companies"
"Join thousands of..."
"4.9/5"
"98% satisfaction"
"Featured in..."
customer logos
quotes
testimonials

unless the repository contains authoritative evidence.

AI-generated designs often fabricate these because templates expect social proof.

Do not.

Design around the real material.

---

# 55. DO NOT CREATE FAKE METRICS

Do not invent KPI blocks to make a homepage more interesting.

If the project genuinely has meaningful numbers, present them.

If it does not, do not manufacture them.

Information architecture should follow evidence.

---

# 56. SEO SHOULD NOT DESTROY HUMAN WRITING

Preserve important search terms naturally.

Do not repeat the same keyword in every heading.

Do not create paragraphs solely to accommodate keyword density.

Use descriptive page titles and headings.

Keep language readable.

Human editorial quality takes priority over mechanical keyword repetition.

---

# 57. DESIGN AND WRITING MUST SUPPORT EACH OTHER

Do not treat visual design and copy as independent passes.

If a headline becomes shorter, reconsider its line breaks.

If a paragraph becomes denser, reconsider its measure.

If a section no longer needs an eyebrow, reconsider its spacing.

If cards are removed, rewrite text that relied on card headings.

If visual hierarchy becomes stronger, the copy can often become quieter.

Avoid overdesigning weak copy.

Avoid overwriting weak design.

---

# 58. HERO COPY SHOULD NOT SOUND LIKE AN AI STARTUP

Inspect the hero especially carefully.

Avoid the standard formula:

EYEBROW

HUGE GENERIC PROMISE WITH GRADIENT WORD

supporting paragraph explaining obvious benefits

[Get Started] [Learn More]

three KPI cards

Instead determine:

What is the single most important thing this site needs to communicate?

Say that.

Let typography, imagery and composition carry some of the emotional work.

The copy does not need to perform every function.

---

# 59. USE REAL MATERIAL AS VISUAL IDENTITY

If the project contains distinctive:

photography;
drawings;
screenshots;
technical diagrams;
maps;
 scans;
documents;
materials;
textures;
objects;
buildings;
products;
research imagery;
historical imagery;

use those as the source of visual identity.

Do not cover strong real material with generic web decoration.

The website's own content is often more distinctive than anything you could invent.

---

# 60. CHOOSE ONE SIGNATURE VISUAL DEVICE

A strong design usually needs one recognizable idea, not fifteen.

After understanding the subject, choose ONE subtle device.

Possible categories include:

specific rule treatment;
caption system;
numbering system;
directional alignment;
distinctive image crop;
typographic contrast;
margin annotation;
material texture;
technical baseline;
archival frame;
color field;
navigation behavior.

Choose whatever genuinely belongs to the project.

Do not combine multiple motifs just because they are available.

A signature device should create recognition, not spectacle.

---

# 61. DO NOT TURN EVERY SUBJECT INTO A VISUAL METAPHOR

If the company works in networks, do not automatically draw connected nodes.

If it works in AI, do not add neural-network graphics.

If it works in space, do not automatically add stars.

If it works in finance, do not automatically add chart lines.

If it works in biology, do not automatically add floating cells.

If it works in architecture, do not automatically use blueprint grids.

Literal metaphors become clichés quickly.

Use domain cues with restraint.

---

# 62. DO NOT USE "FUTURISTIC" AS A SUBSTITUTE FOR DESIGN

Technology-related websites do not automatically require:

dark backgrounds;
neon cyan;
monospace;
grid overlays;
terminal text;
glowing borders;
HUD elements;
scanlines.

Use those only when genuinely grounded in the project.

---

# 63. RESPONSIVE DESIGN REQUIRES ART DIRECTION

Mobile is not simply desktop stacked vertically.

Review mobile independently.

Ask:

Does the typographic hierarchy still work?

Are headings absurdly large?

Are images appearing in the correct order?

Do figures remain understandable?

Do captions remain attached?

Are data tables usable?

Do cards become excessively tall?

Does the navigation remain clear?

Does whitespace still feel deliberate?

Is the page too long because desktop decoration has stacked vertically?

Adjust intentionally.

---

# 64. TEST SHORT VIEWPORTS

Do not test only 1440×900 desktop screenshots.

Check shorter laptop screens.

A design may look excellent on a tall monitor and terrible on a 768px-high laptop.

Inspect:

hero height;
sticky elements;
navigation;
above-the-fold composition;
modal height;
viewport-dependent sections.

---

# 65. TEST ZOOM

Check approximately:

150% zoom
200% zoom

Ensure:

text remains readable;
content does not overlap;
horizontal page scrolling does not appear unnecessarily;
navigation remains accessible;
figures remain usable;
controls remain visible.

---

# 66. ACCESSIBILITY IS PART OF HUMAN DESIGN

Do not trade accessibility for style.

Maintain or improve:

contrast;
focus states;
keyboard use;
touch targets;
semantic structure;
labeling;
reading order;
reduced motion;
form usability;
alt text;
caption relationships.

Do not hide focus outlines.

Do not make secondary text barely visible.

Do not create tiny uppercase metadata that becomes unreadable.

Do not rely on hover alone.

---

# 67. PERFORMANCE IS A DESIGN CONSTRAINT

Human-quality design does not require heavy runtime effects.

Prefer:

CSS;
existing assets;
optimized images;
efficient local/static fonts;
existing framework capabilities.

Avoid adding:

large animation libraries;
WebGL;
canvas backgrounds;
continuous rendering;
video backgrounds;
large third-party UI systems

unless the project genuinely requires them.

Complexity is not polish.

---

# 68. IMPLEMENT FOUNDATIONS BEFORE DECORATING COMPONENTS

After the audit and design thesis, work in this order:

PHASE 1 — TYPOGRAPHY

Select and test fonts.

PHASE 2 — TOKENS

Establish color, spacing, measures, radii and rules.

PHASE 3 — PAGE GEOMETRY

Refine containers, reading widths, grids and section rhythm.

PHASE 4 — GLOBAL UI

Header, navigation, links, buttons, forms, footer.

PHASE 5 — CONTENT TYPES

Images, figures, cards, lists, tables, quotes, metadata, people, products, publications or other project-specific structures.

PHASE 6 — COPY

Edit generic text while preserving facts and domain meaning.

PHASE 7 — SPECIAL PAGES

Refine pages with unique content requirements.

PHASE 8 — RESPONSIVE

Review compositions at multiple sizes.

PHASE 9 — SUBTRACTION

Remove anything that does not earn its visual weight.

---

# 69. ITERATE FROM SCREENSHOTS

After the first substantial implementation pass, render the site again.

Capture matching AFTER screenshots.

Compare BEFORE and AFTER directly.

Do not rely on memory.

Inspect:

hierarchy;
typography;
density;
spacing;
images;
section rhythm;
repetition;
navigation;
footer;
mobile.

Source-code cleanliness does not prove visual quality.

The browser is the final rendering environment.

---

# 70. PERFORM THREE DESIGN PASSES

Do not accept the first coherent redesign.

PASS 1 — SYSTEM

Check:

typography;
palette;
spacing;
tokens;
base components;
consistency.

PASS 2 — ART DIRECTION

Check:

image authority;
rhythm;
hierarchy;
asymmetry;
section variation;
content-specific treatment;
brand specificity.

PASS 3 — SUBTRACTION

Remove:

unnecessary cards;
unnecessary backgrounds;
unnecessary borders;
unnecessary badges;
unnecessary labels;
unnecessary icons;
unnecessary animation;
unnecessary decorative shapes;
unnecessary text.

The third pass should usually make the page quieter.

---

# 71. PERFORM A COPY PASS SEPARATELY

After design stabilization, read the visible website from beginning to end.

Do not inspect sentences in isolation.

Look for repeated phrases across sections.

Check:

Does every section need its heading?

Are multiple sections saying the same thing?

Are generic adjectives carrying too much weight?

Does every CTA say "Learn More"?

Are there too many sentences beginning with "We"?

Are there too many sentences beginning with "Our"?

Does the writing sound uniformly enthusiastic?

Are there three-part slogans everywhere?

Is punctuation repetitive?

Does any paragraph sound like it was written to fill space?

Rewrite accordingly.

---

# 72. DO NOT MAKE ALL WRITING "CASUAL"

Human writing does not necessarily mean conversational writing.

Choose voice according to context.

A research institute may need:

precise;
measured;
institutional;
academic;
direct

language.

A restaurant may need:

warm;
sensory;
local;
informal

language.

A developer tool may need:

technical;
concise;
specific

language.

A cultural organization may need:

editorial;
descriptive;
historically aware

language.

Do not impose startup friendliness on every project.

---

# 73. RETAIN AUTHORIAL QUIRKS WHEN THEY WORK

If the existing project has distinctive language, do not normalize it unnecessarily.

Preserve:

unusual but effective phrases;
technical terminology;
regional vocabulary;
founder voice;
institutional vocabulary;
project-specific terminology.

AI often makes writing generic by smoothing every irregularity.

Do not over-smooth.

---

# 74. USE RESTRAINT WITH TITLE CASE AND UPPERCASE

Do not put every label in uppercase.

Do not convert every heading to Title Case automatically.

Use casing appropriate to the voice.

Overused uppercase micro-labels are a common template tell.

---

# 75. DO NOT ADD CONTENT TO FILL VISUAL SPACE

If a section looks empty, fix the composition.

Do not invent:

extra bullets;
fake benefits;
fake quotes;
unnecessary explanatory paragraphs;
unverified numbers;
additional feature cards.

Whitespace is allowed.

The absence of content is not necessarily a problem.

---

# 76. REMOVE TEMPLATE SECTIONS THAT CONTAIN NO REAL INFORMATION

If the existing site includes a section that is clearly generic filler and carries no meaningful unique information, consider whether its content can be merged or removed.

However:

do not remove structurally important sections without understanding the project.

If preserving existing structure is a hard requirement, improve or condense the section instead.

---

# 77. NO AUTOMATIC "PREMIUM" TREATMENT

Do not make every website:

black;
cream;
gold;
large serif;
slow animated;
minimal

because that currently signals "premium."

A design can be restrained without imitating luxury branding.

Choose a visual vocabulary appropriate to the subject.

---

# 78. NO AUTOMATIC BRUTALISM

Do not respond to "avoid generic AI" by making the site deliberately ugly, raw or aggressively brutalist.

Brutalism is one possible design language.

It is not the universal opposite of AI design.

---

# 79. NO AUTOMATIC EDITORIAL SERIF

Likewise, do not automatically add a large serif headline because editorial design is less common in generated sites.

Typography still needs to suit the project.

Human design comes from judgment, not from swapping clichés.

---

# 80. NO AUTOMATIC ANTI-DESIGN

Avoiding AI aesthetics does not mean:

misaligned text;
random fonts;
inconsistent colors;
arbitrary overlapping;
strange cursor behavior;
illegible layouts.

Intentionality remains the goal.

---

# 81. THE AI STARTUP SWAP TEST

Perform this test after each major pass.

Imagine replacing:

logo;
text;
images

with those of a generic AI SaaS company.

Would the visual design still work almost perfectly?

If YES, the design is probably too generic.

Continue refining.

The website's visual system should emerge sufficiently from its actual identity that transplanting it unchanged would feel wrong.

---

# 82. THE COMPETITOR SWAP TEST

Imagine replacing the content with its closest competitor.

Would the site still feel equally appropriate?

If YES, ask whether more identity can come from:

real content;
imagery;
history;
material;
typography;
specific information structures;
language.

Do not force arbitrary differentiation, but look for genuine sources of specificity.

---

# 83. THE NO-LOGO TEST

Hide the logo mentally.

Does the website still communicate something about what kind of organization this is?

If not, the identity may rely too heavily on branding assets.

Improve:

typography;
content treatment;
imagery;
layout;
detail.

---

# 84. THE HUMAN EDITOR TEST

Ask:

Would a designer be able to explain why this image is this width?

Why is this heading aligned here?

Why does this section have more space?

Why is this text narrow?

Why does this component have a border?

Why is this link a button?

Why does this object have a radius?

Why does this animation exist?

Why is this sentence here?

If the answer is repeatedly:

"because the component template uses it"

or:

"because that's what modern websites look like"

reconsider the decision.

---

# 85. THE SUBTRACTION TEST

For every decorative element ask:

What information, hierarchy or atmosphere does this contribute?

If removing it changes almost nothing, remove it.

Human polish often comes from removing the correct 20% of a generated design.

---

# 86. THE COPY SWAP TEST

Replace the important nouns in a sentence.

For example:

"Our powerful platform empowers teams to streamline workflows and achieve more."

Change "platform" to:

bank
gym
CRM
hospital
AI tool
university

If the sentence still works everywhere, it is generic.

Rewrite it using actual project information.

---

# 87. THE CLAIM TEST

For every strong claim ask:

Where is the evidence for this?

If the repository or provided content does not support the claim, remove or soften it.

Do not convert assumptions into marketing claims.

---

# 88. THE COMPONENT DIVERSITY TEST

Inspect the page from a distance.

How many repeated rounded rectangles are visible?

How many sections share identical geometry?

How many icons appear above headings?

How many labels are pills?

How many CTA buttons appear?

How many sections are centered?

If the same answer appears repeatedly, reduce repetition.

---

# 89. THE FONT TEST

Ask:

Would this font combination still be the first obvious choice if this project had not been generated by a web-design model?

If the answer is simply:

"Inter because it is clean"

search further.

Typography does not need to be obscure.

It needs to be intentional.

---

# 90. THE SCREENSHOT TEST

Ask:

If this screenshot appeared anonymously on a design gallery, could someone plausibly infer the kind of organization behind it?

Not necessarily the exact brand.

But does it communicate:

institution;
publication;
laboratory;
studio;
manufacturer;
restaurant;
software company;
museum;
nonprofit;
research project;
government service;
retailer;

through more than its words?

If not, improve specificity.

---

# 91. COMMON FAILURE PATTERNS THAT SHOULD TRIGGER REWORK

Reconsider the redesign if several of these remain:

Inter everywhere
system sans everywhere
giant generic hero
gradient headline text
purple/cyan glow
glassmorphism
floating orbs
random blobs
every section in a card
20px radius everywhere
pill navigation
pill buttons everywhere
icon boxes
constant badges
uniform three-column grids
repeated feature cards
centered everything
startup KPI blocks
fake testimonials
fake logos
fake statistics
abstract AI art
generic illustrations
dark mode solely because the subject is technical
monospace solely because the subject is technical
scroll reveal on everything
excessive animation
same spacing everywhere
same component geometry everywhere
same image frame everywhere
generic marketing copy
"Unlock"
"Elevate"
"Seamless"
"Empower"
"Revolutionize"
"Next-generation"
"Whether you're..."
"In today's..."
constant rhetorical questions
constant em dashes
constant triplets
constant "not just X, but Y"
constant "Built for X"
every CTA saying "Learn More"

One of these may be appropriate.

A cluster usually signals a generated aesthetic.

---

# 92. VALIDATE FUNCTIONALITY AFTER VISUAL CHANGES

Run the project's existing:

lint;
type checks;
tests;
build;
content validation;
route tests;
visual tests;
accessibility tests

where available.

Do not modify tests merely to accommodate a visual redesign unless the expected presentation intentionally changed.

Do not weaken safety checks.

Do not disable accessibility rules.

Fix the implementation.

---

# 93. CHECK ALL REPRESENTATIVE PAGES AGAIN

After implementation, inspect representative pages at:

wide desktop;
normal desktop;
short laptop;
tablet;
mobile;
landscape mobile;
150% zoom;
200% zoom;
reduced motion.

Check:

overflow;
clipping;
widows/orphans where noticeable;
strange line breaks;
navigation;
figures;
tables;
images;
forms;
long headings;
long buttons;
localized text if available;
content-heavy states.

---

# 94. COMPARE BEFORE AND AFTER

Prepare matched screenshots.

The redesign should clearly improve:

typography;
hierarchy;
rhythm;
content specificity;
image treatment;
readability;
visual confidence;
editorial tone.

But it should not look like a completely unrelated website unless a full rebrand was explicitly requested.

---

# 95. PRESERVE STRONG EXISTING DECISIONS

Do not change something merely because you have permission to redesign.

During the audit, identify what is already good.

Preserve strong:

copy;
layouts;
images;
interactions;
information hierarchy;
navigation;
components;
color decisions.

The goal is not maximum change.

The goal is maximum improvement per meaningful change.

---

# 96. WORK LIKE AN EDITOR

Prefer:

adjusting
refining
removing
rebalancing
reframing
tightening
clarifying

before:

rebuilding
replacing
inventing
adding.

Human polish often comes from a sequence of small corrections.

---

# 97. WORK LIKE AN ART DIRECTOR

At the same time, do not be afraid to make decisive visual changes when the current identity is generic.

Typography may need to change substantially.

Spacing may need to change substantially.

Card structures may need to disappear.

The hero composition may need to be rebalanced.

Color may need to be simplified.

Image treatment may need to become much stronger.

Distinguish architectural caution from aesthetic timidity.

Preserve functionality.

Be decisive about appearance.

---

# 98. WORK LIKE A COPY EDITOR

Do not rewrite everything.

Remove:

generic filler;
duplicated meaning;
inflated claims;
AI clichés;
unnecessary adjectives;
mechanical enthusiasm.

Strengthen:

specificity;
clarity;
voice;
rhythm;
terminology;
factual precision.

Never make the copy less accurate in order to make it more exciting.

---

# 99. FINAL IMPLEMENTATION REPORT

When finished, provide a concise report with these sections.

## ORIGINAL VISUAL PROBLEMS

Name specific recurring patterns.

Do not simply say "the site looked generic."

## ORIGINAL EDITORIAL PROBLEMS

Identify generic, redundant or machine-like writing patterns.

## DESIGN THESIS

Describe the chosen visual direction in concrete terms.

Avoid empty phrases such as:

modern
clean
sleek
professional

## TYPOGRAPHY

Explain what changed and why.

## COLOR AND MATERIAL

Explain the palette and how it derives from the project.

## LAYOUT AND RHYTHM

Explain changes to spacing, section structure and page geometry.

## COMPONENTS

Explain what card, button, badge, table, list, image or navigation patterns changed.

## IMAGERY

Explain image art direction.

## COPY

Explain what kinds of language were rewritten.

Confirm that unsupported claims were not added.

## PRESERVED FUNCTIONALITY

Confirm what architectural and behavioral systems were deliberately left untouched.

## VALIDATION

List tests and build commands executed.

## VISUAL QA

List pages and viewport sizes inspected.

## REMAINING LIMITATIONS

State anything that could not be verified.

---

# 100. FINAL ACCEPTANCE CRITERIA

The project is complete only when the following are true.

The site remains functionally correct.

The site's architecture remains appropriate.

The website's identity is clearer than before.

The typography feels intentionally selected.

The design does not rely on generic startup conventions.

Cards are used selectively.

Border radii are controlled.

Color has hierarchy.

Images are treated according to their content.

Different information types have distinct visual treatment.

The layout has rhythm rather than repetition.

Responsive layouts feel intentionally composed.

Motion is restrained.

Accessibility remains intact or improves.

Prominent copy sounds human and project-specific.

Generic AI marketing phrases have been removed.

Unsupported claims have not been introduced.

Existing good writing has not been rewritten unnecessarily.

The site cannot be convincingly converted into an unrelated AI SaaS landing page merely by swapping its logo and text.

The finished site looks as though a thoughtful designer and editor spent time understanding the actual project before making decisions.

---

# 101. MOST IMPORTANT DIRECTIVE

Do not "de-AI" the website by adding eccentricity.

Do not replace generic AI design with trendy anti-AI design.

Do not make it brutalist simply to seem human.

Do not make it editorial simply to seem sophisticated.

Do not add serif typography merely to look bespoke.

Do not add asymmetry merely to look designed.

Do not add texture merely to look tactile.

Do not remove useful conventions merely to look original.

Instead:

UNDERSTAND THE SUBJECT.

UNDERSTAND THE USERS.

UNDERSTAND THE CONTENT.

UNDERSTAND THE EXISTING SYSTEM.

IDENTIFY WHICH DECISIONS ARE GENERIC.

KEEP THE DECISIONS THAT ARE GOOD.

REMOVE THE ONES THAT ARE AUTOMATIC.

MAKE THE REMAINING DECISIONS SPECIFIC.

A website feels human-designed when its choices appear to come from understanding the thing being represented rather than from knowing what websites are currently supposed to look like.

That is the goal.

---

# 102. EXECUTION INSTRUCTION

Begin now.

Do not start by editing.

First:

inspect the repository;
read its documentation;
understand the architecture;
run the site;
inspect representative pages;
capture screenshots;
audit visual AI tells;
audit editorial AI tells;
identify existing strengths;
derive a project-specific design thesis.

Then implement.

When choosing between:

adding something

and

making an existing element more intentional,

prefer the latter.

When choosing between:

a fashionable design convention

and

a project-specific solution,

prefer the project-specific solution.

When choosing between:

more decoration

and

better typography, spacing, imagery or writing,

prefer typography, spacing, imagery and writing.

When choosing between:

rewriting accurate specialized content

and

preserving its precision,

preserve precision.

When choosing between:

inventing content to complete a layout

and

redesigning the layout around the real content,

redesign around the real content.

Do not declare completion until you have rendered and critically reviewed the finished website in the browser.

The browser output, not the source code, is the final artifact.