"""
GLSL Shader Definitions for Neural Visualization
WebGL/OpenGL ES 3.0 compatible shaders
"""

# =============================================================================
# MOLECULAR SCALE: Ion Probability Densities
# =============================================================================

VERTEX_SHADER_MOLECULE = """
#version 300 es
precision highp float;

// Attributes
layout(location = 0) in vec3 a_position;
layout(location = 1) in float a_charge;
layout(location = 2) in float a_probability;

// Uniforms
uniform mat4 u_modelViewProjection;
uniform mat4 u_modelView;
uniform float u_time;
uniform float u_scale;

// Varying
out vec3 v_position;
out float v_charge;
out float v_probability;
out vec3 v_normal;

void main() {
    // Brownian motion perturbation
    vec3 noise = vec3(
        sin(a_position.x * 100.0 + u_time * 2.0),
        cos(a_position.y * 100.0 + u_time * 1.7),
        sin(a_position.z * 100.0 + u_time * 2.3)
    ) * 0.001 * u_scale;

    vec3 pos = a_position + noise;

    gl_Position = u_modelViewProjection * vec4(pos, 1.0);
    gl_PointSize = mix(2.0, 10.0, a_probability) * u_scale;

    v_position = (u_modelView * vec4(pos, 1.0)).xyz;
    v_charge = a_charge;
    v_probability = a_probability;
    v_normal = normalize(pos);
}
"""

FRAGMENT_SHADER_ION_CLOUD = """
#version 300 es
precision highp float;

in vec3 v_position;
in float v_charge;
in float v_probability;

uniform float u_opacity;
uniform sampler2D u_colormap;

out vec4 fragColor;

void main() {
    // Circular point sprite
    vec2 coord = gl_PointCoord - vec2(0.5);
    float dist = length(coord);
    if (dist > 0.5) discard;

    // Charge-based coloring
    // Na+ = warm, K+ = cool, Ca2+ = bright, Cl- = muted
    float normalizedCharge = (v_charge + 2.0) / 4.0; // Map [-2, +2] to [0, 1]
    vec3 color = texture(u_colormap, vec2(normalizedCharge, 0.5)).rgb;

    // Probability density affects opacity
    float alpha = v_probability * (1.0 - dist * 2.0) * u_opacity;

    // Glow effect for high probability regions
    if (v_probability > 0.8) {
        color += vec3(0.3, 0.3, 0.5) * (v_probability - 0.8) * 5.0;
    }

    fragColor = vec4(color, alpha);
}
"""

# =============================================================================
# CELLULAR SCALE: Neuron Morphology with Voltage Mapping
# =============================================================================

VERTEX_SHADER_NEURON = """
#version 300 es
precision highp float;

layout(location = 0) in vec3 a_position;
layout(location = 1) in vec3 a_normal;
layout(location = 2) in float a_voltage;
layout(location = 3) in float a_radius;
layout(location = 4) in int a_compartmentType; // 0=soma, 1=axon, 2=dendrite

uniform mat4 u_modelViewProjection;
uniform mat4 u_modelView;
uniform mat3 u_normalMatrix;
uniform float u_time;

out vec3 v_worldPos;
out vec3 v_normal;
out float v_voltage;
flat out int v_compartmentType;

void main() {
    // Slight pulsing for active regions
    float pulse = 1.0 + 0.02 * sin(u_time * 10.0) * step(0.0, a_voltage + 40.0);
    vec3 pos = a_position * pulse;

    gl_Position = u_modelViewProjection * vec4(pos, 1.0);
    v_worldPos = (u_modelView * vec4(pos, 1.0)).xyz;
    v_normal = normalize(u_normalMatrix * a_normal);
    v_voltage = a_voltage;
    v_compartmentType = a_compartmentType;
}
"""

