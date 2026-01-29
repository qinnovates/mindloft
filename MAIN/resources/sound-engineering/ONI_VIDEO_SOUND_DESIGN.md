# ONI Demo Video Sound Design Documentation

**Created:** 2026-01-29
**Project:** ONI Framework Demo Video
**Tool:** ElevenLabs Sound Generation API
**Purpose:** Document the audio design philosophy, frequencies, and psychological principles used in the ONI demo video.

---

## Overview

The ONI demo video employs a carefully layered audio design that builds anticipation, elicits curiosity, and creates emotional resonance with the viewer. The sound design follows principles from music theory, game audio engineering, and cognitive psychology.

---

## Audio Timeline

| Time | Frames | Sound Layer | Purpose |
|------|--------|-------------|---------|
| 0:00-7:00 | 0-210 | Ambient + Original Pulse | Establish atmosphere, trigger curiosity |
| 5:00-14:07 | 150-422 | Smooth Pulse (crossfade) | Build anticipation, maintain engagement |
| 14:07-15:67 | 422-470 | Boot Chime (fade in) | Signal transition, elicit excitement |
| 15:67+ | 470+ | Narration begins | Content delivery |
| Credits | 5850+ | Wind/Door Morning | Hopeful closure, new beginnings |

---

## Sound Assets

### 1. Ambient Tech Atmosphere
**File:** `ambient-tech.mp3`
**Duration:** 22 seconds
**Volume:** 35%, fades out over 3 seconds

**Prompt Used:**
```
soft ambient electronic pad with gentle pulse, futuristic technology atmosphere,
calm and soothing with subtle excitement, like the hum of advanced neural
technology awakening, mysterious yet hopeful
```

**Frequency Characteristics:**
- Low-mid frequency pad (100-400Hz base)
- Subtle high-frequency shimmer (2-6kHz)
- Slow LFO modulation creating gentle movement

**Psychological Effect:**
- Creates sense of space and immersion
- Low frequencies trigger feeling of presence and safety
- Subtle movement maintains subconscious attention without demanding focus

---

### 2. Original Pulse (Deep Curiosity Trigger)
**File:** `original-pulse.mp3`
**Duration:** 8 seconds
**Volume:** 70%, crossfades out at 5-7 seconds

**Prompt Used:**
```
deep low frequency sine wave pulse around 80Hz, slow rhythmic throb like a
heartbeat at 60 BPM, mysterious suspended chord drone, zelda-like wonder tone
with perfect fifth harmony, soft bass hum that builds curiosity and anticipation,
clean and pure like portal game sounds, meditative and hypnotic, subtle rising pitch
```

**Frequency Characteristics:**
- **Base frequency:** ~80Hz (sub-bass, felt more than heard)
- **Rhythm:** 60 BPM (matches resting heart rate)
- **Harmony:** Perfect 5th intervals (3:2 ratio)
- **Texture:** Clean sine wave, minimal harmonics

**Music Theory Principles:**
| Element | Interval/Value | Effect |
|---------|----------------|--------|
| Perfect 5th | 3:2 ratio | Most consonant interval, creates "openness" and wonder |
| 60 BPM | 1Hz pulse | Synchronizes with parasympathetic nervous system |
| 80Hz base | Sub-bass | Triggers primal attention, felt in chest |
| Suspended chord | No resolution | Creates anticipation, brain seeks closure |

**Psychological Effect:**
- **Curiosity activation:** Suspended harmony creates unresolved tension that the brain wants to resolve
- **Calm focus:** 60 BPM matches resting heart rate, inducing calm without sedation
- **Wonder response:** Perfect 5ths are used extensively in Nintendo/Zelda for discovery moments
- **Presence:** 80Hz felt physically, creates sense of "something is here"

---

### 3. Smooth Pulse (Sustained Anticipation)
**File:** `curiosity-pulse.mp3`
**Duration:** 12 seconds
**Volume:** 80%, crossfades in at 5 seconds, fades out at 14 seconds

