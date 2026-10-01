# Assignment 01 Specification: Software Engineering in the AI Era

> Canonical English specification, compiled from `ASSIGNMENT_RAW_VI.md` (Vietnamese source issued by
> the instructor). In the event of any conflict, the Vietnamese source is authoritative. This
> document contains no student PII; identity placeholders are resolved at submission time via
> `git config student.*`.

---

## Administrative Context & Variant Constraints

| Field | Value |
| --- | --- |
| Course | Software Engineering 2026 (SE2026) |
| Assessment type | Personal Assignment 1 (`BT cá nhân 1`) |
| Topic code | AI-03 — GitHub Project Coach for student groups |
| Team ID | SE2026-T07 |
| **Variant code** | **RE-027** |
| Assessment mode | Individual submission (not a team deliverable) |

**Focus stakeholder.** The access administrator — the individual accountable for access rights
within the group repository.

**Triggering change.** During development, a new policy is introduced requiring deletion of
personal data on request.

**Organizational constraint.** The original requirement carries a large number of unverified
assumptions; these must be surfaced and validated rather than accepted at face value.

**Variant-specific parameters.** These figures are mandatory and must be used verbatim wherever the
submission quantifies load, retention, or responsiveness:

| Parameter | Value |
| --- | --- |
| Concurrent active users | **302** |
| Data retention period | **41 days** |
| Team response window for a change request | **20 hours** |

### Source discrepancy (recorded, not silently reconciled)

The Vietnamese source states per-section weights in two places, and they disagree internally while
both summing to 100:

| Section | `YÊU CẦU THỰC HIỆN` list | `Khung chấm điểm` table |
| --- | --- | --- |
| SE in the AI Era | 15 | 15 |
| Software Process | 20 | 20 |
| Product Thinking | 20 | 20 |
| Requirements Engineering | 30 | 35 (20 + 15, split across two criteria) |
| Engineering Evidence & AI Reflection | 15 | 10 |

This document compiles against the **table** weights, which decompose cleanly into the six
standardized criteria below. Both readings total 100.

---

## Problem Framing & Scope

Analyze the AI-03 "GitHub Project Coach for student groups" topic for team SE2026-T07, taking the
**access administrator** as the stakeholder in focus. The scope is the assessment of an
AI-generated deliverable under the RE-027 variant: the personal-data-deletion-on-request policy,
the unverified-assumption constraint, and the three quantitative parameters above.

The submission is a single PDF of at most **6 pages**, excluding the AI usage appendix. It must use
the exact stakeholder, trigger, constraint, parameters, and quality attribute of variant RE-027.
Copying artifacts produced by the team or by other students is prohibited.

### Required content by assessment area

1. **Software Engineering in the AI Era** — three reasons an AI-generated MVP may be runnable yet
   not trustworthy enough to hand over; analysis of the engineer's accountability for the specific
   AI failure mode of **silently ignoring a conflict between two stakeholders**.
2. **Software Process** — select Waterfall, iterative/incremental, Scrum, Kanban, or a hybrid
   AI-native process. Design a **1-week workflow with at least 5 checkpoints** from requirements to
   a verifiable build. Justify the choice against the stated constraints and name **one trade-off**.
3. **Product Thinking** — a problem statement containing **no technology names**; identify the user
   outcome, the product outcome, and **two dangerous assumptions**; build a **stakeholder map with at
   least 4 parties**, identifying **one conflict** that must be resolved.
4. **Requirements Engineering** — **4 user stories**, each with Given/When/Then acceptance criteria
   including **at least one failure case**; **one quality attribute scenario** for *Performance*
   focused on response time under concurrent load with **testable metrics**; a **MoSCoW** analysis for
   the MVP naming explicitly what is **not** built in the first round.
5. **Engineering Evidence & AI Reflection** — a stakeholder–need–conflict matrix; the prompt and an
   excerpt of AI output actually used, with **at least 2 places marked as corrected or rejected** and
   the reason for each; a short traceability table: **Outcome → Requirement → Acceptance criterion →
   Planned test**.

### Submission requirements

- **Destination:** the corresponding assignment on Google Classroom. Not by email; not to the team's
  GitHub repository.
- **Artifacts:** one PDF file only. No Word file, no ZIP, no link requiring instructor-granted access.
- **Filename:** `BT1_<STUDENT_ID>_<VARIANT_CODE>.pdf` — for this variant,
  `BT1_<STUDENT_ID>_RE-027.pdf`. Resolve `<STUDENT_ID>` at submission time via
  `git config student.id`; never hardcode it.
- **Front page, mandatory:** full name, student ID, variant code (also encoded in the filename), team
  ID and topic code, and the commitment statement: *"I take full responsibility for the content of
  this submission and have declared my use of AI."*
- **Section order:** the six headings above in the order given by the assignment, with the AI Usage
  Log appendix last.
- **AI usage declaration:** AI use is permitted, but the student is accountable for submitted
  content. The appendix records the tools used, the main prompts, the AI-proposed content, what was
  kept/modified/rejected, and the reasons. A full chat transcript is not required.
- **Before submitting:** verify the student ID and variant code; resubmission before the deadline is
  permitted and the final Classroom version is the one graded. The instructor may ask the student to
  explain parts of the submission directly, to verify individual authorship.

---

## Technical Grading Rubric (6 Core Criteria)

### 1. Software Engineering in the AI Era — 15%

Distinguish software that *runs* from software that is *trustworthy*. Articulate verification
accountability and correctly analyse the specific failure mode of **AI ignoring a conflict between
two stakeholders**.

### 2. Software Process — 20%

A 1-week workflow with **≥ 5 checkpoints**. The process selection must be argued, not asserted, and
must demonstrate **feedback, verification, and one explicit trade-off**.

### 3. Problem Framing & Product Thinking — 20%

The problem statement must not pre-commit to a solution. Outcomes must be explicit. The stakeholder
map must contain **≥ 4 parties** and expose **at least one conflict** alongside the assumptions
requiring validation.

### 4. User Stories & Acceptance Criteria — 20%

**4 user stories** carrying genuine user value. Given/When/Then criteria must be **observable**, must
include **boundary or failure cases**, and must avoid irrational dependence on implementation
details.

### 5. Quality Scenarios & MVP Scope — 15%

The quality attribute scenario must specify **source, stimulus, environment, response, and a
measurable response measure**, targeting **response time under concurrent load**. The MoSCoW
prioritisation must be **consistent with the stated outcomes** and the MVP boundary.

### 6. Engineering Evidence & AI Auditing — 10%

Concrete evidence artifacts; the prompt and AI output used; **at least 2 justified corrections or
rejections** of AI output; and traceability from outcome through to planned test.

---

## Integrity Thresholds Checklist

Machine-checkable minimums carried over from the Vietnamese source:

- [ ] 1-week workflow with **≥ 5 checkpoints**
- [ ] Stakeholder map with **≥ 4 parties**
- [ ] **4 user stories**, each with Given/When/Then acceptance criteria
- [ ] **≥ 1 failure case** per story (at least one overall, per source reading: *mỗi story*)
- [ ] Quality attribute scenario for Performance, with testable metrics
- [ ] MoSCoW naming what is excluded from the first round
- [ ] Stakeholder–need–conflict matrix
- [ ] **≥ 2 AI corrections or rejections**, each with a stated reason
- [ ] Traceability chain: Outcome → Requirement → Acceptance criterion → Planned test
- [ ] PDF ≤ 6 pages excluding the AI usage appendix
- [ ] Variant RE-027 parameters used verbatim: 302 / 41 days / 20 hours
