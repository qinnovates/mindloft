# Process Improvement Strategy for ONI Framework Publishing

## Current State Analysis

### What's Working
1. **Clear folder structure** - Topic-based organization with `MAIN/publications/` and `MAIN/resources/` separation
2. **Naming conventions** - Consistent `Blog-*` and `TechDoc-*` patterns across all 14 publications
3. **Templates exist** - APA TechDoc, Blog, and INDEX templates provide comprehensive formatting guidance
4. **CLAUDE.md** - Comprehensive AI instructions with file trees, workflows, and quality checklists
5. **MAIN/INDEX.md** - Cross-reference registry with dependency maps, publication matrix, and metrics
6. **Research Pipeline** - Automated research monitoring via `keywords.json` and `research_monitor.py`
7. **YAML front-matter** - Implemented on all publications with title, date, URL, and tags
8. **Topic INDEX.md files** - All 8 topic folders have INDEX.md with dependencies, key concepts, and future work
9. **APA formatting** - Technical documents follow APA 7th edition with proper citations and acknowledgments

### Gaps Identified
1. ~~No automated validation of file naming~~ → Checklist documented, automation pending
2. ~~README.md updates are manual and error-prone~~ → Process documented in CLAUDE.md
3. ~~No version tracking for individual documents~~ → Partial (front-matter on publications)
4. ~~Cross-references between papers not systematically maintained~~ → **RESOLVED: MAIN/INDEX.md**
5. ~~INDEX.md only deployed to 1 of 5 topic folders~~ → **RESOLVED: All 8 folders have INDEX.md**
6. No content calendar or publishing schedule tracking
7. No CHANGELOG.md at repository root
8. No automated docx generation workflow (currently manual pandoc commands)

---

## Recommended Improvements

### 1. Pre-Commit Checklist Automation

Create a checklist that Claude runs through before every commit:

```markdown
## Pre-Commit Verification

### File Naming
- [ ] All blog posts match `Blog-[Topic_Name].md`
- [ ] All papers match `TechDoc-[Topic_Name].md`
- [ ] Folder names are lowercase-hyphenated
- [ ] INDEX.md exists in topic folder

### Content Quality
- [ ] APA formatting on TechDocs (author, abstract, keywords, numbered sections)
- [ ] References are APA formatted with DOIs where available
- [ ] Acknowledgments section included (TechDocs)
- [ ] Front matter complete (Blog posts)
- [ ] Related Articles section included (Blog posts)

### Repository Updates
- [ ] MAIN/INDEX.md Quick Navigation updated
- [ ] MAIN/INDEX.md Reading Order updated
- [ ] MAIN/INDEX.md Dependency Map updated
- [ ] MAIN/INDEX.md Cross-Reference Matrix updated
- [ ] MAIN/INDEX.md Metrics updated
- [ ] Topic INDEX.md created/updated
- [ ] docx files regenerated via pandoc
```

### 2. Document Metadata Standard

Add consistent metadata to all documents:

```yaml
---
# Required for all documents
title: ""
type: "Blog" | "TechDoc" | "Template" | "Instructions"
topic: ""  # Maps to folder name
version: "1.0"
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"

# For Blog posts
url: ""
tags: []

# For TechDocs
keywords: []
abstract: ""
---
```

### 3. Cross-Reference Registry

Maintained in MAIN/INDEX.md. Current state (as of January 2026):

| Document | References | Referenced By |
|----------|------------|---------------|
| ONI Framework | - | All other papers |
| Coherence Metric | ONI Framework | Neural Firewall, Neural Ransomware, Quantum Encryption |
| Scale-Frequency | ONI Framework | Quantum Encryption |
| Neural Firewall | ONI Framework, Coherence Metric | Neural Ransomware |
| Neural Ransomware | ONI Framework, Coherence Metric, Neural Firewall | - |
| Quantum Encryption | ONI Framework, Scale-Frequency, Coherence Metric | - |

### 4. Version Changelog

Create `CHANGELOG.md` at repository root:

```markdown
# Changelog

## [2026-01-22]
### Added
- Tunneling Traversal Time publication (Blog + TechDoc)
- Topic INDEX.md for tunneling-traversal-time
- Quantum Security TechDoc

### Changed
- Updated MAIN/INDEX.md with new publication (metrics now 7 topics, 13 docs)
- Cross-reference matrix expanded to include TTT

## [2026-01-21]
### Added
- MAIN/INDEX.md as central navigation hub
- INDEX_TEMPLATE.md for topic folders
- Quantum Security Blog post

### Changed
- Reorganized into MAIN/publications structure
- Renamed files from Medium-* to Blog-* convention
- Updated all topic INDEX.md files

### Removed
- medium_template_v2.py (consolidated into BLOG_TEMPLATE.md)
```

### 5. Publishing Workflow States

Track content through stages:

