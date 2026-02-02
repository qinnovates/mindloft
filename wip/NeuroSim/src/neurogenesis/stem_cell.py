"""
Neural Stem Cell Model
Cell cycle dynamics and differentiation
"""

import numpy as np
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

from .parameters import NeurogenesisParameters


class CellCyclePhase(Enum):
    """Cell cycle phases"""
    G0_QUIESCENT = 0   # Quiescent, not dividing
    G1 = 1             # Gap 1, growth and preparation
    S = 2              # DNA synthesis
    G2 = 3             # Gap 2, preparation for mitosis
    M = 4              # Mitosis
    DIFFERENTIATED = 5  # Terminally differentiated


@dataclass
class NeuralStemCell:
    """
    Single neural stem cell state
    Models cell cycle, signaling, and differentiation
    """
    position: np.ndarray = field(default_factory=lambda: np.zeros(3))  # (x, y, z) in μm
    phase: CellCyclePhase = CellCyclePhase.G0_QUIESCENT

    # =========================================================================
    # Cell Cycle Regulators
    # =========================================================================
    cyclin_D: float = 0.1    # G1 cyclin
    cyclin_E: float = 0.0    # G1/S cyclin
    cyclin_A: float = 0.0    # S/G2 cyclin
    cyclin_B: float = 0.0    # M cyclin
    p21: float = 0.5         # CDK inhibitor
    p53: float = 0.1         # Tumor suppressor
    Rb: float = 0.8          # Retinoblastoma protein (hypophosphorylated)
    E2F: float = 0.1         # Transcription factor

    # =========================================================================
    # Differentiation Markers
    # =========================================================================
    nestin: float = 1.0      # Stem cell marker
    Sox2: float = 0.9        # Stemness transcription factor
    DCX: float = 0.0         # Doublecortin - neuroblast marker
    NeuN: float = 0.0        # Mature neuron marker
    GFAP: float = 0.0        # Astrocyte marker

    # =========================================================================
    # Metabolic State
    # =========================================================================
    ATP_level: float = 1.0   # Normalized cellular ATP
    ROS_level: float = 0.1   # Reactive oxygen species

    # =========================================================================
    # History
    # =========================================================================
    age: float = 0.0         # Hours since last division
    division_count: int = 0  # Total divisions

    def compute_proliferation_signal(self, params: NeurogenesisParameters) -> float:
        """
        Integrate environmental signals into proliferation decision
        Returns probability of transitioning from G0 to G1

        Args:
            params: Environmental parameters

        Returns:
            Proliferation signal strength [0, 1]
        """
        # =====================================================================
        # Metabolic gating
        # =====================================================================
        metabolic_score = (
            0.3 * np.tanh((params.ATP_ADP_ratio - 5) / 5) +
            0.2 * params.oxygen_saturation +
            0.2 * np.tanh((params.glucose_concentration - 3) / 2) +
            0.1 * (1 - self.ROS_level) +
            0.2 * self.ATP_level
        )

        # =====================================================================
        # Mechanical sensing (YAP/TAZ pathway)
        # =====================================================================
        stiffness_optimal = 3000  # Pa - optimal for NSC proliferation
        mechanical_score = np.exp(
            -((np.log10(params.substrate_stiffness) -
               np.log10(stiffness_optimal))**2) / 0.5
        )
        mechanical_score *= (1 + 0.3 * np.tanh(params.CSF_shear_stress - 0.5))

        # =====================================================================
        # Electrical stimulation
        # =====================================================================
        theta_optimal = 5.0  # Hz
        electrical_score = np.exp(-((params.theta_frequency - theta_optimal)**2) / 2)
        electrical_score *= (1 + params.gamma_modulation)

        # =====================================================================
        # Growth factor signaling (Hill functions)
        # =====================================================================
        K_BDNF = 50e-12  # M
        K_Wnt = 0.3
        K_Shh = 5e-10

        growth_factor_score = (
            0.25 * params.BDNF_concentration / (K_BDNF + params.BDNF_concentration) +
            0.25 * params.Wnt_activity**2 / (K_Wnt**2 + params.Wnt_activity**2) +
            0.20 * params.Shh_concentration / (K_Shh + params.Shh_concentration) +
            0.15 * params.EGF_concentration / (1e-11 + params.EGF_concentration) +
            0.15 * params.FGF2_concentration / (1e-12 + params.FGF2_concentration)
        )

        # =====================================================================
        # Temperature sensitivity (Q10 ≈ 2)
        # =====================================================================
        T_optimal = 310.15
        temp_score = np.exp(-((params.local_temperature - T_optimal)**2) / 4)

        # =====================================================================
        # Inhibitory signals
        # =====================================================================
        inhibition = (
            0.5 * self.p21 +
            0.3 * self.p53 +
            0.2 * (1 - self.nestin)  # Loss of stemness
        )

        # =====================================================================
        # Integrate signals
        # =====================================================================
        total_signal = (
            0.25 * metabolic_score +
            0.20 * mechanical_score +
            0.15 * electrical_score +
            0.30 * growth_factor_score +
            0.10 * temp_score
        ) * (1 - inhibition)

        return np.clip(total_signal, 0, 1)

    def update_cell_cycle(self, params: NeurogenesisParameters,
                          dt: float) -> Optional['NeuralStemCell']:
        """
        Update cell cycle state, potentially returning daughter cell

        Args:
            params: Environmental parameters
            dt: Time step in hours

        Returns:
            Daughter cell if division occurred, None otherwise
        """
        daughter = None

        # =====================================================================
        # State-dependent dynamics
        # =====================================================================
        if self.phase == CellCyclePhase.G0_QUIESCENT:
            # Check for G0 → G1 transition
            prolif_signal = self.compute_proliferation_signal(params)
            if np.random.random() < prolif_signal * dt:
                self.phase = CellCyclePhase.G1
                self.cyclin_D = 0.2

        elif self.phase == CellCyclePhase.G1:
            # Cyclin D accumulation
            self.cyclin_D += (0.1 * self.E2F - 0.05 * self.cyclin_D) * dt

            # Rb phosphorylation releases E2F
            if self.cyclin_D > 0.5:
                self.Rb *= (1 - 0.05 * dt)
                self.E2F = 0.5 * (1 - self.Rb)

            # Restriction point
            if self.E2F > 0.3 and self.ATP_level > 0.7:
                self.phase = CellCyclePhase.S
                self.cyclin_E = 0.5

        elif self.phase == CellCyclePhase.S:
            # DNA replication (simplified)
            self.cyclin_A += 0.1 * dt
            self.cyclin_E *= (1 - 0.1 * dt)  # Cyclin E degradation

            if self.cyclin_A > 1.0:
                self.phase = CellCyclePhase.G2

        elif self.phase == CellCyclePhase.G2:
            self.cyclin_B += 0.1 * dt
            if self.cyclin_B > 1.0:
                self.phase = CellCyclePhase.M

        elif self.phase == CellCyclePhase.M:
            # Mitosis - create daughter cell
            if np.random.random() < 0.9:  # Successful division
                # Create daughter cell
                daughter = NeuralStemCell(
                    position=self.position + np.random.randn(3) * 5,  # μm displacement
                    phase=CellCyclePhase.G0_QUIESCENT,
                    nestin=self.nestin,
                    Sox2=self.Sox2
                )

                # Symmetric vs asymmetric division (Notch-dependent)
                if np.random.random() < params.Notch_activity:
                    # Asymmetric: one stem, one differentiating
                    daughter.DCX = 0.3
                    daughter.nestin = 0.5
                    daughter.Sox2 = 0.5
                else:
                    # Symmetric: both remain stem cells
                    pass

                # Reset parent
                self.division_count += 1
                self.age = 0

            # Reset to G0/G1 regardless
            self.phase = CellCyclePhase.G0_QUIESCENT

            # Reset cyclins
            self.cyclin_D = 0.1
            self.cyclin_E = 0
            self.cyclin_A = 0
            self.cyclin_B = 0
            self.Rb = 0.8
            self.E2F = 0.1

        # Update age
        self.age += dt

        return daughter

    def update_differentiation(self, params: NeurogenesisParameters,
                               dt: float):
        """
        Update differentiation state based on markers and environment

        Args:
            params: Environmental parameters
            dt: Time step in hours
        """
        # Neuroblast → Neuron transition
        if self.DCX > 0.5 and self.age > 48:  # 2+ days as neuroblast
            # Gradual maturation
            self.NeuN += 0.01 * dt
            self.DCX *= (1 - 0.01 * dt)
            self.nestin *= (1 - 0.02 * dt)

        # Check for terminal differentiation
        if self.NeuN > 0.8:
            self.phase = CellCyclePhase.DIFFERENTIATED

        # GFAP increase if Notch is high and BDNF is low (astrocyte fate)
        if params.Notch_activity > 0.7 and params.BDNF_concentration < 5e-12:
            self.GFAP += 0.005 * dt
            self.DCX *= (1 - 0.01 * dt)

    def update_metabolism(self, params: NeurogenesisParameters, dt: float):
        """
        Update metabolic state

        Args:
            params: Environmental parameters
            dt: Time step in hours
        """
        # ATP depends on oxygen and glucose
        target_ATP = (
            0.5 * params.oxygen_saturation +
            0.3 * np.tanh(params.glucose_concentration / 5) +
            0.2 * params.ATP_ADP_ratio / 20
        )
        self.ATP_level += 0.1 * (target_ATP - self.ATP_level) * dt

        # ROS increases with metabolic activity, decreases with antioxidants
        # Simplified: ROS correlates with high activity but low oxygen
        ros_production = 0.1 * (1 - params.oxygen_saturation)
        ros_clearance = 0.05 * self.ATP_level
        self.ROS_level += (ros_production - ros_clearance) * dt
        self.ROS_level = np.clip(self.ROS_level, 0, 1)

    def is_stem_cell(self) -> bool:
        """Check if cell maintains stem cell identity"""
        return self.nestin > 0.5 and self.Sox2 > 0.5

    def is_neuroblast(self) -> bool:
        """Check if cell is a neuroblast"""
        return self.DCX > 0.3 and self.NeuN < 0.5

    def is_mature_neuron(self) -> bool:
        """Check if cell is a mature neuron"""
        return self.NeuN > 0.7

    def is_astrocyte(self) -> bool:
        """Check if cell is an astrocyte"""
        return self.GFAP > 0.5

    def get_cell_type(self) -> str:
        """Get current cell type as string"""
        if self.is_mature_neuron():
            return "neuron"
        elif self.is_astrocyte():
            return "astrocyte"
        elif self.is_neuroblast():
            return "neuroblast"
        elif self.is_stem_cell():
            return "stem_cell"
        else:
            return "progenitor"