**Prompt Used:**
```
soft low frequency pulsing drone, gentle rhythmic throb like a calm heartbeat,
smooth warm bass hum at 60 BPM, ambient pad with subtle pulse, soothing and
hypnotic, rounded sine wave texture, peaceful yet anticipatory, velvet smooth
electronic pulse, meditation music with gentle rhythm
```

**Frequency Characteristics:**
- Warmer, rounder tone than original pulse
- Less harmonic content (purer sine wave)
- Maintains 60 BPM rhythm
- Smoother attack/release envelope

**Psychological Effect:**
- Continues the curiosity state without fatigue
- Smoother texture prevents listener exhaustion
- Maintains engagement through sustained tension
- Prepares listener for the "payoff" (boot chime)

---

### 4. Boot Chime (Transition Signal)
**File:** `boot-chime.mp3`
**Duration:** 3 seconds
**Volume:** 60%, fades in over 1.5 seconds

**Prompt Used:**
```
soft pleasant digital chime, gentle OS boot up sound, cheerful ascending tones
like a friendly computer awakening, bright and optimistic, clean modern beep
sequence, inspiring and warm, not retro but refined digital
```

**Frequency Characteristics:**
- Mid-high frequencies (400Hz-2kHz)
- Ascending pitch pattern
- Clean digital timbre
- Quick attack, medium decay

**Music Theory Principles:**
- **Ascending melody:** Rising pitch = anticipation resolved, "arrival"
- **Major tonality:** Bright, positive, welcoming
- **Clean timbre:** Modern, technological, trustworthy

**Psychological Effect:**
- **Resolution:** Releases tension built by pulses
- **Excitement:** Ascending tones trigger dopamine response
- **Trust:** Clean digital sounds signal competence and modernity
- **Transition marker:** Clear signal that "something is beginning"

---

### 5. Wind Door Morning (Closing)
**File:** `wind-door-morning.mp3`
**Duration:** 8 seconds
**Volume:** 50%

**Prompt Used:**
```
gentle wind blowing through an open door into a bright sunlit room, peaceful
morning breeze with soft chimes, hopeful and serene, new beginnings, fresh
air and warmth
```

**Frequency Characteristics:**
- Broadband noise (wind): 200Hz-8kHz
- Sparse high-frequency chimes: 1-4kHz
- Natural, organic texture

**Psychological Effect:**
- **Openness:** Wind through door = threshold, opportunity
- **Hope:** Morning associations = new day, fresh start
- **Calm resolution:** Peaceful ending, no tension
- **Call to action reinforcement:** "The door is open, come in"

---

## Sound Psychology Principles Applied

### 1. Frequency-Emotion Mapping

| Frequency Range | Feeling | Application in Video |
|-----------------|---------|---------------------|
| 20-80Hz (Sub-bass) | Power, presence, visceral | Original pulse base |
| 80-250Hz (Bass) | Warmth, foundation | Both pulses |
| 250-500Hz (Low-mid) | Body, fullness | Ambient pad |
| 500Hz-2kHz (Mid) | Clarity, voice range | Boot chime |
| 2-6kHz (Presence) | Excitement, attention | Chime harmonics |
| 6-20kHz (Air) | Sparkle, space | Wind, ambient shimmer |

### 2. Rhythm & Heart Rate Synchronization

**60 BPM = 1 beat per second = resting heart rate**

Research shows that rhythms near resting heart rate:
- Activate parasympathetic nervous system
- Reduce cortisol (stress hormone)
- Increase openness to new information
- Create sense of safety and trust

This is why meditation music, ASMR, and "focus" playlists often use 60 BPM.

### 3. Harmonic Intervals & Emotion

| Interval | Ratio | Feeling | Used For |
|----------|-------|---------|----------|
| Unison | 1:1 | Unity, power | Not used (too static) |
| Perfect 5th | 3:2 | Wonder, openness | Pulse harmony |
| Perfect 4th | 4:3 | Stability, question | Implicit in suspended chords |
| Major 3rd | 5:4 | Happiness, brightness | Boot chime |
| Minor 2nd | 16:15 | Tension, mystery | Avoided (too dissonant) |

