"""
QIF Equations — Core implementation of the QI equation and supporting metrics.

This module implements:
- Coherence Metric (Cₛ)
- QI Equation Candidate 1 (Additive/Engineering)
- QI Equation Candidate 2 (Tensor/Theoretical)
- Decoherence factor ΓD(t)
- Tunneling coefficient T

All equations match QIF-TRUTH.md (canonical source).
"""

import numpy as np
from dataclasses import dataclass, field
from typing import Optional


# ──────────────────────────────────────────────
# Coherence Metric
# ──────────────────────────────────────────────

def phase_variance(phases: np.ndarray) -> float:
    """σ²ᵩ — Phase variance relative to mean phase.

    Args:
        phases: Array of phase values (radians) from neural signals.

    Returns:
        Circular variance of phases (0 = perfect sync, higher = more jitter).
    """
    # Use circular variance for phase data (handles wraparound)
    mean_vector = np.abs(np.mean(np.exp(1j * phases)))
    return 1.0 - mean_vector  # 0 = perfectly locked, 1 = random


def transport_variance(probabilities: np.ndarray) -> float:
    """σ²τ — Transport variance (pathway integrity).

    Based on negative log-likelihood of transmission probabilities.

    Args:
        probabilities: Array of transmission success probabilities (0-1).

    Returns:
        Transport variance (0 = perfect transmission, higher = degraded).
    """
    # Clip to avoid log(0)
    p = np.clip(probabilities, 1e-10, 1.0)
    return -np.mean(np.log(p))


def gain_variance(amplitudes: np.ndarray) -> float:
    """σ²ᵧ — Gain variance (amplitude stability).

    Normalized variance of signal amplitudes relative to mean.

    Args:
        amplitudes: Array of signal amplitude measurements.

    Returns:
        Gain variance (0 = perfectly stable, higher = fluctuating).
    """
    mean_amp = np.mean(amplitudes)
    if mean_amp == 0:
        return float('inf')
    return np.mean(((amplitudes - mean_amp) / mean_amp) ** 2)


def coherence_metric(sigma_phi: float, sigma_tau: float, sigma_gamma: float) -> float:
    """Cₛ = e^(−(σ²ᵩ + σ²τ + σ²ᵧ))

    The QIF coherence metric. Scores signal trustworthiness from 0 to 1.

    Args:
        sigma_phi: Phase variance
        sigma_tau: Transport variance
        sigma_gamma: Gain variance

    Returns:
        Coherence score (0 to 1). >0.6 = high, 0.3-0.6 = medium, <0.3 = low.
    """
    total_variance = sigma_phi + sigma_tau + sigma_gamma
    return np.exp(-total_variance)


def coherence_decision(cs: float, auth_valid: bool) -> str:
    """Decision matrix for coherence + authentication.

    Returns action string based on QIF-TRUTH.md thresholds.
    """
    if cs > 0.6:
        return "ACCEPT" if auth_valid else "REJECT + ALERT"
    elif cs > 0.3:
        return "ACCEPT + FLAG" if auth_valid else "REJECT + ALERT"
    else:
        return "REJECT + CRITICAL"


# ──────────────────────────────────────────────
# Decoherence
# ──────────────────────────────────────────────

def decoherence_factor(t: float, tau_d: float) -> float:
    """ΓD(t) = 1 − e^(−t/τ_D)

    Decoherence factor: 0 = fully quantum, 1 = fully classical.

    Args:
        t: Time elapsed (seconds)
        tau_d: Decoherence time constant (seconds). Tunable parameter.

    Returns:
        Decoherence factor (0 to 1).
    """
    if tau_d <= 0:
        return 1.0  # Instant decoherence
    return 1.0 - np.exp(-t / tau_d)


def quantum_gate(t: float, tau_d: float) -> float:
    """(1 − ΓD(t)) = e^(−t/τ_D)

    The quantum gate: how much quantum protection remains.
    1 = fully quantum, 0 = fully classical.
    """
    return 1.0 - decoherence_factor(t, tau_d)


# ──────────────────────────────────────────────
# Quantum Tunneling
# ──────────────────────────────────────────────

# Physical constants
HBAR = 1.0546e-34   # Reduced Planck constant (J·s)
M_E = 9.109e-31     # Electron mass (kg) — used as reference

