"""
ONI Framework - Organic Neural Interface Security Library

A Python implementation of the ONI Framework for brain-computer interface security.
Provides tools for signal validation, coherence metrics, and neural firewall simulation.

Author: Kevin L. Qi
License: Apache 2.0
"""

__version__ = "0.1.0"
__author__ = "Kevin L. Qi"

from .coherence import CoherenceMetric, calculate_cs
from .layers import ONIStack, Layer
from .firewall import NeuralFirewall
from .scale_freq import ScaleFrequencyInvariant

__all__ = [
    "CoherenceMetric",
    "calculate_cs",
    "ONIStack",
    "Layer",
    "NeuralFirewall",
    "ScaleFrequencyInvariant",
]
