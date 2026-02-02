"""
Main Simulation Engine
Integrates all physical constraints for neural tissue simulation
"""

import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import spsolve
from dataclasses import dataclass, field
from typing import Dict, List, Callable, Optional

from .grid import VoxelGrid
from .constants import PhysicalConstants, IonProperties, MembraneProperties, MetabolicProperties
from .conservation import ConservationLaws, StochasticProcesses, TimeIntegrator


@dataclass
class NeuralFieldState:
    """
    Primary field variables: Φ(x,y,z,t), pO₂(x,y,z,t), Ca²⁺(x,y,z,t)
    """
    grid: VoxelGrid

    # Electric potential field (V)
    Phi: np.ndarray = None

    # Oxygen tension field (mmHg)
    pO2: np.ndarray = None

    # Calcium concentration field (M)
    Ca: np.ndarray = None

    # Ion concentrations (M)
    Na_i: np.ndarray = None
    Na_e: np.ndarray = None
    K_i: np.ndarray = None
    K_e: np.ndarray = None
    Cl_i: np.ndarray = None
    Cl_e: np.ndarray = None

    # Metabolic fields
    ATP: np.ndarray = None
    ADP: np.ndarray = None

    # Temperature field (K)
    T: np.ndarray = None

    def __post_init__(self):
        """Initialize all fields with physiological resting values"""
        self.Phi = self.grid.create_field(MembraneProperties.V_rest)
        self.pO2 = self.grid.create_field(MetabolicProperties.pO2_tissue)
        self.Ca = self.grid.create_field(IonProperties.C_Ca_i)
        self.Na_i = self.grid.create_field(IonProperties.C_Na_i)
        self.Na_e = self.grid.create_field(IonProperties.C_Na_e)
        self.K_i = self.grid.create_field(IonProperties.C_K_i)
        self.K_e = self.grid.create_field(IonProperties.C_K_e)
        self.Cl_i = self.grid.create_field(IonProperties.C_Cl_i)
        self.Cl_e = self.grid.create_field(IonProperties.C_Cl_e)
        self.ATP = self.grid.create_field(MetabolicProperties.C_ATP_rest)
        self.ADP = self.grid.create_field(MetabolicProperties.C_ADP_rest)
        self.T = self.grid.create_field(PhysicalConstants.T_body)

    def get_all_concentrations(self) -> Dict[str, np.ndarray]:
        """Return dictionary of all ion concentrations"""
        return {
            'Na_i': self.Na_i, 'Na_e': self.Na_e,
            'K_i': self.K_i, 'K_e': self.K_e,
            'Ca': self.Ca,
            'Cl_i': self.Cl_i, 'Cl_e': self.Cl_e
        }


