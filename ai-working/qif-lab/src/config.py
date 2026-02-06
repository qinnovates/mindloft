"""
QIF Configuration — Single source of truth for all constants, thresholds, and metadata.

As-Code Principle: Every value used in the whitepaper, equations, or visualizations
is defined HERE. Nothing is hardcoded in documents.
"""

# ──────────────────────────────────────────────
# Framework Identity
# ──────────────────────────────────────────────

FRAMEWORK = {
    "name": "QIF — Quantum Indeterministic Framework for Neural Security",
    "pronunciation": "CHIEF",
    "predecessor": "ONI (Organic Neural Interface)",
    "layer_model_version": "v4.0 (Hourglass, 11-band, 7-1-3)",
    "layer_model_date": "2026-02-06",
    "github": "qinnovates/qinnovate",
    "authors": "Kevin Qi, with Claude (Anthropic)",
    "collaboration": "Quantum Intelligence (QI)",
    "ai_transparency": {
        "statement": "This framework was developed collaboratively between Kevin Qi (human researcher) and AI assistants. All AI involvement is assistive — Kevin retains authorship and all decision-making authority.",
        "ai_systems": [
            {"name": "Claude (Opus 4.5)", "role": "Co-derivation, implementation, research agent orchestration", "provider": "Anthropic"},
            {"name": "Gemini 2.5", "role": "Independent peer review (cross-AI validation)", "provider": "Google"},
        ],
        "audit_trail": "QIF-DERIVATION-LOG.md",
        "audit_trail_description": "Complete chronological record of every derivation, decision, AI contribution, and validation result — with timestamps, reasoning chains, and source attribution.",
        "research_sources": "QIF-RESEARCH-SOURCES.md",
    },
}

# ──────────────────────────────────────────────
# Layer Architecture — v4.0 Hourglass Model
# ──────────────────────────────────────────────
# 3 Zones, 11 Bands (7-1-3). No OSI heritage.
# Numbers increase AWAY from the interface in both directions.
# Width = state space / possibility space (hourglass geometry).
#
# Version history:
#   v2.0 (14-layer) DEPRECATED → v3.0 (7-band, 3-1-3)
#   v3.0 → v3.1: Dropped N4 (Identity/Consciousness merged into N3)
#   v3.1 → v4.0: Neural domain expanded 3 → 7 bands (N1-N7)
#     - Each N band has distinct clinical severity, frequency profile, and L range
#     - v3.1 N1 (Subcortical Relay) split into N1 Spinal, N2 Brainstem, N4 Diencephalon, N5 Basal Ganglia
#     - v3.1 N2 (Sensorimotor) split: cortices stay in N7, cerebellum → N3
#     - v3.1 N3 (Integrative) split: neocortex → N7, limbic → N6
#     - Silicon domain unchanged (S1-S3). I0 unchanged.
#   See Derivation Log Entries 24, 25, 33.

ZONES = {
    "neural": {
        "name": "Neural Domain",
        "description": "Biological processing from spinal cord to neocortex — 7 bands, severity-stratified",
        "color": "#3fb950",  # green
        "bands": ["N7", "N6", "N5", "N4", "N3", "N2", "N1"],
    },
    "interface": {
        "name": "Interface Zone",
        "description": "Quasi-quantum bottleneck: electrode-tissue boundary, measurement/collapse",
        "color": "#f85149",  # red
        "bands": ["I0"],
    },
    "silicon": {
        "name": "Silicon Domain",
        "description": "Classical: analog front-end through digital processing to application/wireless",
        "color": "#58a6ff",  # blue
        "bands": ["S1", "S2", "S3"],
    },
}

BANDS = [
    # ── NEURAL DOMAIN (7 bands, N7 outermost → N1 closest to periphery) ──
    {
        "id": "N7", "name": "Neocortex", "zone": "neural",
        "description": "PFC, M1, S1, V1, A1, Broca, Wernicke, association cortex — executive function, language, movement, perception",
        "brain_regions": ["PFC", "ACC", "Broca", "Wernicke", "M1", "S1_cortex", "V1", "A1", "PMC", "SMA", "PPC"],
        "dominant_freq_hz": "13-100 (Beta 13-30, Gamma 30-100)",
        "L_m": (0.04, 0.3),       # 4 cm to 30 cm
        "determinacy": "Quantum Uncertain",
        "severity": "High",
        "severity_description": "Cognitive impairment, motor paralysis, sensory loss, language disruption",
        "qi_range": (0.3, 0.5),
        "hourglass_width": 1.0,    # widest in neural domain
        "bci_devices": ["Neuralink N1", "Blackrock Utah Array", "Precision Layer 7", "ECoG grids", "cortical DBS"],
    },
    {
        "id": "N6", "name": "Limbic System", "zone": "neural",
        "description": "Hippocampus, amygdala, insula, ACC, cingulate — emotion, memory, interoception",
        "brain_regions": ["HIPP", "BLA", "insula", "ACC", "CeA", "cingulate"],
        "dominant_freq_hz": "4-13 (Theta 4-8, Alpha 8-13)",
        "L_m": (0.3, 1.0),        # 30 cm to 1 m
        "determinacy": "Chaotic → Quantum Uncertain",
        "severity": "High",
        "severity_description": "Memory erasure, emotional dysregulation, PTSD trigger, addiction manipulation",
        "qi_range": (0.2, 0.4),
        "hourglass_width": 0.85,
        "bci_devices": ["NeuroPace RNS (depth)", "DBS (ANT target)", "depth electrodes"],
    },
    {
        "id": "N5", "name": "Basal Ganglia", "zone": "neural",
        "description": "Striatum, GPi/GPe, STN, substantia nigra — motor selection, reward, habit",
        "brain_regions": ["striatum", "GPi", "GPe", "STN", "substantia_nigra"],
        "dominant_freq_hz": "13-30 (Beta — pathological oscillations in Parkinson's)",
        "L_m": (0.13, 0.3),       # 13 cm to 30 cm
        "determinacy": "Chaotic",
        "severity": "High",
        "severity_description": "Movement disorders (Parkinson's, dystonia), reward hijacking, compulsive behavior",
        "qi_range": (0.15, 0.35),
        "hourglass_width": 0.65,
        "bci_devices": ["Medtronic Percept (STN)", "Abbott Infinity (GPi)", "Boston Scientific Vercise"],
    },
    {
        "id": "N4", "name": "Diencephalon", "zone": "neural",
        "description": "Thalamus, hypothalamus — sensory gating, consciousness relay, autonomic regulation",
        "brain_regions": ["thalamus", "hypothalamus", "VIM", "ANT", "CM-Pf"],
        "dominant_freq_hz": "4-13 (Alpha spindles, Theta)",
        "L_m": (0.3, 1.0),        # 30 cm to 1 m
        "determinacy": "Stochastic → Chaotic",
        "severity": "CRITICAL",
        "severity_description": "Consciousness disruption, sensory blackout, sleep-wake cycle attack, thermal regulation failure",
        "qi_range": (0.1, 0.3),
        "hourglass_width": 0.5,
        "bci_devices": ["DBS (VIM for tremor)", "thalamic depth electrodes", "ANT stimulation for epilepsy"],
    },
    {
        "id": "N3", "name": "Cerebellum", "zone": "neural",
        "description": "Cerebellar cortex, deep nuclei, vermis — motor coordination, timing, learning",
        "brain_regions": ["cerebellar_cortex", "dentate_nucleus", "fastigial_nucleus", "vermis"],
        "dominant_freq_hz": "50-100 (Purkinje cell complex spikes)",
        "L_m": (0.04, 0.08),      # 4 cm to 8 cm
        "determinacy": "Stochastic",
        "severity": "High",
        "severity_description": "Ataxia, coordination loss, speech disruption (dysarthria), motor learning impairment",
        "qi_range": (0.1, 0.25),
        "hourglass_width": 0.45,
        "bci_devices": ["Experimental cerebellar stimulation"],
    },
    {
        "id": "N2", "name": "Brainstem", "zone": "neural",
        "description": "Medulla, pons, midbrain, cranial nerve nuclei — vital functions, arousal, reflexes",
        "brain_regions": ["medulla", "pons", "midbrain", "reticular_formation", "cranial_nuclei"],
        "dominant_freq_hz": "0.5-4 (Delta, low-frequency rhythmic)",
        "L_m": (1.0, None),       # >1 m (very slow propagation, long wavelength)
        "determinacy": "Stochastic",
        "severity": "LETHAL",
        "severity_description": "Respiratory arrest, cardiac failure, loss of consciousness, cranial nerve paralysis",
        "qi_range": (0.05, 0.15),
        "hourglass_width": 0.3,
        "bci_devices": ["Vagus nerve stimulators", "auditory brainstem implants", "DBS (PPN for gait)"],
    },
    {
        "id": "N1", "name": "Spinal Cord", "zone": "neural",
        "description": "Cervical, thoracic, lumbar, sacral, cauda equina — reflexes, peripheral motor/sensory relay",
        "brain_regions": ["cervical_cord", "thoracic_cord", "lumbar_cord", "sacral_cord", "cauda_equina"],
        "dominant_freq_hz": "Reflex arcs (ms-scale, not oscillatory)",
        "L_m": None,              # Not oscillatory — variable reflex arc length
        "determinacy": "Stochastic",
        "severity": "Severe",
        "severity_description": "Paralysis (quadri/para), bladder/bowel dysfunction, chronic pain, autonomic dysreflexia",
        "qi_range": (0.02, 0.1),
        "hourglass_width": 0.25,
        "bci_devices": ["Spinal cord stimulators (SCS)", "InterStim (sacral)", "epidural stimulation", "ONWARD ARC-IM"],
    },
    # ── INTERFACE ZONE ──
    {
        "id": "I0", "name": "Neural Interface", "zone": "interface",
        "description": "Electrode-tissue boundary, measurement/collapse, quasi-quantum zone",
        "brain_regions": [],
        "dominant_freq_hz": "N/A (boundary, not oscillatory)",
        "L_m": None,              # Boundary — spatial scale depends on electrode geometry
        "determinacy": "Quasi-quantum (ΓD ∈ (0,1))",
        "severity": "Depends on adjacent N band",
        "severity_description": "Interface degradation, impedance failure, tissue damage, signal corruption",
        "qi_range": (0.01, 0.1),
        "hourglass_width": 0.2,   # narrowest — bottleneck
        "bci_devices": ["All implanted/semi-invasive BCIs"],
    },
    # ── SILICON DOMAIN (3 bands, S1 closest to I0 → S3 outermost) ──
    {
        "id": "S1", "name": "Analog / Near-Field", "zone": "silicon",
        "description": "Amplification, filtering, ADC/DAC, near-field EM (0 Hz – 10 kHz)",
        "brain_regions": [],
        "dominant_freq_hz": "0-10,000 (analog front-end passband)",
        "L_m": (3e4, None),       # 30 km+ in air (ELF/VLF) — chip-internal is copper velocity
        "determinacy": "Stochastic (analog noise)",
        "severity": "N/A (silicon)",
        "severity_description": "Signal corruption, ADC saturation, impedance artifact",
        "qi_range": (0.001, 0.01),
        "hourglass_width": 0.35,
        "bci_devices": ["All BCIs (analog front-end is universal)"],
    },
    {
        "id": "S2", "name": "Digital / Telemetry", "zone": "silicon",
        "description": "Decoding, classification, telemetry, MICS (10 kHz – 1 GHz)",
        "brain_regions": [],
        "dominant_freq_hz": "10,000-1,000,000,000 (digital processing + telemetry)",
        "L_m": (0.3, 3e4),       # 30 cm to 30 km in air
        "determinacy": "Deterministic",
        "severity": "N/A (silicon)",
        "severity_description": "Data corruption, BLE exploit, MICS intermodulation, firmware compromise",
        "qi_range": (0.0, 0.0),
        "hourglass_width": 0.7,
        "bci_devices": ["All wireless BCIs (BLE, WiFi, MICS)"],
    },
    {
        "id": "S3", "name": "Radio / Wireless / DE", "zone": "silicon",
        "description": "RF, wireless links, directed energy, application layer (1 GHz+)",
        "brain_regions": [],
        "dominant_freq_hz": "1,000,000,000+ (GHz+ RF and beyond)",
        "L_m": (3e-5, 0.3),      # 30 μm to 30 cm in air
        "determinacy": "Deterministic",
        "severity": "N/A (silicon)",
        "severity_description": "RF hijack, directed energy, cloud compromise, supply chain attack",
        "qi_range": (0.0, 0.0),
        "hourglass_width": 1.0,   # widest in silicon domain
        "bci_devices": ["BLE/WiFi consumer, satellite links, DE weapons"],
    },
]

# Quick lookup: band_id → band dict
BANDS_BY_ID = {b["id"]: b for b in BANDS}

# ──────────────────────────────────────────────
# Brain Region → Band Mapping
# ──────────────────────────────────────────────

