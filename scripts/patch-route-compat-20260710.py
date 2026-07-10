from pathlib import Path

root = Path(__file__).resolve().parents[1]

index_path = root / 'index.html'
index = index_path.read_text(encoding='utf-8')
old = '  <section class="home-roles-section" id="roles" aria-labelledby="roles-title">'
new = '  <span id="audience-gateway" class="home-anchor-alias" aria-hidden="true"></span>\n  <section class="home-roles-section" id="roles" aria-labelledby="roles-title">'
if old not in index:
    raise SystemExit('index marker not found or already patched')
index_path.write_text(index.replace(old, new, 1), encoding='utf-8')

css_path = root / 'css' / 'home-clarity.css'
css = css_path.read_text(encoding='utf-8')
css_marker = '/* Common section structure */'
css_insert = '''/* Backward-compatible target for older global navigation links. */
.home-anchor-alias {
  display: block;
  position: relative;
  top: -92px;
  height: 0;
  visibility: hidden;
}

'''
if '.home-anchor-alias {' not in css:
    if css_marker not in css:
        raise SystemExit('css marker not found')
    css = css.replace(css_marker, css_insert + css_marker, 1)
css_path.write_text(css, encoding='utf-8')

nav_path = root / 'scripts' / 'simplify-global-nav.js'
nav = nav_path.read_text(encoding='utf-8')
old_nav = 'href="/index.html#audience-gateway"'
new_nav = 'href="/index.html#roles"'
if old_nav not in nav:
    raise SystemExit('global nav marker not found or already patched')
nav_path.write_text(nav.replace(old_nav, new_nav), encoding='utf-8')
