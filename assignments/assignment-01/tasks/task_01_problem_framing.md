# TASK-01: Problem Framing and Product Thinking

**Task ID:** TASK-01  |  **Target Rubric Criterion:** Criterion 3: Problem Framing and Product Thinking (20%)  |  **Status:** Complete

## Input Prompt to AI

```text
Act as a Principal Requirements Engineer and Product Architect.

Implement Task 01 to fulfill Rubric Criterion 3: "Problem Framing and Product Thinking" (20% weight) for Assignment 01, Variant RE-027.

Execute the following actions:

1. Author Core Problem Framing Document:
   - Create directory `assignments/assignment-01/docs/` if not already present.
   - Author `assignments/assignment-01/docs/03_problem_framing.md` adhering strictly to ISO/IEC/IEEE 29148 and implementation-independent problem framing:
     * `# Criterion 3: Problem Framing and Product Thinking (Variant RE-027)`
     * `## 1. Operational Problem Statement`: Articulate the operational dilemma of the Access Administrator facing the Personal-Data-Deletion-on-Request policy while managing 302 concurrent active users, a 41-day audit retention limit, and a 20-hour change request response window. Strictly avoid any implementation bias (no mentioning specific tech stacks, databases, or frameworks).
     * `## 2. Measurable Operational Outcomes`: Define 3 concrete, quantitative outcome targets labeled with IDs:
       - `OUTCOME-01`: 100% of data-deletion and access-revocation requests fulfilled within the <= 20-hour response window.
       - `OUTCOME-02`: 100% compliance with the 41-day audit retention limit with zero exposure of residual direct personal identifiers (via irreversible tokenization/pseudonymization).
       - `OUTCOME-03`: System maintains concurrent session error rates < 0.1% under peak baseline load of 302 concurrent active users during access policy re-evaluations.
     * `## 3. Stakeholder Analysis and Conflict Matrix`: Map at least 4 distinct stakeholder parties:
       1. Access Administrator (Focus stakeholder)
       2. Data Subject / End User
       3. Security Operations (SecOps) & Compliance Auditor
       4. Data Protection Officer (DPO) / Legal Counsel
       Detail their role, core operational need, and explicit conflict/tension points with other parties (especially the tension between the 41-day audit retention requirement and complete personal data deletion).
     * `## 4. Unverified Candidate Assumptions (ISO 29148)`: Enumerate 3 critical candidate assumptions requiring external validation (the continuous clock vs business hour definition of the 20-hour window, the legal boundary between personal profiles and audit log entries, and the peak-load transaction profile across 302 concurrent users).

2. Record Task Execution Audit:
   - Create `assignments/assignment-01/tasks/task_01_problem_framing.md` using the streamlined `TASK_TEMPLATE.md` structure:
     * Header: Task ID `TASK-01`, Target Rubric Criterion `Criterion 3: Problem Framing and Product Thinking (20%)`, Status `Complete`.
     * Input Prompt: Enclose this exact prompt inside a ```text code fence.
     * Human-in-the-Loop Audit (Criterion 6 Evidence): Include an audit table documenting the rejection of technical implementation coupling (e.g., rejecting an AI draft proposing SQL triggers and OAuth tokens in favor of domain-level operational requirements, and enforcing explicit conflict modeling between SecOps 41-day retention and DPO deletion).
     * Artifacts & Git Execution: Document modified paths and commit metadata.

3. Integrity Verification & Git Push:
   - Verify that all RE-027 parameters (Access Administrator, Personal-Data-Deletion-on-Request, 302 users, 41 days, 20 hours) are preserved verbatim.
   - Run a terminal sweep ensuring 0 literal student PII and 100% ASCII compliance.
   - Stage, commit with Conventional Commits:
     `docs(assignment-01): formulate problem framing and stakeholder analysis (task-01)`
   - Push to `origin/main`.

Confirm completion and display the table of contents for `03_problem_framing.md`.
```

## Human-in-the-Loop Audit (Criterion 6)

| AI Draft Proposal | Human Action (Accepted / Modified / Rejected) | Engineering Justification |
| --- | --- | --- |
| Proposed SQL triggers, database-level cascading deletes, and OAuth token revocation flows as the implementation mechanism for deletion. | **Rejected** | Problem framing must remain implementation-agnostic per ISO/IEC/IEEE 29148. Coupling to specific database features and auth protocols pre-commits the solution and violates the "no technology names" constraint. |
| Presented SecOps 41-day retention and DPO deletion as a single combined requirement without explicit conflict modeling. | **Rejected** | The tension between audit traceability and identifier removal is the central architectural conflict of this variant. Masking it as one requirement obscures the design trade-off and weakens evidence for Criterion 3. |
| Framed the 20-hour window as a simple SLA target without qualifying continuous vs business-hour interpretation. | **Modified** | Added ASSUMPTION-01 to capture the clock-model ambiguity as an unverified candidate assumption requiring legal/policy validation. |

## Artifacts and Git Execution

Paths modified:

```text
assignments/assignment-01/docs/03_problem_framing.md
assignments/assignment-01/tasks/task_01_problem_framing.md
```

```bash
git add assignments/assignment-01/docs/03_problem_framing.md assignments/assignment-01/tasks/task_01_problem_framing.md
git commit -m "docs(assignment-01): formulate problem framing and stakeholder analysis (task-01)"
```