class NeuroSimulator:
    """
    Main simulation engine integrating all physical constraints
    """

    def __init__(self, grid: VoxelGrid,
                 neurons: List = None):
        self.grid = grid
        self.state = NeuralFieldState(grid)
        self.time_integrator = TimeIntegrator()
        self.conservation = ConservationLaws()
        self.stochastic = StochasticProcesses()
        self.neurons = neurons or []

        # Precompute operators
        self.laplacian = grid.laplacian_operator()

        # Diffusion coefficients (m²/s)
        self.D = {
            'Na': IonProperties.D_Na,
            'K': IonProperties.D_K,
            'Ca': IonProperties.D_Ca,
            'Cl': IonProperties.D_Cl,
            'O2': IonProperties.D_O2,
            'ATP': IonProperties.D_ATP,
            'glutamate': IonProperties.D_glutamate
        }

        # Tracking
        self.t = 0.0
        self.history = []

        # Gating variables (will be initialized on first step)
        self.gating = None

    def _init_gating(self):
        """Initialize Hodgkin-Huxley gating variables"""
        self.gating = {
            'm': np.full_like(self.state.Phi, 0.05),
            'h': np.full_like(self.state.Phi, 0.6),
            'n': np.full_like(self.state.Phi, 0.32)
        }

    def compute_ion_currents(self, V: np.ndarray,
                             gating: Dict[str, np.ndarray]) -> Dict[str, np.ndarray]:
        """
        Hodgkin-Huxley currents with spatial distribution

        Returns:
            Dictionary with Na, K, L, and total currents (A/m²)
        """
        m, h, n = gating['m'], gating['h'], gating['n']

        # Conductances (S/m²)
        g_Na = MembraneProperties.g_Na_max * m**3 * h
        g_K = MembraneProperties.g_K_max * n**4
        g_L = MembraneProperties.g_L

        # Reversal potentials (Nernst equation)
        RT_F = PhysicalConstants.R * PhysicalConstants.T_body / PhysicalConstants.F

        E_Na = RT_F * np.log(self.state.Na_e / np.maximum(self.state.Na_i, 1e-10))
        E_K = RT_F * np.log(self.state.K_e / np.maximum(self.state.K_i, 1e-10))
        E_L = MembraneProperties.E_L

        I_Na = g_Na * (V - E_Na)
        I_K = g_K * (V - E_K)
        I_L = g_L * (V - E_L)

        return {'Na': I_Na, 'K': I_K, 'L': I_L, 'total': I_Na + I_K + I_L}

    def compute_gating_dynamics(self, V: np.ndarray,
                                gating: Dict[str, np.ndarray],
                                dt: float) -> Dict[str, np.ndarray]:
        """
        Update gating variables using Rush-Larsen method for stability

        Args:
            V: Membrane potential field (V)
            gating: Current gating variable values
            dt: Time step (s)

        Returns:
            Updated gating variables
        """
        V_mV = V * 1e3  # Convert to mV for rate equations

        # Rate functions (standard HH, voltage in mV)
        # Handle numerical edge cases with safe divisions
        def safe_alpha_m(v):
            x = v + 40
            return np.where(np.abs(x) < 1e-7,
                           1.0,
                           0.1 * x / (1 - np.exp(-x / 10)))

        def safe_alpha_n(v):
            x = v + 55
            return np.where(np.abs(x) < 1e-7,
                           0.1,
                           0.01 * x / (1 - np.exp(-x / 10)))

        alpha_m = safe_alpha_m(V_mV)
        beta_m = 4 * np.exp(-(V_mV + 65) / 18)
        alpha_h = 0.07 * np.exp(-(V_mV + 65) / 20)
        beta_h = 1 / (1 + np.exp(-(V_mV + 35) / 10))
        alpha_n = safe_alpha_n(V_mV)
        beta_n = 0.125 * np.exp(-(V_mV + 65) / 80)

        # Steady-state values
        m_inf = alpha_m / (alpha_m + beta_m)
        h_inf = alpha_h / (alpha_h + beta_h)
        n_inf = alpha_n / (alpha_n + beta_n)

        # Time constants
        tau_m = 1e-3 / (alpha_m + beta_m)  # Convert to seconds
        tau_h = 1e-3 / (alpha_h + beta_h)
        tau_n = 1e-3 / (alpha_n + beta_n)

        # Rush-Larsen update (exponential integrator)
        new_gating = {
            'm': m_inf + (gating['m'] - m_inf) * np.exp(-dt / tau_m),
            'h': h_inf + (gating['h'] - h_inf) * np.exp(-dt / tau_h),
            'n': n_inf + (gating['n'] - n_inf) * np.exp(-dt / tau_n)
        }

        return new_gating

    def compute_diffusion(self, C: np.ndarray, D: float, dt: float) -> np.ndarray:
        """
        Solve diffusion equation: ∂C/∂t = D∇²C
        Uses implicit Crank-Nicolson for stability

        Args:
            C: Concentration field (M)
            D: Diffusion coefficient (m²/s)
            dt: Time step (s)

        Returns:
            Updated concentration field
        """
        C_flat = C.flatten()

        # Crank-Nicolson: (I - 0.5*dt*D*L)C^{n+1} = (I + 0.5*dt*D*L)C^n
        n = len(C_flat)
        I = sp.eye(n, format='csr')
        A = I - 0.5 * dt * D * self.laplacian
        b = (I + 0.5 * dt * D * self.laplacian) @ C_flat

        # Solve sparse system
        C_new = spsolve(A, b)

        return C_new.reshape(C.shape)

    def compute_oxygen_metabolism(self, pO2: np.ndarray,
                                  ATP: np.ndarray) -> tuple:
        """
        Oxygen consumption and ATP production
        Michaelis-Menten kinetics

        Returns:
            (CMRO2, ATP_production) - consumption and production rates
        """
        V_max = MetabolicProperties.CMRO2_Vmax
        K_m = MetabolicProperties.CMRO2_Km

        CMRO2 = V_max * pO2 / (K_m + pO2)  # Oxygen consumption rate

        # ATP production: ~6 ATP per O2 (oxidative phosphorylation)
        ATP_production = 6 * CMRO2

        return CMRO2, ATP_production

    def compute_temperature_update(self, T: np.ndarray,
                                   metabolic_heat: np.ndarray,
                                   dt: float) -> np.ndarray:
        """
        Bioheat equation update

        Args:
            T: Temperature field (K)
            metabolic_heat: Heat source field (W/m³)
            dt: Time step (s)

        Returns:
            Updated temperature field
        """
        k = MetabolicProperties.k_tissue
        rho_cp = MetabolicProperties.rho_cp

        # Diffusive heat transport
        T_new = self.compute_diffusion(T, k / rho_cp, dt)

        # Add metabolic heat source
        T_new += metabolic_heat * dt / rho_cp

        return T_new

    def check_conservation(self) -> Dict[str, float]:
        """
        Verify all conservation laws are satisfied

        Returns:
            Dictionary with conservation metrics
        """
        # Mass conservation
        masses = self.conservation.check_mass_conservation(
            {'Na': self.state.Na_i + self.state.Na_e,
             'K': self.state.K_i + self.state.K_e,
             'Ca': self.state.Ca},
            self.grid
        )

        # Charge conservation
        charge = self.conservation.check_charge_conservation(
            {'Na': self.state.Na_i, 'K': self.state.K_i,
             'Ca': self.state.Ca, 'Cl': self.state.Cl_i},
            {'Na': 1, 'K': 1, 'Ca': 2, 'Cl': -1},
            self.grid
        )

        return {'masses': masses, 'charge': charge}

    def step(self, dt: float = None) -> float:
        """
        Single simulation step integrating all physics

        Args:
            dt: Time step (s), or None to use adaptive

        Returns:
            Actual dt used (may be adapted)
        """
        if dt is None:
            dt = self.time_integrator.dt_current

        # Initialize gating variables if needed
        if self.gating is None:
            self._init_gating()

        # Store old state for error estimation
        Phi_old = self.state.Phi.copy()

        # 1. Compute ionic currents
        currents = self.compute_ion_currents(self.state.Phi, self.gating)

        # 2. Update gating variables
        self.gating = self.compute_gating_dynamics(
            self.state.Phi, self.gating, dt
        )

        # 3. Update membrane potential
        C_m = MembraneProperties.C_m
        dV = -currents['total'] / C_m * dt
        self.state.Phi += dV

        # 4. Diffusion of ions
        for ion, D in [('Na_i', self.D['Na']), ('K_i', self.D['K']),
                       ('Ca', self.D['Ca']), ('Cl_i', self.D['Cl'])]:
            field = getattr(self.state, ion)
            setattr(self.state, ion, self.compute_diffusion(field, D, dt))

        # 5. Oxygen metabolism
        CMRO2, ATP_prod = self.compute_oxygen_metabolism(
            self.state.pO2, self.state.ATP
        )
        self.state.pO2 -= CMRO2 * dt
        self.state.ATP += ATP_prod * dt

        # Oxygen diffusion
        self.state.pO2 = self.compute_diffusion(
            self.state.pO2, self.D['O2'], dt
        )

        # 6. Temperature update
        metabolic_heat = 10 * CMRO2  # Simplified heat from metabolism
        self.state.T = self.compute_temperature_update(
            self.state.T, metabolic_heat, dt
        )

        # 7. Apply boundary conditions
        for field_name in ['Phi', 'pO2', 'Ca', 'Na_i', 'K_i', 'Cl_i', 'T']:
            field = getattr(self.state, field_name)
            self.grid.apply_boundary_conditions(field, bc_type='neumann')

        # 8. Adapt timestep for next iteration
        error_estimate = np.max(np.abs(self.state.Phi - Phi_old)) / \
                        (np.max(np.abs(self.state.Phi)) + 1e-10)
        stiffness = np.max(np.abs(currents['total'])) / C_m
        dt_next = self.time_integrator.adapt_timestep(error_estimate, stiffness)

        # Update time
        self.t += dt

        # Record history (subsampled)
        if len(self.history) == 0 or self.t - self.history[-1]['t'] >= 1e-4:
            self.history.append({
                't': self.t,
                'V_mean': np.mean(self.state.Phi),
                'V_max': np.max(self.state.Phi),
                'ATP_mean': np.mean(self.state.ATP),
                'pO2_mean': np.mean(self.state.pO2),
                'T_mean': np.mean(self.state.T)
            })

        return dt

    def run(self, t_end: float, callback: Callable = None,
            progress_interval: float = 0.1) -> None:
        """
        Run simulation until t_end

        Args:
            t_end: End time (s)
            callback: Optional function called each step with (t, state)
            progress_interval: Fraction of total time between progress reports
        """
        last_progress = 0.0

        while self.t < t_end:
            dt_used = self.step()

            if callback:
                callback(self.t, self.state)

            # Progress reporting
            progress = self.t / t_end
            if progress - last_progress >= progress_interval:
                print(f"Progress: {progress*100:.1f}%, t={self.t*1e3:.3f} ms, "
                      f"dt={dt_used*1e9:.1f} ns")
                last_progress = progress

    def apply_stimulus(self, region: tuple, current: float, duration: float):
        """
        Apply current injection stimulus

        Args:
            region: (x_min, x_max, y_min, y_max, z_min, z_max) in grid units
            current: Current amplitude (A/m²)
            duration: Stimulus duration (s)
        """
        x1, x2, y1, y2, z1, z2 = region
        # Store stimulus info for application during steps
        self._stimulus = {
            'region': (slice(x1, x2), slice(y1, y2), slice(z1, z2)),
            'current': current,
            'end_time': self.t + duration
        }

    def reset(self):
        """Reset simulation to initial state"""
        self.t = 0.0
        self.state = NeuralFieldState(self.grid)
        self.gating = None
        self.history = []
        self.time_integrator.reset()


