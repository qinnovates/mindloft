"""
Spatial Discretization for Neural Simulation
Voxel-based grid with adaptive resolution
"""

import numpy as np
import scipy.sparse as sp
from dataclasses import dataclass
from typing import Tuple, Optional


@dataclass
class VoxelGrid:
    """
    Spatial discretization: 1 μm³ voxels
    Density: 10⁸ voxels/mm³ neural tissue
    """
    dx: float = 1e-6  # 1 μm voxel edge

    # Domain bounds (can be subregion of full brain)
    x_min: float = 0.0
    x_max: float = 1e-3  # 1 mm default (scalable)
    y_min: float = 0.0
    y_max: float = 1e-3
    z_min: float = 0.0
    z_max: float = 1e-3

    def __post_init__(self):
        """Calculate grid dimensions"""
        self.nx = int((self.x_max - self.x_min) / self.dx)
        self.ny = int((self.y_max - self.y_min) / self.dx)
        self.nz = int((self.z_max - self.z_min) / self.dx)
        self.n_voxels = self.nx * self.ny * self.nz

        # Coordinate arrays
        self.x = np.linspace(self.x_min + self.dx/2,
                             self.x_max - self.dx/2, self.nx)
        self.y = np.linspace(self.y_min + self.dx/2,
                             self.y_max - self.dx/2, self.ny)
        self.z = np.linspace(self.z_min + self.dx/2,
                             self.z_max - self.dx/2, self.nz)

    def create_field(self, initial_value: float = 0.0) -> np.ndarray:
        """Initialize a 3D scalar field"""
        return np.full((self.nx, self.ny, self.nz), initial_value, dtype=np.float64)

    def create_vector_field(self, initial_value: Tuple[float, float, float] = (0., 0., 0.)) -> np.ndarray:
        """Initialize a 3D vector field"""
        field = np.zeros((self.nx, self.ny, self.nz, 3), dtype=np.float64)
        field[:, :, :, 0] = initial_value[0]
        field[:, :, :, 1] = initial_value[1]
        field[:, :, :, 2] = initial_value[2]
        return field

    def laplacian_operator(self) -> sp.csr_matrix:
        """
        7-point stencil Laplacian for 3D diffusion
        ∇²f ≈ (f_{i+1} + f_{i-1} + f_{j+1} + f_{j-1} + f_{k+1} + f_{k-1} - 6f_{i,j,k}) / Δx²
        """
        n = self.n_voxels

        # Main diagonal: -6/dx²
        main_diag = -6 * np.ones(n) / (self.dx ** 2)

        # Off-diagonals for neighbors
        # x-neighbors (stride 1)
        x_diag = np.ones(n - 1) / (self.dx ** 2)
        # Zero out connections across y-boundaries
        for i in range(1, self.nx):
            x_diag[i * self.ny * self.nz - 1] = 0

        # y-neighbors (stride nx)
        y_diag = np.ones(n - self.nz) / (self.dx ** 2)

        # z-neighbors (stride nx*ny)
        z_diag = np.ones(n - self.nx * self.ny) / (self.dx ** 2)

        # Build sparse matrix
        diagonals = [
            main_diag,
            x_diag, x_diag,
            y_diag, y_diag,
            z_diag, z_diag
        ]
        offsets = [0, 1, -1, self.nz, -self.nz, self.nx * self.ny, -self.nx * self.ny]

        L = sp.diags(diagonals, offsets, shape=(n, n), format='csr')
        return L

    def gradient_operator(self, axis: int) -> sp.csr_matrix:
        """
        Central difference gradient operator for specified axis
        axis: 0=x, 1=y, 2=z
        """
        n = self.n_voxels

        if axis == 0:
            stride = 1
        elif axis == 1:
            stride = self.nz
        elif axis == 2:
            stride = self.nx * self.ny
        else:
            raise ValueError("axis must be 0, 1, or 2")

        # Central difference: (f_{i+1} - f_{i-1}) / (2*dx)
        pos_diag = np.ones(n - stride) / (2 * self.dx)
        neg_diag = -np.ones(n - stride) / (2 * self.dx)

        G = sp.diags([pos_diag, neg_diag], [stride, -stride],
                     shape=(n, n), format='csr')
        return G

    def index_to_coords(self, idx: int) -> Tuple[int, int, int]:
        """Convert flat index to (i, j, k) coordinates"""
        i = idx // (self.ny * self.nz)
        remainder = idx % (self.ny * self.nz)
        j = remainder // self.nz
        k = remainder % self.nz
        return i, j, k

    def coords_to_index(self, i: int, j: int, k: int) -> int:
        """Convert (i, j, k) coordinates to flat index"""
        return i * self.ny * self.nz + j * self.nz + k

    def position_to_index(self, x: float, y: float, z: float) -> Optional[int]:
        """Convert physical position to flat index, or None if outside domain"""
        if not (self.x_min <= x < self.x_max and
                self.y_min <= y < self.y_max and
                self.z_min <= z < self.z_max):
            return None

        i = int((x - self.x_min) / self.dx)
        j = int((y - self.y_min) / self.dx)
        k = int((z - self.z_min) / self.dx)

        return self.coords_to_index(i, j, k)

    def apply_boundary_conditions(self, field: np.ndarray,
                                   bc_type: str = 'neumann',
                                   bc_value: float = 0.0) -> np.ndarray:
        """
        Apply boundary conditions to field

        bc_type: 'dirichlet' (fixed value) or 'neumann' (zero flux)
        bc_value: boundary value for Dirichlet
        """
        if bc_type == 'dirichlet':
            field[0, :, :] = bc_value
            field[-1, :, :] = bc_value
            field[:, 0, :] = bc_value
            field[:, -1, :] = bc_value
            field[:, :, 0] = bc_value
            field[:, :, -1] = bc_value
        elif bc_type == 'neumann':
            # Zero-flux: copy interior values to boundaries
            field[0, :, :] = field[1, :, :]
            field[-1, :, :] = field[-2, :, :]
            field[:, 0, :] = field[:, 1, :]
            field[:, -1, :] = field[:, -2, :]
            field[:, :, 0] = field[:, :, 1]
            field[:, :, -1] = field[:, :, -2]
        else:
            raise ValueError(f"Unknown boundary condition type: {bc_type}")

        return field


class AdaptiveGrid:
    """
    Adaptive mesh refinement for multi-scale simulation
    Coarser resolution in bulk, finer near neurons
    """

    def __init__(self, base_grid: VoxelGrid, max_levels: int = 3):
        self.base_grid = base_grid
        self.max_levels = max_levels
        self.refinement_regions = []

    def add_refinement_region(self, center: Tuple[float, float, float],
                              radius: float, level: int):
        """Mark a spherical region for refinement"""
        self.refinement_regions.append({
            'center': np.array(center),
            'radius': radius,
            'level': min(level, self.max_levels)
        })

    def get_effective_dx(self, position: Tuple[float, float, float]) -> float:
        """Get effective voxel size at given position"""
        pos = np.array(position)
        dx = self.base_grid.dx

        for region in self.refinement_regions:
            dist = np.linalg.norm(pos - region['center'])
            if dist < region['radius']:
                dx = min(dx, self.base_grid.dx / (2 ** region['level']))

        return dx
