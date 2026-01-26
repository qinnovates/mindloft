/**
 * Layers Scene - 14-layer ONI model visualization
 * Animated pan through all layers with L8 emphasis
 */

import React from 'react';
import { AbsoluteFill, useCurrentFrame, spring, useVideoConfig, interpolate } from 'remotion';
import { colors, typography } from '../data/oni-theme';

// Layer definitions - ordered L1 to L14 for animation
const layers = [
  { id: 'L1', name: 'Physical Carrier', zone: 'silicon', color: colors.silicon.L1, osi: 'Physical' },
  { id: 'L2', name: 'Signal Processing', zone: 'silicon', color: colors.silicon.L2, osi: 'Data Link' },
  { id: 'L3', name: 'Protocol', zone: 'silicon', color: colors.silicon.L3, osi: 'Network' },
  { id: 'L4', name: 'Transport', zone: 'silicon', color: colors.silicon.L4, osi: 'Transport' },
  { id: 'L5', name: 'Session', zone: 'silicon', color: colors.silicon.L5, osi: 'Session' },
  { id: 'L6', name: 'Presentation', zone: 'silicon', color: colors.silicon.L6, osi: 'Presentation' },
  { id: 'L7', name: 'Application Interface', zone: 'silicon', color: colors.silicon.L7, osi: 'Application' },
  { id: 'L8', name: 'Neural Gateway', zone: 'gateway', color: colors.gateway.L8, osi: null },
  { id: 'L9', name: 'Ion Channel Encoding', zone: 'biology', color: colors.biology.L9, osi: null },
  { id: 'L10', name: 'Spike Train', zone: 'biology', color: colors.biology.L10, osi: null },
  { id: 'L11', name: 'Neural Population', zone: 'biology', color: colors.biology.L11, osi: null },
  { id: 'L12', name: 'Circuit Dynamics', zone: 'biology', color: colors.biology.L12, osi: null },
  { id: 'L13', name: 'Cognitive Function', zone: 'biology', color: colors.biology.L13, osi: null },
  { id: 'L14', name: 'Identity & Ethics', zone: 'biology', color: colors.biology.L14, osi: null },
];