def tunneling_coefficient(V0: float, E: float, d: float, m: float = M_E) -> float:
    """T ≈ e^(−2κd) where κ = √(2m(V₀−E))/ℏ

    Tunneling probability through a rectangular barrier.

    Args:
        V0: Barrier height (eV, converted internally to Joules)
        E: Particle energy (eV)
        d: Barrier width (meters)
        m: Particle mass (kg, defaults to electron mass)

    Returns:
        Tunneling probability (0 to 1).
    """
    eV_to_J = 1.602e-19
    V0_J = V0 * eV_to_J
    E_J = E * eV_to_J

    if E_J >= V0_J:
        return 1.0  # No barrier

    kappa = np.sqrt(2 * m * (V0_J - E_J)) / HBAR
    return np.exp(-2 * kappa * d)


# ──────────────────────────────────────────────
# QI Equation — Candidate 1 (Additive/Engineering)
# ──────────────────────────────────────────────

@dataclass
class QICandidate1Params:
    """Parameters for Candidate 1: QI(t) = α·Cclass + β·(1−ΓD)·[Qi + δ·Qentangle] − γ·Qtunnel"""
    alpha: float = 1.0      # Classical weight
    beta: float = 1.0       # Quantum weight
    gamma: float = 0.5      # Tunneling vulnerability weight
    delta: float = 0.5      # Entanglement weight
    tau_d: float = 1e-5     # Decoherence time (seconds) — tunable


def qi_candidate1(
    c_class: float,
    qi_indeterminacy: float,
    q_entangle: float,
    q_tunnel: float,
    t: float,
    params: Optional[QICandidate1Params] = None,
) -> float:
    """QI(t) = α·Cclass + β·(1 − ΓD(t))·[Qi + δ·Qentangle] − γ·Qtunnel

    Candidate 1: Additive/Engineering form of the QI equation.

    Args:
        c_class: Classical security score (from coherence metric + anomaly detection)
        qi_indeterminacy: Quantum indeterminacy term (Robertson-Schrödinger + Von Neumann)
        q_entangle: Entanglement-based security term
        q_tunnel: Tunneling vulnerability term
        t: Time elapsed since quantum state preparation (seconds)
        params: Scaling coefficients and decoherence time

    Returns:
        QI score. Higher = more secure.
    """
    if params is None:
        params = QICandidate1Params()

    gate = quantum_gate(t, params.tau_d)

    classical_term = params.alpha * c_class
    quantum_term = params.beta * gate * (qi_indeterminacy + params.delta * q_entangle)
    tunnel_term = params.gamma * q_tunnel

    return classical_term + quantum_term - tunnel_term


# ──────────────────────────────────────────────
# QI Equation — Candidate 2 (Tensor/Theoretical)
# ──────────────────────────────────────────────

@dataclass
class QICandidate2Params:
    """Parameters for Candidate 2: QI = Cclass ⊗ e^(−Squantum)"""
    lam: float = 1.0    # Tunneling scaling (λ)
    mu: float = 1.0      # Entanglement scaling (μ)


def von_neumann_entropy(eigenvalues: np.ndarray) -> float:
    """S(ρ) = −Tr(ρ ln ρ) = −Σ λᵢ ln(λᵢ)

    Von Neumann entropy from eigenvalues of density matrix.

    Args:
        eigenvalues: Eigenvalues of the density matrix (must sum to 1).

    Returns:
        Von Neumann entropy (≥ 0). 0 = pure state, ln(d) = maximally mixed.
    """
    # Filter out zero eigenvalues to avoid log(0)
    eigs = eigenvalues[eigenvalues > 1e-15]
    return -np.sum(eigs * np.log(eigs))


def s_quantum(
    svn: float,
    phi_tunnel: float,
    e_entangle: float,
    params: Optional[QICandidate2Params] = None,
) -> float:
    """Squantum = SvN(ρ(t)) + λ·Φtunnel − μ·E(ρAB)

    Combined quantum action term for Candidate 2.

    Args:
        svn: Von Neumann entropy of system state
        phi_tunnel: WKB tunneling action integral
        e_entangle: Entanglement entropy
        params: Scaling coefficients

    Returns:
        Squantum value. Lower = more secure.
    """
    if params is None:
        params = QICandidate2Params()

    return svn + params.lam * phi_tunnel - params.mu * e_entangle


