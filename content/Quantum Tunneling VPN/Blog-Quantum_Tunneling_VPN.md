---
title: "From Macroscopic Quantum Tunneling to Quantum Keys: How the Nobel Prize Will Secure Brain-Computer Interfaces"
subtitle: "Inspired by John Martinis' Nobel-winning work on macroscopic quantum tunneling, a deep dive into where physics meets network security — and why the future might be closer than we think"
tags: ["#QuantumComputing", "#Cybersecurity", "#VPN", "#Neuroscience", "#ONI", "#QKD", "#BCI", "#PostQuantumCryptography"]
---

# From Macroscopic Quantum Tunneling to Quantum Keys: How the Nobel Prize Will Secure Brain-Computer Interfaces

### Inspired by John Martinis' Nobel-winning work on macroscopic quantum tunneling, a deep dive into where physics meets network security — and why the future might be closer than we think

· · ·

## The Question That Started Everything

**Quantum tunneling** is a phenomenon where particles pass through barriers they don't have enough energy to climb over, because at quantum scales, particles exist as probability waves that can extend through obstacles and emerge on the other side.

Imagine rolling a ball toward a hill. If the ball doesn't have enough energy to reach the top, it rolls back. Classical physics says: barrier wins.

Quantum mechanics says: *not so fast.*

Here's a hypothesis that seized me while listening to Neil deGrasse Tyson interview John Martinis on StarTalk last week:

*If quantum tunneling allows particles to pass through barriers they shouldn't have the energy to cross — and if this effect scales up to macroscopic systems you can hold in your hand — then what's stopping us from building networks that tunnel data the same way? Not metaphorically. Physically.*

VPNs already use the word "tunnel." We encrypt packets and send them through hostile public networks, trusting math to protect us. But what if the tunnel wasn't mathematical abstraction? What if data could quantum tunnel through barriers — bypassing interception not through encryption, but through the fundamental physics of reality itself?

It's an elegant thought. It draws on real physics — the same physics that just won Martinis, Clarke, and Devoret the 2025 Nobel Prize. And it captures something genuinely strange about quantum mechanics: barriers aren't absolute.

But there's a problem: the universe has rules, and those rules operate at scales that matter.

Let me explain what Martinis actually discovered — why it's revolutionary — and then show you where the real convergence between quantum tunneling and network security is happening.

· · ·

## Why I'm Writing This: Knowing What We Don't Know

Before we dive deeper, I want to be transparent about something.

Neil deGrasse Tyson once said in his MasterClass:

> *"One of the greatest challenges in life is knowing enough to think you're right, but not enough to know you're wrong."*

That quote is why this article exists.

Listening to Neil interview John Martinis on StarTalk, I found myself connecting dots between quantum tunneling and network security — between Josephson junctions and VPN protocols — between macroscopic quantum effects and the neural security frameworks I've been developing. The connections felt compelling. Maybe too compelling.

I've spent considerable time developing the **ONI (Organic Neural Interface) framework** for neural security — exploring coherence breaches, the Scale-Frequency Invariant, and threats to brain-computer interfaces. I know enough about quantum mechanics to see tantalizing connections. But do I know enough to know where I'm wrong?

This piece is my attempt to find out. To map the boundaries of what quantum tunneling can and cannot do for network security. To identify where the physics supports my intuitions — and where it doesn't. To strategize future directions for the ONI project by understanding, honestly, what we're working with.

**So consider this article a public exploration — research notes toward future iterations. The wavefunction hasn't collapsed yet. Let's see where the probabilities cluster.**

· · ·

## What Is Quantum Tunneling? (And What Did Martinis Prove?)

### The Basic Phenomenon

At quantum scales, particles don't have definite positions — they have probability distributions. Part of that probability extends *through* the barrier. And sometimes, the particle appears on the other side without ever having the energy to "climb over."

This is **quantum tunneling**. It's not a loophole or a trick. It's how the universe actually works.

### The Nobel-Winning Breakthrough

For decades, physicists assumed quantum tunneling only happened at subatomic scales — electrons, photons, individual particles. **John Martinis**, working with John Clarke and Michel Devoret at UC Berkeley in 1984-1985, proved something astonishing:

*Quantum tunneling can happen in systems large enough to hold in your hand.*

Using **Josephson junctions** — two superconducting metals separated by a thin insulator, cooled to 15 millikelvin — they demonstrated that billions of electrons, behaving as **Cooper pairs**, could tunnel coherently through barriers as a single quantum entity.

The Royal Swedish Academy called it "the first clear demonstration of macroscopic quantum tunnelling."

**Stop and think about that.** Before Martinis, the quantum world was microscopic — safely contained in atoms and particles too small to see. After Martinis, we knew quantum effects could reach up into the world of things we can touch. That's not a small shift. That's a paradigm change.

### Tunneling Traversal Time: The Part That Matters

Here's what caught my attention in the StarTalk episode. Tyson asked Martinis: *"Does tunneling happen instantly?"*

The answer is no. And the physics of *why* is crucial.

Tunneling takes time. Researchers at the University of Toronto measured 0.61 milliseconds for atoms tunneling through a 1.3-micrometre barrier. Even more striking: July 2025 research from POSTECH revealed that electrons actually collide with atomic nuclei *inside* the tunnel — it's not a clean pass-through.

There's a traversal. There's a duration. There's something happening inside the barrier.