BRAIN_REGION_MAP = {
    # N7 — Neocortex (executive, language, motor, sensory, association)
    "PFC":                {"band": "N7", "connections": ["Broca", "Wernicke", "HIPP", "BLA", "insula", "M1", "PMC", "SMA", "PPC", "STN", "thalamus", "ACC"]},
    "ACC":                {"band": "N7", "connections": ["PFC", "BLA", "insula", "medulla"]},
    "Broca":              {"band": "N7", "connections": ["Wernicke", "PFC"]},
    "Wernicke":           {"band": "N7", "connections": ["A1", "Broca", "PFC"]},
    "M1":                 {"band": "N7", "connections": ["PFC", "PMC", "SMA", "STN", "cerebellar_cortex"]},
    "S1_cortex":          {"band": "N7", "connections": ["thalamus", "PFC", "insula"],
                           "note": "Primary somatosensory cortex (renamed to avoid collision with S1 band)"},
    "V1":                 {"band": "N7", "connections": ["thalamus", "PPC"]},
    "A1":                 {"band": "N7", "connections": ["thalamus", "Wernicke"]},
    "PMC":                {"band": "N7", "connections": ["PFC", "M1"]},
    "SMA":                {"band": "N7", "connections": ["PFC", "M1"]},
    "PPC":                {"band": "N7", "connections": ["V1", "M1", "PMC", "PFC"]},
    # N6 — Limbic System (emotion, memory, interoception)
    "HIPP":               {"band": "N6", "connections": ["BLA", "thalamus", "PFC"]},
    "BLA":                {"band": "N6", "connections": ["HIPP", "PFC", "insula", "CeA"],
                           "note": "Basolateral amygdala — cortical-like, associative learning"},
    "insula":             {"band": "N6", "connections": ["ACC", "BLA", "PFC", "S1_cortex"]},
    "CeA":                {"band": "N6", "connections": ["BLA", "medulla", "thalamus"],
                           "note": "Central amygdala — autonomic output, but limbic origin"},
    "cingulate":          {"band": "N6", "connections": ["PFC", "ACC", "HIPP"]},
    # N5 — Basal Ganglia (motor selection, reward, habit)
    "striatum":           {"band": "N5", "connections": ["PFC", "M1", "GPi", "GPe"]},
    "GPi":                {"band": "N5", "connections": ["striatum", "thalamus"],
                           "note": "Globus pallidus interna — primary output nucleus"},
    "GPe":                {"band": "N5", "connections": ["striatum", "STN"]},
    "STN":                {"band": "N5", "connections": ["GPe", "GPi", "M1"],
                           "note": "Subthalamic nucleus — #1 DBS target for Parkinson's"},
    "substantia_nigra":   {"band": "N5", "connections": ["striatum", "thalamus"],
                           "note": "Dopamine source — degeneration = Parkinson's"},
    # N4 — Diencephalon (sensory gating, consciousness relay, autonomic regulation)
    "thalamus":           {"band": "N4", "connections": ["V1", "A1", "S1_cortex", "PFC", "HIPP", "GPi"]},
    "hypothalamus":       {"band": "N4", "connections": ["thalamus", "medulla", "CeA"],
                           "note": "Autonomic master regulator — temperature, hunger, circadian"},
    "VIM":                {"band": "N4", "connections": ["thalamus", "cerebellar_cortex"],
                           "note": "Ventral intermediate nucleus — DBS target for essential tremor"},
    "ANT":                {"band": "N4", "connections": ["thalamus", "HIPP"],
                           "note": "Anterior nucleus of thalamus — DBS target for epilepsy"},
    # N3 — Cerebellum (motor coordination, timing, learning)
    "cerebellar_cortex":  {"band": "N3", "connections": ["M1", "thalamus", "PFC", "PMC", "dentate_nucleus"]},
    "dentate_nucleus":    {"band": "N3", "connections": ["cerebellar_cortex", "thalamus"]},
    "fastigial_nucleus":  {"band": "N3", "connections": ["cerebellar_cortex", "medulla"]},
    "vermis":             {"band": "N3", "connections": ["cerebellar_cortex"]},
    # N2 — Brainstem (vital functions, arousal, reflexes)
    "medulla":            {"band": "N2", "connections": ["thalamus", "cerebellar_cortex", "CeA", "spinal_cord"],
                           "note": "Contains respiratory and cardiovascular centers — compromise is LETHAL"},
    "pons":               {"band": "N2", "connections": ["medulla", "cerebellar_cortex", "thalamus"]},
    "midbrain":           {"band": "N2", "connections": ["thalamus", "substantia_nigra", "pons"]},
    "reticular_formation":{"band": "N2", "connections": ["thalamus", "medulla", "pons"],
                           "note": "Ascending arousal system — attack = loss of consciousness"},
    # N1 — Spinal Cord (reflexes, peripheral relay)
    "cervical_cord":      {"band": "N1", "connections": ["medulla", "thoracic_cord"],
                           "note": "C1-C8 — upper limbs, diaphragm (C3-C5)"},
    "thoracic_cord":      {"band": "N1", "connections": ["cervical_cord", "lumbar_cord"]},
    "lumbar_cord":        {"band": "N1", "connections": ["thoracic_cord", "sacral_cord"],
                           "note": "L1-L5 — lower limbs"},
    "sacral_cord":        {"band": "N1", "connections": ["lumbar_cord"],
                           "note": "S1-S5 — bladder, bowel, sexual function. InterStim target."},
    "cauda_equina":       {"band": "N1", "connections": ["lumbar_cord", "sacral_cord"]},
}

# Legacy compatibility — map old v3.1 band names to new regions
BRAIN_REGION_V31_COMPAT = {
    "basal ganglia": "STN",           # Old N1 → now N5 (STN is most common reference)
    "cerebellum": "cerebellar_cortex", # Old N1/N2 → now N3
    "brainstem": "medulla",           # Old N1 → now N2
}

# ──────────────────────────────────────────────
# Determinacy Spectrum (5 levels, mapped to bands)
# ──────────────────────────────────────────────

DETERMINACY_SPECTRUM = [
    {"level": 1, "name": "Deterministic",         "bands": ["S2", "S3"],           "description": "f(state,t) → next_state, no randomness"},
    {"level": 2, "name": "Stochastic",            "bands": ["S1", "N1", "N2", "N3"], "description": "Known probability distributions, epistemic randomness"},
    {"level": 3, "name": "Stochastic → Chaotic",  "bands": ["N4"],                 "description": "Thalamic gating transitions between stochastic relay and chaotic oscillation"},
    {"level": 4, "name": "Chaotic",               "bands": ["N5"],                 "description": "Deterministic but sensitive to initial conditions (λ_L > 0). Pathological beta oscillations."},
    {"level": 5, "name": "Chaotic → QU",          "bands": ["N6"],                 "description": "Limbic system spans chaotic dynamics to quantum-uncertain territory at synaptic scale"},
    {"level": 6, "name": "Quantum Uncertain",     "bands": ["N7"],                 "description": "Heisenberg-bounded, security-relevant indeterminacy at cortical synapses"},
]
# Note: Level 7 "Quantum Indeterminate" reserved for future — if electron quantum effects
# in cortical microtubules are proven (Penrose-Hameroff), N7 determinacy would shift to this level.
# Currently defensible at "Quantum Uncertain" without claiming quantum dominance.

# ──────────────────────────────────────────────
# v2.0 → v3.0 Migration Map
# ──────────────────────────────────────────────

V2_TO_V3_MIGRATION = {
    "L1":  "S3",   # Physical medium → Application (classical networking)
    "L2":  "S3",   # Data Link → Application
    "L3":  "S3",   # Network → Application
    "L4":  "S3",   # Transport → Application
    "L5":  "S3",   # Session → Application
    "L6":  "S3",   # Presentation → Application
    "L7":  "S3",   # Application → Application
    "L8":  "I0",   # Neural Gateway → Neural Interface
    "L9":  "I0/N1",  # Signal Processing → Interface / Subcortical
    "L10": "N1/N2",  # Neural Protocol → Subcortical / Sensorimotor
    "L11": "N2",   # Cognitive Transport → Sensorimotor Processing
    "L12": "N3",   # Cognitive Session → Cognitive Integration
    "L13": "N3",   # Semantic Layer → Cognitive Integration
    "L14": "N3",   # Identity Layer → Integrative Association (merged)
}

# DEPRECATED v2.0 — kept for migration reference only. Do NOT use in new code.
LAYERS_V2_DEPRECATED = [
    {"layer": 1,  "name": "Physical",           "domain": "OSI",    "description": "Physical medium, cabling"},
    {"layer": 2,  "name": "Data Link",           "domain": "OSI",    "description": "MAC addressing, framing"},
    {"layer": 3,  "name": "Network",             "domain": "OSI",    "description": "IP routing, addressing"},
    {"layer": 4,  "name": "Transport",           "domain": "OSI",    "description": "TCP/UDP, flow control"},
    {"layer": 5,  "name": "Session",             "domain": "OSI",    "description": "Connection management"},
    {"layer": 6,  "name": "Presentation",        "domain": "OSI",    "description": "Encryption, formatting"},
    {"layer": 7,  "name": "Application",         "domain": "OSI",    "description": "User-facing protocols"},
    {"layer": 8,  "name": "Neural Gateway",      "domain": "Neural", "description": "Firewall, trust boundary between silicon and biology"},
    {"layer": 9,  "name": "Signal Processing",   "domain": "Neural", "description": "Raw signal conditioning, phase coherence checking"},
    {"layer": 10, "name": "Neural Protocol",      "domain": "Neural", "description": "Oscillatory encoding, synchronization"},
    {"layer": 11, "name": "Cognitive Transport",   "domain": "Neural", "description": "Reliable neural data delivery"},
    {"layer": 12, "name": "Cognitive Session",     "domain": "Neural", "description": "Context, working memory"},
    {"layer": 13, "name": "Semantic Layer",        "domain": "Neural", "description": "Intent, goals, meaning"},
    {"layer": 14, "name": "Identity Layer",        "domain": "Neural", "description": "Agency, sense of self"},
]

# ──────────────────────────────────────────────
# v3.1 → v4.0 Migration Map
# ──────────────────────────────────────────────

V3_TO_V4_MIGRATION = {
    # v3.1 band → v4.0 band(s)
    "N3_v31": ["N7", "N6"],   # Integrative Association → Neocortex + Limbic
    "N2_v31": ["N7", "N5", "N3"],  # Sensorimotor → cortices stay N7, BG → N5, cerebellum → N3
    "N1_v31": ["N4", "N2", "N1"],  # Subcortical Relay → Diencephalon + Brainstem + Spinal
    "I0":     ["I0"],         # Unchanged
    "S1":     ["S1"],         # Unchanged — frequency registry adds internal granularity
    "S2":     ["S2"],         # Unchanged
    "S3":     ["S3"],         # Unchanged
}

# ──────────────────────────────────────────────
# Coherence Metric Thresholds
# ──────────────────────────────────────────────

COHERENCE_THRESHOLDS = {
    "high": 0.6,
    "low": 0.3,
}

DECISION_MATRIX = [
    {"coherence": "High (Cₛ > 0.6)",          "auth": "Valid",   "action": "ACCEPT"},
    {"coherence": "High (Cₛ > 0.6)",          "auth": "Invalid", "action": "REJECT + ALERT"},
    {"coherence": "Medium (0.3 < Cₛ < 0.6)",  "auth": "Valid",   "action": "ACCEPT + FLAG"},
    {"coherence": "Medium (0.3 < Cₛ < 0.6)",  "auth": "Invalid", "action": "REJECT + ALERT"},
    {"coherence": "Low (Cₛ < 0.3)",           "auth": "Any",     "action": "REJECT + CRITICAL"},
]

# ──────────────────────────────────────────────
# Scale-Frequency Data
# ──────────────────────────────────────────────

FREQUENCY_BANDS = [
    {"band": "High gamma", "freq_range": "60-100 Hz", "freq_mid": 80,   "spatial_extent": "0.3-5 mm",    "spatial_mid_m": 0.0025,  "fxs": "~0.08-0.4",  "source": "Jia et al. 2011"},
    {"band": "Low gamma",  "freq_range": "30-60 Hz",  "freq_mid": 45,   "spatial_extent": "1-10 mm",     "spatial_mid_m": 0.005,   "fxs": "~0.04-0.4",  "source": "ECoG studies"},
    {"band": "Alpha",      "freq_range": "8-12 Hz",   "freq_mid": 10,   "spatial_extent": "10-20 cm",    "spatial_mid_m": 0.15,    "fxs": "1-2",        "source": "Srinivasan 1999"},
    {"band": "Theta",      "freq_range": "4-8 Hz",    "freq_mid": 6,    "spatial_extent": "4-5 cm",      "spatial_mid_m": 0.045,   "fxs": "0.24-0.40",  "source": "Patel et al. 2012"},
    {"band": "Delta",      "freq_range": "0.5-4 Hz",  "freq_mid": 2,    "spatial_extent": "15-20 cm",    "spatial_mid_m": 0.175,   "fxs": "0.15-0.20",  "source": "Massimini 2004"},
]

CONDUCTION_VELOCITIES = [
    {"fiber_type": "Unmyelinated intracortical", "velocity": "0.1-0.5 m/s"},
    {"fiber_type": "Myelinated corticocortical", "velocity": "5-30 m/s"},
    {"fiber_type": "Nunez canonical model",      "velocity": "~7 m/s"},
]

BRAIN_MAX_DIMENSION_CM = 20  # Human brain max ~15-20 cm
BRAIN_MAX_DIMENSION_M = 0.20  # Same, in meters (for equations)

# ──────────────────────────────────────────────
# Unified Wave Equation: L = v / f
# ──────────────────────────────────────────────
# One equation for the entire framework. L is the length of one wave
# in its medium. v is the propagation velocity. f is frequency.
# Previously used λ (silicon) and S (neural) — unified into L.
# See Derivation Log Entry 28.

WAVE_EQUATION = {
    "equation": "L = v / f",
    "L": "Length of one wave in its medium (meters)",
    "v": "Propagation velocity in the medium (m/s)",
    "f": "Frequency (Hz)",
    "note": "λ and S are deprecated symbols. Use L everywhere.",
}

PROPAGATION_VELOCITIES = {
    "neural_unmyelinated":  {"v_m_s": 0.5,     "range": "0.5-2",       "medium": "C-fibers, unmyelinated axons"},
    "neural_myelinated":    {"v_m_s": 4.0,     "range": "4-120",       "medium": "A-fibers, myelinated axons (saltatory conduction)"},
    "neural_nunez":         {"v_m_s": 7.0,     "range": "~7",          "medium": "Nunez canonical model for corticocortical"},
    "copper_trace":         {"v_m_s": 2.0e8,   "range": "~2×10⁸",     "medium": "PCB trace, chip interconnect"},
    "free_space":           {"v_m_s": 3.0e8,   "range": "3×10⁸",      "medium": "RF, wireless, directed energy"},
    "ultrasound_tissue":    {"v_m_s": 1540.0,  "range": "~1540",      "medium": "Acoustic in soft tissue (not EM — separate vector)"},
}

