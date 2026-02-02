# Email Draft: Tyler Schroder, Yale Digital Ethics Center

> **To:** tyler.schroder@yale.edu
> **Subject:** Building on Your BCI Cybersecurity Framework — ONI: A Technical Implementation for Neurosecurity
> **Status:** DRAFT — Review before sending

---

Dear Tyler,

I hope this message finds you well. My name is Kevin Qi — I'm a researcher working at the intersection of cybersecurity, neuroscience, and AI ethics. I came across your paper "Cyber Risks to Next-Gen Brain-Computer Interfaces: Analysis and Recommendations" and wanted to reach out because our work is deeply complementary. I'm applying to Yale this month with a focus on furthering BCI neurosecurity research, and I'd welcome your perspective on how to advance this critical area.

## Your Paper's Impact on My Work

Your CVSS-based threat model and the HALO Device Survey (Table 1) crystallized something I've been working on independently: we share the same foundational concern that BCI security cannot be an afterthought. Your finding that seven of the leading BCI products lack encryption — devices that interface directly with the brain — is a stark illustration of the gap between what exists and what's needed. Your five recommendation areas (software updates, authentication/authorization, attack surface minimization, encryption, and adversarial AI defense) map almost exactly to the security layers I've been developing in a framework called ONI (Open Neural Interface).

## The ONI Framework: Implementing Your Recommendations

Where your paper identifies the problems and recommends policy directions, ONI attempts to provide executable technical specifications. We build on the same foundational work — particularly Denning, Matsuoka, & Kohno (2009), which your paper also cites — and extend it into a layered architecture:

**14-Layer Security Model.** ONI extends the OSI network model (Layers 1–7, Silicon) through a critical Layer 8 "Neural Gateway" bridge into biological layers (9–14), culminating in an Identity Layer. This gives manufacturers and regulators a concrete reference architecture to implement your recommendations across every attack surface — from physical carrier to cognitive semantics.

**Coherence Metric (Cs).** Your paper recommends "Cognitive Status monitoring technology — stop decision-making if adversarial input is detected" (Section 6.5). ONI implements this as a quantitative metric:

    Cs = e^(−(σ²φ + σ²τ + σ²γ))

Where σ²φ, σ²τ, and σ²γ represent phase, transport, and gain variance respectively. When Cs drops below 0.5, the Neural Firewall blocks the signal. Below 0.1, emergency shutoff is triggered. This transforms your policy recommendation into a measurable, enforceable standard — what you call "cognitive status" becomes a real-time computable value.

**Neural Firewall at Layer 8.** This directly addresses your authentication/authorization and attack surface recommendations. Operating on a zero-trust model at the hardware boundary between silicon and biology, it enforces amplitude bounds (max 500 μV read, 5 mA stimulation), rate limiting (DoS detection at 10,000 signals/100ms), and integrity checks on every signal crossing the bio-silicon boundary.

**BCI Anonymizer.** Your paper identifies encryption as critical but notes most BCIs lack it due to power constraints. ONI's BCI Anonymizer takes a complementary approach: rather than encrypting everything (which your paper correctly notes exhausts power budgets), it classifies neural data by sensitivity using Event-Related Potentials. Motor commands (LRP, CNV) are marked PUBLIC and transmitted freely. But P300 attention signals, N170 face recognition patterns, and N400 semantic processing are classified as SENSITIVE or PRIVATE and filtered before transmission. This addresses the privacy concern at its source — data that never leaves the brain can't be intercepted.

**Kohno Threat Taxonomy Integration.** Both our work traces back to Kohno's three threat categories — Alteration, Blocking, Eavesdropping — mapped to the CIA triad. ONI operationalizes each: Alteration → Coherence Metric + amplitude bounds at L8; Blocking → rate limiting + DoS detection; Eavesdropping → BCI Anonymizer + Privacy Score at L13-L14.

## Beyond Implants: The Non-Invasive Frontier

I also wanted to share something I encountered while researching the current BCI market that raises its own set of ethical questions. Apple has filed a patent (US20230225659A1) for biosignal sensing in AirPods — up to 17 EEG/ECG/EMG electrodes in a concentric ring array on the ear tip. This is significant because it signals that consumer-grade neural sensing is approaching commercial reality, not in a decade, but potentially within 2–4 years.

However, there's a fundamental architectural limitation: the electrodes face into the ear canal while the temporal lobe — the auditory cortex, hippocampus, and the thinnest part of the skull (2–4mm) — sits perpendicular to that measurement axis. This limits spatial resolution for meaningful brain state detection.

This is where I believe the next evolution lies: bone conduction transducers positioned at the temporal lobe, combined with glasses for visual rendering. This approach offers direct proximity to the auditory cortex, avoids ear canal obstruction (a personal concern — I have hearing damage that makes in-ear devices problematic), and provides a larger surface area for electrode arrays that could enable actual spatial mapping rather than single-axis measurement.

The ethical implications are substantial. A non-invasive, consumer-grade device that can detect brain states, adapt AI learning in real-time to individual neural patterns, and deliver audio through bone conduction and visual information through glasses — this isn't a distant hypothetical. The component technologies exist today. The question is whether our security and ethics frameworks will be ready when they converge.

## A Question I'd Value Your Perspective On

Your paper focuses on implantable BCIs regulated as Class III devices. But consider this: when Apple ships AirPods with EEG electrodes, they won't be Class III — they'll likely be consumer electronics or, at most, Class II wellness devices. The same BCI-unique risks you identify in Table 2 — incorrect vision processing, incorrect speech synthesis, unwanted brain stimulation — could emerge in consumer devices operating under far less regulatory scrutiny.

**Here's the question that keeps me up at night:** If an adaptive AI learning system is continuously personalizing its model to a user's neural patterns — optimizing what content to show, how to present information, even adjusting audio delivery based on detected attention states — at what point does "personalization" become a form of cognitive manipulation? And if that system is compromised by an adversary (your network attack vector), the attacker wouldn't just steal data — they would have the ability to subtly reshape how a person thinks and learns, without the person ever being aware of it. Your paper addresses "adversarial stimuli" for implanted BCIs, but the same vulnerability class applies to any system that closes the loop between neural sensing and content delivery.

This isn't theoretical. The technologies for each component exist now. The convergence is what creates the novel ethical territory.

## How I'd Like to Further This Research

I'm applying to Yale this month and would deeply appreciate your advice on how to position my work to contribute to BCI neurosecurity research at the Digital Ethics Center. Specifically:

1. **Where do you see the most urgent gaps** between your paper's policy recommendations and the technical implementations needed to enforce them?
2. **How should frameworks like ONI engage with regulatory bodies** (FDA, EU MDR) to translate technical specifications into enforceable standards?
3. **Does the Digital Ethics Center have ongoing work** on non-invasive BCI ethics that I might contribute to?

The ONI Framework is open-source and published on GitHub. I'd welcome the opportunity to discuss how our work might intersect, whether through collaboration, feedback on the framework's approach, or simply continuing this conversation.

Thank you for your time and for the important work you and your colleagues are doing at the intersection of cybersecurity and neuroethics. Your paper was the clearest articulation I've found of the problems — I'm trying to build the solutions.

Best regards,

Kevin Qi
ONI Framework — github.com/qikevinl/oni