```
Research → Draft → Review → Formatted → Committed → Published
```

For each document, track:
- Current state
- Last update date
- Medium URL (if published)
- Any pending updates needed

---

## Template Inventory

### Current Templates
| Template | Purpose | Location | Status |
|----------|---------|----------|--------|
| TECHDOC_TEMPLATE_APA.md | Technical papers (APA 7th) | MAIN/resources/templates/ | Active |
| BLOG_TEMPLATE.md | Blog posts (Medium-optimized) | MAIN/resources/templates/ | Active |
| INDEX_TEMPLATE.md | Topic folder indexes | MAIN/resources/templates/ | Active |
| PUBLISHING_INSTRUCTIONS.md | Workflow guide | MAIN/resources/processes/ | Active |

### Deprecated Templates
| Template | Reason | Replaced By |
|----------|--------|-------------|
| medium_template_v2.py | Consolidated | BLOG_TEMPLATE.md |
| MEDIUM_TEMPLATE.md | Renamed | BLOG_TEMPLATE.md |

### Proposed Additional Templates

#### 1. Research Note Template (NOT YET IMPLEMENTED)
For shorter, less formal research notes that may become papers later:

```markdown
# Research Note: [Topic]

**Date:** YYYY-MM-DD
**Status:** Draft | In Review | Archived
**Related Papers:** [links]

## Key Insight

[1-2 paragraph summary]

## Supporting Evidence

[Bullet points or short sections]

## Questions for Further Research

- [ ] Question 1
- [ ] Question 2

## Raw Notes

[Unstructured notes, quotes, references]
```

#### 2. Topic Index Template — IMPLEMENTED
Template exists at `MAIN/resources/templates/INDEX_TEMPLATE.md`. **Deployed to all 7 topic folders.**

---

## Automation Opportunities

### 1. INDEX.md Auto-Update Script

Logic for Claude to follow after each content addition:

1. Scan `MAIN/publications/*/` for all markdown files
2. Count total documents (Blog + TechDoc per folder)
3. Update MAIN/INDEX.md metrics section
4. Verify all links in Quick Navigation section are valid
5. Update dependency map if new topic added

### 2. File Naming Validator

Before commit, verify:
```
- Blog posts: /^Blog-[A-Z][a-zA-Z_]+\.md$/
- TechDocs: /^TechDoc-[A-Z][a-zA-Z_]+\.md$/
- Folders: /^[a-z]+(-[a-z]+)*$/
- Required files per folder: INDEX.md, Blog-*.md, TechDoc-*.md
```

### 3. Cross-Reference Checker

After editing any paper:
1. Extract all internal references (links to other ONI papers)
2. Verify referenced documents exist
3. Check if referenced documents need updates for consistency

### 4. Docx Generation Automation

After each markdown update:
```bash
cd MAIN/publications/[topic]/
pandoc Blog-*.md -o Blog-*.docx
pandoc TechDoc-*.md -o TechDoc-*.docx
```

---

## Current File Tree (Implemented)

```
ONI/
├── README.md
├── CLAUDE.md                       # AI instructions
├── ABOUT.md
├── CHANGELOG.md                    # PENDING
├── CONTRIBUTING.md
├── LICENSE
│
└── MAIN/
    ├── INDEX.md                     # Central navigation hub
    │
    ├── resources/
    │   ├── templates/
    │   │   ├── TECHDOC_TEMPLATE_APA.md
    │   │   ├── BLOG_TEMPLATE.md
    │   │   └── INDEX_TEMPLATE.md
    │   ├── processes/
    │   │   ├── PUBLISHING_INSTRUCTIONS.md
    │   │   └── PROCESS_IMPROVEMENTS.md   # This file
    │   └── pipeline/
    │       ├── scripts/
    │       │   ├── keywords.json
    │       │   └── research_monitor.py
    │       ├── incoming/
    │       └── processed/
    │
    ├── publications/
    │   ├── 0-oni-framework/
    │   │   ├── INDEX.md              # COMPLETE
    │   │   ├── Blog-ONI_Framework.md
    │   │   └── TechDoc-ONI_Framework.md
    │   │
    │   ├── coherence-metric/
    │   │   ├── INDEX.md              # COMPLETE
    │   │   ├── Blog-Coherence_Metric.md
    │   │   └── TechDoc-Coherence_Metric_Detailed.md
    │   │
    │   ├── neural-firewall/
    │   │   ├── INDEX.md              # COMPLETE
    │   │   ├── Blog-Neural_Firewall.md
    │   │   └── TechDoc-Neural_Firewall_Architecture.md
    │   │
    │   ├── neural-ransomware/
    │   │   ├── INDEX.md              # COMPLETE
    │   │   ├── Blog-Neural_Ransomware.md
    │   │   └── TechDoc-Neural_Ransomware.md
    │   │
    │   ├── scale-frequency/
    │   │   ├── INDEX.md              # COMPLETE
    │   │   ├── Blog-Scale_Frequency.md
    │   │   └── TechDoc-Scale_Frequency.md
    │   │
    │   └── quantum-encryption/        # Consolidated quantum topics
    │       ├── INDEX.md              # COMPLETE
    │       ├── Blog-Quantum_Security.md
    │       ├── Blog-Quantum_Keys.md
    │       ├── Blog-Tunneling_Traversal_Time.md
    │       ├── TechDoc-Quantum_Encryption.md
    │       └── TechDoc-Tunneling_Traversal_Time.md
    │
    └── oni-visualizations/
        └── README.md
```

