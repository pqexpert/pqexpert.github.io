#!/usr/bin/env python3
"""Check required governance files, public routing, and local references."""

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
import json
import os
import re
import subprocess
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
REQUIRED_ENGAGEMENT_ATTRIBUTION = (
    "cyber-resilience",
    "post-quantum-readiness",
    "security-operations",
    "executive-briefing",
    "prime-lab-research",
)
REQUIRED_CAREER_ATTRIBUTION = (
    "career-nav",
    "career-hero",
    "career-bottom",
    "career-footer",
)
LEGACY_LAUNCH17_ROUTES = (
    "cyber-resilience",
    "post-quantum-readiness",
    "security-operations",
    "teaming-and-suppliers",
    "research-collaboration",
    "executive-briefing",
    "hire-josh",
    "ask-the-author",
    "editorial-and-rights",
    "speaking-and-interviews",
    "private-contact",
    "professional-verification",
    "customer-support",
    "cmmc-readiness",
    "rsc-partners",
    "restoration-ledger",
    "introductions",
)
FORBIDDEN_PUBLIC_ROUTING = (
    "restoration-mt.com",
)

PUBLIC_TEXT_GLOBS = (
    "*.html",
    "assets/js/*.js",
    "assets/provenance/*",
    "docs/PUBLIC_*.md",
)
FORBIDDEN_PUBLIC_MARKERS = (
    "mailto:",
    "protected-identity",
    "identityReveal",
    "atob(",
    "orcid.org",
)
PHONE_PATTERN = re.compile(
    r"(?<!\d)(?:\+?1[-.\s]?)?\(?\d{3}\)?[-.\s]\d{3}[-.\s]\d{4}(?!\d)"
)
EMAIL_PATTERN = re.compile(
    r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b",
    re.IGNORECASE,
)
CREDENTIAL_PATTERNS = (
    re.compile(r"-----BEGIN (?:OPENSSH|RSA|EC|DSA|PGP)? ?PRIVATE KEY"),
    re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9]{36,}|github_pat_[A-Za-z0-9_]{50,})\b"),
    re.compile(r"\bsk-(?:proj-|svcacct-)?[A-Za-z0-9_-]{32,}\b"),
    re.compile(r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b"),
    re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b"),
)


def private_markers() -> tuple[str, ...]:
    """Load optional private checks without embedding identity data in source."""
    configured = os.environ.get("PQEXPERT_PRIVATE_MARKERS_FILE")
    if not configured:
        return ()
    try:
        path = Path(configured).expanduser().resolve()
        if path == ROOT or ROOT in path.parents:
            raise ValueError("Private marker configuration must be outside the repository.")
        values = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(values, list) or not values or not all(
            isinstance(value, str) and value.strip() for value in values
        ):
            raise ValueError("Private marker configuration must be a nonempty JSON string list.")
        return tuple(value.casefold() for value in values)
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        # Exception text can contain a private path or file contents.
        raise ValueError("Private marker configuration could not be read safely.") from exc


def source_files() -> list[Path]:
    """Include repository source and new files, excluding Git-ignored local data."""
    result = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    return [ROOT / os.fsdecode(path) for path in sorted(set(result.stdout.split(b"\0"))) if path]


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
    try:
        protected_markers = private_markers()
        public_sources = source_files()
    except (ValueError, OSError, subprocess.CalledProcessError):
        print("Site quality check failed: source inventory or private check configuration is invalid.")
        return 1

    for relative in REQUIRED_FILES:
        if not (ROOT / relative).exists():
            errors.append(f"missing required file: {relative}")

    html_files = sorted(ROOT.glob("*.html"))
    if not html_files:
        errors.append("no root HTML files found")

    engage_path = ROOT / "engage.html"
    if engage_path.exists():
        engage_text = engage_path.read_text(encoding="utf-8")
        for source in REQUIRED_ENGAGEMENT_ATTRIBUTION:
            if f"utm_content={source}" not in engage_text:
                errors.append(
                    f"engage.html: missing bounded attribution for {source!r}"
                )

    career_path = ROOT / "career.html"
    if career_path.exists():
        career_text = career_path.read_text(encoding="utf-8")
        for source in REQUIRED_CAREER_ATTRIBUTION:
            if f"utm_content={source}" not in career_text:
                errors.append(
                    f"career.html: missing bounded attribution for {source!r}"
                )

    moved_path = ROOT / "404.html"
    if moved_path.exists():
        moved_text = moved_path.read_text(encoding="utf-8")
        for route in LEGACY_LAUNCH17_ROUTES:
            if f'"{route}"' not in moved_text:
                errors.append(
                    f"404.html: missing moved-route recovery for {route!r}"
                )
            if route != "private-contact" and f"utm_content={route}" not in moved_text:
                errors.append(
                    f"404.html: missing bounded moved-route attribution for {route!r}"
                )
        if "utm_content=private-contact" in moved_text:
            errors.append(
                "404.html: private-contact must remain free of campaign attribution"
            )
        if '"private-contact": { name: "Private Contact", path: "/contact.html?journey=private#inquiry"' not in moved_text:
            errors.append(
                "404.html: private-contact recovery must use the private journey without attribution"
            )

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

    for pattern in PUBLIC_TEXT_GLOBS:
        for public_file in sorted(ROOT.glob(pattern)):
            if not public_file.is_file():
                continue
            text = public_file.read_text(encoding="utf-8")
            lowered = text.lower()

            for marker in FORBIDDEN_PUBLIC_MARKERS:
                if marker.lower() in lowered:
                    errors.append(
                        f"{public_file.relative_to(ROOT)}: restricted public markup detected (value redacted)"
                    )

    # A public repository exposes scripts and documentation as well as web pages.
    # Keep personal denylist values outside the checkout and redact all matches.
    for public_file in public_sources:
        relative = public_file.relative_to(ROOT)
        if public_file.is_symlink():
            errors.append(f"{relative}: symlink requires a separate publication review")
            continue
        if not public_file.is_file():
            continue
        try:
            text = public_file.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        except OSError:
            errors.append(f"{relative}: source could not be checked")
            continue
        lowered = text.casefold()

        if any(marker in lowered for marker in protected_markers):
            errors.append(f"{relative}: private marker detected (value redacted)")
        if any(not email.lower().endswith("@example.com") for email in EMAIL_PATTERN.findall(text)):
            errors.append(f"{relative}: public email address detected (value redacted)")
        if PHONE_PATTERN.search(text):
            errors.append(f"{relative}: public phone number detected (value redacted)")
        if any(pattern.search(text) for pattern in CREDENTIAL_PATTERNS):
            errors.append(f"{relative}: potential credential detected (value redacted)")

    for image_relative in ("assets/img/headshot.jpg", "assets/img/og-image.jpg"):
        image_path = ROOT / image_relative
        if not image_path.exists():
            errors.append(f"missing public image: {image_relative}")
            continue

        image_bytes = image_path.read_bytes()
        if not image_bytes.startswith(b"\xff\xd8\xff"):
            errors.append(f"{image_relative}: expected metadata-stripped JPEG")

        lowered_bytes = image_bytes.lower()
        for marker in (b"exif", b"<x:xmpmeta", b"photoshop", b"raw profile type iptc"):
            if marker in lowered_bytes:
                errors.append(
                    f"{image_relative}: embedded metadata marker {marker.decode('ascii')!r}"
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
