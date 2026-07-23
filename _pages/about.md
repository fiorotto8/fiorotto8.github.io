---
layout: portfolio-page
permalink: /
title: "Davide Fiorina"
excerpt: "Experimental particle and astroparticle physicist developing gaseous detectors and optical TPCs for rare-event searches, X-ray polarimetry, and precision timing."
author_profile: false
---

{% include base_path %}

<!-- Hero -->
<section class="home-hero">
  <div class="home-hero__text">
    <p class="hero-kicker">Experimental particle &amp; astroparticle physics</p>
    <h1 class="home-hero__title">Davide Fiorina</h1>
    <p class="home-hero__lead">I design, build, and operate gaseous detectors for rare-event searches, X-ray polarimetry, and precision timing.</p>
    <p class="home-hero__role">Postdoctoral researcher at GSSI and Technical Coordinator for the CYGNO experiment, currently leading CYGNO04 integration and commissioning at LNGS.</p>
    <p class="home-hero__human">I am happiest moving between detector design, hands-on work, and the first data from a new system.</p>
    <div class="hero-actions button-row">
      <a href="{{ base_path }}/research/" class="site-button site-button--primary">Explore research</a>
      <a href="{{ base_path }}/files/CV.pdf" class="site-button site-button--secondary" download>Download CV</a>
      <a href="mailto:{{ site.author.email }}" class="site-button site-button--secondary">Contact</a>
    </div>
  </div>
  <div class="home-hero__image-wrapper">
    <img src="{{ base_path }}/images/profile/PXL_20230623_153017470-840.webp"
         srcset="{{ base_path }}/images/profile/PXL_20230623_153017470-480.webp 480w,
                 {{ base_path }}/images/profile/PXL_20230623_153017470-600.webp 600w,
                 {{ base_path }}/images/profile/PXL_20230623_153017470-840.webp 840w,
                 {{ base_path }}/images/profile/PXL_20230623_153017470.webp 1129w"
         sizes="(max-width: 699px) 280px, 420px"
         alt="Davide Fiorina in a clean room working on detector assembly"
         class="home-hero__image"
         width="840"
         height="1116"
         decoding="async">
  </div>
</section>

<!-- Current status strip -->
<section class="status-strip" aria-label="Current work and location">
  <div class="status-strip__item">
    <span class="status-strip__label">Now</span>
    CYGNO04 integration and commissioning
  </div>
  <div class="status-strip__item">
    <span class="status-strip__label">Also</span>
    Optical TPCs for hard X-ray polarimetry
  </div>
  <div class="status-strip__item">
    <span class="status-strip__label">Based at</span>
    GSSI and Laboratori Nazionali del Gran Sasso
  </div>
</section>

<!-- Institutions and collaborations -->
<section class="affiliation-strip" aria-labelledby="affiliations-heading">
  <div class="affiliation-strip__intro">
    <h2 id="affiliations-heading">Institutions &amp; collaborations</h2>
    <p>Current and previous research across GSSI, INFN, CYGNO, CERN, and the University of Pavia.</p>
  </div>
  <ul class="affiliation-strip__logos">
    <li>
      <img src="{{ base_path }}/images/gssi-logo.webp"
           alt="Gran Sasso Science Institute"
           width="215"
           height="220"
           loading="lazy"
           decoding="async">
    </li>
    <li>
      <img src="{{ base_path }}/images/infn-logo.webp"
           alt="Istituto Nazionale di Fisica Nucleare"
           width="397"
           height="220"
           loading="lazy"
           decoding="async">
    </li>
    <li>
      <img src="{{ base_path }}/images/cygno-logo-180.webp"
           srcset="{{ base_path }}/images/cygno-logo-180.webp 180w,
                   {{ base_path }}/images/cygno-logo.webp 360w"
           sizes="(max-width: 699px) 140px, 120px"
           alt="CYGNO experiment"
           width="180"
           height="180"
           loading="lazy"
           decoding="async">
    </li>
    <li>
      <img src="{{ base_path }}/images/CERN-logo.svg"
           alt="CERN"
           width="600"
           height="600"
           loading="lazy"
           decoding="async">
    </li>
    <li>
      <img src="{{ base_path }}/images/unipv-logo-320.webp"
           srcset="{{ base_path }}/images/unipv-logo-320.webp 320w,
                   {{ base_path }}/images/unipv-logo.webp 560w"
           sizes="(max-width: 699px) 308px, 140px"
           alt="University of Pavia"
           width="320"
           height="125"
           loading="lazy"
           decoding="async">
    </li>
  </ul>
