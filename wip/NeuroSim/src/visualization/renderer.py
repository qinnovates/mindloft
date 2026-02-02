"""
Real-Time Visualization Engine
Multi-scale neural rendering with OpenGL/WebGL
"""

import numpy as np
from dataclasses import dataclass, field
from typing import Dict, List, Tuple, Optional, Callable
from enum import Enum


class RenderMode(Enum):
    """Visualization scale modes"""
    MOLECULAR = 1       # Ion probability densities
    CELLULAR = 2        # Neuron morphologies
    NETWORK = 3         # Fiber tracts/connections
    COMBINED = 4        # Multi-scale view


@dataclass
class Camera:
    """3D camera for scene navigation"""
    position: np.ndarray = field(default_factory=lambda: np.array([0., 0., 500.]))
    target: np.ndarray = field(default_factory=lambda: np.array([0., 0., 0.]))
    up: np.ndarray = field(default_factory=lambda: np.array([0., 1., 0.]))
    fov: float = 45.0
    near: float = 0.1
    far: float = 10000.0

    def get_view_matrix(self) -> np.ndarray:
        """Compute view matrix (camera transform)"""
        f = self.target - self.position
        f = f / np.linalg.norm(f)
        r = np.cross(f, self.up)
        r = r / np.linalg.norm(r)
        u = np.cross(r, f)

        view = np.eye(4)
        view[0, :3] = r
        view[1, :3] = u
        view[2, :3] = -f
        view[:3, 3] = -np.array([np.dot(r, self.position),
                                  np.dot(u, self.position),
                                  np.dot(-f, self.position)])
        return view

    def orbit(self, delta_azimuth: float, delta_elevation: float):
        """Orbit camera around target"""
        # Convert to spherical coordinates
        offset = self.position - self.target
        r = np.linalg.norm(offset)
        theta = np.arctan2(offset[0], offset[2])
        phi = np.arcsin(offset[1] / r)

        # Apply rotation
        theta += delta_azimuth
        phi = np.clip(phi + delta_elevation, -np.pi/2 + 0.1, np.pi/2 - 0.1)

        # Convert back
        self.position = self.target + r * np.array([
            np.sin(theta) * np.cos(phi),
            np.sin(phi),
            np.cos(theta) * np.cos(phi)
        ])

    def zoom(self, factor: float):
        """Zoom camera (move along view direction)"""
        direction = self.target - self.position
        distance = np.linalg.norm(direction)
        new_distance = distance * factor
        self.position = self.target - (direction / distance) * new_distance


@dataclass
class RenderBuffer:
    """GPU buffer specification"""
    vertex_buffer: int = 0    # VBO handle
    index_buffer: int = 0     # EBO handle
    vertex_array: int = 0     # VAO handle
    n_vertices: int = 0
    n_indices: int = 0


@dataclass
class DashboardPanel:
    """Specification for a dashboard visualization panel"""
    title: str
    x_label: str
    y_label: str
    data_source: str      # Key into simulation data
    plot_type: str        # 'line', 'heatmap', 'spectrogram', 'histogram'
    update_rate_hz: float = 30.0
    history_seconds: float = 10.0

    # Visual properties
    color: Tuple[float, float, float] = (0.2, 0.6, 0.9)
    line_width: float = 2.0
    y_range: Optional[Tuple[float, float]] = None


