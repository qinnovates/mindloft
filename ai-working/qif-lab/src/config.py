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
    "layer_model_version": "v2.0",
    "layer_model_date": "2026-01-22",
    "github": "qinnovates/qinnovate",
    "authors": "Kevin Qi, with Claude (Anthropic)",
    "collaboration": "Quantum Intelligence (QI)",
}

# ──────────────────────────────────────────────
# Layer Architecture
# ──────────────────────────────────────────────

LAYERS = [
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
# Neuralink N1 Specs
# ──────────────────────────────────────────────

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
    {"attack": "Signal injection",            "layers": "L9-L10",  "classical": "Yes",     "quantum": "Enhanced (coherence metric)"},
    {"attack": "Neural ransomware",           "layers": "L12-L13", "classical": "Partial",  "quantum": "Yes (QI score drop)"},
    {"attack": "Eavesdropping",               "layers": "L8-L9",   "classical": "No",       "quantum": "Yes (Heisenberg disturbance)"},
    {"attack": "Man-in-the-middle",           "layers": "L8",      "classical": "Partial",  "quantum": "Yes (no-cloning + Bell test)"},
    {"attack": "Quantum tunneling exploit",   "layers": "L8-L9",   "classical": "No",       "quantum": "Yes (tunneling profile anomaly)"},
    {"attack": "Davydov soliton attack",      "layers": "L8-L9",   "classical": "No",       "quantum": "Yes (tunneling term Qtunnel)"},
    {"attack": "Harvest-now-decrypt-later",   "layers": "L6-L7",   "classical": "No",       "quantum": "Prevented (QKD)"},
    {"attack": "Identity spoofing",           "layers": "L14",     "classical": "Partial",  "quantum": "Yes (quantum biometric)"},
]
