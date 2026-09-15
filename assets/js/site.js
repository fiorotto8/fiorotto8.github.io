/* Native scrolling, section tracking and legacy links; no dependencies. */
(() => {
  'use strict';
  const redirect = document.querySelector('[data-redirect]');
  if (redirect) {
    const destination = new URL(redirect.dataset.redirect, window.location.href);
    if (window.location.hash) destination.hash = window.location.hash;
    destination.search = window.location.search;
    window.location.replace(destination.href);
    return;
  }

  const sections = [...document.querySelectorAll('[data-scroll-section]')];
  if (!sections.length) return;
  const links = [...document.querySelectorAll('[data-nav]')];
  const progress = document.querySelector('.reading-progress span');
  const header = document.querySelector('.site-header');
  const aliases = {
    'current-research': 'research',
    'current-research-section': 'research',
    'earlier-programmes': 'previous-projects-section',
    'selected-work': 'publications',
    'teaching-teaser': 'teaching',
    'collaborate': 'contact'
  };
  let queued = false;
  let anchorSection = null;

  function update() {
    queued = false;
    const line = header.offsetHeight + Math.min(180, window.innerHeight * 0.2);
    let active = sections[0];
    for (const section of sections) {
      if (section.getBoundingClientRect().top <= line) active = section;
    }
    const maxScroll = document.documentElement.scrollHeight - window.innerHeight;
    if (maxScroll > 0 && window.scrollY >= maxScroll - 3) {
      active = sections[sections.length - 1];
      // A short final section cannot always reach the top of a tall viewport.
      // Keep the selected, visible destination until the reader scrolls again.
      if (anchorSection) {
        const bounds = anchorSection.getBoundingClientRect();
        if (bounds.bottom > header.offsetHeight && bounds.top < window.innerHeight) active = anchorSection;
      }
    }
    document.body.dataset.section = active.id;
    for (const link of links) {
      if (link.dataset.nav === active.id) link.setAttribute('aria-current', 'location');
      else link.removeAttribute('aria-current');
    }
    progress.style.transform = `scaleX(${maxScroll > 0 ? Math.min(1, Math.max(0, window.scrollY / maxScroll)) : 0})`;
  }
  function queueUpdate() {
    if (!queued) { queued = true; requestAnimationFrame(update); }
  }
  function revealHash() {
    let id;
    try { id = decodeURIComponent(window.location.hash.slice(1)); }
    catch (_) { return; }
    if (!id) return;
    const alias = aliases[id];
    if (alias) {
      id = alias;
      history.replaceState(null, '', window.location.pathname + window.location.search + '#' + id);
    }
    const target = document.getElementById(id);
    if (!target) return;
    anchorSection = target.closest('[data-scroll-section]');
    let opened = false;
    for (let parent = target; parent; parent = parent.parentElement) {
      if (parent.tagName === 'DETAILS' && !parent.open) { parent.open = true; opened = true; }
    }
    // Native fragments handle ordinary links; explicitly align revealed content.
    if (opened || alias) requestAnimationFrame(() => target.scrollIntoView({ behavior: 'instant', block: 'start' }));
    queueUpdate();
  }
  function measureHeader() {
    document.documentElement.style.setProperty('--header-height', `${header.offsetHeight}px`);
    queueUpdate();
  }
  window.addEventListener('scroll', queueUpdate, { passive: true });
  function resumeScrollTracking() {
    anchorSection = null;
    queueUpdate();
  }
  window.addEventListener('wheel', resumeScrollTracking, { passive: true });
  window.addEventListener('touchmove', resumeScrollTracking, { passive: true });
  window.addEventListener('pointerdown', resumeScrollTracking, { passive: true });
  window.addEventListener('keydown', (event) => {
    if (['ArrowDown', 'ArrowUp', 'PageDown', 'PageUp', 'Home', 'End', ' '].includes(event.key)) resumeScrollTracking();
  });
  links.forEach(link => link.addEventListener('click', () => {
    anchorSection = document.getElementById(link.dataset.nav);
    queueUpdate();
  }));
  window.addEventListener('resize', measureHeader);
  window.addEventListener('hashchange', revealHash);
  window.addEventListener('pageshow', () => { revealHash(); queueUpdate(); });
  document.addEventListener('toggle', queueUpdate, true);
  if ('ResizeObserver' in window) {
    new ResizeObserver(measureHeader).observe(header);
    new ResizeObserver(queueUpdate).observe(document.querySelector('main'));
  }
  // Include expanded content when printing, then restore the reader's state.
  let printDetails = [];
  window.addEventListener('beforeprint', () => {
    printDetails = [...document.querySelectorAll('details:not([open])')];
    printDetails.forEach(detail => { detail.open = true; });
  });
  window.addEventListener('afterprint', () => {
    printDetails.forEach(detail => { detail.open = false; });
    printDetails = [];
  });
  measureHeader();
  revealHash();
})();