export const LayersScene: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Scene duration: 1200 frames (40 seconds at 30fps)
  // Phase 1: 0-150 - Intro text "14 layers spanning silicon to synapse"
  // Phase 2: 150-450 - Show L1-L7 with OSI model labels
  // Phase 3: 450-750 - Zoom into L8 Neural Gateway
  // Phase 4: 750-1050 - Show L9-L14 biology layers
  // Phase 5: 1050-1200 - Full stack view

  const phase1End = 150;
  const phase2End = 450;
  const phase3End = 750;
  const phase4End = 1050;

  // Intro text animation
  const introOpacity = interpolate(frame, [0, 30, 120, phase1End], [0, 1, 1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  // L8 zoom effect during phase 3
  const l8ZoomProgress = interpolate(frame, [phase2End, phase2End + 100, phase3End - 100, phase3End], [1, 1.8, 1.8, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  const l8GlowIntensity = interpolate(frame, [phase2End, phase2End + 50, phase3End - 50, phase3End], [0, 1, 1, 0.3], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  // Current focus layer for highlighting
  const getCurrentLayer = () => {
    if (frame < phase1End) return -1;
    if (frame < phase2End) {
      // Pan through L1-L7
      const layerFrame = frame - phase1End;
      const layerIndex = Math.min(6, Math.floor(layerFrame / 40));
      return layerIndex;
    }
    if (frame < phase3End) return 7; // L8
    if (frame < phase4End) {
      // Pan through L9-L14
      const layerFrame = frame - phase3End;
      const layerIndex = Math.min(13, 8 + Math.floor(layerFrame / 50));
      return layerIndex;
    }
    return -1; // Full view
  };

  const currentLayerIndex = getCurrentLayer();

  // Layer bar dimensions
  const layerHeight = 55;
  const layerWidth = 700;
  const gap = 6;

  // Calculate vertical offset to keep current layer centered
  const totalHeight = layers.length * (layerHeight + gap);
  const getYOffset = () => {
    if (currentLayerIndex < 0) return 0;
    const targetY = currentLayerIndex * (layerHeight + gap) + layerHeight / 2;
    const centerY = totalHeight / 2;
    return centerY - targetY;
  };

  const yOffset = interpolate(
    spring({ frame, fps, config: { damping: 30, stiffness: 50 } }),
    [0, 1],
    [0, getYOffset()]
  );

  return (
    <AbsoluteFill
      style={{
        background: '#000000',
      }}
    >
      {/* Subtle gradient background */}
      <div
        style={{
          position: 'absolute',
          inset: 0,
          background: `radial-gradient(ellipse 80% 60% at 50% 50%,
            rgba(0, 40, 60, 0.3) 0%,
            transparent 70%
          )`,
        }}
      />

      {/* Phase 1: Intro text */}
      {frame < phase1End && (
        <div
          style={{
            position: 'absolute',
            inset: 0,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            justifyContent: 'center',
            opacity: introOpacity,
          }}
        >
          <div
            style={{
              fontSize: 56,
              fontWeight: 600,
              fontFamily: "-apple-system, 'SF Pro Display', sans-serif",
              color: '#ffffff',
              letterSpacing: '-0.02em',
              textAlign: 'center',
            }}
          >
            14 layers spanning
          </div>
          <div
            style={{
              fontSize: 56,
              fontWeight: 600,
              fontFamily: "-apple-system, 'SF Pro Display', sans-serif",
              letterSpacing: '-0.02em',
              marginTop: 10,
              display: 'flex',
              gap: 20,
            }}
          >
            <span style={{ color: colors.silicon.L3 }}>silicon</span>
            <span style={{ color: 'rgba(255,255,255,0.5)' }}>to</span>
            <span style={{ color: colors.biology.L12 }}>synapse</span>
          </div>
        </div>
      )}

      {/* Layer stack */}
      {frame >= phase1End && (
        <div
          style={{
            position: 'absolute',
            inset: 0,
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
          }}
        >
          <div
            style={{
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
              gap,
              transform: `translateY(${yOffset}px)`,
            }}
          >
            {layers.map((layer, index) => {
              const layerNum = index + 1;

              // Staggered reveal
              const revealDelay = phase1End + index * 15;
              const layerOpacity = interpolate(frame, [revealDelay, revealDelay + 30], [0, 1], {
                extrapolateLeft: 'clamp',
                extrapolateRight: 'clamp',
              });

              // Highlight current layer
              const isCurrentLayer = index === currentLayerIndex;
              const isSiliconPhase = frame >= phase1End && frame < phase2End;
              const isGatewayPhase = frame >= phase2End && frame < phase3End;
              const isBiologyPhase = frame >= phase3End && frame < phase4End;

              // Scale effect
              let scale = 1;
              if (isCurrentLayer) {
                scale = layer.zone === 'gateway' ? l8ZoomProgress : 1.08;
              }

              // Glow effect
              let boxShadow = 'none';
              if (isCurrentLayer && layer.zone === 'gateway') {
                boxShadow = `0 0 ${40 * l8GlowIntensity}px ${colors.gateway.L8}, 0 0 ${80 * l8GlowIntensity}px ${colors.gateway.L8}66`;
              } else if (isCurrentLayer) {
                boxShadow = `0 0 25px ${layer.color}88`;
              }

              // Dimming for non-current layers
              const dimAmount = isCurrentLayer ? 1 : 0.4;

              // Zone labels
              const showSiliconLabel = index === 0 && frame >= phase1End;
              const showGatewayLabel = index === 7;
              const showBiologyLabel = index === 8 && frame >= phase3End;

              return (
                <React.Fragment key={layer.id}>
                  {/* Silicon zone label */}
                  {showSiliconLabel && (
                    <div
                      style={{
                        fontSize: 16,
                        fontWeight: 500,
                        fontFamily: "-apple-system, 'SF Pro Display', sans-serif",
                        color: isSiliconPhase ? colors.silicon.L3 : 'rgba(100,150,200,0.6)',
                        letterSpacing: '0.2em',
                        marginBottom: 12,
                        opacity: layerOpacity,
                      }}
                    >
                      SILICON LAYERS (L1-L7) — CLASSICAL OSI MODEL
                    </div>
                  )}

                  {/* Gateway zone label */}
                  {showGatewayLabel && (
                    <div
                      style={{
                        fontSize: 18,
                        fontWeight: 600,
                        fontFamily: "-apple-system, 'SF Pro Display', sans-serif",
                        color: isGatewayPhase ? colors.gateway.L8 : 'rgba(255,150,0,0.6)',
                        letterSpacing: '0.15em',
                        margin: '20px 0 12px',
                        opacity: layerOpacity,
                        textShadow: isGatewayPhase ? `0 0 20px ${colors.gateway.L8}` : 'none',
                      }}
                    >
                      ★ NEURAL GATEWAY — THE BRIDGE ★
                    </div>
                  )}

                  {/* Biology zone label */}
                  {showBiologyLabel && (
                    <div
                      style={{
                        fontSize: 16,
                        fontWeight: 500,
                        fontFamily: "-apple-system, 'SF Pro Display', sans-serif",
                        color: isBiologyPhase ? colors.biology.L11 : 'rgba(100,200,100,0.6)',
                        letterSpacing: '0.2em',
                        margin: '20px 0 12px',
                        opacity: layerOpacity,
                      }}
                    >
                      BIOLOGY LAYERS (L9-L14) — NEURAL PROCESSING
                    </div>
                  )}

                  {/* Layer bar */}
                  <div
                    style={{
                      width: layerWidth,
                      height: layerHeight,
                      backgroundColor: layer.color,
                      borderRadius: 10,
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'space-between',
                      padding: '0 24px',
                      opacity: layerOpacity * dimAmount,
                      transform: `scale(${scale})`,
                      boxShadow,
                      transition: 'transform 0.3s ease, opacity 0.3s ease',
                    }}
                  >
                    <div style={{ display: 'flex', alignItems: 'center', gap: 16 }}>
                      <span
                        style={{
                          color: '#ffffff',
                          fontSize: 22,
                          fontWeight: 700,
                          fontFamily: "-apple-system, 'SF Pro Display', sans-serif",
                        }}
                      >
                        {layer.id}
                      </span>
                      <span
                        style={{
                          color: 'rgba(255,255,255,0.9)',
                          fontSize: 18,
                          fontWeight: 500,
                          fontFamily: "-apple-system, 'SF Pro Text', sans-serif",
                        }}
                      >
                        {layer.name}
                      </span>
                    </div>
                    {layer.osi && isSiliconPhase && (
                      <span
                        style={{
                          color: 'rgba(255,255,255,0.6)',
                          fontSize: 14,
                          fontWeight: 400,
                          fontFamily: "-apple-system, 'SF Pro Text', sans-serif",
                          fontStyle: 'italic',
                        }}
                      >
                        OSI: {layer.osi}
                      </span>
                    )}
                  </div>
                </React.Fragment>
              );
            })}
          </div>
        </div>
      )}

      {/* Phase 3: L8 emphasis text */}
      {frame >= phase2End && frame < phase3End && (
        <div
          style={{
            position: 'absolute',
            bottom: 100,
            left: 0,
            right: 0,
            display: 'flex',
            justifyContent: 'center',
            opacity: interpolate(frame, [phase2End + 50, phase2End + 100, phase3End - 50, phase3End], [0, 1, 1, 0]),
          }}
        >
          <div
            style={{
              fontSize: 28,
              fontWeight: 400,
              fontFamily: "-apple-system, 'SF Pro Display', sans-serif",
              color: colors.gateway.L8,
              letterSpacing: '0.1em',
              textAlign: 'center',
              textShadow: `0 0 30px ${colors.gateway.L8}`,
            }}
          >
            The critical bridge between machine and mind
          </div>
        </div>
      )}

      {/* Subtle vignette */}
      <div
        style={{
          position: 'absolute',
          inset: 0,
          boxShadow: 'inset 0 0 200px rgba(0,0,0,0.5)',
          pointerEvents: 'none',
        }}
      />
    </AbsoluteFill>
  );
};
