"""
Physical Constants for Neural Simulation
All values in SI units
"""


class PhysicalConstants:
    """Fundamental physical constants"""

    # Fundamental constants
    F = 96485.33          # Faraday constant (C/mol)
    R = 8.314             # Gas constant (J/(mol·K))
    k_B = 1.381e-23       # Boltzmann constant (J/K)
    epsilon_0 = 8.854e-12 # Vacuum permittivity (F/m)
    h = 6.626e-34         # Planck constant (J·s)
    h_bar = 1.055e-34     # Reduced Planck constant (J·s)
    e = 1.602e-19         # Elementary charge (C)
    N_A = 6.022e23        # Avogadro's number (1/mol)

    # Temperature
    T_body = 310.15       # Body temperature (K) = 37°C

    # Gravitational
    g = 9.81              # Gravitational acceleration (m/s²)

    # Atmospheric
    P_atm = 101325        # Atmospheric pressure (Pa)
    P_atm_mmHg = 760      # Atmospheric pressure (mmHg)


class IonProperties:
    """Ion-specific properties"""

    # Diffusion coefficients (m²/s)
    D_Na = 1.33e-9
    D_K = 1.96e-9
    D_Ca = 0.79e-9
    D_Cl = 2.03e-9
    D_O2 = 2.0e-9
    D_ATP = 0.3e-9
    D_glutamate = 0.76e-9

    # Valences
    z_Na = +1
    z_K = +1
    z_Ca = +2
    z_Cl = -1

    # Resting concentrations (M)
    # Intracellular
    C_Na_i = 15e-3
    C_K_i = 140e-3
    C_Ca_i = 100e-9
    C_Cl_i = 10e-3

    # Extracellular
    C_Na_e = 145e-3
    C_K_e = 5e-3
    C_Ca_e = 2e-3
    C_Cl_e = 110e-3


class MembraneProperties:
    """Membrane electrical properties"""

    # Capacitance
    C_m = 1e-2            # Membrane capacitance (F/m²) = 1 μF/cm²
    C_m_myelin = 5e-5     # Myelinated membrane (F/m²) = 0.005 μF/cm²

    # Resting potential
    V_rest = -65e-3       # Resting membrane potential (V)

    # Reversal potentials (V)
    E_Na = 61e-3
    E_K = -89e-3
    E_Ca = 136e-3
    E_Cl = -65e-3
    E_L = -54.4e-3        # Leak

    # Conductances (S/m²)
    g_Na_max = 120e-3     # Max Na+ conductance
    g_K_max = 36e-3       # Max K+ conductance
    g_L = 0.3e-3          # Leak conductance


class MetabolicProperties:
    """Metabolic and energetic parameters"""

    # ATP
    C_ATP_rest = 3e-3     # Resting ATP concentration (M)
    C_ADP_rest = 0.3e-3   # Resting ADP concentration (M)
    dG_ATP = -54e3        # Free energy of ATP hydrolysis (J/mol)
    ATP_per_spike = 1e8   # ATP molecules consumed per action potential

    # Oxygen
    pO2_tissue = 30       # Tissue oxygen tension (mmHg)
    pO2_blood = 100       # Arterial oxygen tension (mmHg)
    CMRO2_Vmax = 160e-6 / 60  # Max O2 consumption (mol/(m³·s))
    CMRO2_Km = 3.0        # Michaelis constant (mmHg)

    # Temperature/Heat
    k_tissue = 0.5        # Thermal conductivity (W/(m·K))
    rho_cp = 3.6e6        # Volumetric heat capacity (J/(m³·K))
    Q_met = 15            # Metabolic heat generation (W/kg)


class CSFProperties:
    """Cerebrospinal fluid properties"""

    rho = 1007            # Density (kg/m³)
    mu = 0.8e-3           # Dynamic viscosity (Pa·s)

    # Intracranial pressure
    P_ICP_min = 7         # Minimum ICP (mmHg)
    P_ICP_max = 15        # Maximum ICP (mmHg)
    P_ICP_nominal = 10    # Nominal ICP (mmHg)

    # Pulsatility
    f_cardiac = 1.2       # Cardiac frequency (Hz)
    f_respiratory = 0.25  # Respiratory frequency (Hz)
    A_cardiac = 2         # Cardiac amplitude (mmHg)
    A_respiratory = 3     # Respiratory amplitude (mmHg)


class CranialGeometry:
    """Cranial dimensions"""

    # Ellipsoid semi-axes (m)
    a = 0.08              # Anterior-posterior (8 cm)
    b = 0.07              # Left-right (7 cm)
    c = 0.045             # Superior-inferior (4.5 cm)

    # Volume
    volume = 4/3 * 3.14159 * a * b * c  # ≈ 1350 cm³
