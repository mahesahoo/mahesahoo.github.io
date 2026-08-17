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
