# ONI Framework

**Organic Neural Interface Framework** - A Python library for brain-computer interface security.

[![PyPI version](https://badge.fury.io/py/oni-framework.svg)](https://badge.fury.io/py/oni-framework)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Tests](https://github.com/qikevinl/ONI/actions/workflows/tests.yml/badge.svg)](https://github.com/qikevinl/ONI/actions/workflows/tests.yml)

> **Research Status:** This library implements theoretical frameworks for BCI security that have not yet been empirically validated. It is intended for research, experimentation, and to provide shared vocabulary for the emerging field of neural interface security. The mathematical models (Cₛ coherence metric, f × S ≈ k invariant) are derived from neuroscience literature but require experimental validation against real BCI data. Contributions and validation efforts are welcome.

## Overview

The ONI Framework provides tools for validating and securing neural signals at the brain-computer interface boundary. It implements:

- **Coherence Metric (Cₛ)** - Quantify signal trustworthiness across timing, pathway, and amplitude dimensions
- **14-Layer Model** - Unified architecture bridging biological (L1-L7) and silicon (L9-L14) domains
- **Neural Firewall** - Zero-trust signal filtering at the Neural Gateway (L8)
- **Scale-Frequency Invariant** - Validate signals against the f × S ≈ k constraint

## Installation

```bash
# From PyPI (recommended)
pip install oni-framework

# With visualization support
pip install oni-framework[viz]

# From source (for development)
git clone https://github.com/qikevinl/ONI.git
cd ONI/MAIN/oni-framework
pip install -e ".[dev]"
```

## Quick Start

### Calculate Coherence Score

```python
from oni import CoherenceMetric, calculate_cs

# Create metric with 40 Hz gamma reference
metric = CoherenceMetric(reference_freq=40.0)

# Sample signal data
arrival_times = [0.0, 0.025, 0.050, 0.075, 0.100]  # seconds
amplitudes = [100, 98, 102, 99, 101]  # μV

# Calculate coherence
cs = metric.calculate(arrival_times, amplitudes)
print(f"Coherence Score: {cs:.3f}")

# Interpret the score
level, description = metric.interpret(cs)
print(f"{level}: {description}")
```

### Use the Neural Firewall

```python
from oni import NeuralFirewall, Signal

# Create firewall with default thresholds
firewall = NeuralFirewall(
    threshold_high=0.6,
    threshold_low=0.3,
    amplitude_bounds=(0, 500),  # μV limits
)

# Create a signal to validate
signal = Signal(
    arrival_times=[0.0, 0.025, 0.050],
    amplitudes=[100, 98, 102],
    authenticated=True,
)

# Filter the signal
result = firewall.filter(signal)

print(f"Decision: {result.decision.name}")
print(f"Coherence: {result.coherence:.3f}")
print(f"Alert Level: {result.alert_level.name}")
print(f"Reason: {result.reason}")
```

### Explore the 14-Layer Model

```python
from oni import ONIStack

stack = ONIStack()

# Print the stack diagram
print(stack.ascii_diagram())

# Access specific layers
gateway = stack.layer(8)  # Neural Gateway
print(f"Layer 8: {gateway.name}")
print(f"Function: {gateway.function}")
print(f"Attack surfaces: {gateway.attack_surfaces}")

# Iterate through biological layers
for layer in stack.biological_layers():
    print(f"L{layer.number}: {layer.name}")
```

### Validate Scale-Frequency Relationship

```python
from oni import ScaleFrequencyInvariant

sfi = ScaleFrequencyInvariant()

# Check if 40 Hz at 100 μm scale is valid
frequency = 40  # Hz
spatial_scale = 1e-4  # meters (100 μm)

is_valid = sfi.validate(frequency, spatial_scale)
deviation = sfi.deviation(frequency, spatial_scale)

print(f"Valid: {is_valid}")
print(f"Deviation from k: {deviation:.1%}")

# Get expected frequency for a scale
expected_f = sfi.expected_frequency(spatial_scale=1e-3)
print(f"Expected frequency at 1mm: {expected_f:.1f} Hz")

# Print hierarchy report
print(sfi.hierarchy_report())
```

## Core Concepts

### Coherence Metric Formula

```
Cₛ = e^(−(σ²φ + σ²τ + σ²γ))

Where:
- σ²φ = phase variance (timing jitter)
- σ²τ = transport variance (pathway integrity)
- σ²γ = gain variance (amplitude stability)
```

### Firewall Decision Matrix

| Coherence | Authentication | Decision |
|-----------|----------------|----------|
| High (>0.6) | Valid | ACCEPT |
| High (>0.6) | Invalid | REJECT |
| Medium (0.3-0.6) | Valid | ACCEPT + FLAG |
| Medium (0.3-0.6) | Invalid | REJECT |
| Low (<0.3) | Any | REJECT |

### Scale-Frequency Invariant

```
f × S ≈ k (constant)

Higher frequencies → Smaller spatial scales
Lower frequencies → Larger spatial scales
```

## Project Structure

```
oni-framework/
├── oni/
│   ├── __init__.py      # Package exports
│   ├── coherence.py     # Cₛ calculation
│   ├── layers.py        # 14-layer model
│   ├── firewall.py      # Signal filtering
│   └── scale_freq.py    # f × S ≈ k invariant
├── tests/
│   └── test_*.py        # Unit tests
├── pyproject.toml       # Package configuration
└── README.md            # This file
```

## API Reference

### `oni.CoherenceMetric`

- `calculate(arrival_times, amplitudes)` → Coherence score (0-1)
- `calculate_variances(...)` → Individual variance components
- `interpret(cs)` → (level, description) tuple

### `oni.NeuralFirewall`

- `filter(signal)` → FilterResult with decision
- `filter_batch(signals)` → List of FilterResults
- `get_stats()` → Filtering statistics
- `register_callback(level, fn)` → Alert callbacks

### `oni.ONIStack`

- `layer(n)` → Get layer by number (1-14)
- `biological_layers()` → L1-L7
- `silicon_layers()` → L9-L14
- `bridge_layer()` → L8 (Neural Gateway)
- `ascii_diagram()` → Visual representation

### `oni.ScaleFrequencyInvariant`

- `validate(frequency, scale)` → Boolean validity
- `deviation(frequency, scale)` → Fractional deviation
- `expected_frequency(scale)` → Predicted frequency
- `anomaly_score(frequency, scale)` → 0-1 anomaly score

## Research Background

This library implements concepts from the ONI Framework research:

- [ONI Framework Overview](../publications/0-oni-framework/)
- [Coherence Metric Technical Document](../publications/coherence-metric/)
- [Neural Firewall Architecture](../publications/neural-firewall/)
- [Scale-Frequency Invariant](../publications/scale-frequency/)

## Contributing

Contributions welcome! See [CONTRIBUTING.md](../../CONTRIBUTING.md) for guidelines.

**Seeking input from:**
- Neuroscientists — Validate biological assumptions
- Security engineers — Identify attack vectors
- BCI researchers — Test against real data

## License

Apache License 2.0 - See [LICENSE](../../LICENSE)

## Citation

If you use this library in research, please cite:

```bibtex
@software{oni_framework,
  author = {Qi, Kevin L.},
  title = {ONI Framework: Security Library for Brain-Computer Interfaces},
  year = {2026},
  url = {https://github.com/qikevinl/ONI}
}
```
