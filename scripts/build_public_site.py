#!/usr/bin/env python3
"""Stage only reviewed website files; never publish the repository root."""

from __future__ import annotations

from pathlib import Path
import shutil
import sys

sys.dont_write_bytecode = True
import check_site


ROOT = Path(__file__).resolve().parents[1]
PUBLIC_FILES = (
    ".nojekyll",
    "CNAME",
    "robots.txt",
    "sitemap.xml",
    "404.html",
    "about.html",
    "capabilities.html",
    "career.html",
    "contact.html",
    "engage.html",
    "index.html",
    "principles.html",
    "privacy.html",
    "provenance.html",
    "rsc.html",
    "thanks.html",
    "work.html",
    "writing.html",
    "about-us/index.html",
    "assets/css/style.css",
    "assets/js/main.js",
    "assets/js/intake.js",
    "assets/img/favicon.svg",
    "assets/img/headshot.jpg",
    "assets/img/og-image.jpg",
    "assets/provenance/pqexpert_manifest.json",
    "assets/provenance/pqexpert_provenance_summary.txt",
    "assets/provenance/c2pa_readme.txt",
)


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python scripts/build_public_site.py NEW_OUTPUT_DIRECTORY")
        return 1
    destination = Path(sys.argv[1]).resolve()
    if destination.exists():
        print("Public site output directory must not already exist.")
        return 1

    for relative in PUBLIC_FILES:
        source = ROOT / relative
        if source.is_symlink() or not source.is_file():
            print(f"Public site input is missing or a symlink: {relative}")
            return 1

    destination.mkdir(parents=True)
    for relative in PUBLIC_FILES:
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / relative, target)

    # Check the staged site, so a link to an excluded source file fails the build.
    check_site.ROOT = destination
    for html_file in sorted(destination.rglob("*.html")):
        parser = check_site.ReferenceParser()
        parser.feed(html_file.read_text(encoding="utf-8"))
        for _, reference in parser.references:
            if not check_site.target_exists(html_file, reference):
                print(f"Public site has an unavailable local reference in {html_file.relative_to(destination)}.")
                return 1

    print(f"Prepared {len(PUBLIC_FILES)} reviewed public files with valid local references.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
