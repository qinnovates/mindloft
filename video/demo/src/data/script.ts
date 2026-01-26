/**
 * ONI Framework Demo Video Script
 * ~400 words, 3:30 runtime
 *
 * For ElevenLabs generation, use voice: "Adam" (authoritative) or "Rachel" (professional)
 * Request word-level timestamps for precise sync
 */

export interface ScriptLine {
  text: string;
  startFrame: number;
  endFrame: number;
  scene: string;
}

export const script: ScriptLine[] = [
  // Scene 0: Cold Open (0:00-0:08)
  {
    scene: 'coldOpen',
    text: "Brain-computer interfaces are no longer science fiction.",
    startFrame: 0,
    endFrame: 120,
  },
  {
    scene: 'coldOpen',
    text: "They're in operating rooms. They're in research labs. They're coming to consumers.",
    startFrame: 120,
    endFrame: 240,
  },

  // Scene 1: Title (0:08-0:15)
  {
    scene: 'title',
    text: "But who's protecting the most sensitive data in existence?",
    startFrame: 240,
    endFrame: 360,
  },
  {
    scene: 'title',
    text: "Your thoughts.",
    startFrame: 360,
    endFrame: 450,
  },

  // Scene 2: Problem (0:15-0:40)
  {
    scene: 'problem',
    text: "Today's brain-computer interfaces lack standardized security frameworks.",
    startFrame: 450,
    endFrame: 570,
  },
  {
    scene: 'problem',
    text: "There's no OSI model for neural interfaces.",
    startFrame: 570,
    endFrame: 690,
  },
  {
    scene: 'problem',
    text: "No common language between neuroscientists, engineers, and security researchers.",
    startFrame: 690,
    endFrame: 870,
  },
  {
    scene: 'problem',
    text: "Until now.",
    startFrame: 870,
    endFrame: 960,
  },
  {
    scene: 'problem',
    text: "Introducing ONI—the Open Neurosecurity Interoperability.",
    startFrame: 960,
    endFrame: 1200,
  },

  // Scene 3: 14-Layer Model (0:40-1:20)
  {
    scene: 'layers',
    text: "ONI defines fourteen layers spanning silicon to synapse.",
    startFrame: 1200,
    endFrame: 1350,
  },
  {
    scene: 'layers',
    text: "Layers one through seven mirror the classical OSI model—physical signals, protocols, transport, and application interfaces.",
    startFrame: 1350,
    endFrame: 1650,
  },
  {
    scene: 'layers',
    text: "But here's where ONI goes further.",
    startFrame: 1650,
    endFrame: 1770,
  },
  {
    scene: 'layers',
    text: "Layer eight is the Neural Gateway—the critical bridge where silicon meets synapse.",
    startFrame: 1770,
    endFrame: 2010,
  },
  {
    scene: 'layers',
    text: "This is where traditional security ends and neurosecurity begins.",
    startFrame: 2010,
    endFrame: 2190,
  },
  {
    scene: 'layers',
    text: "Layers nine through fourteen map the biological stack—from ion channels to spike trains, neural populations, circuit dynamics, cognitive function, and ultimately, identity.",
    startFrame: 2190,
    endFrame: 2400,
  },

  // Scene 4: Coherence Metric (1:20-2:00)
  {
    scene: 'coherence',
    text: "But how do you measure neural security?",
    startFrame: 2400,
    endFrame: 2520,
  },
  {
    scene: 'coherence',
    text: "ONI introduces the Coherence Score—a unified metric combining phase variance, timing precision, and frequency stability.",
    startFrame: 2520,
    endFrame: 2760,
  },
  {
    scene: 'coherence',
    text: "When coherence drops below threshold, automated defense mechanisms activate.",
    startFrame: 2760,
    endFrame: 2940,
  },
  {
    scene: 'coherence',
    text: "Whether it's MRI interference, electromagnetic disruption, or a malicious injection attack—the system responds instantly.",
    startFrame: 2940,
    endFrame: 3180,
  },
  {
    scene: 'coherence',
    text: "And the Scale-Frequency Invariant ensures neural patterns maintain constant relationships across all scales.",
    startFrame: 3180,
    endFrame: 3420,
  },
  {
    scene: 'coherence',
    text: "As scale increases, frequency decreases proportionally. The product remains invariant—a fingerprint of healthy neural activity.",
    startFrame: 3420,
    endFrame: 3660,
  },

  // Scene 5: TARA Platform (2:00-2:30)
  {
    scene: 'tara',
    text: "For security professionals, there's TARA—the Telemetry Analysis and Response Automation platform.",
    startFrame: 3660,
    endFrame: 3900,
  },
  {
    scene: 'tara',
    text: "Real-time brain topology visualization.",
    startFrame: 3900,
    endFrame: 4050,
  },
  {
    scene: 'tara',
    text: "Attack simulation across all fourteen layers.",
    startFrame: 4050,
    endFrame: 4230,
  },
  {
    scene: 'tara',
    text: "Neural Signal Assurance Monitoring that flags anomalies before they become breaches.",
    startFrame: 4230,
    endFrame: 4500,
  },

  // Scene 6: Academic Foundation (2:30-2:55)
  {
    scene: 'academic',
    text: "ONI isn't built in a vacuum.",
    startFrame: 4500,
    endFrame: 4620,
  },
  {
    scene: 'academic',
    text: "It extends the threat models of Kohno and colleagues at the University of Washington.",
    startFrame: 4620,
    endFrame: 4860,
  },
  {
    scene: 'academic',
    text: "It incorporates neurosecurity research from Columbia, Yale, and the Graz BCI Lab.",
    startFrame: 4860,
    endFrame: 5130,
  },
  {
    scene: 'academic',
    text: "Every claim is cited. Every formula is documented.",
    startFrame: 5130,
    endFrame: 5280,
  },
  {
    scene: 'academic',
    text: "Built for researchers, developers, regulators, security teams...",
    startFrame: 5280,
    endFrame: 5460,
  },
  {
    scene: 'academic',
    // NOTE: This line should have slow pan-in animation with white text for emphasis
    text: "...and you.",
    startFrame: 5460,
    endFrame: 5700, // Extended for dramatic effect
  },

  // Scene 7: Call to Action (2:55-3:15)
  {
    scene: 'cta',
    text: "Ready to secure the neural frontier?",
    startFrame: 5700,
    endFrame: 5850,
  },
  {
    scene: 'cta',
    text: "Install ONI with a single command.",
    startFrame: 5850,
    endFrame: 6000,
  },
  {
    scene: 'cta',
    text: "pip install oni-framework",
    startFrame: 6000,
    endFrame: 6150,
  },
  {
    scene: 'cta',
    text: "Join us in building the security standards for brain-computer interfaces.",
    startFrame: 6150,
    endFrame: 6360,
  },

  // Scene 8: Credits (3:15-3:35) - Powerful closing
  {
    scene: 'credits',
    text: "Our mind.",
    startFrame: 6360,
    endFrame: 6450,
  },
  {
    scene: 'credits',
    text: "Our future.",
    startFrame: 6450,
    endFrame: 6540,
  },
  {
    scene: 'credits',
    text: "Our rules.",
    startFrame: 6540,
    endFrame: 6630,
  },
  {
    scene: 'credits',
    text: "Because the most important connections deserve the most thought.",
    startFrame: 6630,
    endFrame: 6810,
  },
  {
    scene: 'credits',
    text: "Welcome to the OSI of Mind.",
    startFrame: 6810,
    endFrame: 6990,
  },
];

// Full script as single text for voiceover generation
export const fullScript = script.map(line => line.text).join(' ');

// Word count: ~420 words
// Estimated read time at 110 WPM: ~3:50 (fits 3:53 with natural pacing)
// Final frame: 6990 = 3:53 at 30fps
//
// ANIMATION NOTES:
// - Scene 4 (Coherence): Show threshold trigger → defense mechanism activation
//   - Visual: Gauge drops below threshold → shield/alert animation
//   - Examples: MRI interference, electromagnetic disruption, injection attacks
// - Scene 4 (Scale-Frequency): Animated visualization of f × S ≈ k
//   - Scale bar grows (10→1000), Frequency shrinks (100→1 Hz), k stays ~1000
// - Scene 6 ("...and you"): SLOW PAN-IN with WHITE TEXT for emphasis
// - TARA scene: REMOVED "100% open source" line
