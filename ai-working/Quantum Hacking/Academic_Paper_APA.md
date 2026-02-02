# Quantum Computing Security: Attack Vectors, Theoretical Constraints, and the Post-Quantum Threat Landscape

---

**Running head:** QUANTUM COMPUTING SECURITY

---

## Abstract

The emergence of fault-tolerant quantum computing presents unprecedented challenges to contemporary cryptographic infrastructure while simultaneously introducing novel attack surfaces on quantum hardware itself. This paper examines the theoretical foundations constraining quantum-enabled attacks, evaluates empirically validated threat vectors, and synthesizes current research on quantum computer vulnerabilities. We analyze the hypothesis that quantum entanglement enables spatially unbounded attacks on quantum systems, demonstrating through the no-communication theorem and Bell inequality interpretations that such attacks violate fundamental physical constraints. However, we identify substantive threats including cryptographic vulnerabilities to Shor's algorithm, harvest-now-decrypt-later (HNDL) strategies, and physical attacks exploiting quantum decoherence, side-channel leakage, and fault injection. Resource estimates for cryptographically relevant quantum computers have decreased from 20 million to fewer than 1 million qubits over six years, accelerating migration timelines to post-quantum cryptography. We propose a taxonomic framework for quantum security threats distinguishing between attacks *by* quantum computers, attacks *on* quantum computers, and attacks exploiting the classical-quantum interface.

**Keywords:** quantum computing, cybersecurity, post-quantum cryptography, Shor's algorithm, quantum entanglement, no-communication theorem, side-channel attacks, decoherence

---

## Introduction

Quantum computing represents a paradigm shift in computational capability with profound implications for cybersecurity. While classical computers manipulate deterministic bits, quantum computers exploit superposition and entanglement to perform certain computations exponentially faster than any known classical algorithm (Shor, 1994; Grover, 1996). This capability directly threatens the mathematical foundations of contemporary public-key cryptography, which relies on the computational intractability of integer factorization and discrete logarithm problems (Rivest et al., 1978).

Concurrently, speculation has emerged regarding whether quantum mechanical phenomena—particularly entanglement—might enable novel attack modalities transcending classical spatial and temporal constraints. The apparent non-locality demonstrated by Bell inequality violations (Bell, 1964; Aspect et al., 1982) has prompted hypotheses that quantum correlations could facilitate attacks across arbitrary distances without conventional communication channels.

This paper addresses three research questions: (1) Do quantum mechanical principles permit spatially unbounded attacks via entanglement? (2) What empirically validated attack vectors threaten quantum computing systems? (3) What is the current threat timeline for cryptographically relevant quantum computation?

---

## Theoretical Foundations

### Quantum Superposition and Measurement

A quantum bit (qubit) exists in a superposition state described by:

$$|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$$

where $\alpha, \beta \in \mathbb{C}$ and $|\alpha|^2 + |\beta|^2 = 1$ (Nielsen & Chuang, 2010). Upon measurement, the state collapses to $|0\rangle$ with probability $|\alpha|^2$ or $|1\rangle$ with probability $|\beta|^2$. Critically, the measurement outcome is fundamentally random—it cannot be predetermined or controlled by any physical process consistent with quantum mechanics.

### Quantum Entanglement

Two qubits may exist in an entangled state where the combined system cannot be described as a product of individual qubit states. The canonical Bell state is:

$$|\Phi^+\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$$

Measurement of either qubit instantaneously determines the state of the other, regardless of spatial separation. This correlation persists even when measurements are space-like separated, precluding any classical signal between measurement events (Aspect et al., 1982).

### The No-Communication Theorem

Despite the apparent non-locality of entanglement correlations, the no-communication theorem (Eberhard, 1978; Ghirardi et al., 1980) establishes that quantum mechanics cannot transmit information faster than light. The theorem proves that:

1. The reduced density matrix of one subsystem of an entangled pair is independent of any operation performed on the other subsystem.
2. Local measurement outcomes are statistically indistinguishable from random noise without classical communication to compare results.
3. Any attempt to encode information in one qubit's measurement basis choice does not affect the probability distribution observed by the distant party.

Formally, for any bipartite quantum state $\rho_{AB}$ and any local operation $\mathcal{E}_A$ on subsystem A:

$$\text{Tr}_A[\mathcal{E}_A \otimes \mathcal{I}_B(\rho_{AB})] = \text{Tr}_A[\rho_{AB}] = \rho_B$$

