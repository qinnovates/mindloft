"""
ONI Framework - Organic Neural Interface Security Library

A Python implementation of the ONI Framework for brain-computer interface security.
Provides tools for signal validation, coherence metrics, and neural firewall simulation.

Includes neurosecurity components inspired by:
- Kohno et al. (2009): Neurosecurity threat model and CIA triad for BCIs
- Chizeck & Bonaci (2014): BCI Anonymizer architecture

Author: Kevin L. Qi
License: Apache 2.0
"""

__version__ = "0.2.0"
__author__ = "Kevin L. Qi"

from .coherence import CoherenceMetric, calculate_cs
from .layers import ONIStack, Layer
from .firewall import NeuralFirewall
from .scale_freq import ScaleFrequencyInvariant

# Neurosecurity module (Kohno 2009 + BCI Anonymizer implementation)
from .neurosecurity import (
    ThreatType,
    SecurityDecision,
    KohnoThreatModel,
    NeurosecurityFirewall,
    NeurosecurityConfig,
    BCIAnonymizer,
    AnonymizerConfig,
    ERPType,
    PrivacySensitivity,
    PrivacyScoreCalculator,
    PrivacyScoreResult,
)

__all__ = [
    # Core
    "CoherenceMetric",
    "calculate_cs",
    "ONIStack",
    "Layer",
    "NeuralFirewall",
    "ScaleFrequencyInvariant",
    # Neurosecurity (Kohno 2009)
    "ThreatType",
    "SecurityDecision",
    "KohnoThreatModel",
    "NeurosecurityFirewall",
    "NeurosecurityConfig",
    # BCI Anonymizer (Chizeck & Bonaci 2014)
    "BCIAnonymizer",
    "AnonymizerConfig",
    "ERPType",
    "PrivacySensitivity",
    # Privacy Score
    "PrivacyScoreCalculator",
    "PrivacyScoreResult",
]
