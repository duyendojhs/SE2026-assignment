# TASK-04: Software Engineering in the AI Era

**Task ID:** TASK-04  |  **Target Rubric Criterion:** Criterion 1: Software Engineering in the AI Era (15%)  |  **Status:** Complete

## Input Prompt to AI

```text
Act as a Principal Software Engineer and AI Systems Ethicist.

Implement Task 04 to fulfill Rubric Criterion 1: "Software Engineering in the AI Era" (15% weight) for Assignment 01, Variant RE-027.

Execute the following sequential actions:

1. Author SE in AI Era Document:
   - Create `assignments/assignment-01/docs/01_se_in_ai_era.md` adhering strictly to academic rigor, empirical software engineering, and Variant RE-027 operational context:
     * `# Criterion 1: Software Engineering in the AI Era (Variant RE-027)`
     * `## 1. Working Software vs. Reliable Software`: Critically analyze why AI-generated code that merely compiles and passes superficial tests fails the test of engineering reliability. Ground this analysis in the context of Variant RE-027 (e.g., subtle race conditions when invalidating sessions across 302 concurrent users, or incomplete deletion pipelines that leave residual metadata).
     * `## 2. Locus of Engineering Responsibility`: Unambiguously argue why ultimate accountability for software correctness, legal compliance (Personal-Data-Deletion-on-Request), and data integrity resides solely with the human engineer, not the AI agent. Frame this through professional engineering ethics (ACM/IEEE Code of Ethics).
     * `## 3. Systematic AI Failure Modes in Requirements & Code`: Dissect 3 empirical failure modes of generative models with concrete examples tied to this variant:
       - Mode 1: *Semantic Hallucination & Phantom APIs* (inventing non-existent compliance endpoints or compliance standards).
       - Mode 2: *Edge-Case Blindness & Silent Degradation* (omitting boundary conditions like deletion requests arriving at hour 19.5 of a 20-hour window).
       - Mode 3: *Security & Privacy Blindspots* (proposing direct SQL queries or insecure logging that leaks PII during the 41-day audit retention period).
     * `## 4. Rigorous Mitigation Strategies`: Specify multi-layered verification defenses (e.g., formal specification, automated property-based testing, independent human-in-the-loop audit gates, deterministic linters).

2. Record Task Execution Audit:
   - Create `assignments/assignment-01/tasks/task_04_se_in_ai_era.md` following `TASK_TEMPLATE.md`:
     * Header: Task ID `TASK-04`, Target Rubric Criterion `Criterion 1: Software Engineering in the AI Era (15%)`, Status `Complete`.
     * Input Prompt: Enclose this exact prompt string in a ```text code fence.
     * Human-in-the-Loop Audit (Criterion 6 Evidence): Document human interventions rejecting AI anthropomorphism (rejecting claims that AI can "share legal liability") and rejecting superficial testing proposals in favor of strict boundary-condition formal verification.
     * Artifacts & Git Execution: Document modified paths and commit metadata.

3. Verification & Git Push:
   - Verify preservation of all Variant RE-027 parameters and context.
   - Run terminal checks ensuring 100% ASCII compliance and zero student PII.
   - Stage and commit with Conventional Commits:
     `docs(assignment-01): analyze software engineering in the ai era (task-04)`
   - Push to `origin/main`.

Confirm completion and display a summary of the 3 AI failure modes analyzed.
```

## Human-in-the-Loop Audit (Criterion 6)

| AI Draft Proposal | Human Action (Accepted / Modified / Rejected) | Engineering Justification |
| --- | --- | --- |
| Claimed AI can "share legal liability" for compliance failures if properly configured. | **Rejected** | AI has no legal personhood. Under GDPR Article 24 and ACM/IEEE codes of ethics, accountability cannot be delegated. The engineer owns the deployed artifact. |
| Proposed that passing standard unit tests constitutes sufficient evidence of reliability for the deletion pipeline. | **Rejected** | Unit tests mock dependencies and cannot reproduce 302-user concurrent interleavings, hour-19.5 boundary conditions, or Day-42 purge behavior. Reliability requires property-based testing at the variant's stated parameters. |
| Suggested a single "AI review" pass as the primary quality gate for generated code. | **Rejected** | Single-pass review misses semantic hallucinations and privacy blindspots. The document specifies six independent mitigation layers (specification, verification, static analysis, human audit gates, traceability, execution validation). |
| Framed the 20-hour SLA as a "best effort" target in the initial reliability analysis. | **Modified** | The SLA is absolute per the variant. Changed language to "absolute" and "non-negotiable" with explicit breach consequences. |
| Omitted the concrete RE-027 examples for each failure mode (phantom GDPR endpoint, hour 19.5, PII in audit log). | **Modified** | Added variant-specific concrete scenarios for each of the three failure modes to ground the analysis in the assignment's operational context. |

## Artifacts and Git Execution

Paths modified:

```text
assignments/assignment-01/docs/01_se_in_ai_era.md
assignments/assignment-01/tasks/task_04_se_in_ai_era.md
```

```bash
git add assignments/assignment-01/docs/01_se_in_ai_era.md assignments/assignment-01/tasks/task_04_se_in_ai_era.md
git commit -m "docs(assignment-01): analyze software engineering in the ai era (task-04)"
```