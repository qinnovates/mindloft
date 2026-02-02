"""
Physical Quantity Colormaps
Scientifically meaningful color mappings for neural data
"""

import numpy as np
from typing import Tuple


def create_blackbody_colormap(n_samples: int = 256) -> np.ndarray:
    """
    Temperature → Blackbody radiation colormap
    Maps 308K-312K (35°C-39°C) to visible spectrum approximation

    Args:
        n_samples: Number of color samples

    Returns:
        (n_samples, 3) uint8 array of RGB colors
    """
    T = np.linspace(308, 312, n_samples)

    # Simplified Planck-like coloring (not physically accurate, but evocative)
    # Cool temps: deep red, Body temp: orange-white, Fever: bright white-blue
    colors = np.zeros((n_samples, 3))

    t_norm = (T - 308) / 4  # 0 to 1

    # Red channel: always present
    colors[:, 0] = np.clip(0.5 + t_norm, 0, 1)

    # Green channel: rises with temperature
    colors[:, 1] = np.clip(t_norm * 1.5 - 0.2, 0, 1)

    # Blue channel: only at high temps
    colors[:, 2] = np.clip(t_norm * 2 - 1, 0, 1)

    return (colors * 255).astype(np.uint8)


def create_oxygenation_colormap(n_samples: int = 256) -> np.ndarray:
    """
    Blood flow oxygenation: blue (deoxygenated) → red (oxygenated)

    Args:
        n_samples: Number of color samples

    Returns:
        (n_samples, 3) uint8 array of RGB colors
    """
    saturation = np.linspace(0, 1, n_samples)
    colors = np.zeros((n_samples, 3))

    # Deoxy: dark blue (#1a237e), Oxy: bright red (#d32f2f)
    colors[:, 0] = 0.1 + 0.73 * saturation  # R: 26 → 211
    colors[:, 1] = 0.14 * (1 - saturation) + 0.18 * saturation  # G: 35 → 47
    colors[:, 2] = 0.49 * (1 - saturation) + 0.18 * saturation  # B: 126 → 47

    return (colors * 255).astype(np.uint8)


def create_voltage_colormap(n_samples: int = 256) -> np.ndarray:
    """
    Membrane potential colormap: -90mV (blue) to +50mV (magenta)

    Args:
        n_samples: Number of color samples

    Returns:
        (n_samples, 3) uint8 array of RGB colors
    """
    colors = np.zeros((n_samples, 3))

    for i in range(n_samples):
        t = i / (n_samples - 1)

        # 7-color gradient
        if t < 0.167:
            # Dark blue to blue
            s = t / 0.167
            colors[i] = [0.05 * (1-s) + 0.0 * s,
                        0.05 * (1-s) + 0.3 * s,
                        0.3 * (1-s) + 0.6 * s]
        elif t < 0.333:
            # Blue to teal
            s = (t - 0.167) / 0.167
            colors[i] = [0.0, 0.3 * (1-s) + 0.6 * s, 0.6 * (1-s) + 0.4 * s]
        elif t < 0.5:
            # Teal to green
            s = (t - 0.333) / 0.167
            colors[i] = [0.0 * (1-s) + 0.4 * s,
                        0.6 * (1-s) + 0.8 * s,
                        0.4 * (1-s) + 0.2 * s]
        elif t < 0.667:
            # Green to yellow
            s = (t - 0.5) / 0.167
            colors[i] = [0.4 * (1-s) + 0.9 * s,
                        0.8 * (1-s) + 0.7 * s,
                        0.2 * (1-s) + 0.0 * s]
        elif t < 0.833:
            # Yellow to orange
            s = (t - 0.667) / 0.167
            colors[i] = [0.9 * (1-s) + 1.0 * s,
                        0.7 * (1-s) + 0.3 * s,
                        0.0]
        else:
            # Orange to magenta
            s = (t - 0.833) / 0.167
            colors[i] = [1.0, 0.3 * (1-s) + 0.0 * s, 0.0 * (1-s) + 0.3 * s]

    return (colors * 255).astype(np.uint8)


