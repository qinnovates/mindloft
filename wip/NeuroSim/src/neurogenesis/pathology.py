"""
Alzheimer's Pathology Model and Functional Metrics
Representation of disease states for reversal experiments
"""

import numpy as np
from dataclasses import dataclass
from typing import Dict, Optional


@dataclass
class AlzheimersPathology:
    """
    Simulated AD pathology for reversal experiments
    Each pathological feature maps to physical constraints
    """

    # =========================================================================
    # Amyloid-β Plaques (Diffusion Barriers)
    # =========================================================================
    plaque_density: float = 0.0        # plaques/mm³
    plaque_radius: float = 25e-6       # m (typical 25-50 μm)
    Abeta_oligomer_conc: float = 0.0   # nM

    # =========================================================================
    # Tau Tangles (Transport Disruption)
    # =========================================================================
    tangle_density: float = 0.0        # tangles/neuron fraction
    tau_hyperphosphorylation: float = 0.0  # Fraction of tau
    microtubule_stability: float = 1.0     # Normalized

    # =========================================================================
    # Neuroinflammation
    # =========================================================================
    microglial_activation: float = 0.0     # Fraction activated
    IL1_beta: float = 0.0                  # pg/mL
    TNF_alpha: float = 0.0                 # pg/mL

    # =========================================================================
    # Synaptic Loss
    # =========================================================================
    synapse_density: float = 1.0           # Normalized to healthy

    # =========================================================================
    # Metabolic Dysfunction
    # =========================================================================
    glucose_hypometabolism: float = 0.0    # Reduction fraction
    mitochondrial_dysfunction: float = 0.0  # Fraction impaired

    def compute_diffusion_coefficient_modifier(self,
                                               position: Optional[np.ndarray] = None) -> float:
        """
        Amyloid plaques act as diffusion barriers

        Args:
            position: Optional spatial position for heterogeneous distribution

        Returns:
            Local diffusion coefficient scaling factor (0-1)
        """
        if self.plaque_density == 0:
            return 1.0

        # Tortuosity increases with plaque density
        # Based on effective medium theory for diffusion in porous media
        tortuosity_increase = 1 + 2 * self.plaque_density * self.plaque_radius**2
        return 1.0 / tortuosity_increase

    def compute_transport_velocity_modifier(self) -> float:
        """
        Tau tangles disrupt axonal transport

        Returns:
            Transport velocity scaling factor (0-1)
        """
        return self.microtubule_stability * (1 - self.tau_hyperphosphorylation)

    def compute_synaptic_efficacy(self) -> float:
        """
        Combined effect on synaptic transmission

        Returns:
            Synaptic efficacy (0-1)
        """
        # Aβ oligomers directly impair synaptic function
        oligomer_effect = 1 / (1 + self.Abeta_oligomer_conc / 1.0)  # IC50 ~ 1 nM

        return self.synapse_density * oligomer_effect

    def compute_metabolic_capacity(self) -> float:
        """
        Metabolic capacity considering glucose utilization and mitochondria

        Returns:
            Metabolic capacity (0-1)
        """
        glucose_capacity = 1 - self.glucose_hypometabolism
        mito_capacity = 1 - self.mitochondrial_dysfunction
        return glucose_capacity * mito_capacity

    def get_severity_score(self) -> float:
        """
        Overall pathology severity score

        Returns:
            Severity score (0-1), higher is worse
        """
        scores = [
            self.plaque_density / 1000,  # Normalize to typical max
            self.Abeta_oligomer_conc / 10,
            self.tau_hyperphosphorylation,
            1 - self.microtubule_stability,
            self.microglial_activation,
            1 - self.synapse_density,
            self.glucose_hypometabolism,
            self.mitochondrial_dysfunction
        ]
        return np.clip(np.mean(scores), 0, 1)

    def update(self, dt: float, intervention_strength: float = 0.0):
        """
        Update pathology state over time

        Args:
            dt: Time step in hours
            intervention_strength: Therapeutic intervention strength (0-1)
        """
        # Natural progression (slow worsening)
        progression_rate = 0.001  # per hour

        if intervention_strength == 0:
            # Disease progression
            self.plaque_density *= (1 + progression_rate * dt)
            self.tau_hyperphosphorylation = min(
                1, self.tau_hyperphosphorylation + 0.0001 * dt
            )
            self.synapse_density = max(0.1, self.synapse_density - 0.0001 * dt)
        else:
            # Intervention effects
            self.plaque_density *= (1 - 0.01 * intervention_strength * dt)
            self.tau_hyperphosphorylation *= (1 - 0.005 * intervention_strength * dt)
            self.synapse_density = min(
                1, self.synapse_density + 0.001 * intervention_strength * dt
            )

        # Update dependent variables
        self.microtubule_stability = 1 - 0.8 * self.tau_hyperphosphorylation


