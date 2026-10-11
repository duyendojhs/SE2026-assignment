# Criterion 3: Problem Framing and Product Thinking (Variant RE-027)

## 1. Operational Problem Statement

The Access Administrator is accountable for governing access rights within a shared GitHub project
environment used by student teams. During active development, a Personal-Data-Deletion-on-Request
policy is introduced, mandating that personal data be deleted upon request by the data subject.
This policy creates an operational dilemma: the Access Administrator must simultaneously honor
deletion requests, maintain an auditable trail for security and compliance purposes, and sustain
operational continuity for up to 302 concurrent active users.

The environment operates under three hard constraints:

- **Concurrency ceiling**: 302 concurrent active users generating access requests and session
  activity.
- **Audit retention ceiling**: Personal data and access events must remain retrievable for 41 days
  to satisfy audit obligations.
- **Policy response ceiling**: Any change request, including a deletion request, must receive a
  response within 20 hours.

The core problem is to establish an operational model that satisfies the deletion policy without
invalidating the audit retention requirement or exceeding the response window, while preserving
system stability under peak load. The solution must be defined in terms of operational outcomes,
not implementation mechanisms.

---

## 2. Measurable Operational Outcomes

| Outcome ID | Description |
| --- | --- |
| **OUTCOME-01** | 100% of data-deletion and access-revocation requests fulfilled within the <= 20-hour response window. |
| **OUTCOME-02** | 100% compliance with the 41-day audit retention limit with zero exposure of residual direct personal identifiers (achieved via irreversible tokenization or pseudonymization). |
| **OUTCOME-03** | System maintains concurrent session error rates < 0.1% under peak baseline load of 302 concurrent active users during access policy re-evaluations. |

Each outcome is expressed as a verifiable operational target. Implementation choices -- data stores,
orchestration mechanisms, tokenization algorithms -- are intentionally excluded.

---

## 3. Stakeholder Analysis and Conflict Matrix

| Stakeholder | Role | Core Operational Need |
| --- | --- | --- |
| **Access Administrator** (Focus) | Accountable for access rights governance across the shared repository. | Authoritative, timely execution of access grants, revocations, and deletion directives without service disruption. |
| **Data Subject / End User** | Individual whose personal data is processed within the system. | Right to request deletion of their personal data and receive confirmation within the mandated window. |
| **Security Operations (SecOps) & Compliance Auditor** | Responsible for monitoring, detection, and audit trail integrity. | Continuous, tamper-evident access logs retaining sufficient context for forensic investigation for the full 41-day period. |
| **Data Protection Officer (DPO) / Legal Counsel** | Accountable for regulatory compliance with data protection law. | Demonstrable adherence to deletion obligations; no personal identifiers retained beyond what the law permits. |

### Explicit Conflict Points

| Conflict ID | Parties | Tension Description |
| --- | --- | --- |
| **CONFLICT-01** | SecOps & Compliance Auditor vs. DPO / Legal Counsel | The 41-day audit retention requirement demands that access events remain attributable to identifiable actors. The deletion policy demands removal of direct personal identifiers. These obligations are mutually exclusive unless an irreversible transformation (tokenization/pseudonymization) is applied that satisfies both audit linkage and identifier removal. |
| **CONFLICT-02** | Access Administrator vs. Data Subject | The Access Administrator must process deletion requests within 20 hours while concurrently managing 302 active sessions. A synchronous, per-request deletion workflow may exceed the window under load, forcing a queuing or batch model that introduces latency risk. |
| **CONFLICT-03** | SecOps & Compliance Auditor vs. Access Administrator | The Access Administrator needs operational flexibility to revoke access instantly. SecOps requires that every revocation be logged with full context before the action takes effect, potentially adding latency that threatens the 20-hour window. |

---

## 4. Unverified Candidate Assumptions (ISO 29148)

Per ISO/IEC/IEEE 29148, the following candidate assumptions are recorded. Each must be validated
with the appropriate authority before it constrains the solution. None is accepted as a baseline.

| Assumption ID | Statement | Validation Required From |
| --- | --- | --- |
| **ASSUMPTION-01** | The 20-hour response window is measured in continuous elapsed hours (calendar clock), not business hours. | Policy owner / Legal Counsel |
| **ASSUMPTION-02** | Audit log entries are legally distinct from personal profiles; tokenized references in logs do not constitute personal data under the applicable regulation. | DPO / Legal Counsel |
| **ASSUMPTION-03** | The peak-load transaction profile across 302 concurrent users follows a read-heavy access-check pattern with bursty write spikes during policy re-evaluation, rather than uniform write load. | Platform operations / SecOps |

These assumptions directly affect the operational feasibility of OUTCOME-01 through OUTCOME-03. If
ASSUMPTION-01 is false (business hours only), the effective window compresses dramatically. If
ASSUMPTION-02 is false, tokenization alone does not satisfy deletion, requiring a different
architectural approach. If ASSUMPTION-03 is false, capacity planning for OUTCOME-03 must be
re-derived from a different load model.