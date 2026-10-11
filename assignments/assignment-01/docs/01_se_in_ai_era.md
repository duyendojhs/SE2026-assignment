# Criterion 1: Software Engineering in the AI Era (Variant RE-027)

## 1. Working Software vs. Reliable Software

Generative AI systems can produce code that compiles, passes unit tests, and even deploys without
immediate errors. In the context of Variant RE-027, this creates a dangerous illusion of readiness.
The operational environment -- 302 concurrent active users, a 20-hour change-request SLA, a 41-day
audit retention mandate, and a Personal-Data-Deletion-on-Request policy -- exposes gaps that
superficial validation cannot detect.

Consider three concrete failure vectors where "working" code diverges from reliable software:

**Race conditions in session invalidation.** An AI-generated deletion pipeline may correctly remove
a user's profile and emit a confirmation event, yet fail to atomically invalidate the user's active
sessions across all 302 concurrent connections. Under peak load, the window between profile removal
and session termination becomes a race: new access requests may be evaluated against stale tokens,
granting access to a logically deleted identity. A passing unit test that mocks the session store
in isolation will not reveal this, because the test harness cannot reproduce the timing
interleavings of 302 concurrent sessions under a revocation storm.

**Incomplete deletion pipelines with residual metadata.** The deletion policy demands
irreversible removal of direct personal identifiers. An AI-generated implementation may correctly
tokenize the primary identity table while leaving foreign-key references, cached query results,
search indexes, or message-queue payloads intact. These residuals constitute direct PII exposure
during the 41-day audit retention period, violating OUTCOME-02. A test suite that asserts "the
user table is clean" will pass while the search index still returns the deleted user's email.

**SLA deadline drift under partial degradation.** The 20-hour response window is absolute. An
AI-generated escalation subsystem may correctly implement priority queues and notification
templates, yet assume reliable network delivery. When the primary alert channel degrades -- a
scenario explicitly modeled in QS-03 -- the system silently queues escalation tasks without
triggering the fallback channel, causing requests to breach the SLA. A test that asserts "an
escalation event is created" will pass while the alert never reaches the Access Administrator.

In each case, the code executes without error. The failure is not a crash or exception; it is a
violation of an operational guarantee that the test suite did not encode. Reliability requires
that every operational constraint of the variant be expressed as a verifiable property and checked
under realistic adversarial conditions -- not merely that the code runs.

---

## 2. Locus of Engineering Responsibility

The ACM Code of Ethics and Professional Conduct (Section 1.2) states: "Computing professionals
should take responsibility for the work they do." The IEEE Code of Ethics similarly holds that
engineers "shall accept responsibility for their decisions and actions." Generative AI alters the
mechanics of production but not the locus of accountability.

When an AI generates a deletion pipeline that leaks PII into an audit log, the legal consequence
falls on the deploying organization and the engineer who signed off on the release. The AI agent
has no legal personhood, no professional license, and no capacity to suffer sanctions. It cannot
be called to testify before a regulator or a court. The engineer who accepts the AI output,
integrates it, and authorizes its deployment is the sole party who can be held accountable for
the system's behavior in production.

This is not a theoretical distinction. Under GDPR Article 24, the controller -- the human-led
organization -- must implement appropriate technical and organizational measures and be able to
demonstrate compliance. An AI-generated artifact without a documented, human-verified assurance
chain does not satisfy this requirement. The engineer's professional duty is to construct that
assurance chain: to specify the required behavior, to verify the implementation against the
specification, and to record the evidence of verification. The AI is a tool in this process,
subject to the same scrutiny as any compiler, linter, or static analyzer.

Responsibility cannot be delegated to the tool. The engineer who uses AI must still:
- Define the precise operational requirements (as done in `03_problem_framing.md`)
- Specify acceptance criteria that capture boundary and failure cases (as done in `04_user_stories.md`)
- Construct quality scenarios with mathematically precise response measures (as done in `05_quality_and_mvp.md`)
- Maintain bidirectional traceability from outcome to test (as done in `TRACEABILITY.md`)
- Document every AI-assisted artifact with its disposition and rationale (as done in every `task_*.md`)

The AI output is a draft. The engineering judgment that accepts, modifies, or rejects it is the
act of engineering. The engineer owns the result.

---

## 3. Systematic AI Failure Modes in Requirements and Code

Empirical studies of large language models in code generation (e.g., Codex, CodeLlama, GPT-4)
consistently reveal three failure modes that are structurally persistent, not incidental bugs.
Each is illustrated with a concrete failure scenario tied to Variant RE-027.

### Mode 1: Semantic Hallucination and Phantom APIs

**Description.** The model invents APIs, standards, endpoints, or compliance frameworks that do
not exist, presenting them with the same confidence as real ones.

