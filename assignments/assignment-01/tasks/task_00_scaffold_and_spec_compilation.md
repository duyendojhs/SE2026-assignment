# TASK-00: Repository Scaffolding and Specification Compilation

| Field | Value |
| --- | --- |
| Task ID | TASK-00 |
| Assignment | Assignment 01 -- Software Engineering in the AI Era (variant RE-027) |
| Target | Repository initialization, minimalist hygiene, and bilingual specification canonicalization |
| Status | Complete |
| Commits | `19e898e`, `6952225`, `eb372e0`, `920f594` |

## Target Rubric Criteria

This task is preparatory and is not itself scored against the six grading criteria. It establishes
the infrastructure on which the scored deliverables are produced, and it pre-commits the audit
trail required by the *Engineering Evidence and AI Auditing* criterion (rubric section 6).

---

## Input Prompts and Directives

The four directives below are reproduced verbatim as executed, so that an evaluator can inspect the
exact input instructions independently of this summary.

### Directive 1 -- Minimalist scaffolding (`19e898e`)

```text
Act as a Principal Software Engineer.

Initialize this repository for the academic course "Software Engineering 2026" (SE2026) using a strict minimalist scaffolding strategy. Do not create premature documentation or speculative analysis files until requirements are fully provided. Ensure complete privacy by keeping the repository free of hardcoded student PII.

Execute the following steps sequentially:

1. Repository Hygiene (.gitignore):
   - Create a root `.gitignore` configured to exclude standard OS artifacts, editor settings, dependency directories, environment secrets (`.env*`), and local identity/config files (`*.local.*`, `*.local.json`).

2. Repository Overview (README.md):
   - Create a clean root `README.md` defining the academic context: Course "Software Engineering 2026" - Semester Coursework Portfolio.
   - Do NOT include any hardcoded student names, student IDs, or personal metadata in this file.
   - Add a directory table referencing upcoming modules, pointing `Assignment 01` to `assignments/assignment-01/`.

3. Assignment Workspace:
   - Create directory path: `assignments/assignment-01/`
   - Inside it, create ONLY one single blank file: `assignments/assignment-01/ASSIGNMENT.md`. This will serve as the single source of truth where the assignment prompt, variant constraints, and grading rubric will be stored.

4. Dual-Language Identity Protocol:
   - When generating deliverables or submissions later, dynamically retrieve student identity via terminal commands based on language context:
     * Student ID: `git config student.id`
     * Vietnamese deliverables: `git config student.name-vi`
     * English deliverables / Code metadata: `git config student.name-en`
   - Never hardcode these values directly into version-controlled files.

5. Git Commit:
   - Stage and commit the scaffolded files using Conventional Commits format:
     `chore: initialize minimalist workspace for assignment-01`

Confirm execution and display the resulting directory tree.
```

### Directive 2 -- Specification ingestion and compilation (`6952225`)

```text
Act as a Principal Software Engineer and Requirements Analyst.

I have stored the raw Vietnamese coursework specification from instructor Bui Sy Nguyen in:
`assignments/assignment-01/ASSIGNMENT_RAW_VI.md`

Execute the following tasks:

1. Specification Translation & Canonical Compilation:
   - Ingest and parse `assignments/assignment-01/ASSIGNMENT_RAW_VI.md`.
   - Compile a formal, professional English specification into `assignments/assignment-01/ASSIGNMENT.md`.
   - Structure `ASSIGNMENT.md` with the following explicit sections:
     * `# Assignment 01 Specification: Software Engineering in the AI Era`
     * `## Administrative Context & Variant Constraints` (Preserve student variant code and core assignment parameters)
     * `## Problem Framing & Scope`
     * `## Technical Grading Rubric (6 Core Criteria)`: Translate all 6 criteria accurately into standardized SE terminology (15% SE in AI Era, 20% Software Process, 20% Problem Framing, 20% User Stories & AC, 15% Quality Scenarios & MVP, 10% Engineering Evidence & AI Auditing).