# =============================================================================
# EXAMPLE USAGE
# =============================================================================

if __name__ == "__main__":
    # Create 100 μm³ simulation domain
    grid = VoxelGrid(
        dx=1e-6,
        x_max=100e-6, y_max=100e-6, z_max=100e-6
    )

    print(f"Grid: {grid.nx}×{grid.ny}×{grid.nz} = {grid.n_voxels:,} voxels")

    # Initialize simulator
    sim = NeuroSimulator(grid)

    # Apply stimulus (depolarize central region)
    center = grid.nx // 2
    sim.state.Phi[center-5:center+5, center-5:center+5, center-5:center+5] = -40e-3

    # Run for 10 ms
    print("\nRunning simulation...")
    sim.run(t_end=10e-3)

    print(f"\nFinal time: {sim.t*1e3:.3f} ms")
    print(f"Mean membrane potential: {np.mean(sim.state.Phi)*1e3:.2f} mV")
    print(f"Max membrane potential: {np.max(sim.state.Phi)*1e3:.2f} mV")
    print(f"Mean ATP: {np.mean(sim.state.ATP)*1e3:.2f} mM")
    print(f"Mean pO2: {np.mean(sim.state.pO2):.1f} mmHg")
    print(f"Mean temperature: {np.mean(sim.state.T) - 273.15:.2f}°C")
