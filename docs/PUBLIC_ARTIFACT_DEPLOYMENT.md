# Publish a website artifact instead of the repository root

This repository provides a GitHub Actions publication path. Its activation must be confirmed in repository Pages settings; adding a workflow or observing its successful deployment alone does not establish that an existing branch/root publishing source has been disabled.

## Public artifact

`scripts/build_public_site.py` copies 27 explicitly listed website files and generates an empty `.nojekyll` marker in a new output directory, then checks local references within that output. The 28-file artifact includes the HTML pages, legacy About redirect, referenced CSS/JavaScript/images, three public provenance downloads, domain declaration, crawler files, and the generated marker.

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
2. Publish the reviewed workflow and builder to `main` and verify their exact contents on that branch.
3. In repository Settings, open Pages and change the build source from **Deploy from a branch** to **GitHub Actions**. Keep the existing custom domain and HTTPS settings, then run **Publish public site** on `main` if a deployment for the intended commit has not already succeeded.
4. Verify the workflow's build and deploy jobs succeed for the intended commit. The `github-pages` environment should permit deployment from `main` only.
5. Verify the homepage, About redirect, navigation, contact paths, images, and provenance downloads on the custom domain.
6. Confirm `/scripts/check_site.py`, `/deploy.sh`, `/GOVERNANCE.md`, and `/docs/FAMILY_JOURNEYS.md` return a 404 response rather than their repository contents. The custom 404 recovery page may render for those URLs; inspect the status as well as the page.

The existing **Site quality** workflow remains available for pull requests. The deployment workflow also validates its exact source commit before staging and deployment. It does not change DNS or the custom domain.

## Legacy branch/root fallback

Until the Pages build source is confirmed as **GitHub Actions**, a legacy branch build may deploy after the custom artifact. `_config.yml` excludes the current repository-only files and directories from that Jekyll build. Keep `.nojekyll` out of the source root: a root marker bypasses Jekyll and its exclusions. The custom artifact builder generates its own marker without changing the reviewed website bytes.

This fallback protects the current source inventory; it is not an allowlist for future repository files. Review the exclusion list whenever source-only files are added, and prefer the explicit artifact deployment. Verify excluded URLs after the last completed Pages deployment, including legacy runs. Do not infer the active administrative setting from workflow success alone.

## Other hosts

Any other host connected to this repository has its own output-directory and deployment settings. A GitHub Pages source change does not alter another provider's publication.

For the existing Vercel Git integration, `vercel.json` runs the source check and the same public-artifact builder, then serves only `public-site/`. It retains the static "Other" framework preset and does not create a project, change domains, add functions, change the plan, or modify paid build settings. The generated directory is Git-ignored.

After the Git integration deploys the intended commit, confirm the production deployment is ready and repeat the public-file and excluded-file checks on its assigned domains. The source check expects a Git checkout, as provided by this existing Git deployment path; a source upload without Git metadata will fail that check and must not be treated as a tested deployment.

## Rollback

Prefer a corrective commit followed by the artifact deployment. If the deployment mechanism itself fails, an authorized operator can temporarily use the recorded branch/root Pages setting only with the reviewed `_config.yml` exclusions and no root `.nojekyll`. Recheck public pages and excluded-file HTTP status after deployment, then return to the reviewed artifact path. Do not restore unrestricted root publication, force-push, or rewrite repository history as a deployment rollback.

## References

- [Configure a GitHub Pages publishing source](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)
- [Use custom workflows with GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)
- [GitHub Pages static site generators and the no-Jekyll marker](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site#static-site-generators)
- [Jekyll exclusion configuration](https://jekyllrb.com/docs/configuration/options/)