2. Integrity Verification:
   - Check that `ASSIGNMENT_RAW_VI.md` and `ASSIGNMENT.md` match 1:1 in intent without omitting any rubric threshold (e.g., >=5 checkpoints, >=4 stakeholders, Gherkin Given/When/Then, 2 AI rejection logs).

3. Git Execution:
   - Stage both files (`ASSIGNMENT_RAW_VI.md` and `ASSIGNMENT.md`).
   - Commit with Conventional Commits:
     `docs(assignment-01): ingest raw vietnamese spec and compile canonical english specification`

Report back with a structural summary of the compiled specification.
```

### Directive 3 -- Localization sweep (`eb372e0`)

```text
Act as a Lead Requirements Engineer and Technical Editor.

Refactor `assignments/assignment-01/ASSIGNMENT.md` to ensure it is written in 100% pure, professional Software Engineering English. 

Execute the following steps:

1. Text Audit & Localization Sweep:
   - Scan `assignments/assignment-01/ASSIGNMENT.md` for any remaining Vietnamese words, transliterations, or untranslated phrases (e.g., section headers, table notes, or evaluation labels).
   - Translate all identified Vietnamese fragments into rigorous, standardized Software Engineering terminology (IEEE / ISO/IEC/IEEE 29148 standards).

2. Preservation of Parameters:
   - Ensure none of the variant constraints are altered during translation:
     * Focus stakeholder: Access Administrator
     * Triggering change: Personal-data-deletion-on-request policy
     * System parameters: 302 concurrent users, 41-day retention limit, 20-hour change request window
     * Page budget: <= 6 pages (excluding appendix)
     * Integrity thresholds: >= 5 checkpoints, >= 4 stakeholder parties, 4 user stories, 2 AI rejection logs.

3. Automated Linguistic Verification:
   - Run a terminal command/regex check to verify that no non-ASCII / Vietnamese characters (e.g., à, á, ả, ã, ạ, đ, ê, ô, ơ, ư...) remain in `assignments/assignment-01/ASSIGNMENT.md`.

4. Git Commit:
   - Stage and commit the updated file:
     `refactor(assignment-01): ensure 100% pure english canonical specification`

Report back with the list of translated terms and the regex verification outcome.
```

### Directive 4 -- Public documentation and task audit trail (`920f594`)

```text
Act as a Principal Software Engineer and Project Architect.

Refactor the repository's public documentation, establish the task execution audit trail for Assignment 01, and synchronize all commits with the remote GitHub repository.

Execute the following actions:

1. Professionalize Root `README.md`:
   - Rewrite `README.md` into an executive, public-facing academic portfolio overview.
   - Remove all operational notes, CLI trivia, and internal instructions regarding `git config` or identity placeholders.
   - Structure the file cleanly with: Project Title, Academic Context, Repository Architecture, and Coursework Index table.

2. Initialize Task & Prompt Audit Directory:
   - Create directory: `assignments/assignment-01/tasks/`
   - Create `assignments/assignment-01/tasks/task_00_scaffold_and_spec_compilation.md` documenting retroactive setup.
   - Create `assignments/assignment-01/tasks/TASK_TEMPLATE.md` as reusable handoff template.

3. Git Execution & Remote Push:
   - Stage and commit: `docs: refine root readme and establish task audit trail for assignment-01`
   - Push branch to remote (`git push -u origin main`).