@dataclass
class FunctionalMetrics:
    """
    Metrics for evaluating functional recovery
    """

    # =========================================================================
    # Structural Metrics
    # =========================================================================
    neuron_count: float = 0.0          # New neurons / baseline
    synapse_density: float = 0.0       # Normalized
    axon_integrity: float = 0.0        # Transport function

    # =========================================================================
    # Electrophysiological Metrics
    # =========================================================================
    LTP_magnitude: float = 0.0         # Long-term potentiation
    gamma_power: float = 0.0           # Cognitive processing marker
    theta_gamma_coupling: float = 0.0  # Memory encoding

    # =========================================================================
    # Cognitive Proxies (from network simulations)
    # =========================================================================
    pattern_completion: float = 0.0    # Memory retrieval
    pattern_separation: float = 0.0    # Discrimination
    working_memory_span: float = 0.0   # Capacity measure

    # =========================================================================
    # Metabolic Health
    # =========================================================================
    glucose_utilization: float = 0.0   # Normalized
    ATP_efficiency: float = 0.0        # Normalized
    oxidative_stress: float = 0.0      # Lower is better

    def compute_composite_score(self, weights: Optional[Dict[str, float]] = None) -> float:
        """
        Weighted composite recovery score

        Args:
            weights: Optional custom weights for each metric

        Returns:
            Composite score (0-1)
        """
        if weights is None:
            weights = {
                # Structural (40%)
                'neuron_count': 0.15,
                'synapse_density': 0.15,
                'axon_integrity': 0.10,
                # Electrophysiology (25%)
                'LTP_magnitude': 0.10,
                'gamma_power': 0.05,
                'theta_gamma_coupling': 0.10,
                # Cognitive (30%)
                'pattern_completion': 0.15,
                'pattern_separation': 0.10,
                'working_memory_span': 0.05,
                # Metabolic (5%)
                'glucose_utilization': 0.025,
                'ATP_efficiency': 0.025
            }

        score = sum(
            weights.get(k, 0) * getattr(self, k, 0)
            for k in weights.keys()
        )

        # Penalize oxidative stress
        score *= (1 - 0.5 * self.oxidative_stress)

        return np.clip(score, 0, 1)

    def get_structural_score(self) -> float:
        """Get aggregate structural health score"""
        return np.mean([
            self.neuron_count,
            self.synapse_density,
            self.axon_integrity
        ])

    def get_functional_score(self) -> float:
        """Get aggregate functional score"""
        return np.mean([
            self.LTP_magnitude,
            self.gamma_power,
            self.theta_gamma_coupling,
            self.pattern_completion,
            self.pattern_separation,
            self.working_memory_span
        ])

    def get_metabolic_score(self) -> float:
        """Get aggregate metabolic health score"""
        return np.mean([
            self.glucose_utilization,
            self.ATP_efficiency,
            1 - self.oxidative_stress
        ])

    def to_dict(self) -> Dict[str, float]:
        """Convert to dictionary"""
        return {
            'neuron_count': self.neuron_count,
            'synapse_density': self.synapse_density,
            'axon_integrity': self.axon_integrity,
            'LTP_magnitude': self.LTP_magnitude,
            'gamma_power': self.gamma_power,
            'theta_gamma_coupling': self.theta_gamma_coupling,
            'pattern_completion': self.pattern_completion,
            'pattern_separation': self.pattern_separation,
            'working_memory_span': self.working_memory_span,
            'glucose_utilization': self.glucose_utilization,
            'ATP_efficiency': self.ATP_efficiency,
            'oxidative_stress': self.oxidative_stress,
            'composite_score': self.compute_composite_score()
        }

    @classmethod
    def from_simulation(cls, stem_cells: list, params, pathology) -> 'FunctionalMetrics':
        """
        Compute metrics from simulation results

        Args:
            stem_cells: List of NeuralStemCell objects
            params: NeurogenesisParameters
            pathology: AlzheimersPathology

        Returns:
            Computed FunctionalMetrics
        """
        # Count cell types
        n_initial = 100  # Baseline
        mature_neurons = sum(1 for c in stem_cells if hasattr(c, 'NeuN') and c.NeuN > 0.5)
        young_neurons = sum(1 for c in stem_cells if hasattr(c, 'DCX') and 0.1 < c.DCX < 0.5)

        return cls(
            neuron_count=mature_neurons / n_initial,
            synapse_density=pathology.compute_synaptic_efficacy(),
            axon_integrity=pathology.compute_transport_velocity_modifier(),
            LTP_magnitude=np.clip(
                0.5 * params.BDNF_concentration / 50e-12 +
                0.3 * (params.theta_frequency / 5) +
                0.2 * params.Wnt_activity,
                0, 1
            ),
            gamma_power=np.clip(
                params.gamma_modulation * (1 + 0.5 * params.ATP_ADP_ratio / 10),
                0, 1
            ),
            theta_gamma_coupling=params.gamma_modulation,
            pattern_completion=np.clip(mature_neurons / 50, 0, 1),
            pattern_separation=np.clip(young_neurons / 30, 0, 1),
            working_memory_span=params.gamma_modulation * np.exp(
                -((params.theta_frequency - 6)**2) / 4
            ),
            glucose_utilization=params.glucose_concentration / 5.0,
            ATP_efficiency=params.ATP_ADP_ratio / 20.0,
            oxidative_stress=pathology.mitochondrial_dysfunction
        )