class Dashboard:
    """Real-time data visualization dashboard"""

    def __init__(self, layout: Tuple[int, int] = (3, 3)):
        self.rows, self.cols = layout
        self.panels: List[Optional[DashboardPanel]] = [None] * (self.rows * self.cols)

    def configure_default_layout(self):
        """Set up standard neuroscience dashboard"""

        # Row 1: Electrophysiology
        self.panels[0] = DashboardPanel(
            title="Population Firing Rate",
            x_label="Time (s)",
            y_label="Rate (Hz)",
            data_source="population_rate",
            plot_type="line",
            y_range=(0, 100)
        )

        self.panels[1] = DashboardPanel(
            title="Power Spectrum (0-100 Hz)",
            x_label="Frequency (Hz)",
            y_label="Power (μV²/Hz)",
            data_source="lfp_power_spectrum",
            plot_type="line",
            y_range=(0, None)
        )

        self.panels[2] = DashboardPanel(
            title="Spectrogram",
            x_label="Time (s)",
            y_label="Frequency (Hz)",
            data_source="lfp_spectrogram",
            plot_type="heatmap",
            y_range=(0, 100)
        )

        # Row 2: Information Theory
        self.panels[3] = DashboardPanel(
            title="Population Entropy",
            x_label="Time (s)",
            y_label="Entropy (bits)",
            data_source="population_entropy",
            plot_type="line",
            color=(0.9, 0.4, 0.2)
        )

        self.panels[4] = DashboardPanel(
            title="Mutual Information",
            x_label="Time (s)",
            y_label="MI (bits)",
            data_source="mutual_information",
            plot_type="line",
            color=(0.2, 0.8, 0.4)
        )

        self.panels[5] = DashboardPanel(
            title="Transfer Entropy",
            x_label="Source → Target",
            y_label="TE (bits)",
            data_source="transfer_entropy_matrix",
            plot_type="heatmap"
        )

        # Row 3: Energetics
        self.panels[6] = DashboardPanel(
            title="ATP Consumption",
            x_label="Time (s)",
            y_label="ATP (mM/s)",
            data_source="atp_consumption_rate",
            plot_type="line",
            color=(0.8, 0.2, 0.6)
        )

        self.panels[7] = DashboardPanel(
            title="Energy Efficiency",
            x_label="Time (s)",
            y_label="bits/ATP × 10⁸",
            data_source="bits_per_atp",
            plot_type="line",
            color=(0.4, 0.7, 0.9)
        )

        self.panels[8] = DashboardPanel(
            title="Efficiency Distribution",
            x_label="bits/Joule",
            y_label="Count",
            data_source="efficiency_histogram",
            plot_type="histogram",
            color=(0.6, 0.5, 0.8)
        )


