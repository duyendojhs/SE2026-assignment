# Criterion 4: User Stories and Acceptance Criteria (Variant RE-027)

## 1. Traceability and Story Derivation

The four core user stories below are derived directly from the measurable operational outcomes and
stakeholder conflict matrix established in `03_problem_framing.md`:

| Story ID | Primary Outcome Trace | Secondary Trace | Rationale |
| --- | --- | --- | --- |
| **US-01** | OUTCOME-01 | CONFLICT-02 | The Access Administrator must process deletion requests within the 20-hour window; this story captures the bulk processing workflow under load. |
| **US-02** | OUTCOME-02 | CONFLICT-01 | SecOps and Auditors require audit records for 41 days while the DPO requires zero direct PII exposure; this story captures pseudonymized access under retention limits. |
| **US-03** | OUTCOME-03 | CONFLICT-03 | The Access Administrator must revoke access without destabilizing 302 concurrent sessions; this story captures the race-condition boundary under peak load. |
| **US-04** | OUTCOME-01 | CONFLICT-02 | When a deletion request nears the 20-hour deadline, automated escalation ensures the window is not breached; this story captures the SLA safeguard. |

No additional stories are introduced; every story maps to at least one outcome or conflict.

---

## 2. Core User Stories and Gherkin Acceptance Criteria

### US-01: Bulk Processing of Personal Data Deletion Requests

**As an** Access Administrator, **I want** to process incoming personal data deletion requests in
bulk, **so that** all requests are fulfilled within the <= 20-hour response window even under
concurrent load.

#### Acceptance Criteria

| Scenario | Given | When | Then |
| --- | --- | --- | --- |
| **AC-01.1 (Nominal)** | A batch of deletion requests has been queued, each associated with a distinct data subject, and the current elapsed time since the oldest request is less than 10 hours | The Access Administrator initiates the bulk deletion workflow | All requests in the batch are marked fulfilled, each data subject's direct identifiers are irreversibly tokenized across the system, and a fulfillment confirmation is recorded for every request |
| **AC-01.2 (Boundary -- Late-Arrival with Dependencies)** | A deletion request arrives at hour 19.5 of the 20-hour window, and the target data subject has active session dependencies that prevent immediate tokenization | The Access Administrator triggers the bulk workflow including this late request | The request is flagged for expedited handling, dependent sessions are gracefully terminated or transferred, tokenization completes before the 20-hour deadline, and the confirmation records the escalation path taken |
| **AC-01.3 (Failure -- Window Exceeded)** | A deletion request has aged past 20 hours without fulfillment due to an unhandled dependency deadlock | The system evaluates request age | The request is marked as SLA breach, an escalation alert is emitted to the Access Administrator and DPO, and the breach record includes the root-cause category |

---

### US-02: Pseudonymized Audit Record Access Under Retention Limit

**As a** SecOps Analyst or Compliance Auditor, **I want** to query pseudonymized audit records
spanning up to 41 days, **so that** forensic investigations retain full event traceability without
exposing direct personal identifiers.

#### Acceptance Criteria

| Scenario | Given | When | Then |
| --- | --- | --- | --- |
| **AC-02.1 (Nominal)** | The audit store contains pseudonymized records aged between 1 and 41 days, each linked to a stable surrogate key that replaces the original personal identifier | The SecOps Analyst queries the audit store for events within a specified time range | The query returns complete event records with surrogate keys, zero direct personal identifiers appear in the result set, and the response includes the age of each record relative to the 41-day limit |
| **AC-02.2 (Boundary -- Retention Expiry at Day 42)** | Pseudonymized audit records exist for day 41 and day 42 after their originating event | The retention enforcement process executes at the 41-day boundary | Records aged exactly 41 days remain retrievable; records aged 42 days are purged from the audit store; the purge operation is logged with the surrogate keys of removed records; no direct personal identifiers are exposed during purge |
| **AC-02.3 (Failure -- Re-identification Attempt)** | A query is constructed that attempts to join pseudonymized audit records with an external data source containing direct personal identifiers | The SecOps Analyst executes the join query | The system rejects the query or returns a result set that suppresses the join columns containing direct identifiers, and an audit event is recorded noting the attempted re-identification pattern |

