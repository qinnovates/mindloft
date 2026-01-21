# ONI Framework Wiki

> **The central connection point for all ONI Framework research, publications, and development.**

**Version:** 1.0
**Last Updated:** 2026-01-21
**Status:** Active Development

---

## Framework Overview

The **Organic Neural Interface (ONI) Framework** extends the OSI networking model into biological neural systems, creating a unified architecture for brain-computer interface security. This wiki connects all research topics, maps dependencies, and provides navigation paths for readers and contributors.

---

## Dependency Map

```
                    ┌─────────────────────────────────────┐
                    │         ONI FRAMEWORK (L1-L14)       │
                    │    The foundational 14-layer model   │
                    └──────────────┬──────────────────────┘
                                   │
            ┌──────────────────────┼──────────────────────┐
            │                      │                      │
            ▼                      ▼                      ▼
   ┌─────────────────┐   ┌─────────────────┐   ┌─────────────────┐
   │ SCALE-FREQUENCY │   │ COHERENCE METRIC│   │  NEURAL FIREWALL│
   │  f × S ≈ k law  │   │ Signal validation│   │  Zero-trust L8  │
   └────────┬────────┘   └────────┬────────┘   └────────┬────────┘
            │                     │                      │
            │                     └──────────┬───────────┘
            │                                │
            │                                ▼
            │                     ┌─────────────────────┐
            │                     │  NEURAL RANSOMWARE  │
            │                     │   Threat modeling   │
            └─────────────────────┴─────────────────────┘
```

**Reading Order (Recommended):**
1. ONI Framework → Foundation concepts
2. Scale-Frequency → Mathematical invariants
3. Coherence Metric → Signal validation
4. Neural Firewall → Security architecture
5. Neural Ransomware → Threat landscape

---

## Topics & Publications

### Core Foundation

| Topic | Purpose | Documents | Status |
|-------|---------|-----------|--------|
| [ONI Framework](MAIN/publications/0-oni-framework/INDEX.md) | 14-layer biological extension of OSI model | [Medium](MAIN/publications/0-oni-framework/Medium-ONI_Framework.md) · [TechDoc](MAIN/publications/0-oni-framework/TechDoc-ONI_Framework.md) | Published |

### Signal Processing

| Topic | Purpose | Documents | Status |
|-------|---------|-----------|--------|
| [Coherence Metric](MAIN/publications/coherence-metric/INDEX.md) | Mathematical framework for signal trust scoring | [Medium](MAIN/publications/coherence-metric/Medium-Coherence_Metric.md) · [TechDoc](MAIN/publications/coherence-metric/TechDoc-Coherence_Metric_Detailed.md) | Published |
| [Scale-Frequency](MAIN/publications/scale-frequency/INDEX.md) | Cross-scale frequency invariants (f × S ≈ k) | [Medium](MAIN/publications/scale-frequency/Medium-Scale_Frequency.md) · [TechDoc](MAIN/publications/scale-frequency/TechDoc-Scale_Frequency.md) | Published |

### Security Architecture

| Topic | Purpose | Documents | Status |
|-------|---------|-----------|--------|
| [Neural Firewall](MAIN/publications/neural-firewall/INDEX.md) | Zero-trust security at the neural gateway (L8) | [Medium](MAIN/publications/neural-firewall/Medium-Neural_Firewall.md) · [TechDoc](MAIN/publications/neural-firewall/TechDoc-Neural_Firewall_Architecture.md) | Published |
| [Neural Ransomware](MAIN/publications/neural-ransomware/INDEX.md) | Threat analysis and defensive architectures | [Medium](MAIN/publications/neural-ransomware/Medium-Neural_Ransomware.md) · [TechDoc](MAIN/publications/neural-ransomware/TechDoc-Neural_Ransomware.md) | Published |

---

## Cross-Reference Matrix

Shows which topics reference which. Use this to understand conceptual dependencies.

|                    | ONI Framework | Coherence | Scale-Freq | Firewall | Ransomware |
|--------------------|:-------------:|:---------:|:----------:|:--------:|:----------:|
| **ONI Framework**  | —             | ●         | ●          | ●        | ●          |
| **Coherence**      | ◄             | —         | ○          | ●        | ●          |
| **Scale-Frequency**| ◄             | ○         | —          | ○        | ○          |
| **Firewall**       | ◄             | ◄         | ○          | —        | ●          |
| **Ransomware**     | ◄             | ◄         | ○          | ◄        | —          |