In my ONI framework, we call this the **liminal phase** — the state between states, where the system is neither here nor there. And it's governed by physics I'll return to shortly.

· · ·

## How VPN Tunneling Actually Works

Let's ground ourselves in the technology we use today.

When you connect to a VPN, your device:

1. Establishes an encrypted connection to a VPN server
2. Encapsulates your data packets inside encrypted packets
3. Sends them through the public internet (the "hostile" network)
4. The VPN server decrypts and forwards to the destination

The "tunnel" is a metaphor. Your packets don't phase through routers — they travel the same physical paths as everyone else's. The protection comes from encryption: even if an attacker intercepts your packets, they see gibberish.

### The Parallel Worth Noting

In quantum tunneling, the barrier is an energy potential — an insulator, a gap, a field.

In VPN tunneling, the barrier is adversarial observation — the threat of interception, analysis, exploitation.

Both tunnels exist to get something valuable through something hostile.

**Here's a question for you:** Is the parallel between quantum tunneling and VPN tunneling merely linguistic coincidence, or does it point to something deeper about how we think about barriers and bypass?

· · ·

## Could True Quantum Tunneling VPNs Exist?

Now that we understand both phenomena, let's assess the seductive idea honestly.

### The Physics Challenge

Quantum tunneling operates at:
- Subatomic to nanometer scales (electrons, Cooper pairs)
- Cryogenic temperatures (millikelvin)
- Isolated, coherent systems

Network data involves:
- Macroscopic information encoded in electrical/optical signals
- Room temperature (or close to it)
- Massive decoherence from environmental interaction

### The Mathematics: Where Dreams Meet Reality

Here's the equation that governs quantum tunneling probability:

```
T = e^(-2*kappa*L)

where:
kappa = sqrt(2m(V0 - E)) / h-bar

m     = particle mass
V0    = barrier potential height
E     = particle energy
L     = barrier width
h-bar = reduced Planck constant (1.055 x 10^-34 J*s)
```

**The critical insight:** Transmission probability decays *exponentially* with barrier width L and particle mass m.

Let me make this concrete:

```
+----------------+---------------------------------------+
| Barrier Width  | Transmission Probability (electron)   |
+----------------+---------------------------------------+
| 1 nanometer    | ~10^-5 (0.001%)                       |
+----------------+---------------------------------------+
| 10 nanometers  | ~10^-50                               |
+----------------+---------------------------------------+
| 1 micrometer   | ~10^-5000                             |
+----------------+---------------------------------------+
| 1 millimeter   | Effectively 0                         |
+----------------+---------------------------------------+
```

Network-relevant distances (meters to kilometers) are `10^12` times larger than atomic scales. The exponential decay makes true quantum tunneling for data transmission mathematically impossible at these scales.

### The No-Cloning Problem

Even if you could encode network data in quantum states and tunnel them, you'd face the **no-cloning theorem**. You cannot copy an arbitrary quantum state. This is great for security — but problematic for networking, where we need to route, replicate, and process data.

### Verdict: Not With Current Physics

True quantum tunneling VPNs — where data phases through barriers via quantum mechanical tunneling — remain in the realm of theoretical speculation. The physics doesn't scale.

**But here's the twist:** We don't need quantum tunneling for data if we can use it for *keys*.

QKD gives us the security benefits of quantum mechanics (observer-detectable interception) without requiring data itself to tunnel. The keys traverse the quantum realm; the data travels classically, protected by those keys.

**This is the kind of lateral thinking that drives real innovation.** When one path is blocked by physics, ask: what *can* we use from this domain?

· · ·

## The Real Convergence: Where Physics Meets Network Security

Here's where it gets interesting. The convergence isn't metaphorical — it's operational.

### 1. Quantum Key Distribution (QKD): The Observer Effect as Security

In quantum mechanics, observation changes the system. This isn't philosophy — it's physics.

**QKD exploits this directly.** When you distribute encryption keys using quantum states (typically photon polarization), any eavesdropper who tries to intercept the key *disturbs* the quantum state. The disturbance is detectable. The key is discarded. The attacker gains nothing.

This is the **Coherence Breach** weaponized for defense.

In my ONI framework's Scale-Frequency Invariant:

> **`f x S ~ k`**

When an attacker probes the system (increasing frequency f), the spatial coherence (S) must collapse to maintain the constant k. In QKD, this collapse *is* the security mechanism. The attacker's observation is self-defeating.

### 2. Post-Quantum VPNs: Racing the Clock

Nation-states are already stockpiling encrypted traffic, waiting for quantum computers to break RSA and ECC. This is called **HNDL — Harvest Now, Decrypt Later**.

The VPN industry is responding:

```
+-------------+--------------------------------------------------------+
| Provider    | 2025-2026 Development                                  |
+-------------+--------------------------------------------------------+
| NordVPN     | Post-quantum encryption across all apps (May 2025);    |
|             | PQ authentication planned H1 2026                      |
+-------------+--------------------------------------------------------+
| ExpressVPN  | Quantum-resistant feature expansion                    |
+-------------+--------------------------------------------------------+
| Proton VPN  | Quantum-proof architecture roadmap                     |
+-------------+--------------------------------------------------------+
```

These aren't quantum tunneling VPNs. They're classical VPNs with quantum-resistant cryptography. The tunnel is still mathematical — but the math is evolving to survive the quantum threat.

### 3. Space-Based QKD: The Infrastructure of Tomorrow