FRAGMENT_SHADER_MEMBRANE_POTENTIAL = """
#version 300 es
precision highp float;

in vec3 v_worldPos;
in vec3 v_normal;
in float v_voltage;
flat in int v_compartmentType;

uniform vec3 u_lightDir;
uniform vec3 u_viewDir;
uniform float u_voltageMin; // -90 mV
uniform float u_voltageMax; // +50 mV

out vec4 fragColor;

// Plasma-like colormap for membrane potential
vec3 voltageToColor(float v) {
    float t = clamp((v - u_voltageMin) / (u_voltageMax - u_voltageMin), 0.0, 1.0);

    // Deep blue (rest) -> cyan -> green -> yellow -> red (depolarized)
    vec3 c0 = vec3(0.05, 0.05, 0.3);  // -90 mV: dark blue
    vec3 c1 = vec3(0.0, 0.3, 0.6);    // -70 mV: blue
    vec3 c2 = vec3(0.0, 0.6, 0.4);    // -50 mV: teal
    vec3 c3 = vec3(0.4, 0.8, 0.2);    // -30 mV: green
    vec3 c4 = vec3(0.9, 0.7, 0.0);    // 0 mV: yellow
    vec3 c5 = vec3(1.0, 0.3, 0.0);    // +30 mV: orange
    vec3 c6 = vec3(1.0, 0.0, 0.3);    // +50 mV: magenta (action potential)

    if (t < 0.167) return mix(c0, c1, t / 0.167);
    if (t < 0.333) return mix(c1, c2, (t - 0.167) / 0.167);
    if (t < 0.5)   return mix(c2, c3, (t - 0.333) / 0.167);
    if (t < 0.667) return mix(c3, c4, (t - 0.5) / 0.167);
    if (t < 0.833) return mix(c4, c5, (t - 0.667) / 0.167);
    return mix(c5, c6, (t - 0.833) / 0.167);
}

void main() {
    vec3 baseColor = voltageToColor(v_voltage);

    // Add glow for action potentials
    float spikeFactor = smoothstep(-30.0, 0.0, v_voltage);
    vec3 glowColor = vec3(1.0, 0.8, 0.4) * spikeFactor * 0.5;

    // Phong shading
    vec3 N = normalize(v_normal);
    vec3 L = normalize(u_lightDir);
    vec3 V = normalize(u_viewDir - v_worldPos);
    vec3 R = reflect(-L, N);

    float ambient = 0.3;
    float diffuse = max(dot(N, L), 0.0) * 0.5;
    float specular = pow(max(dot(R, V), 0.0), 32.0) * 0.3;

    vec3 finalColor = baseColor * (ambient + diffuse) + vec3(specular) + glowColor;

    // Compartment-specific adjustments
    if (v_compartmentType == 1) { // Axon: slightly more translucent
        fragColor = vec4(finalColor, 0.85);
    } else if (v_compartmentType == 2) { // Dendrite: spines visible
        fragColor = vec4(finalColor, 0.9);
    } else { // Soma
        fragColor = vec4(finalColor, 1.0);
    }
}
"""

# =============================================================================
# NETWORK SCALE: Fiber Tracts and Connectivity
# =============================================================================

VERTEX_SHADER_STREAMLINES = """
#version 300 es
precision highp float;

layout(location = 0) in vec3 a_position;
layout(location = 1) in float a_strength;
layout(location = 2) in float a_parameterT;

uniform mat4 u_modelViewProjection;
uniform float u_time;

out float v_strength;
out float v_parameterT;

void main() {
    gl_Position = u_modelViewProjection * vec4(a_position, 1.0);
    v_strength = a_strength;
    v_parameterT = a_parameterT;
}
"""

