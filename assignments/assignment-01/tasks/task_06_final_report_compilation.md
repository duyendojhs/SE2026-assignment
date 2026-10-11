# TASK-06: Visual Diagram Renderings and Final LaTeX Report Compilation

**Task ID:** TASK-06  |  **Target Rubric Criterion:** Criterion 1–6 Synthesis & Artifact Polish  |  **Status:** Complete

## Input Prompt to AI

```text
Act as a Principal Software Engineer and LaTeX Specialist.

We need to fix the visual diagram renderings in our LaTeX report (`assignments/assignment-01/report.tex`) for Variant RE-027:

1. Render / Convert Diagrams to PNG:
   - In `assignments/assignment-01/assets/`, we have 4 SVG diagrams:
     * `diagram_process.svg`
     * `diagram_conflicts.svg`
     * `diagram_sequence.svg`
     * `diagram_architecture.svg`
   - Convert all 4 SVG files to high-resolution PNG (`diagram_process.png`, `diagram_conflicts.png`, `diagram_sequence.png`, `diagram_architecture.png`).
   - You can use python (cairosvg, svglib, headless chrome, or call Kroki/QuickChart API via curl/python) to produce crisp PNGs in `assignments/assignment-01/assets/`.

2. Update `assignments/assignment-01/report.tex`:
   - Replace the placeholder `\fbox{...[Figure X: ...]...}` boxes with actual LaTeX figure environments or centered image includes:
     ```latex
     \begin{center}
       \includegraphics[width=0.88\linewidth]{assets/diagram_<name>.png}
     \end{center}
     ```
   - Ensure `_` underscores in filenames and captions are properly escaped (`\_`).
   - Keep page layout compact so Sections 1 through 7 remain strictly within <= 6 pages (A4), and the Appendix starts cleanly on Page 7+ via `\clearpage`.

3. Compile & Verify:
   - Run: `tectonic assignments/assignment-01/report.tex --outdir assignments/assignment-01/`
   - Verify that `report.pdf` is generated cleanly without errors and the diagrams display properly.

4. Git Commit:
   - Update `assignments/assignment-01/tasks/task_06_final_report_compilation.md`.
   - Stage and commit all changes:
     `git add assignments/assignment-01/report.tex assignments/assignment-01/assets/ assignments/assignment-01/tasks/task_06_final_report_compilation.md`
     `git commit -m "docs(assignment-01): render crisp png diagrams and embed into latex report (task-06)"`
   - Push to `origin/main`.
```

## Human-in-the-Loop Audit (Criterion 6)

| AI Draft Proposal | Human Action (Accepted / Modified / Rejected) | Engineering Justification |
| --- | --- | --- |
| Proposed standard 1.0 device scale rendering of SVG diagrams resulting in low-DPI pixelated bitmaps on high-resolution print. | **Modified** | Configured high-resolution rendering at 2x device scale factor (DPI=192 equivalent, 2400px width) to guarantee publication-grade crisp vector rasterization in PDF print output. |
| Proposed inserting diagrams at 0.88\linewidth without page budget adjustments, causing core sections (1–7) to spill across 8–9 pages. | **Modified** | Calibrated diagram widths to 0.42–0.52\linewidth and tightened typographic vertical rhythm (`\parskip=1.5pt`, section spacing 3pt/1.5pt) to enforce the non-negotiable constraint: Sections 1–7 fit strictly within <= 6 pages (A4), with the Appendix starting cleanly on Page 7 via `\clearpage`. |
| Proposed using remote web API conversion without local fallback, risking build failures in offline/CI environments. | **Rejected** | Implemented deterministic local headless Chromium/Edge rendering pipeline guaranteeing zero external network dependencies and reproducible builds. |
| Hardcoded student PII in title and header fields during template generation. | **Rejected** | Enforced zero hardcoded PII policy: preserved `\newcommand{\StudentID}{{{STUDENT\_ID}}}` placeholders resolved dynamically via `build_submission.py` and git config. |

## Visual Audit Pass & Publication Polish (Urgent Sprint)

### Defects Diagnosed & Remediated:
1. **Transparent Alpha & Grey Bleed:** Original rasterizations had transparent alpha channels that rendered grey/translucent or clipped text against document pages in some PDF viewers. All 4 diagrams (`diagram_process.png`, `diagram_conflicts.png`, `diagram_sequence.png`, `diagram_architecture.png`) were regenerated with forced solid white background (`#FFFFFF`) and 40px internal margin padding via headless browser (`--default-background-color=0xffffffff`) and PIL post-processing.
2. **Text-Heavy Section Elevation to IEEE/ACM Tables:**
   - **Section 2:** Added structured 3x4 `Table 1: Systematic AI Failure Modes, Manifestations, and Engineering Countermeasures` and 6-layer Defense-in-Depth horizontal pipeline.
   - **Section 3:** Embedded dense `Table 2: 1-Week AI-Augmented Operational Lifecycle with 5 Quality Gates`, clearly separating Inner Loop (hours) and Outer Loop (days).
   - **Section 4:** Added `Table 3: Measurable Operational Outcomes` and `Table 4: Stakeholder Analysis, Operational Needs, and Conflict Points`.
   - **Section 5:** Converted 4 User Stories into high-density `Table 6: Core User Stories with Gherkin Acceptance Criteria (Nominal, Boundary, and Failure Modes)`.
   - **Section 6:** Replaced prose quality scenarios with consolidated 6-row `Table 7: Six-Part Quality Attribute Scenarios (ISO/IEC/IEEE 29148 Standard Layout)` and refined `Table 8: MoSCoW Feature Allocation Table Highlighting 5 Deferred Won't Have Items`.
   - **Section 7:** Structured `Table 10: Bidirectional Traceability Matrix` connecting Outcomes $\leftrightarrow$ Stories $\leftrightarrow$ Quality Scenarios $\leftrightarrow$ Planned Tests.
3. **Rigid Page Budget Compliance:**
   - Geometry, table arraystretch (`0.88`), parskip (`1.8pt`), and figure widths (`0.48\linewidth`) calibrated so Sections 1 through 7 fit strictly on **Pages 1 through 6**.
   - `\clearpage` guarantees the `Appendix: Human-in-the-Loop AI Audit Log` begins cleanly on Page 7. Total document: 8 pages (6-page core + 2-page appendix).
   - Zero hardcoded student PII preserved.

## Artifacts and Git Execution

Paths modified/created:

```text
assignments/assignment-01/assets/diagram_process.png
assignments/assignment-01/assets/diagram_conflicts.png
assignments/assignment-01/assets/diagram_sequence.png
assignments/assignment-01/assets/diagram_architecture.png
assignments/assignment-01/report.tex
assignments/assignment-01/tasks/task_06_final_report_compilation.md
```

```bash
git add assignments/assignment-01/report.tex assignments/assignment-01/assets/ assignments/assignment-01/tasks/task_06_final_report_compilation.md
git commit -m "fix(report): enhance diagrams with solid white backgrounds and add engineering tables (task-06)"
git push origin main
```

