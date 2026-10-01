# Software Engineering Coursework Portfolio (SE2026)

## Academic Context

This repository is the semester coursework portfolio for **Software Engineering 2026 (SE2026)**. It
collects the specifications, requirement artifacts, and engineering evidence produced for each
assignment of the course.

Work in this portfolio is conducted against two reference standards:

- **ISO/IEC/IEEE 29148** — the standard for requirements engineering. Requirement statements are
  written to be unambiguous, verifiable, and traceable; quality attributes are specified as
  scenarios with an explicit source, stimulus, environment, artifact, response, and response measure.
- **Human-in-the-loop AI engineering** — AI tooling is treated as an unverified contributor rather
  than an author. Every AI-generated artifact passes through documented human review, and each
  disposition (accepted, modified, rejected) is recorded together with its rationale.

## Repository Architecture

```
SE2026-assignment/
├── README.md
├── .gitignore
└── assignments/
    └── assignment-01/
        ├── ASSIGNMENT.md          canonical specification (English)
        ├── ASSIGNMENT_RAW_VI.md   source specification, as issued
        └── tasks/                 task and prompt audit trail
```

Each assignment directory is self-contained: it holds the authoritative specification for that
assignment and an audit trail of the work performed against it.

## Coursework Index

| Assignment | Topic | Status | Specification |
| --- | --- | --- | --- |
| Assignment 01 | Software Engineering in the AI Era (variant RE-027) | In progress | [`assignments/assignment-01/`](assignments/assignment-01/) |
