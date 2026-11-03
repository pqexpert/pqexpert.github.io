# Publish a website artifact instead of the repository root

This change prepares a GitHub Actions publication path. It must be activated in repository Pages settings; adding a workflow alone does not change an existing branch/root publishing source.

## Public artifact

`scripts/build_public_site.py` copies an explicit list of 28 website files into a new output directory and checks local references within that output. The artifact includes the HTML pages, legacy About redirect, referenced CSS/JavaScript/images, three public provenance downloads, domain declaration, crawler files, and the no-Jekyll marker.

Repository governance, operating procedures, Python checks, shell helpers, CI configuration, and Git history are excluded. Future public files must be added deliberately to the list. Repository visibility remains a separate setting: excluding a file from the website does not hide it in a public GitHub repository.

For local verification, run the source quality check, then give the builder a new output directory outside the checkout:

```bash
python scripts/check_site.py
python scripts/build_public_site.py /tmp/pqexpert-public-site-review
python -m http.server --directory /tmp/pqexpert-public-site-review 8000
```

The builder refuses an existing output directory rather than deleting or reusing its contents.

## Activation

1. Review the artifact and retain the current Pages settings for rollback.
2. In repository Settings, open Pages and change the build source from **Deploy from a branch** to **GitHub Actions**. Keep the existing custom domain and HTTPS settings.
3. Merge the reviewed workflow and builder into `main`, or manually run **Publish public site** on `main` if the workflow is already present.
4. Verify the workflow's build and deploy jobs succeed for the intended commit. The `github-pages` environment should permit deployment from `main` only.
5. Verify the homepage, About redirect, navigation, contact paths, images, and provenance downloads on the custom domain.
6. Confirm `/scripts/check_site.py`, `/deploy.sh`, `/GOVERNANCE.md`, and `/docs/FAMILY_JOURNEYS.md` return a 404 response rather than their repository contents. The custom 404 recovery page may render for those URLs; inspect the status as well as the page.

The existing **Site quality** workflow remains available for pull requests. The deployment workflow also validates its exact source commit before staging and deployment. It does not change DNS or the custom domain.

## Other hosts

Any other host connected to this repository has its own output-directory and deployment settings. Verify and configure that host separately to publish the same reviewed artifact; a GitHub Pages source change does not alter another provider's publication.

## Rollback

Prefer a corrective commit followed by the artifact deployment. If the deployment mechanism itself fails, an authorized operator can temporarily restore the recorded branch/root Pages setting and recheck the domain. That fallback publishes repository files again, so use it only for bounded recovery and return to the reviewed artifact promptly. Do not force-push or rewrite repository history as a deployment rollback.

## References

- [Configure a GitHub Pages publishing source](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)
- [Use custom workflows with GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)
