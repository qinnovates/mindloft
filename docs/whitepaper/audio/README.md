# Whitepaper AI Voiceover Audio Files

This directory holds audio files for the interactive whitepaper's AI voiceover feature. When a visitor enables the voiceover toggle, audio narration plays section-by-section as they scroll through the whitepaper.

## How It Works

The whitepaper JS contains an `AUDIO_MANIFEST` mapping each section ID to an audio file path. Dropping MP3 files here with the correct filenames makes them work automatically — no code changes needed.

If a file is missing, the voiceover bar shows "audio coming soon" with no error.

## File Naming Convention

| File | Section | Whitepaper Section ID |
|------|---------|----------------------|
| `01-introduction.mp3` | 1. Introduction | `intro` |
| `02-why-standard.mp3` | 2. Why BCIs Need a Standard | `why-standard` |
| `03-cost-of-inaction.mp3` | 3. The Cost of Inaction | `cost-of-inaction` |
| `04-14-layer-model.mp3` | 4. The 14-Layer Model | `14-layer-model` |
| `05-design-principles.mp3` | 5. Design Principles | `design-principles` |
| `06-coherence-metric.mp3` | 6. The Coherence Metric | `coherence-metric` |
| `07-scale-frequency.mp3` | 7. Scale-Frequency Invariant | `scale-frequency` |
| `08-unified-metric.mp3` | 8. Unified Metric | `unified-metric` |
| `09-neural-firewall.mp3` | 9. The Neural Firewall | `neural-firewall` |
| `10-tara.mp3` | 10. TARA | `tara` |
| `11-regulatory.mp3` | 11. Regulatory Alignment | `regulatory` |
| `12-quantum.mp3` | 12. Quantum-Ready Security | `quantum` |
| `13-conclusion.mp3` | 13. Conclusion | `conclusion` |

## Audio Generation

**Recommended approach:** Use an AI text-to-speech service to generate narration from each section's content.

**Services:**
- ElevenLabs (high quality, natural voice)
- OpenAI TTS API (`tts-1-hd` model)
- Google Cloud Text-to-Speech

**Specifications:**
- Format: MP3
- Bitrate: 128kbps
- Channels: Mono
- Each file should narrate the full text content of its corresponding section
- Keep individual files under 5 MB (~5 minutes at 128kbps mono)

## Workflow

1. Copy the text content of a whitepaper section
2. Generate audio via your preferred TTS service
3. Save as the corresponding filename (e.g., `01-introduction.mp3`)
4. Drop into this directory
5. Push to GitHub — the voiceover toggle will pick it up automatically
