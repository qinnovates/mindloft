# Code of Conduct

## Our Pledge

Contributors and maintainers commit to creating a harassment-free, ethically grounded environment for all participants — regardless of age, body size, disability, ethnicity, sex characteristics, gender identity and expression, level of experience, education, socio-economic status, nationality, personal appearance, race, religion, sexual identity and orientation, neurodivergence, or cognitive ability.

As a project that develops security standards for brain-computer interfaces, we hold ourselves to an elevated standard: the same principles of cognitive liberty, mental privacy, and human dignity that the QIF framework protects in code, we protect in community.

## Our Standards

### Positive Behaviors

- Using welcoming and inclusive language
- Being respectful of differing viewpoints, experiences, and cognitive styles
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members
- Citing sources and acknowledging uncertainty in technical claims
- Respecting the boundary between security research and harmful application

### Neuroethics Principles

As contributors to a neural security framework, we additionally commit to:

- **Cognitive Liberty** — Respecting every individual's right to mental self-determination. We do not develop, promote, or endorse tools or techniques designed to manipulate, coerce, or override cognitive autonomy without informed consent.
- **Mental Privacy** — Treating neural data as a special category requiring the highest protection. We do not advocate for or contribute to surveillance of mental states without explicit, informed consent.
- **Mental Integrity** — Protecting against unauthorized alteration of neural function. Research into attack vectors is conducted solely for defensive purposes, documented transparently, and subject to responsible disclosure.
- **Psychological Continuity** — Recognizing the right to maintain personal identity. We do not develop capabilities intended to alter personality, memory, or sense of self without clinical justification and informed consent.
- **Cognitive Authenticity** — Upholding the right to know which thoughts are genuinely one's own. Our coherence metrics and security tools exist to protect authenticity, not to undermine it.

These principles are grounded in the framework's [Neuroethics Alignment](MAIN/governance/NEUROETHICS_ALIGNMENT.md) document and align with the [UNESCO Recommendation on the Ethics of Neurotechnology (2025)](MAIN/governance/UNESCO_ALIGNMENT.md).

### Unacceptable Behaviors

- Sexualized language, imagery, or unwelcome sexual advances
- Trolling, insults, derogatory comments, and personal or political attacks
- Public or private harassment
- Publishing others' private information — including but not limited to physical addresses, electronic addresses, or neural data — without explicit permission
- Weaponizing framework knowledge: using QIF security research, attack surface documentation, or threat models to develop offensive capabilities targeting real BCI users
- Misrepresenting framework claims: presenting unverified hypotheses as validated findings, or omitting uncertainty tags from research contributions
- Other conduct that would be inappropriate in a professional or academic setting

## Dual-Use Research Responsibility

The QIF framework documents attack surfaces and threat models for brain-computer interfaces. This information is published openly for defensive purposes — to help device manufacturers, security researchers, and regulators protect neural interfaces.

Contributors must:

1. **Frame offensively** only for defense — Attack research exists to improve defenses. Document mitigations alongside any new threat vectors.
2. **Follow responsible disclosure** — Report vulnerabilities in real BCI devices through the manufacturer's security channels before public discussion. See [SECURITY.md](SECURITY.md).
3. **Acknowledge limitations** — Use the project's [verification protocol](MAIN/legacy-core/resources/agents/RESEARCH_VERIFICATION_PROTOCOL.md) uncertainty tags (Verified, Inferred, Unverified, Hypothesis) to clearly communicate confidence levels.
4. **Consider downstream impact** — Before publishing, consider whether the contribution could disproportionately benefit attackers over defenders. When in doubt, discuss with maintainers first.

## Human-AI Collaboration Transparency

This project uses AI assistance in research and development. Contributors working with AI tools must:

- Disclose AI involvement in significant contributions using `Co-Authored-By` commit tags
- Document human decisions versus AI suggestions in the [Transparency](MAIN/governance/TRANSPARENCY.md) audit trail for major contributions
- Never present AI-generated content as independently verified research without human validation
- Apply the same verification standards to AI-generated claims as to human-generated claims

## Our Responsibilities

Maintainers clarify behavioral standards and take appropriate corrective action. They may remove, edit, or reject contributions misaligned with this Code of Conduct, or temporarily or permanently ban contributors engaged in inappropriate, threatening, offensive, or harmful conduct.

For contributions involving neuroethics-sensitive areas (attack research, neural data handling, cognitive manipulation vectors), maintainers will additionally consult the project's governance documents before accepting changes.

## Scope

This Code of Conduct applies within all project spaces — including issues, pull requests, discussions, and documentation — and when individuals represent the project publicly, such as through official communications, social media, conference presentations, or as appointed representatives at events.

The neuroethics principles in this Code extend to derivative works: if you fork or build upon the QIF framework, we strongly encourage adopting equivalent ethical commitments.

## Enforcement

Report violations to the maintainer via [GitHub Private Vulnerability Reporting](https://github.com/qinnovates/mindloft/security/advisories/new) or through the contact methods listed in [ABOUT.md](ABOUT.md). All complaints will be reviewed and investigated promptly and fairly, with reporter confidentiality maintained.

Maintainers who do not follow or enforce this Code of Conduct in good faith may face temporary or permanent repercussions as determined by the project leadership.

## Attribution

This Code of Conduct adapts the [Contributor Covenant v1.4](https://www.contributor-covenant.org/version/1/4/code-of-conduct.html), extended with neuroethics principles derived from:

- Ienca, M., & Andorno, R. (2017). Towards new human rights in the age of neuroscience and neurotechnology. *Life Sciences, Society and Policy*, 13(1), 5.
- Yuste, R., Goering, S., et al. (2017). Four ethical priorities for neurotechnologies and AI. *Nature*, 551(7679), 159-163.
- UNESCO. (2025). *Recommendation on the Ethics of Neurotechnology*.

---

*Version 1.0 — Last Updated: 2026-02-05*
