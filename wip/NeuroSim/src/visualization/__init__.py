"""
NeuroSim Visualization Module
Multi-scale rendering and publication figure generation
"""

from .shaders import (
    VERTEX_SHADER_MOLECULE,
    FRAGMENT_SHADER_ION_CLOUD,
    VERTEX_SHADER_NEURON,
    FRAGMENT_SHADER_MEMBRANE_POTENTIAL,
    VERTEX_SHADER_STREAMLINES,
    FRAGMENT_SHADER_FIBER_TRACT
)
from .renderer import NeuroVisualizer, Camera, RenderMode, RenderBuffer
from .colormaps import create_blackbody_colormap, create_oxygenation_colormap
from .figures import NeurogenesisPaperFigures, JournalSpec

__all__ = [
    # Shaders
    'VERTEX_SHADER_MOLECULE',
    'FRAGMENT_SHADER_ION_CLOUD',
    'VERTEX_SHADER_NEURON',
    'FRAGMENT_SHADER_MEMBRANE_POTENTIAL',
    'VERTEX_SHADER_STREAMLINES',
    'FRAGMENT_SHADER_FIBER_TRACT',
    # Renderer
    'NeuroVisualizer',
    'Camera',
    'RenderMode',
    'RenderBuffer',
    # Colormaps
    'create_blackbody_colormap',
    'create_oxygenation_colormap',
    # Figures
    'NeurogenesisPaperFigures',
    'JournalSpec'
]