class NeuroVisualizer:
    """
    Main visualization engine for multi-scale neural rendering

    Note: This is a specification/pseudocode implementation.
    Actual OpenGL calls would require PyOpenGL or similar.
    """

    def __init__(self, width: int = 1920, height: int = 1080):
        self.width = width
        self.height = height
        self.camera = Camera()

        # Shader programs (would be compiled handles)
        self.shaders: Dict[str, int] = {}

        # Render buffers for different scales
        self.buffers: Dict[str, RenderBuffer] = {}

        # Colormaps (would be texture handles)
        self.colormaps: Dict[str, int] = {}

        # Render targets for post-processing
        self.framebuffers: Dict[str, int] = {}

        # Time tracking
        self.time = 0.0

        # Dashboard
        self.dashboard = Dashboard()
        self.dashboard.configure_default_layout()

    def initialize(self):
        """Initialize OpenGL context and resources"""
        # In actual implementation:
        # - Create OpenGL context
        # - Compile shaders
        # - Create textures for colormaps
        # - Set up framebuffers
        print("NeuroVisualizer initialized")
        print(f"Resolution: {self.width}x{self.height}")

    def update_ion_cloud(self, ion_type: str,
                         positions: np.ndarray,
                         probabilities: np.ndarray):
        """
        Update ion probability density visualization

        Args:
            ion_type: 'Na', 'K', 'Ca', 'Cl'
            positions: (N, 3) array of particle positions
            probabilities: (N,) array of probability densities
        """
        charge_map = {'Na': 1.0, 'K': 1.0, 'Ca': 2.0, 'Cl': -1.0}
        charges = np.full(len(positions), charge_map.get(ion_type, 0))

        # Interleave data: position (3) + charge (1) + probability (1)
        vertex_data = np.zeros((len(positions), 5), dtype=np.float32)
        vertex_data[:, :3] = positions
        vertex_data[:, 3] = charges
        vertex_data[:, 4] = probabilities

        buffer_key = f'ion_{ion_type}'
        if buffer_key not in self.buffers:
            self.buffers[buffer_key] = RenderBuffer()

        # Would upload to GPU here
        self.buffers[buffer_key].n_vertices = len(positions)

    def update_neuron_morphology(self, neuron_id: int,
                                  vertices: np.ndarray,
                                  normals: np.ndarray,
                                  voltages: np.ndarray,
                                  indices: np.ndarray,
                                  compartment_types: np.ndarray):
        """
        Update neuron surface mesh with voltage data

        Args:
            neuron_id: Unique identifier
            vertices: (N, 3) vertex positions
            normals: (N, 3) surface normals
            voltages: (N,) membrane potential at each vertex
            indices: (M, 3) triangle indices
            compartment_types: (N,) 0=soma, 1=axon, 2=dendrite
        """
        # Interleave: position (3) + normal (3) + voltage (1) + type (1)
        vertex_data = np.zeros((len(vertices), 8), dtype=np.float32)
        vertex_data[:, :3] = vertices
        vertex_data[:, 3:6] = normals
        vertex_data[:, 6] = voltages
        vertex_data[:, 7] = compartment_types.astype(np.float32)

        buffer_key = f'neuron_{neuron_id}'
        if buffer_key not in self.buffers:
            self.buffers[buffer_key] = RenderBuffer()

        self.buffers[buffer_key].n_vertices = len(vertices)
        self.buffers[buffer_key].n_indices = len(indices.flatten())

    def update_fiber_tracts(self, connections: List[Dict]):
        """
        Update network connectivity visualization

        Args:
            connections: List of dicts with 'points', 'strength'
        """
        all_points = []
        all_strengths = []
        all_params = []

        for conn in connections:
            points = conn['points']  # (M, 3) curve through space
            strength = conn['strength']

            n_points = len(points)
            params = np.linspace(0, 1, n_points)

            all_points.append(points)
            all_strengths.append(np.full(n_points, strength))
            all_params.append(params)

        if all_points:
            combined_points = np.vstack(all_points)
            combined_strengths = np.hstack(all_strengths)
            combined_params = np.hstack(all_params)

            vertex_data = np.zeros((len(combined_points), 5), dtype=np.float32)
            vertex_data[:, :3] = combined_points
            vertex_data[:, 3] = combined_strengths
            vertex_data[:, 4] = combined_params

            if 'fiber_tracts' not in self.buffers:
                self.buffers['fiber_tracts'] = RenderBuffer()
            self.buffers['fiber_tracts'].n_vertices = len(combined_points)

    def _perspective_matrix(self) -> np.ndarray:
        """Compute perspective projection matrix"""
        aspect = self.width / self.height
        f = 1.0 / np.tan(np.radians(self.camera.fov) / 2)

        proj = np.zeros((4, 4))
        proj[0, 0] = f / aspect
        proj[1, 1] = f
        proj[2, 2] = (self.camera.far + self.camera.near) / (self.camera.near - self.camera.far)
        proj[2, 3] = (2 * self.camera.far * self.camera.near) / (self.camera.near - self.camera.far)
        proj[3, 2] = -1
        return proj

    def render_frame(self, mode: RenderMode,
                     simulation_state=None) -> np.ndarray:
        """
        Render single frame

        Args:
            mode: Visualization mode
            simulation_state: Optional NeuralFieldState

        Returns:
            (height, width, 4) RGBA image array
        """
        # Would clear framebuffer here
        # glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        view = self.camera.get_view_matrix()
        projection = self._perspective_matrix()
        mvp = projection @ view

        if mode in [RenderMode.MOLECULAR, RenderMode.COMBINED]:
            self._render_ion_clouds(mvp)

        if mode in [RenderMode.CELLULAR, RenderMode.COMBINED]:
            self._render_neurons(mvp, view)

        if mode in [RenderMode.NETWORK, RenderMode.COMBINED]:
            self._render_fiber_tracts(mvp)

        # Update time
        self.time += 1/60  # Assuming 60 FPS

        # Would read framebuffer here
        frame = np.zeros((self.height, self.width, 4), dtype=np.uint8)
        return frame

    def _render_ion_clouds(self, mvp: np.ndarray):
        """Render molecular scale: ion probability isosurfaces"""
        # Would use additive blending
        # glEnable(GL_BLEND)
        # glBlendFunc(GL_SRC_ALPHA, GL_ONE)

        for ion in ['Na', 'K', 'Ca', 'Cl']:
            buffer_key = f'ion_{ion}'
            if buffer_key in self.buffers:
                # glUseProgram(self.shaders['ion_cloud'])
                # Set uniforms, bind buffers, draw
                pass

    def _render_neurons(self, mvp: np.ndarray, view: np.ndarray):
        """Render cellular scale: neuron morphologies"""
        # Standard depth-tested rendering
        # glEnable(GL_DEPTH_TEST)

        for key, buffer in self.buffers.items():
            if key.startswith('neuron_'):
                # glUseProgram(self.shaders['neuron'])
                # Set uniforms, bind buffers, draw triangles
                pass

    def _render_fiber_tracts(self, mvp: np.ndarray):
        """Render network scale: connection streamlines"""
        if 'fiber_tracts' in self.buffers:
            # glUseProgram(self.shaders['fiber_tract'])
            # glDrawArrays(GL_LINE_STRIP, ...)
            pass