---

## Implementation Priority

### Phase 1 (Immediate) — COMPLETE
- [x] Create CLAUDE.md (comprehensive AI instructions)
- [x] Create BLOG_TEMPLATE.md (v2 with style guide)
- [x] Standardize file naming (`Blog-*` and `TechDoc-*` patterns)
- [x] Update all file trees in documentation
- [x] Create INDEX_TEMPLATE.md
- [x] Deploy INDEX.md to all topic folders (8 of 8 complete)
- [x] Create MAIN/INDEX.md with dependency map and cross-reference matrix

### Phase 2 (Next Session) — IN PROGRESS
- [ ] Create CHANGELOG.md at repository root
- [ ] Create Research Note template file
- [ ] Add docx generation to standard workflow documentation
- [ ] Verify all topic INDEX.md files have consistent formatting

### Phase 3 (Future)
- [x] Build cross-reference registry → **MAIN/INDEX.md**
- [x] Document pre-commit checklist → **In CLAUDE.md**
- [ ] Automate pre-commit checklist as `.git/hooks/pre-commit`
- [x] Add document metadata to publications → **YAML front-matter on all 13 publications**
- [ ] Add consistent metadata to infrastructure files (templates, processes)
- [ ] Implement content calendar for publishing schedule tracking
- [ ] Create automated docx generation script

---

## Metrics Summary

| Metric | Count | Last Updated |
|--------|-------|--------------|
| Total Topics | 6 | 2026-01-22 |
| Published Documents | 14 | 2026-01-22 |
| Blog Posts | 8 | 2026-01-22 |
| Technical Documents | 6 | 2026-01-22 |
| Topic INDEX.md Files | 6 | 2026-01-22 |
| Prototypes | 1 | 2026-01-21 |
| Templates | 3 | 2026-01-21 |
| Planned Topics | 5 | 2026-01-21 |

---

## Next Steps (Recommended Actions)

### Immediate Priority
1. **Create CHANGELOG.md** at repository root with semantic versioning history
2. **Verify docx files** exist for all publications (currently only tunneling-traversal-time has them)

### Short-Term
3. **Create Research Note template** as `MAIN/resources/templates/RESEARCH_NOTE_TEMPLATE.md`
4. **Add YAML metadata** to all infrastructure files in `resources/`
5. **Generate docx files** for all publications using pandoc

### Medium-Term
6. **Create pre-commit hook** (`.git/hooks/pre-commit`) to automate validation
7. **Implement content calendar** for publishing schedule tracking
8. **Create docx generation script** to automate Word document creation

---

## Recent Additions Log

### 2026-01-22 (oni-framework release)
- **oni-framework Python package v0.1.0** released:
  - `oni.coherence` - Cₛ calculation with phase, transport, gain variance
  - `oni.layers` - 14-layer ONI model with attack surfaces and defenses
  - `oni.firewall` - Zero-trust Neural Firewall with decision matrix
  - `oni.scale_freq` - Scale-Frequency Invariant (f × S ≈ k) validation
  - 77 unit tests, all passing
  - Published to PyPI: `pip install oni-framework`
  - GitHub Release: v0.1.0
  - GitHub Actions CI/CD for tests and publishing
- **All documentation updated:**
  - README.md: Added Python Library section with quick start
  - MAIN/INDEX.md: Added oni-framework section with module table
  - CLAUDE.md: Updated file tree with oni-framework structure
  - Repository structure diagrams updated throughout

### 2026-01-22 (continued)
- **Quantum Keys** publication added:
  - Blog post converted from .pages file (Nobel Prize QKD topic)
  - INDEX.md with dependencies, key concepts, timeline projections
  - Keywords extracted and added to keywords.json
- **MAIN/INDEX.md** updated with:
  - Quantum Keys entry in Quick Navigation
  - Step 8 in Reading Order
  - Expanded Dependency Map (QKeys alongside TTT under Quantum Security)
  - QKeys row/column in Cross-Reference Matrix (8x8)
  - Updated folder structure
  - Metrics updated (8 topics, 14 documents, 8 blogs)
