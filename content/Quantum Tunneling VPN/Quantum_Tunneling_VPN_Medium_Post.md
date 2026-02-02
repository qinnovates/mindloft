---
title: "What If VPNs Could Tunnel Like Particles Through Walls?"
subtitle: "Why a Nobel Prize-winning discovery made me rethink everything about network security — and where I might be wrong"
date: 2026-01-21
author: Kevin L. Qi
tags: ["#QuantumComputing", "#Cybersecurity", "#VPN", "#Neuroscience", "#ONI", "#QKD"]
---

# What If VPNs Could Tunnel Like Particles Through Walls?

### Why a Nobel Prize-winning discovery made me rethink everything about network security — and where I might be wrong

**_A deep dive into the intersection of quantum physics and network security — and an honest exploration of what we don't know yet._**

*Picture this* — You're listening to a podcast about quantum mechanics when a physicist casually mentions that particles can pass through solid barriers they shouldn't have the energy to cross. Not metaphorically. *Physically.*

Then he says something that makes you pause: this effect doesn't just happen at the subatomic level. It happens in systems large enough to hold in your hand.

Your mind starts racing. VPNs use "tunnels." They move data through hostile networks. What if the tunnel wasn't just a metaphor? What if data could quantum tunnel through barriers — bypassing interception not through encryption, but through the fundamental physics of reality itself?

This isn't science fiction. This is the question that seized me while listening to Neil deGrasse Tyson interview **John Martinis** — the physicist who just won the **2025 Nobel Prize** for proving that quantum tunneling works at macroscopic scales.

And I need to find out if I'm right — or completely wrong.

· · ·

### Why I'm Writing This: Knowing What We Don't Know

Neil deGrasse Tyson once said in his MasterClass:

> *"One of the greatest challenges in life is knowing enough to think you're right, but not enough to know you're wrong."*

That quote is why this article exists.

Listening to Neil interview John Martinis on StarTalk, I found myself connecting dots between quantum tunneling and network security — between **Josephson junctions** and VPN protocols — between macroscopic quantum effects and the neural security frameworks I've been developing.

The connections felt compelling. Maybe too compelling.

I've spent considerable time developing the **ONI (Organic Neural Interface) framework** for neural security — exploring coherence breaches, the Scale-Frequency Invariant, and threats to brain-computer interfaces. I know *enough* about quantum mechanics to see tantalizing connections. But do I know enough to know where I'm wrong?

This piece is my attempt to find out.

· · ·

### The Problem: Two Tunnels, Same Word

Here's the thing — we use "tunneling" in two completely different contexts:

**Quantum tunneling:** A particle passes through an energy barrier it doesn't have the energy to overcome. It shouldn't happen according to classical physics. But quantum mechanics says: probability distributions extend through barriers. Sometimes the particle appears on the other side.

**VPN tunneling:** Encrypted data packets travel through hostile public networks, protected by mathematics. The "tunnel" is a metaphor. Your packets don't phase through routers — they travel the same paths as everyone else's, just encrypted.

Same word. Completely different physics.

But what if they didn't have to be?

· · ·

### The Insight: Martinis Proved Quantum Effects Scale Up

For decades, physicists assumed quantum tunneling only happened at subatomic scales — electrons, photons, individual particles.

**John Martinis proved them wrong.**

Working with John Clarke and Michel Devoret at UC Berkeley in 1984-1985, Martinis demonstrated something astonishing: quantum tunneling can happen in systems **large enough to hold in your hand**.

Using **Josephson junctions** — two superconducting metals separated by a thin insulator, cooled to 15 millikelvin — they showed that billions of electrons, behaving as **Cooper pairs**, could tunnel coherently through barriers as a single quantum entity.

The Royal Swedish Academy called it "the first clear demonstration of macroscopic quantum tunnelling."

Here's what caught my attention in the StarTalk episode. Tyson asked Martinis: *"Does tunneling happen instantly?"*

The answer is no. **Tunneling takes time.**

Researchers at the University of Toronto measured 0.61 milliseconds for atoms tunneling through a 1.3-micrometre barrier. July 2025 research from POSTECH revealed that electrons actually *collide with atomic nuclei inside the tunnel* — it's not a clean pass-through.

There's a traversal. There's a duration. There's something happening *inside* the barrier.

In my ONI framework, we call this the **liminal phase** — the state between states.

· · ·

### The Solution: Where Physics Actually Meets Network Security

