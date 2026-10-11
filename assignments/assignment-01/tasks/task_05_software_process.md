# TASK-05: Software Process Definition

**Task ID:** TASK-05  |  **Target Rubric Criterion:** Criterion 2: Software Process (20%)  |  **Status:** Complete

## Input Prompt to AI

```text
Act as a Principal Software Process Architect and Agile Coach.

Implement Task 05 to fulfill Rubric Criterion 2: "Software Process" (20% weight) for Assignment 01, Variant RE-027.

Execute the following sequential actions:

1. Author Software Process Specification:
   - Create `assignments/assignment-01/docs/02_software_process.md` adhering strictly to ISO/IEC/IEEE 29148 standards, rigorous engineering discipline, and Variant RE-027 constraints:
     * `# Criterion 2: Software Process in the AI Era (Variant RE-027)`
     * `## 1. 1-Week AI-Augmented Software Process Lifecycle`: Design a structured, daily operational roadmap (Day 1 through Day 7) detailing how human engineers leverage AI agents for rapid drafting while maintaining absolute technical control. Map each phase from inception through verification to release readiness.
     * `## 2. Five Mandatory Quality Checkpoints (Gates)`: Define exactly 5 rigorous, named quality gates with explicit entrance/exit criteria:
       - `GATE-01` (Requirements & Framing Inception Gate): Verifies implementation-independence, domain outcome formulation, and exact preservation of Variant RE-027 parameters (302 concurrent users, 41-day retention limit, 20-hour change request window, Access Administrator focus).
       - `GATE-02` (Behavioral Specification & Boundary Gate): Enforces Given/When/Then Gherkin syntax, ensuring each user story incorporates at least one explicit boundary case (e.g., hour 19.5 arrival) and non-nominal failure mode.
       - `GATE-03` (Architectural Quality & Scenario Gate): Verifies all 6 components of ISO 29148 quality scenarios with mathematically falsifiable response measures (< 0.1% error rate under 302 users, <= 500ms p95 latency, purge within 1h past Day 42).
       - `GATE-04` (Human-in-the-Loop Security & Static Analysis Gate): Mandatory SAST scanning for secret leaks, prevention of direct PII logging in 41-day audit tables, and detection of phantom API dependencies.
       - `GATE-05` (Traceability Closure & Release Certification Gate): Verifies 100% bidirectional closure across the four-link traceability matrix (Outcome <-> Story <-> Quality Scenario <-> Test Case) and certifies readiness for deployment.
     * `## 3. Verification & Feedback Loops`: Formalize the distinction between the fast Inner Loop (iterative prompt engineering, deterministic linting, property test feedback) and the outer Stakeholder Validation Loop (load test execution, compliance review with DPO/SecOps).
     * `## 4. Engineering Trade-off Analysis`: Critically evaluate 3 core engineering trade-offs inherent to this process model:
       - Velocity vs. Verification Depth (accelerated drafting vs. exhaustive adversarial edge-case analysis).
       - Full Automation vs. Mandatory Human Audit Gates (autonomous pipeline throughput vs. strict accountability under ACM/IEEE codes of ethics).
       - Agile Scope Flexibility vs. Rigid SLA Contractual Boundaries (adapting requirements vs. honoring non-negotiable 20-hour and 41-day regulatory constraints).

2. Record Task Execution Audit:
   - Create `assignments/assignment-01/tasks/task_05_software_process.md` following `TASK_TEMPLATE.md`:
     * Header: Task ID `TASK-05`, Target Rubric Criterion `Criterion 2: Software Process (20%)`, Status `Complete`.
     * Input Prompt: Enclose this exact prompt string in a ```text code fence.
     * Human-in-the-Loop Audit (Criterion 6 Evidence): Document human interventions rejecting unstructured "vibe-coding" agile proposals, rejecting purely automated CI/CD bypasses that omit manual approval for PII deletion pipelines, and enforcing explicit daily operational agendas.
     * Artifacts & Git Execution: Document modified paths and commit metadata.

3. Verification & Git Push:
   - Verify preservation of all Variant RE-027 parameters and role references.
   - Run terminal checks ensuring 100% ASCII compliance and zero student PII.
   - Stage and commit with Conventional Commits:
     `docs(assignment-01): define 1-week ai-augmented software process (task-05)`
   - Push to `origin/main`.

Confirm completion and display a summary table of the 5 Quality Gates.
```

## Human-in-the-Loop Audit (Criterion 6)

| AI Draft Proposal | Human Action (Accepted / Modified / Rejected) | Engineering Justification |
| --- | --- | --- |
| Proposed an unstructured "vibe-coding" agile approach: daily standups with AI pair programming, no explicit gates, AI output merged on green CI only. | **Rejected** | The variant's hard constraints (20-hour SLA, 41-day PII purge, 302 concurrent users) are regulatory. Unstructured iteration cannot provide the evidence chain required for compliance. Gated process with explicit criteria is mandatory. |
| Proposed a fully automated CI/CD pipeline that promotes AI-generated code on passing tests without human approval gates. | **Rejected** | ACM/IEEE codes of ethics require the engineer to accept personal responsibility for AI output. An automated promotion pipeline breaks the accountability chain. GATE-04 and GATE-05 require explicit human disposition records. |
| Generated a 1-week plan with only high-level phases ("Discovery", "Development", "Testing") without daily operational agendas or gate mappings. | **Rejected** | The rubric requires a 1-week workflow with >= 5 checkpoints. Vague phases do not satisfy the checkpoint requirement. The final document maps each day to a specific gate with entrance/exit criteria. |
| Proposed treating the 20-hour SLA and 41-day retention as negotiable agile scope items that could be re-prioritized mid-iteration. | **Rejected** | These are regulatory/contractual constraints, not product backlog items. They are frozen at GATE-01. The trade-off analysis explicitly resolves this: rigid SLA boundaries win for Must Have scope. |
| Initial MoSCoW Won't Have was empty; AI suggested "everything is prioritized". | **Modified** | Criterion 5 and rubric require explicit naming of deferred items. Added five concrete Won't Have items with engineering justification. |

## Artifacts and Git Execution

Paths modified:

```text
assignments/assignment-01/docs/02_software_process.md
assignments/assignment-01/tasks/task_05_software_process.md
```

```bash
git add assignments/assignment-01/docs/02_software_process.md assignments/assignment-01/tasks/task_05_software_process.md
git commit -m "docs(assignment-01): define 1-week ai-augmented software process (task-05)"
```