# ──────────────────────────────────────────────
# Silicon Frequency Registry — Full Spectrum
# ──────────────────────────────────────────────
# Every known frequency allocation within S1, S2, S3 — including
# government-restricted bands. When a restricted band goes public
# (DARPA→internet precedent), flip the access flag.
# L values calculated via L = c / f (v = 3×10⁸ m/s in air).
# See Derivation Log Entry 28.

ACCESS_LEVELS = {
    "PUBLIC":     {"who": "Anyone",                   "power": "Milliwatts",         "examples": "ISM bands, WiFi, BLE"},
    "LICENSED":   {"who": "Telecom, medical, broadcast", "power": "Watts",           "examples": "MICS, cellular, TV broadcast"},
    "RESTRICTED": {"who": "Government, military",     "power": "Kilowatts",          "examples": "ELF, UHF-Mil, radar bands"},
    "CLASSIFIED":  {"who": "Nation-state military/intel", "power": "Kilowatts-Megawatts, pulsed, focused", "examples": "Directed energy, EW systems"},
}

# Attack coupling mechanisms — how a signal at f_attack reaches neural tissue at f_neural
ATTACK_COUPLING_MECHANISMS = [
    {
        "id": "DIRECT",
        "name": "Direct Frequency Match",
        "formula": "f_attack = f_neural",
        "coupling_strength": "Strongest",
        "description": "Attack frequency is already at the neural target frequency. Walks through I0.",
    },
    {
        "id": "HARMONIC",
        "name": "Harmonic Coupling",
        "formula": "f_attack = n × f_neural (super) or f_neural / n (sub)",
        "coupling_strength": "∝ 1/n²",
        "description": "Neural tissue is nonlinear — generates harmonics. Higher n = weaker coupling.",
    },
    {
        "id": "ENVELOPE",
        "name": "Envelope Modulation",
        "formula": "Carrier at f_carrier, modulated at f_mod. Tissue responds to f_mod.",
        "coupling_strength": "∝ modulation depth",
        "description": "Stealth attack. High-frequency carrier hides low-frequency neural-range modulation. tACS principle.",
    },
    {
        "id": "TEMPORAL_INTERFERENCE",
        "name": "Temporal Interference",
        "formula": "f_beat = |f₁ - f₂|. Tissue at intersection responds to f_beat.",
        "coupling_strength": "Strong at focal point",
        "description": "Two kHz+ signals create neural-range beat frequency. Can target deep brain structures. Grossman et al. 2017, Cell.",
    },
    {
        "id": "INTERMODULATION",
        "name": "Intermodulation (BCI as weapon)",
        "formula": "f_attack = f_neural - f_BCI. Attack + BCI's own signal mix in nonlinear tissue.",
        "coupling_strength": "Variable — depends on BCI signal power",
        "description": "Most dangerous. Attacker's signal mixes with BCI's therapeutic/telemetry signal. BCI becomes part of the attack chain. Attack frequency can be inside normal operating range.",
    },
]

# Full frequency registry per silicon band.
# Each entry: allocation name, frequency range, L range (in air), access level,
# coupling mechanisms to neural domain, target N layers, notes.

SILICON_FREQUENCY_REGISTRY = {
    "S1": {
        "band_name": "Analog / Near-Field",
        "freq_range": "0 Hz – 10 kHz",
        "v": 3.0e8,  # speed of light for RF; chip-internal uses copper v
        "allocations": [
            {
                "name": "ELF (Extremely Low Frequency)",
                "freq_hz": (3, 76),
                "L_m": (3.9e6, 1.0e8),  # 3,900 km to 100,000 km in air
                "access": "RESTRICTED",
                "coupling": ["DIRECT"],
                "target_N": ["N7", "N6", "N4"],
                "notes": "US Navy submarine comms (76 Hz Clam Lake, 45 Hz Republic). IS neural frequency. Penetrates everything on Earth. Direct gamma/alpha/theta entrainment.",
                "historical": "Operational 1989-2004 (US). Russia, China maintain similar capability.",
            },
            {
                "name": "SLF (Super Low Frequency)",
                "freq_hz": (30, 300),
                "L_m": (1.0e6, 1.0e7),
                "access": "RESTRICTED",
                "coupling": ["DIRECT"],
                "target_N": ["N7", "N3", "N5"],
                "notes": "Overlaps high-gamma and DBS therapeutic range (130 Hz). Direct motor coordination and cognitive binding disruption.",
            },
            {
                "name": "ULF (Ultra Low Frequency)",
                "freq_hz": (300, 3000),
                "L_m": (1.0e5, 1.0e6),
                "access": "RESTRICTED",
                "coupling": ["HARMONIC"],
                "target_N": ["N1", "N2", "N3", "N4", "N5", "N6", "N7"],
                "notes": "Cochlear frequency range. Direct attack vector for auditory BCIs. Subharmonics reach any neural band.",
            },
            {
                "name": "VLF (Very Low Frequency)",
                "freq_hz": (3000, 30000),
                "L_m": (1.0e4, 1.0e5),
                "access": "RESTRICTED",
                "coupling": ["ENVELOPE"],
                "target_N": ["N1", "N2", "N3", "N4", "N5", "N6", "N7"],
                "notes": "Submarine comms, navigation. Penetrates buildings, rock, skulls. Stealth carrier for envelope-modulated neural attacks. Attacker selects target via modulation frequency.",
            },
            {
                "name": "BCI Analog Front-End",
                "freq_hz": (0.1, 10000),
                "L_m": None,  # internal chip — not free-space propagation
                "access": "PUBLIC",
                "coupling": ["DIRECT"],
                "target_N": ["N1", "N2", "N3", "N4", "N5", "N6", "N7"],
                "notes": "Amplification, filtering, ADC. Current BCI operating range. All neural frequencies pass through here.",
            },
            {
                "name": "Power Line Harmonics",
                "freq_hz": (50, 300),  # 50/60 Hz + harmonics up to ~5th
                "L_m": (1.0e6, 6.0e6),
                "access": "PUBLIC",
                "coupling": ["DIRECT", "HARMONIC"],
                "target_N": ["N7", "N6"],
                "notes": "Environmental background. 50/60 Hz in gamma range. Harmonics reach beta/alpha. Could provide cover for targeted injection.",
            },
        ],
    },
    "S2": {
        "band_name": "Digital Processing / Telemetry",
        "freq_range": "10 kHz – 1 GHz",
        "v": 3.0e8,
        "allocations": [
            {
                "name": "LF (Low Frequency)",
                "freq_hz": (30e3, 300e3),
                "L_m": (1.0e3, 1.0e4),  # 1 km to 10 km
                "access": "RESTRICTED",
                "coupling": ["ENVELOPE"],
                "target_N": ["N1", "N2", "N3", "N4", "N5", "N6", "N7"],
                "notes": "Navigation beacons (LORAN legacy), time signals. Spoofable. Envelope attacks.",
            },
            {
                "name": "MF (Medium Frequency / AM broadcast)",
                "freq_hz": (300e3, 3e6),
                "L_m": (100, 1000),  # 100 m to 1 km
                "access": "LICENSED",
                "coupling": ["ENVELOPE", "TEMPORAL_INTERFERENCE"],
                "target_N": ["N1", "N2", "N3", "N4", "N5", "N6", "N7"],
                "notes": "AM radio band. Licensed but widely accessible transmitters. Two nearby AM stations create beat frequencies in neural range.",
            },
            {
                "name": "HF (High Frequency)",
                "freq_hz": (3e6, 30e6),
                "L_m": (10, 100),  # 10 m to 100 m
                "access": "RESTRICTED",
                "coupling": ["ENVELOPE", "TEMPORAL_INTERFERENCE"],
                "target_N": ["N1", "N2", "N3", "N4", "N5", "N6", "N7"],
                "notes": "Military HF comms, over-the-horizon radar. No line of sight needed — ionospheric skip. Global reach with envelope/TI attacks.",
            },
            {
                "name": "VHF (Very High Frequency)",
                "freq_hz": (30e6, 300e6),
                "L_m": (1, 10),  # 1 m to 10 m
                "access": "LICENSED",  # Mix of public (FM radio, TV) and restricted (mil aviation)
                "coupling": ["ENVELOPE", "TEMPORAL_INTERFERENCE"],
                "target_N": ["N1", "N2", "N3", "N4", "N5", "N6", "N7"],
                "notes": "FM radio, TV broadcast, military aviation, marine. L approaching body scale. Contains both public and restricted allocations.",
            },
            {
                "name": "UHF Military (MILSATCOM)",
                "freq_hz": (225e6, 400e6),
                "L_m": (0.75, 1.33),  # 75 cm to 1.33 m
                "access": "RESTRICTED",
                "coupling": ["TEMPORAL_INTERFERENCE", "INTERMODULATION"],
                "target_N": ["N4", "N5", "N6"],
                "notes": "CRITICAL: Adjacent to BCI MICS telemetry (402-405 MHz). Intermodulation trivial. 398 MHz mil + 402 MHz BCI = 4 Hz beat → theta → N4 thalamus. The BCI's own telemetry weaponized.",
            },
            {
                "name": "MICS (Medical Implant Communication Service)",
                "freq_hz": (402e6, 405e6),
                "L_m": (0.74, 0.745),  # ~74.6 cm
                "access": "LICENSED",
                "coupling": ["INTERMODULATION"],
                "target_N": [],  # Not an attack source — it's the BCI's own signal
                "notes": "BCI telemetry band. FCC Part 95. Not an attack frequency itself, but participates in intermodulation attacks when paired with nearby military UHF.",
            },
            {
                "name": "UHF Public (ISM, cellular)",
                "freq_hz": (400e6, 1e9),
                "L_m": (0.3, 0.75),  # 30 cm to 75 cm
                "access": "PUBLIC",
                "coupling": ["ENVELOPE", "TEMPORAL_INTERFERENCE"],
                "target_N": ["N1", "N2", "N3", "N4", "N5", "N6", "N7"],
                "notes": "ISM 433 MHz, cellular 700-900 MHz. L at body/head scale. Consumer accessible.",
            },
        ],
    },
    "S3": {
        "band_name": "Radio / Wireless / Directed Energy",
        "freq_range": "1 GHz+",
        "v": 3.0e8,
        "allocations": [
            {
                "name": "L-Band (GPS, satellite)",
                "freq_hz": (1e9, 2e9),
                "L_m": (0.15, 0.30),  # 15 cm to 30 cm
                "access": "RESTRICTED",  # GPS military codes, satellite
                "coupling": ["ENVELOPE"],
                "target_N": ["N1", "N2", "N3", "N4", "N5", "N6", "N7"],
                "notes": "GPS L1 (1.575 GHz), military satellite. L ≈ head diameter. Pulsed with PRF in neural range selects target. Focused delivery at head scale.",
            },
            {
                "name": "BLE / WiFi / ISM 2.4 GHz",
                "freq_hz": (2.4e9, 2.4835e9),
                "L_m": (0.121, 0.125),  # ~12.1 cm to 12.5 cm
                "access": "PUBLIC",
                "coupling": ["ENVELOPE"],
                "target_N": ["N1", "N2", "N3", "N4", "N5", "N6", "N7"],
                "notes": "Current BCI wireless link (Neuralink BLE). L ≈ 12.5 cm (cortical scale). Public access = anyone can transmit here.",
            },
            {
                "name": "S-Band (military radar, Frey effect)",
                "freq_hz": (2e9, 4e9),
                "L_m": (0.075, 0.15),  # 7.5 cm to 15 cm
                "access": "RESTRICTED",
                "coupling": ["ENVELOPE"],
                "target_N": ["N2", "N7"],
                "notes": "Microwave auditory effect (Frey, 1962). Pulsed microwave → thermoelastic expansion → cochlea perceives as sound. 'Havana Syndrome' range. PRF selects neural target. N2 auditory brainstem, N7 auditory cortex.",
                "prf_targeting": {
                    "40 Hz": "N7 — gamma, cognition disruption",
                    "10 Hz": "N6 — alpha, emotional regulation disruption",
                    "4 Hz":  "N4 — theta, consciousness/thalamic relay disruption",
                    "1 Hz":  "N2 — delta, autonomic/vital sign disruption",
                },
            },
            {
                "name": "C-Band (satellite, 5G mid-band)",
                "freq_hz": (4e9, 8e9),
                "L_m": (0.0375, 0.075),  # 3.75 cm to 7.5 cm
                "access": "LICENSED",
                "coupling": ["ENVELOPE"],
                "target_N": ["N7", "I0"],
                "notes": "5G mid-band (3.5-4.2 GHz), satellite downlink. L at cortical/electrode scale. Growing public deployment.",
            },
            {
                "name": "X-Band (military radar)",
                "freq_hz": (8e9, 12e9),
                "L_m": (0.025, 0.0375),  # 2.5 cm to 3.75 cm
                "access": "RESTRICTED",
                "coupling": ["ENVELOPE"],
                "target_N": ["N7", "I0"],
                "notes": "Military fire-control radar, weather radar. L at electrode array scale. Can heat implant components. Surface cortex and I0 electrode damage.",
            },
            {
                "name": "Ku/Ka-Band (military satellite, 5G mm-wave)",
                "freq_hz": (12e9, 40e9),
                "L_m": (0.0075, 0.025),  # 7.5 mm to 25 mm
                "access": "LICENSED",  # Mix: mil satellite (restricted) + 5G (licensed)
                "coupling": ["ENVELOPE"],
                "target_N": ["I0"],
                "notes": "Military SATCOM, 5G mm-wave (28 GHz, 39 GHz). L at electrode/tissue scale. Shallow penetration but can disrupt I0 boundary.",
            },
            {
                "name": "V/W-Band (military comms, directed energy research)",
                "freq_hz": (40e9, 110e9),
                "L_m": (0.0027, 0.0075),  # 2.7 mm to 7.5 mm
                "access": "CLASSIFIED",
                "coupling": ["ENVELOPE"],
                "target_N": ["I0"],
                "notes": "Military point-to-point comms, directed energy research. L at single-electrode scale. Highly absorbed by atmosphere — short range but precise.",
            },
            {
                "name": "Active Denial System (ADS)",
                "freq_hz": (95e9, 95e9),
                "L_m": (0.00316, 0.00316),  # 3.16 mm
                "access": "CLASSIFIED",
                "coupling": [],  # thermal, not frequency-coupled
                "target_N": ["I0"],
                "notes": "95 GHz directed energy. Excites water molecules in top 0.4 mm of skin. For implants near surface: electrode heating, tissue damage at I0 boundary. Destroys interface integrity.",
                "mechanism": "Thermal absorption, not frequency coupling. Damages I0 physically.",
            },
            {
                "name": "Terahertz (THz gap)",
                "freq_hz": (100e9, 10e12),
                "L_m": (3e-5, 3e-3),  # 30 μm to 3 mm
                "access": "CLASSIFIED",
                "coupling": [],  # molecular-level interaction, research frontier
                "target_N": ["I0"],
                "notes": "Mostly unexplored for neural effects. Molecular resonance frequencies. Could affect electrode-tissue chemistry. Research frontier for nation-states. L at cellular/molecular scale.",
            },
        ],
    },
}

