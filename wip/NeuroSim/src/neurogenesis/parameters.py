"""
Neurogenesis Parameter Space
26-dimensional intervention space for neural stem cell optimization
"""

import numpy as np
from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class NeurogenesisParameters:
    """
    Minimal parameter set hypothesized to influence neural stem cell mitosis
    Based on known biology but organized for computational exploration
    """

    # =========================================================================
    # Layer 1: Metabolic Priming
    # =========================================================================
    ATP_ADP_ratio: float = 10.0          # Normal: 10, range: [1, 100]
    oxygen_saturation: float = 0.95      # Normal: 0.95, range: [0.1, 1.0]
    glucose_concentration: float = 5.0   # mM, range: [1, 20]
    lactate_concentration: float = 1.0   # mM, range: [0.1, 10]
    NAD_NADH_ratio: float = 700          # Normal: 700, range: [10, 2000]

    # =========================================================================
    # Layer 2: Mechanical Triggers
    # =========================================================================
    substrate_stiffness: float = 1000    # Pa (Young's modulus), range: [100, 50000]
    CSF_shear_stress: float = 0.5        # Pa, range: [0.01, 5]
    hydrostatic_pressure: float = 1333   # Pa (10 mmHg), range: [666, 2666]
    matrix_porosity: float = 0.3         # Volume fraction, range: [0.1, 0.8]
    integrin_density: float = 1000       # receptors/μm², range: [100, 5000]

    # =========================================================================
    # Layer 3: Electrical Patterns
    # =========================================================================
    theta_frequency: float = 5.0         # Hz, range: [3, 8]
    theta_amplitude: float = 50e-6       # V (local field), range: [10e-6, 200e-6]
    gamma_modulation: float = 0.3        # Nested gamma strength, range: [0, 1]
    DC_field_strength: float = 0         # V/m (galvanotaxis), range: [-100, 100]
    membrane_potential_nsc: float = -70e-3  # V, range: [-90e-3, -40e-3]

    # =========================================================================
    # Layer 4: Molecular Signaling Gradients
    # =========================================================================
    BDNF_concentration: float = 10e-12   # M (10 pM), range: [1e-12, 1e-9]
    BDNF_gradient: float = 0.1           # nM/mm, range: [0, 1]
    Wnt_activity: float = 0.5            # Normalized, range: [0, 1]
    beta_catenin_nuclear: float = 0.3    # Nuclear fraction, range: [0, 1]
    Notch_activity: float = 0.5          # Normalized, range: [0, 1]
    Shh_concentration: float = 1e-9      # M, range: [1e-12, 1e-7]
    EGF_concentration: float = 1e-11     # M, range: [1e-13, 1e-9]
    FGF2_concentration: float = 5e-12    # M, range: [1e-13, 1e-10]

    # =========================================================================
    # Layer 5: Thermodynamic Conditions
    # =========================================================================
    local_temperature: float = 310.15    # K (37°C), range: [308, 312]
    temperature_gradient: float = 0      # K/mm, range: [-0.5, 0.5]
    entropy_production_rate: float = 1.0 # Normalized, range: [0.1, 10]

    def to_vector(self) -> np.ndarray:
        """Convert parameters to optimization vector"""
        return np.array([
            # Metabolic (5)
            self.ATP_ADP_ratio,
            self.oxygen_saturation,
            self.glucose_concentration,
            self.lactate_concentration,
            self.NAD_NADH_ratio,
            # Mechanical (5)
            self.substrate_stiffness,
            self.CSF_shear_stress,
            self.hydrostatic_pressure,
            self.matrix_porosity,
            self.integrin_density,
            # Electrical (5)
            self.theta_frequency,
            self.theta_amplitude,
            self.gamma_modulation,
            self.DC_field_strength,
            self.membrane_potential_nsc,
            # Molecular (8)
            self.BDNF_concentration,
            self.BDNF_gradient,
            self.Wnt_activity,
            self.beta_catenin_nuclear,
            self.Notch_activity,
            self.Shh_concentration,
            self.EGF_concentration,
            self.FGF2_concentration,
            # Thermodynamic (3)
            self.local_temperature,
            self.temperature_gradient,
            self.entropy_production_rate
        ])

    @classmethod
    def from_vector(cls, v: np.ndarray) -> 'NeurogenesisParameters':
        """Reconstruct from optimization vector"""
        return cls(
            # Metabolic
            ATP_ADP_ratio=v[0],
            oxygen_saturation=v[1],
            glucose_concentration=v[2],
            lactate_concentration=v[3],
            NAD_NADH_ratio=v[4],
            # Mechanical
            substrate_stiffness=v[5],
            CSF_shear_stress=v[6],
            hydrostatic_pressure=v[7],
            matrix_porosity=v[8],
            integrin_density=v[9],
            # Electrical
            theta_frequency=v[10],
            theta_amplitude=v[11],
            gamma_modulation=v[12],
            DC_field_strength=v[13],
            membrane_potential_nsc=v[14],
            # Molecular
            BDNF_concentration=v[15],
            BDNF_gradient=v[16],
            Wnt_activity=v[17],
            beta_catenin_nuclear=v[18],
            Notch_activity=v[19],
            Shh_concentration=v[20],
            EGF_concentration=v[21],
            FGF2_concentration=v[22],
            # Thermodynamic
            local_temperature=v[23],
            temperature_gradient=v[24],
            entropy_production_rate=v[25]
        )

    @staticmethod
    def get_bounds() -> List[Tuple[float, float]]:
        """Parameter bounds for optimization"""
        return [
            # Metabolic (5)
            (1, 100),        # ATP_ADP_ratio
            (0.1, 1.0),      # oxygen_saturation
            (1, 20),         # glucose_concentration
            (0.1, 10),       # lactate_concentration
            (10, 2000),      # NAD_NADH_ratio
            # Mechanical (5)
            (100, 50000),    # substrate_stiffness
            (0.01, 5),       # CSF_shear_stress
            (666, 2666),     # hydrostatic_pressure
            (0.1, 0.8),      # matrix_porosity
            (100, 5000),     # integrin_density
            # Electrical (5)
            (3, 8),          # theta_frequency
            (10e-6, 200e-6), # theta_amplitude
            (0, 1),          # gamma_modulation
            (-100, 100),     # DC_field_strength
            (-90e-3, -40e-3),# membrane_potential_nsc
            # Molecular (8)
            (1e-12, 1e-9),   # BDNF_concentration
            (0, 1),          # BDNF_gradient
            (0, 1),          # Wnt_activity
            (0, 1),          # beta_catenin_nuclear
            (0, 1),          # Notch_activity
            (1e-12, 1e-7),   # Shh_concentration
            (1e-13, 1e-9),   # EGF_concentration
            (1e-13, 1e-10),  # FGF2_concentration
            # Thermodynamic (3)
            (308, 312),      # local_temperature
            (-0.5, 0.5),     # temperature_gradient
            (0.1, 10)        # entropy_production_rate
        ]

    @staticmethod
    def get_parameter_names() -> List[str]:
        """Get ordered list of parameter names"""
        return [
            'ATP_ADP_ratio', 'oxygen_saturation', 'glucose_concentration',
            'lactate_concentration', 'NAD_NADH_ratio',
            'substrate_stiffness', 'CSF_shear_stress', 'hydrostatic_pressure',
            'matrix_porosity', 'integrin_density',
            'theta_frequency', 'theta_amplitude', 'gamma_modulation',
            'DC_field_strength', 'membrane_potential_nsc',
            'BDNF_concentration', 'BDNF_gradient', 'Wnt_activity',
            'beta_catenin_nuclear', 'Notch_activity', 'Shh_concentration',
            'EGF_concentration', 'FGF2_concentration',
            'local_temperature', 'temperature_gradient', 'entropy_production_rate'
        ]

    @staticmethod
    def get_layer_indices() -> dict:
        """Get indices for each parameter layer"""
        return {
            'metabolic': list(range(0, 5)),
            'mechanical': list(range(5, 10)),
            'electrical': list(range(10, 15)),
            'molecular': list(range(15, 23)),
            'thermodynamic': list(range(23, 26))
        }

    def perturb(self, noise_scale: float = 0.1) -> 'NeurogenesisParameters':
        """Create perturbed copy of parameters"""
        v = self.to_vector()
        bounds = self.get_bounds()

        for i in range(len(v)):
            range_size = bounds[i][1] - bounds[i][0]
            noise = np.random.normal(0, noise_scale * range_size)
            v[i] = np.clip(v[i] + noise, bounds[i][0], bounds[i][1])

        return self.from_vector(v)

    def interpolate(self, other: 'NeurogenesisParameters',
                    alpha: float) -> 'NeurogenesisParameters':
        """Interpolate between two parameter sets"""
        v1 = self.to_vector()
        v2 = other.to_vector()
        v_interp = (1 - alpha) * v1 + alpha * v2
        return self.from_vector(v_interp)
