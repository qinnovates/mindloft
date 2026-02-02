# Phase 1: Single Neuron Physics Model

Complete mathematical framework for physics-constrained neural simulation.

## A. Environmental Boundary Conditions

### Cranial Geometry (Ellipsoidal Domain)
```
Ω_cranium = {(x,y,z) : (x/a)² + (y/b)² + (z/c)² ≤ 1}
where a = 8.0 cm, b = 7.0 cm, c = 4.5 cm
Volume ≈ 1,350 cm³
```

### Intracranial Pressure Field
```
P_ICP(x,t) = P_base + ΔP_cardiac(t) + ΔP_respiratory(t)
P_base ∈ [7, 15] mmHg = [933, 2000] Pa
ΔP_cardiac(t) = A_c · sin(2πf_c·t), f_c ≈ 1.2 Hz, A_c ≈ 1-3 mmHg
ΔP_respiratory(t) = A_r · sin(2πf_r·t), f_r ≈ 0.25 Hz, A_r ≈ 2-5 mmHg
```

### CSF Dynamics (Simplified Navier-Stokes)
```
ρ_CSF(∂u/∂t + (u·∇)u) = -∇P + μ∇²u + ρ_CSF·g

Parameters:
  ρ_CSF = 1007 kg/m³ (CSF density)
  μ_CSF = 0.7-1.0 mPa·s (dynamic viscosity)
  g = (0, 0, -9.81) m/s² (gravitational acceleration)

Reynolds number: Re = ρuL/μ ≈ 100-500 (laminar-transitional)
```

---

## B. Core Physics Variables

### 1. Electrodiffusion Equations (Nernst-Planck-Poisson System)

For ion species i ∈ {Na⁺, K⁺, Ca²⁺, Cl⁻}:
```
∂Cᵢ/∂t = -∇·Jᵢ + Rᵢ

Jᵢ = -Dᵢ(∇Cᵢ + (zᵢF/RT)Cᵢ∇Φ) + Cᵢu_bulk

Poisson equation:
ε∇²Φ = -F·Σᵢ(zᵢCᵢ)
```

### Ion Parameters Table

| Ion | D (m²/s) | z | C_intra (mM) | C_extra (mM) | E_nernst (mV) |
|-----|----------|---|--------------|--------------|---------------|
| Na⁺ | 1.33×10⁻⁹ | +1 | 15 | 145 | +61 |
| K⁺  | 1.96×10⁻⁹ | +1 | 140 | 5 | -89 |
| Ca²⁺| 0.79×10⁻⁹ | +2 | 0.0001 | 2 | +136 |
| Cl⁻ | 2.03×10⁻⁹ | -1 | 10 | 110 | -65 |

### 2. Temperature Field (Bioheat Equation)
```
ρc_p(∂T/∂t) = k∇²T + Q_met + Q_blood(T_art - T)

T_baseline = 310.15 K (37°C)
k_tissue = 0.5 W/(m·K)
ρc_p = 3.6×10⁶ J/(m³·K)
Q_met = 10-25 W/kg (metabolic heat generation)
Q_blood = ω_b·c_b where ω_b = blood perfusion rate
```

### 3. Hemodynamic Coupling (Oxygen Delivery)
```
∂pO₂/∂t = D_O₂∇²pO₂ - CMRO₂(pO₂, [ATP]) + J_capillary

Michaelis-Menten consumption:
CMRO₂ = V_max · pO₂/(K_m + pO₂)
V_max ≈ 160 μmol/(100g·min)
K_m ≈ 1-5 mmHg

Capillary delivery:
J_capillary = P_s·S_cap·(pO₂_blood - pO₂_tissue)
```

### 4. Atmospheric Pressure Coupling
```
P_external = 101.325 kPa (760 mmHg at sea level)
P_gradient = P_external - P_ICP
Compliance: C = dV/dP ≈ 0.5-2.0 mL/mmHg (Monro-Kellie doctrine)
```

---

## C. Molecular Components as Parameter Sets

### 1. Myelin Sheath (Cable Theory Modification)
```
Myelinated segment:
  C_m = ε₀εᵣ/d_myelin
  εᵣ = 5-7 (relative permittivity)
  d_myelin = 1-2 μm
  C_myelin ≈ 0.005 μF/cm² (vs 1 μF/cm² bare membrane)

Internodal length: L_inter ≈ 100·d_axon (Rushton's rule)
Node of Ranvier length: ≈ 1 μm
```

