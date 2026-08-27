# PQExpert.io

PQExpert.io is the **canonical public client, professional, evidence, and engagement surface** for Josh Allen and Restoration Security Consultants (RSC).

Live site: https://pqexpert.io

## Operating architecture

The current system is intentionally split by function:

- **PQExpert.io** = public front door, client intake, capability/evidence surface, writing, verification, and engagement routing.
- **Restoration Security Consultants (RSC)** = commercial operating context used when a scoped conversation becomes company-backed delivery, contracting, or business-development work.
- **GitHub** = durable engineering, technical documentation, architecture, runbooks, implementation evidence, tests, provenance, recovery knowledge, and repository-local truth.
- **Notion** = governance and control layer for strategic state, decisions, maturity, approval boundaries, and operating priorities.

Public readers should not have to discover a separate RSC website before opening a serious conversation. PQExpert remains the public route unless contracting, compliance, due diligence, or another authoritative process requires deeper entity detail.

See:

- [`docs/PUBLIC_SYSTEM_ARCHITECTURE.md`](docs/PUBLIC_SYSTEM_ARCHITECTURE.md)
- [`docs/PUBLIC_PROJECT_PORTFOLIO.md`](docs/PUBLIC_PROJECT_PORTFOLIO.md)
- [`docs/CLIENT_ROUTING.md`](docs/CLIENT_ROUTING.md)
- [`docs/PUBLIC_EVIDENCE_MAP.md`](docs/PUBLIC_EVIDENCE_MAP.md)
- [`docs/DEPLOYMENT_RECOVERY.md`](docs/DEPLOYMENT_RECOVERY.md)
- [`THREAT_MODEL.md`](THREAT_MODEL.md)
- [`GOVERNANCE.md`](GOVERNANCE.md)

## Purpose

PQExpert.io gives clients, technical reviewers, partners, hiring managers, public-sector readers, and policy audiences a fast route to evidence-backed cybersecurity, infrastructure, systems-resilience, post-quantum readiness, technical-strategy, and national-security work.

The site follows six rules:

1. **One public front door.** PQExpert is the canonical external route.
2. **Service before status.** Public work exists to increase useful capability and beneficial outcomes.
3. **Evidence before hype.** Verified work, in-development work, and research direction remain visibly distinct.
4. **GitHub holds durable technical truth.** Implementation, docs, runbooks, tests, provenance, and recovery knowledge live with repositories.
5. **Notion governs state and decisions.** Governance does not replace repo-local implementation truth.
6. **Protected information stays out.** Public pages and public repository history exclude protected identity, job-search records, clearance-related material, client secrets, private spiritual-practice material, health information, credentials, and sensitive operational data.

## Site architecture

- `index.html`: primary client/front-door, credibility, system-architecture, and routing surface
- `about.html`: professional context and operating standards
- `capabilities.html`: evidence-backed capability map
- `work.html`: verified work plus public-safe private-R&D portfolio
- `writing.html`: public writing and research
- `career.html`: hiring and recruiter route
- `rsc.html`: how the RSC commercial layer fits behind PQExpert
- `engage.html`: client, partner, research, briefing, and hiring routing
- `contact.html`: canonical public contact route
- `principles.html`: public operating principles
- `provenance.html`: public evidence and claim provenance
- `docs/`: public-safe architecture, project, routing, evidence, deployment, and recovery documentation
- `THREAT_MODEL.md`: public-surface threat model and residual-risk register
- `assets/`: styles, scripts, and public media

## Public project model

The private engineering estate includes work around:

- dynamic threat modeling;
- governed continuous validation / red-team automation;
- post-quantum readiness and migration analysis;
- hardened reproducible environments;
- secure access / desktop-streaming experiments;
- RSC operator-console and observability work;
- controlled CRM/workflow automation;
- penetration-testing and security-analysis tooling;
- integration/orchestration and delta-propagation controls.

Public descriptions are maturity-labeled. Private repository existence, naming, or architecture does not imply production deployment, customer adoption, certification, or contract performance.

## Repository documentation contract

Material repositories should carry documentation close to the implementation. At minimum, mature projects should converge on:

- `README.md` — purpose, current reality, quickstart, boundaries, maturity
- `AGENTS.md` — agent/automation governance when agents or coding automation operate in the repo
- `SECURITY.md` — vulnerability reporting, secret handling, security assumptions, authorization boundaries
- architecture documentation — components, data flows, trust boundaries, dependencies
- runbook / recovery documentation — startup, shutdown, backup, restore, rollback, health checks
- roadmap / status — what is verified, in development, blocked, or conceptual
- tests / CI — where meaningful
- provenance / limitations — evidence, uncertainty, claims, and public/private boundaries

The private cross-repository estate map and documentation standard are maintained in the governed private hub repository. This public repo contains only the public-safe projection.

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
- Does the claim support useful service without sacrificing safety, dignity, privacy, or evidentiary discipline?

A roadmap item or planned repository is not implementation evidence. A course topic is not equivalent to professional experience. No page may imply an active clearance, customer, partnership, patent, production deployment, institutional adoption, certification, or contract award without governed evidence.

## Change workflow

1. Confirm the claim or state against the owning governed source.
2. Check the change against `GOVERNANCE.md` and the public operating principles.
3. Put durable implementation/documentation changes in GitHub, not only in a dashboard or chat thread.
4. Keep protected information out of repository content and commit history.
5. Update the relevant page and provenance/public project entry together.
6. Run `python scripts/check_site.py`.
7. Review the rendered site on desktop and mobile.
8. Publish only after links, claims, maturity labels, routing, and public/private boundaries are correct.

See [CONTRIBUTING.md](CONTRIBUTING.md), [GOVERNANCE.md](GOVERNANCE.md), [SECURITY.md](SECURITY.md), [THREAT_MODEL.md](THREAT_MODEL.md), and [docs/DEPLOYMENT_RECOVERY.md](docs/DEPLOYMENT_RECOVERY.md).

## Public implementation roadmap

The employment-first technical-proof and public-credibility roadmap is tracked in [issue #1](https://github.com/pqexpert/pqexpert.github.io/issues/1).

## License status

No general reuse license has been granted yet. Repository visitors should not assume permission to reuse written content, images, branding, or code beyond rights provided by applicable law. A deliberate code/content licensing decision remains open.
