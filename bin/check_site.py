"""Check that the Pages artifact contains the site and resolves its local links."""

import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit


class PageLinks(HTMLParser):
    def __init__(self, file):
        super().__init__()
        self.links = []
        self.canonical = None
        self.feed(file.read_text(encoding="utf-8"))

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.links.extend(attrs[key] for key in ("href", "src", "data-src") if attrs.get(key))
        if tag == "link" and attrs.get("rel") == "canonical":
            self.canonical = attrs.get("href")


def check_site(root):
    required = (
        "index.html", "blog/index.html", "about/index.html", "publications/index.html",
        "showcase/index.html", "projects/index.html", "404.html", "feed.xml",
        "sitemap.xml", "robots.txt",
    )
    errors = [f"Missing output: {name}" for name in required if not (root / name).is_file()]
    if errors:
        return errors

    homepage = PageLinks(root / "index.html").canonical
    if not homepage:
        return ["Missing canonical URL on the homepage"]
    base = urlsplit(homepage)
    prefix = base.path.rstrip("/") + "/"

    for file in root.rglob("*.html"):
        relative = file.relative_to(root).as_posix()
        for link in PageLinks(file).links:
            target = urlsplit(urljoin(urljoin(homepage, relative), link))
            if (target.scheme, target.netloc) != (base.scheme, base.netloc):
                continue
            path = unquote(target.path)
            if not path.startswith(prefix):
                errors.append(f"{relative}: local link outside the site root {link}")
                continue
            local = root / path.removeprefix(prefix)
            if not local.is_file() and not (local / "index.html").is_file():
                errors.append(f"{relative}: missing local link {link}")

    for name in (".git", ".obsidian", ".tools", "_verification", "bin", "docs", "templates", "themes"):
        if (root / name).exists():
            errors.append(f"Source directory leaked into output: {name}")
    return errors


if __name__ == "__main__":
    output = Path(sys.argv[1] if len(sys.argv) > 1 else "public")
    problems = check_site(output)
    if problems:
        sys.exit("\n".join(dict.fromkeys(problems)))
    print("Generated pages, local links, and deployment contents are valid.")
