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