Let me be specific about where quantum mechanics *actually* impacts network security. It's not through quantum tunneling VPNs. It's through something more practical.

**1. Quantum Key Distribution (QKD): The Observer Effect as Security**

In quantum mechanics, observation changes the system. This isn't philosophy — it's physics.

QKD exploits this directly. When you distribute encryption keys using quantum states (typically photon polarization), any eavesdropper who tries to intercept the key **disturbs the quantum state**. The disturbance is detectable. The key is discarded. The attacker gains nothing.

This is the **Coherence Breach** weaponized for defense.

In my ONI framework's Scale-Frequency Invariant:

> **`f × S ≈ k`**

When an attacker probes the system (increasing frequency f), the spatial coherence (S) must collapse to maintain the constant k. In QKD, this collapse is *the security mechanism*. The attacker's observation is self-defeating.

**2. Post-Quantum VPNs: Racing the Clock**

From my previous article on Quantum Hacking, you know about **HNDL — Harvest Now, Decrypt Later**. Nation-states are already stockpiling encrypted traffic, waiting for quantum computers to break RSA and ECC.

The VPN industry is responding:

```
┌─────────────┬───────────────────────────────────────────────────────────────┐
│ Provider    │ 2025-2026 Development                                         │
├─────────────┼───────────────────────────────────────────────────────────────┤
│ NordVPN     │ Post-quantum encryption across all apps (May 2025);           │
│             │ PQ authentication planned H1 2026                             │
├─────────────┼───────────────────────────────────────────────────────────────┤
│ ExpressVPN  │ Quantum-resistant feature expansion                           │
├─────────────┼───────────────────────────────────────────────────────────────┤
│ Proton VPN  │ Quantum-proof architecture roadmap                            │
└─────────────┴───────────────────────────────────────────────────────────────┘
```

These aren't quantum tunneling VPNs. They're classical VPNs with quantum-resistant cryptography. The tunnel is still mathematical — but the math is evolving to survive the quantum threat.

**3. Space-Based QKD: The Infrastructure of Tomorrow**

Nokia, Honeywell, and Colt are launching the first commercial **space-based QKD trials in 2026-2027**. The European Space Agency's Eagle-1 satellite launches in 2026 for EuroQCI.

Why space? QKD over fiber has distance limits (~100km without repeaters). Satellites can distribute quantum keys globally.

· · ·

### The Technical Reality: Why True Quantum Tunneling VPNs Don't Work (Yet)

Here's where I have to be honest about the physics.

Quantum tunneling operates at:
- Subatomic to nanometer scales
- Cryogenic temperatures (millikelvin)
- Isolated, coherent systems

Network data involves:
- Macroscopic information in electrical/optical signals
- Room temperature
- Massive decoherence from environmental interaction

The **transmission coefficient** for quantum tunneling:

> **`T ≈ e^(-2κL)`**

Where `κ` (kappa) depends on barrier height and particle energy, and L is barrier width. Tunneling probability drops *exponentially* with barrier thickness. At network-relevant scales, T approaches zero.

Even if you could encode network data in quantum states and tunnel them, you'd face the **no-cloning theorem**. You cannot copy an arbitrary quantum state. Great for QKD security — problematic for networking, where we need to route, replicate, and process data.

**Verdict:** True quantum tunneling VPNs — where data phases through barriers via quantum mechanical tunneling — remain theoretical speculation. The physics doesn't scale.

**But here's the twist:** We don't need quantum tunneling for data if we can use it for keys.

QKD gives us the security benefits of quantum mechanics without requiring data itself to tunnel. The keys traverse the quantum realm; the data travels classically, protected by those keys.

· · ·

### Why This Matters: The `f × S ≈ k` Framework Applied

Let me connect this to my Scale-Frequency Invariant in a way that illuminates both domains.

**In Quantum Computing:**
When an attacker probes a quantum computer (increasing f), coherence (S) collapses. The computation fails. This is a denial-of-service attack written into physics.

**In Quantum Networking:**
QKD systems maintain coherence across the key distribution channel. If an attacker increases their interaction frequency, the spatial coherence of the quantum key collapses. But unlike quantum computing — where collapse is catastrophic — in QKD, collapse is *the alarm*.

**The Unifying Insight:**
Both quantum computing and quantum networking are governed by the same coherence constraints. The difference is whether collapse is a vulnerability (computing) or a feature (key distribution).