Nokia, Honeywell, and Colt are launching the first commercial space-based QKD trials in 2026-2027. The European Space Agency's Eagle-1 satellite launches in 2026 for EuroQCI.

Why space? QKD over fiber has distance limits (~100km without repeaters). Satellites can distribute quantum keys globally, enabling truly quantum-secured networks at scale.

· · ·

## Part 1: The Quantum Encryption Revolution

### The Fundamental Irony

The same physics that enables quantum tunneling — superposition, entanglement, the uncertainty principle — creates both the **greatest threat** to current encryption AND the **ultimate solution** for future security.

**Think about that paradox.** The same quantum mechanics that will break RSA encryption also provides mathematically unbreakable security when used correctly. Physics giveth and physics taketh away.

### The Threat: Shor's Algorithm

Peter Shor's 1994 algorithm can factor large integers in polynomial time on a quantum computer. This means:

- **RSA-2048:** 1 billion years to crack classically -> potentially hours on a quantum computer
- **ECC (Elliptic Curve):** Same vulnerability
- **Every HTTPS connection, every VPN, every digital signature** using these algorithms: eventually breakable

Current estimate from Google's Craig Gidney: fewer than **1 million noisy qubits** could break RSA-2048 in under a week.

### The Solution: Quantum Mechanics as Security

But here's what's fascinating — the same quantum effects that threaten classical encryption provide *fundamentally unbreakable* security when used correctly.

The security doesn't come from computational hardness. It comes from the **laws of physics themselves**.

· · ·

## Part 2: How Quantum Encryption Actually Works

### Layer 1: The No-Cloning Theorem — The Foundation of Everything

In 1982, Wootters, Zurek, and Dieks proved something profound: **it is impossible to create an identical copy of an arbitrary unknown quantum state**.

This isn't a technological limitation. It's a mathematical necessity arising from the linearity of quantum mechanics.

**Security implication:**

```
+--------------------------------------------------------------------+
|                     NO-CLONING THEOREM IN ACTION                   |
+--------------------------------------------------------------------+
|                                                                    |
|  Eve tries to intercept and copy quantum key                       |
|            |                                                       |
|            v                                                       |
|  No-cloning theorem PREVENTS perfect copy                          |
|            |                                                       |
|            v                                                       |
|  Eve's measurement DISTURBS quantum state                          |
|            |                                                       |
|            v                                                       |
|  Alice and Bob DETECT anomalies in error rate                      |
|            |                                                       |
|            v                                                       |
|  Key is DISCARDED - Eve learns nothing                             |
|                                                                    |
|  Result: Physics itself prevents eavesdropping                     |
|                                                                    |
+--------------------------------------------------------------------+
```

The best an attacker can achieve is **5/6 fidelity** (83.3%) — and even this imperfect cloning is detectable through error rate analysis.

### Layer 2: Quantum Random Number Generation (QRNG)

Every encryption system depends on randomness. Keys, initialization vectors, session tokens — all start with numbers that must be unpredictable.

**The problem with classical randomness:**
- Pseudo-random number generators (PRNGs) are deterministic
- Given the seed, the entire sequence is predictable
- Side-channel attacks can reveal the seed

**QRNG measures true randomness** from quantum phenomena — typically photon arrival times, vacuum fluctuations, or beam splitter outputs. This randomness is fundamentally unpredictable because it arises from quantum indeterminacy, not algorithmic complexity.

**Current implementations:**
- ID Quantique (commercial QRNG chips)
- Quantinuum Quantum Origin
- Cisco Outshift QRNG
- Space-grade QRNGs for satellite communications

### Layer 3: Quantum Key Distribution (QKD)

QKD protocols use quantum states to distribute encryption keys with **information-theoretic security** — security that doesn't depend on computational assumptions.

**BB84 Protocol (1984):**

Charles Bennett and Gilles Brassard's protocol works like this:

1. Alice generates random bits and random polarization bases (rectilinear or diagonal)
2. Alice encodes bits in photon polarizations and sends to Bob
3. Bob measures using randomly chosen bases
4. Alice and Bob publicly compare bases (not values)
5. They keep only bits where bases matched
6. They check a sample for errors — high error rate = eavesdropping detected

**E91 Protocol (1991):**

Artur Ekert's protocol uses **entangled photon pairs** (Bell states):

```
|Phi+> = (1/sqrt(2))(|00> + |11>)
```

When Alice and Bob share entangled pairs:
- Their measurements are perfectly correlated
- Any eavesdropping breaks the entanglement
- Bell inequality violations confirm the channel is secure

**2025 Development — Hybrid Protocols:**

New frameworks combine BB84, B92, E91, and GHZ protocols with AI-assisted dynamic selection:
- Average quantum bit error rate (QBER): 0.02
- Key generation rate: 12 bits per round
- E91 consistently produces Bell violation S=2.5 (confirming entanglement fidelity)

### Layer 4: Quantum Secure Direct Communication (QSDC)

Here's where it gets revolutionary. **QSDC transmits messages directly through quantum channels without using keys at all.**

Traditional approach:
```
QKD distributes key -> Classical encryption with key -> Message transmission
```

QSDC approach:
```
Message encoded in quantum states -> Transmitted directly -> Decoded at destination
```

**Advantages:**
- No key storage or management
- Eliminates key distribution vulnerabilities
- Information encrypted and decrypted simultaneously
- Any attack yields only random noise

**Current state:** 15-user network demonstrated over 40km fiber, 50 bps at 1.5 km (sufficient for text, images, audio).