</section>

<!-- Current research -->
<section id="current-research">
  <h2 class="section-heading">Current research</h2>
  <p class="section-intro">From detector concept and simulation through construction, commissioning, and data analysis.</p>

  <div class="project-grid">
    <!-- CYGNO04 -->
    <article class="project-card">
      <div class="project-card__image-wrapper">
        <img src="{{ base_path }}/images/research/cygno/cygno04-cleanroom-720.webp"
             srcset="{{ base_path }}/images/research/cygno/cygno04-cleanroom-720.webp 720w,
                     {{ base_path }}/images/research/cygno/cygno04-cleanroom.webp 1600w"
             sizes="(max-width: 699px) calc(100vw - 36px), (max-width: 1099px) calc(50vw - 42px), 370px"
             alt="CYGNO04 detector integration in the clean room at LNGS"
             class="project-card__image"
             width="720"
             height="715"
             loading="lazy"
             decoding="async">
      </div>
      <div class="project-card__body">
        <h3 class="project-card__title">CYGNO04</h3>
        <p class="project-card__text">A 400 L optical TPC for directional dark-matter searches at LNGS.</p>
        <p class="project-card__role">Technical coordination, detector integration, and commissioning.</p>
        <ul class="project-tags">
          <li class="project-tag">Optical TPC</li>
          <li class="project-tag">Directional dark matter</li>
        </ul>
        <a href="{{ base_path }}/research/#cygno04" class="site-button site-button--secondary">CYGNO04 details</a>
      </div>
    </article>

    <!-- X-ray polarimetry -->
    <article class="project-card">
      <div class="project-card__image-wrapper">
        <img src="{{ base_path }}/images/research/xray-polarimetry/polarimetry-test-720.webp"
             srcset="{{ base_path }}/images/research/xray-polarimetry/polarimetry-test-720.webp 720w,
                     {{ base_path }}/images/research/xray-polarimetry/polarimetry-test.webp 984w"
             sizes="(max-width: 699px) calc(100vw - 36px), (max-width: 1099px) calc(50vw - 42px), 370px"
             alt="Laboratory test of the optical TPC for X-ray polarimetry"
             class="project-card__image project-card__image--contain"
             width="720"
             height="539"
             loading="lazy"
             decoding="async">
      </div>
      <div class="project-card__body">
        <h3 class="project-card__title">Optical TPCs for X-ray polarimetry</h3>
        <p class="project-card__text">Triple-GEM optical TPCs for reconstructing photoelectron tracks and measuring polarisation in the 10&ndash;60 keV range.</p>
        <p class="project-card__role">Detector development, calibration, simulation, and track reconstruction.</p>
        <ul class="project-tags">
          <li class="project-tag">Triple-GEM</li>
          <li class="project-tag">Polarimetry</li>
        </ul>
        <a href="{{ base_path }}/research/#xray-polarimetry" class="site-button site-button--secondary">Polarimetry details</a>
      </div>
    </article>

    <!-- Neutrinos, CEvNS, space -->
    <article class="project-card">
      <div class="project-card__image-wrapper">
        <img src="{{ base_path }}/images/research/R&amp;D/EXPO-720.webp"
             srcset="{{ base_path }}/images/research/R&amp;D/EXPO-720.webp 720w,
                     {{ base_path }}/images/research/R&amp;D/EXPO.webp 1169w"
             sizes="(max-width: 699px) calc(100vw - 36px), (max-width: 1099px) calc(100vw - 48px), 370px"
             alt="Spacecraft architecture used for the EXPO polarimetry mission study; legacy XIPE component labels are visible"
             class="project-card__image project-card__image--contain"
             width="720"
             height="522"
             loading="lazy"
             decoding="async">
      </div>
      <div class="project-card__body">
        <h3 class="project-card__title">Neutrinos, CEvNS, and space instrumentation</h3>
        <p class="project-card__text">Directional solar-neutrino studies, coherent neutrino scattering concepts, and space-instrument simulation.</p>
        <p class="project-card__role">Detector modelling and response simulations for low-energy signals.</p>
        <p class="project-card__note">The EXPO architecture diagram retains legacy XIPE component labels.</p>
        <ul class="project-tags">
          <li class="project-tag">Neutrinos</li>
          <li class="project-tag">CEvNS</li>
        </ul>
        <a href="{{ base_path }}/research/#new-rd" class="site-button site-button--secondary">New R&amp;D details</a>
      </div>
    </article>
  </div>