This is why hybrid approaches make sense: quantum for key generation/distribution (where the observer effect is an asset), classical for data transport (where we need robustness, not fragility).

· · ·

### The Catch: What I Don't Know

This framework isn't bulletproof. There are gaps I can't fill yet.

**Does `f × S ≈ k` hold at network scales?** I've derived it from neural signaling principles and quantum coherence theory. But it needs experimental validation across domains.

**Can the liminal phase be exploited?** If tunneling isn't instantaneous, what happens inside the barrier? Is there a security-relevant phenomenon we're missing?

**Where does macroscopic end?** Martinis proved quantum effects at scales we can hold. But where's the boundary? And can we push it further?

I'm publishing anyway because we need shared vocabulary. We need researchers across physics, neuroscience, and security talking to each other. And we need to be honest about what we don't know.

· · ·

### Part of Something Larger: ONI and Neural Security

This research has crystallized several directions for future iterations of the ONI framework:

**1. The Blood-Brain Barrier as Quantum Barrier?**

The blood-brain barrier is a physical barrier protecting neural tissue. Could quantum tunneling principles inform how we think about neural interface security — signals crossing barriers they "shouldn't" be able to cross?

Speculative. But the traversal time research suggests barriers aren't binary. There's a liminal phase. And in neural security, understanding what happens *inside* that liminal phase may be critical.

**2. QKD for Neural Interfaces**

If brain-computer interfaces become widespread, securing the communication channel becomes paramount. QKD principles — where eavesdropping is physically detectable — could provide a security layer no classical encryption can match.

Imagine a neural interface where any attempt to intercept the signal between brain and device collapses the quantum key, alerting the user to tampering. The Coherence Breach as a defense mechanism.

**3. `f × S ≈ k` at Biological Scales**

Does the Scale-Frequency Invariant hold for biological neural systems? If so, what are the constants? How does coherence manifest in neural signaling, and what does it mean to "breach" it?

These are open questions. Questions I know enough to ask — but not enough to answer.

Yet.

· · ·

### What's Next

If you're a **physicist**: Tell me where the `f × S ≈ k` framework breaks down. What am I missing about quantum coherence at macroscopic scales?

If you're a **security engineer**: How would you attack a QKD-secured neural interface? What are the side channels I haven't considered?

If you're a **neuroscientist**: Does the liminal phase concept map to anything you see in neural signal propagation? Is there a biological analog to tunneling traversal time?

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

### Sources

- [StarTalk: Macroscopic Quantum Tunneling with John Martinis](https://startalkmedia.com/show/macroscopic-quantum-tunneling-with-john-martinis)
- [Britannica: John M. Martinis](https://www.britannica.com/biography/John-M-Martinis)
- [Nature: Groundbreaking quantum-tunnelling experiments win physics Nobel](https://www.nature.com/articles/d41586-025-03194-2)
- [ScienceDaily: Quantum tunneling mystery solved (POSTECH)](https://www.sciencedaily.com/releases/2025/07/250727235835.htm)
- [Phys.org: Ultra-fast quantum tunneling device for 6G](https://phys.org/news/2026-01-ultra-fast-quantum-tunneling-device.html)
- [TechRadar: NordVPN post-quantum milestones 2026](https://www.techradar.com/vpn/vpn-privacy-security/post-quantum-encryption-is-not-the-end-nordvpn-aims-for-world-first-security-milestones-in-2026)
- [The Quantum Insider: Predictions for 2026](https://thequantuminsider.com/2025/12/30/tqis-expert-predictions-on-quantum-technology-in-2026/)
- [Qolab: John Martinis](https://qolab.ai/our_team/john-martinis/)
- [Springer: Tunneling Traversal Time](https://link.springer.com/article/10.1007/s13194-022-00483-9)
- [Quantum Zeitgeist: What Is A Josephson Junction?](https://quantumzeitgeist.com/what-is-a-josephson-junction/)

· · ·

### Acknowledgements

Writing and structural assistance was provided by Claude Code (Anthropic). All ideas, analyses, and conclusions are the author's own.

**AI Tools Citation (APA 7th Edition):**
- Anthropic. (2026). Claude Code (Version 4.5) [Large language model]. https://www.anthropic.com/claude

· · ·

**Sub-Tags:** #QuantumComputing #Cybersecurity #VPN #Neuroscience #BrainComputerInterface #QKD #PostQuantumCryptography #ONI