The reduced state $\rho_B$ remains unchanged regardless of operations on A (Peres & Terno, 2004).

### The No-Cloning Theorem

The no-cloning theorem (Wootters & Zurek, 1982; Dieks, 1982) states that no quantum operation can create an identical copy of an arbitrary unknown quantum state. This follows from the linearity of quantum mechanics and has profound security implications—it prevents eavesdroppers from copying quantum states without detection and fundamentally constrains information extraction from quantum systems.

### Bell Inequality Violations and Locality

Bell's theorem (Bell, 1964) demonstrates that quantum mechanical predictions for entangled systems cannot be reproduced by any local hidden variable theory satisfying:

1. **Locality**: The measurement outcome at one location is independent of the measurement setting at a space-like separated location.
2. **Realism**: Physical properties have definite values independent of measurement.

The CHSH inequality $|S| \leq 2$ (Clauser et al., 1969) is violated by quantum mechanics up to $S = 2\sqrt{2} \approx 2.83$. Loophole-free experiments have confirmed these violations with statistical significance exceeding $10^{-16}$ (Hensen et al., 2015; Giustina et al., 2015).

However, Bell inequality violations demonstrate the failure of *local realism*, not the possibility of faster-than-light communication. The correlations revealed by Bell tests require classical communication to detect—without comparing measurement records, neither party can determine that violations occurred (Brunner et al., 2014).

---

## Analysis of the Spatially Unbounded Attack Hypothesis

### Hypothesis Statement

The hypothesis under evaluation posits: "If qubits can be observed in superposition with defined probability, then attackers anywhere in the universe can theoretically target a quantum computer that transcends time and space using probabilities, statistics, and quantum theory."

### Theoretical Evaluation

This hypothesis fails on multiple grounds:

**Violation of No-Communication Theorem.** Any attack requiring information transfer from attacker to target system is constrained by the no-communication theorem. Entanglement correlations cannot carry information; they require classical communication to extract meaning. An attacker possessing one half of an entangled pair with a target quantum computer could not:

- Influence computation outcomes (measurement outcomes are random)
- Extract computation results (requires classical readout)
- Introduce errors selectively (would require controlled operations, which break entanglement)

**Entanglement Distribution Problem.** For an attacker to exploit entanglement with a target system, entangled pairs must first be distributed. This distribution is itself constrained by the speed of light and requires either:

- Physical transport of quantum systems
- Quantum communication channels (which are detectable)
- Pre-positioned entangled resources (which must be established through conventional means)

No mechanism exists for establishing entanglement with arbitrary distant systems without prior interaction.

**Measurement Collapse.** Any observation of a quantum system collapses its state. An attacker attempting to observe or influence a computation would necessarily disturb it, making the attack detectable. This is the foundation of quantum key distribution security (Bennett & Brassard, 1984).

**Causality Constraints.** Attacks "transcending time" would violate causality—a consequence quantum mechanics explicitly preserves. The no-signaling conditions embedded in quantum field theory prevent any operation from having observable effects outside its future light cone (Peres & Terno, 2004).

### Conclusion on Hypothesis

The hypothesis is inconsistent with established quantum mechanical theory and has no experimental support. While quantum mechanics exhibits genuine non-local correlations, these correlations cannot be exploited for communication or attack without violating theorems that are mathematical consequences of quantum mechanics' fundamental structure.

---

## Empirically Validated Quantum Security Threats

While spatially unbounded attacks are theoretically impossible, substantial quantum security threats exist within physical constraints.

### Cryptographic Threats

#### Shor's Algorithm

Shor's algorithm (Shor, 1994) factors integers in polynomial time $O(n^3)$, compared to the best classical algorithms' sub-exponential complexity $O(\exp(n^{1/3}(\log n)^{2/3}))$. This renders RSA, DSA, ECDSA, and Diffie-Hellman vulnerable to quantum attack.

Resource estimates have decreased dramatically:

| Year | RSA-2048 Qubit Estimate | Source |
|------|------------------------|--------|
| 2019 | 20 million | Gidney & Ekerå |
| 2021 | 4 million | Various |
| 2025 | <1 million | Gidney (Google) |

Current NIST guidance recommends deprecating vulnerable algorithms after 2030 and prohibiting them after 2035 (NIST, 2024).

#### Grover's Algorithm