### 2. Tau Protein Stability Coefficient
```
Microtubule dynamics:
  τ_stability = k_bind·[Tau_functional] / (k_off + k_phos·[kinase])

Phosphorylation cascade:
  d[Tau_p]/dt = k_phos·[Tau]·[GSK3β] - k_dephos·[Tau_p]·[PP2A]

Transport velocity: v_transport = v₀·τ_stability·exp(-E_a/RT)
  v₀ ≈ 1 μm/s (kinesin-mediated)
```

### 3. Receptor Kinetics

#### AMPA
```
α_AMPA = 1.1×10⁶ M⁻¹s⁻¹ (binding rate)
β_AMPA = 190 s⁻¹ (unbinding rate)
g_AMPA = 10-35 pS (single channel conductance)
τ_decay ≈ 2-4 ms
```

#### NMDA
```
g_NMDA(V, [Mg²⁺]) = g_max / (1 + [Mg²⁺]/K_Mg · exp(-V/V_slope))
K_Mg ≈ 3.6 mM, V_slope ≈ 17 mV
τ_rise ≈ 5-10 ms, τ_decay ≈ 50-150 ms
```

#### GABA_A
```
α_GABA = 5×10⁶ M⁻¹s⁻¹
β_GABA = 180 s⁻¹
E_Cl = -70 to -80 mV
```

### 4. Iron/Ferritin Magnetic Susceptibility
```
χ_tissue = χ_dia + χ_para([Fe])
χ_dia ≈ -9×10⁻⁶ (diamagnetic baseline)
χ_para = μ₀·μ_eff²·N_Fe/(3k_B·T)
[Fe]_normal ≈ 50-200 μg/g wet tissue
[Fe]_Alzheimer ≈ 200-400 μg/g (elevated in plaques)
```

### 5. ATP Energy Budget
```
ATP per action potential:
  Na⁺/K⁺-ATPase: ~3×10⁸ ions pumped → ~10⁸ ATP molecules

Energy per spike:
  E_spike = n_ATP · ΔG_ATP
  ΔG_ATP ≈ -54 kJ/mol under cellular conditions
  E_spike ≈ 9×10⁻¹² J = 9 pJ

Power consumption (10 Hz firing):
  P = 10 Hz × 9 pJ = 90 pW per neuron
  Brain total: 86×10⁹ neurons × 90 pW × (1/10 active) ≈ 0.8 W (electrical)
  + 19W metabolic maintenance ≈ 20W total
```

---

## D. Complete Mathematical Framework

### Extended Hodgkin-Huxley with Fractal Geometry

#### Membrane Potential Dynamics
```
C_m(x) · ∂V/∂t = (1/r_a(x)) · ∂²V/∂x² · A(x) - I_ion + I_ext

where A(x) = cross-sectional area following Fibonacci branching
```

#### Fractal Dendritic Geometry
```
At branch point with parent diameter d_p and daughters d₁, d₂:
  d_p^γ = d₁^γ + d₂^γ  (Rall's power law)
  γ = 3/2 (optimal for passive propagation)

Fibonacci constraint:
  d₂/d₁ ≈ φ⁻¹ = 0.618... (golden ratio)

Fractal dimension of dendritic arbor:
  D_f = log(N_branches)/log(1/r_scale) ≈ 1.4-1.8
```

#### Ion Channel Gating (Markov formalism)
```
Na⁺ channel (8-state model):
  C₀ ↔ C₁ ↔ C₂ ↔ C₃ ↔ O
       ↓    ↓    ↓    ↓
       I₀ ↔ I₁ ↔ I₂ ↔ I₃

dm/dt = α_m(V)(1-m) - β_m(V)m
dh/dt = α_h(V)(1-h) - β_h(V)h
dn/dt = α_n(V)(1-n) - β_n(V)n

α_m = 0.1(V+40)/(1-exp(-(V+40)/10))
β_m = 4·exp(-(V+65)/18)
α_h = 0.07·exp(-(V+65)/20)
β_h = 1/(1+exp(-(V+35)/10))
α_n = 0.01(V+55)/(1-exp(-(V+55)/10))
β_n = 0.125·exp(-(V+65)/80)
```

