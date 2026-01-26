/**
 * Credits Scene - Powerful closing with manifesto
 * Features: Dramatic text reveals, cinematic pacing, circular wave finale
 */

import React from 'react';
import { AbsoluteFill, useCurrentFrame, spring, useVideoConfig, interpolate } from 'remotion';
import { FloatingParticles } from '../components/Particles';
import { colors } from '../data/oni-theme';

// Complex geometric wave animation for the finale - intertwining vectors
const GeometricWaveEffect: React.FC<{ intensity: number }> = ({ intensity }) => {
  const frame = useCurrentFrame();

  // Generate flowing wave paths
  const generateWavePath = (
    yOffset: number,
    amplitude: number,
    frequency: number,
    phase: number,
    points: number = 100
  ) => {
    const pathPoints: string[] = [];
    for (let i = 0; i <= points; i++) {
      const x = (i / points) * 1920;
      const wave1 = Math.sin((x * frequency) / 100 + phase) * amplitude;
      const wave2 = Math.sin((x * frequency * 1.5) / 100 + phase * 0.7) * (amplitude * 0.5);
      const wave3 = Math.cos((x * frequency * 0.5) / 100 + phase * 1.3) * (amplitude * 0.3);
      const y = yOffset + wave1 + wave2 + wave3;
      pathPoints.push(`${i === 0 ? 'M' : 'L'} ${x} ${y}`);
    }
    return pathPoints.join(' ');
  };

  // Wave configurations - multiple intertwining layers
  const waves = [
    { y: 540, amp: 80, freq: 2, speed: 0.03, color: '#3b82f6', width: 3 },
    { y: 540, amp: 100, freq: 1.5, speed: 0.025, color: '#8b5cf6', width: 2.5 },
    { y: 540, amp: 60, freq: 2.5, speed: 0.035, color: '#06b6d4', width: 2 },
    { y: 540, amp: 120, freq: 1, speed: 0.02, color: '#a855f7', width: 2 },
    { y: 540, amp: 40, freq: 3, speed: 0.04, color: '#3b82f6', width: 1.5 },
    { y: 540, amp: 90, freq: 1.8, speed: 0.028, color: '#06b6d4', width: 1.5 },
  ];

  // Geometric shapes that orbit and rotate
  const numShapes = 12;
  const shapes = Array.from({ length: numShapes }, (_, i) => {
    const angle = (i / numShapes) * Math.PI * 2 + frame * 0.01;
    const radius = 300 + Math.sin(frame * 0.02 + i) * 50;
    const x = 960 + Math.cos(angle) * radius;
    const y = 540 + Math.sin(angle) * radius * 0.6;
    const rotation = frame * (0.5 + i * 0.1);
    const size = 20 + Math.sin(frame * 0.03 + i * 0.5) * 10;
    return { x, y, rotation, size, index: i };
  });

  return (
    <svg
      style={{
        position: 'absolute',
        width: '100%',
        height: '100%',
        pointerEvents: 'none',
      }}
      viewBox="0 0 1920 1080"
    >
      <defs>
        <filter id="geoBlur">
          <feGaussianBlur stdDeviation="1.5" />
        </filter>
        <filter id="geoGlow">
          <feGaussianBlur stdDeviation="4" result="blur" />
          <feMerge>
            <feMergeNode in="blur" />
            <feMergeNode in="SourceGraphic" />
          </feMerge>
        </filter>
        <linearGradient id="waveGrad1" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%" stopColor="#3b82f6" stopOpacity="0" />
          <stop offset="20%" stopColor="#3b82f6" stopOpacity="0.8" />
          <stop offset="80%" stopColor="#8b5cf6" stopOpacity="0.8" />
          <stop offset="100%" stopColor="#8b5cf6" stopOpacity="0" />
        </linearGradient>
        <linearGradient id="waveGrad2" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%" stopColor="#06b6d4" stopOpacity="0" />
          <stop offset="30%" stopColor="#06b6d4" stopOpacity="0.6" />
          <stop offset="70%" stopColor="#a855f7" stopOpacity="0.6" />
          <stop offset="100%" stopColor="#a855f7" stopOpacity="0" />
        </linearGradient>
      </defs>

      {/* Flowing wave lines */}
      {waves.map((wave, i) => (
        <path
          key={`wave-${i}`}
          d={generateWavePath(wave.y, wave.amp, wave.freq, frame * wave.speed + i * 0.5)}
          fill="none"
          stroke={wave.color}
          strokeWidth={wave.width}
          opacity={0.4 * intensity}
          filter="url(#geoGlow)"
        />
      ))}

      {/* Orbiting geometric shapes */}
      {shapes.map((shape) => (
        <g
          key={`shape-${shape.index}`}
          transform={`translate(${shape.x}, ${shape.y}) rotate(${shape.rotation})`}
        >
          {/* Alternating between different geometric shapes */}
          {shape.index % 3 === 0 ? (
            // Triangle
            <polygon
              points={`0,${-shape.size} ${shape.size * 0.866},${shape.size * 0.5} ${-shape.size * 0.866},${shape.size * 0.5}`}
              fill="none"
              stroke={shape.index % 2 === 0 ? '#3b82f6' : '#8b5cf6'}
              strokeWidth={1.5}
              opacity={0.5 * intensity}
            />
          ) : shape.index % 3 === 1 ? (
            // Square/Diamond
            <rect
              x={-shape.size / 2}
              y={-shape.size / 2}
              width={shape.size}
              height={shape.size}
              fill="none"
              stroke={shape.index % 2 === 0 ? '#06b6d4' : '#a855f7'}
              strokeWidth={1.5}
              opacity={0.4 * intensity}
            />
          ) : (
            // Hexagon
            <polygon
              points={Array.from({ length: 6 }, (_, j) => {
                const a = (j / 6) * Math.PI * 2 - Math.PI / 2;
                return `${Math.cos(a) * shape.size},${Math.sin(a) * shape.size}`;
              }).join(' ')}
              fill="none"
              stroke={shape.index % 2 === 0 ? '#3b82f6' : '#06b6d4'}
              strokeWidth={1.5}
              opacity={0.45 * intensity}
            />
          )}
        </g>
      ))}

      {/* Central connecting lines that pulse */}
      {Array.from({ length: 6 }, (_, i) => {
        const angle1 = (i / 6) * Math.PI * 2 + frame * 0.008;
        const angle2 = ((i + 3) / 6) * Math.PI * 2 + frame * 0.008;
        const r1 = 200 + Math.sin(frame * 0.025 + i) * 30;
        const r2 = 200 + Math.sin(frame * 0.025 + i + Math.PI) * 30;
        return (
          <line
            key={`line-${i}`}
            x1={960 + Math.cos(angle1) * r1}
            y1={540 + Math.sin(angle1) * r1 * 0.6}
            x2={960 + Math.cos(angle2) * r2}
            y2={540 + Math.sin(angle2) * r2 * 0.6}
            stroke={i % 2 === 0 ? '#3b82f6' : '#8b5cf6'}
            strokeWidth={1}
            opacity={0.25 * intensity}
            filter="url(#geoBlur)"
          />
        );
      })}
    </svg>
  );
};