Grover's search algorithm (Grover, 1996) provides quadratic speedup for unstructured search, reducing symmetric key security by half. AES-256 provides approximately 128-bit security against quantum adversaries—still secure, but requiring key size adjustments.

#### Harvest Now, Decrypt Later

Nation-state actors are collecting encrypted communications for future decryption once quantum capability materializes (BCG, 2025). Data requiring confidentiality beyond quantum computing timelines is already compromised.

### Physical Attacks on Quantum Hardware

#### Decoherence Attacks

Quantum coherence is extraordinarily fragile. Superconducting qubits require temperatures of approximately 15 mK and isolation from electromagnetic interference. Research demonstrates that attackers with physical or electromagnetic access can induce decoherence through:

- Thermal perturbation
- Electromagnetic interference
- Acoustic vibration
- Ionizing radiation

Such attacks cause computation failure without necessarily revealing their artificial origin (Xu et al., 2023).

#### Side-Channel Attacks

Power analysis attacks on quantum computer controllers reveal information about executed quantum operations (Xu et al., 2023). Timing analysis, electromagnetic emanations, and acoustic signatures provide additional side channels. Cloud-based quantum computers present particular vulnerabilities, as classical control infrastructure is shared across users (IBM Security, 2022).

#### Fault Injection

Microwave pulse injection at qubit resonance frequencies can flip qubit states mid-computation. Research demonstrates that fault injection can:

- Introduce targeted errors bypassing error correction
- Modify algorithm behavior
- Extract information through differential fault analysis

The similarity between injected faults and natural decoherence complicates detection (Rishabh et al., 2023).

#### Multi-Tenant Vulnerabilities

Cloud quantum computing platforms serve multiple users on shared hardware. Crosstalk between qubits—unintended electromagnetic coupling—creates potential for cross-tenant attacks. A malicious user could potentially influence neighboring qubits or extract information about concurrent computations (Harper et al., 2023).

---

## Threat Taxonomy

We propose a three-category taxonomy for quantum security threats:

### Category 1: Attacks BY Quantum Computers

Threats where quantum computers serve as attack tools against classical systems:

- Cryptographic attacks (Shor's, Grover's algorithms)
- Optimization attacks (solving NP-hard security problems)
- Machine learning attacks (quantum-enhanced adversarial ML)

### Category 2: Attacks ON Quantum Computers

Threats targeting quantum computing hardware and software:

- Decoherence/denial-of-service attacks
- Side-channel attacks on controllers
- Fault injection attacks
- Multi-tenant crosstalk exploitation
- Quantum memory attacks
- Calibration data poisoning

### Category 3: Attacks on the Classical-Quantum Interface

Threats exploiting the boundary between classical and quantum systems:

- Control signal manipulation
- Classical pre/post-processing vulnerabilities
- Quantum random number generator attacks
- Hybrid algorithm vulnerabilities

---

## Discussion

### Implications for Security Planning

Organizations should:

1. **Inventory cryptographic dependencies** and classify data by required confidentiality duration
2. **Assume HNDL is occurring** for high-value data
3. **Begin post-quantum migration** using NIST-standardized algorithms (CRYSTALS-Kyber, CRYSTALS-Dilithium)
4. **Monitor quantum hardware security research** as the field matures

### Research Directions

Priority research areas include:

- Quantum error correction security properties
- Multi-tenant isolation mechanisms
- Side-channel resistant quantum control systems
- Formal verification of quantum protocols
- Post-quantum cryptography implementation security

### Limitations

This analysis relies on current understanding of quantum mechanics, which may be incomplete. However, the no-communication theorem is a mathematical consequence of quantum mechanics' Hilbert space structure—any modification permitting faster-than-light communication would require abandoning quantum mechanics entirely, not merely extending it.

---

## Conclusion

Quantum computing presents genuine and substantial security threats, but these threats operate within physical constraints. The hypothesis that quantum entanglement enables spatially unbounded attacks is inconsistent with the no-communication theorem, no-cloning theorem, and causality preservation inherent to quantum mechanics.

The actual threat landscape includes cryptographic vulnerabilities requiring urgent migration to post-quantum standards, physical attacks exploiting quantum hardware fragility, and interface vulnerabilities in hybrid classical-quantum systems. With resource estimates for cryptographically relevant quantum computers decreasing and NIST deprecation timelines approaching, organizations must treat quantum security as an operational rather than theoretical concern.