def create_ion_charge_colormap(n_samples: int = 256) -> np.ndarray:
    """
    Ion charge colormap: -2 (cyan) to +2 (red)
    Neutral at green

    Args:
        n_samples: Number of color samples

    Returns:
        (n_samples, 3) uint8 array of RGB colors
    """
    charge = np.linspace(-2, 2, n_samples)
    colors = np.zeros((n_samples, 3))

    for i, c in enumerate(charge):
        if c < 0:
            # Negative: cyan to green
            t = (c + 2) / 2  # 0 to 1
            colors[i] = [0, 0.5 + 0.5 * t, 1 - t]
        else:
            # Positive: green to red
            t = c / 2  # 0 to 1
            colors[i] = [t, 1 - 0.5 * t, 0]

    return (colors * 255).astype(np.uint8)


def create_calcium_colormap(n_samples: int = 256) -> np.ndarray:
    """
    Calcium concentration colormap: low (dark) to high (bright green-yellow)

    Args:
        n_samples: Number of color samples

    Returns:
        (n_samples, 3) uint8 array of RGB colors
    """
    conc = np.linspace(0, 1, n_samples)
    colors = np.zeros((n_samples, 3))

    # Dark green to bright yellow-green
    colors[:, 0] = conc ** 0.7  # Red increases
    colors[:, 1] = 0.3 + 0.7 * conc  # Green high throughout
    colors[:, 2] = 0.1 * (1 - conc)  # Blue decreases

    return (colors * 255).astype(np.uint8)


def create_diverging_colormap(n_samples: int = 256,
                              low_color: Tuple[float, float, float] = (0.2, 0.3, 0.8),
                              mid_color: Tuple[float, float, float] = (0.95, 0.95, 0.95),
                              high_color: Tuple[float, float, float] = (0.8, 0.2, 0.2)) -> np.ndarray:
    """
    Diverging colormap with neutral midpoint

    Args:
        n_samples: Number of color samples
        low_color: RGB tuple for low values
        mid_color: RGB tuple for midpoint
        high_color: RGB tuple for high values

    Returns:
        (n_samples, 3) uint8 array of RGB colors
    """
    colors = np.zeros((n_samples, 3))
    mid = n_samples // 2

    for i in range(n_samples):
        if i < mid:
            t = i / mid
            colors[i] = [
                low_color[0] * (1-t) + mid_color[0] * t,
                low_color[1] * (1-t) + mid_color[1] * t,
                low_color[2] * (1-t) + mid_color[2] * t
            ]
        else:
            t = (i - mid) / (n_samples - mid - 1)
            colors[i] = [
                mid_color[0] * (1-t) + high_color[0] * t,
                mid_color[1] * (1-t) + high_color[1] * t,
                mid_color[2] * (1-t) + high_color[2] * t
            ]

    return (colors * 255).astype(np.uint8)


def apply_colormap(data: np.ndarray, colormap: np.ndarray,
                   vmin: float = None, vmax: float = None) -> np.ndarray:
    """
    Apply colormap to data array

    Args:
        data: Input data array
        colormap: (n_samples, 3) colormap array
        vmin: Minimum value for normalization
        vmax: Maximum value for normalization

    Returns:
        (data.shape, 3) RGB array
    """
    if vmin is None:
        vmin = np.min(data)
    if vmax is None:
        vmax = np.max(data)

    # Normalize to [0, 1]
    if vmax > vmin:
        normalized = (data - vmin) / (vmax - vmin)
    else:
        normalized = np.zeros_like(data)

    normalized = np.clip(normalized, 0, 1)

    # Map to colormap indices
    indices = (normalized * (len(colormap) - 1)).astype(int)

    # Apply colormap
    return colormap[indices]
