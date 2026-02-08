# AI Transparency Log

> **Living record of every AI system used in the development, validation, and refinement of the QIF ecosystem.**
>
> **Purpose:** Full transparency about which AI systems contributed what, when, and in what role. This enables peer reviewers, collaborators, and the public to understand exactly where human reasoning ends and AI assistance begins — and where AI systems checked each other's work.
>
> **Policy:** Every AI interaction that materially affects QIF documents, code, or conclusions MUST be logged here. This includes both commercial and open-source models.
>
> **Started:** 2026-02-07
> **Maintainer:** Kevin Qi (Qinnovate)

---

## 1. AI Systems Registry

### Commercial Models (Safety-Filtered / Restricted Team)

| System | Provider | Model ID | Access Method | Primary Role |
|--------|----------|----------|---------------|--------------|
| **Claude Opus 4.6** | Anthropic | claude-opus-4-6 | Claude Code CLI | Primary author, implementation, coordination, code |
| **Gemini 2.5 Pro** | Google | gemini-2.5-pro | Gemini CLI (`gemini`) | Independent peer reviewer, cross-document consistency |
| **Grok 3 Mini** | xAI | x-ai/grok-3-mini-beta | OpenRouter API | Independent reviewer, scientific rigor, alternative perspective |

### Open-Source / Unrestricted Models (Unrestricted Team)

| System | Provider | Model ID | Access Method | Primary Role |
|--------|----------|----------|---------------|--------------|
| **DeepSeek-R1-0528** | DeepSeek | deepseek/deepseek-r1-0528:free | OpenRouter API | Adversarial security review, math verification |
| **QwQ-32B** | Alibaba/Qwen | qwen/qwq-32b | OpenRouter API | Mathematical physics verification, bounds checking |
| **WhiteRabbitNeo V3** | WhiteRabbitNeo | WhiteRabbitNeo-V3-7B | Local (GGUF, planned) | Cybersecurity specialist, exploit chain analysis |

### Validation Protocol

**For every major review cycle, BOTH teams are consulted:**

1. **Restricted Team** (Gemini + Grok + Claude): Consistency checking, scientific framing, academic rigor
2. **Unrestricted Team** (DeepSeek-R1 + QwQ-32B + WhiteRabbitNeo): Adversarial security, unfiltered critique, exploit feasibility
3. **Synthesis:** Claude coordinates findings from all models, Kevin makes final decisions

### Why Multiple AI Systems?

1. **Counteracting confirmation bias:** The primary author (Claude) may have systematic blind spots. Independent AI reviewers catch what the author misses.
2. **Safety filter circumvention:** Commercial AI models sometimes hedge on security analysis. Unrestricted models provide unfiltered adversarial feedback.
3. **Specialization:** Each model excels in different domains (Gemini: consistency; DeepSeek-R1: reasoning; QwQ: math; WhiteRabbitNeo: cybersecurity).
4. **Pre-human-review quality gate:** AI reviewers catch mechanical errors (inconsistent numbers, stale references, equation bugs) so human reviewers can focus on genuinely novel critique.

---

## 2. Contribution Timeline

### 2026-02-02 — Framework Genesis

| AI System | Contribution | Artifacts Affected |
|-----------|-------------|-------------------|
| Claude Opus 4.6 | Derived QIF v3.0/3.1 hourglass model (Entries 1-15) | QIF-TRUTH.md, QIF-DERIVATION-LOG.md |
| Claude Opus 4.6 | Implemented equations in qif_equations.py | qif-lab/src/qif_equations.py |
| Claude Opus 4.6 | Implemented synthetic data generators | qif-lab/src/synthetic_data.py |

### 2026-02-03 — Whitepaper v3.1

