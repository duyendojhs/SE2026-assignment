# Criterion 2: Software Process in the AI Era (Variant RE-027)

## 1. One-Week AI-Augmented Software Process Lifecycle

This process model integrates AI-assisted drafting within a rigorously gated, human-accountable
engineering discipline. Every AI-generated artifact passes through explicit verification gates
before it can advance. The week is structured as a single iteration from inception to release
readiness, matching the variant's 20-hour change-request window and the assignment's one-week
workflow requirement.

| Day | Phase | Human Engineering Activity | AI-Assisted Activity | Gate Target |
| --- | --- | --- | --- | --- |
| **Day 1** | Inception & Framing | Define operational problem, stakeholder map, and measurable outcomes; validate Variant RE-027 parameters are preserved verbatim | Draft problem statement, outcome candidates, stakeholder matrix from structured prompt | GATE-01 |
| **Day 2** | Behavioral Specification | Author 4 user stories with Gherkin acceptance criteria; ensure each has >= 1 boundary/failure case; verify traceability to outcomes | Generate initial story drafts and Gherkin scenarios from outcome specifications | GATE-02 |
| **Day 3** | Quality Scenario Engineering | Formulate 3 six-part ISO 29148 quality scenarios with mathematical response measures; establish MoSCoW scope | Draft scenario components and MoSCoW table from outcome and constraint inputs | GATE-03 |
| **Day 4** | Architecture & Risk Analysis | Define system boundaries, data flows, and threat model for PII deletion; identify AI failure mode mitigations | Generate architectural decision records and risk register from constraints | -- |
| **Day 5** | Implementation Planning & Static Verification | Plan implementation tasks, define CI pipeline stages, configure deterministic linters and SAST rules for PII protection | Generate task breakdown, CI configuration, and lint rule sets from architecture | GATE-04 |
| **Day 6** | Traceability Closure & Test Specification | Complete bidirectional traceability matrix; specify planned test cases (TC-PERF-01, TC-PRIV-01, TC-SLA-01, TC-CONCUR-01) with pass thresholds | Generate traceability links and test case templates from prior artifacts | GATE-05 |
| **Day 7** | Release Certification & Audit Compilation | Execute all gate verifications; compile AI usage appendix with dispositions; verify PII absence and ASCII compliance; certify release | Assemble audit trail, generate summary tables, verify formatting compliance | GATE-05 (final) |

**AI Role Discipline.** The AI is a drafting accelerator, never a decision authority. Every AI
output is treated as an unverified candidate. The human engineer specifies the intent, reviews
the draft, records the disposition (Accepted / Modified / Rejected) with engineering
justification, and only then commits the artifact. No AI output bypasses a gate.

---

## 2. Five Mandatory Quality Checkpoints (Gates)

Each gate has explicit entrance criteria (what must be complete before review) and exit criteria
(what must be true to pass). Gates are sequential; failure at any gate blocks progression.

### GATE-01: Requirements & Framing Inception Gate

| Aspect | Specification |
| --- | --- |
| **Entrance Criteria** | Operational problem statement drafted; stakeholder map with >= 4 parties; 3 measurable outcomes (OUTCOME-01, 02, 03) defined; conflict matrix with >= 3 conflicts; 3 unverified candidate assumptions recorded |
| **Exit Criteria** | Problem statement contains zero technology names; outcomes are quantitative and falsifiable; Variant RE-027 parameters (Access Administrator, Personal-Data-Deletion-on-Request, 302 users, 41-day retention, 20-hour window) preserved verbatim in all artifacts; all assumptions marked as unverified candidates per ISO 29148 |
| **Verification Method** | Human review against checklist; automated grep for variant parameters; ASCII compliance check |

### GATE-02: Behavioral Specification & Boundary Gate

| Aspect | Specification |
| --- | --- |
| **Entrance Criteria** | 4 user stories drafted in standard format (As an <actor>, I want <capability>, so that <benefit>); each story linked to at least one outcome or conflict |
| **Exit Criteria** | Every story has >= 2 Gherkin scenarios (Given/When/Then); at least one scenario per story is an explicit boundary or failure case (e.g., hour 19.5 arrival, Day 42 purge, race condition, channel failure); no HTTP codes, SQL, REST endpoints, or implementation details in any criterion; traceability from each story to its outcome(s) |
| **Verification Method** | Human review of scenario structure; automated pattern match for Given/When/Then; implementation-coupling grep (HTTP, SQL, REST, API, database) |

