# Assignment 01 Specification: Software Engineering in the AI Era

> Canonical English specification, compiled from `ASSIGNMENT_RAW_VI.md` (source-language document
> issued by the instructor). In the event of any conflict, the source document is authoritative.
> This specification contains no student personally identifiable information; identity placeholders
> are resolved at submission time via `git config student.*`.
>
> Requirement terminology follows ISO/IEC/IEEE 29148. Non-ASCII characters are deliberately
> avoided throughout, so relational and arithmetic operators are written in ASCII form
> (`>=`, `<=`, `->`).

---

## Administrative Context & Variant Constraints

| Field | Value |
| --- | --- |
| Course | Software Engineering 2026 (SE2026) |
| Assessment type | Personal Assignment 1 |
| Topic code | AI-03 -- GitHub Project Coach for student groups |
| Team identifier | SE2026-T07 |
| **Variant code** | **RE-027** |
| Assessment mode | Individual submission (not a team deliverable) |

**Focus stakeholder.** The Access Administrator -- the individual accountable for access rights
within the group repository.

**Triggering change.** A Personal-Data-Deletion-on-Request policy is introduced during development,
requiring deletion of personal data at the request of the data subject.

**Organizational constraint.** The originating requirement carries numerous unverified assumptions.
Per ISO/IEC/IEEE 29148, these are recorded as candidate assumptions rather than accepted as
baselines, and each must be validated before it constrains the solution.

**Variant-specific parameters.** These values are binding and must be applied verbatim wherever the
submission quantifies load, retention, or responsiveness:

| Parameter | Value |
| --- | --- |
| Concurrent active users | **302** |
| Data retention limit | **41 days** |
| Change request response window | **20 hours** |

### Source discrepancy (recorded, not silently reconciled)

The source document states section weights in two locations that disagree with one another, although
both sum to 100:

| Section | Task Requirements section | Scoring Rubric section |
| --- | --- | --- |
| SE in the AI Era | 15 | 15 |
| Software Process | 20 | 20 |
| Product Thinking | 20 | 20 |
| Requirements Engineering | 30 | 35 (20 + 15, disaggregated across two criteria) |
| Engineering Evidence & AI Reflection | 15 | 10 |

This specification compiles against the **Scoring Rubric** weights, which disaggregate cleanly into
the six standardized criteria below. Both readings total 100.

---

## Problem Framing & Scope

Analyze the AI-03 "GitHub Project Coach for student groups" topic for team SE2026-T07, taking the
**Access Administrator** as the stakeholder of interest. The scope is the assessment of an
AI-generated deliverable under variant RE-027: the Personal-Data-Deletion-on-Request policy, the
unverified-assumption constraint, and the three quantitative parameters above.

The submission is a single PDF of at most **6 pages**, excluding the AI usage appendix. It must apply
the exact stakeholder, trigger, constraint, parameters, and quality attribute of variant RE-027.
Reuse of artifacts produced by the team or by other students is prohibited.

### Required content by assessment area

1. **Software Engineering in the AI Era** -- three reasons an AI-generated MVP may be executable yet
   insufficiently trustworthy for handover; analysis of engineer accountability for the specific
   failure mode in which the **AI silently disregards a conflict between two stakeholders**.
2. **Software Process** -- select from Waterfall, iterative/incremental, Scrum, Kanban, or a hybrid
   AI-native process. Design a **one-week workflow with at least 5 checkpoints**, spanning
   requirements elicitation through to a verifiable build increment. Justify the selection against
   the stated constraints and state **one trade-off**.
3. **Product Thinking** -- a problem statement containing **no technology names**; identify the user
   outcome, the product outcome, and **two hazardous assumptions**; produce a stakeholder map of
   **at least 4 parties**, identifying **one conflict** requiring resolution.
4. **Requirements Engineering** -- **4 user stories**, each carrying Given/When/Then acceptance
   criteria and including **at least one failure case**; **one quality attribute scenario** for the
   *Performance* attribute, addressing response time under concurrent load with **measurable
   response measures**; a **MoSCoW** prioritisation for the MVP that states explicitly what is
   **deferred** beyond the first increment.
