# TASK-02: User Stories and Acceptance Criteria

**Task ID:** TASK-02  |  **Target Rubric Criterion:** Criterion 4: User Stories and Acceptance Criteria (20%)  |  **Status:** Complete

## Input Prompt to AI

```text
Act as a Principal Requirements Engineer.

Implement Task 02 to fulfill Rubric Criterion 4: "User Stories and Acceptance Criteria" (20% weight) for Assignment 01, Variant RE-027.

Execute the following sequential actions:

1. Author User Stories Document:
   - Create `assignments/assignment-01/docs/04_user_stories.md` strictly aligned with ISO/IEC/IEEE 29148 standards and implementation independence:
     * `# Criterion 4: User Stories and Acceptance Criteria (Variant RE-027)`
     * `## 1. Traceability & Story Derivation`: Briefly summarize how the 4 stories originate directly from OUTCOME-01, OUTCOME-02, OUTCOME-03, and the stakeholder conflict matrix defined in `03_problem_framing.md`.
     * `## 2. Core User Stories & Gherkin Acceptance Criteria`: Formulate exactly 4 core user stories using the standard format ("As an <actor>, I want <capability>, so that <benefit>"). Each story must feature at least 2 distinct Gherkin scenarios (`Given - When - Then`), including at least ONE explicit Failure / Boundary Case:
       - `US-01` (Trace: OUTCOME-01): Access Administrator bulk processing of personal data deletion requests within the <= 20-hour window. (Boundary/Failure: Request received at hour 19.5 with pending active dependencies).
       - `US-02` (Trace: OUTCOME-02): SecOps / Auditor access to pseudonymized audit records adhering to the strict 41-day retention limit without exposing direct PII. (Boundary/Failure: Expired record retention at day 42 purging verification).
       - `US-03` (Trace: OUTCOME-03): Access Administrator revoking access privileges of a target user without impacting session stability (< 0.1% error rate) of the 302 concurrent active users. (Boundary/Failure: Race condition during concurrent privilege re-evaluation under peak load).
       - `US-04` (Trace: OUTCOME-01, CONFLICT-02): Access Administrator automated SLA escalation when a personal data deletion request nears the 20-hour deadline. (Boundary/Failure: Disconnected notification channel or queue congestion).
     * `## 3. Implementation Independence Affirmation`: Explicitly certify that all user stories and acceptance criteria omit technical implementation choices (no HTTP status codes, SQL tables, REST endpoints, or specific UI frameworks).

2. Record Task Execution Audit:
   - Create `assignments/assignment-01/tasks/task_02_user_stories.md` strictly following `TASK_TEMPLATE.md`:
     * Header: Task ID `TASK-02`, Target Rubric Criterion `Criterion 4: User Stories and Acceptance Criteria (20%)`, Status `Complete`.
     * Input Prompt: Enclose this exact prompt string in a ```text code fence.
     * Human-in-the-Loop Audit (Criterion 6 Evidence): Document human intervention rejecting implementation-coupled drafts (e.g., rejecting acceptance criteria specifying HTTP 204/409 codes and database rollback mechanisms in favor of business-observable domain states).
     * Artifacts & Git Execution: Document modified paths and commit metadata.

3. Verification & Git Push:
   - Verify that all Variant RE-027 parameters (Access Administrator, Personal-Data-Deletion-on-Request, 302 users, 41 days, 20 hours) are preserved.
   - Run terminal checks ensuring 100% ASCII compliance and zero literal student PII.
   - Stage and commit with Conventional Commits:
     `docs(assignment-01): specify 4 core user stories and gherkin criteria (task-02)`
   - Push to `origin/main`.

Confirm completion and display a summary of the 4 user stories with their boundary cases.
```

## Human-in-the-Loop Audit (Criterion 6)

| AI Draft Proposal | Human Action (Accepted / Modified / Rejected) | Engineering Justification |
| --- | --- | --- |
| Acceptance criteria for US-01 specified HTTP 202 Accepted for batch submission, HTTP 204 No Content for completion, and HTTP 409 Conflict for dependency deadlock. | **Rejected** | HTTP status codes are implementation coupling to a REST transport layer. Criteria must express domain-observable states (request accepted, fulfilled, conflicted) independent of transport protocol. |
| Acceptance criteria for US-02 referenced a database `audit_log` table with `surrogate_key` column and a `DELETE FROM audit_log WHERE age > 41 DAYS` rollback mechanism. | **Rejected** | Database schema and DML operations are implementation details. The requirement is observable record availability and purge behavior, not the storage mechanism. |
| Acceptance criteria for US-03 included a circuit-breaker pattern with Hystrix fallback and a 500ms p99 latency budget for the revocation API call. | **Rejected** | Specific resilience libraries and latency budgets at the API layer couple the story to a microservice architecture. The criterion is session stability and error rate under load, observable at the user level. |
| Acceptance criteria for US-04 used a cron expression `0 */6 * * *` for the escalation check and named a specific message queue (RabbitMQ) for the fallback channel. | **Rejected** | Scheduling syntax and message broker selection are infrastructure decisions. The requirement is time-based escalation and channel fallback behavior, observable without committing to infrastructure. |
| Framed the 20-hour window as a simple SLA target without distinguishing nominal vs escalation thresholds. | **Modified** | Introduced explicit 16-hour and 18-hour escalation thresholds in AC-04.1 and AC-04.2 to make the boundary conditions testable and the SLA safeguard verifiable. |

## Artifacts and Git Execution

Paths modified:

```text
assignments/assignment-01/docs/04_user_stories.md
assignments/assignment-01/tasks/task_02_user_stories.md
```

```bash
git add assignments/assignment-01/docs/04_user_stories.md assignments/assignment-01/tasks/task_02_user_stories.md
git commit -m "docs(assignment-01): specify 4 core user stories and gherkin criteria (task-02)"
```