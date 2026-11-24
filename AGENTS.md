# AGENTS.md — mahesahoo.com

Read this before changing anything. It's the handoff: why it exists, what's
decided, what bites.

## What / why
Personal portfolio for **mahesahoo.com**. Static HTML, no framework, no runtime
build. Deployed by GitHub Pages on push to `main`. Cloudflare sits in front
(DNS + proxy + cache).

Owner: Mahesh (`mahesahoo`). Voice: direct, understated, no salesmanship — the
copy was deliberately "neutralised" once already. Don't reintroduce hype.

## Where things live
| Path | Role |
|---|---|
| `index.html` | the whole site (single page) |
| `src/input.css` | theme variables, custom components, animations |
| `src/fonts.css` | **generated** by `scripts/fetch_fonts.py`, don't hand-edit |
| `styles.css` | **generated** by `npm run build`, don't hand-edit |
| `404.html` | themed 404, served by GitHub Pages for any missing path |
| `sitemap.xml`, `robots.txt` | `robots.txt` is *not* in this repo — Cloudflare injects it |
| `resume/index.html` | `/resume` → 301 → `/resume/` → forwards to `resume.pdf` |
| `scripts/` | `fetch_fonts.py`, `stamp_css.py` |

## Build & deploy
```sh
npm run build     # Tailwind -> styles.css, then stamps styles.css?v=<hash>
npm run watch     # iterate; no stamping
git push origin main   # that IS the deploy
```

## Decisions (don't relitigate without reason)
- **Static + precompiled Tailwind.** No CDN, no JS framework, no build at runtime.
- **Self-hosted fonts** (3 woff2, Latin subset, variable). Zero third-party requests.
  Google served byte-identical files per weight, so they're deduped into one file
  per family with a weight range.
- **Cache-buster in the href** (`styles.css?v=<md5>`). Cloudflare caches CSS 4 h;
  without this, a rebuild keeps serving the old sheet.
- **Avatar is WebP** (19 KB vs 145 KB PNG). `profile.png` is kept only for
  `og:image` and the Apple touch icon, where crawlers are happier with PNG.
- **`/resume` is a redirect, not a rewrite.** GitHub Pages has no rewrite engine;
  a folder with `index.html` is the only supported way.
- **Projects section = AI Project Mentor, GATEwise, Pengu.** ProductiVize, TDS
  Virtual TA and Hypertrophy Systems were removed on purpose. Don't re-add them.
- **Contact email is `mahesh@mahesahoo.com`** (Zoho). Mail is on Zoho, MX points there.

## Gotchas that have actually burned us
- **Push rejected with GH007** if the commit author is the Gmail address — GitHub
  treats it as private. Commit with
  `git -c user.email="mahesahoo@users.noreply.github.com" ... commit --reset-author`.
- **Stale assets at the edge.** Cloudflare caches by URL: `resume.pdf` served an
  old copy for hours after a push. Fix = purge in the dashboard, or change the URL.
- **`*:Zone.Identifier` files** appear when editing on Windows. Now gitignored;
  never commit them.
- **`.fade-in` sections are invisible in a full-page screenshot** because they
  reveal on scroll. Not a bug. Scroll before capturing.
- **Tailwind must be rebuilt** after any class change in `index.html`, or new
  utilities simply don't exist in `styles.css`.

## Checks before calling it done
```sh
# live after ~1 min of Pages build
curl -s https://mahesahoo.com/ | grep -c "fonts.googleapis"   # expect 0
curl -sI https://mahesahoo.com/fonts/inter.woff2 | head -1    # expect 200
curl -s  https://mahesahoo.com/nope-xyz | grep "Nothing here" # custom 404
```
Screenshot with Playwright if layout changed (`#projects` card links should share
a baseline).

## Next
Open items live in `~/dev/NEXT.md` (repo-adjacent, not committed). Currently:
pin repos on GitHub, fix the global git email, licences, HSTS/cache rules,
Search Console submission.

## Feedback log
Append dated one-liners here. Don't rewrite past entries.
- 2026-11-24 — Voice rule: user asked for copy to be *neutralised* once. No hype, no salesmanship.
- 2026-11-24 — User does not want a hero "now" line; the About section already carries it.
- 2026-11-24 — Explain changes in plain language + give a way to verify, not just commit hashes.