**RE-027 Example.** The AI drafts a deletion workflow that calls a `DELETE /api/v1/compliance/gdpr/purge`
endpoint, asserting it is a "standard GDPR compliance API." No such standard endpoint exists.
The AI further references "ISO 27001 Annex A.18.1.4" as mandating a specific tokenization
algorithm, when Annex A.18.1.4 concerns cryptographic key management, not tokenization. The
generated code includes calls to a phantom `TokenizationService.anonymize()` method that does not
exist in any standard library.

**Consequence.** The engineer who integrates this code without verification introduces a runtime
dependency on a non-existent service. The deletion request silently fails, the 20-hour SLA is
breached, and the audit trail records a successful completion that never occurred.

---

### Mode 2: Edge-Case Blindness and Silent Degradation

**Description.** The model optimizes for the nominal path and omits boundary conditions, error
states, and failure modes unless explicitly prompted for each one. Even when prompted, it tends
to produce generic error handling rather than domain-specific boundary logic.

**RE-027 Example.** The AI generates a bulk deletion processor that iterates over queued requests
and tokenizes each user. It omits the case where a request arrives at hour 19.5 of the 20-hour
window (AC-01.2) and the target user has active session dependencies that prevent immediate
tokenization. The generated code either blocks indefinitely, timing out the batch, or skips the
request with a generic "retry later" status -- both of which breach the SLA. It also omits the
case where a dependency deadlock causes a request to age past 20 hours without fulfillment
(AC-01.3), producing no SLA-breach alert.

**Consequence.** The system appears to work under light load with cooperative data. Under the
variant's actual constraints -- 302 concurrent users, late-arrival requests, dependency deadlocks
-- it silently degrades, breaching the SLA without alerting the Access Administrator.

---

### Mode 3: Security and Privacy Blindspots

**Description.** The model defaults to convenient but insecure patterns: string interpolation in
SQL queries, logging full request payloads, storing secrets in configuration files, and
transmitting PII in error messages. It does not instinctively apply data minimization,
tokenization, or least-privilege principles.

**RE-027 Example.** The AI proposes a deletion audit log that records the full deletion request
payload -- including the data subject's email, name, and government ID -- in a structured log
table for "debugging purposes." This log is retained for 41 days per the audit requirement,
directly contradicting the deletion policy. In another instance, the AI generates a SQL query
using string concatenation: `DELETE FROM profiles WHERE email = '${request.email}'`, exposing
an injection vector. In a third, it suggests caching the pre-tokenization profile in Redis with
a TTL of 41 days "for performance," creating a shadow copy of the PII the policy demands be
destroyed.

**Consequence.** The system complies with the audit retention requirement by retaining the very
data the deletion policy requires be eliminated. A compliance audit would find direct PII in the
audit log, the cache, and potentially in error logs -- all generated by AI suggestions the
engineer did not reject.

---

## 4. Rigorous Mitigation Strategies

No single technique suffices. The following layered defenses are required for any AI-assisted
artifact in this variant:

| Layer | Technique | Application to RE-027 |
| --- | --- | --- |
| **Specification** | Formal operational requirements in ISO/IEC/IEEE 29148 form (outcomes, scenarios, traceability) | All three outcomes, four user stories, three quality scenarios, and the traceability matrix are specified without reference to implementation. The AI cannot hallucinate an API that the specification does not reference. |
| **Verification** | Property-based testing with adversarial input generation | Test the deletion pipeline with concurrent session dependencies, late-arrival requests at hour 19.5, and dependency deadlocks. Test the audit store for PII leakage under join attempts. Test the escalation path with degraded channels. |
| **Static Analysis** | Deterministic linters and secret scanners integrated in CI | Rules forbidding string-interpolated SQL, PII in log output, hardcoded secrets, and direct PII in tables with retention > 0 days. |
| **Human Audit Gates** | Independent review of every AI-assisted artifact with recorded disposition | Every task record (`task_00` through `task_05`) documents the AI draft, the human action (Accepted/Modified/Rejected), and the engineering justification. No AI output reaches the submission without this gate. |
| **Traceability Closure** | Bidirectional traceability from outcome to planned test, verified by tooling | `TRACEABILITY.md` links every outcome to user stories, quality scenarios, and test cases. A gap in the matrix is a failed gate. |
| **Execution Validation** | Load testing at the variant's stated parameters (302 concurrent, 41-day retention, 20-hour window) | The MVP validation criteria (VC-01 through VC-04) are executed against the deployed system, not mocks. |

These layers are independent: a failure in one (e.g., the AI hallucinates an API) is caught by
another (the specification does not reference it; the linter flags the undefined import; the
human audit gate rejects the draft). The system is reliable because the assurance chain is
redundant, not because any single layer is perfect.