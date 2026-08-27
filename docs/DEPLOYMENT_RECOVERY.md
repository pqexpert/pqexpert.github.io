# PQExpert.io Deployment and Recovery

## Purpose

PQExpert.io is a static GitHub Pages site. This document is the durable public-repository runbook for publishing, verification, rollback, and custom-domain recovery.

The goal is simple: a future operator should be able to restore the public front door without relying on a chat thread, a remembered command, or a force push.

## Current source model

- Repository: `pqexpert/pqexpert.github.io`
- Production source branch: `main`
- Site source: repository root
- Custom-domain declaration: `CNAME`
- Expected custom domain: `pqexpert.io`
- Static validation: `.github/workflows/site-quality.yml`
- Local validation: `python scripts/check_site.py`

GitHub repository state is the durable source for the static site. GitHub Pages serves the published copy. The published copy may lag the merge briefly while Pages rebuilds or caches expire.

## Normal publish path

1. Create a branch from current `main`.
2. Make the smallest coherent change.
3. Run or allow the `Site quality` workflow to validate the branch/PR.
4. Review public/private boundaries, maturity labels, navigation, contact routing, and local references.
5. Merge only after the quality check is green.
6. Confirm the `main` push quality run is green.
7. Verify the live site after Pages propagation.

Do **not** use a force push as the normal deployment mechanism.

## Local validation

```bash
python scripts/check_site.py
```

For visual review:

```bash
python -m http.server 8000
```

Then open `http://localhost:8000`.

## Required production invariants

Before treating a release as healthy, verify:

- `main` contains the intended source;
- `CNAME` still resolves to `pqexpert.io` as the repository declaration;
- the `Site quality` workflow passes;
- the homepage describes PQExpert as the public client/professional front door;
- client-facing navigation remains on PQExpert rather than sending readers to a separate RSC website;
- contact and engagement routes work;
- public pages do not expose credentials, secrets, client data, private identity material, restricted research, or sensitive implementation detail;
- in-development projects remain maturity-labeled;
- no unsupported customer, certification, clearance, deployment, contract, or adoption claim has been introduced.

## Deployment verification

Use three independent checks when possible:

1. **Source check** — inspect `main` and confirm the expected commit/file contents.
2. **Automation check** — confirm the `Site quality` run for the production commit is green.
3. **Published-site check** — load `https://pqexpert.io` and verify the rendered copy reflects the production source after propagation.

If source and automation are correct but the public site still shows an older copy, treat that as a deployment/cache propagation issue before rewriting source unnecessarily.

## Rollback

Preferred rollback is an ordinary Git revert or a corrective pull request.

Do not rewrite `main` history merely to return to an older public state.

A safe rollback sequence is:

1. identify the last known-good production commit;
2. identify the change that introduced the problem;
3. revert that change or prepare a corrective branch;
4. allow the normal quality check to run;
5. merge the correction;
6. verify the production `main` check;
7. verify the live site after propagation.

## Custom-domain recovery

If the repository source is healthy but `pqexpert.io` does not resolve correctly:

1. Confirm the repository `CNAME` file contains `pqexpert.io`.
2. Inspect the repository's GitHub Pages settings and confirm the production source is still `main` / repository root and the custom domain is still set.
3. Inspect the authoritative DNS provider for the current domain records. Do not guess or overwrite DNS from memory.
4. Compare the live DNS configuration with GitHub Pages' current custom-domain guidance before making a change.
5. Preserve HTTPS enforcement once GitHub reports the domain is correctly configured.
6. After any DNS or Pages change, allow normal DNS/certificate propagation and verify from more than one resolver/network if necessary.

The repository intentionally does not hard-code provider-specific DNS records because those are external operational state and may change.

## Domain / Pages incident triage

### Source is wrong
Fix GitHub source through the normal branch/PR/revert path.

### Source is correct, workflow is red
Resolve the quality-check failure before treating the release as healthy.

### Source and workflow are correct, live site is stale
Allow for Pages/cache propagation; verify the latest production commit and check the live site again before creating duplicate source changes.

### Custom domain fails but `pqexpert.github.io` works
Treat the problem as Pages/custom-domain/DNS state rather than application source.

### Both GitHub Pages and custom domain fail
Check repository availability, Pages configuration, source branch, CNAME, recent changes, and GitHub service status before changing DNS.

## Emergency public-safety correction

If a live page exposes a credential, secret, client-sensitive material, protected identity information, or dangerous implementation detail:

1. remove or redact the exposed content immediately through a minimal corrective commit/PR;
2. rotate any exposed credential or secret through the owning system — deleting it from the page is not sufficient;
3. assess Git history and cached/public copies;
4. follow `SECURITY.md` for incident handling;
5. document the durable corrective control so the same class of exposure is less likely to recur.

## Legacy deploy script

`deploy.sh` is retained as a convenience wrapper for validation and a normal non-force push. It is **not** a repository-creation/bootstrap tool and must not rewrite production history.

## Recovery principle

**Source first, verification second, deployment third, DNS fourth.**

Fix the layer that is actually broken. Do not use a domain or deployment symptom as a reason to rewrite healthy application source.
