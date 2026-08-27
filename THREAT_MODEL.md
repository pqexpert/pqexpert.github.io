# PQExpert.io Public-Surface Threat Model

## Scope

This threat model covers the public static website and repository controls for `pqexpert.io`. It does not describe private client environments, private R&D internals, credentials, or offensive-security implementation details.

## Assets to protect

- public trust and claim accuracy;
- domain and GitHub Pages availability;
- repository integrity and production history;
- visitor contact information submitted through the public form;
- professional identity and brand integrity;
- confidentiality of private technical, client, identity, academic, and operational information;
- accurate separation between Verified, In Development, Research, and private/blocked work;
- correct routing between PQExpert public intake and RSC commercial delivery context.

## Trust boundaries

1. **GitHub repository / main branch** — durable static source.
2. **GitHub Actions / quality checks** — automated validation, not a substitute for review.
3. **GitHub Pages / custom domain** — publication and TLS/DNS boundary.
4. **Browser / public visitor** — untrusted input and client environment.
5. **Formspree** — third-party contact-form processor.
6. **Calendly and other outbound professional links** — external services outside repository control.
7. **External fonts / social / publishing links** — third-party availability and privacy boundaries.
8. **Private governance and technical repositories** — intentionally not exposed through the public site.

## Primary threats and controls

### 1. Sensitive information accidentally published

**Threat:** Credentials, customer information, protected identity material, sensitive infrastructure detail, private research, or other non-public context enters HTML, Markdown, assets, or Git history.

**Controls:**

- explicit public/private boundary in `GOVERNANCE.md` and `SECURITY.md`;
- public-safe evidence map rather than raw private records;
- pull-request review for normal publication;
- repository search and static checks for known routing/claim regressions;
- minimal-disclosure rule for private R&D;
- immediate secret rotation if a secret is exposed; deletion alone is insufficient.

**Residual risk:** Human review can miss novel sensitive material; commit history and caches may retain deleted content.

### 2. Claim inflation / misleading maturity

**Threat:** A private repository, mockup, architecture document, prototype, or experiment is presented as production deployment, customer adoption, certification, contract performance, or proven security.

**Controls:**

- maturity labels: Verified / In Development / Research;
- `docs/PUBLIC_EVIDENCE_MAP.md`;
- public project portfolio with explicit limitations;
- proof-before-claim governance;
- no unsupported customer, clearance, contract, certification, adoption, patent, or production claims.

**Residual risk:** Marketing language can drift over time unless evidence and page changes remain coupled.

### 3. Client-routing confusion

**Threat:** Public visitors are sent to an obsolete or competing RSC website and cannot quickly understand where to engage.

**Controls:**

- PQExpert designated canonical public front door;
- RSC described as commercial operating context behind appropriate scoped work;
- CI forbids `restoration-mt.com` references in public HTML;
- internal `/rsc.html`, `/engage.html`, and `/contact.html` routes.

**Residual risk:** Search engines, old bookmarks, cached pages, or third-party profiles may still surface legacy URLs.

### 4. Repository or production-history corruption

**Threat:** Force push or ad-hoc deployment rewrites `main`, bypassing review and making rollback/provenance difficult.

**Controls:**

- `deploy.sh` does not force push;
- normal branch -> PR -> quality check -> merge path;
- rollback by revert/corrective PR;
- deployment/recovery runbook.

**Residual risk:** Repository administrators can still bypass controls if permissions allow it.

### 5. Domain / Pages misconfiguration or hijack

**Threat:** DNS, CNAME, GitHub Pages configuration, or account compromise redirects the public site or causes outage.

**Controls:**

- repository `CNAME` declaration;
- custom-domain recovery runbook;
- GitHub account security and appropriate repository permissions;
- HTTPS enforcement when Pages reports the domain is correctly configured;
- source/deployment/DNS triage separation.

**Residual risk:** DNS registrar/provider compromise and GitHub account compromise are external control-plane risks.

### 6. Contact-form abuse, spam, or malicious input

**Threat:** Public form receives spam, phishing, malicious links, sensitive data, or attempts to induce unsafe action.

**Controls:**

- public warning not to submit classified, export-controlled, credential, secret, customer-sensitive, or sensitive operational material;
- Formspree is treated as an untrusted external intake boundary;
- messages are context for human review, not authoritative instructions or automatic authorization;
- no public form submission grants scanning, access, contracting, employment, or operational authority.

**Residual risk:** Third-party form abuse and social engineering remain possible.

### 7. Third-party dependency / outbound-link risk

**Threat:** External services change behavior, become unavailable, track users, or are compromised.

**Controls:**

- core site remains static and functional without JavaScript-heavy third-party application dependencies;
- critical public narrative and intake route remain in repository-controlled pages;
- external links use appropriate `rel` attributes where applicable;
- third-party services are not treated as canonical technical truth.

**Residual risk:** Formspree, Calendly, fonts, social platforms, and publishing platforms remain external dependencies.

### 8. Static-site content tampering / malicious script introduction

**Threat:** Compromised contributor or dependency introduces script, redirect, tracking, credential capture, or deceptive content.

**Controls:**

- source review and Git history;
- site-quality CI;
- minimal static architecture;
- no secrets in client-side code;
- security review for new scripts, forms, embeds, or external dependencies.

**Residual risk:** Current static checks are not a full SAST, CSP, dependency, or browser-security scanner.

### 9. Stale public evidence

**Threat:** Previously accurate capability, role, project status, contact route, or maturity becomes outdated.

**Controls:**

- public claim map;
- repository-local status documents for technical projects;
- Notion governance for current strategic/maturity state;
- periodic public review and explicit date/context where material.

**Residual risk:** Staleness can occur between reviews.

## Security non-goals

This repository does not attempt to:

- publish private threat models for RSC clients or R&D systems;
- serve as a secrets vault;
- authorize testing of any external system;
- prove compliance, certification, clearance, or accreditation;
- replace the security controls of GitHub, DNS providers, Formspree, Calendly, or other external services.

## Change triggers

Re-review this threat model when:

- a new form, script, embed, analytics product, payment path, or authentication layer is added;
- the hosting or domain architecture changes;
- the site begins accepting files or other rich user input;
- a private technical system becomes directly connected to the public site;
- a security incident or sensitive publication occurs;
- RSC/PQExpert routing or identity architecture changes materially.