| AI System | Contribution | Artifacts Affected |
|-----------|-------------|-------------------|
| Claude Opus 4.6 | Drafted QIF-WHITEPAPER-v3.1.md | QIF-WHITEPAPER.md |
| Gemini 2.5 Pro | **First independent review** — identified 7 corrections (Entry 16): Q(c) mislabeled, Moore's Law error, tunneling gating error, Ht normalization needed, L=v/f unification, candidate equations unified, Dsf log-scale | QIF-WHITEPAPER.md, QIF-TRUTH.md |

### 2026-02-06 — v4.0 Architecture + NSP + Attack Taxonomy

| AI System | Contribution | Artifacts Affected |
|-----------|-------------|-------------------|
| Claude Opus 4.6 | Derived v4.0 (11-band) architecture (Entry 33-34) | config.py, QIF-DERIVATION-LOG.md |
| Claude Opus 4.6 | Drafted NSP-PROTOCOL-SPEC.md (full RFC-style spec) | NSP-PROTOCOL-SPEC.md |
| Claude Opus 4.6 | Unified 60-technique threat taxonomy (Entry 37-38) | config.py, threat-registry.json |
| Claude Opus 4.6 | Derived Black Hole Security Principle (Entry 35) | QIF-WHITEPAPER-v5.md |
| Gemini 2.5 Pro | Reviewed Black Hole Principle — reframed as "conceptual analogy, not formal equivalence" | QIF-WHITEPAPER-v5.md §8 |

### 2026-02-06 — Project Runemate

| AI System | Contribution | Artifacts Affected |
|-----------|-------------|-------------------|
| Claude Opus 4.6 | Drafted RUNEMATE.md specification | RUNEMATE.md |
| Claude Opus 4.6 | Implemented staves_compiler.py PoC | staves_compiler.py |

### 2026-02-07 — Runemate Three-Pass Review + NSP Number Unification (Entry 39)

| AI System | Contribution | Artifacts Affected |
|-----------|-------------|-------------------|
| Gemini 2.5 Pro | **Pass 1:** Identified 8 gaps (layout engine, OP_STYLE_REF, interactivity, media, security, edge cases, no_std, CSS) | RUNEMATE.md, staves_compiler.py |
| Claude Opus 4.6 | Fixed all 8 Pass 1 gaps | RUNEMATE.md, staves_compiler.py |
| Gemini 2.5 Pro | **Pass 2:** Upgraded to A-. Identified 4 new gaps (delta updates, state management, error display, conformance testing) | RUNEMATE.md |
| Claude Opus 4.6 | Fixed all 4 Pass 2 gaps | RUNEMATE.md |
| Gemini 2.5 Pro | **Pass 3:** With full ecosystem context, identified 6 cross-document inconsistencies (PQC numbers, band mapping, gateway, complexity, side channels, firmware) | RUNEMATE.md, QIF-WHITEPAPER-v5.md, NSP-PROTOCOL-SPEC.md |
| Claude Opus 4.6 | Computed canonical PQC numbers from NSP message struct definitions (21,117 B PQ handshake) | All documents |
| Claude Opus 4.6 | Fixed all 6 Pass 3 gaps including QIF band mapping and gateway threat model | RUNEMATE.md, runemate-constants.ts, staves_compiler.py |

### 2026-02-07 — Unrestricted AI Validation Team Established (Entry 40)

| AI System | Contribution | Artifacts Affected |
|-----------|-------------|-------------------|
| Claude Opus 4.6 | Researched best open-source unrestricted models | AI-TRANSPARENCY.md |
| Gemini 2.5 Pro | Cross-validated open model recommendations | QIF-DERIVATION-LOG.md |
| Claude Opus 4.6 | Propagated v4.0 architecture to ALL documents | QIF-TRUTH.md, QIF-WHITEPAPER-v5.md, NSP-PROTOCOL-SPEC.md, RUNEMATE.md |
| Gemini 2.5 Pro | **v4.0 review:** Found 5 remaining issues (abstract tunneling gating, §2.3 "7-band", NSP Band IDs, NSP parameters, calibration weights) | All documents |
| Claude Opus 4.6 | Fixed all 5 Gemini v4.0 issues | All documents |
| DeepSeek-R1-0528 | **First adversarial review** — sent focused NSP attack surface payload (~15KB). Response timed out on free tier. | Pending retry |
| QwQ-32B | **First math review** — sent QIF equations (~15KB). Found 3 issues: deprecated σ²τ in coherence equation, wrong units in f×S table, missing weights in Σq equation. All fixed. | QIF-TRUTH.md |