### Layer 5: Post-Quantum Cryptography

While QKD provides physics-based security, we also need **classical algorithms that resist quantum attack** for situations where QKD isn't practical.

**NIST-Standardized Algorithms (2024):**

```
+-------------------------+---------------+-----------+---------------------+
| Algorithm               | Type          | Standard  | Use Case            |
+-------------------------+---------------+-----------+---------------------+
| CRYSTALS-Kyber (ML-KEM) | Lattice-based | FIPS 203  | Key encapsulation   |
+-------------------------+---------------+-----------+---------------------+
| CRYSTALS-Dilithium      | Lattice-based | FIPS 204  | Digital signatures  |
| (ML-DSA)                |               |           |                     |
+-------------------------+---------------+-----------+---------------------+
| SPHINCS+ (SLH-DSA)      | Hash-based    | FIPS 205  | Digital signatures  |
+-------------------------+---------------+-----------+---------------------+
| FALCON                  | Lattice-based | Pending   | Compact signatures  |
+-------------------------+---------------+-----------+---------------------+
```

**The mathematical foundation — Lattice Problems:**

```
Module Learning With Errors (M-LWE):

b(x) = a(x)*s(x) + e(x)

Where:
- a(x) = public polynomial (random coefficients)
- s(x) = secret polynomial (small coefficients)
- e(x) = error polynomial (small coefficients)

Finding s from (a, b) is computationally hard - even for quantum computers.
```

Unlike RSA (factoring) or ECC (discrete logarithm), lattice problems have no known efficient quantum algorithm. This is the mathematical bedrock of post-quantum security.

### Layer 6: Quantum Digital Signatures

Authentication in a post-quantum world requires new approaches:

**Post-Quantum Signatures (Classical Algorithms):**
- **Dilithium/ML-DSA:** Lattice-based, NIST standardized
- **SPHINCS+:** Hash-based, relies only on hash function security
- **Google Cloud KMS** now offers both ML-DSA-65 and SLH-DSA-SHA2-128S

**True Quantum Signatures:**
- Use quantum states as signature keys
- Security based on no-cloning theorem
- Public keys are quantum states that can only be created by someone knowing the private classical key

### Layer 7: Quantum Homomorphic Encryption

The ultimate goal: **compute on encrypted data without ever decrypting it**.

```
+-----------------------------------------------------------------+
|            QUANTUM HOMOMORPHIC ENCRYPTION                       |
+-----------------------------------------------------------------+
|                                                                 |
|  Client encrypts data -> Sends to quantum server                |
|            |                                                    |
|            v                                                    |
|  Server performs computation ON ENCRYPTED DATA                  |
|            |                                                    |
|            v                                                    |
|  Server returns encrypted result                                |
|            |                                                    |
|            v                                                    |
|  Client decrypts -> Gets answer                                 |
|                                                                 |
|  Server NEVER sees plaintext data                               |
|                                                                 |
+-----------------------------------------------------------------+
```

This enables secure cloud quantum computing where you can delegate computations to untrusted servers while maintaining complete privacy.

· · ·

## Part 3: Bell States — The Heart of Quantum Security

Understanding Bell states is essential to understanding quantum security.

### The Four Bell States

These are maximally entangled two-qubit states:

```
|Phi+> = (1/sqrt(2))(|00> + |11>)    <- Most common in protocols
|Phi-> = (1/sqrt(2))(|00> - |11>)
|Psi+> = (1/sqrt(2))(|01> + |10>)
|Psi-> = (1/sqrt(2))(|01> - |10>)
```

### Why Bell States Matter for Security

When Alice and Bob share a Bell state:

1. **Perfect correlation:** Measuring one qubit instantly determines the other's state
2. **Non-locality:** This correlation exists regardless of distance
3. **Eavesdropping detection:** Any measurement by Eve breaks the correlation
4. **Bell inequality violation:** Quantum correlations exceed what's classically possible — this proves the channel is genuinely quantum (and secure)

In the E91 protocol, Alice and Bob verify security by checking Bell inequality violations. If S > 2 (the classical limit), the channel is quantum and secure. If `S <= 2`, either the source isn't entangled or someone is eavesdropping.

**Here's a conceptual challenge:** Bell states demonstrate "spooky action at a distance" — Einstein's phrase for quantum entanglement. How do you reconcile the fact that measuring one particle *instantly* affects its entangled partner, regardless of distance, with the principle that information cannot travel faster than light?

The answer: you can't *use* entanglement to send information faster than light. The correlations only become meaningful when Alice and Bob compare their measurements — which requires classical communication. But this subtlety is precisely what makes QKD secure: the quantum correlations are real, but exploiting them requires the kind of classical comparison that reveals any eavesdropping.

· · ·

## Part 4: The Complete Quantum Encryption Stack

Here's how all these pieces fit together:

