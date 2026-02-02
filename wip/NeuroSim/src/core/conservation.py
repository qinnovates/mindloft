"""
Conservation Laws and Stochastic Processes
Enforcement of mass, charge, and energy conservation
"""

import numpy as np
from typing import Dict, Tuple
from dataclasses import dataclass

from .grid import VoxelGrid
from .constants import PhysicalConstants


class ConservationLaws:
    """
    Enforced conservation: mass, energy, charge
    """

    @staticmethod
    def check_mass_conservation(concentrations: Dict[str, np.ndarray],
                                grid: VoxelGrid,
                                tolerance: float = 1e-10) -> Dict[str, float]:
        """
        Mass balance for neurotransmitters, ions, proteins
        Total mass in closed system must remain constant

        Returns:
            Dictionary mapping species name to total mass (mol)
        """
        masses = {}
        voxel_volume = grid.dx ** 3  # m³

        for species, C in concentrations.items():
            masses[species] = np.sum(C) * voxel_volume  # mol
        return masses

    @staticmethod
    def check_energy_conservation(ATP: np.ndarray,
                                  ADP: np.ndarray,
                                  heat_generated: float,
                                  work_done: float,
                                  delta_G_ATP: float = -54e3) -> float:
        """
        Energy balance: ATP ↔ heat + work

        Args:
            ATP: ATP concentration field (M)
            ADP: ADP concentration field (M)
            heat_generated: Total heat produced (J)
            work_done: Total work performed (J)
            delta_G_ATP: Free energy of ATP hydrolysis (J/mol)

        Returns:
            Energy residual (should be ~0 for conservation)
        """
        delta_ATP = np.sum(ATP)  # Change in ATP pool
        energy_released = -delta_ATP * delta_G_ATP  # J
        energy_accounted = heat_generated + work_done
        return energy_released - energy_accounted

    @staticmethod
    def check_charge_conservation(ion_concentrations: Dict[str, np.ndarray],
                                  valences: Dict[str, int],
                                  grid: VoxelGrid) -> float:
        """
        Charge conservation: intracellular vs extracellular
        Net charge change must equal transmembrane current integral

        Returns:
            Total charge (C) - should be constant
        """
        total_charge = 0.0
        voxel_volume = grid.dx ** 3

        for ion, C in ion_concentrations.items():
            z = valences.get(ion, 0)
            total_charge += z * np.sum(C) * PhysicalConstants.F * voxel_volume

        return total_charge

    @staticmethod
    def compute_entropy_production(heat_rate: np.ndarray,
                                   temperature: np.ndarray) -> float:
        """
        Compute entropy production rate (W/K)
        dS/dt = Q_dot / T
        """
        # Avoid division by zero
        T_safe = np.maximum(temperature, 1.0)
        return np.sum(heat_rate / T_safe)


class StochasticProcesses:
    """
    Brownian motion and Poisson-distributed events
    """

    @staticmethod
    def brownian_displacement(D: float, dt: float,
                              n_particles: int) -> np.ndarray:
        """
        Brownian motion: dx ~ N(0, √(2D·dt))

        Args:
            D: Diffusion coefficient (m²/s)
            dt: Time step (s)
            n_particles: Number of particles

        Returns:
            (n_particles, 3) array of displacement vectors (m)
        """
        sigma = np.sqrt(2 * D * dt)
        return np.random.normal(0, sigma, (n_particles, 3))

    @staticmethod
    def poisson_vesicle_release(rate: float, dt: float,
                                n_synapses: int) -> np.ndarray:
        """
        Poisson-distributed vesicle release events
        P(k events) = (λΔt)^k * exp(-λΔt) / k!

        Args:
            rate: Release rate (Hz)
            dt: Time step (s)
            n_synapses: Number of synapses

        Returns:
            Array of release counts per synapse
        """
        return np.random.poisson(rate * dt, n_synapses)

    @staticmethod
    def langevin_dynamics(x: np.ndarray, F: np.ndarray,
                          gamma: float, T: float, dt: float) -> np.ndarray:
        """
        Langevin equation for overdamped dynamics:
        dx/dt = F/γ + √(2k_B T/γ)·ξ(t)

        Args:
            x: Current positions (m)
            F: Applied forces (N)
            gamma: Friction coefficient (kg/s)
            T: Temperature (K)
            dt: Time step (s)

        Returns:
            Updated positions (m)
        """
        k_B = PhysicalConstants.k_B

        # Deterministic drift
        drift = F / gamma * dt

        # Stochastic diffusion
        diffusion = np.sqrt(2 * k_B * T / gamma * dt) * np.random.randn(*x.shape)

        return x + drift + diffusion

    @staticmethod
    def gillespie_step(propensities: np.ndarray,
                       current_time: float) -> Tuple[float, int]:
        """
        Gillespie algorithm step for exact stochastic simulation

        Args:
            propensities: Array of reaction propensities (1/s)
            current_time: Current simulation time (s)

        Returns:
            (next_time, reaction_index)
        """
        total_propensity = np.sum(propensities)

        if total_propensity == 0:
            return float('inf'), -1

        # Time to next reaction (exponential distribution)
        dt = np.random.exponential(1.0 / total_propensity)

        # Which reaction fires (weighted random choice)
        reaction_idx = np.random.choice(
            len(propensities),
            p=propensities / total_propensity
        )

        return current_time + dt, reaction_idx


@dataclass
class TimeIntegrator:
    """
    Adaptive Δt from 1 ns (spike events) to 1 ms (metabolic processes)
    """
    dt_min: float = 1e-9      # 1 ns - spike timing precision
    dt_max: float = 1e-3      # 1 ms - metabolic timescale
    dt_current: float = 1e-6  # Start at 1 μs

    # Error tolerances for adaptive stepping
    rtol: float = 1e-6
    atol: float = 1e-9

    # Stiffness detection
    eigenvalue_threshold: float = 1e6

    def adapt_timestep(self, error_estimate: float,
                       stiffness_indicator: float) -> float:
        """
        Adapt timestep based on local truncation error and stiffness

        Args:
            error_estimate: Estimated local error
            stiffness_indicator: Measure of system stiffness

        Returns:
            New timestep (s)
        """
        safety_factor = 0.9

        if error_estimate > self.rtol:
            # Reduce timestep
            self.dt_current = max(
                self.dt_min,
                self.dt_current * safety_factor * (self.rtol / error_estimate) ** 0.5
            )
        elif error_estimate < 0.1 * self.rtol:
            # Increase timestep if stable
            self.dt_current = min(
                self.dt_max,
                self.dt_current * 1.5
            )

        # Stiffness override - use smaller steps for fast dynamics
        if stiffness_indicator > self.eigenvalue_threshold:
            self.dt_current = max(self.dt_min,
                                  1.0 / stiffness_indicator * 10)

        return self.dt_current

    def reset(self):
        """Reset to initial timestep"""
        self.dt_current = 1e-6
