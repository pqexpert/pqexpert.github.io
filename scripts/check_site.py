#!/usr/bin/env python3
"""Check required governance files, public routing, and local references."""

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = (
    "README.md",
    "GOVERNANCE.md",
    "SECURITY.md",
    "CONTRIBUTING.md",
    "CNAME",
    "404.html",
    "index.html",
    "principles.html",
    "robots.txt",
    "sitemap.xml",
    "docs/PUBLIC_SYSTEM_ARCHITECTURE.md",
    "docs/PUBLIC_PROJECT_PORTFOLIO.md",
    "docs/CLIENT_ROUTING.md",
    "docs/PUBLIC_EVIDENCE_MAP.md",
    "docs/DEPLOYMENT_RECOVERY.md",
)
HTML_REQUIREMENTS = ("<title", 'name="description"', "<html")
SKIP_SCHEMES = ("http", "https", "mailto", "tel", "javascript", "data")
FORBIDDEN_PUBLIC_ROUTING = (
    "restoration-mt.com",
)


class ReferenceParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.references: list[tuple[str, str]] = []

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        attr_name = "href" if tag in {"a", "link"} else "src" if tag in {
            "img",
            "script",
            "source",
        } else None
        if not attr_name:
            return
        for name, value in attrs:
            if name == attr_name and value:
                self.references.append((tag, value))


def target_exists(source: Path, reference: str) -> bool:
    parts = urlsplit(reference)
    if parts.scheme.lower() in SKIP_SCHEMES or parts.netloc:
        return True
    if not parts.path or parts.path == "/":
        return True

    path = Path(unquote(parts.path.lstrip("/")))
    target = ROOT / path if parts.path.startswith("/") else source.parent / path
    if target.is_dir():
        target = target / "index.html"
    return target.exists()


def main() -> int:
    errors: list[str] = []

    for relative in REQUIRED_FILES:
        if not (ROOT / relative).exists():
            errors.append(f"missing required file: {relative}")

    html_files = sorted(ROOT.glob("*.html"))
    if not html_files:
        errors.append("no root HTML files found")

    for html_file in html_files:
        text = html_file.read_text(encoding="utf-8")
        lowered = text.lower()
        for marker in HTML_REQUIREMENTS:
            if marker not in lowered:
                errors.append(f"{html_file.name}: missing {marker}")

        for forbidden in FORBIDDEN_PUBLIC_ROUTING:
            if forbidden.lower() in lowered:
                errors.append(
                    f"{html_file.name}: forbidden public routing reference {forbidden!r}; "
                    "keep the client journey on PQExpert and route RSC internally"
                )

        parser = ReferenceParser()
        parser.feed(text)
        for tag, reference in parser.references:
            if not target_exists(html_file, reference):
                errors.append(
                    f"{html_file.name}: unresolved {tag} reference {reference!r}"
                )

    if errors:
        print("Site quality check failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        f"Site quality check passed for {len(html_files)} HTML files; "
        "required governance/docs are present and public routing guardrails passed."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