**Legend:** ● = references this topic | ◄ = referenced by this topic | ○ = related concept

---

## Layer Quick Reference

The ONI Framework extends OSI's 7 layers to 14, bridging silicon and biology:

| Layer | Name | Domain | Function |
|:-----:|------|--------|----------|
| L1 | Molecular | Biology | Ion channels, neurotransmitters |
| L2 | Cellular | Biology | Action potentials, synaptic transmission |
| L3 | Microcircuit | Biology | Local neural computation |
| L4 | Regional | Biology | Brain region specialization |
| L5 | Systems | Biology | Distributed neural networks |
| L6 | Whole-Brain | Biology | Global integration patterns |
| L7 | Behavioral | Biology | Observable outputs, motor commands |
| **L8** | **Neural Gateway** | **Bridge** | **BCI hardware boundary (Firewall lives here)** |
| L9 | Signal Processing | Silicon | Filtering, amplification, digitization |
| L10 | Protocol | Silicon | Data formatting, transmission rules |
| L11 | Transport | Silicon | Reliable data delivery |
| L12 | Session | Silicon | Connection management |
| L13 | Presentation | Silicon | Data interpretation |
| L14 | Application | Silicon | End-user interfaces |

---

## Roadmap: Future Topics

Planned research areas for framework expansion:

| Priority | Topic | Description | Dependencies | Status |
|:--------:|-------|-------------|--------------|--------|
| 1 | Neural Authentication | Identity verification via neural signatures | Coherence, Firewall | Planned |
| 2 | Adversarial Stimulation | Attack vectors through neural feedback | Ransomware, Firewall | Planned |
| 3 | Cross-Device Protocol | Multi-BCI communication standards | ONI L10-L12 | Conceptual |
| 4 | Neural Privacy Framework | Data minimization for neural signals | Coherence, Firewall | Conceptual |
| 5 | Regulatory Mapping | FDA/EU compliance for ONI architecture | All topics | Conceptual |

---

## Adding New Topics

When expanding the framework, follow this process:

### 1. Create Topic Folder
```bash
mkdir MAIN/publications/[topic-name]/
```

### 2. Create Topic INDEX.md
Use the [INDEX template](MAIN/artifacts/templates/INDEX_TEMPLATE.md) with:
- Topic summary
- Dependency list (what this topic builds on)
- Document inventory
- Related topics

### 3. Add Publications
- `Medium-[Topic_Name].md` — Accessible narrative
- `TechDoc-[Topic_Name].md` — Academic depth

### 4. Update This Wiki
- Add topic to appropriate section table
- Update dependency map if needed
- Add to cross-reference matrix

### 5. Update keywords.json
Add keywords for research monitoring integration.

---

## Resources

### Templates
- [TechDoc Template (APA)](MAIN/artifacts/templates/TECHDOC_TEMPLATE_APA.md)
- [Medium Template](MAIN/artifacts/templates/MEDIUM_TEMPLATE.md)
- [Topic INDEX Template](MAIN/artifacts/templates/INDEX_TEMPLATE.md)

### Processes
- [Publishing Instructions](MAIN/artifacts/processes/PUBLISHING_INSTRUCTIONS.md)
- [Process Improvements](MAIN/artifacts/processes/PROCESS_IMPROVEMENTS.md)

### Research Pipeline
- [Keywords Registry](MAIN/artifacts/cicd-pipeline/continuous-research-delivery/scripts/keywords.json)
- [Research Monitor](MAIN/artifacts/cicd-pipeline/continuous-research-delivery/scripts/research_monitor.py)

---

## Metrics

| Metric | Count |
|--------|-------|
| Total Topics | 5 |
| Published Documents | 10 |
| Medium Posts | 5 |
| Technical Documents | 5 |
| Planned Topics | 5 |

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for collaboration guidelines. The ONI Framework welcomes contributions from neuroscience, security, hardware, and ethics disciplines.

---

## License

Apache 2.0 — See [LICENSE](LICENSE)

---

*This wiki is a living document. It evolves as the framework grows.*