The universe permits quantum computers to factor integers exponentially faster than classical computers. It does not permit attacks transcending spacetime. Both facts carry profound implications for cybersecurity—but only the facts consistent with physics should inform security planning.

---

## References

Aspect, A., Dalibard, J., & Roger, G. (1982). Experimental test of Bell's inequalities using time-varying analyzers. *Physical Review Letters*, 49(25), 1804-1807. https://doi.org/10.1103/PhysRevLett.49.1804

Bell, J. S. (1964). On the Einstein Podolsky Rosen paradox. *Physics Physique Fizika*, 1(3), 195-200. https://doi.org/10.1103/PhysicsPhysiqueFizika.1.195

Bennett, C. H., & Brassard, G. (1984). Quantum cryptography: Public key distribution and coin tossing. *Proceedings of IEEE International Conference on Computers, Systems and Signal Processing*, 175-179.

Boston Consulting Group. (2025). How quantum computing will upend cybersecurity. https://www.bcg.com/publications/2025/how-quantum-computing-will-upend-cybersecurity

Brunner, N., Cavalcanti, D., Pironio, S., Scarani, V., & Wehner, S. (2014). Bell nonlocality. *Reviews of Modern Physics*, 86(2), 419-478. https://doi.org/10.1103/RevModPhys.86.419

Clauser, J. F., Horne, M. A., Shimony, A., & Holt, R. A. (1969). Proposed experiment to test local hidden-variable theories. *Physical Review Letters*, 23(15), 880-884. https://doi.org/10.1103/PhysRevLett.23.880

Dieks, D. (1982). Communication by EPR devices. *Physics Letters A*, 92(6), 271-272. https://doi.org/10.1016/0375-9601(82)90084-6

Eberhard, P. H. (1978). Bell's theorem and the different concepts of locality. *Il Nuovo Cimento B*, 46(2), 392-419. https://doi.org/10.1007/BF02728628

Ghirardi, G. C., Rimini, A., & Weber, T. (1980). A general argument against superluminal transmission through the quantum mechanical measurement process. *Lettere al Nuovo Cimento*, 27(10), 293-298.

Gidney, C., & Ekerå, M. (2021). How to factor 2048 bit RSA integers in 8 hours using 20 million noisy qubits. *Quantum*, 5, 433. https://doi.org/10.22331/q-2021-04-15-433

Giustina, M., et al. (2015). Significant-loophole-free test of Bell's theorem with entangled photons. *Physical Review Letters*, 115(25), 250401. https://doi.org/10.1103/PhysRevLett.115.250401

Grover, L. K. (1996). A fast quantum mechanical algorithm for database search. *Proceedings of the 28th Annual ACM Symposium on Theory of Computing*, 212-219. https://doi.org/10.1145/237814.237866

Hensen, B., et al. (2015). Loophole-free Bell inequality violation using electron spins separated by 1.3 kilometres. *Nature*, 526(7575), 682-686. https://doi.org/10.1038/nature15759

National Institute of Standards and Technology. (2024). Post-quantum cryptography standardization. https://csrc.nist.gov/projects/post-quantum-cryptography

Nielsen, M. A., & Chuang, I. L. (2010). *Quantum computation and quantum information* (10th anniversary ed.). Cambridge University Press.

Peres, A., & Terno, D. R. (2004). Quantum information and relativity theory. *Reviews of Modern Physics*, 76(1), 93-123. https://doi.org/10.1103/RevModPhys.76.93

Rivest, R. L., Shamir, A., & Adleman, L. (1978). A method for obtaining digital signatures and public-key cryptosystems. *Communications of the ACM*, 21(2), 120-126. https://doi.org/10.1145/359340.359342

Shor, P. W. (1994). Algorithms for quantum computation: Discrete logarithms and factoring. *Proceedings of the 35th Annual Symposium on Foundations of Computer Science*, 124-134. https://doi.org/10.1109/SFCS.1994.365700

Wootters, W. K., & Zurek, W. H. (1982). A single quantum cannot be cloned. *Nature*, 299(5886), 802-803. https://doi.org/10.1038/299802a0

Xu, C., et al. (2023). Classification of quantum computer fault injection attacks. *arXiv preprint*. https://arxiv.org/abs/2309.05478

---

*Prepared with research assistance from Claude Code (Anthropic). All theoretical analysis based on peer-reviewed literature and established physical principles.*