### GATE-03: Architectural Quality & Scenario Gate

| Aspect | Specification |
| --- | --- |
| **Entrance Criteria** | 3 quality scenarios drafted covering Performance (QS-01), Security/Privacy (QS-02), Reliability/Availability (QS-03); MoSCoW categorization drafted |
| **Exit Criteria** | Every scenario specifies all 6 ISO 29148 components (Source, Stimulus, Artifact, Environment, Response, Response Measure); Response Measures are mathematically falsifiable: < 0.1% error rate, 302 users, p95 <= 500 ms, 100% PII elimination, <= 41 days retention, 0% re-identification, purge <= 1h past Day 42, 100% requests <= 20h, zero lost requests, escalation <= 15 min; MoSCoW Won't Have explicitly names at least 3 deferred items with engineering justification |
| **Verification Method** | Human review of six-component completeness; quantitative threshold check; MoSCoW boundary audit |

### GATE-04: Human-in-the-Loop Security & Static Analysis Gate

| Aspect | Specification |
| --- | --- |
| **Entrance Criteria** | Implementation task breakdown drafted; CI pipeline configured with deterministic linters and SAST; AI-assisted code artifacts (if any) available for review |
| **Exit Criteria** | SAST scan passes with zero critical/high findings for secret leakage, PII in log output, string-interpolated SQL, hardcoded credentials, or undefined (phantom) imports; linter enforces ASCII-only source; all AI-assisted code artifacts have recorded human disposition in audit trail; no AI-generated code merged without gate passage |
| **Verification Method** | Automated SAST/lint execution in CI; human audit of disposition records |

### GATE-05: Traceability Closure & Release Certification Gate

| Aspect | Specification |
| --- | --- |
| **Entrance Criteria** | All prior gates passed; traceability matrix drafted linking Outcomes, User Stories, Quality Scenarios, and Planned Tests; AI usage appendix compiled |
| **Exit Criteria** | 100% bidirectional traceability verified: every Outcome maps to >= 1 User Story and >= 1 Quality Scenario; every User Story maps to >= 1 Outcome and >= 1 Quality Scenario; every Quality Scenario maps to >= 1 Outcome and >= 1 User Story; every Planned Test maps to exactly 1 Quality Scenario and >= 1 User Story; no orphan entries; AI usage appendix contains >= 2 Modified/Rejected dispositions with rationale; zero PII in repository; 100% ASCII compliance |
| **Verification Method** | Automated traceability matrix validation; human certification sign-off |

---

## 3. Verification and Feedback Loops

Two distinct loops operate concurrently, with different cycle times and accountability boundaries.

### Inner Loop (Fast Cycle: Hours)

**Purpose:** Rapid iteration on AI-assisted drafting with deterministic feedback.

| Stage | Activity | Tooling | Accountability |
| --- | --- | --- | --- |
| **Prompt Engineering** | Human specifies intent via structured prompt; AI generates draft | Prompt templates, few-shot examples | Human defines intent |
| **Deterministic Linting** | ASCII compliance, PII pattern detection, implementation-coupling grep | Custom grep/rg rules, secret scanner | Machine-enforced |
| **Property-Based Testing** | Adversarial input generation against acceptance criteria | Hypothesis, jqf, or equivalent | Machine-executed, human-specified properties |
| **Human Audit Gate** | Engineer reviews draft, records disposition, commits or rejects | Task audit template (TASK_TEMPLATE.md) | Human decides |

**Cycle Time:** Minutes to hours per artifact. The inner loop never produces deployable artifacts;
it produces gate-ready candidates.

### Outer Loop: Stakeholder Validation (Slow Cycle: Days)

**Purpose:** Validation of operational guarantees with domain stakeholders.