export const CreditsScene: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Phase timing for the manifesto
  const showMind = frame >= 0;
  const showFuture = frame >= 90;
  const showRules = frame >= 180;
  const showBecause = frame >= 270;
  const showWelcome = frame >= 420;

  // Glow pulse
  const glowPulse = interpolate(
    Math.sin(frame * 0.04),
    [-1, 1],
    [0.5, 1]
  );

  // Manifesto phrases
  const manifestoPhrases = [
    { text: 'Your Mind.', delay: 0, show: showMind },
    { text: 'Your Privacy.', delay: 90, show: showFuture },
    { text: 'Our Future.', delay: 180, show: showRules },
  ];

  return (
    <AbsoluteFill
      style={{
        background: colors.gradients.background,
      }}
    >
      {/* Ambient particles */}
      <FloatingParticles
        count={40}
        color={colors.primary.accentPurple}
        speed={0.08}
        minSize={1}
        maxSize={3}
      />

      {/* Background glow */}
      <div
        style={{
          position: 'absolute',
          top: '50%',
          left: '50%',
          width: 800,
          height: 600,
          transform: 'translate(-50%, -50%)',
          background: `radial-gradient(ellipse, ${colors.primary.accentPurple}15 0%, transparent 60%)`,
          filter: 'blur(60px)',
          opacity: glowPulse,
        }}
      />

      {/* Main content */}
      <div
        style={{
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          justifyContent: 'center',
          height: '100%',
          gap: 0,
        }}
      >
        {/* Manifesto: Our mind. Our future. Our rules. */}
        <div
          style={{
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            gap: 20,
            marginBottom: 60,
          }}
        >
          {manifestoPhrases.map((phrase, i) => {
            const phraseProgress = spring({
              frame: frame - phrase.delay,
              fps,
              config: { damping: 25, stiffness: 60 },
            });

            const y = interpolate(Math.max(0, phraseProgress), [0, 1], [50, 0]);
            const opacity = Math.max(0, phraseProgress);
            const blur = interpolate(Math.max(0, phraseProgress), [0, 1], [15, 0]);

            // Fade out when next section appears
            const fadeOut = showBecause
              ? interpolate(frame - 270, [0, 60], [1, 0], { extrapolateRight: 'clamp' })
              : 1;

            if (!phrase.show) return null;

            return (
              <div
                key={phrase.text}
                style={{
                  fontSize: 72,
                  fontWeight: 700,
                  letterSpacing: '-0.02em',
                  background: `linear-gradient(180deg, #ffffff 0%, ${colors.primary.accent} 100%)`,
                  WebkitBackgroundClip: 'text',
                  WebkitTextFillColor: 'transparent',
                  transform: `translateY(${y}px)`,
                  opacity: opacity * fadeOut,
                  filter: `blur(${blur}px)`,
                  textAlign: 'center',
                }}
              >
                {phrase.text}
              </div>
            );
          })}
        </div>

        {/* "Because the most important connections..." */}
        {showBecause && !showWelcome && (
          <div
            style={{
              position: 'absolute',
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
              gap: 20,
            }}
          >
            {(() => {
              const becauseProgress = spring({
                frame: frame - 270,
                fps,
                config: { damping: 30, stiffness: 50 },
              });

              const fadeOut = showWelcome
                ? interpolate(frame - 420, [0, 40], [1, 0], { extrapolateRight: 'clamp' })
                : 1;

              return (
                <div
                  style={{
                    fontSize: 36,
                    fontWeight: 400,
                    color: colors.text.secondary,
                    textAlign: 'center',
                    maxWidth: 900,
                    lineHeight: 1.5,
                    opacity: Math.max(0, becauseProgress) * fadeOut,
                    transform: `translateY(${interpolate(Math.max(0, becauseProgress), [0, 1], [30, 0])}px)`,
                  }}
                >
                  Because life's most important connections
                  <br />
                  <span style={{ color: colors.text.primary, fontWeight: 700 }}>
                    deserve the most thought.
                  </span>
                </div>
              );
            })()}
          </div>
        )}

        {/* "Welcome to the OSI of Mind" - Final reveal with white bg and geometric waves */}
        {showWelcome && (
          <>
            {/* Background: dim to bright "birth" effect */}
            <div
              style={{
                position: 'absolute',
                inset: 0,
                background: interpolate(frame - 420, [0, 30, 80], [0, 0.3, 1], {
                  extrapolateLeft: 'clamp',
                  extrapolateRight: 'clamp',
                }) > 0.8 ? '#ffffff' : `rgb(${Math.round(interpolate(frame - 420, [0, 80], [20, 255], {
                  extrapolateLeft: 'clamp',
                  extrapolateRight: 'clamp',
                }))}, ${Math.round(interpolate(frame - 420, [0, 80], [20, 255], {
                  extrapolateLeft: 'clamp',
                  extrapolateRight: 'clamp',
                }))}, ${Math.round(interpolate(frame - 420, [0, 80], [30, 255], {
                  extrapolateLeft: 'clamp',
                  extrapolateRight: 'clamp',
                }))})`,
                opacity: 1,
              }}
            />

            {/* Bright glow burst effect */}
            <div
              style={{
                position: 'absolute',
                top: '50%',
                left: '50%',
                width: interpolate(frame - 420, [0, 60], [0, 2000], {
                  extrapolateLeft: 'clamp',
                  extrapolateRight: 'clamp',
                }),
                height: interpolate(frame - 420, [0, 60], [0, 2000], {
                  extrapolateLeft: 'clamp',
                  extrapolateRight: 'clamp',
                }),
                transform: 'translate(-50%, -50%)',
                background: 'radial-gradient(circle, rgba(255,255,255,1) 0%, rgba(255,255,255,0.8) 30%, transparent 70%)',
                opacity: interpolate(frame - 420, [0, 40, 80], [0, 0.9, 0], {
                  extrapolateLeft: 'clamp',
                  extrapolateRight: 'clamp',
                }),
                pointerEvents: 'none',
              }}
            />

            {/* Complex geometric wave background animation */}
            <GeometricWaveEffect
              intensity={interpolate(frame - 420, [0, 60], [0, 1], {
                extrapolateLeft: 'clamp',
                extrapolateRight: 'clamp',
              })}
            />

            <div
              style={{
                position: 'absolute',
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center',
                gap: 40,
                zIndex: 10,
              }}
            >
              {(() => {
                const welcomeProgress = spring({
                  frame: frame - 420,
                  fps,
                  config: { damping: 20, stiffness: 40 },
                });

                const scale = interpolate(Math.max(0, welcomeProgress), [0, 1], [0.9, 1]);
                const blur = interpolate(Math.max(0, welcomeProgress), [0, 1], [20, 0]);

                // Pulsing glow effect
                const pulseGlow = 20 + Math.sin(frame * 0.08) * 10;

                return (
                  <>
                  <div
                    style={{
                      fontSize: 28,
                      fontWeight: 300,
                      letterSpacing: '0.3em',
                      color: '#64748b',
                      textTransform: 'uppercase',
                      opacity: Math.max(0, welcomeProgress),
                      transform: `translateY(${interpolate(Math.max(0, welcomeProgress), [0, 1], [20, 0])}px)`,
                    }}
                  >
                    Welcome to
                  </div>

                  <div
                    style={{
                      fontSize: 88,
                      fontWeight: 800,
                      letterSpacing: '-0.02em',
                      color: '#000000',
                      opacity: Math.max(0, welcomeProgress),
                      transform: `scale(${scale})`,
                      filter: `blur(${blur}px)`,
                      textAlign: 'center',
                    }}
                  >
                    "The OSI of Mind"
                  </div>

                  {/* ONI tagline - NEURO with gradient */}
                  <div
                    style={{
                      fontSize: 18,
                      fontWeight: 400,
                      letterSpacing: '0.1em',
                      color: '#64748b',
                      opacity: interpolate(frame - 480, [0, 30], [0, 1], {
                        extrapolateLeft: 'clamp',
                        extrapolateRight: 'clamp',
                      }),
                      textAlign: 'center',
                      maxWidth: 700,
                      lineHeight: 1.6,
                    }}
                  >
                    Open{' '}
                    <span
                      style={{
                        background: 'linear-gradient(90deg, #2563eb 0%, #3b82f6 40%, #06b6d4 70%, #8b5cf6 100%)',
                        WebkitBackgroundClip: 'text',
                        WebkitTextFillColor: 'transparent',
                        fontWeight: 600,
                      }}
                    >
                      Neuro
                    </span>
                    security Interoperability
                  </div>

                  {/* Credits footer */}
                  <div
                    style={{
                      position: 'absolute',
                      bottom: -200,
                      display: 'flex',
                      flexDirection: 'column',
                      alignItems: 'center',
                      gap: 12,
                      opacity: interpolate(frame - 500, [0, 30], [0, 0.7], {
                        extrapolateLeft: 'clamp',
                        extrapolateRight: 'clamp',
                      }),
                    }}
                  >
                    <div style={{ fontSize: 14, color: '#64748b' }}>
                      Created by <span style={{ color: '#1e293b', fontWeight: 600 }}>Kevin Qi</span>
                    </div>
                    <div style={{ fontSize: 12, color: '#94a3b8' }}>
                      Built with Claude Code • Apache 2.0 • 2026
                    </div>
                  </div>
                  </>
                );
              })()}
            </div>
          </>
        )}
      </div>

      {/* Corner accents */}
      {[
        { top: 40, left: 40 },
        { top: 40, right: 40 },
        { bottom: 40, left: 40 },
        { bottom: 40, right: 40 },
      ].map((pos, i) => (
        <div
          key={i}
          style={{
            position: 'absolute',
            ...pos,
            width: 60,
            height: 60,
            borderTop: pos.top !== undefined ? `1px solid ${colors.primary.accent}22` : 'none',
            borderBottom: pos.bottom !== undefined ? `1px solid ${colors.primary.accent}22` : 'none',
            borderLeft: pos.left !== undefined ? `1px solid ${colors.primary.accent}22` : 'none',
            borderRight: pos.right !== undefined ? `1px solid ${colors.primary.accent}22` : 'none',
            opacity: interpolate(frame, [0, 60], [0, 0.5], { extrapolateRight: 'clamp' }),
          }}
        />
      ))}
    </AbsoluteFill>
  );
};
