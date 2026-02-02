# My Mom's Heart Attack Went Undetected for 20 Days. I'm Building a Device So This Never Happens Again.

*A personal story, a broken system, and a vision for the future of cardiac diagnostics*

---

## The Call That Changed Everything

I was traveling abroad when I got the message that no one wants to receive: my mom was in the hospital.

For twenty days, she had been suffering. Twenty days of what she described as severe indigestion and cramping—a feeling she said came from her stomach. She went to doctors. They ran tests. They sent her home. They told her it was probably acid reflux, maybe stress.

Twenty days.

When I finally returned and took her to the emergency room myself, they ran an EKG. It came back normal. They ran an ECG. Normal. The machines that we trust to catch heart attacks—the same technology that has been the gold standard for decades—saw nothing wrong.

What saved my mother's life was a doctor who finally said, "Let's run a blood test."

That test was called a **high-sensitivity troponin assay**. It measures cardiac troponin—a protein that only exists in heart muscle cells. When those cells die, they release troponin into the bloodstream. My mother's blood was full of it.

She had been having a heart attack for twenty days. Not the dramatic, chest-clutching kind you see in movies. A silent one. An **NSTEMI**—a Non-ST-Elevation Myocardial Infarction—the type that doesn't show up on a standard EKG because it doesn't produce the classic electrical signature doctors are trained to look for.

Her heart had been failing, and no one knew.

---

## This Happens More Often Than You Think

After my mother's diagnosis, I started researching. What I found was disturbing.