| Stage | Activity | Participants | Accountability |
| --- | --- | --- | --- |
| **Load Test Execution** | Run TC-PERF-01 and TC-CONCUR-01 at 302 concurrent users in staging | Engineer, Platform Ops | Engineer certifies results |
| **Compliance Review** | DPO / Legal Counsel validates deletion pipeline against policy; SecOps validates audit retention | DPO, SecOps, Engineer | DPO/SecOps sign off |
| **SLA Drill** | Simulate degraded alert channels; verify TC-SLA-01 pass | Engineer, Access Administrator | Access Administrator certifies |
| **Release Certification** | GATE-05 final verification; compilation of submission PDF | Engineer | Engineer certifies |

**Cycle Time:** Hours to days. The outer loop gates deployment. No artifact reaches the submission
PDF without outer-loop validation.

---

## 4. Engineering Trade-off Analysis

### Trade-off 1: Velocity vs. Verification Depth

| Dimension | Velocity Emphasis | Verification Depth Emphasis |
| --- | --- | --- |
| **Description** | Accelerate drafting by accepting AI output with lighter review, reducing inner-loop cycles | Invest in exhaustive adversarial edge-case analysis, property-based testing, and formal specification |
| **Benefit** | Faster artifact production; more time for stakeholder validation | Higher confidence in edge-case correctness; fewer production surprises under variant constraints |
| **Cost** | Risk of undetected boundary failures (hour 19.5, Day 42 purge, race conditions) | Longer inner-loop cycles; requires specialized testing expertise |
| **Resolution for RE-027** | **Verification depth wins.** The variant's hard constraints (20-hour SLA, 41-day retention, 302 concurrent users) are non-negotiable. A velocity shortcut that misses a boundary case directly breaches the SLA or leaks PII. The process mandates property-based testing and explicit boundary scenarios at GATE-02 and GATE-03. |

### Trade-off 2: Full Automation vs. Mandatory Human Audit Gates

| Dimension | Full Automation | Mandatory Human Audit Gates |
| --- | --- | --- |
| **Description** | CI/CD pipeline automatically promotes AI-generated artifacts that pass automated tests | Every AI artifact requires human review, disposition recording, and explicit acceptance before merge |
| **Benefit** | Maximum throughput; zero human bottleneck | Unambiguous accountability per ACM/IEEE codes of ethics; catches semantic hallucinations and privacy blindspots that automated tests miss |
| **Cost** | Engineer cannot demonstrate personal responsibility for AI output; legal liability unclear | Slower promotion; requires engineer time for every artifact |
| **Resolution for RE-027** | **Mandatory human audit gates win.** The deletion policy involves legal compliance (GDPR-class regulation). The engineer must be able to testify to the specific verification performed on every AI-assisted artifact. The audit trail in every `task_*.md` is the evidence chain. No automated gate substitutes for this. |

### Trade-off 3: Agile Scope Flexibility vs. Rigid SLA Contractual Boundaries

| Dimension | Agile Scope Flexibility | Rigid SLA Contractual Boundaries |
| --- | --- | --- |
| **Description** | Allow requirements to evolve during the week based on stakeholder feedback; re-prioritize stories mid-iteration | Treat the 20-hour SLA, 41-day retention, 302-user concurrency, and Personal-Data-Deletion-on-Request policy as immutable constraints that cannot be re-scoped |
| **Benefit** | Adapts to learning; avoids building the wrong thing | Guarantees regulatory and contractual compliance; prevents scope creep that endangers the hard constraints |
| **Cost** | Risk of drifting from variant parameters; stakeholder requests may conflict with hard limits | Less responsive to new stakeholder insights during the week |
| **Resolution for RE-027** | **Rigid SLA boundaries win for Must Have scope.** The variant parameters are regulatory/contractual, not negotiable. Agile flexibility applies only to Should Have and Could Have items (configurable thresholds, dashboard, webhooks). Must Have scope is frozen at inception (GATE-01). The MoSCoW Won't Have list exists precisely to protect this boundary. |

---

## Process Conformance Checklist

- [ ] All 7 days executed with defined gate targets
- [ ] All 5 gates passed with recorded evidence
- [ ] Inner loop tooling configured and operational (lint, property tests, SAST)
- [ ] Outer loop stakeholder reviews scheduled and completed
- [ ] Trade-off decisions documented and communicated to stakeholders
- [ ] AI usage appendix complete with >= 2 Modified/Rejected dispositions
- [ ] Final submission PDF assembled and verified

**Status**: Process defined. Execution follows the daily roadmap above.