5. **Engineering Evidence and AI Reflection** -- a stakeholder-need-conflict matrix; the prompt and
   an excerpt of the AI output actually used, marking **at least 2 locations as corrected or
   rejected**, each with a stated rationale; a traceability table establishing the chain
   **Outcome -> Requirement -> Acceptance Criterion -> Planned Test**.

### Submission requirements

- **Destination:** the corresponding assignment on Google Classroom. Not by email, and not to the
  team's GitHub repository.
- **Artifacts:** one PDF file only. No Word document, no ZIP archive, and no link requiring
  instructor-granted access.
- **Filename:** `BT1_<STUDENT_ID>_<VARIANT_CODE>.pdf`; for this variant,
  `BT1_<STUDENT_ID>_RE-027.pdf`. Resolve `<STUDENT_ID>` at submission time via
  `git config student.id`; never hardcode it.
- **Front page, mandatory:** full name, student identifier, variant code (also encoded in the
  filename), team identifier and topic code, and the following declaration of accountability:
  *"I assume full responsibility for the content of this submission and have declared my use of AI."*
- **Section order:** the six headings above, in the order prescribed by the assignment, with the AI
  Usage Log appendix placed last.
- **AI usage declaration:** AI use is permitted, but the submitting student remains accountable for
  all submitted content. The appendix records the tools used, the principal prompts, the
  AI-proposed content, the elements retained, modified, or rejected, and the reasons for each
  disposition. A complete chat transcript is not required.
- **Before submission:** verify the student identifier and variant code. Resubmission before the
  deadline is permitted, and the final version held on Google Classroom is the version graded. The
  instructor may require the student to explain portions of the submission directly in order to
  verify individual authorship.

---

## Technical Grading Rubric (6 Core Criteria)

### 1. Software Engineering in the AI Era -- 15%

Distinguish software that is **operational** from software that is **trustworthy**. Articulate
verification and validation accountability, and correctly analyze the specific failure mode in
which the **AI disregards a conflict between two stakeholders**.

### 2. Software Process -- 20%

A one-week workflow with **>= 5 checkpoints**. The process selection must be argued rather than
asserted, and must demonstrate **feedback incorporation, verification, and one explicit trade-off**.

### 3. Problem Framing and Product Thinking -- 20%

The problem statement must not pre-commit to a solution. Outcomes must be stated explicitly. The
stakeholder map must contain **>= 4 parties** and must expose **at least one conflict**, together
with the assumptions requiring validation.

### 4. User Stories and Acceptance Criteria -- 20%

**4 user stories** conveying genuine user value. Given/When/Then acceptance criteria must be
**observable**, must include **boundary or failure cases**, and must avoid unwarranted coupling to
implementation detail.

### 5. Quality Scenarios and MVP Scope -- 15%

The quality attribute scenario must specify **source, stimulus, environment, artifact, response, and
response measure**, and must target **response time under concurrent load**. The MoSCoW
prioritisation must be **consistent with the stated outcomes** and with the MVP boundary.

### 6. Engineering Evidence and AI Auditing -- 10%

Concrete evidence artifacts; the prompt and the AI output relied upon; **at least 2 corrections or
rejections of AI output**, each supported by a rationale; and bidirectional traceability from
outcome through to planned test.

---

## Integrity Thresholds Checklist

Verifiable minimums carried over from the source document:

- [ ] One-week workflow with **>= 5 checkpoints**
- [ ] Stakeholder map with **>= 4 parties**
- [ ] **4 user stories**, each with Given/When/Then acceptance criteria
- [ ] **>= 1 failure case per user story**; the source attaches this obligation to each story, and
      the weaker reading of ">= 1 across the whole set" is not treated as compliant
- [ ] Performance quality attribute scenario with measurable response measures
- [ ] MoSCoW prioritisation naming the capabilities deferred beyond the first increment
- [ ] Stakeholder-need-conflict matrix
- [ ] **>= 2 AI rejection or correction logs**, each with a stated rationale
- [ ] Traceability chain: Outcome -> Requirement -> Acceptance Criterion -> Planned Test
- [ ] PDF of **<= 6 pages**, excluding the AI usage appendix
- [ ] Variant RE-027 parameters applied verbatim: 302 / 41 days / 20 hours