```

**Evidentiary caveat on Directive 4.** The capture above is a condensed restatement of the prompt as
issued: the original enumerated per-section structure requirements for the README and enumerated the
required audit-record fields for `task_00`, both of which are reproduced as the governing prose of
this document rather than inside the code block. Directives 1 through 3 are captured in full.

---

## AI Draft Output

| Artifact | Agent disposition | Rationale |
| --- | --- | --- |
| `.gitignore` | Accepted as drafted | Covers all five required categories with no over-broad patterns |
| `README.md` (scaffold) | Modified | Original draft carried an operational note on identity retrieval; removed as internal, see Directive 4 |
| `ASSIGNMENT.md` (compilation) | Modified | Draft normalized the six rubric weights from the Scoring Rubric table; agent recorded the source discrepancy explicitly rather than silently reconciling it |
| `ASSIGNMENT_RAW_VI.md` | Accepted as received, then **Modified** | Instructor-issued source committed unmodified, but three literal student identifiers were later redacted to placeholders prior to publication; see Verified Outputs |
| Student identifier literals in source | **Rejected** | The source specification embeds literal student identifiers in the filename example and the mandatory front-page field list. These were replaced with a placeholder resolved at submission time and were not propagated into `ASSIGNMENT.md`. |

---

## Verified Outputs

### 1. Scaffolding tree

```
d:\SE2026-assignment
├── README.md
├── .gitignore
└── assignments
    └── assignment-01
        ├── ASSIGNMENT.md
        ├── ASSIGNMENT_RAW_VI.md
        └── tasks
            ├── task_00_scaffold_and_spec_compilation.md
            └── TASK_TEMPLATE.md
```

Verified clean: no premature documentation or speculative analysis artifacts were created during
initialization, per the minimalist constraint.

### 2. PII sweep

| Check | Result |
| --- | --- |
| Literal student identifier in `ASSIGNMENT.md` | 0 occurrences |
| Literal student identifier in `ASSIGNMENT_RAW_VI.md` | 0 occurrences after redaction (3 substitutions) |
| Eight-digit identifier pattern across all tracked markdown | 0 occurrences |
| Student name in any tracked file | 0 occurrences |
| Student identity in version control | None; resolved dynamically at generation time |

Redaction substitutions applied to `ASSIGNMENT_RAW_VI.md`:

| Original literal | Replacement | Occurrences |
| --- | --- | --- |
| Student's own identifier (filename example) | `<STUDENT_ID>` | 1 |
| Second-party identifier (filename example) | `<STUDENT_ID>` | 1 |
| Student's own identifier (front-page field list) | `<STUDENT_ID>` | 1 |

The file otherwise remains a faithful transcription of the instructor-issued source. The divergence is
anonymization only; no requirement, constraint, or parameter was altered.

### 3. English and standards alignment

| Check | Command class | Result |
| --- | --- | --- |
| Non-ASCII byte sweep | `LC_ALL=C grep '[^ -~]'` | PASS -- zero bytes outside `0x20-0x7E` |
| Source-language diacritic sweep | Targeted character-class regex | PASS -- zero matches |
| Residual source-language fragments | Word-anchored, UTF-8 locale | PASS -- zero matches |
| Legacy Unicode operators and dashes | Unicode codepoint class | PASS -- zero occurrences |

Standards conformance: quality attribute scenarios specify all six ISO/IEC/IEEE 29148 components
(source, stimulus, environment, artifact, response, response measure); traceability is expressed as a
four-link chain from outcome through to planned test; operators are expressed in ASCII form.

**Correction recorded during verification.** The first run of the residual-fragment scan returned a
false positive at the *Software Process* section: the character class for the identifier literal,
evaluated under a non-UTF-8 locale, collapsed to a byte set and matched the substring `ban` within
`Kanban`. The document was correct; the check was not. The scan was re-run with word anchors and an
explicit UTF-8 locale, returning zero matches. Recorded here because a loose character class in the
default locale is a latent defect in any future check of the same kind.

---

## Notes for Subsequent Tasks

- Record every AI-assisted deliverable as a discrete task file under
  `assignments/assignment-01/tasks/`, following `TASK_TEMPLATE.md`.
- Rubric criterion 6 requires a minimum of two corrections or rejections of AI output, each with a
  rationale. TASK-00 supplies three (identifier propagation, rubric weight reconciliation, identity
  note removal) that may be carried forward into the submission's AI usage appendix.