---

### US-03: Access Revocation Under Peak Concurrent Load

**As an** Access Administrator, **I want** to revoke the access privileges of a target user
immediately, **so that** the revocation takes effect without degrading session stability for the
302 concurrent active users (error rate < 0.1%).

#### Acceptance Criteria

| Scenario | Given | When | Then |
| --- | --- | --- | --- |
| **AC-03.1 (Nominal)** | The system is operating at 302 concurrent active users with a measured session error rate below 0.01% | The Access Administrator issues a revocation directive for a single target user | The target user's active sessions are terminated within 30 seconds, all other concurrent sessions continue without interruption, and the post-revocation error rate remains below 0.1% |
| **AC-03.2 (Boundary -- Race Condition During Re-evaluation)** | The system is at peak load (302 concurrent users), and a policy re-evaluation cycle is in progress when a revocation directive is issued for a user with multiple active sessions across different repositories | The Access Administrator issues the revocation directive concurrently with the policy re-evaluation | The revocation takes effect atomically for the target user across all repositories; no other user's session experiences an authorization error; the re-evaluation cycle completes with consistent policy state; total elapsed time for the combined operation does not exceed the 20-hour window |
| **AC-03.3 (Failure -- Cascade Failure Under Load)** | The system is at peak load, and a revocation triggers an unexpected policy propagation failure that affects unrelated users | The Access Administrator issues the revocation directive | The system isolates the failure to the target user's sessions, other users' sessions remain stable, the error rate for non-target users stays below 0.1%, and a failure report is generated identifying the propagation path that caused the cascade |

---

### US-04: Automated SLA Escalation for Near-Deadline Deletion Requests

**As an** Access Administrator, **I want** automated escalation when a personal data deletion
request approaches the 20-hour response deadline, **so that** no request breaches the SLA due to
queue congestion or notification failure.

#### Acceptance Criteria

| Scenario | Given | When | Then |
| --- | --- | --- | --- |
| **AC-04.1 (Nominal)** | A deletion request has been in the queue for 16 hours without fulfillment | The 16-hour mark is reached | An automated escalation alert is sent to the Access Administrator and the DPO, the request priority is elevated in the processing queue, and the escalation event is logged with a timestamp |
| **AC-04.2 (Boundary -- Notification Channel Disconnected)** | A deletion request reaches the 18-hour mark, and the primary notification channel (e.g., messaging, email) is unavailable | The escalation trigger fires | The system falls back to a secondary notification channel, logs the channel failure, retries the primary channel at 5-minute intervals, and the escalation alert is delivered via the secondary channel within 15 minutes |
| **AC-04.3 (Failure -- Queue Congestion Blocking Escalation)** | The processing queue is congested such that the escalation task itself cannot be enqueued within the monitoring interval | The 16-hour or 18-hour escalation threshold is reached | A critical alert is emitted directly to the Access Administrator's dashboard bypassing the queue, the queue congestion condition is logged as a system health incident, and the deletion request is marked for manual intervention with full audit trail |

---

## 3. Implementation Independence Affirmation

All user stories and acceptance criteria above are expressed strictly in terms of:

- **Actors and roles** (Access Administrator, SecOps Analyst, Compliance Auditor, Data Subject)
- **Observable domain states** (request queued, fulfilled, flagged, escalated; records pseudonymized, purged, retrievable; sessions terminated, stable, error rate measured)
- **Quantitative operational boundaries** (20-hour window, 41-day retention, 302 concurrent users, 0.1% error rate, 16-hour / 18-hour escalation thresholds)

No story or criterion references:

- HTTP status codes, REST endpoints, or API contracts
- Database schemas, tables, triggers, or rollback mechanisms
- Specific authentication protocols (OAuth, SAML, JWT)
- UI frameworks, client libraries, or frontend technologies
- Programming languages, runtimes, or infrastructure platforms
- Internal data structures, serialization formats, or message queue topologies

The stories describe **what** the system must achieve and **under what observable conditions**, not
**how** any component is implemented. This satisfies the implementation-independence requirement of
ISO/IEC/IEEE 29148 and the "no technology names" constraint of the variant.