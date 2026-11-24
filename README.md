# mahesahoo.com

Personal portfolio site, deployed via GitHub Pages (see `CNAME`).

Static HTML — `index.html` is what ships. Styling is Tailwind CSS, compiled
ahead of time into `styles.css` (no CDN, no runtime build step, no JS framework).

## Editing styles

Tailwind utility classes are used directly in `index.html`. Custom CSS
(theme variables, animations, one-off component styles) lives in
`src/input.css`. After changing either file, rebuild:

```sh
npm install   # first time only
npm run build # writes the compiled, minified styles.css
```

`npm run watch` rebuilds on save while you're iterating.

The build also stamps `styles.css?v=<hash>` into `index.html` and `404.html`
(`scripts/stamp_css.py`). Cloudflare caches CSS for four hours, so without the
hash a rebuild would keep serving the old stylesheet to repeat visitors.

## Fonts

Self-hosted, Latin subset, three files in `fonts/` (`inter.woff2`,
`playfair-display.woff2`, `playfair-display-italic.woff2`). No Google Fonts
request at runtime. Regenerate with:

```sh
python scripts/fetch_fonts.py   # writes fonts/ + src/fonts.css
npm run build
```

`src/fonts.css` is generated — edit `scripts/fetch_fonts.py`, not the CSS.