```
+-------------------------------------------------------------------------+
|                    QUANTUM ENCRYPTION ARCHITECTURE                      |
+-------------------------------------------------------------------------+
|                                                                         |
|  LAYER 7: COMPUTATION                                                   |
|  +-- Quantum Homomorphic Encryption (compute on encrypted data)         |
|                                                                         |
|  LAYER 6: AUTHENTICATION                                                |
|  +-- Post-Quantum Signatures (Dilithium, SPHINCS+)                      |
|  +-- True Quantum Signatures (no-cloning based)                         |
|                                                                         |
|  LAYER 5: KEY DISTRIBUTION                                              |
|  +-- QKD Protocols (BB84, E91, hybrid)                                  |
|  +-- QSDC (keyless direct communication)                                |
|  +-- Post-Quantum KEMs (Kyber/ML-KEM)                                   |
|                                                                         |
|  LAYER 4: DATA ENCRYPTION                                               |
|  +-- Symmetric encryption with quantum-distributed keys                 |
|  +-- Quantum one-time pads                                              |
|                                                                         |
|  LAYER 3: RANDOMNESS                                                    |
|  +-- QRNG (true quantum random number generation)                       |
|                                                                         |
|  LAYER 2: ENTANGLEMENT INFRASTRUCTURE                                   |
|  +-- Bell state generation and distribution                             |
|  +-- Quantum repeaters (entanglement swapping)                          |
|  +-- Quantum memories                                                   |
|                                                                         |
|  LAYER 1: PHYSICAL SECURITY PRINCIPLES                                  |
|  +-- No-Cloning Theorem (prevents copying)                              |
|  +-- Heisenberg Uncertainty (measurement disturbs)                      |
|  +-- Quantum Tunneling (enables qubit operations)                       |
|  +-- Superposition and Collapse (the observer effect)                   |
|                                                                         |
+-------------------------------------------------------------------------+
```

· · ·

## Part 5: Quantum Computers on the Moon

Now let's return to the infrastructure question: where do we put the quantum computers that power this encryption ecosystem?

### Permanently Shadowed Regions (PSRs)

Near the lunar poles — particularly the South Pole at craters like **Shackleton** and **Faustini** — exist regions that **never receive direct sunlight**. These are called **Permanently Shadowed Regions (PSRs)**.

Temperatures: **20-40 Kelvin** (-253C to -233C). Colder than Pluto.

### The Physics Case for Lunar Quantum Computing

```
+-----------------+-------------------------+-------------------------------+
| Property        | Earth Requirement       | Lunar PSR Provides            |
+-----------------+-------------------------+-------------------------------+
| Temperature     | 10-20 mK (dilution      | 20-40 K (natural)             |
|                 | refrigerator)           |                               |
+-----------------+-------------------------+-------------------------------+
| Cooling energy  | Massive infrastructure  | Up to 85% reduction           |
+-----------------+-------------------------+-------------------------------+
| Vacuum          | Complex chambers        | Natural (~10^-12 torr)        |
+-----------------+-------------------------+-------------------------------+
| Vibration       | Isolation systems       | Seismically quiet             |
+-----------------+-------------------------+-------------------------------+
| EM interference | Extensive shielding     | Far-side: complete radio      |
|                 |                         | silence from Earth            |
+-----------------+-------------------------+-------------------------------+
```

### The Gap: Still Need Dilution Refrigerators

Superconducting qubits require **10-20 millikelvin** — still **1,000x colder** than PSR temperatures. You still need dilution refrigerators. But they'd be *far* more efficient starting from 40K instead of 300K.

### Helium-3: The Lunar Resource

**Interlune** is planning to mine lunar **Helium-3** — critical for dilution refrigerators:
- **2027:** Helium-3 extraction test mission
- **2029:** Pilot plant on the Moon
- **2030s:** Tech demos for lunar quantum computing

### Earth-Moon Quantum Links

**NASA's Deep Space Quantum Link** project aims to establish quantum communication between Earth and the **Lunar Gateway**.

Current state:
- Maximum demonstrated entanglement distribution: ~2,000 km
- Earth-Moon distance: 384,400 km
- Gap factor: **192x**

This requires **quantum repeaters** using entanglement swapping:

```
With repeaters:    Rate ~ 1/poly(D)   (polynomial decay)
Without repeaters: Rate ~ 1/exp(D)    (exponential decay)
```

Current progress:
- 10 secret bits/second over 1,000 km with 9 repeater stations
- 90% storage-and-retrieval efficiency in quantum memories (Welinq QDrive, 2025)
- 99% fidelity entanglement over 30 km for 17 days (Deutsche Telekom, March 2025)

**Question to consider:** What happens to security when your quantum computer is 384,400 km away? The ~2.5-second round-trip latency rules out real-time applications. But for asynchronous processing of sensitive data — where security matters more than speed — lunar quantum computing might offer the most secure architecture imaginable. What applications would benefit most from this tradeoff?

· · ·

## Part 6: Neural Terminals to Quantum Computers

Here's the hypothesis that connects everything: **Could BCIs act as quantum terminals?**

### The Universal Quantum Terminal Architecture

A 2024 paper in *Scientific Reports* describes this concept:

> "To democratize the quantum advantage, an optimized cost-benefit strategy entails the deployment of small-scale, non-error-corrected mobile devices, which delegate computational tasks to error-corrected servers."

Simple quantum devices (terminals) connect via entanglement to powerful quantum servers (cloud). The terminal doesn't need to be a full quantum computer — just capable of generating and measuring entangled photons.

### IBM and Inclusive Brains: It's Already Starting

In **June 2025**, IBM and Inclusive Brains announced a joint study to:
- Apply **quantum machine learning** to brain activity classification
- Boost performance of multi-modal **brain-machine interfaces**

### Quantum Effects in the Brain

Research suggests quantum coherence may exist in biological neural systems:
- **Photosynthesis:** Quantum coherence at room temperature (hundreds of femtoseconds)
- **Bird navigation:** Quantum entanglement in cryptochrome proteins (microseconds)
- **Microtubules:** Room-temperature quantum oscillations in neural structures