### 4. Game Audio Principles (Nintendo/Zelda/Portal)

**Discoveries & Wonder:**
- Use perfect 5ths and octaves
- Ascending melodies for positive discovery
- Clean, pure tones (sine waves, bells)

**Anticipation:**
- Suspended chords (no resolution)
- Subtle rhythmic pulse
- Gradual pitch rise

**Trust & Safety:**
- Warm low frequencies
- Smooth envelopes (no harsh attacks)
- Consonant harmony

---

## Implementation in Remotion

```tsx
// Ambient - fades out over 3 seconds before boot chime
<Audio
  src={staticFile("audio/ambient-tech.mp3")}
  volume={(f) => interpolate(f, [0, problem.start - 70, problem.start + 20], [0.35, 0.35, 0])}
/>

// Original pulse - deeper, fades out as smooth takes over
<Audio
  src={staticFile("audio/original-pulse.mp3")}
  volume={(f) => interpolate(f, [0, 30, 150, 210], [0, 0.7, 0.7, 0])}
/>

// Smooth pulse - crossfades in, continues to boot chime
<Audio
  src={staticFile("audio/curiosity-pulse.mp3")}
  volume={(f) => interpolate(f, [0, 60, duration - 20, duration], [0, 0.8, 0.8, 0])}
/>

// Boot chime - fades in gradually
<Audio
  src={staticFile("audio/boot-chime.mp3")}
  volume={(f) => interpolate(f, [0, 45], [0, 0.6])}
/>

// Closing wind - plays during credits
<Audio src={staticFile("audio/wind-door-morning.mp3")} volume={0.5} />
```

---

## Crossfade Technique

The transition from Original Pulse to Smooth Pulse uses a crossfade:

```
Frames 150-210 (5-7 seconds):
  - Original Pulse: 70% → 0%
  - Smooth Pulse: 0% → 80%
```

This creates seamless continuity while the character of the sound subtly shifts from "deep and mysterious" to "smooth and anticipatory."

---

## ElevenLabs API Reference

**Endpoint:** `https://api.elevenlabs.io/v1/sound-generation`

**Parameters:**
```json
{
  "text": "Description of desired sound",
  "duration_seconds": 3-22,
  "prompt_influence": 0.3-0.7
}
```

**Prompt Influence:**
- `0.3` = More creative interpretation
- `0.5` = Balanced
- `0.7` = Closer to literal prompt

---

## File Locations

| File | Location |
|------|----------|
| `ambient-tech.mp3` | `video/demo/public/audio/` |
| `original-pulse.mp3` | `video/demo/public/audio/` |
| `curiosity-pulse.mp3` | `video/demo/public/audio/` |
| `boot-chime.mp3` | `video/demo/public/audio/` |
| `wind-door-morning.mp3` | `video/demo/public/audio/` |
| This documentation | `MAIN/resources/sound-engineering/` |

---

## References

1. **Music Theory & Emotion:**
   - Huron, D. (2006). *Sweet Anticipation: Music and the Psychology of Expectation*
   - Juslin, P. N., & Sloboda, J. A. (2010). *Handbook of Music and Emotion*

2. **Game Audio Design:**
   - Collins, K. (2008). *Game Sound: An Introduction to the History, Theory, and Practice of Video Game Music and Sound Design*
   - Nintendo Sound Team principles (Zelda, Mario sound design philosophy)

3. **Psychoacoustics:**
   - Moore, B. C. J. (2012). *An Introduction to the Psychology of Hearing*
   - Heart rate synchronization research (Thaut, M. H., 2005)

4. **Frequency-Emotion Mapping:**
   - Hevner, K. (1936). Experimental studies of the elements of expression in music
   - Gabrielsson, A., & Lindström, E. (2010). The role of structure in the musical expression of emotions

---

*Tags: #sound-design #audio #psychology #music-theory #elevenlabs #remotion #oni-video*