class MetricsComputer:
    """Compute dashboard metrics from simulation state"""

    def __init__(self, sampling_rate: float = 1000.0):
        self.fs = sampling_rate
        self.history = {}

    def compute_power_spectrum(self, signal: np.ndarray,
                               nperseg: int = 1024) -> Tuple[np.ndarray, np.ndarray]:
        """Compute power spectral density"""
        try:
            from scipy.signal import welch
            freqs, psd = welch(signal, fs=self.fs, nperseg=nperseg)
            return freqs, psd
        except ImportError:
            # Fallback: simple FFT-based estimate
            n = len(signal)
            freqs = np.fft.rfftfreq(n, 1/self.fs)
            psd = np.abs(np.fft.rfft(signal))**2 / n
            return freqs, psd

    def compute_entropy(self, spike_counts: np.ndarray,
                        n_bins: int = 20) -> float:
        """Shannon entropy of spike count distribution"""
        hist, _ = np.histogram(spike_counts, bins=n_bins, density=True)
        hist = hist[hist > 0]  # Remove zeros
        return -np.sum(hist * np.log2(hist + 1e-10)) * (spike_counts.max() / n_bins)

    def compute_mutual_information(self, x: np.ndarray,
                                   y: np.ndarray,
                                   n_bins: int = 10) -> float:
        """Mutual information between two signals"""
        hist_2d, _, _ = np.histogram2d(x, y, bins=n_bins, density=True)
        hist_x = np.sum(hist_2d, axis=1)
        hist_y = np.sum(hist_2d, axis=0)

        # I(X;Y) = H(X) + H(Y) - H(X,Y)
        H_x = -np.sum(hist_x[hist_x > 0] * np.log2(hist_x[hist_x > 0] + 1e-10))
        H_y = -np.sum(hist_y[hist_y > 0] * np.log2(hist_y[hist_y > 0] + 1e-10))
        H_xy = -np.sum(hist_2d[hist_2d > 0] * np.log2(hist_2d[hist_2d > 0] + 1e-10))

        return max(0, H_x + H_y - H_xy)

    def compute_bits_per_joule(self, information_rate: float,
                               power_watts: float) -> float:
        """Energy efficiency metric: bits/Joule"""
        if power_watts < 1e-15:
            return 0.0
        return information_rate / power_watts

    def compute_bits_per_atp(self, information_bits: float,
                             atp_molecules: float) -> float:
        """Molecular efficiency: bits per ATP molecule consumed"""
        if atp_molecules < 1:
            return 0.0
        return information_bits / atp_molecules