**If** biological neural systems exhibit quantum effects, BCIs might need to preserve quantum coherence — making them natural quantum terminals.

### The Complete Vision

```
+---------------------------------------------------------------------------------+
|                    QUANTUM NEURAL NETWORK ARCHITECTURE                          |
+---------------------------------------------------------------------------------+
|                                                                                 |
|  +-------------+    +--------------+    +-------------+    +----------------+   |
|  |   NEURAL    |    |   QUANTUM    |    |   QUANTUM   |    |    LUNAR PSR   |   |
|  |  INTERFACE  |<-->|   TERMINAL   |<-->|  REPEATER   |<-->|    QUANTUM     |   |
|  |   (BCI)     |    |   (Local)    |    |   CHAIN     |    |    COMPUTER    |   |
|  +-------------+    +--------------+    +-------------+    +----------------+   |
|        |                   |                   |                   |            |
|        v                   v                   v                   v            |
|   Neural signals     QKD-secured         Earth-Moon          Fault-tolerant    |
|   (classical +       classical           entanglement        computation in    |
|   potentially        channel             distribution        natural cryo      |
|   quantum)                                                                      |
|                                                                                 |
|  SECURITY: `f x S ~ k` coherence monitoring at every layer                      |
|                                                                                 |
+---------------------------------------------------------------------------------+
```

· · ·

## Part 7: The `f x S ~ k` Framework Applied

Let me connect my Scale-Frequency Invariant to this entire quantum encryption ecosystem.

### The Formula

> **`f x S ~ k`**

Where:
- **f** = frequency of interaction/probing
- **S** = spatial extent of coherence
- **k** = system stability constant

### Application Across Domains

**In Quantum Computing (Vulnerability):**
When an attacker probes a quantum computer (increasing f), coherence (S) collapses. The computation fails. This is a **denial-of-service attack written into physics**.

**In QKD (Security Feature):**
If an attacker increases their interaction frequency with a quantum channel, the spatial coherence of the key collapses. But here, **collapse is the alarm** — eavesdropping is detected.

**In Neural Interfaces (The Bridge):**
If biological neural systems exhibit quantum coherence, then:
- Neural interfaces must preserve coherence to function optimally
- Attacks that disrupt coherence degrade BCI performance
- The `f x S ~ k` framework applies to neural-quantum security

**The Unifying Insight:**
Coherence is the fundamental resource. Whether we're protecting quantum computers, quantum networks, or quantum-biological interfaces, the physics is the same. The difference is whether coherence collapse is a **vulnerability** or a **security feature**.

**This is the kind of cross-domain thinking that opens new research directions.** When you see the same mathematical relationship appearing in different fields — quantum physics, cryptography, neuroscience — it suggests an underlying unity worth exploring.

· · ·

## The Catch: What We Don't Know

This framework isn't bulletproof. There are gaps I can't fill yet.

**Does `f x S ~ k` hold universally?** I've derived it from neural signaling principles and quantum coherence theory. But it needs experimental validation across domains — from microtubules to quantum repeater networks to lunar PSR systems.

**Can biological quantum coherence be harnessed?** The microsecond coherence times in microtubules are intriguing, but we don't know if they're functionally significant or exploitable.

**What happens in the liminal phase?** Tunneling traversal time research shows something happens *inside* barriers. Is there security-relevant physics we're missing?

**When will quantum advantage arrive?** Estimates range from 5-15 years for cryptographically relevant quantum computers. The "harvest now, decrypt later" threat is already real.

I'm publishing anyway because we need shared vocabulary. We need researchers across physics, cryptography, neuroscience, and security talking to each other.

**The best ideas often come from the boundaries between disciplines.** If you're a student reading this, that's where I'd encourage you to look. Not deep in the center of any one field, but at the edges where fields collide.

· · ·

## Timeline: What's Possible When

```
+--------------+-------------------------------------------------------------+
| Timeframe    | Capability                                                  |
+--------------+-------------------------------------------------------------+
| NOW          | Post-quantum encryption in VPNs (NordVPN, Proton)           |
| (2025-2026)  | QKD over metropolitan distances                             |
|              | QRNG in commercial products                                 |
|              | Google Cloud KMS quantum-safe signatures                    |
+--------------+-------------------------------------------------------------+
| NEAR-TERM    | Space-based QKD trials (Nokia/Honeywell satellites)         |
| (2026-2028)  | Artemis III landing at lunar South Pole                     |
|              | 15+ user QSDC networks                                      |
+--------------+-------------------------------------------------------------+
| MEDIUM-TERM  | Continental quantum networks with repeaters                 |
| (2028-2032)  | Quantum-enhanced BCI research matures                       |
|              | Lunar Helium-3 extraction begins                            |
+--------------+-------------------------------------------------------------+
| LONG-TERM    | Earth-Moon quantum links (NASA Deep Space Quantum Link)     |
| (2030s)      | Lunar PSR quantum computing tech demos                      |
|              | Quantum homomorphic encryption practical                    |
+--------------+-------------------------------------------------------------+
| FAR-TERM     | Operational lunar quantum computers as cloud resources      |
| (2040s+)     | Neural quantum terminals connecting to off-world compute    |
|              | Global quantum internet                                     |
+--------------+-------------------------------------------------------------+
```

· · ·