FRAGMENT_SHADER_FIBER_TRACT = """
#version 300 es
precision highp float;

in float v_strength;
in float v_parameterT;

uniform float u_time;
uniform float u_minStrength;
uniform float u_maxStrength;

out vec4 fragColor;

void main() {
    float normalizedStrength = (v_strength - u_minStrength) / (u_maxStrength - u_minStrength);

    // Color by connection strength: weak=thin/transparent, strong=thick/bright
    vec3 color = mix(
        vec3(0.2, 0.3, 0.5),  // Weak: blue-gray
        vec3(1.0, 0.9, 0.3),   // Strong: golden
        normalizedStrength
    );

    // Animated flow along tract
    float flow = fract(v_parameterT - u_time * 0.1);
    float pulse = smoothstep(0.0, 0.1, flow) * smoothstep(0.3, 0.2, flow);
    color += vec3(0.3) * pulse * normalizedStrength;

    float alpha = mix(0.2, 0.9, normalizedStrength);

    fragColor = vec4(color, alpha);
}
"""

# =============================================================================
# FIELD VISUALIZATION: Electric Field Lines
# =============================================================================

VERTEX_SHADER_FIELD_LINES = """
#version 300 es
precision highp float;

layout(location = 0) in vec3 a_position;
layout(location = 1) in vec3 a_direction;
layout(location = 2) in float a_magnitude;

uniform mat4 u_modelViewProjection;
uniform float u_time;
uniform float u_maxMagnitude;

out vec3 v_direction;
out float v_magnitude;

void main() {
    // Animate field line segments
    vec3 offset = a_direction * sin(u_time * 3.0) * 0.01;
    vec3 pos = a_position + offset;

    gl_Position = u_modelViewProjection * vec4(pos, 1.0);
    v_direction = a_direction;
    v_magnitude = a_magnitude / u_maxMagnitude;
}
"""

FRAGMENT_SHADER_FIELD_LINES = """
#version 300 es
precision highp float;

in vec3 v_direction;
in float v_magnitude;

out vec4 fragColor;

void main() {
    // Color by field direction and magnitude
    vec3 color = normalize(abs(v_direction));
    color = mix(vec3(0.1), color, v_magnitude);

    // Intensity based on magnitude
    float alpha = 0.3 + 0.7 * v_magnitude;

    fragColor = vec4(color, alpha);
}
"""

# =============================================================================
# CALCIUM WAVE VISUALIZATION
# =============================================================================

VERTEX_SHADER_CALCIUM_WAVE = """
#version 300 es
precision highp float;

layout(location = 0) in vec3 a_position;
layout(location = 1) in float a_concentration;

uniform mat4 u_modelViewProjection;
uniform float u_time;
uniform float u_waveSpeed;

out float v_concentration;
out vec3 v_position;

void main() {
    // Wave propagation effect
    float wave = sin(length(a_position) * 10.0 - u_time * u_waveSpeed);
    float height = a_concentration * (1.0 + 0.1 * wave);

    vec3 pos = a_position;
    pos.y += height * 0.1;

    gl_Position = u_modelViewProjection * vec4(pos, 1.0);
    gl_PointSize = 3.0 + 7.0 * a_concentration;

    v_concentration = a_concentration;
    v_position = pos;
}
"""

FRAGMENT_SHADER_CALCIUM_WAVE = """
#version 300 es
precision highp float;

in float v_concentration;
in vec3 v_position;

out vec4 fragColor;

void main() {
    // Point sprite circle
    vec2 coord = gl_PointCoord - vec2(0.5);
    float dist = length(coord);
    if (dist > 0.5) discard;

    // Calcium: green to yellow color scheme
    vec3 lowCa = vec3(0.0, 0.2, 0.0);   // Dark green (low)
    vec3 highCa = vec3(1.0, 1.0, 0.0);  // Yellow (high)
    vec3 color = mix(lowCa, highCa, v_concentration);

    // Glow
    float glow = 1.0 - dist * 2.0;
    color += vec3(0.2, 0.3, 0.0) * glow * v_concentration;

    float alpha = (1.0 - dist * 2.0) * (0.5 + 0.5 * v_concentration);

    fragColor = vec4(color, alpha);
}
"""