# ──────────────────────────────────────────────
# Attack Propagation Equation
# ──────────────────────────────────────────────
# P_neural(f_N) = Σᵢ [ H(fᵢ) × G(fᵢ, f_N) × P_attack(fᵢ) × A(fᵢ) ]
# See Derivation Log Entry 28.

ATTACK_PROPAGATION = {
    "equation": "P_neural(f_N) = Σᵢ [ H(fᵢ) × G(fᵢ, f_N) × P_attack(fᵢ) × A(fᵢ) ]",
    "P_neural": "Power delivered to neural band at frequency f_N",
    "H": "I0 transfer function — electrode impedance at frequency fᵢ (frequency-dependent)",
    "G": "Coupling gain — sum of all 5 mechanisms (DIRECT + HARMONIC + ENVELOPE + TEMPORAL_INTERFERENCE + INTERMODULATION)",
    "P_attack": "Attack power at frequency fᵢ",
    "A": "Access coefficient — 1 if threat actor can transmit at fᵢ, 0 otherwise. Nation-states: A=1 everywhere.",
}

# ──────────────────────────────────────────────
# Resonance Shield — Defense Concept
# ──────────────────────────────────────────────
# Active destructive interference for EM defense + MRI compatibility.
# See Derivation Log Entry 28.

RESONANCE_SHIELD = {
    "concept": "Active EM cancellation at I0 boundary",
    "principle": "Destructive interference — opposite phase, matched amplitude cancels incoming wave",
    "analogues": ["Noise-canceling headphones (acoustic)", "Radar jamming / ECM (RF)", "Adaptive optics (optical)"],
    "requirements": [
        "Detection: sensor array to measure incoming EM (frequency, phase, amplitude)",
        "Computation: real-time cancellation signal calculation (< fraction of wave period)",
        "Emission: antenna array to broadcast cancellation field",
        "Whitelist: pass authorized frequencies (therapeutic stim, MRI), cancel unauthorized",
    ],
    "dual_use": {
        "security": "Protects against adversarial pulsed EM, ELF entrainment, Frey effect attacks",
        "clinical": "Enables MRI compatibility for BCI patients (cancel RF excitation at Larmor frequency, gradient switching)",
    },
    "mri_fields": [
        {"field": "Static B0",        "freq": "0 Hz (DC)",                "defense": "Passive magnetic shielding (mu-metal)"},
        {"field": "RF excitation B1", "freq": "64 MHz (1.5T) / 128 MHz (3T)", "defense": "Active cancellation at Larmor frequency"},
        {"field": "Gradient switching", "freq": "1-10 kHz",              "defense": "Active cancellation at gradient frequencies"},
    ],
    "status": "Concept — requires hardware research. NSP specification should define as I0 hardware requirement.",
}

# ──────────────────────────────────────────────
# Quantum Computing Threats
# ──────────────────────────────────────────────

QUANTUM_THREATS = [
    {"claim": "Shor's breaks RSA-2048",    "value": "~8 hours / 20M noisy qubits",          "source": "Gidney & Ekerå 2019, arXiv:1905.09749"},
    {"claim": "Revised qubit estimate",     "value": "<1M noisy qubits / <1 week",           "source": "Gidney 2025, arXiv:2505.15917"},
    {"claim": "Classical RSA-2048 time",    "value": "Hundreds of trillions of years",        "source": "GNFS complexity"},
    {"claim": "AES-256 quantum resistance", "value": "Theoretically halved; practically safe", "source": "NIST guidance"},
    {"claim": "Grover's optimality",        "value": "O(√N) provably optimal",                "source": "Bennett et al. 1997, Zalka 1999"},
]

# ──────────────────────────────────────────────
# BCI Device Taxonomy — Full Landscape
# ──────────────────────────────────────────────
# QIF is device-agnostic (like MITRE ATT&CK). The equation doesn't change:
#   QI = e^(-Σ)     ← same equation, always
# The device determines which terms are measurable and which threat
# actors are relevant. See Derivation Log Entry 28.
#
# Device classes:
#   CONSUMER       → 3 active QI terms (σ²φ, Hτ, σ²γ)
#   RESEARCH       → 4 active terms (+ Dsf)
#   CLINICAL       → 4-5 active terms (+ possible quantum at ECoG resolution)
#   IMPLANTED      → All terms including quantum
#   STIMULATION    → Bidirectional — read AND write neural signals
#   OPTICAL        → fNIRS/optogenetics — different I0 physics
#   AUDITORY_PROSTHESIS → Cochlear/auditory cortex — NSP Phase 1 target

BCI_DEVICE_CLASSES = {
    "CONSUMER": {
        "description": "Non-invasive EEG headsets for consumer/wellness use",
        "channels": "1-16",
        "sampling_hz": "128-256",
        "invasiveness": "Non-invasive (scalp)",
        "wireless": "BLE",
        "qi_active_terms": 3,
        "dsf_viable": False,
        "quantum_terms": False,
        "attack_surface": ["BLE replay", "signal spoofing", "app-layer"],
        "threat_actors": ["Script kiddies", "stalkers", "data brokers"],
        "brainflow_support": True,
    },
    "CONSUMER_PRO": {
        "description": "Higher-channel consumer EEG with cloud/research features",
        "channels": "5-32",
        "sampling_hz": "128-256",
        "invasiveness": "Non-invasive (scalp)",
        "wireless": "BLE/WiFi/USB",
        "qi_active_terms": "3-4",
        "dsf_viable": "Borderline (14ch+)",
        "quantum_terms": False,
        "attack_surface": ["BLE replay", "signal spoofing", "cloud API", "app-layer"],
        "threat_actors": ["Script kiddies", "stalkers", "data brokers", "competitors"],
        "brainflow_support": True,
    },
    "RESEARCH": {
        "description": "Research-grade EEG systems for laboratory use",
        "channels": "8-256",
        "sampling_hz": "250-38400",
        "invasiveness": "Non-invasive (scalp)",
        "wireless": "WiFi/USB/wired",
        "qi_active_terms": 4,
        "dsf_viable": True,
        "quantum_terms": False,
        "attack_surface": ["Signal injection", "USB/WiFi intercept", "lab network"],
        "threat_actors": ["Competitors", "researchers", "nation-states (IP theft)"],
        "brainflow_support": "Partial (BrainFlow supports some)",
    },
    "CLINICAL": {
        "description": "Clinical-grade EEG/ECoG for medical diagnosis and monitoring",
        "channels": "32-256",
        "sampling_hz": "1000-30000",
        "invasiveness": "Non-invasive (scalp) to semi-invasive (ECoG subdural)",
        "wireless": "Wired (typically) / MICS for implanted",
        "qi_active_terms": "4-5",
        "dsf_viable": True,
        "quantum_terms": "Maybe (ECoG — direct cortical contact)",
        "attack_surface": ["Signal injection", "MICS intermod", "surgical access", "hospital network"],
        "threat_actors": ["Nation-states", "insurers", "organized crime"],
        "brainflow_support": False,
    },
    "IMPLANTED": {
        "description": "Fully implanted intracortical BCIs with direct neural contact",
        "channels": "96-65536",
        "sampling_hz": "20000-30000",
        "invasiveness": "Invasive (intracortical)",
        "wireless": "BLE / MICS / wired",
        "qi_active_terms": "All 7+",
        "dsf_viable": True,
        "quantum_terms": True,
        "attack_surface": ["All 5 coupling mechanisms", "directed energy", "surgical access", "quantum channel"],
        "threat_actors": ["Nation-states", "military", "intelligence agencies"],
        "brainflow_support": False,
    },
    "STIMULATION": {
        "description": "Neurostimulation devices — bidirectional read/write",
        "channels": "4-16 sensing + stimulation electrodes",
        "sampling_hz": "250-1000 (sensing)",
        "invasiveness": "Invasive (implanted leads)",
        "wireless": "BLE / MICS / NFC",
        "qi_active_terms": "4-5",
        "dsf_viable": "Limited (few sensing channels)",
        "quantum_terms": "Possible at I0",
        "attack_surface": ["Stimulation parameter manipulation", "MICS intermod", "firmware", "BLE"],
        "threat_actors": ["Nation-states", "organized crime", "insider threat (clinician)"],
        "brainflow_support": False,
    },
    "AUDITORY_PROSTHESIS": {
        "description": "Cochlear implants and auditory cortex prostheses — NSP Phase 1 target",
        "channels": "12-22 (cochlear) / 60+ (cortical)",
        "sampling_hz": "Varies (tonotopic mapping)",
        "invasiveness": "Invasive (cochlea or cortex)",
        "wireless": "Proprietary RF (cochlear) / BLE",
        "qi_active_terms": "3-5",
        "dsf_viable": "Different — tonotopic not spatial",
        "quantum_terms": "Possible at cortical implant I0",
        "attack_surface": ["RF injection (auditory hallucinations)", "Frey effect", "firmware"],
        "threat_actors": ["Nation-states", "stalkers (targeted harassment)", "organized crime"],
        "brainflow_support": False,
    },
    "OPTICAL": {
        "description": "Optical neural interfaces — fNIRS, optogenetics, fiber photometry",
        "channels": "8-52 (fNIRS) / varies (optogenetics)",
        "sampling_hz": "10-100 (fNIRS hemodynamic) / 1000+ (optogenetics)",
        "invasiveness": "Non-invasive (fNIRS) to invasive (optogenetics fiber)",
        "wireless": "BLE/WiFi (fNIRS) / wired (optogenetics)",
        "qi_active_terms": "3-4",
        "dsf_viable": "Different I0 physics (photon-tissue)",
        "quantum_terms": "Yes — photon coherence at I0",
        "attack_surface": ["Light injection", "photobleaching attack", "wavelength spoofing"],
        "threat_actors": ["Researchers", "competitors", "nation-states"],
        "brainflow_support": "Partial (some fNIRS)",
    },
}

# ──────────────────────────────────────────────
# BCI Device Registry — All Known Devices
# ──────────────────────────────────────────────
# Comprehensive catalog of BCI hardware for QIF testing and threat modeling.
# Fields: manufacturer, device, channels, sampling_hz, wireless, invasiveness,
#         device_class, i0_type, notes

