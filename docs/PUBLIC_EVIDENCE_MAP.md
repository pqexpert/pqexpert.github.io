# PQExpert Public Evidence Map

## Purpose

This map connects the major public claims on PQExpert.io to the type of evidence that must support them. It is a public-safe provenance aid, not a publication of private records.

A public claim should be no stronger than its resolving evidence.

## Evidence states

- **Verified** — resolving evidence exists for the material claim.
- **In Development** — implementation or engineering activity exists, but the promoted outcome is not fully resolved.
- **Research / Concept** — analysis, architecture, hypothesis, experiment, or planned work without enough implementation evidence for a stronger state.
- **Do Not Publish / Blocked** — evidence or work may exist, but privacy, authorization, security, legal, or sensitivity constraints prevent public promotion.

## Current public claim map

| Public claim / surface | Public state | Evidence class | Durable technical / documentary owner | Public limitation |
|---|---|---|---|---|
| GCTI cyber operations and lab modernization | Verified | Institutional / operational records and governed career evidence | Governed evidence records; GitHub only where implementation is legitimately repository-backed | Do not expose institutional secrets, credentials, sensitive infrastructure, or unsupported production detail |
| Syracuse graduate work / degree in progress | Verified | Official academic record and current enrollment evidence | Governed academic evidence; public page contains only resume-safe summary | Degree remains in progress; no unverified completion date or credential award |
| RSC commercial operating context | Verified as entity/context; services maturity varies | Company records plus scoped technical evidence | RSC / private governed repositories for technical work; governed business records for entity facts | Do not infer current customers, contract awards, deployments, or partnerships without evidence |
| Dynamic Threat Model (DTM) | In Development | Private repository, product-scope docs, agent governance, future implementation/tests | `pqexpert/DTM` | Repository existence does not imply production deployment or customer use |
| CART / continuous validation | In Development | Private repository, authorization-first architecture/design, implementation scaffold | `pqexpert/CART` | Not a production autonomous red-team platform; explicit authorization required |
| Post-Quantum Core / readiness | In Development | Private repository, readiness architecture/design, future inventory/experiment evidence | `pqexpert/pqc` | No claim of post-quantum security, certification, or production cryptographic replacement without exact evidence |
| Golden ISO | In Development | Private repository, provenance/reproducibility architecture, future build/test artifacts | `pqexpert/golden-iso-project` | No accreditation, compliance, ATO, mission approval, or production-hardening claim without evidence |
| Secure Connect | In Development | Private repository, source/config/tests/security docs | `pqexpert/secure-connect.us` | Secure-access experiment; no blanket Zero Trust, compliance, or post-quantum-security claim |
| PT toolkit | In Development / Private | Private implementation, mock/dry-run behavior, authorization governance | `pqexpert/pt` | Authorized security testing only; no public target/finding/credential detail |
| RSC Operations Console | In Development / Operator Layer | Private repository, operator interface, command/verification documentation | `Restoration-MT/rsc-operations-console` | Derived operator surface; dashboard visibility does not make data canonical or fresh by itself |
| BridgeGHL | In Development / Controlled Integration | Private repository, dry-run/execute/audit implementation | `Fungible-MT-LLC/BridgeGHL` | External-write bridge; public client routing still starts on PQExpert |
| Private Integration Orchestrator | In Development / Integration Hub | Private repository, integration contracts, topology, propagation docs | Private governed repository | Hub/orchestrator role does not imply every portfolio product is integrated end-to-end |
| Local Fabric | In Development | Reviewed source, native DNS/recovery/binding/schedule receipts; public-safe cutover summary | `Fungible-MT-LLC/BridgeGHL` and each mission owner | Component checks do not establish unattended mission completion, full network protection or restore acceptance; see [cutovers](PUBLIC_SYSTEM_ARCHITECTURE.md#verified-component-cutovers) |
| Accepted Local Fabric subset — November 2026 | Verified bounded operations | Reviewed implementation, native App publication/review, local triage receipt, and encrypted recovery download/decryption verification | Private governed implementation and operating records; public summary at `/provenance.html#autonomous-operations` | Accepted local inference/retrieval, scoped source publication, private routing and verified recovery; broader mission completion, CoOS production, saturation and 24/7 availability remain unproven |
| CoOS | Research / Concept | Constitutional cooperation architecture and promotion boundary | `pqexpert/FungibleRD-MVP` | Research readiness is not production promotion; no independent human identity or self-approval authority |
| Public writing / policy analysis | Verified per published artifact | Published article / paper / brief and cited sources | Published surface plus governed source material | Publication demonstrates analysis, not institutional endorsement or operational deployment |

## Claim promotion checklist

Before changing a public maturity state or adding a material claim, confirm:

1. What exact sentence are we trying to support?
2. What evidence resolves that sentence?
3. Does the evidence describe the same environment, time period, scope, and maturity?
4. Is the evidence public-safe to summarize?
5. Does publication create client, privacy, security, legal, academic, or relationship risk?
6. Is a limitation or uncertainty statement required?
7. Does the repository / artifact actually exist in the state being claimed?
8. Has the public page and provenance map been updated together?

## Evidence does not automatically equal publication

Some facts should remain private even when strongly verified. Evidence strength and publication authorization are separate decisions.

Examples include:

- client-specific findings;
- credentials and secrets;
- protected identity information;
- sensitive infrastructure;
- clearance-related material;
- classified or export-controlled information;
- unpublished research that creates operational risk;
- private relationship or health information.

## Public routing rule

Evidence helps a reader decide whether to start a conversation. It does not require the reader to navigate the private technical estate or a second RSC website.

The external path remains:

`PQExpert -> evidence / fit -> contact -> scope -> appropriate operating context`