## Part of Something Larger: ONI and Neural Security

This research crystallizes several directions for the ONI framework:

### 1. QKD-Secured Neural Interfaces

If brain-computer interfaces become widespread, QKD principles could provide security that no classical encryption can match. Any attempt to intercept the signal between brain and device collapses the quantum key, alerting the user to tampering.

**The Coherence Breach as a defense mechanism.**

### 2. Quantum-Biological Security Layer

If neurons exhibit quantum coherence, security frameworks must account for quantum effects at the biological level. The `f x S ~ k` framework may apply directly to neural signal integrity.

### 3. Lunar PSR as Ultimate Secure Backend

For the most sensitive neural computations — consciousness mapping, memory storage, cognitive enhancement — the backend could run on quantum computers in lunar PSRs:
- Naturally isolated (384,400 km from Earth)
- Naturally cold (40K ambient)
- Quantum-secured communication
- Far-side radio silence

The latency (~2.5 seconds round-trip) limits real-time applications, but for asynchronous processing of complex neural data, it could be the most secure architecture imaginable.

· · ·

## Conclusion: The Wavefunction Hasn't Collapsed Yet

I started this piece with a seductive hypothesis: could VPNs tunnel data like particles phase through walls?

The honest answer is no — not with physics as we understand it. The scales don't match. The coherence requirements are incompatible with macroscopic data transport. The mathematics of tunneling probability make it vanishingly unlikely at network-relevant dimensions.

**But here's what I learned from John Martinis' work:**

*The boundaries of the quantum world are further out than we assumed.*

In 1984, no one expected quantum effects to manifest in systems you could hold. Martinis, Clarke, and Devoret proved otherwise. Today, we're building quantum computers with thousands of qubits, distributing quantum keys via satellite, and racing to make our classical infrastructure quantum-resistant.

The tunnel between quantum and classical isn't a wall. It's a gradient. And we're learning to operate across it.

· · ·

## What's Next: Questions Worth Pursuing

If you're a **physicist**: Tell me where the `f x S ~ k` framework breaks down. What am I missing about quantum coherence at macroscopic scales?

If you're a **cryptographer**: How do we bridge the gap between QKD's physics-based security and the practical needs of global networks? What are the attack vectors on quantum repeater chains?

If you're a **security engineer**: How would you attack a QKD-secured neural interface? What side channels exist in quantum systems?

If you're a **neuroscientist**: Does the liminal phase concept map to anything in neural signal propagation? Is there a biological analog to tunneling traversal time?

If you're at **NASA or a space agency**: How realistic is lunar PSR quantum computing? What infrastructure bottlenecks am I underestimating?

If you're a **student** just starting out: Which of these questions excites you most? That's probably where you should dig deeper.

Neil was right: the challenge is knowing enough to think you're right, but not enough to know you're wrong.

The wavefunction hasn't collapsed yet. Let's see where the probabilities cluster.

· · ·

*This article is part of a series on the ONI (Organic Neural Firewall) Framework.*

