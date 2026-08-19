# PQExpert.io

Professional portfolio and public credibility surface for Josh Allen.

Live site: https://pqexpert.io

## Purpose

PQExpert.io gives hiring managers, technical reviewers, public-sector partners, and policy audiences a fast route to verified cybersecurity, infrastructure, systems-resilience, and national-security work.

The site follows five rules:

1. Service before status.
2. Evidence before hype.
3. Verified work, development work, and research direction remain visibly distinct.
4. Public pages use the Josh Allen professional identity.
5. Protected identity, job-search, clearance-related, contact-intelligence, client, secret, private spiritual-practice, and health data do not belong in this repository.

## Public operating charter

The portfolio is governed by [GOVERNANCE.md](GOVERNANCE.md) and the public [Operating Principles](principles.html) page. Public doctrine emphasizes human dignity, safety, stewardship, fairness, sustainable execution, learning, and beneficial outcomes while keeping private spiritual and health material out of the public proof surface.

## Site architecture

- `index.html`: primary credibility and routing surface
- `about.html`: professional context and operating standards
- `capabilities.html`: evidence-backed capability map
- `work.html`: selected work and maturity labels
- `writing.html`: public writing and research
- `career.html`: hiring and recruiter route
- `rsc.html`: concise company context
- `engage.html`: conversation routing
- `contact.html`: contact options
- `principles.html`: public operating principles
- `provenance.html`: public evidence and claim provenance
- `assets/`: styles, scripts, and public media

## Local review

The site is static and can be reviewed with any local HTTP server:

```bash
python -m http.server 8000
```

Open http://localhost:8000.

Run the repository quality check before publishing:

```bash
python scripts/check_site.py
```

## Evidence governance

Every material public claim should answer:

- What was done?
- In what environment?
- With which tools or methods?
- What changed?
- What evidence is public-safe?
- Is the work verified, in development, or research direction?
- Does the claim support useful service without sacrificing safety, dignity, or evidentiary discipline?

A roadmap item or planned repository is not implementation evidence. A course topic is not equivalent to professional experience. No page may imply an active clearance, customer, partnership, patent, production deployment, or institutional adoption without governed evidence.

## Change workflow

1. Confirm the claim against the governed source.
2. Check the change against `GOVERNANCE.md` and the public operating principles.
3. Keep protected information out of the repository and commit history.
4. Update the relevant page and provenance entry together.
5. Run `python scripts/check_site.py`.
6. Review the rendered site on desktop and mobile.
7. Publish only after links, claims, maturity labels, and public/private boundaries are correct.

See [CONTRIBUTING.md](CONTRIBUTING.md), [GOVERNANCE.md](GOVERNANCE.md), and [SECURITY.md](SECURITY.md).

## Public implementation roadmap

The employment-first technical-proof roadmap is tracked in [issue #1](https://github.com/pqexpert/pqexpert.github.io/issues/1).

## License status

No general reuse license has been granted yet. Repository visitors should not assume permission to reuse written content, images, branding, or code beyond rights provided by applicable law. A deliberate code/content licensing decision remains open.