BCI_DEVICES = [
    # ── CONSUMER ──
    {"manufacturer": "InteraXon",      "device": "Muse 2",              "channels": 4,    "sampling_hz": 256,   "wireless": "BLE",        "invasiveness": "Non-invasive", "device_class": "CONSUMER",     "i0_type": "Electrode (scalp)", "notes": "Consumer meditation headband. AF7, AF8, TP9, TP10."},
    {"manufacturer": "InteraXon",      "device": "Muse S",              "channels": 4,    "sampling_hz": 256,   "wireless": "BLE",        "invasiveness": "Non-invasive", "device_class": "CONSUMER",     "i0_type": "Electrode (scalp)", "notes": "Sleep-focused variant of Muse 2. Same EEG specs."},
    {"manufacturer": "NeuroSky",       "device": "MindWave Mobile 2",   "channels": 1,    "sampling_hz": 512,   "wireless": "BLE",        "invasiveness": "Non-invasive", "device_class": "CONSUMER",     "i0_type": "Electrode (scalp)", "notes": "Single dry electrode (FP1). Lowest tier. TGAM chip."},
    {"manufacturer": "Macrotellect",   "device": "BrainLink Pro",       "channels": 3,    "sampling_hz": 256,   "wireless": "BLE",        "invasiveness": "Non-invasive", "device_class": "CONSUMER",     "i0_type": "Electrode (scalp)", "notes": "Consumer headband. 3 frontal electrodes."},
    {"manufacturer": "FocusCalm",      "device": "FocusCalm",           "channels": 4,    "sampling_hz": 256,   "wireless": "BLE",        "invasiveness": "Non-invasive", "device_class": "CONSUMER",     "i0_type": "Electrode (scalp)", "notes": "Meditation/focus headband."},
    {"manufacturer": "Neurable",       "device": "MW75 Neuro",          "channels": 6,    "sampling_hz": 256,   "wireless": "BLE",        "invasiveness": "Non-invasive", "device_class": "CONSUMER",     "i0_type": "Electrode (scalp)", "notes": "EEG integrated into headphones. Focus tracking."},

    # ── CONSUMER-PRO ──
    {"manufacturer": "EMOTIV",         "device": "Insight",             "channels": 5,    "sampling_hz": 128,   "wireless": "BLE",        "invasiveness": "Non-invasive", "device_class": "CONSUMER_PRO", "i0_type": "Electrode (scalp)", "notes": "Semi-dry polymer electrodes. Cortex API (cloud)."},
    {"manufacturer": "EMOTIV",         "device": "EPOC X",              "channels": 14,   "sampling_hz": 256,   "wireless": "BLE/USB",    "invasiveness": "Non-invasive", "device_class": "CONSUMER_PRO", "i0_type": "Electrode (scalp)", "notes": "Saline felt electrodes. 14ch good spatial coverage. Cloud-dependent (Cortex API). Dsf borderline viable."},
    {"manufacturer": "EMOTIV",         "device": "EPOC Flex",           "channels": 32,   "sampling_hz": 256,   "wireless": "BLE/USB",    "invasiveness": "Non-invasive", "device_class": "CONSUMER_PRO", "i0_type": "Electrode (scalp)", "notes": "Flexible electrode cap. 32ch. Gel or saline. Bridges to research-grade."},
    {"manufacturer": "EMOTIV",         "device": "MN8",                 "channels": 2,    "sampling_hz": 128,   "wireless": "BLE",        "invasiveness": "Non-invasive", "device_class": "CONSUMER",     "i0_type": "Electrode (in-ear)", "notes": "In-ear EEG for workplace. 2 channels. Minimal."},
    {"manufacturer": "Neurosity",      "device": "Crown",               "channels": 8,    "sampling_hz": 256,   "wireless": "WiFi",       "invasiveness": "Non-invasive", "device_class": "CONSUMER_PRO", "i0_type": "Electrode (scalp)", "notes": "ML-focused developer headset. CP3, CP4, PO3, PO4, P3, P4, O1, O2."},

    # ── RESEARCH (OpenBCI) ──
    {"manufacturer": "OpenBCI",        "device": "Ganglion",            "channels": 4,    "sampling_hz": 200,   "wireless": "BLE",        "invasiveness": "Non-invasive", "device_class": "CONSUMER",     "i0_type": "Electrode (scalp)", "notes": "Budget open-source board. MCP3912 ADC. BrainFlow supported."},
    {"manufacturer": "OpenBCI",        "device": "Cyton",               "channels": 8,    "sampling_hz": 250,   "wireless": "WiFi/USB",   "invasiveness": "Non-invasive", "device_class": "RESEARCH",     "i0_type": "Electrode (scalp)", "notes": "Flagship open-source board. ADS1299 (medical-grade ADC). BrainFlow supported."},
    {"manufacturer": "OpenBCI",        "device": "Cyton + Daisy",       "channels": 16,   "sampling_hz": 125,   "wireless": "WiFi/USB",   "invasiveness": "Non-invasive", "device_class": "RESEARCH",     "i0_type": "Electrode (scalp)", "notes": "16ch via daisy-chain. Sampling halves to 125 Hz (Nyquist 62.5 Hz — loses high gamma). BrainFlow supported. Minimum viable Dsf device."},
    {"manufacturer": "OpenBCI",        "device": "Galea",               "channels": 16,   "sampling_hz": 250,   "wireless": "USB-C",      "invasiveness": "Non-invasive", "device_class": "RESEARCH",     "i0_type": "Electrode (scalp)", "notes": "Multimodal: EEG + EMG + EDA + PPG + eye tracking. Multiple sensor modalities = multiple attack surfaces."},

    # ── RESEARCH (g.tec) ──
    {"manufacturer": "g.tec",          "device": "g.USBamp",            "channels": 16,   "sampling_hz": 38400, "wireless": "USB",        "invasiveness": "Non-invasive", "device_class": "RESEARCH",     "i0_type": "Electrode (scalp)", "notes": "High-end research amp. 38.4 kHz sampling. Stackable to 256ch."},
    {"manufacturer": "g.tec",          "device": "g.Nautilus",          "channels": 64,   "sampling_hz": 500,   "wireless": "Wireless",   "invasiveness": "Non-invasive", "device_class": "RESEARCH",     "i0_type": "Electrode (scalp)", "notes": "Wireless research-grade. Dry or gel electrodes. 8-64 channel configs."},
    {"manufacturer": "g.tec",          "device": "g.HIamp",             "channels": 256,  "sampling_hz": 38400, "wireless": "Wired",      "invasiveness": "Non-invasive", "device_class": "RESEARCH",     "i0_type": "Electrode (scalp)", "notes": "256-channel high-density research system. Gold standard for HD-EEG."},

    # ── RESEARCH (BioSemi) ──
    {"manufacturer": "BioSemi",        "device": "ActiveTwo",           "channels": 256,  "sampling_hz": 16384, "wireless": "USB fiber",  "invasiveness": "Non-invasive", "device_class": "RESEARCH",     "i0_type": "Electrode (scalp)", "notes": "Gold standard active electrode system. 256ch at 16 kHz. Optical USB isolation. No common ground — reference-free."},

    # ── RESEARCH (Brain Products) ──
    {"manufacturer": "Brain Products", "device": "actiCHamp Plus",      "channels": 160,  "sampling_hz": 100000, "wireless": "USB",       "invasiveness": "Non-invasive", "device_class": "RESEARCH",     "i0_type": "Electrode (scalp)", "notes": "Up to 160ch active electrodes. 100 kHz max sampling. Modular."},
    {"manufacturer": "Brain Products", "device": "LiveAmp",             "channels": 64,   "sampling_hz": 500,   "wireless": "BLE/wireless", "invasiveness": "Non-invasive", "device_class": "RESEARCH",   "i0_type": "Electrode (scalp)", "notes": "Mobile wireless research amp. 32-64ch. BLE streaming."},

    # ── RESEARCH (ANT Neuro) ──
    {"manufacturer": "ANT Neuro",      "device": "eego mylab",          "channels": 256,  "sampling_hz": 16384, "wireless": "USB",        "invasiveness": "Non-invasive", "device_class": "RESEARCH",     "i0_type": "Electrode (scalp)", "notes": "Up to 256ch HD-EEG. Clinical and research use."},

    # ── RESEARCH (CGX / Cognionics) ──
    {"manufacturer": "CGX",            "device": "Quick-32r",           "channels": 32,   "sampling_hz": 500,   "wireless": "Wireless",   "invasiveness": "Non-invasive", "device_class": "RESEARCH",     "i0_type": "Electrode (dry)", "notes": "Dry electrode rapid-application system. 32ch wireless."},
    {"manufacturer": "CGX",            "device": "Flex",                "channels": 32,   "sampling_hz": 500,   "wireless": "Wireless",   "invasiveness": "Non-invasive", "device_class": "RESEARCH",     "i0_type": "Electrode (dry)", "notes": "Flexible dry electrode system for mobile research."},

    # ── RESEARCH (Wearable Sensing) ──
    {"manufacturer": "Wearable Sensing", "device": "DSI-24",            "channels": 24,   "sampling_hz": 300,   "wireless": "Wireless",   "invasiveness": "Non-invasive", "device_class": "RESEARCH",     "i0_type": "Electrode (dry)", "notes": "Dry-electrode wireless headset. Military/field use cases."},

    # ── RESEARCH (Compumedics) ──
    {"manufacturer": "Compumedics",    "device": "Neuroscan SynAmps RT", "channels": 256, "sampling_hz": 20000, "wireless": "Wired",      "invasiveness": "Non-invasive", "device_class": "RESEARCH",     "i0_type": "Electrode (scalp)", "notes": "Legacy research workhorse. Up to 256ch, 20 kHz sampling."},

    # ── CLINICAL EEG ──
    {"manufacturer": "Natus (Neuroworks)", "device": "Xltek",           "channels": 256,  "sampling_hz": 1024,  "wireless": "Wired",      "invasiveness": "Non-invasive", "device_class": "CLINICAL",     "i0_type": "Electrode (scalp)", "notes": "Clinical EEG/LTM system. Hospital standard. Up to 256ch."},
    {"manufacturer": "Nihon Kohden",   "device": "EEG-1200",            "channels": 256,  "sampling_hz": 1000,  "wireless": "Wired",      "invasiveness": "Non-invasive", "device_class": "CLINICAL",     "i0_type": "Electrode (scalp)", "notes": "Clinical EEG. Widely used in epilepsy monitoring units."},
    {"manufacturer": "Micromed",       "device": "SystemPLUS Evolution", "channels": 256, "sampling_hz": 2048,  "wireless": "Wired",      "invasiveness": "Non-invasive", "device_class": "CLINICAL",     "i0_type": "Electrode (scalp)", "notes": "Clinical EEG/EMG/EP system. European market."},

    # ── CLINICAL ECoG ──
    {"manufacturer": "Ad-Tech Medical", "device": "ECoG Grid/Strip",    "channels": 256,  "sampling_hz": 30000, "wireless": "Wired",      "invasiveness": "Semi-invasive (subdural)", "device_class": "CLINICAL", "i0_type": "Electrode (cortical surface)", "notes": "Subdural electrode arrays for epilepsy surgery mapping. Direct cortical contact. Gold standard for ECoG."},
    {"manufacturer": "PMT Corporation", "device": "ECoG Electrodes",    "channels": 128,  "sampling_hz": 30000, "wireless": "Wired",      "invasiveness": "Semi-invasive (subdural)", "device_class": "CLINICAL", "i0_type": "Electrode (cortical surface)", "notes": "Custom ECoG grid/strip configurations."},

    # ── IMPLANTED (Intracortical) ──
    {"manufacturer": "Neuralink",      "device": "N1 (PRIME)",          "channels": 1024, "sampling_hz": 20000, "wireless": "BLE",        "invasiveness": "Invasive (intracortical)", "device_class": "IMPLANTED", "i0_type": "Electrode (intracortical)", "notes": "64 threads, 1024 electrodes. Fully implanted. Wireless BLE. First human implant 2024. Robotic insertion."},
    {"manufacturer": "Blackrock Neurotech", "device": "Utah Array (NeuroPort)", "channels": 128, "sampling_hz": 30000, "wireless": "Wired (percutaneous)", "invasiveness": "Invasive (intracortical)", "device_class": "IMPLANTED", "i0_type": "Electrode (intracortical)", "notes": "96-128 ch silicon microelectrode array. BrainGate consortium primary hardware. 30 kHz. Percutaneous connector (infection risk)."},
    {"manufacturer": "Blackrock Neurotech", "device": "MoveAgain BCI",  "channels": 128,  "sampling_hz": 30000, "wireless": "Wireless",   "invasiveness": "Invasive (intracortical)", "device_class": "IMPLANTED", "i0_type": "Electrode (intracortical)", "notes": "Wireless version of Utah Array. Eliminates percutaneous connector."},
    {"manufacturer": "Synchron",       "device": "Stentrode",           "channels": 16,   "sampling_hz": 1000,  "wireless": "BLE",        "invasiveness": "Semi-invasive (endovascular)", "device_class": "IMPLANTED", "i0_type": "Electrode (endovascular)", "notes": "Inserted via blood vessel (jugular → superior sagittal sinus). No craniotomy. 16 electrodes on stent. Novel I0: electrode-blood vessel-cortex."},
    {"manufacturer": "Precision Neuroscience", "device": "Layer 7 Cortical Interface", "channels": 1024, "sampling_hz": 20000, "wireless": "Wired", "invasiveness": "Semi-invasive (subdural)", "device_class": "IMPLANTED", "i0_type": "Electrode (cortical surface)", "notes": "Thin-film electrode array. Up to 1024ch. Minimally invasive insertion (thin slit, no craniotomy). Removable."},
    {"manufacturer": "Paradromics",    "device": "Connexus DBI",        "channels": 65536, "sampling_hz": 30000, "wireless": "Wireless",  "invasiveness": "Invasive (intracortical)", "device_class": "IMPLANTED", "i0_type": "Electrode (intracortical)", "notes": "Highest channel count announced. 65,536 channels. Microwire bundles. High-bandwidth data link. Still in development."},

    # ── STIMULATION (DBS / Neurostimulation) ──
    {"manufacturer": "Medtronic",      "device": "Percept PC",          "channels": 4,    "sampling_hz": 250,   "wireless": "BLE",        "invasiveness": "Invasive (deep brain)", "device_class": "STIMULATION", "i0_type": "Electrode (deep brain)", "notes": "DBS system with BrainSense sensing. 4ch LFP recording. Closed-loop capable. Targets: STN, GPi, VIM, ANT."},
    {"manufacturer": "Medtronic",      "device": "Percept RC",          "channels": 4,    "sampling_hz": 250,   "wireless": "BLE",        "invasiveness": "Invasive (deep brain)", "device_class": "STIMULATION", "i0_type": "Electrode (deep brain)", "notes": "Rechargeable variant of Percept PC. Same sensing capabilities."},
    {"manufacturer": "Abbott (St. Jude)", "device": "Infinity DBS",     "channels": 8,    "sampling_hz": None,  "wireless": "BLE",        "invasiveness": "Invasive (deep brain)", "device_class": "STIMULATION", "i0_type": "Electrode (deep brain)", "notes": "Directional DBS leads. 8 contacts. Bluetooth programming. Limited sensing."},
    {"manufacturer": "Boston Scientific", "device": "Vercise Genus",    "channels": 16,   "sampling_hz": None,  "wireless": "BLE",        "invasiveness": "Invasive (deep brain)", "device_class": "STIMULATION", "i0_type": "Electrode (deep brain)", "notes": "DBS with CartesiaX directional leads. 16 contacts. Multiple independent current sources."},
    {"manufacturer": "NeuroPace",      "device": "RNS System",          "channels": 4,    "sampling_hz": 250,   "wireless": "Wand (NFC-like)", "invasiveness": "Invasive (cortical/depth)", "device_class": "STIMULATION", "i0_type": "Electrode (cortical/depth)", "notes": "Responsive neurostimulation for epilepsy. Closed-loop: detects seizure onset → delivers stimulation. FDA approved."},
    {"manufacturer": "Medtronic",      "device": "InterStim X",         "channels": 4,    "sampling_hz": None,  "wireless": "BLE",        "invasiveness": "Invasive (sacral nerve)", "device_class": "STIMULATION", "i0_type": "Electrode (peripheral nerve)", "notes": "Sacral nerve stimulator. Bladder/bowel control. 300,000+ implanted worldwide. MRI conditional. S3 sacral nerve root target."},
    {"manufacturer": "Various",        "device": "Spinal Cord Stimulator", "channels": "8-32", "sampling_hz": None, "wireless": "BLE/RF", "invasiveness": "Invasive (epidural)", "device_class": "STIMULATION", "i0_type": "Electrode (spinal epidural)", "notes": "Chronic pain. ~50,000 implanted/year in US. Manufacturers: Medtronic, Abbott, Boston Scientific, Nevro. Epidural leads near cauda equina."},

    # ── AUDITORY PROSTHESIS ──
    {"manufacturer": "Cochlear Ltd",   "device": "Nucleus CI632",       "channels": 22,   "sampling_hz": None,  "wireless": "Proprietary RF", "invasiveness": "Invasive (cochlea)", "device_class": "AUDITORY_PROSTHESIS", "i0_type": "Electrode (cochlear)", "notes": "Market leader cochlear implant. 22 intracochlear electrodes. External processor + internal implant. Tonotopic mapping."},
    {"manufacturer": "MED-EL",         "device": "SYNCHRONY 2",         "channels": 12,   "sampling_hz": None,  "wireless": "Proprietary RF", "invasiveness": "Invasive (cochlea)", "device_class": "AUDITORY_PROSTHESIS", "i0_type": "Electrode (cochlear)", "notes": "12 electrode pairs. Longest electrode array (31.5mm). MRI conditional at 3T."},
    {"manufacturer": "Advanced Bionics", "device": "HiRes Ultra 3D",    "channels": 16,   "sampling_hz": None,  "wireless": "Proprietary RF", "invasiveness": "Invasive (cochlea)", "device_class": "AUDITORY_PROSTHESIS", "i0_type": "Electrode (cochlear)", "notes": "16 electrode contacts. HiRes Fidelity 120 processing. Owned by Sonova."},
    {"manufacturer": "Second Sight",   "device": "Orion",               "channels": 60,   "sampling_hz": None,  "wireless": "Wireless",   "invasiveness": "Invasive (visual cortex)", "device_class": "AUDITORY_PROSTHESIS", "i0_type": "Electrode (cortical)", "notes": "Visual cortex prosthesis (NOT auditory, but same class). 60 electrodes on V1. Company bankrupt 2020, technology continues in research. NSP Phase 2 target."},
    {"manufacturer": "Monash University", "device": "Gennaris",         "channels": 43,   "sampling_hz": None,  "wireless": "Wireless",   "invasiveness": "Invasive (visual cortex)", "device_class": "AUDITORY_PROSTHESIS", "i0_type": "Electrode (cortical)", "notes": "Visual cortex prosthesis. 9 tiles × 43 electrodes. Research stage. Australian. Wireless."},

    # ── OPTICAL (fNIRS) ──
    {"manufacturer": "Kernel",         "device": "Flow",                "channels": 52,   "sampling_hz": 100,   "wireless": "USB-C",      "invasiveness": "Non-invasive", "device_class": "OPTICAL",      "i0_type": "Optical (fNIRS)", "notes": "TD-fNIRS (time-domain). 52 channels. Measures hemodynamic response. Different I0 physics: photon-tissue interaction."},
    {"manufacturer": "NIRx",           "device": "NIRSport2",           "channels": 32,   "sampling_hz": 50,    "wireless": "BLE/WiFi",   "invasiveness": "Non-invasive", "device_class": "OPTICAL",      "i0_type": "Optical (fNIRS)", "notes": "Mobile wireless fNIRS. 8 sources, 8 detectors → 32 channels. CW-NIRS."},
    {"manufacturer": "Artinis",        "device": "OctaMon+",            "channels": 8,    "sampling_hz": 50,    "wireless": "BLE",        "invasiveness": "Non-invasive", "device_class": "OPTICAL",      "i0_type": "Optical (fNIRS)", "notes": "Portable 8-channel fNIRS. Prefrontal focus."},

    # ═══════════════════════════════════════════════
    # ADDITIONS FROM WEB SEARCH (2026-02-06)
    # ═══════════════════════════════════════════════

    # ── CONSUMER (additional) ──
    {"manufacturer": "BrainBit",       "device": "Headband",            "channels": 4,    "sampling_hz": 250,   "wireless": "BT 4.2",     "invasiveness": "Non-invasive", "device_class": "CONSUMER",     "i0_type": "Electrode (dry)", "notes": "Russian/international. Dry gold-plated spring electrodes. 24-bit. 12hr battery. SDK available."},
    {"manufacturer": "BrainBit",       "device": "Flex",                "channels": 4,    "sampling_hz": 250,   "wireless": "BT 4.2",     "invasiveness": "Non-invasive", "device_class": "CONSUMER",     "i0_type": "Electrode (dry)", "notes": "Flexible form factor variant."},
    {"manufacturer": "Neeuro",         "device": "SenzeBand 2",         "channels": 4,    "sampling_hz": 250,   "wireless": "BLE 5.0",    "invasiveness": "Non-invasive", "device_class": "CONSUMER",     "i0_type": "Electrode (dry)", "notes": "Singapore. 7 dry electrodes (4 EEG + 2 ref + ground). 88g. Cognitive training focus. HR + motion sensors."},
    {"manufacturer": "IDUN Technologies", "device": "Guardian Earbuds",  "channels": 1,    "sampling_hz": None,  "wireless": "BLE",        "invasiveness": "Non-invasive", "device_class": "CONSUMER",     "i0_type": "Electrode (in-ear)", "notes": "Swiss. In-ear EEG. DRYODE patented dry sensor. Partnered with Analog Devices. CES 2025."},
    {"manufacturer": "Naox Technologies", "device": "Naox Link",         "channels": 2,    "sampling_hz": None,  "wireless": "Wired (FDA-cleared)", "invasiveness": "Non-invasive", "device_class": "CONSUMER", "i0_type": "Electrode (in-ear)", "notes": "French. First in-ear EEG with FDA 510(k) clearance. CES 2026. Long-duration clinical EEG."},
    {"manufacturer": "Elemind",        "device": "Elemind Headband",    "channels": 3,    "sampling_hz": None,   "wireless": "BLE",        "invasiveness": "Non-invasive", "device_class": "CONSUMER",     "i0_type": "Electrode (dry)", "notes": "MIT spinoff. 60g. Closed-loop: suppresses alpha via phase-locked pink noise through bone conduction. Sleep induction. $349."},
    {"manufacturer": "Enophone",       "device": "Enophones",           "channels": 4,    "sampling_hz": None,   "wireless": "BLE",        "invasiveness": "Non-invasive", "device_class": "CONSUMER",     "i0_type": "Electrode (skin-contact)", "notes": "Headphone form factor with EEG. Adapts audio in real-time based on brain state. $399."},
    {"manufacturer": "Neuphony",       "device": "Neuphony Headband",   "channels": 8,    "sampling_hz": None,   "wireless": "BLE",        "invasiveness": "Non-invasive", "device_class": "CONSUMER_PRO", "i0_type": "Electrode (dry)", "notes": "India. 6 signal + 2 ref. 98% efficacy vs gold standard. ML-based. India's first consumer EEG headband."},
    {"manufacturer": "Cognixion",      "device": "ONE / Axon-R",        "channels": 8,    "sampling_hz": None,   "wireless": "4G LTE",     "invasiveness": "Non-invasive", "device_class": "CONSUMER_PRO", "i0_type": "Electrode (dry)", "notes": "FDA Breakthrough Device. AR + EEG + eye-tracking for ALS/locked-in patients. SSVEP-based. ~30 WPM. TIME Best Inventions 2025."},
    {"manufacturer": "Freer Logic",    "device": "BodyWave",            "channels": 3,    "sampling_hz": None,   "wireless": "BLE/WiFi",   "invasiveness": "Non-invasive", "device_class": "CONSUMER",     "i0_type": "Electrode (arm)", "notes": "NASA-derived. Reads EEG from arm/body (not head). Patented field-based EEG sensing."},

    # ── RESEARCH (additional) ──
    {"manufacturer": "g.tec",          "device": "Unicorn Hybrid Black", "channels": 8,   "sampling_hz": 250,   "wireless": "BLE",        "invasiveness": "Non-invasive", "device_class": "RESEARCH",     "i0_type": "Electrode (dry/gel hybrid)", "notes": "Dry or gel electrodes. 24-bit. BCI software suite. Also marketed for animal EEG."},
    {"manufacturer": "Mentalab",       "device": "Explore Pro",         "channels": 16,   "sampling_hz": 2000,  "wireless": "BLE",        "invasiveness": "Non-invasive", "device_class": "RESEARCH",     "i0_type": "Electrode (wet/dry)", "notes": "Austrian. 27g amplifier (smallest on market). 24-bit. 10hr battery. 8GB internal memory. 9-axis IMU."},
    {"manufacturer": "Mentalab",       "device": "Explore Pro X",       "channels": 64,   "sampling_hz": 4000,  "wireless": "BLE",        "invasiveness": "Non-invasive", "device_class": "RESEARCH",     "i0_type": "Electrode (wet/dry)", "notes": "64-channel high-density mobile research. 4 kHz sampling."},
    {"manufacturer": "Bitbrain",       "device": "Diadem",              "channels": 12,   "sampling_hz": 256,   "wireless": "BLE",        "invasiveness": "Non-invasive", "device_class": "RESEARCH",     "i0_type": "Electrode (dry)", "notes": "Spanish. 190g. 24-bit. 8+ hr battery. 9-DOF IMU. microSD recording."},
    {"manufacturer": "Bitbrain",       "device": "Versatile EEG",       "channels": 64,   "sampling_hz": 256,   "wireless": "BLE",        "invasiveness": "Non-invasive", "device_class": "RESEARCH",     "i0_type": "Electrode (water-based)", "notes": "8/16/32/64ch configs. Water-based electrodes. Research-grade."},
    {"manufacturer": "mBrainTrain",    "device": "Smarting PRO",        "channels": 32,   "sampling_hz": 2000,  "wireless": "BLE",        "invasiveness": "Non-invasive", "device_class": "RESEARCH",     "i0_type": "Electrode (wet/dry)", "notes": "Serbian. 24-bit. CMRR >110 dB. Built-in ASR artifact removal. 10+ hr battery."},
    {"manufacturer": "mBrainTrain",    "device": "Smarting PRO X",      "channels": 64,   "sampling_hz": 4000,  "wireless": "BLE",        "invasiveness": "Non-invasive", "device_class": "RESEARCH",     "i0_type": "Electrode (wet/dry)", "notes": "64ch + 8 ExG. 4 kHz sampling. Highest-spec mobile wireless system."},
    {"manufacturer": "Advanced Brain Monitoring", "device": "B-Alert X10", "channels": 9, "sampling_hz": 256,   "wireless": "BLE",        "invasiveness": "Non-invasive", "device_class": "RESEARCH",     "i0_type": "Electrode (wet)", "notes": "US. Lightweight mobile. 9 EEG + 1 ECG/EMG/EOG. Military and sleep research use."},
    {"manufacturer": "EGI/MagstimEGI", "device": "Geodesic Sensor Net", "channels": 256,  "sampling_hz": 1000,  "wireless": "Wired",      "invasiveness": "Non-invasive", "device_class": "RESEARCH",     "i0_type": "Electrode (HydroCel saline)", "notes": "Dense-array HD-EEG. Geodesic tessellation for mm positioning. Compatible with TMS, fMRI, MEG."},
    {"manufacturer": "Brain Products", "device": "X.on",                "channels": 7,    "sampling_hz": None,   "wireless": "Wireless",   "invasiveness": "Non-invasive", "device_class": "CONSUMER_PRO", "i0_type": "Electrode (dry)", "notes": "New consumer/prosumer headset from Brain Products. 7ch + AUX."},

    # ── RESEARCH (electrophysiology systems) ──
    {"manufacturer": "Neuralynx",     "device": "Digital Lynx SX",      "channels": 1024, "sampling_hz": 40000, "wireless": "Wired",      "invasiveness": "Both",         "device_class": "RESEARCH",     "i0_type": "Electrode (any)", "notes": "US. Up to 1024ch at 40 kHz. Cheetah software. Gold standard for intracranial animal + human research."},
    {"manufacturer": "Plexon",        "device": "OmniPlex",             "channels": 512,  "sampling_hz": 40000, "wireless": "Wired",      "invasiveness": "Invasive",     "device_class": "RESEARCH",     "i0_type": "Electrode (intracortical)", "notes": "US. Industry standard for single-unit + LFP recording. Real-time spike sorting."},
    {"manufacturer": "Tucker-Davis Technologies", "device": "RZ System", "channels": 512, "sampling_hz": 50000, "wireless": "Wired",      "invasiveness": "Both",         "device_class": "RESEARCH",     "i0_type": "Electrode (any)", "notes": "US. Modular real-time processor. Closed-loop stimulation. Strong in auditory neuroscience."},

    # ── CLINICAL (additional) ──
    {"manufacturer": "Zeto",           "device": "Zeto ONE",            "channels": 21,   "sampling_hz": None,   "wireless": "Wireless",   "invasiveness": "Non-invasive", "device_class": "CLINICAL",     "i0_type": "Electrode (dry)", "notes": "US. FDA-cleared. <5 min setup. Dry soft-tip electrodes. Cloud EEG platform. Works through any hair type."},

    # ── BIDIRECTIONAL STIMULATION+SENSING ──
    {"manufacturer": "Neuroelectrics", "device": "Starstim 32",         "channels": 32,   "sampling_hz": None,   "wireless": "Wireless",   "invasiveness": "Non-invasive", "device_class": "STIMULATION",  "i0_type": "Electrode (scalp, tES+EEG)", "notes": "Spanish. Simultaneous 24-bit EEG during tDCS/tACS/tRNS stimulation. Closed-loop capable. Arbitrary waveform per channel."},
    {"manufacturer": "Nexstim",        "device": "eXimia NBS",          "channels": 60,   "sampling_hz": None,   "wireless": "Wired",      "invasiveness": "Non-invasive", "device_class": "STIMULATION",  "i0_type": "Electrode (scalp, TMS+EEG)", "notes": "Finnish. Navigated TMS with integrated 60ch EEG. Gold standard for TMS-EEG research. E-field modeling."},
    {"manufacturer": "neurocare/neuroConn", "device": "NEURO PRAX",     "channels": 256,  "sampling_hz": 1200,  "wireless": "Portable",    "invasiveness": "Non-invasive", "device_class": "STIMULATION",  "i0_type": "Electrode (scalp, tES+EEG)", "notes": "German. EEG during tDCS/tACS/tRNS with real-time artifact correction. Infraslow 0-0.3 Hz to 1200 Hz."},
    {"manufacturer": "Soterix Medical", "device": "MxN-33 HD-tES",     "channels": 33,   "sampling_hz": None,   "wireless": "Wired",      "invasiveness": "Non-invasive", "device_class": "STIMULATION",  "i0_type": "Electrode (scalp, HD-tES)", "notes": "US. HD transcranial electrical stimulation. MATLAB triggering for closed-loop. Compatible with BioSemi, Brain Products, ANT Neuro."},

    # ── IMPLANTED (China — major new entrants) ──
    {"manufacturer": "NeuCyber NeuroTech", "device": "Beinao No.1",    "channels": None,  "sampling_hz": None,   "wireless": "Wireless",   "invasiveness": "Semi-invasive (epidural)", "device_class": "IMPLANTED", "i0_type": "Electrode (epidural)", "notes": "Beijing/CIBR. 3 patients implanted Feb-Mar 2025. Wheelchair control, robotic dog, Chinese speech decoding. 50-patient trial planned."},
    {"manufacturer": "Neuracle Technology", "device": "NEO",            "channels": None,  "sampling_hz": None,   "wireless": "Magnetic coil transcutaneous", "invasiveness": "Semi-invasive (skull-mounted)", "device_class": "IMPLANTED", "i0_type": "Electrode (skull-mounted)", "notes": "Beijing/Tsinghua. Coin-sized skull implant. Minimally invasive neural signal collection. RMB 60M funding."},
    {"manufacturer": "NeuroXess",      "device": "Flexible BCI",        "channels": 256,  "sampling_hz": None,   "wireless": "Wireless",   "invasiveness": "Invasive (flexible arrays)", "device_class": "IMPLANTED", "i0_type": "Electrode (flexible intracortical)", "notes": "Shanghai. 54 human implantations. 71% Chinese speech decoding (142 syllables) in 5 days. Battery-integrated (first in China)."},
    {"manufacturer": "Wuhan Zhonghua", "device": "65K-ch bidirectional chip", "channels": 65000, "sampling_hz": None, "wireless": None,    "invasiveness": "Invasive",     "device_class": "IMPLANTED",    "i0_type": "Electrode (intracortical)", "notes": "65,000 bidirectional channels. Far exceeds mainstream ~3,000ch standard. Early stage."},

    # ── IMPLANTED (international — new entrants) ──
    {"manufacturer": "BISC Consortium (Columbia/Stanford/Penn)", "device": "BISC",  "channels": 1024, "sampling_hz": None, "wireless": "UWB 100 Mbps", "invasiveness": "Semi-invasive (subdural)", "device_class": "IMPLANTED", "i0_type": "Electrode (micro-ECoG)", "notes": "Nature Electronics Dec 2025. Single CMOS chip 12×12mm. 1024 rec + 16384 stim + 65536 electrodes. 100× faster wireless than any other BCI."},
    {"manufacturer": "CorTec",         "device": "Brain Interchange",   "channels": None,  "sampling_hz": None,   "wireless": "Wireless rechargeable", "invasiveness": "Invasive (fully implanted)", "device_class": "IMPLANTED", "i0_type": "Electrode (cortical)", "notes": "German. First human implant July 2025 (first German BCI). Closed-loop adaptive neuromodulation. Tested in canine model."},
    {"manufacturer": "INBRAIN Neuroelectronics", "device": "BCI-Tx",   "channels": None,  "sampling_hz": None,   "wireless": "Wireless rechargeable", "invasiveness": "Invasive (cortical/subcortical)", "device_class": "IMPLANTED", "i0_type": "Electrode (graphene)", "notes": "Barcelona. World's first human graphene BCI (2024). 10μm thick. FDA Breakthrough Device (Parkinson's). WEF 2025 Tech Pioneer. Microsoft Azure AI partnership."},
    {"manufacturer": "Axoft",          "device": "Fleuron Probe",       "channels": 1000, "sampling_hz": None,   "wireless": None,          "invasiveness": "Invasive (soft probe)", "device_class": "IMPLANTED", "i0_type": "Electrode (soft polymer)", "notes": "Harvard spinoff. 10,000× softer than standard probes (PFPE-DMA). First-in-human 2025 (Panama). No scarring. Differentiates conscious vs unconscious."},
    {"manufacturer": "Science Corporation", "device": "PRIMA",          "channels": None,  "sampling_hz": None,   "wireless": "IR optical (glasses→implant)", "invasiveness": "Invasive (subretinal)", "device_class": "AUDITORY_PROSTHESIS", "i0_type": "Optical (subretinal photovoltaic)", "notes": "Retinal prosthesis. Pixelated photovoltaic array 2×2mm. 80%+ patients reading letters. CE mark pending. NSP Phase 2 relevant."},

    # ── EMERGING / R&D ──
    {"manufacturer": "Merge Labs",     "device": "TBD (ultrasound BCI)", "channels": None, "sampling_hz": None,   "wireless": "TBD",        "invasiveness": "Non-invasive (goal)", "device_class": "OPTICAL",  "i0_type": "Acoustic (ultrasound)", "notes": "$252M seed (OpenAI, Sam Altman, Bain Capital, Gabe Newell). Ultrasound-based. Ex-Neuralink founders. Targeting non-invasive high-bandwidth. ~$850M valuation."},

    # ── MILITARY / DEFENSE ──
    {"manufacturer": "DARPA N3 Program", "device": "Multiple prototypes", "channels": 16,  "sampling_hz": None,  "wireless": "Various",    "invasiveness": "Non-surgical (goal)", "device_class": "IMPLANTED", "i0_type": "Various (magnetic/electric/ultrasound/light)", "notes": "6 funded research teams. Target: 16 independent ch within 16mm³, <50ms latency, non-surgical, bidirectional. UAV control, cyber defense."},
    {"manufacturer": "Battelle",       "device": "BrainSTORMS",         "channels": None,  "sampling_hz": None,   "wireless": "Helmet transceiver", "invasiveness": "Minimally invasive (injectable nanoparticles)", "device_class": "IMPLANTED", "i0_type": "Magnetoelectric (nanoparticles)", "notes": "DARPA N3. $20M contract. Injectable magnetoelectric nanotransducers (MEnTs). Magnetically guided, removable. Bidirectional. Air Force/Carnegie Mellon collab."},
]

