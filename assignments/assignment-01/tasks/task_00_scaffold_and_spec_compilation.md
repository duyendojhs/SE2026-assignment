# TASK-00: Repository Scaffolding and Specification Compilation

| Field | Value |
| --- | --- |
| Task ID | TASK-00 |
| Assignment | Assignment 01 -- Software Engineering in the AI Era (variant RE-027) |
| Target | Repository initialization, minimalist hygiene, and bilingual specification canonicalization |
| Status | Complete |
| Commits | `19e898e`, `6952225`, `eb372e0` |

## Target Rubric Criteria

This task is preparatory and is not itself scored against the six grading criteria. It establishes
the infrastructure on which the scored deliverables are produced, and it pre-commits the audit
trail required by the *Engineering Evidence and AI Auditing* criterion (rubric section 6).

---

## Input Prompts and Directives

Four engineering directives were issued across three commits.

### Directive 1 -- Minimalist scaffolding (`19e898e`)

Initialize the repository under a strict minimalist strategy: create a root `.gitignore` covering OS
artifacts, editor settings, dependency directories, environment secrets (`.env*`), and local
identity or config files (`*.local.*`, `*.local.json`); create a root `README.md` defining the
academic context with no student PII; create `assignments/assignment-01/` containing exactly one
file, `ASSIGNMENT.md`; establish a dual-language identity protocol that resolves student identity
dynamically at generation time rather than hardcoding it into version-controlled files; commit using
Conventional Commits.

**Agent execution:** wrote the three files, staged them, committed
`chore: initialize minimalist workspace for assignment-01`.

### Directive 2 -- Specification ingestion and compilation (`6952225`)

Ingest the instructor-issued source specification, compile a formal English specification into
`ASSIGNMENT.md` with mandated section structure (Administrative Context and Variant Constraints;
Problem Framing and Scope; Technical Grading Rubric with six standardized criteria), verify
integrity of the translation against the source thresholds, and commit both documents.

**Agent execution:** parsed the source, compiled the specification, verified threshold coverage and
absence of literal student identifiers, committed
`docs(assignment-01): ingest raw vietnamese spec and compile canonical english specification`.

### Directive 3 -- Localization sweep (`eb372e0`)

Audit `ASSIGNMENT.md` for any residual source-language fragments and transliterations, translate all
of them into ISO/IEC/IEEE 29148 terminology, preserve every variant constraint unaltered, run an
automated non-ASCII verification, and commit.

**Agent execution:** performed the localization sweep, normalized all operators to ASCII, ran the
verification suite, committed
`refactor(assignment-01): ensure 100% pure english canonical specification`.

### Directive 4 -- Documentation and audit trail (this task)

Refactor the root `README.md` into a public-facing academic portfolio overview with no operational or
CLI content; establish the task and prompt audit trail under
`assignments/assignment-01/tasks/`; synchronize the branch with the remote.

**Agent execution:** authored this record and `TASK_TEMPLATE.md`, committed
`docs: refine root readme and establish task audit trail for assignment-01`.

---

## AI Draft Output

| Artifact | Agent disposition | Rationale |
| --- | --- | --- |
| `.gitignore` | Accepted as drafted | Covers all five required categories with no over-broad patterns |
| `README.md` (scaffold) | Modified | Original draft carried an operational note on identity retrieval; removed as internal, see Directive 4 |
| `ASSIGNMENT.md` (compilation) | Modified | Draft normalized the six rubric weights from the Scoring Rubric table; agent recorded the source discrepancy explicitly rather than silently reconciling it |
| `ASSIGNMENT_RAW_VI.md` | Accepted as received | Instructor-issued source, committed unmodified |
| Student identifier literal | Rejected | The source specification embeds a literal student identifier in the filename example. The compiled specification replaced it with a placeholder resolved at submission time, and the identifier was not propagated into `ASSIGNMENT.md`. |

---

## Verified Outputs

### 1. Scaffolding tree

```
d:\SE2026-assignment
├── .gitignore
├── README.md
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
| Student name in any tracked file | 0 occurrences |
| Tracked file inventory | Restricted to documentation and audit artifacts |
| Student identity in version control | None; resolved dynamically at generation time |

`ASSIGNMENT_RAW_VI.md` retains a literal student identifier supplied by the instructor. It is
committed unmodified as the authoritative source record; the identifier was not propagated into any
derived artifact.

### 3. English and standards alignment

| Check | Command class | Result |
| --- | --- | --- |
| Non-ASCII byte sweep | `LC_ALL=C grep '[^ -~]'` | PASS -- zero bytes outside `0x20-0x7E` |
| Source-language diacritic sweep | Targeted character-class regex | PASS -- zero matches |
| Residual source-language fragments | Word-anchored, UTF-8 locale | PASS -- zero matches |
| Legacy Unicode operators and dashes | `grep -oP '[\x{2265}\x{2264}\x{2192}\x{2013}\x{2014}]'` | PASS -- zero occurrences |

Standards conformance: quality attribute scenarios specify all six ISO/IEC/IEEE 29148 components
(source, stimulus, environment, artifact, response, response measure); traceability is expressed as a
four-link chain from outcome through to planned test; operators are expressed in ASCII form.

**Correction recorded during verification.** The first run of the residual-fragment scan returned a
false positive at the *Software Process* section: the character class `b[a\u00e1]n`, evaluated under
a non-UTF-8 locale, collapsed to a byte set and matched the substring `ban` within `Kanban`. The
document was correct; the check was not. The scan was re-run with word anchors and an explicit UTF-8
locale, returning zero matches. Recorded here because a loose character class in the default locale
is a latent defect in any future check of the same kind.

---

## Notes for Subsequent Tasks

- Record every AI-assisted deliverable as a discrete task file under
  `assignments/assignment-01/tasks/`, following `TASK_TEMPLATE.md`.
- Rubric criterion 6 requires a minimum of two corrections or rejections of AI output, each with a
  rationale. TASK-00 already supplies two (identifier propagation, rubric weight reconciliation) that
  may be carried forward into the submission's AI usage appendix.
