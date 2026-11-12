# PQExpert Public System Architecture

## Purpose

This document explains the external-facing operating model behind PQExpert without exposing private governance, client, identity, credential, or security material.

The architecture separates **governance**, **durable engineering/documentation**, **public projection**, and **commercial delivery** so each layer has a clear job.

## Canonical roles

| Layer | Canonical role | What belongs here | What does not belong here |
|---|---|---|---|
| Notion | Governance and control | Strategic state, decisions, maturity, approval boundaries, priorities, cross-system governance | Repository-local implementation truth, secrets, production code |
| GitHub | Durable engineering and documentation | Code, architecture, runbooks, tests, provenance, implementation evidence, recovery knowledge, repo-local technical truth | Private governance that has no engineering use, unsupported public claims |
| PQExpert.io | Public projection and intake | Capabilities, evidence, writing, public-safe project maturity, verification, client/professional routing | Secrets, private identity, client data, internal control-plane detail |
| RSC | Commercial operating context | Contracting/delivery/business-development context when a scoped engagement requires it | The default public website that readers must navigate before contacting the work |

## Client path

The intended public route is deliberately short:

`PQExpert -> evidence / fit -> contact -> scope -> RSC or other appropriate operating context -> delivery`

A reader should not have to understand entity architecture before deciding whether the work is relevant.

## Technical path

The intended technical route is:

`governed decision -> repository-local implementation/docs -> tests / verification -> public-safe projection if appropriate`

A dashboard, builder, agent, or public site should never become the only durable location for an implementation-critical fact.

## Public/private boundary

Public pages may describe:

- verified operational experience;
- public-safe tools and methods;
- public-safe project categories;
- maturity state;
- limitations;
- engagement routes;
- public writing and research;
- the relationship between PQExpert and RSC.

Public pages should not expose:

- credentials, secrets, tokens, private infrastructure details;
- protected legal/identity material that is not required for public review;
- client or customer confidential information;
- clearance-related material;
- private spiritual-practice or health information;
- unpublished sensitive research;
- internal attack paths, target data, or operationally sensitive security details.

## Maturity model

- **Verified**: resolving evidence supports the public claim.
- **In Development**: implementation exists or is actively progressing, but the promoted outcome is not yet fully resolved.
- **Research / Concept**: analysis, architecture, hypothesis, experiment, or planned work without enough implementation evidence for a stronger state.
- **Not Public / Blocked**: work exists but authorization, security, privacy, maturity, or evidence conditions prevent public promotion.

## Documentation rule

When a system matters to continuity, verification, security, automation, or delivery, its important technical knowledge should be recoverable from GitHub without relying on a chat transcript or one operator's memory.

The private hub repository maintains the detailed cross-repository estate map and documentation standard. This public repository carries only the external-safe projection.


## Local operation and CoOS — 2026-11-11

The operating direction is a persistent local environment that can perform admitted work without an active cloud chat session. Local inference, private networking, versioned implementations and durable evidence support that direction. They do not, individually, prove unattended mission completion.

CoOS is the constitutional cooperation research program: people, agents and organizations coordinate through explicit capability, authority, resource and evidence boundaries. Its current source classification remains Research / Concept. Production promotion requires a named owner, exact source, bounded effects, negative tests, recovery and native outcome evidence. Research readiness and operational acceptance are different claims.

The existing Fabric has four mission lanes: income, RSC operations, assigned store operations and evidence synthesis. Coordination transports requests; domain owners retain authority. Store information and client records remain compartmented. Public documentation does not imply endorsement by an organization served by an actor.

Where automation uses the label **Josh Allen — managed operational agent**, it denotes bounded automated assistance. It is not a separate human, an independent moral agent or authority to sign, contact people, spend money or approve its own work. Public communication must identify the actual sender and preserve human decision rights.

### Network design

| Layer | Intended control | Evidence required |
| --- | --- | --- |
| Public sites and intake | Existing public DNS and authenticated application edges | Domain ownership, valid TLS, consent-aware intake and receipt |
| Private devices | Encrypted overlay, explicit admission and signed device identity | Authorized membership and positive/negative access tests |
| Private services | Defined service route, minimum callers and application authentication | Listener/firewall/access-policy readback |
| DNS | One resolver configuration owner per host; explicit upstream policy | System, browser, container, IPv4 and IPv6 tests |
| Security observation | Endpoint/network events with bounded response | Indexed alert plus verified containment and reversal |
| Autonomous work | Per-mission authority and durable receipts | Useful native result, replay protection and downstream consumption |

DNS or DHCP denial alone does not prevent access by direct address. An encrypted network does not replace host controls or application authorization. Actors sharing a host require process and credential separation; multiple names do not create isolation.

### Cutover record

The November 11 engineering inspection observed active local chat/model services, signed private-network membership, private service mappings and successful CRM bridge readback. It also found resolver ownership contention and a failed recovery upload. These are dated component observations, not a full security assessment or proof of complete autonomous operation.

Subsequent November 11 checks verified DNS ownership repair, a fresh encrypted recovery upload, Google account/resource validation and native Calendar scheduling. These close specific component faults. The remaining acceptance steps are controlled resolver egress, explicit service grants, indexed denial/response evidence, a recovery restore rehearsal and useful local mission cycles. Public status remains **In Development** until the relevant evidence exists. No blanket “fully secure,” “fully autonomous,” compliance certification or customer-adoption claim is made.

Public release notes should record what changed, the exact reviewed version, tests, observed outcome, limitations and rollback. Sensitive topology, credentials, customer data and private human context remain outside public documentation.

### Deployment ownership

GitHub Pages owns this public website. Automatic Vercel Git deployments are disabled in `vercel.json`; retained Vercel resources are not production authority. Reversing that setting requires an explicit hosting decision and verified domain/callback ownership.

### Verified component cutovers

| Component | Accepted outcome | Remaining evidence |
| --- | --- | --- |
| System DNS | Resolver ownership repaired; public/private resolution and IPv4/IPv6 exit routing sampled successfully | Reconnect/reboot continuity and application/container DNS bypass tests |
| Recovery | Fresh encrypted upload verified at the recovery receiver | Restore rehearsal and continued retention checks |
| Google consumers | Account, Calendar ownership, Drive scope/folder access and isolated runtime binding readback verified | Useful consumer work and downstream result acceptance |
| Native Calendar | Sole native writer enabled; existing six daily slots and paused hosted predecessor verified | Reliable provider connectivity, native write readback when a legitimate note is due, and feedback backlog consumption |

These are component acceptance records, not a blanket security or autonomous-operation certification. Public documentation is deliberately separate from private operational receipts.