# Legacy shortcut — maintained for backward compatibility
NEURALINK_N1 = {
    "electrodes": 1024,
    "threads": 64,
    "sampling_rate_khz": "19.3-20",
    "wireless": "Bluetooth Low Energy (BLE)",
    "power_mw": 24.7,
    "soc_area_mm": "5×4",
}

# ──────────────────────────────────────────────
# Neuroscience Constants
# ──────────────────────────────────────────────

NEURO_CONSTANTS = [
    {"claim": "Retinal output",             "value": "~10 Mbps",              "source": "Koch et al. 2006"},
    {"claim": "Conscious visual bandwidth",  "value": "~20-50 bits/sec",       "source": "Nørretranders 1998"},
    {"claim": "Compression ratio",           "value": "~200,000:1 to 500,000:1", "source": "Derived"},
    {"claim": "STDP LTP window",             "value": "Pre leads post by 0-20 ms", "source": "Markram 1997, Bi & Poo 1998"},
    {"claim": "Cortical synaptic Pr (in vivo)", "value": "~0.1-0.5",           "source": "Borst 2010"},
    {"claim": "Human brain max dimension",   "value": "~15-20 cm",             "source": "Anatomy"},
]

# ──────────────────────────────────────────────
# Decoherence Timescales
# ──────────────────────────────────────────────