</section>

<!-- Earlier detector programmes -->
<section id="earlier-programmes">
  <h2 class="section-heading">Earlier detector programmes</h2>

  <div class="earlier-programme">
    <h3 class="earlier-programme__title">PICOSEC Micromegas</h3>
    <p class="earlier-programme__text">Coordinated PICOSEC Micromegas R&amp;D for future muon-collider detector concepts. <a href="{{ base_path }}/research/#picosec">PICOSEC project details</a></p>
  </div>

  <div class="earlier-programme">
    <h3 class="earlier-programme__title">CMS GEM detectors</h3>
    <p class="earlier-programme__text">Worked on CMS triple-GEM detectors from R&amp;D and quality control to Run 3 operations. <a href="{{ base_path }}/research/#cms-gem">CMS GEM project details</a></p>
  </div>
</section>

<!-- Selected work -->
<section id="selected-work">
  <h2 class="section-heading">Selected work</h2>
  <p class="section-intro">Recent papers and presentations selected from a broader record. The complete publication list is available on <a href="{{ site.author.scopus }}" target="_blank" rel="noopener noreferrer">Scopus</a>.</p>

  <ul class="compact-list">
    <li class="compact-list__item">
      <a href="https://arxiv.org/abs/2510.26239" target="_blank" rel="noopener noreferrer">A Large-Area Optical Time Projection Chamber for Hard X-ray Polarimetry with Directional Imaging of Low-Energy Electron Recoils</a> <span class="status-label">(2025, arXiv)</span>
    </li>
    <li class="compact-list__item">
      <a href="https://doi.org/10.1140/epjc/s10052-026-15318-7" target="_blank" rel="noopener noreferrer">Modeling the light response of an optically readout GEM based TPC for the CYGNO experiment</a> <span class="status-label">(2026, EPJC)</span>
    </li>
    <li class="compact-list__item">
      <a href="https://doi.org/10.1088/1748-0221/20/05/P05035" target="_blank" rel="noopener noreferrer">Study on discharge and short-circuit generation in CMS GE1/1 triple-GEM detectors during Run 3</a> <span class="status-label">(2025, JINST)</span>
    </li>
    <li class="compact-list__item">
      <a href="https://agenda.infn.it/event/51443/timetable/?print=1" target="_blank" rel="noopener noreferrer">When Spin adds to N<sup>2</sup>: a proposal to probe the axial side of CEvNS with Fluorine</a> — WHAT ELSE, LNGS (2026)
    </li>
    <li class="compact-list__item">
      X-POT: X-ray Polarimetry with Optical Time Projection Chamber — ASAPP 2025 (2025)
    </li>
  </ul>

  <div class="button-row" style="margin-top: var(--space-3);">
    <a href="{{ base_path }}/publications/" class="site-button site-button--secondary">Selected publications</a>
    <a href="{{ base_path }}/talks/" class="site-button site-button--secondary">All talks</a>
  </div>
</section>

<!-- Teaching, supervision, and outreach -->
<section id="teaching-teaser">
  <h2 class="section-heading">Teaching, supervision, and outreach</h2>
  <p>I supervise students, teach detector laboratories, help organise international schools, and give public seminars.</p>
  <a href="{{ base_path }}/teaching/" class="site-button site-button--secondary">Teaching &amp; outreach</a>
</section>

<!-- Contact -->
<section id="contact" class="contact-block">
  <h2 class="section-heading">Get in touch</h2>
  <p>For collaborations, seminars, or student projects, email is the most direct route.</p>
  <div class="button-row button-row--centred">
    <a href="mailto:{{ site.author.email }}" class="site-button site-button--primary">Email me</a>
  </div>
  <nav class="profile-links" aria-label="Research profiles">
    <a href="https://github.com/{{ site.author.github }}" target="_blank" rel="noopener noreferrer">GitHub</a>
    <a href="{{ site.author.orcid }}" target="_blank" rel="noopener noreferrer">ORCID</a>
    <a href="{{ site.author.scopus }}" target="_blank" rel="noopener noreferrer">Scopus</a>
  </nav>
</section>