def qi_candidate2(
    c_class: float,
    svn: float,
    phi_tunnel: float,
    e_entangle: float,
    params: Optional[QICandidate2Params] = None,
) -> float:
    """S_QI = Cclass · e^(−Squantum)

    Candidate 2: Tensor/Theoretical form (scalar approximation).

    Note: The full tensor product QI = Cclass ⊗ e^(−Squantum) operates on
    Hilbert spaces. This function computes the scalar security metric
    S_QI = Tr(QI · ρ_total), which for a classical-quantum product state
    reduces to the product of classical and quantum factors.

    Args:
        c_class: Classical security score
        svn: Von Neumann entropy
        phi_tunnel: WKB tunneling action
        e_entangle: Entanglement entropy
        params: Scaling coefficients

    Returns:
        S_QI score. Higher = more secure.
    """
    sq = s_quantum(svn, phi_tunnel, e_entangle, params)
    return c_class * np.exp(-sq)


# ──────────────────────────────────────────────
# Convenience: Full pipeline from raw signals
# ──────────────────────────────────────────────

@dataclass
class QIResult:
    """Complete QI assessment result."""
    # Coherence
    sigma_phi: float = 0.0
    sigma_tau: float = 0.0
    sigma_gamma: float = 0.0
    coherence: float = 0.0
    # Candidate 1
    qi_score_c1: float = 0.0
    # Candidate 2
    qi_score_c2: float = 0.0
    # Decision
    decision: str = ""
    # Metadata
    t: float = 0.0
    tau_d: float = 0.0
    quantum_gate_value: float = 0.0


def full_qi_assessment(
    phases: np.ndarray,
    transport_probs: np.ndarray,
    amplitudes: np.ndarray,
    qi_indeterminacy: float = 0.5,
    q_entangle: float = 0.3,
    q_tunnel: float = 0.1,
    t: float = 1e-6,
    tau_d: float = 1e-5,
    auth_valid: bool = True,
    density_eigenvalues: Optional[np.ndarray] = None,
    phi_tunnel: float = 0.1,
    e_entangle: float = 0.3,
) -> QIResult:
    """Run full QI assessment pipeline on raw signal data.

    Args:
        phases: Phase measurements (radians)
        transport_probs: Transmission probabilities
        amplitudes: Signal amplitudes
        qi_indeterminacy: Quantum indeterminacy value
        q_entangle: Entanglement security value
        q_tunnel: Tunneling vulnerability value
        t: Time since quantum state prep (seconds)
        tau_d: Decoherence time (seconds)
        auth_valid: Authentication status
        density_eigenvalues: Eigenvalues for Von Neumann entropy (Candidate 2)
        phi_tunnel: WKB tunneling action (Candidate 2)
        e_entangle: Entanglement entropy (Candidate 2)

    Returns:
        QIResult with all computed values.
    """
    result = QIResult()

    # Coherence metric
    result.sigma_phi = phase_variance(phases)
    result.sigma_tau = transport_variance(transport_probs)
    result.sigma_gamma = gain_variance(amplitudes)
    result.coherence = coherence_metric(result.sigma_phi, result.sigma_tau, result.sigma_gamma)

    # Decoherence
    result.t = t
    result.tau_d = tau_d
    result.quantum_gate_value = quantum_gate(t, tau_d)

    # Candidate 1
    c1_params = QICandidate1Params(tau_d=tau_d)
    result.qi_score_c1 = qi_candidate1(
        c_class=result.coherence,
        qi_indeterminacy=qi_indeterminacy,
        q_entangle=q_entangle,
        q_tunnel=q_tunnel,
        t=t,
        params=c1_params,
    )

    # Candidate 2
    if density_eigenvalues is not None:
        svn = von_neumann_entropy(density_eigenvalues)
    else:
        # Default: use decoherence-scaled entropy approximation
        svn = -quantum_gate(t, tau_d) * np.log(max(quantum_gate(t, tau_d), 1e-15))

    result.qi_score_c2 = qi_candidate2(
        c_class=result.coherence,
        svn=svn,
        phi_tunnel=phi_tunnel,
        e_entangle=e_entangle,
    )

    # Decision
    result.decision = coherence_decision(result.coherence, auth_valid)

    return result