### 2026-02-07 — First Multi-Model Validation Cycle Completed (Entry 41)

| AI System | Contribution | Artifacts Affected |
|-----------|-------------|-------------------|
| Grok-3 Mini (xAI) | **Cross-document consistency review** — Found stale v3.1 band list in NSP §1 Terminology. Grade: C (1 real issue + 1 false positive on whitepaper versioning) | NSP-PROTOCOL-SPEC.md |
| Claude Opus 4.6 | Fixed NSP §1 Terminology: "seven bands N3-S3" → "eleven bands N7-S3" | NSP-PROTOCOL-SPEC.md |
| Gemini 2.5 Pro | **Re-review confirming 5 previous fixes** — All 5 Gemini round 2 fixes verified correct. Found 2 new minor issues: timestamp wrap behavior undocumented, QI Components field lacks quantum anomaly bits. 1 false positive (Σq "missing" — only partial payload was sent). Grade: C | NSP-PROTOCOL-SPEC.md |
| Claude Opus 4.6 | Fixed NSP timestamp wrap documentation and QI Components quantum terms note | NSP-PROTOCOL-SPEC.md |
| QwQ-32B (Alibaba/Qwen) | **First math/physics verification** — Graded whitepaper §5.5 quantum terms A (correct). Found 3 issues in QIF-TRUTH.md: (1) coherence equation uses deprecated σ²τ instead of Hτ, (2) f×S table units "m·Hz" should be "m/s", (3) Σq equation missing weights ψ₁,ψ₂,ψ₃ and negative sign on Q̂e. Grade: C for QIF-TRUTH equations section | QIF-TRUTH.md |
| Claude Opus 4.6 | Fixed all 3 QwQ-32B issues + updated band index list in §4.1, corrections table in §4.7 | QIF-TRUTH.md |
| DeepSeek-R1-0528 | **Adversarial security review attempted** — Focused NSP payload sent via OpenRouter API. Response timed out on free tier. | No artifacts |

---

## 3. Human vs. AI Decision Authority

**Kevin Qi (human) makes ALL architectural decisions.** AI systems propose, analyze, and critique — but the human decides.

Key examples:
- **v4.0 architecture:** Claude proposed the 7-1-3 expansion. Kevin confirmed.
- **MITRE-compatible format:** Kevin directed. Claude implemented.
- **Unrestricted model team:** Kevin directed. Claude researched and set up.
- **Black Hole Principle reframing:** Gemini critiqued. Kevin accepted the critique and directed the reframing.
- **PQC number unification:** Gemini identified the inconsistency. Claude computed the fix. Kevin approved.

---

## 4. Limitations and Disclosure

1. **AI-generated content:** The majority of prose in QIF documents was drafted by Claude Opus 4.6, based on Kevin's direction, research, and decisions.
2. **AI review is not peer review:** Gemini, DeepSeek, and QwQ provide valuable feedback but are NOT substitutes for human domain experts. They catch mechanical errors; they cannot assess genuine scientific novelty.
3. **Confirmation bias risk:** Despite using multiple AI systems, they all operate on the same training data distributions and may share systematic blind spots.
4. **No AI system has physical intuition.** Physics claims are validated against published literature, not AI "understanding."
5. **The validation pipeline converges, not certifies.** When all AI reviewers agree on A+, it means "no further mechanical issues found" — not "this is correct."

---

*Document version: 1.1*
*Created: 2026-02-07*
*Last updated: 2026-02-07*
*Location: qinnovates/mindloft/drafts/ai-working/AI-TRANSPARENCY.md*
