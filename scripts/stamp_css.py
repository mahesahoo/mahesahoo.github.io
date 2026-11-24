"""stamp_css.py — rewrite the styles.css cache-buster with a content hash.

Cloudflare caches styles.css for 4 hours, so a rebuild would otherwise keep
serving the old stylesheet to repeat visitors. Stamping the href makes every
build unique:

    styles.css?v=3f8a1c9d

Run by `npm run build`.
"""
import hashlib
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
TARGETS = ["index.html", "404.html"]
PATTERN = re.compile(r'(styles\.css\?v=)[0-9a-z]+')


def main():
    digest = hashlib.md5((ROOT / "styles.css").read_bytes()).hexdigest()[:8]
    for name in TARGETS:
        p = ROOT / name
        if not p.exists():
            continue
        s = p.read_text()
        new, n = PATTERN.subn(rf"\g<1>{digest}", s)
        if n:
            p.write_text(new)
            print(f"{name}: styles.css?v={digest}")
        else:
            print(f"{name}: no cache-buster found")


if __name__ == "__main__":
    main()