- **README.md** updated with:
  - Quantum Keys section in Topics & Documents
  - Tunneling Traversal Time section in Topics & Documents
  - Repository Structure updated with new folders
  - Footer metrics updated
- **CLAUDE.md** file tree updated with quantum-keys and tunneling-traversal-time folders

### 2026-01-22
- **Tunneling Traversal Time** publication added:
  - TechDoc with APA 7th edition formatting
  - Blog post with template-compliant structure
  - INDEX.md with dependencies, key concepts, threat model
  - docx files generated for both documents
- **MAIN/INDEX.md** updated with:
  - New entry in Quick Navigation
  - Step 7 in Reading Order
  - Expanded Dependency Map (TTT under Quantum Security)
  - TTT row/column in Cross-Reference Matrix
  - Updated folder structure
  - Metrics updated (7 topics, 13 documents)

### 2026-01-21
- Quantum Security publication added
- MAIN folder restructure completed
- All topic INDEX.md files deployed
- Blog/TechDoc naming convention standardized

---

## Adoption Strategy

### Current Strengths (Adoption Value)

| Asset | Value |
|-------|-------|
| 14-layer ONI model | Novel conceptual framework bridging OSI to biology |
| Cₛ coherence formula | Concrete, implementable metric |
| f × S ≈ k invariant | Testable mathematical claim |
| Threat models | Actionable security architecture |
| Documentation quality | Low barrier to understanding |

### Critical Gaps for Adoption

| Gap | Issue | Impact |
|-----|-------|--------|
| No empirical validation | All theory, no experimental data | Low credibility |
| No reference implementation | No working code | Nothing to use today |
| No industry touchpoints | No BCI manufacturer engagement | No pathway to deployment |
| No peer review | Self-published only | Lacks academic credibility |
| No community | Single-author project | No momentum |

### Adoption Roadmap

#### Phase 1: Credibility (1-3 months)
- [ ] Validate Cₛ formula against public BCI dataset (BCI Competition)
- [ ] Submit one paper to peer-reviewed venue (Journal of Neural Engineering, Frontiers)
- [x] Create working Python package `oni-framework` ✓ **COMPLETED v0.1.0**
- [ ] Post preprint to arXiv (cs.CR or q-bio.NC)

#### Phase 2: Visibility (3-6 months)
- [ ] Conference presentation (IEEE EMBS, BCI Meeting)
- [ ] Whitepaper targeting BCI manufacturers
- [ ] Engage 2-3 academic collaborators
- [ ] Cross-post on r/neuralengineering, r/netsec, Hacker News

#### Phase 3: Industry Adoption (6-12 months)
- [ ] Reference implementation with full documentation
- [ ] Integration guide for BCI manufacturers
- [ ] Regulatory alignment document (FDA, EU MDR)
- [ ] FDA pre-submission meeting request

### High-Impact Actions (Prioritized)

| Action | Effort | Impact | Status |
|--------|--------|--------|--------|
| Validate Cₛ on BCI Competition data | Medium | High | Pending |
| ~~Python package `oni-framework`~~ | ~~Medium~~ | ~~High~~ | **DONE v0.1.0** |
| arXiv preprint of TechDoc-ONI_Framework | Low | Medium | Pending |
| FDA pre-submission meeting request | Low | High | Pending |
| Neuralink security researcher outreach | Low | Variable | Pending |

### Target Stakeholders

| Stakeholder | What They Need | How ONI Helps |
|-------------|----------------|---------------|
| BCI manufacturers | Security architecture guidance | 14-layer model, firewall design |
| Neuroscience researchers | Validated metrics | Cₛ formula, f × S ≈ k |
| Security engineers | Threat models, attack surfaces | Neural ransomware, quantum security |
| Regulators (FDA, EU) | Compliance frameworks | Layer-based risk assessment |
| Ethics boards | Governance frameworks | Human sovereignty principles |

### Python Package Specification (`oni-framework`)

**Core Modules:**
```
oni/
├── __init__.py
├── coherence.py      # Cₛ calculation (phase, transport, gain variance)
├── layers.py         # 14-layer model representation
├── firewall.py       # Signal filtering simulation
├── threats.py        # Threat model definitions
├── scale_freq.py     # f × S ≈ k invariant calculations
└── visualize.py      # Layer diagrams, coherence plots
```

**MVP Features:**
1. `oni.coherence.calculate_cs(signal_data)` → Cₛ score (0-1)
2. `oni.layers.ONIStack()` → 14-layer model object
3. `oni.firewall.NeuralFirewall(threshold)` → Filter signals by Cₛ
4. `oni.visualize.layer_diagram()` → ASCII/matplotlib layer viz

**Target:** Installable via `pip install oni-framework`

---

*Strategy Version: 3.3*
*Last Updated: January 22, 2026*
*Author: Kevin L. Qi with Claude (Anthropic)*
