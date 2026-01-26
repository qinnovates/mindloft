/**
 * Title Scene - Apple-quality production
 * Smooth, elegant, minimal
 */

import React from 'react';
import { AbsoluteFill, useCurrentFrame, useVideoConfig, spring, interpolate, Easing } from 'remotion';
import { WaveGrid } from '../components/reactbits';

export const TitleScene: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Apple-style ease - smooth and deliberate
  const appleEase = (t: number) => {
    // Cubic bezier approximation of Apple's signature ease
    return t < 0.5
      ? 4 * t * t * t
      : 1 - Math.pow(-2 * t + 2, 3) / 2;
  };

  // Slow, elegant fade in for waves
  const waveOpacity = interpolate(frame, [0, 60], [0, 0.6], {
    extrapolateRight: 'clamp',
  });

  // Subtle wave glow - gentle pulse
  const waveGlow = interpolate(
    Math.sin(frame * 0.02),
    [-1, 1],
    [6, 10]
  );

  // ONI reveal - slow and majestic
  const oniRevealRaw = interpolate(frame, [30, 90], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  const oniReveal = appleEase(oniRevealRaw);

  // Individual letter staggers - very subtle
  const letterDelays = [0, 8, 16];
  const letterConfigs = ['O', 'N', 'I'].map((letter, i) => {
    const letterRaw = interpolate(frame - 35 - letterDelays[i], [0, 50], [0, 1], {
      extrapolateLeft: 'clamp',
      extrapolateRight: 'clamp',
    });
    return {
      letter,
      progress: appleEase(letterRaw),
    };
  });

  // Tagline - fades in after ONI settles
  const taglineRaw = interpolate(frame, [100, 140], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  const taglineProgress = appleEase(taglineRaw);

  // Subtitle
  const subtitleRaw = interpolate(frame, [130, 170], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  const subtitleProgress = appleEase(subtitleRaw);

  // Very subtle glow breathing
  const glowBreath = interpolate(
    Math.sin(frame * 0.025),
    [-1, 1],
    [0.85, 1]
  );

  return (
    <AbsoluteFill
      style={{
        background: '#000000',
      }}
    >
      {/* Subtle radial gradient behind */}
      <div
        style={{
          position: 'absolute',
          inset: 0,
          background: `radial-gradient(ellipse 80% 70% at 50% 50%,
            rgba(0, 40, 60, 0.4) 0%,
            rgba(0, 20, 35, 0.2) 40%,
            transparent 70%
          )`,
          opacity: waveOpacity,
        }}
      />

      {/* Clean wave background - subtle and elegant */}
      <div style={{ opacity: waveOpacity }}>
        <WaveGrid
          lineCount={8}
          color="#0088b0"
          secondaryColor="#006080"
          amplitude={25}
          speed={0.08}
          strokeWidth={1}
          showNodes={false}
          glow={true}
          glowIntensity={waveGlow}
        />
      </div>

      {/* Content */}
      <div
        style={{
          position: 'absolute',
          inset: 0,
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          justifyContent: 'center',
          gap: 40,
        }}
      >
        {/* ONI Letters with orbiting electron */}
        <div
          style={{
            position: 'relative',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
          }}
        >
          {letterConfigs.map(({ letter, progress }, i) => {
            const y = interpolate(progress, [0, 1], [40, 0]);
            const opacity = progress;
            const scale = interpolate(progress, [0, 1], [0.95, 1]);

            return (
              <div
                key={i}
                style={{
                  position: 'relative',
                  fontSize: 200,
                  fontWeight: 700,
                  fontFamily: "-apple-system, 'SF Pro Display', 'Helvetica Neue', sans-serif",
                  letterSpacing: '0.02em',
                  color: '#ffffff',
                  transform: `translateY(${y}px) scale(${scale})`,
                  opacity,
                  textShadow: `0 0 ${40 * glowBreath}px rgba(0, 160, 220, 0.4)`,
                }}
              >
                {letter}
              </div>
            );
          })}

          {/* Electron orbiting horizontally around ONI, passing through O */}
          {letterConfigs[0].progress > 0.9 && (() => {
            const electronOpacity = interpolate(letterConfigs[0].progress, [0.9, 1], [0, 1]);

            // Horizontal orbit around all letters
            const orbitSpeed = 0.06;
            const t = frame * orbitSpeed;

            // Path: wide horizontal ellipse, but dips into the O center
            // ONI is about 500px wide, O is at left
            const pathWidth = 320; // Half-width of orbit
            const pathHeight = 30; // Slight vertical movement

            // Custom path that goes through the O
            // When electron is on the left side (near O), it curves inward
            const rawX = Math.cos(t) * pathWidth;
            const baseY = Math.sin(t) * pathHeight;

            // Dip into the O when passing through left side
            const inOZone = rawX < -150; // Near the O
            const dipAmount = inOZone ? Math.sin((rawX + 150) / 80 * Math.PI) * 50 : 0;
            const electronY = baseY + (Math.sin(t) > 0 ? dipAmount : -dipAmount);

            // Offset to center the orbit on the full ONI text
            const electronX = rawX + 50;

            // Trail
            const trailCount = 10;
            const trails = Array.from({ length: trailCount }, (_, i) => {
              const trailT = t - (i + 1) * 0.12;
              const trailRawX = Math.cos(trailT) * pathWidth;
              const trailBaseY = Math.sin(trailT) * pathHeight;
              const trailInOZone = trailRawX < -150;
              const trailDip = trailInOZone ? Math.sin((trailRawX + 150) / 80 * Math.PI) * 50 : 0;
              return {
                x: trailRawX + 50,
                y: trailBaseY + (Math.sin(trailT) > 0 ? trailDip : -trailDip),
                opacity: (trailCount - i) / trailCount * 0.5,
                size: 8 - i * 0.6,
              };
            });

            return (
              <div
                style={{
                  position: 'absolute',
                  top: '50%',
                  left: '50%',
                  width: 0,
                  height: 0,
                  opacity: electronOpacity,
                }}
              >
                {/* Trail particles */}
                {trails.map((trail, idx) => (
                  <div
                    key={idx}
                    style={{
                      position: 'absolute',
                      width: trail.size,
                      height: trail.size,
                      borderRadius: '50%',
                      background: '#40d8ff',
                      opacity: trail.opacity,
                      transform: `translate(calc(-50% + ${trail.x}px), calc(-50% + ${trail.y}px))`,
                      filter: `blur(${idx * 0.3}px)`,
                    }}
                  />
                ))}

                {/* Main electron */}
                <div
                  style={{
                    position: 'absolute',
                    width: 14,
                    height: 14,
                    borderRadius: '50%',
                    background: '#40d8ff',
                    transform: `translate(calc(-50% + ${electronX}px), calc(-50% + ${electronY}px))`,
                    boxShadow: `
                      0 0 8px #40d8ff,
                      0 0 16px #40d8ff,
                      0 0 24px rgba(64, 216, 255, 0.7)
                    `,
                  }}
                />
              </div>
            );
          })()}
        </div>

        {/* Tagline */}
        <div
          style={{
            fontSize: 22,
            fontWeight: 300,
            letterSpacing: '0.25em',
            textTransform: 'uppercase',
            fontFamily: "-apple-system, 'SF Pro Display', 'Helvetica Neue', sans-serif",
            opacity: taglineProgress,
            transform: `translateY(${interpolate(taglineProgress, [0, 1], [15, 0])}px)`,
            color: '#ffffff',
          }}
        >
          OPEN <span style={{ fontWeight: 700 }}>NEURO</span>SECURITY INTEROPERABILITY
        </div>
      </div>
    </AbsoluteFill>
  );
};
