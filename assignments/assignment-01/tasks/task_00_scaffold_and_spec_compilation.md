# TASK-00: Repository Scaffolding and Canonical Specification Compilation

| Field | Value |
| --- | --- |
| Task ID | TASK-00 |
| Status | Complete |

## Master Prompt

The superset of all instructions issued for repository setup and specification compilation.

```text
Act as a Principal Software Engineer.

Initialize this repository for the course "Software Engineering 2026" (SE2026) as a semester
coursework portfolio. Work under a strict minimalist strategy: create no premature documentation and
no speculative analysis artifacts. Keep the repository free of hardcoded student PII at all times.

1. Repository Hygiene. Create a root `.gitignore` excluding standard OS artifacts, editor and IDE
   settings, dependency directories, environment secrets (`.env*`), and local identity or config
   files (`*.local.*`, `*.local.json`).

2. Anonymous Portfolio README. Create a root `README.md` presenting the course as an academic
   portfolio. It carries no student names, identifiers, or personal metadata, and no operational
   notes, CLI trivia, or internal identity-handling instructions. Include a coursework index table
   linking each assignment to its directory.

3. Assignment Workspace. Create `assignments/assignment-01/`, holding the canonical English
   specification (`ASSIGNMENT.md`), the instructor-issued source specification
   (`ASSIGNMENT_RAW_VI.md`), and a task audit trail directory (`tasks/`) seeded with a reusable
   handoff template.

4. Canonical Specification Compilation. Ingest the instructor-issued source and compile a formal
   English specification into `ASSIGNMENT.md`, structured as: Administrative Context and Variant
   Constraints; Problem Framing and Scope; Technical Grading Rubric with six standardized criteria;
   and a verifiable integrity-threshold checklist. Translate all six criteria into ISO/IEC/IEEE
   29148 terminology.

5. Localization and PII Redaction. Sweep the compiled specification for residual source-language
   fragments and transliterations and translate all of them into standardized Software Engineering
   English. The specification must be 100 percent pure ASCII with operators in ASCII form. Redact
   every literal student identifier from the source specification, including identifiers embedded in
   filename examples and front-page field lists, and never propagate such literals into derived
   artifacts.

6. Parameter Preservation. The variant RE-027 constraints must survive compilation unaltered:
   Access Administrator as focus stakeholder; Personal-Data-Deletion-on-Request policy as the
   triggering change; 302 concurrent active users; 41-day retention limit; 20-hour change request
   response window; a submission budget of at most 6 pages excluding the AI usage appendix; and the
   integrity thresholds of at least 5 checkpoints, at least 4 stakeholder parties, 4 user stories
   with Given/When/Then acceptance criteria, and at least 2 AI rejection logs.

7. Dual-Language Identity Protocol. Resolve student identity dynamically at generation time rather
   than storing it in version control: the student identifier for submissions, the Vietnamese name
   for Vietnamese-language deliverables, and the English name for English-language deliverables and
   code metadata.

8. Verification and Audit Trail. Verify parameter preservation, absence of PII, and ASCII purity by
   terminal check before each commit. Record every directive as a task artifact under `tasks/`,
   capturing the input prompt, the AI draft output, and the human disposition of each draft element.
```

## Produced Artifacts

- `.gitignore` -- repository hygiene rules
- `README.md` -- portfolio overview and coursework index
- `assignments/assignment-01/ASSIGNMENT.md` -- canonical English specification
- `assignments/assignment-01/ASSIGNMENT_RAW_VI.md` -- instructor-issued source, identifiers redacted
- `assignments/assignment-01/tasks/TASK_TEMPLATE.md` -- reusable handoff template
- `assignments/assignment-01/tasks/task_00_scaffold_and_spec_compilation.md` -- this record

## Core Audit Notes

- **Identity is resolved dynamically, never stored.** Student identity is retrieved from git config
  at generation time; three literal identifiers found in the instructor-issued source were redacted
  to placeholders before publication rather than propagated into derived artifacts.
- **Canonicalization is strict.** All source-language fragments and transliterations were translated
  into ISO/IEC/IEEE 29148 terminology and every operator and dash normalized to ASCII, verified by
  terminal check. A first-pass verification script was itself rejected: a character class evaluated
  under a non-UTF-8 locale collapsed to a byte set and produced a false positive, and was re-run
  under an explicit UTF-8 locale with word anchors.
- **Source ambiguity is recorded, not silently resolved.** The source stated rubric section weights
  in two places that disagreed while both summing to 100. The specification compiles against the
  Scoring Rubric weights and records the discrepancy explicitly.
- **The source specification diverges from the issued original by anonymization only.** No
  requirement, constraint, or parameter was altered.