**Related articles:**
- [The OSI of Mind: Securing Human-AI Interfaces](https://medium.com/@qikevinl/the-osi-of-mind-securing-human-ai-interfaces-3ca381b95c29)
- [Your Brain Has a Spam Filter](https://medium.com/@qikevinl/your-brain-has-a-spam-filter-can-we-reverse-engineer-it-799da714238e)
- [Your Brain Needs a Firewall](https://medium.com/@qikevinl/your-brain-needs-a-firewall-heres-what-it-would-look-like-87b46d292219)
- [Neural Ransomware Isn't Science Fiction](https://medium.com/@qikevinl/neural-ransomware-isnt-science-fiction-e3f9efe4ffb1)
- [Can Hackers Attack Quantum Computers Across Time and Space?](https://medium.com/@qikevinl/quantum-hacking)

· · ·

## Sources

**Quantum Tunneling & Physics:**
- [StarTalk: Macroscopic Quantum Tunneling with John Martinis](https://startalkmedia.com/show/macroscopic-quantum-tunneling-with-john-martinis)
- [Britannica: John M. Martinis](https://www.britannica.com/biography/John-M-Martinis)
- [Nature: Groundbreaking quantum-tunnelling experiments win physics Nobel](https://www.nature.com/articles/d41586-025-03194-2)
- [Physics LibreTexts: Quantum Tunneling](https://phys.libretexts.org/Bookshelves/University_Physics/University_Physics_(OpenStax)/University_Physics_III_-_Optics_and_Modern_Physics_(OpenStax)/07:_Quantum_Mechanics/7.07:_Quantum_Tunneling_of_Particles_through_Potential_Barriers)
- [ScienceDaily: Quantum tunneling mystery solved (POSTECH)](https://www.sciencedaily.com/releases/2025/07/250727235835.htm)
- [Quantum Zeitgeist: What Is A Josephson Junction?](https://quantumzeitgeist.com/what-is-a-josephson-junction/)

**QKD Protocols:**
- [Wikipedia: BB84 Protocol](https://en.wikipedia.org/wiki/BB84)
- [Medium: QKD Explained - BB84, B92, E91](https://medium.com/sss-quantum/quantum-key-distribution-explained-bb84-b92-e91-protocols-38209d0a7dc0)
- [Springer: Hybrid BB84-E91 QKD Protocol](https://link.springer.com/article/10.1007/s10791-025-09807-8)
- [Wiley: Hybrid QKD Framework 2025](https://onlinelibrary.wiley.com/doi/10.1002/cpe.70221)

**QSDC:**
- [Nature: Implementation of Practical QSDC](https://www.nature.com/articles/s41377-019-0132-3)
- [Nature: 15-User QSDC Network](https://www.nature.com/articles/s41377-021-00634-2)
- [Science.org: Free-Space QSDC](https://spj.science.org/doi/10.34133/adi.0004)

**Post-Quantum Cryptography:**
- [Wikipedia: Lattice-Based Cryptography](https://en.wikipedia.org/wiki/Lattice-based_cryptography)
- [Wikipedia: Kyber](https://en.wikipedia.org/wiki/Kyber)
- [IACR: Basic Lattice Cryptography Tutorial](https://eprint.iacr.org/2024/1287)
- [Medium: CRYSTALS-Kyber Explained](https://medium.com/identity-beyond-borders/crystals-kyber-the-key-to-post-quantum-encryption-3154b305e7bd)
- [Google Cloud: Quantum-Safe Digital Signatures](https://cloud.google.com/blog/products/identity-security/announcing-quantum-safe-digital-signatures-in-cloud-kms)
- [Post Quantum: Digital Signatures](https://postquantum.com/post-quantum/post-quantum-digital-signatures/)

**QRNG:**
- [ID Quantique: QRNG Overview](https://www.idquantique.com/random-number-generation/overview/)
- [Palo Alto Networks: What Is QRNG?](https://www.paloaltonetworks.com/cyberpedia/what-is-a-quantum-random-number-generator-qrng)
- [Quside: QRNG Explained](https://quside.com/quantum-random-number-generators-why-how-where/)

**No-Cloning Theorem:**
- [Wikipedia: No-Cloning Theorem](https://en.wikipedia.org/wiki/No-cloning_theorem)
- [Quera: What Is No-Cloning Theorem](https://www.quera.com/glossary/no-cloning-theorem)
- [The Quantum Space: No Clones Allowed](https://thequantumspace.org/2025/09/23/no-clones-allowed/)

**Bell States & Entanglement:**
- [Wikipedia: Bell State](https://en.wikipedia.org/wiki/Bell_state)
- [Post Quantum: Bell States for Cybersecurity](https://postquantum.com/quantum-computing/bell-states-cybersecurity/)
- [Aliro Quantum: What Are Bell States?](https://www.aliroquantum.com/blog/what-are-bell-states)

**Quantum Homomorphic Encryption:**
- [Nature: Experimental Quantum Homomorphic Encryption](https://www.nature.com/articles/s41534-020-00340-8)
- [Nature: Quantum Search on Encrypted Data](https://www.nature.com/articles/s41598-020-61791-9)
- [PMC: Flexible Threshold QHE](https://pmc.ncbi.nlm.nih.gov/articles/PMC11764212/)

**Lunar Quantum Computing:**
- [Wikipedia: Permanently Shadowed Craters](https://en.wikipedia.org/wiki/Permanently_shadowed_crater)
- [The Quantum Insider: Interlune Lunar Helium-3](https://thequantuminsider.com/2025/01/26/quantum-apollo-interlune-plans-to-mine-the-moon-to-power-cryogenic-technology/)
- [QuantumGenie: Why the Moon Matters](https://quantumgenie.ai/insights/why-the-moon-matters-for-quantum-computing-from-helium-3-to-off-planet-quantum-networks)

**Quantum Internet & Repeaters:**
- [Deutsche Telekom: Quantum Internet Breakthrough](https://www.telekom.com/en/media/media-information/archive/breakthrough-for-the-quantum-internet-1090094)
- [Nature: Hybrid Quantum Repeaters](https://www.nature.com/articles/s41534-025-01119-5)
- [UChicago: 200x Longer Quantum Connections](https://news.uchicago.edu/story/breakthrough-could-connect-quantum-computers-200-times-longer-distance)
- [ScienceDaily: Earth-to-Space Quantum Link](https://www.sciencedaily.com/releases/2025/12/251217082515.htm)

**BCI & Quantum Integration:**
- [Scientific Reports: Universal Quantum Terminal](https://www.nature.com/articles/s41598-024-65899-0)
- [IBM: AI, Quantum, and Neurotechnologies](https://newsroom.ibm.com/2025-06-03-ibm-and-inclusive-brains-bring-together-ai,-quantum-and-neurotechnologies-to-improve-the-understanding-of-brain-machine-interfaces)
- [PMC: Quantum Biology](https://pmc.ncbi.nlm.nih.gov/articles/PMC6283985/)
- [PMC: Quantum Microtubules](https://pmc.ncbi.nlm.nih.gov/articles/PMC12060853/)

**VPN Developments:**
- [TechRadar: NordVPN Post-Quantum 2026](https://www.techradar.com/vpn/vpn-privacy-security/post-quantum-encryption-is-not-the-end-nordvpn-aims-for-world-first-security-milestones-in-2026)
- [The Quantum Insider: 2026 Predictions](https://thequantuminsider.com/2025/12/30/tqis-expert-predictions-on-quantum-technology-in-2026/)

· · ·

**Sub-Tags:** #QuantumComputing #Cybersecurity #VPN #Neuroscience #BrainComputerInterface #QKD #QSDC #PostQuantumCryptography #ONI #LunarComputing #QuantumInternet #Neuralink #Encryption #NoCloning #BellStates #Lattice #QRNG
