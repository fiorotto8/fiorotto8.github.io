#!/usr/bin/env python3
"""Check the built site's local links, metadata, records and output boundaries.

Run after bin/build. Uses only the Python standard library.
"""
import argparse
from collections import Counter
from html import unescape
from html.parser import HTMLParser
import json
from pathlib import Path
from urllib.parse import unquote, urlsplit


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.ids = []
        self.headings = []
        self.refs = []
        self.images = []
        self.classes = Counter()
        self.canonical = None
        self.json_blocks = []
        self.in_json = False
        self.raw = path.read_text()
        self.feed(self.raw)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        if tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
            self.headings.append(int(tag[1]))
        self.classes.update(attrs.get('class', '').split())
        if tag == 'img':
            self.images.append(attrs)
        for key in ('href', 'src', 'poster', 'data-redirect'):
            if attrs.get(key):
                self.refs.append(attrs[key])
        if 'srcset' in attrs:
            self.refs.extend(item.strip().split()[0] for item in attrs['srcset'].split(','))
        if tag == 'link' and attrs.get('rel') == 'canonical':
            self.canonical = attrs['href']
        if tag == 'meta' and (attrs.get('property') == 'og:image' or attrs.get('name') == 'twitter:image'):
            self.refs.append(attrs['content'])
        if tag == 'script' and attrs.get('type') == 'application/ld+json':
            self.in_json = True
            self.json_blocks.append('')

    def handle_data(self, data):
        if self.in_json:
            self.json_blocks[-1] += data

    def handle_endtag(self, tag):
        if tag == 'script':
            self.in_json = False


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('site', nargs='?', default='_site')
    parser.add_argument('--baseurl', default='')
    args = parser.parse_args()
    root = Path(args.site).resolve()
    source = Path(__file__).resolve().parents[1]
    pages = {path: Page(path) for path in root.rglob('*.html')}
    errors = []
    referenced_files = set()

    def require(condition, message):
        if not condition:
            errors.append(message)

    require(bool(pages), 'No generated HTML; run bash bin/build first.')
    for path, page in pages.items():
        label = path.relative_to(root).as_posix()
        require(len(page.ids) == len(set(page.ids)), f'{label}: duplicate IDs')
        require(page.headings.count(1) == 1, f'{label}: expected one H1')
        require(all(b <= a + 1 for a, b in zip(page.headings, page.headings[1:])), f'{label}: skipped heading level')
        require(bool(page.canonical), f'{label}: missing canonical URL')
        require('{{' not in page.raw and '{%' not in page.raw, f'{label}: unrendered Liquid')
        for block in page.json_blocks:
            try:
                json.loads(block)
            except ValueError as error:
                errors.append(f'{label}: invalid structured data: {error}')
        for image in page.images:
            require(bool(image.get('alt')), f'{label}: missing image alt text')
            require('width' in image and 'height' in image, f'{label}: missing image dimensions')
        for reference in page.refs:
            url = urlsplit(reference)
            if url.scheme and url.scheme not in ('http', 'https'):
                continue
            if url.netloc and url.hostname not in ('fiorotto8.github.io', 'localhost', '127.0.0.1'):
                continue
            urlpath = unquote(url.path)
            if urlpath.startswith('/'):
                if args.baseurl:
                    require(urlpath.startswith(args.baseurl + '/'), f'{label}: URL escapes baseurl: {reference}')
                    urlpath = urlpath.removeprefix(args.baseurl)
                target = root / urlpath.lstrip('/')
            else:
                target = path.parent / urlpath if urlpath else path
            if target.is_dir():
                target /= 'index.html'
            require(target.is_file(), f'{label}: broken local URL: {reference}')
            referenced_files.add(target.resolve())
            if target in pages and url.fragment:
                require(unquote(url.fragment) in pages[target].ids, f'{label}: missing fragment: {reference}')

    home = pages.get(root / 'index.html')
    require(home is not None, 'Homepage missing')
    if home:
        for anchor in ('intro', 'research', 'publications', 'talks', 'teaching', 'about', 'contact', 'cv', 'cygno04', 'xray-polarimetry', 'new-rd', 'picosec', 'cms-gem'):
            require(anchor in home.ids, f'Missing public anchor: {anchor}')
        for collection in ('publications', 'talks', 'posters'):
            records = json.loads((source / '_data' / f'{collection}.json').read_text())
            for record in records:
                require(record['title'] in unescape(home.raw), f'Missing {collection} title: {record["title"]}')
                if record.get('url'):
                    require(record['url'] in unescape(home.raw), f'Missing source link: {record["url"]}')
        papers = json.loads((source / '_data/publications.json').read_text())
        talks = json.loads((source / '_data/talks.json').read_text())
        posters = json.loads((source / '_data/posters.json').read_text())
        require(home.classes['publication-record'] == len(papers), 'Publication count differs from data')
        require(home.classes['talk-record'] == len(talks) + len(posters), 'Talk/poster count differs from data')

    for route in ('research', 'publications', 'talks', 'teaching', 'cv', 'resume'):
        require(root / route / 'index.html' in pages, f'Missing legacy route: /{route}/')
    for forbidden in ('AGENTS.md', 'CLAUDE.md', 'Universal Website De-AIification and Human Art Direction Prompt.md', 'docs', 'bin', 'vendor', 'files/cv.tex', 'feed.xml', 'images/local', 'images/README.md', 'images/personal_images', 'images/work_images', 'images/image_larger_resolution', 'images/selected'):
        require(not (root / forbidden).exists(), f'Unexpected published file: {forbidden}')
    require((root / 'files/CV.pdf').is_file(), 'CV PDF missing')
    manifest = root / 'images/public/identity/manifest.json'
    require(manifest.is_file(), 'Web manifest missing')
    if manifest.is_file():
        try:
            manifest_data = json.loads(manifest.read_text())
            for icon in manifest_data.get('icons', []):
                icon_url = urlsplit(icon['src']).path
                if args.baseurl:
                    require(icon_url.startswith(args.baseurl + '/'), f'Manifest icon escapes baseurl: {icon_url}')
                    icon_url = icon_url.removeprefix(args.baseurl)
                icon_path = root / icon_url.lstrip('/')
                require(icon_path.is_file(), f'Missing manifest icon: {icon_url}')
                referenced_files.add(icon_path.resolve())
        except ValueError as error:
            errors.append(f'Invalid web manifest: {error}')
    for asset in (root / 'images/public').rglob('*'):
        if asset.is_file():
            require(asset.resolve() in referenced_files, f'Unused public asset: {asset.relative_to(root)}')
    if errors:
        raise SystemExit('\n'.join(errors))
    size = sum(path.stat().st_size for path in root.rglob('*') if path.is_file())
    print(f'PASS: {len(pages)} pages; local links, anchors, headings, metadata, records and output boundaries. Built size: {size / 1024:.0f} KiB.')


if __name__ == '__main__':
    main()
