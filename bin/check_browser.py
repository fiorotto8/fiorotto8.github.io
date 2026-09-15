#!/usr/bin/env python3
"""Exercise the real scroll navigation and generate local review screenshots."""
from playwright.sync_api import sync_playwright
from pathlib import Path
import json
import argparse
parser = argparse.ArgumentParser(description='Browser checks; requires the optional playwright package and Chromium.')
parser.add_argument('--url', default='http://127.0.0.1:4000/')
parser.add_argument('--output', default='.site-review')
args = parser.parse_args()
base = args.url.rstrip('/') + '/'
out=Path(args.output); out.mkdir(parents=True, exist_ok=True)
checks=[]

def decode_images(page):
 """Also exercise lazy photographs inside the native research disclosure."""
 page.evaluate("window.qaClosedDetails = [...document.querySelectorAll('details:not([open])')]; window.qaClosedDetails.forEach(el => el.open = true)")
 for img in page.locator('img').all():
  img.scroll_into_view_if_needed()
  img.evaluate('(el)=>el.decode()')
 page.evaluate('window.qaClosedDetails.forEach(el => el.open = false); delete window.qaClosedDetails')

with sync_playwright() as p:
 browser=p.chromium.launch()
 for width,height in [(1920,1080),(1440,900),(1366,768),(1024,900),(768,1024),(390,844),(320,844),(844,390)]:
  page=browser.new_page(viewport={'width':width,'height':height},reduced_motion='reduce')
  errors=[]; failed=[]
  page.on('pageerror',lambda error: errors.append(str(error)))
  page.on('response',lambda response: failed.append(response.url) if response.status>=400 else None)
  page.goto(base,wait_until='networkidle')
  before=page.locator('.site-header').evaluate('(el)=>el.offsetHeight')
  page.wait_for_timeout(200)
  assert before==page.locator('.site-header').evaluate('(el)=>el.offsetHeight'), 'Header must not grow'
  assert page.evaluate('document.documentElement.scrollWidth === innerWidth'), f'Overflow at {width}'
  # Load and inspect every photograph before taking the full-page screenshot.
  decode_images(page)
  for section in ['research','publications','talks','teaching','about','contact']:
   page.locator(f'[data-nav="{section}"]').click()
   page.wait_for_function('(id)=>document.body.dataset.section===id',arg=section)
   assert page.locator(f'[data-nav="{section}"]').get_attribute('aria-current')=='location'
   top=page.locator('#'+section).evaluate('(el)=>el.getBoundingClientRect().top')
   assert top >= page.locator('.site-header').evaluate('(el)=>el.offsetHeight')-2, (width,section,'covered by header',top)
  if width == 1920:
   page.locator('[data-nav="about"]').click()
   page.wait_for_function('document.body.dataset.section==="about"')
   page.keyboard.press('End')
   page.wait_for_function('document.body.dataset.section==="contact"')
   page.locator('[data-nav="about"]').click()
   page.wait_for_function('document.body.dataset.section==="about"')
   page.locator('[data-nav="about"]').click()
   page.wait_for_function('document.body.dataset.section==="about"')
   checks.append('Tall viewport: About, manual scroll to Contact and repeated About navigation passed')
  for id in ['more-publications','more-talks','posters','previous-projects-section']:
   summary=page.locator('#'+id+' > summary')
   summary.focus(); page.keyboard.press('Enter')
   assert page.locator('#'+id).get_attribute('open') is not None
   page.keyboard.press('Enter')
   assert page.locator('#'+id).get_attribute('open') is None
  page.goto(base)
  page.keyboard.press('Tab')
  assert page.evaluate('document.activeElement.className')=='skip-link'
  page.keyboard.press('Enter')
  assert page.evaluate('document.activeElement.id')=='main-content'
  assert not errors, errors
  assert not failed, failed
  decode_images(page)
  page.evaluate('window.scrollTo(0,0)'); page.wait_for_timeout(80)
  page.screenshot(path=str(out/f'home-{width}.png'),full_page=True)
  page.screenshot(path=str(out/f'hero-{width}.png'))
  if width==1440:
   page.locator('#research').scroll_into_view_if_needed(); page.screenshot(path=str(out/'research-desktop.png'))
   page.locator('#about').scroll_into_view_if_needed(); page.screenshot(path=str(out/'about-desktop.png'))
  checks.append(f'{width}px: no overflow, images decoded, section tracking, anchor clearance, keyboard and details passed')
  page.close()
 # Check all previous routes, research sub-fragments, encoded/invalid fragments, and history.
 page=browser.new_page(viewport={'width':1280,'height':900},reduced_motion='reduce')
 for route,anchor in [('research/','research'),('publications/','publications'),('talks/','talks'),('teaching/','teaching'),('cv/','cv'),('resume','cv'),('research/#picosec','picosec'),('research/#cms-gem','cms-gem'),('research/#new-rd','new-rd'),('#selected-work','publications')]:
  page.goto(base+route,wait_until='networkidle')
  page.wait_for_url('**/#'+anchor)
  if anchor in ['picosec','cms-gem']:
   assert page.locator('#previous-projects-section').get_attribute('open') is not None
   assert page.locator('#'+anchor).is_visible()
  checks.append(f'Legacy /{route} → /#{anchor}: passed')
 page.goto(base,wait_until='networkidle')
 page.locator('[data-nav="research"]').click();page.wait_for_function('document.body.dataset.section==="research"')
 page.locator('[data-nav="publications"]').click();page.wait_for_function('document.body.dataset.section==="publications"')
 page.go_back();page.wait_for_function('document.body.dataset.section==="research"')
 page.go_forward();page.wait_for_function('document.body.dataset.section==="publications"')
 checks.append('Browser back/forward: passed')
 assert page.evaluate('getComputedStyle(document.documentElement).scrollBehavior')=='auto'
 checks.append('Reduced motion: native instant scrolling, no animation')
 # Full document remains useful without scripting.
 context=browser.new_context(java_script_enabled=False,viewport={'width':390,'height':844})
 page=context.new_page(); page.goto(base,wait_until='networkidle')
 page.locator('[data-nav="publications"]').click()
 page.locator('#more-publications > summary').click()
 assert page.locator('#more-publications li').first.is_visible()
 page.goto(base+'research/')
 page.get_by_role('link',name='Continue to research').click()
 assert page.url.endswith('/#research')
 checks.append('No JavaScript: navigation, complete papers and legacy fallback link passed')
 browser.close()
(out/'browser-checks.json').write_text(json.dumps(checks,indent=2)+'\n')
print('\n'.join(checks))