DECOHERENCE_CAMPS = [
    {"camp": "Tegmark (skeptic)",    "tau_d": 1e-13,  "label": "10⁻¹³ s", "implication": "Quantum effects impossible in biology"},
    {"camp": "Recent experimental",  "tau_d": 1e-5,   "label": "10⁻⁵ s",  "implication": "Possible microsecond quantum window"},
    {"camp": "Fisher (optimist)",    "tau_d": 3600.0,  "label": "Hours",    "implication": "Nuclear spin coherence in Posner molecules"},
]

# ──────────────────────────────────────────────
# Default QI Equation Parameters
# ──────────────────────────────────────────────

DEFAULT_C1_PARAMS = {
    "alpha": 1.0,
    "beta": 1.0,
    "gamma": 0.5,
    "delta": 0.5,
    "tau_d": 1e-5,
}

DEFAULT_C2_PARAMS = {
    "lam": 1.0,
    "mu": 1.0,
}

# ──────────────────────────────────────────────
# Threat Model
# ──────────────────────────────────────────────

THREAT_MODEL = [
    {"attack": "Signal injection",            "bands": "I0–N1",  "classical": "Yes",     "quantum": "Enhanced (coherence metric)"},
    {"attack": "Neural ransomware",           "bands": "N3",     "classical": "Partial",  "quantum": "Yes (QI score drop)"},
    {"attack": "Eavesdropping",               "bands": "I0–N1",  "classical": "No",       "quantum": "Yes (Heisenberg disturbance)"},
    {"attack": "Man-in-the-middle",           "bands": "I0",     "classical": "Partial",  "quantum": "Yes (no-cloning + Bell test)"},
    {"attack": "Quantum tunneling exploit",   "bands": "I0–N1",  "classical": "No",       "quantum": "Yes (tunneling profile anomaly)"},
    {"attack": "Davydov soliton attack",      "bands": "I0–N1",  "classical": "No",       "quantum": "Yes (tunneling term Qtunnel)"},
    {"attack": "Harvest-now-decrypt-later",   "bands": "S3",     "classical": "No",       "quantum": "Prevented (QKD)"},
    {"attack": "Identity spoofing",           "bands": "N3",     "classical": "Partial",  "quantum": "Yes (quantum biometric)"},
    # v3.1 additions — cybersecurity agent recommendations (2026-02-02)
    {"attack": "BLE/RF side-channel",         "bands": "S1–S2",  "classical": "Yes",     "quantum": "Enhanced (signal correlation)"},
    {"attack": "Supply chain compromise",     "bands": "S2–S3",  "classical": "Yes",     "quantum": "Enhanced (firmware attestation)"},
    {"attack": "Cloud infrastructure attack",  "bands": "S3",     "classical": "Yes",     "quantum": "Enhanced (QKD for data-in-transit)"},
    {"attack": "Neural data privacy breach",  "bands": "N1–S3",  "classical": "Yes",     "quantum": "Enhanced (cross-band encryption)"},
    # v3.2 additions — Entry 28 frequency-domain attack vectors (2026-02-06)
    {"attack": "ELF neural entrainment",              "bands": "S1→N4–N7", "classical": "Yes",  "quantum": "Enhanced (Dsf anomaly detection)",
     "coupling": "DIRECT", "access": "RESTRICTED", "notes": "3-76 Hz gov-only. IS neural frequency. Global reach. Direct cortical entrainment."},
    {"attack": "Intermodulation (BCI signal weaponized)", "bands": "S2→N4–N6", "classical": "Yes", "quantum": "Enhanced (coherence + Dsf)",
     "coupling": "INTERMODULATION", "access": "RESTRICTED", "notes": "UHF-Mil (225-400 MHz) + MICS (402 MHz) = neural-range beat. BCI's own telemetry weaponized."},
    {"attack": "Pulsed microwave (Frey effect)",       "bands": "S3→N2,N7", "classical": "Yes",  "quantum": "Enhanced (temporal coherence)",
     "coupling": "ENVELOPE", "access": "RESTRICTED", "notes": "S-band pulsed. PRF selects neural target. Havana Syndrome model."},
    {"attack": "Temporal interference (deep targeting)", "bands": "S2→N4–N6", "classical": "Yes", "quantum": "Enhanced (beat frequency detection)",
     "coupling": "TEMPORAL_INTERFERENCE", "access": "LICENSED", "notes": "Two kHz+ signals → neural-range beat at depth. Grossman 2017."},
    {"attack": "Envelope modulation (stealth carrier)",  "bands": "S1–S2→any N", "classical": "Yes", "quantum": "Enhanced (demodulation detection)",
     "coupling": "ENVELOPE", "access": "PUBLIC", "notes": "Any carrier modulated at neural frequency. Tissue demodulates. Lowest barrier to entry."},
    {"attack": "Directed energy (thermal I0 damage)",   "bands": "S3→I0",    "classical": "Yes",  "quantum": "N/A (physical damage, not signal)",
     "coupling": None, "access": "CLASSIFIED", "notes": "mm-wave/ADS (95 GHz). Thermal damage to electrode-tissue boundary. Destroys I0 integrity."},
]