**Women are 50% more likely to be misdiagnosed during a heart attack than men.** For NSTEMI specifically, women have a 41% greater chance of receiving the wrong initial diagnosis ([European Society of Cardiology](https://www.escardio.org/The-ESC/Press-Office/Press-releases/Heart-attack-diagnosis-missed-in-women-more-often-than-in-men)).

Why? Because medical education has historically centered on male patterns of presentation. The "classic" heart attack—crushing chest pain radiating down the left arm—is a male symptom. Women are more likely to experience:

- Shortness of breath
- Nausea
- Back pain
- Fatigue
- And yes—**indigestion and stomach cramping**

My mother's symptoms weren't unusual. They were *typical*—for a woman. But the diagnostic tools weren't designed with her in mind.

In a [study from the Global Registry of Acute Coronary Events](https://www.emdocs.net/missed-myocardial-infarction-in-the-emergency-department/), 8.4% of heart attack patients had no chest pain at all. For patients over 85, **over 40% with NSTEMI have non-diagnostic ECGs**. The machines we rely on are missing critical cases.

And when diagnoses are missed, people die. Patients with atypical presentations have a mortality rate of **13%**, compared to just 4% for those with typical symptoms.

---

## The 200-Year-Old Technology Still in Every Hospital

Let me tell you about the stethoscope.

In 1816, a French physician named **René Laennec** was examining a young woman with symptoms of heart disease. He was uncomfortable placing his ear directly on her chest—the standard practice at the time. So he rolled up some sheets of paper into a tube, placed one end on her chest and the other to his ear.

He was astonished. The sounds were clearer than he had ever heard.

Over the next three years, Laennec perfected his invention, eventually carving a wooden tube that became the first stethoscope. He named it from the Greek words *stethos* (chest) and *skopos* (examination).

That was **over 200 years ago**.

And here's the problem: hearing is subjective. What one doctor hears as a murmur, another might miss entirely. The interpretation depends on the observer's training, experience, hearing acuity, and even the ambient noise in the room.

By definition, this introduces *variability*. In science, variability is the enemy of accuracy. When the same patient can receive different interpretations from different doctors using the same tool, we have a problem.

Modern ECG machines improved upon this—they produce objective electrical tracings. But they introduced their own problems: intimidating electrodes, clinical environments that trigger anxiety, and fundamental limitations in what they can detect.

---

## The Irony of Cardiac Monitoring

Here's something most people don't realize: the very act of monitoring your heart can affect your heart.

It's called **white coat hypertension**—the phenomenon where blood pressure and heart rate increase simply because you're in a clinical setting. Research shows that anywhere from [20-50% of patients](https://www.henryford.com/blog/2021/12/white-coat-syndrome) experience elevated readings due to anxiety, not underlying disease.

Studies have found that even the anticipation of having blood pressure measured—just seeing the cuff—[triggers a physiological stress response](https://www.ahajournals.org/doi/10.1161/01.HYP.31.4.1021). The fight-or-flight response kicks in, heart rate increases, and suddenly the measurement is contaminated by the measurement process itself.

Now imagine you're already anxious about your health. You've been experiencing strange symptoms. You go to the hospital. A technician attaches 10 electrodes to your chest with wires running to a large machine. Leads are clipped. Cables are arranged. You're told to lie still and breathe normally.

Breathe normally? You're terrified.

For patients already experiencing cardiac symptoms, this environment can exacerbate their condition. The very tools designed to diagnose them can make accurate diagnosis harder.

---

## What I'm Building

I'm not a doctor. I'm an engineer. But after watching my mother suffer through a system that failed her—test after test, doctor after doctor, twenty days of a heart attack that no machine could see—I decided to do something about it.

I'm building a device I call **CardioLens** (working name: Cardiac-NSIM).

The concept: a single, handheld, **non-intimidating** device that combines four diagnostic modalities:

1. **ECG/EKG functionality** — electrical activity monitoring
2. **Localized NMR imaging** — the same magnetic resonance technology as MRI, but miniaturized
3. **Optical sensing (PPG)** — photoplethysmography like Apple Watch heart monitoring, capturing blood oxygen and pulse waveforms
4. **Acoustic sensing** — a high-sensitivity digital microphone that replaces the stethoscope, capturing heart sounds with machine precision instead of human hearing

The key innovations:

**Conformal design**: The device curves to match the anatomy of the chest, sitting between the ribs to minimize air gaps and maximize signal quality. Every millimeter closer to the heart increases signal-to-noise ratio exponentially.

**Unidirectional field**: Using a Halbach array configuration, the magnetic field is focused *into* the chest toward the heart, not radiating outward. This means lower power, deeper penetration, and safer operation.

**Integrated dry electrodes**: No cold gel, no intimidating wires. Gold-polymer contact points are built into the device perimeter, capturing ECG signals while the device simply rests on the chest.

**Bio-adhesive fixation**: Early designs considered magnetic back-plates, but rigorous analysis revealed this could interfere with pacemakers and ICDs. Instead, we use a gentle adhesive polymer—similar to a TENS unit—that holds the device in place without any risk to patients with implants.

---

## The Science Behind the Vision

This isn't science fiction. Every component exists today:

- **Low-field portable MRI** is already commercialized by companies like Hyperfine
- **Flexible PCBs** can print RF coils on polyimide substrates that conform to body contours
- **Dry electrodes** with gold coating capture ECG without conductive gel
- **PPG sensors** like those in Apple Watch and pulse oximeters are mature, miniaturized technology
- **MEMS microphones** with medical-grade sensitivity can digitize heart sounds—murmurs, valve clicks, abnormal rhythms—with far more consistency than human ears
- **Signal processing** using frequency-domain orthogonality can separate the microvolt ECG signals from megahertz MRI pulses, while ML algorithms fuse all four data streams into unified diagnostics

The mathematical foundation:

The magnetic field strength on the axis of a coil follows:

$$B(z) = \frac{\mu_0 I R^2}{2(R^2 + z^2)^{3/2}}$$

For a 50mm diameter coil, we can maintain sufficient field strength to image 30-40mm deep—directly into the left ventricle.

By oscillating current at specific Larmor frequencies (42.5 MHz per Tesla for hydrogen protons), we can achieve localized tissue characterization without the massive superconducting magnets of hospital MRI machines.

---

## The Path Forward

I believe we're at an inflection point in medical technology.

MRI machines revolutionized diagnostics but remained locked in hospital basements due to size and cost. Wearables brought monitoring to our wrists but sacrificed depth for convenience. ECGs have been the cardiac standard for decades but miss the very conditions that kill women at disproportionate rates.

The trajectory is clear:
- **1816**: Laennec invents the stethoscope—subjective listening
- **1901**: Einthoven develops the electrocardiogram—objective electrical measurement
- **1977**: First MRI images of living humans—deep tissue visualization
- **2024**: Portable MRI enters clinical use—accessibility begins
- **Next**: **Unified, handheld, multi-modal cardiac imaging**—democratized diagnostics

My vision is a device that:
- A concerned daughter could use to check on her mother
- A rural clinic could employ without million-dollar equipment
- A patient could use at home without fear or intimidation
- A doctor could trust for both screening *and* diagnosis

---

## I Need Help

This is my side project. I'm building it because I have to—because I can't stop thinking about those twenty days my mother suffered while technology failed her.

But I can't do it alone.

I'm looking for:
- **Cardiologists** who understand the clinical gaps
- **Biomedical engineers** with RF coil experience
- **Signal processing experts** for multi-modal data fusion
- **FDA regulatory specialists** for the approval pathway
- **Anyone** who has lost someone to a missed diagnosis and wants to help ensure it doesn't happen again

If this resonates with you—if you've experienced the fear of unexplained symptoms, the frustration of being dismissed, or the grief of a delayed diagnosis—I want to hear from you.

The goal isn't to replace doctors. It's to give them better tools. To give *patients* better tools. To make the invisible visible before it's too late.

---

## A Note to My Mom

You're okay now. You survived. But so many others don't.

This is for them. And this is for you.

---

*This article represents ongoing research and development. Technical concepts were developed with ideation assistance from OpenAI GPT, Google Gemini, and DeepSeek. Research compilation, refinement, and publication supported by Claude Code (Anthropic). All errors are my own; all hope is shared.*

---

**If you're interested in following this project or contributing, connect with me on [LinkedIn/Twitter/GitHub]. If you or a loved one has experienced a missed cardiac diagnosis, your story could help shape this technology. Reach out.**

*Tags: #MedTech #CardiacHealth #WomenHealth #MedicalDevices #Innovation #NSTEMI #HeartAttack*