#### Calcium Dynamics with IP3 Signaling
```
d[Ca²⁺]_i/dt = J_channel + J_release - J_pump - J_buffer

J_release = v_rel · m_∞³ · h · ([Ca²⁺]_ER - [Ca²⁺]_i)
  where m_∞ = [IP₃]/([IP₃] + K_IP3) · [Ca²⁺]_i/([Ca²⁺]_i + K_act)

J_pump = v_SERCA · [Ca²⁺]_i²/(K_SERCA² + [Ca²⁺]_i²)

Buffer binding:
  d[CaB]/dt = k_on·[Ca²⁺]·[B_free] - k_off·[CaB]
```

#### Quantum Tunneling for Vesicle Release
```
Probability of vesicle fusion:
  P_fusion = P_dock · P_prime · P_tunnel

Tunneling through energy barrier:
  P_tunnel ≈ exp(-2∫√(2m(U(x)-E))/ℏ dx)

For SNARE-mediated fusion (effective barrier ≈ 2-5 nm, ΔE ≈ 10-20 kT):
  P_tunnel ≈ 10⁻⁴ to 10⁻² per primed vesicle per ms

Ca²⁺ modulation:
  P_fusion([Ca²⁺]) = P₀ · ([Ca²⁺]/K_d)ⁿ/(1 + ([Ca²⁺]/K_d)ⁿ)
  n ≈ 4-5 (cooperativity, synaptotagmin binding sites)
  K_d ≈ 10-20 μM
```

#### Diffusion-Limited Aggregation for Growth Cone
```
Growth cone navigation algorithm:
1. Sample concentration gradients: ∇C_guidance = (∇[NGF], ∇[Netrin], ∇[Slit])
2. Compute chemotactic force: F_chem = Σᵢ wᵢ · ∇Cᵢ
3. Add stochastic exploration: F_total = F_chem + σ·ξ(t), ξ ~ N(0,1)
4. Update position: dx/dt = μ·F_total
5. Apply substrate adhesion: constrain to ECM with κ_adhesion

Branching probability:
  P_branch = α · |F_chem| · exp(-β·tension) · Θ(ATP - ATP_threshold)
```

---

## Dimensionless Parameters

```
Reynolds number:        Re = ρuL/μ ≈ 10⁻⁴ (intracellular), 100-500 (CSF)
Péclet number:          Pe = uL/D ≈ 10²-10⁴ (advection vs diffusion)
Damköhler number:       Da = k·L/u (reaction vs transport)
Schmidt number:         Sc = μ/(ρD) ≈ 10³ (momentum vs mass diffusion)
Biot number:            Bi = hL/k (convective vs conductive heat)
Electrical length:      λ = √(r_m/(r_i+r_e)) ≈ 0.1-2 mm
Membrane time constant: τ_m = r_m·c_m ≈ 10-50 ms
```

---

## Initial Conditions

```python
# Resting state initialization
V_rest = -65e-3  # V (membrane potential)
[Na]_i = 15e-3   # M
[Na]_e = 145e-3  # M
[K]_i = 140e-3   # M
[K]_e = 5e-3     # M
[Ca]_i = 100e-9  # M
[Ca]_e = 2e-3    # M
[Cl]_i = 10e-3   # M
[Cl]_e = 110e-3  # M
[ATP] = 3e-3     # M
[ADP] = 0.3e-3   # M
T = 310.15       # K
pO2 = 30         # mmHg (tissue)
P_ICP = 10       # mmHg
```

---

## Numerical Stability Criteria

```
Spatial: Δx ≤ λ/10 where λ = electrotonic length constant
Temporal: Δt ≤ min(τ_m/10, Δx²/(2D_max), 1/(4·max(α,β)))
CFL condition: u·Δt/Δx ≤ 1 (for advection terms)
von Neumann: For diffusion, Δt ≤ Δx²/(2·D·n_dim)

Stiffness ratio: τ_fast/τ_slow ≈ 10⁻⁶ → requires implicit methods
Recommended: CVODE with adaptive BDF for stiff ODEs
```