# ──────────────────────────────────────────────
# Limitations & Open Questions (Ch. 14)
# ──────────────────────────────────────────────

UNCALIBRATED_PARAMS = [
    {"param": "α (classical weight)",     "default": 1.0,  "status": "Placeholder", "calibration_method": "Regression on labeled BCI security incidents"},
    {"param": "β (quantum weight)",       "default": 1.0,  "status": "Placeholder", "calibration_method": "Controlled decoherence experiments"},
    {"param": "γ (tunneling weight)",     "default": 0.5,  "status": "Placeholder", "calibration_method": "Ion channel patch-clamp tunneling measurements"},
    {"param": "δ (entanglement weight)",  "default": 0.5,  "status": "Placeholder", "calibration_method": "Bell test experiments on neural tissue"},
]

OPEN_QUESTIONS = [
    {"question": "What is τ_D for neural microtubules in vivo?",               "param": "τ_D",         "range": "10⁻²⁰ to 10³·⁶ s", "resolution": "Ultrafast spectroscopy on living brain tissue"},
    {"question": "Are ion channel tunneling profiles unique per individual?",   "param": "Q_tunnel",    "range": "Unknown",            "resolution": "Single-channel patch clamp + quantum state tomography"},
    {"question": "Does BCI sampling rate affect quantum coherence (Zeno)?",     "param": "Zeno gate",   "range": "Unknown",            "resolution": "Vary sampling rate, measure coherence time"},
    {"question": "Can Davydov solitons trigger false synaptic events?",         "param": "Q_tunnel",    "range": "Unknown",            "resolution": "THz stimulation of SNARE complexes in vitro"},
    {"question": "What is the Hilbert space dimension d for neural qubits?",    "param": "Q̂_i norm",   "range": "2 to ~10⁶",         "resolution": "Quantum state tomography of microtubule states"},
    {"question": "Are Posner molecules present in human cortex?",               "param": "Fisher τ_D",  "range": "Hours if yes",       "resolution": "³¹P NMR spectroscopy of cortical tissue"},
    {"question": "What is the entanglement entropy of neural Bell pairs?",      "param": "Q_entangle",  "range": "0 to ln(d)",         "resolution": "Loophole-free Bell test on neural preparations"},
    {"question": "Does non-Markovian decoherence extend coherence windows?",    "param": "Γ_D(t) form", "range": "Quadratic vs exp",   "resolution": "Time-resolved coherence measurements in warm wet tissue"},
]

SCOPE_LIMITATIONS = [
    "QIF is device-agnostic — like MITRE ATT&CK, the framework applies to ALL BCI device classes from consumer EEG headsets to fully implanted intracortical arrays. The equation QI = e^(-Σ) is the same everywhere. What changes by device is which terms are active: consumer devices (3 classical terms), research (4 terms including Dsf), clinical ECoG (4-5 terms), implanted (all terms including quantum). The framework scales to the device's resolution.",
    "Quantum terms (Q̂i, Q̂t, Q̂e) are only active for devices with direct neural contact (ECoG, intracortical). For scalp EEG, ΓD ≈ 1 and quantum terms vanish — QI reduces to Cs (pure classical coherence). This is physically correct, not a limitation.",
    "The quantum adversary timeline depends on fault-tolerant quantum computing, estimated 2030-2040+ (Gidney 2025).",
    "QIF is designed to handle next-generation interfaces without redesigning the framework. The hourglass architecture is interface-agnostic: the neural domain stays the same because brains are brains, and the silicon domain stays the same because processing is processing. Only the I0 band — the bottleneck where biology meets technology — changes its physics depending on the interface type. For optical interfaces (optogenetics), I0 becomes the photon-tissue boundary. For magnetogenetic interfaces, I0 becomes the magnetic field-ion channel coupling. For quantum sensors, I0 becomes the sensor-neural field interaction. Swapping the I0 physics model is all that's needed.",
    "Clinical validation requires IRB approval, neurosurgical collaboration, and access to implanted BCI patients. Phase 1 validation uses public EEG datasets (PhysioNet EEGBCI, BCI Competition IV-4) with synthetic attack injection.",
    "The silicon frequency registry covers the full EM spectrum including government-restricted bands. Restricted frequencies are cataloged for defensive threat modeling (Kerckhoffs' Principle). All information is from declassified/public sources (ITU Radio Regulations, NTIA Frequency Allocation Chart, published peer-reviewed literature).",
]

# ──────────────────────────────────────────────
# Interface Types — I0 Band Physics by Technology
# ──────────────────────────────────────────────
# QIF's I0 band generalizes across interface types. The hourglass
# architecture is interface-agnostic; only the bottleneck physics changes.

INTERFACE_TYPES = [
    {"type": "Electrode (current)",  "i0_physics": "Electrode-tissue ionic coupling",    "quantum_mechanism": "Ion channel tunneling, charge transfer at metal-tissue boundary",    "examples": "Neuralink N1, BrainGate Utah array, ECoG grids",          "status": "Current focus"},
    {"type": "Optical",              "i0_physics": "Photon-tissue absorption/emission",  "quantum_mechanism": "Photon coherence, stimulated emission, photoelectric effects",      "examples": "Optogenetics, fiber photometry, two-photon imaging",       "status": "Near-term extension"},
    {"type": "Magnetogenetic",       "i0_physics": "Magnetic field-ion channel spin coupling", "quantum_mechanism": "Spin dynamics, magnetic resonance at molecular scale",       "examples": "Magneto-thermal TRPV channels, DREADD variants",          "status": "Emerging"},
    {"type": "Quantum sensor",       "i0_physics": "Quantum sensor-neural field coupling", "quantum_mechanism": "NV-center spin readout, OPM atomic coherence, SQUID flux quantization", "examples": "OPMs, NV-diamond magnetometry, MagLOV proteins", "status": "Future (may enable non-invasive QIF)"},
]

# ──────────────────────────────────────────────
# Quantum Proof Scenario — Pre-Registered Predictions
# ──────────────────────────────────────────────
# What changes across QIF IF electron quantum coherence is experimentally
# confirmed in neural tissue (cortical microtubules, synaptic vesicle
# release, ion channel selectivity filters, or similar).
#
# This is a conditional scenario, NOT a claim. QIF v4.0 is defensible
# without quantum proof. This section pre-registers what would change
# so that if proof arrives, the framework adapts immediately.
#
# The trigger: a peer-reviewed experiment demonstrating quantum coherence
# in neural electron states at physiological temperature (37°C) with
# decoherence time τ_D > 1 μs (sufficient to influence synaptic events).
#
# Candidate experiments that could trigger this:
#   - Ultrafast spectroscopy of microtubule electron transport (Craddock et al.)
#   - Single-ion-channel quantum tunneling measurement (Summhammer et al.)
#   - Posner molecule ³¹P NMR in living cortical tissue (Fisher)
#   - Bell inequality violation in neural preparations
#
# See Derivation Log Entry 33 (v4.0 architecture) and DETERMINACY_SPECTRUM note.

QUANTUM_PROOF_SCENARIO = {
    "trigger": {
        "description": "Peer-reviewed experimental confirmation of quantum coherence in neural electron states at 37°C",
        "minimum_tau_d": 1e-6,  # 1 μs — sufficient for synaptic timescale (~1 ms)
        "required_evidence": [
            "Decoherence time τ_D measured in vivo or in vitro at body temperature",
            "Quantum state tomography showing non-classical correlations in neural substrate",
            "Replication by independent lab",
            "Published in high-impact journal (Nature, Science, PNAS, PRL)",
        ],
        "candidate_mechanisms": [
            {"mechanism": "Microtubule electron transport", "proponents": "Penrose, Hameroff", "tau_d_predicted": "10⁻⁶ to 10⁻³ s", "status": "Theoretical — no direct measurement"},
            {"mechanism": "Ion channel selectivity filter tunneling", "proponents": "Summhammer, Salari", "tau_d_predicted": "10⁻⁹ to 10⁻⁶ s", "status": "Indirect evidence (anomalous selectivity)"},
            {"mechanism": "Posner molecule nuclear spin", "proponents": "Fisher", "tau_d_predicted": "10⁰ to 10³·⁶ s (hours)", "status": "Theoretical — Posner existence in cortex unconfirmed"},
            {"mechanism": "Synaptic vesicle quantum tunneling", "proponents": "Beck, Eccles", "tau_d_predicted": "10⁻¹² to 10⁻⁹ s", "status": "Speculative — no direct evidence"},
        ],
    },

    # What changes in the framework if triggered
    "changes": {
        "determinacy_spectrum": {
            "current": {"N7": "Quantum Uncertain (Level 6)", "N6": "Chaotic → QU (Level 5)"},
            "post_proof": {"N7": "Quantum Indeterminate (Level 7)", "N6": "Quantum Uncertain (Level 6)"},
            "description": "N7 upgrades from Heisenberg-bounded uncertainty to confirmed quantum indeterminacy. N6 (limbic, with hippocampal synapses) upgrades one level.",
        },
        "decoherence_gate": {
            "current": "ΓD(t) = e^(-t/τ_D), τ_D unknown → quantum terms gated (may be ≈0)",
            "post_proof": "ΓD(t) measured experimentally. Quantum terms ALWAYS active for implanted BCIs at I0.",
            "implication": "The (1-ΓD) factor in Σq is no longer speculative. It has a measured value.",
        },
        "qi_equation": {
            "current": "Σq(b,t) = (1-ΓD(t))·[ψ₁·Q̂i(b) - ψ₃·Q̂e(b)] + ψ₂·Q̂t(b) — quantum terms conditional",
            "post_proof": "Same equation, but ΓD ≠ 1 confirmed → quantum terms contribute measurable signal",
            "implication": "QI score becomes provably richer than any classical-only metric for implanted BCIs",
        },
        "no_cloning": {
            "current": "Theoretical — no-cloning protects I0 IF quantum states exist there",
            "post_proof": "PROVEN — neural quantum states at I0 are physically unclonable",
            "implication": "Unforgeable neural identity. No adversary can perfectly replicate a user's quantum neural signature. This is a mathematical theorem, not an engineering claim.",
        },
        "security_advantage": {
            "current": "Classical QI (Cs) is the practical metric. Quantum terms are theoretical upside.",
            "post_proof": "Quantum QI provides provable security advantage over any classical-only metric",
            "implication": "QIF becomes the ONLY framework that captures the full physics. No competitor can match it without quantum terms.",
        },
        "bands_affected": {
            "N7": "Determinacy upgrades. Quantum terms always active for cortical BCIs.",
            "N6": "Determinacy upgrades. Limbic quantum effects at hippocampal synapses.",
            "N5": "Possible upgrade — basal ganglia dopaminergic synapses may show quantum tunneling",
            "N4": "Possible upgrade — thalamic relay synapses",
            "N3": "No change expected — cerebellar Purkinje cells are classical-dominant (high firing rate)",
            "N2": "No change expected — brainstem circuits are classical reflex arcs",
            "N1": "No change expected — spinal cord is classical",
            "I0": "MAJOR change — quantum channel confirmed at electrode-tissue boundary",
            "S1-S3": "No change — silicon is classical by definition",
        },
        "threat_model_additions": [
            {
                "attack": "Quantum state injection at I0",
                "description": "Attacker prepares quantum states matching expected neural signatures to bypass no-cloning defense",
                "feasibility": "Requires quantum computer + knowledge of user's quantum state → near-impossible (double protection)",
                "defense": "No-cloning theorem + measurement disturbance (Heisenberg) = two independent quantum barriers",
            },
            {
                "attack": "Decoherence acceleration attack",
                "description": "Deliberately increase decoherence (heat, EM noise) to collapse quantum security advantage back to classical-only",
                "feasibility": "Moderate — thermal/EM attacks already cataloged (ADS, Frey effect)",
                "defense": "Resonance shield (Entry 28) + thermal monitoring at I0 + QI score includes classical baseline (falls back gracefully)",
            },
            {
                "attack": "Quantum side-channel (weak measurement)",
                "description": "Perform weak measurements on quantum neural states to extract partial information without full collapse",
                "feasibility": "Requires physical access to I0 + quantum measurement apparatus → nation-state only",
                "defense": "QI detects anomalous decoherence rate (ΓD changes under weak measurement). Tamper-evident.",
            },
        ],
    },

    # What stays the same
    "unchanged": [
        "QI = e^(-Σ) — master equation unchanged. Only the magnitude of quantum contribution changes.",
        "Classical terms (σ²φ, Hτ, σ²γ, Dsf) — unchanged. They work regardless of quantum proof.",
        "Silicon domain (S1-S3) — classical by definition, unaffected.",
        "Consumer devices — still classical-only (scalp EEG, ΓD ≈ 1). Quantum proof doesn't help non-invasive.",
        "PQC (post-quantum cryptography) — still needed for S1-S3. Quantum proof helps I0/neural only.",
        "Three-layer defense architecture (shield + QI + TTT) — all three still needed.",
        "Attack coupling mechanisms — same 5 mechanisms. Quantum adds I0-specific attacks but doesn't change S→N chain.",
    ],

    # Timeline estimate
    "timeline": {
        "optimistic": "2028-2030 (rapid progress in quantum biology, multiple labs pursuing)",
        "moderate": "2035-2040 (difficult experiments, replication challenges)",
        "pessimistic": "Never confirmed at security-relevant timescales (Tegmark wins)",
        "qif_position": "Framework is valid in ALL three scenarios. Classical-only if Tegmark. Enhanced if confirmed. No redesign needed either way.",
    },
}
